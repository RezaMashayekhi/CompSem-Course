# Assignment 2 of CMPUT600 2022
# Team members: Reza, Mehrdad

# Imports
import xml.etree.ElementTree as ET

# Reading the xml file
tree = ET.parse('../Data/train.semcor.xml')
root = tree.getroot()

s = ""
for text in root:
    for sentence in text:
        for word in sentence:
            w = word.text
            if " " in word.text:
                w = "_".join(word.text.split())
            s += w + " "
        s += "\n"

print(s)
with open("../Data/texted_train.txt", "w") as f:
    f.write(s)

