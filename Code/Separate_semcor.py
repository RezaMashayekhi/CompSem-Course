# Imports
import shutil
import xml.etree.ElementTree as ET
from xml.dom import minidom  # Pretifies xml

# Part 1: Modifying the data.xml
#
#
# Reading the xml file
xml_filename = "train.xml"
output_filename = "s_train"
output_gold_filename = "en_gold"
input_key_file = "train.semcor.senses.txt"

tree = ET.parse('../Data/' + xml_filename)
root = tree.getroot()

# Copying the xml file to the output
shutil.copy('../Data/' + xml_filename, '../Data/' + output_filename + '.xml')
oTree = ET.parse('../Data/' + output_filename + '.xml')
oRoot = oTree.getroot()

# Removing all children of root which are "text"
for oChild in oRoot.findall("text"):
    oRoot.remove(oChild)

# Modifying the corpus tag
oRoot.set("lang", "english")
del oRoot.attrib["source"]

ogoldRoot = ET.Element("corpus")
ogoldRoot.set("lang", "persian")

with open ("../Data/" + input_key_file,"r") as f:
    keys = f.read().splitlines()

f1 = open("../Data/" + output_filename + "_key.txt","w")
f2 = open("../Data/" + output_gold_filename + "_key.txt","w")

id = 0
line = 0
for text in root:
    for sentence in text:
        print(line)
        if(line<4000 or line>=5000):
            oRoot.append(sentence)
            for instance in sentence.findall("instance"):
                f1.write(keys[id] + "\n")
                id +=1
        else:
            ogoldRoot.append(sentence)
            for instance in sentence.findall("instance"):
                f2.write(keys[id] + "\n")
                id +=1

        line += 1
# ET.indent(oTree, space="    ")
# oTree.write('./Data/' + output_filename + '.xml', encoding="UTF-8", xml_declaration=True)
f1.close()
f2.close()
xmlstr = minidom.parseString(ET.tostring(oRoot)).toprettyxml(indent="    ")
with open("../Data/" + output_filename + ".xml", "w") as f:
    f.write(xmlstr)

xmlstr = minidom.parseString(ET.tostring(ogoldRoot)).toprettyxml(indent="    ")
with open("../Data/" + output_gold_filename + ".xml", "w") as f:
    f.write(xmlstr)