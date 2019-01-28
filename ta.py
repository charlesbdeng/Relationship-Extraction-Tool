from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.language import Language
from collections import Counter
from s_e import sent_ent
from e_e import EM_Creator
from load import load_doc, load_whitelist, encode

import plac


def  TA_Creator(nlp, terms, label):
    pipe = "TA_Creator_" + label
    Language.factories[pipe] = lambda nlp: TypeAssigner(nlp, terms,label)
    nlp.add_pipe(nlp.create_pipe(pipe), before ="EM_"+label)


class TypeAssigner(object):

    def __init__(self, nlp, terms, label):
        patterns = [nlp.make_doc(text) for text in terms]
        # print("patterns: ", patterns)
        self.terms = terms
        self.name = "TA_" + label
        # print(self.name)
        self.label = label
        # print("nlp.vocab: ", str(nlp.vocab[u'435'].text))
        # print(type(nlp.vocab[u'cat'].text))

    def __call__(self, doc):
        for token in doc:

            if token.text in self.terms :

                token.ent_type_ = self.label

        return doc
# drugs_ = load_whitelist('data/drugs.txt')
# effects_ = load_whitelist('data/effects.txt')
# nlp = spacy.load('en_core_web_sm')
# TA_Creator(nlp, drugs_, "DRUGS")
# TA_Creator(nlp, effects_, "EFFECTS")
# EM_Creator(nlp,drugs_,"DRUGS")
# EM_Creator(nlp, effects_, "EFFECTS")

# doc = nlp('Net income was $9.4 million compared to the prior year of $2.7 million. The acetylsalicylic acid cured the headache.')


# doc = nlp(encode(load_doc('data/med.txt')))
# print(doc.ents)
def sentence_parser(doc):
    return [(index, sent.text) for index, sent in enumerate(doc.sents)]
def entity_density(doc, label):
    return Counter([ent.text for ent in doc.ents if ent.label_ == label ])
    #if text counts names, if label, counts type of drug, if regular, spits out 1 of everything
# print(sentence_parser(doc))
# print(type(sentence_parser(doc)[0][0]))
# def sent_ent(doc,label1, label2):
#     sents = []
#     ents1 = [s.text for s in doc.ents if s.label_ == label1]
#     ents2 = [s.text for s in doc.ents if s.label_ == label2]
#
#     for index, sent in enumerate(doc.sents):
#         record = {}
#         entities1 = []
#         entities2= []
# ##later can code for any entities by look up the list, now just stick with the label
#         sentence = sent.text.split()
#         for word in sentence:
#             print(word)
#             if word in ents1:
#                 entities1.append(word)
#             if word in ents2:
#                 entities2.append(word)
#         if len(entities1) > 0 or len(entities2) > 0:
#             record["entities1"] = entities1
#             record["entities2"] = entities2
#             record["sentence"] = sent.text #unicode possibly imcompatible
#             record["index"] = index
#             sents.append(record)
#     return sents

# print(sent_ent(doc,"DRUGS","EFFECTS")[0:10])

# print("obj:", sent_ent(doc,"DRUGS"))







# print(entity_density(doc, "DRUGS"))
# print([type(t.text) for t in doc if t.ent_type_ == "DRUGS"])
#check if all relevant types have been modified
