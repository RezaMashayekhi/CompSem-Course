# Imports
from __future__ import unicode_literals

import random
import xml.etree.ElementTree as ET
from xml.dom import minidom
from hazm import *

normalizer = Normalizer()
lemmatizer = Lemmatizer()
tagger = POSTagger(model='resources/postagger.model')
tagDic = {"V":"Verb", "N":"NOUN", "ADV":"ADV", "Ne":"NOUN"}


inputFileName = "Persian 120k.txt"
outputFileName = "fa_bitext_ims_test.xml"
inputIndexFileName = "fa_bitext_instances_index.txt"

# Making farsi xml

oRoot = ET.Element("corpus")
oTree = ET.ElementTree(oRoot)
oRoot.set("lang", "persian")

faList = []
with open("../Data/" + inputFileName, "r") as f:
    faList = f.read().splitlines()

with open("../Data/" + inputIndexFileName, "r") as f:
    inList = f.read().splitlines()

id = 0
line = 0

for l in faList:
    print(id)

    #fa = normalizer.normalize(l)
    fa = l
    faT = word_tokenize(fa)
    faG = tagger.tag(faT)

    for k in inList[line].split():

        faIndex = int(k)
        lemma = lemmatizer.lemmatize(faT[faIndex]).split("#")[0].replace("/","")
        oLexelt = ET.Element("lexelt")
        oLexelt.set("item", lemma +"." + faG[faIndex][1])
        oRoot.append(oLexelt)

        oInstance = ET.Element("instance")
        oInstance.set("id", lemma + "." + faG[faIndex][1] +"." + str(id))
        oLexelt.append(oInstance)

        oContext = ET.Element("context")
        text = ""
        for j in range(faIndex):
            text += faT[j] + "/" + lemmatizer.lemmatize(faT[j]).split("#")[0] + "/" + faG[j][1] + " "
        oContext.text = text
        oInstance.append(oContext)

        oHead = ET.Element("head")
        oHead.text = faT[faIndex] + "/" + lemma + "/" + faG[faIndex][1]
        text = ""
        for j in range(faIndex + 1, len(faT)):
            text += faT[j] + "/" + lemmatizer.lemmatize(faT[j]).split("#")[0] + "/" + faG[j][1] + " "
        oHead.tail = text
        oContext.append(oHead)

        id += 1
    line += 1

xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + outputFileName, "w") as f:
   f.write(xmlstr)

#ET.indent(oTree, space="    ")
#oTree.write('../Data/' + outputFileName, encoding="UTF-8", xml_declaration=True)



