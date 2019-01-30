from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.language import Language
from collections import Counter
from load import load_doc, load_whitelist, encode
from send import index1,index2,index3
import re
from spacy.symbols import ORTH, LEMMA, POS, TAG


def RM_Creator(nlp, terms, label):
    # terms_ = encode(terms)
    pipe = "RelationMatcher"+label
    Language.factories[pipe] = lambda nlp: RelationMatcher(nlp, terms,label)
    nlp.add_pipe(nlp.create_pipe(pipe), after="ner")


class RelationMatcher(object):

    def __init__(self, nlp, terms, label):
        # print('terms', terms)
        self.matcher = Matcher(nlp.vocab)
        for term in terms:
            regex = ".*" + term + ".*"
            relation_flag = lambda text: bool(re.compile(r"" + regex).match(text))
            IS_RELATION = nlp.vocab.add_flag(relation_flag)
            self.matcher.add('DEFINITELY', None, [{IS_RELATION: True}])
        # print("lemmatized",lemmatized)
        # for alt in patterns:
        #     print(alt)
        #     print(type(alt))
        #     print(type(alt[0]))
        #     print("pos:", alt[0].ent_type_)
        # #//insert a getter function that can return the necessary information
        # # print("patterns: ", patterns)
        # print("name", self.name)
        print("t", terms)
        self.name = "RM_"+ label
        # print(self.name)
        # print("nlp.vocab: ", str(nlp.vocab[u"435"].text))
        # print(type(nlp.vocab[u"cat"].text))
        ##transform into docs
        self.label = label
        ##searched for lemmatizatioon

    def __call__(self, doc):
        relations = []
        for match_id, start, end in self.matcher(doc):

            # print("Hit")

            match = doc[start:end]
            relation = {}
            for tok in match:
                relation["name"] = tok.text
                relation["index"] = tok.i
                tok.ent_type_ = self.label
                relation["pos"] = tok.pos_
                relation["length"] = len(relation["name"])
                relation["sentence"] = tok.sent
                relation["type"] = tok.ent_type_
                relation["token"] = tok
                relation["length"] = len(relation["name"])
                relation["dep"] = tok.dep_
                relation["ancestors"] = [anc for anc in tok.ancestors]
                relation["children"] = tok.children
                relation["head"] = tok.head
            relations.append(relation)

            span = Span(doc, start, end, label=match_id)
            print("SPAN",span.text)
            # print(list(doc.ents))
            #ValueError: [E098] Trying to set conflicting doc.ents: '(150, 153, u'GPE')' and '(151, 153, u'COUNTRIES')'. A token can only be part of one relation, so make sure the entities you're setting don't overlap.
            print("doc ents every iteration throug matches:",  doc.ents)
            if span not in doc.ents:
                doc.ents = list(doc.ents) + [span]
        # print(self.name)
        # print(type(doc.user_data))
        # print("type", type(doc.user_data))
        # print(entities)


        doc.user_data[self.label] = relations
        # print(entities)
        # print(doc.user_data)
        # print("hit3")
        # print("user data", doc.user_data)
        # print(doc.ents)
        print("tokens")
        return doc




# drugs_ = ["aspirin", "acetylsalicylic acid", "tylenol", "analgesic","fever-reducing agent", "antipyretic drug", "inhibitor", "side effects"]
# drugs = encode(drugs_)

# effects = encode(effects_)

# encode strings
# print("encoded: ", encode)

# # drugs_ = load_whitelist("data/drugs.txt")
# # effects_ = load_whitelist("data/effects.txt")
# nlp = spacy.load("en_core_web_sm")
# #
# presidents_ = load_whitelist("data/presidents.txt")
# countries_ = load_whitelist("data/countries.txt")
# # EM_Creator(nlp,drugs_,"DRUGS")
# # EM_Creator(nlp, effects_, "EFFECTS")
# EM_Creator(nlp, presidents_, "PRESIDENTS")
# EM_Creator(nlp, countries_, "COUNTRIES")

# doc = nlp(u"This is a text about Barack Obama and a tree kangaroo")
# print([ents for ents in doc.ents])

# list_ = [False, False, False, False, False, False, False]
# print (any(list_))
# drugs_ = load_whitelist("data/drugs.txt")
# effects_ = load_whitelist("data/effects.txt")
# nlp = spacy.load("en_core_web_sm")
# EM_Creator(nlp,drugs_,"DRUGS")
# doc = nlp("Net income was $9.4 million compared to the prior year of $2.7 million.")
# doc = nlp(load_doc("data/med.txt"))
# doc = nlp(load_doc("data/history.txt"))
# # doc = nlp('Emmanuel Macron is a Macron. Macron was a great man. Emmanuel Macron was very interesting.')
# print(sent_ents(doc, "PRESIDENTS", "COUNTRIES"))

# def sent_ents(doc,label1, label2):
#     sent_index = {}
#     lower_label1 = str(label1.lower())
#     lower_label2 = str(label2.lower())
#     print("This hit")
#     print("lowerLabel: ", lower_label1)
#
#     for index,sent in enumerate(doc.sents):
#         sent_index[sent] = index
#
#
#     entities = []
#     for ent2 in doc.user_data[label2]:
#
#
#         for ent1 in doc.user_data[label1]:
#             obj = dict()
#             if ent1["sentence"] == ent2["sentence"]:
#                 entities = []
#                 entities.append(lower_label1)
#                 entities.append(lower_label2)
#
#                 # print(ent1["name"], ent2["name"])
#                 # print("sentence:", ent1["sentence"])
#                 # print("index", ent1["sentence"].text.index(ent1["name"]))
#                 # print("length", len(ent1["sentence"]))
#                 obj[str("entities")] = entities
#                 print(obj[entities])
#                 obj[lower_label1] = {str("value"): ent1["name"],
#                                 str("position"):  ent1["sentence"].text.index(ent1["name"]),
#                                 str("length"): len(ent1["name"]),
#                                 str("type"): lower_label1
#                                 }
#                 # obj[lower_label2] =  {str("value"): ent2["name"],
#                                 str("position"):  ent2["sentence"].text.index(ent2["name"]),
#                                 str("length"): len(ent2["name"]),
#                                 str("index"): ent2["index"],
#                                 str("type"):lower_label2
#                                 }
#                 sentence = ent1[str("sentence")]
#                 obj[str("sentence")] = {str("text"): str(sentence), str("index"): sent_index[sentence]}
#
#                 obj[str("relation")] = {str("text"): [str(anc) for anc in ent2["ancestors"]]}
#
#                 entities.append(obj)
#     print(json.dumps(entities[0:3]))









# print(sent_ents(doc,"DRUGS", "EFFECTS"))
# doc = nlp("The clients used acetylsalicylic acid on a daily basis.")
# print("user_data:", doc.user_data)

# for ent in doc.ents:
#     print("text_ent:",ent.text)
#
#
#
# for key,entities in doc.user_data.items():
#     for ent in entities:
#         if len(ent["name"]) > 1:
#             print("label:", ent["name"])
#             print("pos:", ent["pos"])
#             print("ent_type", ent["type"])
#             print("elem_type:", type(ent))
#             print("tok:", ent["token"])
# pos: 91
# ent_type DRUGS
# elem_type: <type "spacy.tokens.token.Token">
# for relation in doc.user_data:
#     print(relation)




# print([ents for ents in doc.ents])
# print([(ents.text, ents.label_) for ents in doc.ents])
# print(relation_density(doc))


# print(load_whitelist("data/drugs.txt"))
# EM_Creator(nlp,terms,"Animal")
#
# # nlp.add_pipe(relation_matcher, after="ner")
# # print(nlp.pipe_names)  property# the components in the pipeline
# print(Language.factories)
# doc = nlp(u"This is a text about Obama and tree kangaroos. I like cats and dogs. They are the best. Bill Gates always liked tree kangaroos.")
# # print("get pipeline: ",Language.get_pipe("bad"))
# print(doc.ents)


#run through list if theres a match with the entties

    # print("label: ", w.label_)
