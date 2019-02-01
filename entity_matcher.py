from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher, Matcher
from spacy.tokens import Span
from spacy.language import Language
from connectors import load_doc, load_whitelist, encode
from spacy.symbols import ORTH, LEMMA, POS, TAG


def EntityMatcherCreator(nlp, terms, label):
    pipe = "EntityMatcher_"+label
    Language.factories[pipe] = lambda nlp: EntityMatcher(nlp, terms,label)
    nlp.add_pipe(nlp.create_pipe(pipe), after="ner")

class EntityMatcher(object):
    name = "entity_matcher"
    def __init__(self, nlp, terms, label):
        lemmatized = map(lambda x: " ".join([tok.lemma_ for tok in nlp(x)]), terms)
        lemmatized = [[{LEMMA: lemma}] for lemma in lemmatized]
        phrases = [nlp(term) for term in terms]
        print("t", terms)
        self.name = "EM_"+ label
        self.l_matcher = Matcher(nlp.vocab)
        self.p_matcher = PhraseMatcher(nlp.vocab)
        self.l_matcher.add(label, None, *lemmatized)
        self.p_matcher.add(label, None, *phrases)
        self.label = label
    def take_first(self,elem):
        return elem[1]
    def __call__(self, doc):
        print("l",  self.label)
        l_matches = self.l_matcher(doc)
        p_matches = self.p_matcher(doc)
        matches = list(set(l_matches + p_matches))
        print('matches', matches)
        matches.sort(key=self.take_first)
        final_matches = []
        if len(matches) > 1:
            for index, match in enumerate(matches):
                head = match
                previous = matches[index - 1]
                head_start = head[1]
                head_end = head[2]
                prev_start = previous[1]
                prev_end = previous[2]
                if head_start >= prev_end or index==0:
                    final_matches.append(match)
        else:
            final_matches = matches
        entities = []
        for match_id, start, end in final_matches:
            phrase = doc[start:end]
            compound = len(phrase) > 1
            if compound:
                literal = ""
            for index,tok in enumerate(phrase):
                entity = dict()
                type = self.label.lower()
                if compound:
                    literal = doc[start:end].text
                    if index == len(phrase)-1:
                        tok._.text = literal
                        tok.ent_type_ = self.label
                        entities.append(tok)
                else:
                    tok.ent_type_ = self.label
                    entities.append(tok)
            span = Span(doc, start, end, label=match_id)

            if span not in doc.ents:
                doc.ents = list(doc.ents) + [span]
        doc.user_data[self.label] = entities
        return doc
