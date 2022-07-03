# Imports
from __future__ import unicode_literals

import random
import xml.etree.ElementTree as ET
from xml.dom import minidom
from hazm import *

normalizer = Normalizer()
lemmatizer = Lemmatizer()
tagger = POSTagger(model='resources/postagger.model')
tagDic = {"V": "Verb", "N": "NOUN", "ADV": "ADV", "Ne": "NOUN"}

inputFileName = "Persian Blind Sample annotated.txt"
outputFileName = "fa_blind_test.xml"


# Making farsi xml

oRoot = ET.Element("corpus")
oTree = ET.ElementTree(oRoot)
oRoot.set("lang", "persian")
oText = ET.Element("text")
oText.set("id", "1")
oRoot.append(oText)

faList = []
with open("../Data/" + inputFileName, "r") as f:
    bl = f.read().splitlines()

id = 0

for l in bl:
    oSentence = ET.Element("sentence")
    oSentence.set("id", str(id))

    print(id)
    fa = normalizer.normalize(l)
    faT = l.split("#")[0].split()

    faIndex = 0
    if (bl[id].split("#")[1] != ""):
        # print(bL[id].split("#")[1].split("_")[0])
        faIndex = faT.index(bl[id].split("#")[1].split("_")[0].split()[0])
        if len(bl[id].split("#")[1].split("_")) > 1:
            for i in range(1, len(bl[id].split("#")[1].split("_"))):
                faT[faIndex] = faT[faIndex] + "_" + faT[faIndex + i]
            for i in range(1, len(bl[id].split("#")[1].split("_"))):
                faT.pop(faIndex + i)

    faG = tagger.tag(faT)

    for j in range(0, faIndex):
        oWf = ET.Element("wf")
        oWf.text = faT[j]
        oWf.set("lemma", lemmatizer.lemmatize(faT[j]).split("#")[0])
        oWf.set("pos", faG[j][1])
        oSentence.append(oWf)

    lemma = ""
    for i in range(0, len(faT[faIndex].split("_"))):
        print(lemmatizer.lemmatize(faT[faIndex].split("_")[i]).split("#")[0])
        if (lemmatizer.lemmatize(faT[faIndex].split("_")[i]).split("#")[0] not in ['می', 'نمی', 'نم']):
            lemma += lemmatizer.lemmatize(faT[faIndex].split("_")[i]).split("#")[0] + "_"
    lemma = lemma.strip("_")
    print(faG[faIndex])
    if faG[faIndex][1] == "V" and lemma[-1] != "ن" and lemma[-1] != "ه":
        lemma += "ن"

    oInstance = ET.Element("instance")
    oInstance.text = faT[faIndex]
    oInstance.set("id", lemma + "." + faG[faIndex][1] + "." + str(id))
    oInstance.set("lemma", lemma)
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

# ET.indent(oTree, space="    ")
# oTree.write('../Data/' + outputFileName, encoding="UTF-8", xml_declaration=True)



