from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.language import Language
from collections import Counter
from connectors import load_doc, load_whitelist, encode
from entity_matcher import EntityMatcherCreator
from relation_functions import extract_entity
from e_r import ent_relation
from relation_matcher import RM_Creator
from indexers import index1,index2, index3
from spacy.lemmatizer import Lemmatizer
from spacy.lang.en import LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES
# nlp = spacy.load("en_core_web_sm")
# matcher = Matcher(nlp.vocab)
#
# def set_sentiment(matcher, doc, i, matches):
#     doc.sentiment += 0.1
#
# pattern1 = [{"ORTH": "Google"}, {"ORTH": "I"}, {"ORTH": "/"}, {"ORTH": "O"}]
# matcher.add("GoogleIO", None, pattern1) # match "Google I/O" or "Google i/o"
#
# doc = nlp(u"A text about Google I/O. Google I/O, Google I/O, Google I/O.")
# matches = matcher(doc)
#
# for match_id, start, end in matches:
#    string_id = nlp.vocab.strings[match_id]
#    span = doc[start:end]
#    print(string_id, span.text)
# print("Sentiment", doc.sentiment)
# nlp = spacy.load("en_core_web_sm")
# # # presidents_ = load_whitelist("data/presidents.txt")
# # # countries_ = load_whitelist("data/countries.txt")
# # # print(countries_)
# # # EM_Creator(nlp, presidents_, "PRESIDENTS")
# # # EM_Creator(nlp, countries_, "COUNTRIES")
# # # doc = nlp(load_doc("data/history.txt"))
# # # print(sent_ents(doc,"PRESIDENTS", "COUNTRIES",1))
# lemmatizer = Lemmatizer(LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES)
# lemmas = lemmatizer(u'treating', u'TREAT')
# print(lemmas[0])
#
# disease = ['Fail']
# drug = ['experience']
nlp = spacy.load('en_core_web_sm')
disease = load_whitelist(["psoriasis"])
drug = load_whitelist(["nucleotides"])
cure = load_whitelist(['treat'])
EntityMatcherCreator(nlp, disease, "disease")
EntityMatcherCreator(nlp, drug, "drug")
RM_Creator(nlp, cure, "cure")
# doc = nlp(u"\"In our job, we're going to get this exposure,\" said Mike Holland, an American Airlines captain and resident \"radiation expert\" for the Allied Pilots Association, the union that represents American's 15,000 pilots. \"There's no way you can be a pilot and not get this exposure.\"")

doc = nlp("cylic nucleotides might ultimately safely and effectively treat  psoriasis. It might also treat psoriasis")

# doc = nlp("The use of methotrexate as a treatment for psoriasis.")

# doc = nlp(nlp("Failure can be treated with experience.").text)
print(index3(doc,"drug","disease","cure",1 ))
# print([ents for ents in doc.ents])
# print([doc.user_data])
# import spacy
# from spacy.matcher import Matcher
#
# nlp = spacy.load('en_core_web_sm')
# matcher = Matcher(nlp.vocab)
# pattern = [{'ORTH': '('}, {'SHAPE': 'ddd'}, {'ORTH': ')'}, {'SHAPE': 'ddd'},
#            {'ORTH': '-', 'OP': '?'}, {'SHAPE': 'ddd'}]
# matcher.add('PHONE_NUMBER', None, pattern)
#
# doc = nlp(u"Call me at (123) 456 789 or (123) 456 789!")
# print([t.text for t in doc])
# matches = matcher(doc)
# for match_id, start, end in matches:
#     span = doc[start:end]
#     print(span.text)
# import spacy
# from spacy import displacy
# nlp = spacy.load('en_core_web_sm')
# # doc = nlp("The use of methotrexate as a treatment for psoriasis.")
# doc = nlp("Sinequa does a great job of structuring unstructured information.")
# # doc.user_data["DISEASE"] = ["psoriasis"]
# # doc1 = nlp(u"\"Being able to forecast a higher radiation risk for so-called 'polar' planes, those that tend to fly at higher altitudes near the Earth's poles, would allow commercial airlines to warn pilots to reroute planes to lower altitudes to decrease the risk of long-term exposure to radiation for their crews, who fly the same route over and over again,\" Clifford Lopate, a UNH physics researcher and professor, said in a March 5 statement.")
# # doc2 = nlp(u"\"In our job, we're going to get this exposure,\" said Mike Holland, an American Airlines captain and resident \"radiation expert\" for the Allied Pilots Association, the union that represents American's 15,000 pilots. \"There's no way you can be a pilot and not get this exposure.\"")
# # ents = [(ent,ent.head) for ent in doc]
# #
# displacy.serve([doc], style='dep')
# user_data = ent_relation(ents[6][0],"DISEASE")
# print("usserdata", user_data)
# print(doc.ents[0])
# for ent in ents:
#     print(ent[0])
#     print([child for child in ent[1]])
# nlp = spacy.load('en_core_web_sm')
# person = load_whitelist(["Charles Deng", "Deng", "grind", "complex", "thinkable", "value"])
# position = load_whitelist(['captain'])
# cures = load_whitelist(['treat'])
# RM_Creator(nlp, cures, "CURES")
# TA_Creator(nlp, person, "PERSON")
# TA_Creator(nlp, person, "POSITION")
# doc = nlp(u"\"In our job, we're going to get this exposure,\" said Mike Holland, an American Airlines captain and resident \"radiation expert\" for the Allied Pilots Association, the union that represents American's 15,000 pilots. \"There's no way you can be a pilot and not get this exposure.\"")
# doc = nlp("Charles Deng is a treatment. He cures complex problems outside the thinkable and grind through them to add value. He is a captain")
# # print("person", doc.user_data['PERSON'])
# print("ents",doc.ents)
# print("user_data:", doc.user_data)
# print(doc.user_data['POSITION'])
# print(sent_ents(doc, "PERSON", "POSITION",1))
# matcher = Matcher(nlp.vocab)
# # add match ID "HelloWorld" with no callback and one pattern
# pattern = [[{'LOWER': 'hello'}], [{'LEMMA':'headche'}]]
# matcher.add('HelloWorld', None, *pattern)
# doc = nlp(u'Hello, world! Hello world, these headaches are so good!')
# matches = matcher(doc)
# for match_id, start, end in matches:
#     string_id = nlp.vocab.strings[match_id]  # get string representation
#     span = doc[start:end]  # the matched span
#     print(match_id, string_id, start, end, span.text)
# for tok in doc:
#     print(tok.lemma_)
# import spacy
# from spacy.matcher import Matcher
# import re
# nlp = spacy.load('en_core_web_sm')
# definitely_flag = lambda text: bool(re.compile(r""+'deff?in[ia]tely').match(text))
# IS_DEFINITELY = nlp.vocab.add_flag(definitely_flag)
# matcher = Matcher(nlp.vocab)
# matcher.add('DEFINITELY', None, [{IS_DEFINITELY: True}])
# treat = lambda text: bool(re.compile(r""+'.*treat.*').match(text))
# IS_DEFINITELY = nlp.vocab.add_flag(treat)
# matcher.add('TREAT', None, [{IS_DEFINITELY: True}])
# doc = nlp(u'The spelling is "definitely", not "definately" or "deffinitely". treat')
# matches = matcher(doc)
# for match_id, start, end in matches:
#     span = doc[start:end]
#     print(span.text)
