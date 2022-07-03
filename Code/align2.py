
import xml.etree.ElementTree as ET
from xml.dom import minidom
from hazm import *
from simalign import SentenceAligner

# making an instance of our model.
# You can specify the embedding model and all alignment settings in the constructor.
myaligner = SentenceAligner(model="bert", token_type="bpe", matching_methods="m")

inputFileName = "texted_train.txt"
translatedFileName = "fa_texted_gold.txt"
outputFileName = "aligned_gold.txt"

faList = []
enList = []
with open("../Data/" + inputFileName, "r") as f:
    enList = f.read().splitlines()
with open("../Data/" + translatedFileName, "r") as f:
    faList = f.read().splitlines()

enList = enList[4000:5000]

f = open("../Data/" + outputFileName, "w")

for i in range(len(enList)):
    print(i)
    en = enList[i]
    fa = faList[i]
# The output is a dictionary with different matching methods.
# Each method has a list of pairs indicating the indexes of aligned words (The alignments are zero-indexed).
    alignments = myaligner.get_word_aligns(en.split(), word_tokenize(fa))
    a = alignments["mwmf"]
    s = ""
    for i in a:
        s += str(i) + "#"
    f.write(s + "\n")


