from __future__ import unicode_literals, print_function
import re

def load_doc(file):
    if type(file == "unicode") and file.find(".txt") < 0:
        return file.replace('\n', " ")
    with open(file, "r") as f:
        file_content = f.read()
        return encode(file_content).replace('\n', " ")
def load_whitelist(file):
    try:
        basestring
    except NameError:
        basestring = str
    if isinstance(file, list):
        return file
    if isinstance(file,basestring) and file.find('.txt') < 0:
        return re.findall(r'[^,;]+', file)
    with open(file, "r") as f:
        file_content = f.read()
        if file_content.find(";") > -1:
            return encode(re.findall(r'[^,;]+', file_content))
        else:
            return encode(file_content.split("\n"))
def encode(obj):
    try:
        basestring
    except NameError:
        basestring = str
    if isinstance(obj, list):
        utf = map(lambda x: x.decode('utf-8', 'ignore'), obj)
        return utf
    elif isinstance(obj,basestring):
            return obj.decode('utf-8', 'ignore')
    else:
        return obj
