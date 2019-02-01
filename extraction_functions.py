from __future__ import unicode_literals, print_function
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span, Token
from spacy.language import Language
from connectors import load_doc, load_whitelist, encode
from indexers import index1,index2,index3
from entity_matcher import EntityMatcherCreator
from relation_matcher import RelationMatcherCreator
import json

def entity_entity(label1, label2, entities1,entities2, text, scope):
    nlp = spacy.load("en_core_web_sm")
    Token.set_extension("text", default="", force=True)
    entities1_ = load_whitelist(entities1)
    entities2_ = load_whitelist(entities2)
    text_ = load_doc(text)
    EntityMatcherCreator(nlp,entities1_, label1)
    EntityMatcherCreator(nlp,entities2_, label2)
    doc = nlp(text_)
    return index1(doc,label1,label2, scope)

def relation_entity(label, relation, entities,relations, text, scope):
    nlp = spacy.load("en_core_web_sm")
    Token.set_extension("text", default="", force=True)
    entities_ = load_whitelist(entities)
    relations_ = load_whitelist(relations)
    text_ = load_doc(text)
    EntityMatcherCreator(nlp,entities_, label)
    RelationMatcherCreatortor(nlp,relations_, relation)
    doc = nlp(text_)
    return index2(doc,label,relation, scope)

def all_ent_rel(label1, label2, rel_label, entities1,entities2, relations, text, scope):
    nlp = spacy.load("en_core_web_sm")
    Token.set_extension("text", default="", force=True)
    entities1_ = load_whitelist(entities1)
    entities2_ = load_whitelist(entities2)
    relations_ = load_whitelist(relations)
    text_ = load_doc(text)
    EntityMatcherCreator(nlp,entities1_, label1)
    EntityMatcherCreator(nlp,entities2_, label2)
    RelationMatcherCreatortor(nlp, relations_, rel_label)
    doc = nlp(text_)
    return index3(doc,label1,label2, rel_label,scope)
