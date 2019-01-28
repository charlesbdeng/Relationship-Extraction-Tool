from __future__ import unicode_literals, print_function
import re

def load_doc(file):
    if type(file == "unicode") and file.find(".txt") < 0:
        # print("Identified as string or unicode!")
        # print(type(file))
        # print("encoding", file.encode("utf-8"))
        # print("encode=>decode", file.encode("utf-8").decode("utf-8","ignore"))
        # return file.encode("utf-8").decode("utf-8", "ignore").replace('\n', " ")
        # print(file.replace('\n', " "))
        return file.replace('\n', " ")
    with open(file, "r") as f:
        file_content = f.read()
        # print(file_content)
        # print(type(file_content))

        return encode(file_content).replace('\n', " ")
def load_whitelist(file):
    # print("file",file)
    if isinstance(file, list):
        return file
    if isinstance(file,str) and file.find('.txt') < 0:
        return re.findall(r'[^,;]+', file)
    with open(file, "r") as f:
        file_content = f.read()
        # print("file_content",file_content)
        # re.split("(\W+)")

        if file_content.find(";") > -1:
            # print ("regex", re.findall(r'[^,;]+', file_content))
            return encode(re.findall(r'[^,;]+', file_content))
        else:
            # print("space load works")
            return encode(file_content.split("\n"))
def encode(obj):
    # print('hit encode function')
    # print("object's type",type(obj))
    if isinstance(obj, list):
        utf = map(lambda x: x.decode('utf-8', 'ignore'), obj)
        return utf
    elif isinstance(obj,basestring):
            return obj.decode('utf-8', 'ignore')
    else:
        # print("bypassed all filters")
        return obj
# load_doc('data/history.txt')
