from __future__ import unicode_literals, print_function
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.language import Language
import re
from spacy.symbols import LEMMA


def RelationMatcherCreator(nlp, terms, label):
    #function adds relationMatcher to the pipeline
    pipe = "RelationMatcher"+label
    Language.factories[pipe] = lambda nlp: RelationMatcher(nlp, terms,label)
    nlp.add_pipe(nlp.create_pipe(pipe), after="ner")
class RelationMatcher(object):
    def __init__(self, nlp, terms, label):
        self.matcher = Matcher(nlp.vocab)
        #Example: (treat) will still match the word treatment in a text
        for term in terms: #adds the regex pattern that checks to see if a word contains the terms given
            regex = ".*" + term + ".*"
            relation_flag = lambda text: bool(re.compile(r"" + regex).match(text)) #Function that verifies the property of the token
            IS_RELATION = nlp.vocab.add_flag(relation_flag)
            self.matcher.add('DEFINITELY', None, [{IS_RELATION: True}]) #Matcher checks words for the boolean value of the given property
        print("t", terms)
        self.name = "RM_"+ label
        self.label = label
    def __call__(self, doc):
        relations = []
        for match_id, start, end in self.matcher(doc):
            match = doc[start:end]
            for tok in match:
                tok.ent_type_ = self.label
            relations.append(tok)
            span = Span(doc, start, end, label=match_id)
            if span not in doc.ents:
                doc.ents = list(doc.ents) + [span]
        doc.user_data[self.label] = relations
        print("tokens")
        return doc
