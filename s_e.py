from __future__ import unicode_literals, print_function
import spacy









def sent_ent(doc,label1, label2):
    sents = []
    ents1 = [s.text for s in doc.ents if s.label_ == label1]
    ents2 = [s.text for s in doc.ents if s.label_ == label2]

    for index, sent in enumerate(doc.sents):
        record = {}
        entities1 = []
        entities2= []
##later can code for any entities by look up the list, now just stick with the label
        sentence = sent.text.split()
        for word in sentence:
            # print(word)
            if word in ents1:
                entities1.append(word)
            if word in ents2:
                entities2.append(word)
        if len(entities1) > 0 or len(entities2) > 0:
            record["entities1"] = entities1
            record["entities2"] = entities2
            record["sentence"] = sent.text #unicode possibly imcompatible
            record["index"] = index
            sents.append(record)
    return sents
