from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.language import Language
from collections import Counter
from load import load_doc, load_whitelist, encode
from send import index1,index2,index3
from e_e import EM_Creator
from r_e import RM_Creator
from ta import TA_Creator

import json
# presidents_ = load_whitelist("data/presidents.txt")
# countries_ = load_whitelist("data/countries.txt")
# train = load_doc("data/history.txt")



# load json object list, not from a text file so simply use the given Object
# load doc, doc is given as a string so no need to load_doc, as the doc argu is a file location
# need to add encoding for both lists
# be aware of argument locations



def entity_entity(label1, label2, entities1,entities2, text, scope):
    nlp = spacy.load("en_core_web_sm")
    entities1_ = load_whitelist(entities1)
    entities2_ = load_whitelist(entities2)
    text_ = load_doc(text)
    EM_Creator(nlp,entities1_, label1)
    EM_Creator(nlp,entities2_, label2)
    # TA_Creator(nlp, entities1_,label1)
    # TA_Creator(nlp, entities2_, label2)
    doc = nlp(text_)
    # print("list of json entities",sent_ents(doc,label1,label2))
    return index1(doc,label1,label2, scope)

def relation_entity(label, relation, entities,relations, text, scope):
    nlp = spacy.load("en_core_web_sm")
    entities_ = load_whitelist(entities)
    relations_ = load_whitelist(relations)
    text_ = load_doc(text)
    EM_Creator(nlp,entities_, label)
    RM_Creator(nlp,relations_, relation)
    # TA_Creator(nlp, entities1_,label1)
    # TA_Creator(nlp, entities2_, label2)
    doc = nlp(text_)
    # print("list of json entities",sent_ents(doc,label1,label2))
    return index2(doc,label,relation, scope)
def all_ent_rel(label1, label2, rel_label, entities1,entities2, relations, text, scope):
    nlp = spacy.load("en_core_web_sm")
    entities1_ = load_whitelist(entities1)
    entities2_ = load_whitelist(entities2)
    relations_ = load_whitelist(relations)

    text_ = load_doc(text)
    EM_Creator(nlp,entities1_, label1)
    EM_Creator(nlp,entities2_, label2)
    RM_Creator(nlp, relations_, rel_label)
    # TA_Creator(nlp, entities1_,label1)
    # TA_Creator(nlp, entities2_, label2)
    doc = nlp(text_)
    # print("list of json entities",sent_ents(doc,label1,label2))
    return index3(doc,label1,label2, rel_label,scope)

# print(relex("PRESIDENTS", "COUNTRIES", presidents_, countries_, train, 1  ))
