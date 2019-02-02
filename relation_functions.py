from __future__ import unicode_literals, print_function

def extract_entity(ent,label):
###loops through the entities's head to find words that are associated with a relation and an entity
    if ent == ent.head:
        #if an entity is found return it
        if ent.pos_ == 'NOUN':
            return ent
        else:
            return [ents for ents in ent.subtree if ents.ent_type_ != label and ents.pos_ in ["PRON", "NOUN"]][0] #if a relation is returned, iterate through its children to find entities related to it
    else:
        return extract_entity(ent.head, label)
