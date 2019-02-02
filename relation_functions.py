from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.language import Language

def extract_entity(ent,label):
###loops through the entities's head to find words that are associated with a relation and an entity
    if ent == ent.head:
        #if an entity is found return it
        if ent.pos_ == 'NOUN':
            return ent
        else:
        #if a relation is returned, iterate through its children to find entities related to it 
            ent_true ={
                "PRON": True,
                "NOUN":True,
                "VERB": False,
                "ADV": False,
            }

            return [ents for ents in ent.subtree if ents.ent_type_ != label and ents.pos_ in ["PRON", "NOUN"]][0]
    else:
        return ent_relation(ent.head, label)
