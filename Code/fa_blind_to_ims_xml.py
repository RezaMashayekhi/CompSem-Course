

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


inputFileName = "Persian Blind Sample annotated.txt"
blindAnFileName2 = "Persian Blind Sample annotated.txt"
outputFileName = "fa_blind_ims_test.xml"

# Making farsi xml

oRoot = ET.Element("corpus")
oTree = ET.ElementTree(oRoot)
oRoot.set("lang", "persian")

faList = []
with open("../Data/" + inputFileName, "r") as f:
    faList = f.read().splitlines()

with open("../Data/" + blindAnFileName2, "r") as f:
    bL = f.read().splitlines()


id = 0
for l in faList:
    print(id)
    fa = normalizer.normalize(l)
    faT = bL[id].split("#")[0].split()
    #faT = fa.split()

    print(bL[id].split("#")[0].split())
    print(bL[id].split("#")[1])
    #print(bL[id])

    faIndex = 0
    if(bL[id].split("#")[1] != ""):
        #print(bL[id].split("#")[1].split("_")[0])
        faIndex = faT.index(bL[id].split("#")[1].split("_")[0].split()[0])
        if len(bL[id].split("#")[1].split("_"))>1:
            for i in range(1, len(bL[id].split("#")[1].split("_"))):
                faT[faIndex] = faT[faIndex] + "_" + faT[faIndex+i]
            for i in range(1, len(bL[id].split("#")[1].split("_"))):
                faT.pop(faIndex+i)


    faG = tagger.tag(faT)
    print(faT)

    lemma = ""
    for i in range(0, len(faT[faIndex].split("_"))):
        print(lemmatizer.lemmatize(faT[faIndex].split("_")[i]).split("#")[0])
        if (lemmatizer.lemmatize(faT[faIndex].split("_")[i]).split("#")[0] not in ['می', 'نمی', 'نم']):
            lemma += lemmatizer.lemmatize(faT[faIndex].split("_")[i]).split("#")[0] + "_"
    lemma = lemma.strip("_")

    if faG[faIndex][1] == "V" and lemma[-1]!="ن" and lemma[-1]!="ه":
        lemma +="ن"
    '''    
    lemma = lemmatizer.lemmatize(faT[faIndex]).split("#")[0]
    if (len(faT[faIndex].split("_"))==2):
        print(lemmatizer.lemmatize(faT[faIndex].split("_")[1]))
        lemma = lemmatizer.lemmatize(faT[faIndex].split("_")[0]).split("#")[0] +"_" + lemmatizer.lemmatize(faT[faIndex].split("_")[1]).split("#")[0]
        if len(lemmatizer.lemmatize(faT[faIndex].split("_")[1]).split("#"))>1:
            lemma += "ن"
    if (len(faT[faIndex].split("_"))==3):
        lemma = lemmatizer.lemmatize(faT[faIndex].split("_")[0]).split("#")[0] +"_" + lemmatizer.lemmatize(faT[faIndex].split("_")[1]).split("#")[0] + "_" + lemmatizer.lemmatize(faT[faIndex].split("_")[2]).split("#")[0]
    '''

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

xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + outputFileName, "w") as f:
   f.write(xmlstr)

#ET.indent(oTree, space="    ")
#oTree.write('../Data/' + outputFileName, encoding="UTF-8", xml_declaration=True)



