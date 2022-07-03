# Assignment 1 of CMPUT600 2021. This code formats the xml file for IMS.
# Team members: Reza Mashayekhi, Mehrad

# Imports
import shutil
import xml.etree.ElementTree as ET
from xml.dom import minidom     # Pretifies xml

# Part 1: Modifying the data.xml
#
#
# Reading the xml file
xml_filename = "en_gold.xml"
output_filename = "en_gold_ims"
input_key = "en_gold_key"


tree = ET.parse('../Data/' + xml_filename)
root = tree.getroot()

# Copying the xml file to the output
'''
shutil.copy('../Data/' + xml_filename, '../Data/'+ output_filename + '.xml')
oTree = ET.parse('../Data/' + output_filename + '.xml')
oRoot = oTree.getroot()


# Removing all children of root which are "text"
for oChild in oRoot.findall("text"):
    oRoot.remove(oChild)
'''
oRoot = ET.Element("corpus")

# Modifying the corpus tag
oRoot.set("lang", "english")
#del oRoot.attrib["source"]

listOfInstancesPOS = []
for sentence in root:
    for instance in sentence.findall("instance"):
        print(instance.attrib["id"])
        listOfInstancesPOS.append(instance.attrib["pos"])
        # lexelt tag in output
        oLexelt = ET.Element("lexelt")
        oLexelt.set("item", instance.attrib["lemma"]+"."+instance.attrib["pos"])
        oLexelt.set("pos", instance.attrib["pos"])
        oRoot.append(oLexelt)
        # Instance tag in the output
        oInstance = ET.Element("instance")
        #oInstance.set("docsrc", text.attrib["source"])
        oInstance.set("id", instance.attrib["id"])

        oLexelt.append(oInstance)
        # Context tag in the output
        oContext = ET.Element("context")
        oTextBeforeHead = ""
        for word in sentence:
            if(word.tag == "instance" and word.attrib["id"] == instance.attrib["id"]):
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


        oHead.tail =oTextAfterHead
        oContext.append(oHead)
        #ET.indent(oContext, space="\n")

#ET.indent(oTree, space="    ")
#oTree.write('./Data/' + output_filename + '.xml', encoding="UTF-8", xml_declaration=True)

xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + output_filename + ".xml", "w") as f:
    f.write(xmlstr)


# Part 2: Modifying the key file
#
#
lines = []
with open("../Data/" + input_key + ".txt", "r") as f:
    lines = f.read().splitlines()

print(root.findall("instance"))
with open("../Data/" +input_key + "_ims.txt", "w") as f:
    counter = 0
    for line in lines:
        line = line.split()[1].split("%")[0] + "." + listOfInstancesPOS[counter] + " " + line
        f.write(line + "\n")
        counter += 1
        print(counter)
