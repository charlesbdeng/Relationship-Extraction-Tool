from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher, Matcher
from spacy.tokens import Span
from spacy.language import Language
from connectors import load_doc, load_whitelist, encode
from spacy.symbols import ORTH, LEMMA, POS, TAG


def EntityMatcherCreator(nlp, terms, label): #Adds the entity matcher to the pipeline
    #
    pipe = "EntityMatcher_"+label
    Language.factories[pipe] = lambda nlp: EntityMatcher(nlp, terms,label) #adds into the "factory" of available pipelines
    nlp.add_pipe(nlp.create_pipe(pipe), after="ner") #searches the factory for a specific pipeline and adds to the pipeline
class EntityMatcher(object):
    name = "entity_matcher"
    def __init__(self, nlp, terms, label):
        #lemmatizes all the terms before uploading them as patterns for the matcher to detect
        lemmatized = map(lambda x: " ".join([tok.lemma_ for tok in nlp(x)]), terms)
        lemmatized = [[{LEMMA: lemma}] for lemma in lemmatized]
        #by using the lemma object the matcher compares with the lemmatized version of the word in the text
        phrases = [nlp(term) for term in terms]
        self.name = "EM_"+ label
        #Phrase matcher matches with any word regardless of its cardinality
        #Matcher matches based on the pattern assigned to it
        #Matcher allows for specific pattern matching - lowercase, lemma, alpha, etc
        self.l_matcher = Matcher(nlp.vocab)
        self.p_matcher = PhraseMatcher(nlp.vocab)
        self.l_matcher.add(label, None, *lemmatized)
        self.p_matcher.add(label, None, *phrases)
        self.label = label
    def take_first(self,elem):
        return elem[1]
    def __call__(self, doc):
        #function searches for all instances of the pattern and stores the information in doc container
        l_matches = self.l_matcher(doc)
        p_matches = self.p_matcher(doc)
        #gives a list of tuples with the start and end points of each word matched
        matches = list(set(l_matches + p_matches))
        #takes out duplicate matches that arise from conflicts between Phrase Matcher and Matcher
        matches.sort(key=self.take_first)
        final_matches = []
        #final matches should not have any duplicates
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
        #loops through list and adds the matched words as tokens to user_data in doc container
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
                        #changes the last word of a compound word to its full name
                        tok.ent_type_ = self.label
                        entities.append(tok)
                else:
                    tok.ent_type_ = self.label
                    entities.append(tok)
            span = Span(doc, start, end, label=match_id)
            if span not in doc.ents:
                doc.ents = list(doc.ents) + [span]
        #each set of terms is given its own key in user_data to access all entities associated with its label
        doc.user_data[self.label] = entities
        return doc
