from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.language import Language
from collections import Counter
from load import load_doc, load_whitelist, encode




class DataStore(object):

    name = "data store";


    def __init__(self, nlp, terms):
        patterns = [nlp(text) for text in terms]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(label, None, *patterns)





    def __call__(self, doc):
        matches = self.matcher(doc)
        entities = []
        for match_id, start, end in matches:
            phrase = doc[start:end]
            entity = []
            for index,tok in phrase:
                # print("entity:", tok)
                # print("POS:", tok.pos_)
                entities.append(tok)
        doc.user_data = doc.user_data + entities if type(doc.user_data) == "list" else entities
        return doc










##data storage pipeline that extracts token statements
