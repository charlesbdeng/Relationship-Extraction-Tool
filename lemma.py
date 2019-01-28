from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.language import Language

def LM_Creator(nlp, terms, rel):
    # terms_ = encode(terms)
    pipe = "Lemma_"+label
    Language.factories[pipe] = lambda nlp: EntityMatcher(nlp, terms,label)
    nlp.add_pipe(nlp.create_pipe(pipe), before="ner")


class LemmaMatcher(object):

    def __init__(self, nlp, terms, label):
        patterns = [nlp(text) for text in terms]
        # for alt in patterns:
        #     print(alt)
        #     print(type(alt))
        #     print(type(alt[0]))
        #     print("pos:", alt[0].ent_type_)
        # #//insert a getter function that can return the necessary information
        # # print("patterns: ", patterns)
        # print("name", self.name)
        self.name = "LM_"+ label
        # print(self.name)
        # print("nlp.vocab: ", str(nlp.vocab[u"435"].text))
        # print(type(nlp.vocab[u"cat"].text))
        ##transform into docs
        print(patterns)
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add(label, None, *patterns)
        self.label = label



    def __call__(self, doc):
        matches = self.matcher(doc)
        entities = []
        for match_id, start, end in matches:
            phrase = doc[start:end]
            # print(phrase)
            # print("phrase:", phrase)
            # print("type:", type(phrase))
#             phrase: acetylsalicylic acid
# type: <type "spacy.tokens.span.Span">


            compound = len(phrase) > 1
            if compound:
                literal = ""
                # print(phrase)
                # print(len(phrase))
            for index,tok in enumerate(phrase):
                # print(index)
                entity = dict()
                # print("entity:", tok)
                # print("POS:", tok.pos_

                type = self.label.lower()
                if compound:
                    literal = doc[start:end].text
                    ##regex here to fix - and spaces
                    # print("literal:",literal)
                    if index == len(phrase)-1:
                        entity["name"] = literal
                        entity["index"] = start
                        tok.ent_type_ = self.label
                        entity["pos"] = tok.pos_
                        entity["length"] = len(entity["name"])
                        entity["sentence"] = tok.sent
                        entity["type"] = tok.ent_type_
                        entity["token"] = tok
                        entity["length"] = len(entity["name"])
                        entity["dep"] = tok.dep_
                        entity["ancestors"] = [anc for anc in tok.ancestors]
                        entity["children"] = tok.children
                        entity["head"] = tok.head
                        entities.append(entity)

                else:

                    entity["name"] = tok.text
                    entity["index"] = tok.i
                    tok.ent_type_ = self.label
                    entity["pos"] = tok.pos_
                    entity["length"] = len(entity["name"])
                    entity["sentence"] = tok.sent
                    entity["type"] = tok.ent_type_
                    entity["token"] = tok
                    entity["length"] = len(entity["name"])
                    entity["dep"] = tok.dep_
                    entity["ancestors"] = [anc for anc in tok.ancestors]
                    entity["children"] = tok.children
                    entity["head"] = tok.head
                # print("name", tok)
                # print("ancestors:",[anc for anc in tok.ancestors])
                # print("head", tok.head)
                # print("dep", tok.dep_)
                # print("vocab:", tok.vocab)
                    # print("start", tok.i)

                    entity["pos"] = tok.pos_
                    entity["lemma"] = tok.lemma_


                    entities.append(entity)
                    ##shortened form will appear as well which is good if the query only specifies that form

                # print("name:", tok.text)
                # print("pos: ", tok.pos_)
                # print("length:" ,len(tok))
                # print("sentence:", tok.sent)

            span = Span(doc, start, end, label=match_id)
            # print(span.text)
            # print(list(doc.ents))
            #ValueError: [E098] Trying to set conflicting doc.ents: '(150, 153, u'GPE')' and '(151, 153, u'COUNTRIES')'. A token can only be part of one entity, so make sure the entities you're setting don't overlap.
            # doc.ents = list(doc.ents) + [span]
        # print(self.name)
        # print(type(doc.user_data))
        # print("type", type(doc.user_data))
        # print(entities)

        doc.user_data[self.label] = entities
        # print("hit3")
        return doc
