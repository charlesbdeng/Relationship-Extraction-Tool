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
    return json.dumps(entities)
