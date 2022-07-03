import random
import xml.etree.ElementTree as ET
from xml.dom import minidom
import nltk as nl
from nltk.stem import WordNetLemmatizer
# Init the Wordnet Lemmatizer

dic = {"NN":"NOUN", "JJ":"ADJ", "VBZ": "VERB", "RB":"ADV", "RBS":"ADJ",
        "NNS":"NOUN", "NP":"NOUN", "VVP":"VERB", "JJS":"ADJ", "VVZ":"VERB",
        "VVG":"VERB", "VV":"VERB", "VVN":"VERB", "VVD": "VERB", "EX" :"ADV",
        "RBR":"ADV", "JJR":"ADJ", "IN":"ADV", "DT":"ADJ", "PDT":"ADV", "NPS":"NOUN",
        "RP":"ADV", "CD":"ADJ", "MD":"VERB", "PP":"NOUN", "VHD":"VERB", "VHG": "VERB" ,
        "VHZ": "VERB", "VHN": "VERB", "VHP" : "VERB" , "VH": "VERB", "PP$":"NOUN", "UH":"NOUN",
       "WRB": "ADV", "VBP":"VERB", "IN/that":"NOUN", "CC":"NOUN", "VBD":"VERB", "WP":"NOUN",
       "WDT":"NOUN", "VBN":"VERB", "LS":"NOUN", "SENT":"NOUN", "TO":"NOUN", ",":"NOUN",
       "VB": "VERB", "WP$":"NOUN", "VBG":"VERB"}

lm = WordNetLemmatizer()

blindAnFileName2 = "English_blind_annotated.txt"
outputFileName = "en_blind_test_ims.xml"

# Making farsi xml

oRoot = ET.Element("corpus")
oTree = ET.ElementTree(oRoot)
oRoot.set("lang", "persian")

with open("../Output/Bitext/Blind_Sample/Annotated/" + blindAnFileName2, "r") as f:
    bL = f.read().splitlines()


id = 0
for l in bL:
    print(id)
    en = l
    enT = en.split("#")[0].split()
    #faT = fa.split()

    print(bL[id].split("#")[0].split())
    print(bL[id].split("#")[1])
    #print(bL[id])

    enIndex = 0
    if(en.split("#")[1] != ""):
        #print(bL[id].split("#")[1].split("_")[0])
        enIndex = enT.index(en.split("#")[1])

    lemma = lm.lemmatize(enT[enIndex])
    posL = nl.pos_tag(enT)
    pos = ""
    for j in posL:
        if (enT[enIndex] == j[0] or set(j[0]).issubset(set(enT[enIndex]))):
            pos = j[1]
            break
    if pos != "" and pos in dic:
        pos = dic[pos]
    else:
        pos = "NOUN"

    oLexelt = ET.Element("lexelt")
    oLexelt.set("item", lemma +"." + pos)
    oLexelt.set("pos", pos)
    oRoot.append(oLexelt)

    oInstance = ET.Element("instance")
    oInstance.set("id", lemma + "." + pos +"." + str(id))
    oLexelt.append(oInstance)

    oContext = ET.Element("context")
    text = ""
    for j in range(enIndex):
        text += enT[j] + " "
    oContext.text = text
    oInstance.append(oContext)

    oHead = ET.Element("head")
    oHead.text = enT[enIndex]
    text = ""
    for j in range(enIndex + 1, len(enT)):
        text += enT[j] + " "
    oHead.tail = text
    oContext.append(oHead)
    id += 1

xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + outputFileName, "w") as f:
   f.write(xmlstr)

#ET.indent(oTree, space="    ")
#oTree.write('../Data/' + outputFileName, encoding="UTF-8", xml_declaration=True)



