inputFileName = "en_bitext_key.txt"
inputFileName2 = "fa_bitext_key.txt"
output = "multinet.txt"

with open ("Java/Babel/" + inputFileName,"r") as f:
    en = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    fa = f.read().splitlines()

f = open("Java/Babel/" + output, "w")

dic = {}

for l in en:
    synset = l.split()[1]
    if (synset!= "U" and l.split()[1] not in dic):
        dic[synset] = [[l.split()[0].split(".")[0]], []]
    elif (synset!= "U" and l.split()[1] in dic):
        dic[synset][0].append(l.split()[0].split(".")[0])

for l in fa:
    synset = l.split()[1]
    if (synset!= "U" and l.split()[1] not in dic):
        dic[synset] = [[],[l.split()[0].split(".")[0]]]
    elif (synset!= "U" and l.split()[1] in dic):
        dic[synset][1].append(l.split()[0].split(".")[0])
'''
for i in dic:
    f.write(i + "\t" + str(dic[i][0]) + "\t" + str(dic[i][1]) + "\n")
'''
for i in dic:
    s = i + "\t"
    se = set()
    for j in dic[i][0]:
        se.add(j)
    for j in se:
        s += j + ","
    if (len(se)==0):
        s += "_NONE_"
        
    s += "\t"
    se = set()
    for j in dic[i][1]:
        se.add(j)
    for j in se:
        s += j + ","
    if (len(se)==0):
        s += "_NONE_"
    f.write(s + "\n")
f.close()