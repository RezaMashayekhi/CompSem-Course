inputFileName = "babelnet.txt"
inputFileName2 = "wordnet.txt"
output = "final_wordnet.txt"


with open ("Java/Babel/" + inputFileName,"r") as f:
    en = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    fa = f.read().splitlines()


f = open("Java/Babel/" + output, "w")

dic = {}
j = 0
for l in en:
    synset = l.split("\t")[0].lower()
    dic[synset] = [[],[]]
    if (len(l.split("\t"))>1):
        lemmas = l.split("\t")[1].split(",")
        for j in lemmas:
            if (len(j) > 1):
                dic[synset][0].append(j)
    else:
        #print(synset)
        dic["10000000n"] = l.split(",")[5]
    #print(l)
    #print(dic[synset])

for l in fa:
    synset = l.split("\t")[0][3:]
    if (synset in dic):
        if (len(l.split("\t")) == 3):
            lemmas = l.split("\t")[2].split(",")
            for j in lemmas:
                if (len(j) > 1):
                    dic[synset][1].append(j)

for k in sorted(dic):
    s = k + "\t"
    for j in dic[k][0]:
        s += j + ","

    s += "\t"
    se = set()
    for j in dic[k][1]:
        se.add(j)
    for j in se:
        s += j + ","
    if (len(se) == 0):
        s += "_NONE_"
    f.write(s + "\n")
f.close()