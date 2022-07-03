# Imports
from __future__ import unicode_literals
import xml.etree.ElementTree as ET
from xml.dom import minidom
from hazm import *
from simalign import SentenceAligner
from difflib import SequenceMatcher

normalizer = Normalizer()
lemmatizer = Lemmatizer()
tagger = POSTagger(model='resources/postagger.model')
tagDic = {"V":"Verb", "N":"NOUN", "ADV":"ADV", "Ne":"NOUN"}
# making an instance of our model.
# You can specify the embedding model and all alignment settings in the constructor.
myaligner = SentenceAligner(model="bert", token_type="bpe", matching_methods="m")

inputFileName = "ims_train.xml"
outputFileName = "fa_train.xml"
translatedFileName = "fa_texted_train.txt"
normalizedFileName = "normalized_texted_train.txt"
inputKeyFileName = "train_key.txt"
outputKeyFileName = "fa_train_key.txt"

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
f = open("../Data/" + outputKeyFileName, "w")

i = 0
en = ""
k = 0
for lexelt in root:
    for instance in lexelt:
        for context in instance:
            for head in context:
                if (i == 3498):
                    break
                print(i)
                if (len(head.text.split())>1):
                    head.text = "_".join(head.text.split())
                #pen = en

                en = enList[i]
                print("mohem", head.text, en.split() )
                #if (" ".join(pen.split()) != " ".join(en.split())):
                s = SequenceMatcher(None, context.text + " " + head.text + " " + head.tail, enList[i])
                if(s.ratio()<0.5):
                    #print(" ".join(pen.split()) + "#" + " ".join(en.split()))
                    i += 1
                    en = enList[i]


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
                    index = en.split().index(head.text)
                except:
                    print(head.text, en.split())
                    print(context.text + "#" + head.text + "#" + head.tail)
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
                    alignments = myaligner.get_word_aligns(en.split(), faT)
                    for al in alignments["mwmf"]:
                        if index == al[0]:
                            faIndex = alignments["mwmf"][alignments["mwmf"].index(al)][1]



                    oLexelt = ET.Element("lexelt")
                    oLexelt.set("item", lemmatizer.lemmatize(faT[faIndex]).split("#")[0] +"." + faG[faIndex][1])
                    #text =  oLexelt.attrib["item"].split(".")[0] + "." + oLexelt.attrib["item"].split(".")[1]+ " " + " ".join(keys[i].split()[1:])
                    #print(text.split()[0].split(".")[0])
                    #f.write(" ".join(text.split()[1:]) + "\n")
                    f.write(oLexelt.attrib["item"].split(".")[0] + "." + oLexelt.attrib["item"].split(".")[1] + " " + " ".join(keys[k].split()[1:]) + "\n")
                    oRoot.append(oLexelt)

                    oInstance = ET.Element("instance")
                    oInstance.set("id", instance.attrib["id"])
                    oLexelt.append(oInstance)

                    oAnswer = ET.Element("answer")
                    oAnswer.set("instance", instance.attrib["id"])
                    oAnswer.set("sensekey", keys[k].split()[-1])
                    oInstance.append(oAnswer)

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
''' 
for text in root:
    for sentence in text:
        for instance in sentence.findall("instance"):
            print(instance.attrib["id"])
            listOfInstancesPOS.append(instance.attrib["pos"])
            # lexelt tag in output
            oLexelt = ET.Element("lexelt")
            oLexelt.set("item", instance.attrib["lemma"] + "." + instance.attrib["pos"])
            oLexelt.set("pos", instance.attrib["pos"])
            oRoot.append(oLexelt)
            # Instance tag in the output
            oInstance = ET.Element("instance")
            # oInstance.set("docsrc", text.attrib["source"])
            oInstance.set("id", instance.attrib["id"])

            oLexelt.append(oInstance)
            # Context tag in the output
            oContext = ET.Element("context")
            oTextBeforeHead = ""
            for word in sentence:
                if (word.tag == "instance" and word.attrib["id"] == instance.attrib["id"]):
                    break
                oTextBeforeHead += word.text + " "
            oContext.text = oTextBeforeHead
            oInstance.append(oContext)
            # Head tag in the output
            oHead = ET.Element("head")
            oHead.text = instance.text
            oTextAfterHead = ""
            instanceIsSeen = False
            for word in sentence:
                if instanceIsSeen:
                    oTextAfterHead += word.text + " "
                if (word.tag == "instance" and word.attrib["id"] == instance.attrib["id"]):
                    instanceIsSeen = True

            oHead.tail = oTextAfterHead
            oContext.append(oHead)
            # ET.indent(oContext, space="\n")

# ET.indent(oTree, space="    ")
# oTree.write('./Data/' + output_filename + '.xml', encoding="UTF-8", xml_declaration=True)
'''
f.close()
xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + outputFileName, "w") as f:
    f.write(xmlstr)




