# Imports
from __future__ import unicode_literals

import random
import xml.etree.ElementTree as ET
from xml.dom import minidom
from hazm import *
from simalign import SentenceAligner


normalizer = Normalizer()
lemmatizer = Lemmatizer()
tagger = POSTagger(model='resources/postagger.model')
tagDic = {"V":"Verb", "N":"NOUN", "ADV":"ADV", "Ne":"NOUN"}

myaligner = SentenceAligner(model="bert", token_type="bpe", matching_methods="m")

inputFileName = "en_gold.xml"
outputFileName = "fa_gold.xml"
translatedFileName = "fa_texted_gold.txt"
normalizedFileName = "normalized_texted_train.txt"
inputKeyFileName = "en_gold_key.txt"
outputKeyFileName = "fa_gold_key.txt"
alignedFileName = "aligned_gold.txt"
tree = ET.parse("../Data/" + inputFileName)
root = tree.getroot()

# Making farsi xml
oRoot = ET.Element("corpus")
oRoot.set("lang", "persian")

faList = []
enList = []
with open("../Data/" + translatedFileName, "r") as f:
    faList = f.read().splitlines()
with open("../Data/" + normalizedFileName, "r") as f:
    enList = f.read().splitlines()
with open("../Data/" + inputKeyFileName, "r") as f:
    keys = f.read().splitlines()
with open("../Data/" + alignedFileName, "r") as f:
    aligns = f.read().splitlines()

f = open("../Data/" + outputKeyFileName, "w")

i = 0
en = ""
k = 0
flag=1
#for text in root:
#    if flag==0:
#        break
for sentence in root:
    print(sentence.tag)
    if flag== 0:
        break
    for instance in sentence.findall("instance"):
        if(i==3490):
            flag=0
            break
        print(i)
        if (len(instance.text.split())>1):
            instance.text = "_".join(instance.text.split())
        #pen = en

        #en = enList[i]
        #print("mohem", head.text, en.split() )
        #if (" ".join(pen.split()) != " ".join(en.split())):
        #s = SequenceMatcher(None, context.text + " " + head.text + " " + head.tail, enList[i])
        #if(instance.text not in enList[i]):
        en = ""
        for word in sentence:
            en += word.text + " "


        #if (len(head.text.split())>1):
        #    head.text = "_".join(head.text.split())
        #    nen = context.text + head.text + head.tail
        #else:
        #    nen = en

        #print(head.text, nen.split())
        #index = nen.split().index(head.text)
        #print(head.text,en.split())
        #print(context.text + "#" + head.text + "#" + head.tail)
        try:
            index = en.split().index(instance.text)
        except:
            print(instance.text, en.split())
            print(en)
            print ("not exist")
            #exit()
        else:
            fa = normalizer.normalize(faList[i])
            faT = word_tokenize(fa)
            faG = tagger.tag(faT)
            #print(i , faList[i], faT)
            #alignments = myaligner.get_word_aligns(nen.split(), faT)
            #print(index , alignments["mwmf"])
            #faIndex = alignments["mwmf"][index][1]
            #faIndex = 0
            alignments = []
            x = aligns[i].replace("(", "")
            x = x.replace(")", "")
            for a in x.split("#"):
                if len(a.split(",")) > 1:
                    alignments.append((int(a.split(",")[0]), int(a.split(",")[1])))
            print(alignments)
            #alignments = myaligner.get_word_aligns(en.split(), faT)
            faIndex = 0

            for al in alignments:
                if index == al[0]:
                    faIndex = alignments[alignments.index(al)][1]
            #print(index, faIndex)
            if (faIndex>len(faT)-1 or faIndex>len(faG)-1 ):
                print("out")
                faIndex = random.randint(0, min(len(faT), len(faG))- 1)

            #print(index, faIndex)
            #print(lemmatizer.lemmatize(faT[faIndex]))
            oLexelt = ET.Element("lexelt")
            oLexelt.set("item", lemmatizer.lemmatize(faT[faIndex]).split("#")[0] +"." + faG[faIndex][1])
            #text =  oLexelt.attrib["item"].split(".")[0] + "." + oLexelt.attrib["item"].split(".")[1]+ " " + " ".join(keys[i].split()[1:])
            #print(text.split()[0].split(".")[0])
            #f.write(" ".join(text.split()[1:]) + "\n")
            #print(k)
            #f.write(oLexelt.attrib["item"].split(".")[0] + "." + oLexelt.attrib["item"].split(".")[1] + " " + keys[k] + "\n")
            f.write(keys[
                k] + "\n")
            oRoot.append(oLexelt)

            oInstance = ET.Element("instance")
            oInstance.set("id", instance.attrib["id"])
            oLexelt.append(oInstance)

            '''
            oAnswer = ET.Element("answer")
            oAnswer.set("instance", instance.attrib["id"])
            oAnswer.set("sensekey", keys[k].split()[-1])
            oInstance.append(oAnswer)
            '''

            oContext = ET.Element("context")
            text = ""
            for j in range(faIndex):
                text += faT[j] + "/" + lemmatizer.lemmatize(faT[j]).split("#")[0] + "/" + faG[j][1] + " "
            oContext.text = text
            oInstance.append(oContext)

            oHead = ET.Element("head")
            oHead.text = faT[faIndex] + "/" + lemmatizer.lemmatize(faT[faIndex]).split("#")[0] + "/" + faG[faIndex][1]
            text = ""
            for j in range(faIndex + 1, len(faT)):
                text += faT[j] + "/" + lemmatizer.lemmatize(faT[j]).split("#")[0] + "/" + faG[j][1] + " "
            oHead.tail = text
            oContext.append(oHead)

        k += 1

    i += 1

f.close()
xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + outputFileName, "w") as f:
    f.write(xmlstr)




