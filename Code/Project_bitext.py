'''
inputFileName = "new_en_bitext_key.txt"
inputFileName2 = "new_fa_bitext_key.txt"
output = "fa_bitext_key_proj.txt"

with open ("Java/Babel/" + inputFileName,"r") as f:
    en = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    fa = f.read().splitlines()

f = open("Java/Babel/" + output, "w")

dic = {}


for l in en:
    id = l.split()[0].split(".")[-1]
    dic[id] = l
    #print(id)

for l in fa:
    id = l.split()[0].split(".")[-1]
    #print( "    " + id)
    j = dic[id]
    f.write(l.split()[0] + " " + j.split()[1] + "\n")
'''

inputFileName = "en_gold_key_gen.txt"
inputFileName2 = "fa_gold_key_gen.txt"
output = "fa_gold_key_proj.txt"

with open ("Java/Babel/" + inputFileName,"r") as f:
    en = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    fa = f.read().splitlines()

f = open("Java/Babel/" + output, "w")

dic = {}


for l in en:
    id = l.split()[0]
    dic[id] = l
    #print(id)

for l in fa:
    id = l.split()[0]
    #print( "    " + id)
    j = dic[id]
    f.write(l.split()[0] + " " + j.split()[1] + "\n")

f.close()