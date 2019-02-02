from __future__ import unicode_literals, print_function
import re

def load_doc(file):
    #function to load text
    if type(file == "unicode") and file.find(".txt") < 0:
        return file.replace('\n', " ")
    with open(file, "r") as f:
        file_content = f.read()
        return encode(file_content).replace('\n', " ")


def load_whitelist(file):
    #function to load whitelist
    try:
        basestring
    except NameError:
        basestring = str
    #above code needs to be taken out when running using python 2.7
    if isinstance(file, list):
        return file
    if isinstance(file,basestring) and file.find('.txt') < 0:
        #parses string of words separated by semicolons or commas
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
    #decodes text not in unicode form
    if isinstance(obj, list):
        utf = map(lambda x: x.decode('utf-8', 'ignore'), obj)
        return utf
    elif isinstance(obj,basestring):
            return obj.decode('utf-8', 'ignore')
    else:
        return obj
