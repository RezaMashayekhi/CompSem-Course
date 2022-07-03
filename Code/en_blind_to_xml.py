import random
import xml.etree.ElementTree as ET
from xml.dom import minidom
import nltk as nl
from nltk.stem import WordNetLemmatizer
# Init the Wordnet Lemmatizer
lm = WordNetLemmatizer()


dic = {"NN":"NOUN", "JJ":"ADJ", "VBZ": "VERB", "RB":"ADV", "RBS":"ADJ",
        "NNS":"NOUN", "NP":"NOUN", "VVP":"VERB", "JJS":"ADJ", "VVZ":"VERB",
        "VVG":"VERB", "VV":"VERB", "VVN":"VERB", "VVD": "VERB", "EX" :"ADV",
        "RBR":"ADV", "JJR":"ADJ", "IN":"ADV", "DT":"ADJ", "PDT":"ADV", "NPS":"NOUN",
        "RP":"ADV", "CD":"ADJ", "MD":"VERB", "PP":"NOUN", "VHD":"VERB", "VHG": "VERB" ,
        "VHZ": "VERB", "VHN": "VERB", "VHP" : "VERB" , "VH": "VERB", "PP$":"NOUN", "UH":"NOUN",
       "WRB": "ADV", "VBP":"VERB", "IN/that":"NOUN", "CC":"NOUN", "VBD":"VERB", "WP":"NOUN",
       "WDT":"NOUN", "VBN":"VERB", "LS":"NOUN", "SENT":"NOUN", "TO":"NOUN", ",":"NOUN",
       "VB": "VERB", "WP$":"NOUN", "VBG":"VERB"}


inputFileName = "English Blind Sample (annotated & reformatted).txt"
outputFileName = "en_blind_test.xml"


# Making farsi xml

oRoot = ET.Element("corpus")
oTree = ET.ElementTree(oRoot)
oRoot.set("lang", "english")
oText = ET.Element("text")
oText.set("id", "1")
oRoot.append(oText)


with open("../Data/" + inputFileName, "r") as f:
    bl = f.read().splitlines()

id = 0

for l in bl:
    oSentence = ET.Element("sentence")
    oSentence.set("id", str(id))

    print(id)
    en = l
    enT = en.split("#")[0].split()

    enIndex = 0
    if (en.split("#")[1] != ""):
        # print(bL[id].split("#")[1].split("_")[0])
        enIndex = enT.index(en.split("#")[1])

    posL = nl.pos_tag(enT)
    enG = []
    for i in enT:
        f = 0
        for j in posL:
            if (j[0] == i or set(j[0]).issubset(set(i))):
                enG.append(j[1])
                f = 1
                break
        if f == 0:
            enG.append(nl.pos_tag(i)[1])

    for i in range(0, len(enG)):
        if enG[i] not in dic:
            enG[i] = "NOUN"
        else:
            enG[i] = dic[enG[i]]

    for j in range(0, enIndex):
        oWf = ET.Element("wf")
        oWf.text = enT[j]
        oWf.set("lemma", lm.lemmatize(enT[j]))
        oWf.set("pos", enG[j])
        oSentence.append(oWf)


    oInstance = ET.Element("instance")
    oInstance.text = enT[enIndex]
    oInstance.set("id", lm.lemmatize(enT[enIndex]) + "." + enG[enIndex] + "." + str(id))
    oInstance.set("lemma", lm.lemmatize(enT[enIndex]))
    oInstance.set("pos", enG[enIndex])
    oSentence.append(oInstance)

    for j in range(enIndex + 1, len(enT)):
        oWf = ET.Element("wf")
        oWf.text = enT[j]
        oWf.set("lemma", lm.lemmatize(enT[j]))
        oWf.set("pos", enG[j])
        oSentence.append(oWf)

    oText.append(oSentence)
    id += 1

xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + outputFileName, "w") as f:
    f.write(xmlstr)

# ET.indent(oTree, space="    ")
# oTree.write('../Data/' + outputFileName, encoding="UTF-8", xml_declaration=True)



