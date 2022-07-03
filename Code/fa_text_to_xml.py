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
outputFileName = "fa_bitext_test.xml"
inputIndexFileName = "fa_bitext_instance_index.txt"

# Making farsi xml

oRoot = ET.Element("corpus")
oTree = ET.ElementTree(oRoot)
oRoot.set("lang", "persian")
oText = ET.Element("text")
oText.set("id", "1")
oRoot.append(oText)


faList = []
with open("../Data/" + inputFileName, "r") as f:
    faList = f.read().splitlines()
with open("../Data/" + inputIndexFileName, "r") as f:
    index = f.read().splitlines()

id = 0

for l in faList:
    oSentence = ET.Element("sentence")
    oSentence.set("id", str(id))
    
    print(id)
    fa = normalizer.normalize(l)
    faT = word_tokenize(fa)
    faG = tagger.tag(faT)
    faIndex = int(index[id])
    for j in range(0, faIndex):
        oWf = ET.Element("wf")
        oWf.text = faT[j]
        oWf.set("lemma", lemmatizer.lemmatize(faT[j]).split("#")[0])
        oWf.set("pos", faG[j][1])
        oSentence.append(oWf)

    oInstance = ET.Element("instance")
    oInstance.text = faT[faIndex]
    oInstance.set("id", lemmatizer.lemmatize(faT[faIndex]).split("#")[0] + "." + faG[faIndex][1] + "." + str(id))
    oInstance.set("lemma", lemmatizer.lemmatize(faT[faIndex]).split("#")[0])
    oInstance.set("pos", faG[faIndex][1])
    oSentence.append(oInstance)

    for j in range(faIndex + 1, len(faT)):
        oWf = ET.Element("wf")
        oWf.text = faT[j]
        oWf.set("lemma", lemmatizer.lemmatize(faT[j]).split("#")[0])
        oWf.set("pos", faG[j][1])
        oSentence.append(oWf)
    
    oText.append(oSentence)
    id += 1



xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + outputFileName, "w") as f:
   f.write(xmlstr)

#ET.indent(oTree, space="    ")
#oTree.write('../Data/' + outputFileName, encoding="UTF-8", xml_declaration=True)



