from __future__ import print_function,unicode_literals
# import spacy
# from spacy.matcher import PhraseMatcher
# from spacy.tokens import Span
# from spacy.language import Language
# from collections import Counter
# from e_e import EM_Creator
# from load import load_doc, load_whitelist, encode
import json
from e_r import ent_relation

def index2(doc,label1, relation, scope = 1):
    # print('hit3')
    sent_index = {}
    sent_order = {}
    lower_label = str(label1.lower())
    lower_relation = str(relation.lower())
    # print("This hit")
    # print("lowerLabel: ", lower_label)

    for index,sent in enumerate(doc.sents):
        sent_index[sent] = index
    for index,sent in enumerate(doc.sents):
        sent_order[index] = sent

    entities = []
    types = [lower_label, lower_relation]
    print("doc in sent_ent", doc)
    print("userdata:", doc.user_data)
    for ent1 in doc.user_data[label1]:
        print(ent1['name'])
        print(ent1['sentence'])



        for rel in doc.user_data[relation]:
            obj = dict()
            print(ent1['name'])
            print(ent1['sentence'])
            ent1_sent = ent1["sentence"]
            rel_sent = rel["sentence"]


            # print(rel_sent)
            ent1_sent_i = sent_index[ent1_sent]
            rel_sent_i = sent_index[rel_sent]
            print("entindex1", ent1_sent_i)
            print("entindex2", rel_sent_i)
            print("difference",abs(ent1_sent_i - rel_sent_i))
            if abs(ent1_sent_i - rel_sent_i) < scope:
            # if ent1_sent == rel_sent:
                print('transfered to object')
                # print(ent1["name"], rel["name"])
                # print("sentence:", ent1["sentence"])
                # print("index", ent1["sentence"].text.index(ent1["name"]))
                # print("length", len(ent1["sentence"]))
                obj[str("entities")] = types
                # print(obj[entities])
                obj[lower_label] = {
                                str("value"): ent1["name"],
                                str("position"):  ent1["sentence"].text.index(ent1["name"]),
                                str("length"): len(ent1["name"]),
                                str("type"): lower_label
                                }
                obj[lower_relation] =  {
                                str("value"): rel["name"],
                                str("position"):  rel["sentence"].text.index(rel["name"]),
                                str("length"): len(rel["name"]),
                                str("index"): rel["index"],
                                str("type"):lower_relation
                                }
                sentence1 = ent1[str("sentence")]
                sentence2 = rel[str("sentence")]

                ent_token = rel["token"]
                entity = ent_relation(ent_token, relation)

                if entity:

                    obj[str("entity")] = {
                                        str("value"): str(entity.text),
                                        str("position"): entity.sent.text.index(entity.text),
                                        str("length"): len(entity.text),
                                        str("index"): entity.i,
                                        str("sentence"): str(entity.sent),
                                        #type
                                        }


                low = ent1_sent_i if ent1_sent_i < rel_sent_i  else rel_sent_i
                high = ent1_sent_i if ent1_sent_i > rel_sent_i  else rel_sent_i

                #loop thru and add them as a piece of a list
                phrase_list = [sent.text for sent in list(doc.sents)[low:high+1]]
                phrase_ = " ".join(phrase_list)


                obj[str("phrase")] = {
                                    str("text"): str(phrase_)
                                        }
                obj[str("sentence1")] = {
                                    str("text"): str(sentence1),
                                    str("index"): sent_index[sentence1]
                                    }
                obj[str("sentence2")] = {
                                    str("text"): str(sentence1),
                                    str("index"): sent_index[sentence2]
                }

                obj[str("relation")] = {
                                    str("text"): [str(anc) for anc in rel["ancestors"]],
                                    str("POS"): [anc.pos_ for anc in rel["ancestors"]]
                                    }
                obj[str("relation1")] = {
                                    str("text"): [str(anc) for anc in ent1["ancestors"]]
                                    }
                obj[str("children")] = {
                                    str("text"): [[str(child) for child in anc.children] for anc in rel['ancestors']]
                                    }

                # print("obj", obj)
                entities.append(obj)
    # print("jsondumps,", json.dumps(entities))
    return entities


def index1(doc,label1, label2, scope = 1):
    # print('hit3')
    sent_index = {}
    sent_order = {}
    lower_label1 = str(label1.lower())
    lower_label2 = str(label2.lower())
    # print("This hit")
    # print("lowerLabel: ", lower_label1)

    for index,sent in enumerate(doc.sents):
        sent_index[sent] = index
    for index,sent in enumerate(doc.sents):
        sent_order[index] = sent
    print('label1', doc.user_data[label2])

    entities = []
    types = [lower_label1, lower_label2]
    print("doc in sent_ent", doc)
    print("userdata:", doc.user_data)
    for ent2 in doc.user_data[label2]:
        print(ent2['name'])
        print(ent2['sentence'])



        for ent1 in doc.user_data[label1]:
            obj = dict()
            print(ent1['name'])
            print(ent1['sentence'])
            ent1_sent = ent1["sentence"]
            ent2_sent = ent2["sentence"]


            # print(ent2_sent)
            ent1_sent_i = sent_index[ent1_sent]
            ent2_sent_i = sent_index[ent2_sent]
            print("entindex1", ent1_sent_i)
            print("entindex2", ent2_sent_i)
            print("difference",abs(ent1_sent_i - ent2_sent_i))
            if abs(ent1_sent_i - ent2_sent_i) < scope:
            # if ent1_sent == ent2_sent:
                print('transfered to object')
                # print(ent1["name"], ent2["name"])
                # print("sentence:", ent1["sentence"])
                # print("index", ent1["sentence"].text.index(ent1["name"]))
                # print("length", len(ent1["sentence"]))
                obj[str("entities")] = types
                # print(obj[entities])
                obj[lower_label1] = {
                                str("value"): ent1["name"],
                                str("position"):  ent1["sentence"].text.index(ent1["name"]),
                                str("length"): len(ent1["name"]),
                                str("type"): lower_label1
                                }
                obj[lower_label2] =  {
                                str("value"): ent2["name"],
                                str("position"):  ent2["sentence"].text.index(ent2["name"]),
                                str("length"): len(ent2["name"]),
                                str("index"): ent2["index"],
                                str("type"):lower_label2
                                }
                sentence1 = ent1[str("sentence")]
                sentence2 = ent2[str("sentence")]



                low = ent1_sent_i if ent1_sent_i < ent2_sent_i  else ent2_sent_i
                high = ent1_sent_i if ent1_sent_i > ent2_sent_i  else ent2_sent_i

                #loop thru and add them as a piece of a list
                phrase_list = " ".join([sent.text for sent in list(doc.sents)[low:high+1]])
                phrase_ = "".join(phrase_list)


                obj[str("phrase")] = {
                                    str("text"): str(phrase_list)
                                        }
                obj[str("sentence1")] = {
                                    str("text"): str(sentence1),
                                    str("index"): sent_index[sentence1]
                                    }
                obj[str("sentence2")] = {
                                    str("text"): str(sentence1),
                                    str("index"): sent_index[sentence2]
                }

                obj[str("relation")] = {
                                    str("text"): [str(anc) for anc in ent2["ancestors"] if anc.pos_ in ["VERB", "NOUN"]],
                                    str("POS"): [anc.pos_ for anc in ent2["ancestors"]]
                                    }
                obj[str("relation1")] = {
                                    str("text"): [str(anc) for anc in ent1["ancestors"] if anc.pos_ in ["VERB", "NOUN"]]
                                    }
                obj[str("children")] = {
                                    str("text"): [[str(child) for child in anc.children] for anc in ent2['ancestors'] ]
                                    }
                # print("obj", obj)
                entities.append(obj)
    # print("jsondumps,", json.dumps(entities))
    return entities
def index3(doc,label1, label2,relation,scope = 1):
    # print('hit3')
    sent_index = {}
    sent_order = {}
    lower_label1 = str(label1.lower())
    lower_label2 = str(label2.lower())
    rel_label = str(relation.lower())
    # print("This hit")
    # print("lowerLabel: ", lower_label1)
    for index,sent in enumerate(doc.sents):
        sent_index[sent] = index
    for index,sent in enumerate(doc.sents):
        sent_order[index] = sent
    print("HELLOOOOOOO")
    entities = []
    types = [lower_label1, lower_label2]
    # print("doc in sent_ent", doc)
    # print("userdata:", doc.user_data)
    for ent2 in doc.user_data[label2]:
        print(ent2['name'])
        print(ent2['sentence'])



        for ent1 in doc.user_data[label1]:
            obj = dict()
            print(ent1['name'])
            print(ent1['sentence'])
            ent1_sent = ent1["sentence"]
            ent2_sent = ent2["sentence"]


            # print(ent2_sent)
            ent1_sent_i = sent_index[ent1_sent]
            ent2_sent_i = sent_index[ent2_sent]
            print("entindex1", ent1_sent_i)
            print("entindex2", ent2_sent_i)
            print("difference",abs(ent1_sent_i - ent2_sent_i))
            if abs(ent1_sent_i - ent2_sent_i) < scope:
            # if ent1_sent == ent2_sent:
                print('transfered to object')
                # print(ent1["name"], ent2["name"])
                # print("sentence:", ent1["sentence"])
                # print("index", ent1["sentence"].text.index(ent1["name"]))
                # print("length", len(ent1["sentence"]))
                obj[str("entities")] = types
                # print(obj[entities])
                obj[lower_label1] = {
                                str("value"): ent1["name"],
                                str("position"):  ent1["sentence"].text.index(ent1["name"]),
                                str("length"): len(ent1["name"]),
                                str("type"): lower_label1
                                }
                obj[lower_label2] =  {
                                str("value"): ent2["name"],
                                str("position"):  ent2["sentence"].text.index(ent2["name"]),
                                str("length"): len(ent2["name"]),
                                str("index"): ent2["index"],
                                str("type"):lower_label2
                                }
                sentence1 = ent1[str("sentence")]
                sentence2 = ent2[str("sentence")]



                low = ent1_sent_i if ent1_sent_i < ent2_sent_i  else ent2_sent_i
                high = ent1_sent_i if ent1_sent_i > ent2_sent_i  else ent2_sent_i

                #loop thru and add them as a piece of a list
                phrase_list = [sent.text for sent in list(doc.sents)[low:high+1]]
                for rel in doc.user_data[relation]:
                    if rel["sentence"].text in phrase_list:
                        rel_entity = rel["token"]
                        break

                if rel_entity:
                    print(rel_entity)
                    obj[str(relation)] = {
                                        str("value"): str(rel_entity.text),
                                        str("position"): rel_entity.sent.text.index(rel_entity.text),
                                        str("length"): len(rel_entity.text),
                                        str("index"): rel_entity.i,
                                        str("sentence"): str(rel_entity.sent),
                                        str("type"): rel_label
                                        }
                    obj[str("relation")] = {
                                            str("value"): str(rel_label)
                                            }


                phrase_ = "".join(phrase_list)
                # if doc.user_data["relation"]:
                #     r


                obj[str("phrase")] = {
                                    str("text"): str(phrase_list)
                                        }
                obj[str("sentence1")] = {
                                    str("text"): str(sentence1),
                                    str("index"): sent_index[sentence1]
                                    }
                obj[str("sentence2")] = {
                                    str("text"): str(sentence1),
                                    str("index"): sent_index[sentence2]
                }


                # print("obj", obj)
                entities.append(obj)
    # print("jsondumps,", json.dumps(entities))
    return entities
