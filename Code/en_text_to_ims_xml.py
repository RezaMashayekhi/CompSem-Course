import random
import xml.etree.ElementTree as ET
from xml.dom import minidom
import nltk as nl
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
#nl.download('stopwords')
# Init the Wordnet Lemmatizer
lm = WordNetLemmatizer()

# Lemmatize Single Word
#print(lm.lemmatize("bats"))
#print(nl.pos_tag(['feet']))

inputFileName = "English 120k.txt"
outputFileName = "en_bitext_ims_test.xml"
inputIndexFileName = "en_bitext_instances_index.txt"

dic = {"NN":"NOUN", "JJ":"ADJ", "VBZ": "VERB", "RB":"ADV", "RBS":"ADJ",
        "NNS":"NOUN", "NP":"NOUN", "VVP":"VERB", "JJS":"ADJ", "VVZ":"VERB",
        "VVG":"VERB", "VV":"VERB", "VVN":"VERB", "VVD": "VERB", "EX" :"ADV",
        "RBR":"ADV", "JJR":"ADJ", "IN":"ADV", "DT":"ADJ", "PDT":"ADV", "NPS":"NOUN",
        "RP":"ADV", "CD":"ADJ", "MD":"VERB", "PP":"NOUN", "VHD":"VERB", "VHG": "VERB" ,
        "VHZ": "VERB", "VHN": "VERB", "VHP" : "VERB" , "VH": "VERB", "PP$":"NOUN", "UH":"NOUN",
       "WRB": "ADV", "VBP":"VERB", "IN/that":"NOUN", "CC":"NOUN", "VBD":"VERB", "WP":"NOUN",
       "WDT":"NOUN", "VBN":"VERB", "LS":"NOUN", "SENT":"NOUN", "TO":"NOUN", ",":"NOUN",
       "VB": "VERB", "WP$":"NOUN", "VBG":"VERB"}

stop_words = set(stopwords.words('english'))

oRoot = ET.Element("corpus")
oTree = ET.ElementTree(oRoot)
oRoot.set("lang", "english")


enList = []
with open("../Data/" + inputFileName, "r") as f:
    enList = f.read().splitlines()

inList=[]
with open("../Data/" + inputIndexFileName, "r") as f:
    inList = f.read().splitlines()

id = 0
line = 0
for l in enList:
    print(id)
    en = l
    #if(id==12):
    #    break
    enT = en.split()
    for k in inList[line].split():

        enIndex = int(k)

        lemma = lm.lemmatize(enT[enIndex]).replace("/","")
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

        #print(enT[enIndex],enT)
        #print(posL)
        #print(pos)

        oLexelt = ET.Element("lexelt")
        oLexelt.set("item", lemma + "." + pos)
        oLexelt.set("pos", pos)
        oRoot.append(oLexelt)

        oInstance = ET.Element("instance")
        oInstance.set("id", lemma + "." + pos + "." + str(id))
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
    line += 1

xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + outputFileName, "w") as f:
    f.write(xmlstr)

#oRoot.indent(oTree, space="    ")
#oTree.write('../Data/' + outputFileName, encoding="UTF-8", xml_declaration=True)



