from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.language import Language

def ent_relation(ent,label):

    if ent == ent.head:
        if ent.pos_ == 'NOUN':
            return ent
        else:
            ent_true ={
                "PRON": True,
                "NOUN":True,
                "VERB": False,
                "ADV": False,
            }
            
            return [ents for ents in ent.subtree if ents.ent_type_ != label and ents.pos_ in ["PRON", "NOUN"]][0]
    else:
        return ent_relation(ent.head, label)
