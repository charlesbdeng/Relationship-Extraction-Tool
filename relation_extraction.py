from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.language import Language
from collections import Counter
from load import load_doc, load_whitelist, encode
from send import sent_ents
from e_e import EM_Creator
from ta import TA_Creator

import json
# presidents_ = load_whitelist("data/presidents.txt")
# countries_ = load_whitelist("data/countries.txt")
# train = load_doc("data/history.txt")



# load json object list, not from a text file so simply use the given Object
# load doc, doc is given as a string so no need to load_doc, as the doc argu is a file location
# need to add encoding for both lists
# be aware of argument locations



def relex(label1, label2, entities1,entities2, text, scope):
    nlp = spacy.load("en_core_web_sm")
    entities1_ = load_whitelist(entities1)
    entities2_ = load_whitelist(entities2)
    text_ = load_doc(text)
    EM_Creator(nlp,entities1_, label1)
    EM_Creator(nlp,entities2_, label2)
    TA_Creator(nlp, entities1_,label1)
    TA_Creator(nlp, entities2_, label2)
    doc = nlp(text_)
    # print("list of json entities",sent_ents(doc,label1,label2))
    return sent_ents(doc,label1,label2)

# print(relex("PRESIDENTS", "COUNTRIES", presidents_, countries_, train, 1  ))
