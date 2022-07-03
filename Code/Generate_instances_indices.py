import nltk as nl
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
lm = WordNetLemmatizer()

inputFileName = "English 120k.txt"
faInputFileName = "Persian 120k.txt"
outIndexFileName = "en_bitext_instances_index.txt"
faOutIndexFileName = "fa_bitext_instances_index.txt"
alignFileName = "aligned_bitext.txt"

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



enList = []
with open("../Data/" + inputFileName, "r") as f:
    enList = f.read().splitlines()

faList = []
with open("../Data/" + faInputFileName, "r") as f:
    faList = f.read().splitlines()

alList = []
with open("../Data/" + alignFileName, "r") as f:
    alList = f.read().splitlines()

f1 = open("../Data/" + outIndexFileName, "w")
f2 = open("../Data/" + faOutIndexFileName, "w")

id = 0
line = 0
for l in enList:
    print(id)
    en = l
    enT = en.split()
    indices = ""
    faIndices = ""
    for k in range(len(enT)):
        if (len(enT[k])>1 and enT[k] not in stop_words):
            for m in alList[line].split("#"):
                if str(k) == m.split(",")[0].strip("("):
                    faIndex = int(m.split(",")[1].strip(")").strip())
                    faIndices += str(faIndex) + " "
                    indices += str(k) + " "
                    id += 1
                    break;
    if(len(indices.split()) != len(faIndices.split())):
        print("************")
    f1.write(indices +"\n")
    f2.write(faIndices + "\n")
    line += 1



