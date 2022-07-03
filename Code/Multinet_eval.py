import random

inputFileName = "babelnet.txt"
inputFileName2 = "wordnet.txt"
output1 = "wn_gold_s.txt"
output2 = "wn_gen_s.txt"

with open ("Java/Babel/" + inputFileName,"r") as f:
    en = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    fa = f.read().splitlines()

f1 = open("Java/Babel/" + output1, "w")
f2 = open("Java/Babel/" + output2, "w")

'''
for i in en:
    print(i.split("\t"))
    sense = i.split("\t")[0].lower()
    if(len(i.split("\t")) == 3):
        lemmas = i.split("\t")[2].split(",")
        for j in lemmas:
            if(len(j)>1):
                print(j +"." + sense + " " + sense + "\n")
                #print(j)
                f1.write(j +"." + sense + " " + sense + "\n")
    #else:
        #print("*******")
f1.close()

for i in fa:
    print(i.split("\t"))
    sense = i.split("\t")[0][3:]
    if(len(i.split("\t")) == 3):
        lemmas = i.split("\t")[2].split(",")
        for j in lemmas:
            if(len(j)>1):
                print(j +"." + sense + " " + sense + "\n")
                #print(j)
                f2.write(j +"." + sense + " " + sense + "\n")
    #else:
        #print("*******")
f2.close()
'''


# Sample
dic = {}

for l in en:
    synset = l.split("\t")[0].lower()
    dic[synset] = [[],[]]
    if(len(l.split("\t"))==3):
        lemmas = l.split("\t")[2].split(",")
        for j in lemmas:
            if (len(j) > 1):
                dic[synset][0].append(j)


for l in fa:
    synset = l.split("\t")[0][3:]
    if(len(l.split("\t"))==3):
        lemmas = l.split("\t")[2].split(",")
        for j in lemmas:

            if ((len(j) > 1) and (synset in dic)):
                dic[synset][1].append(j)

keys = list(dic.keys())
for i in range(50):
    r = random.randint(0, len(keys)-1)
    r = keys[r]
    for j in dic[r][0]:
        f1.write(j + "." + r + " " + r + "\n")
    for j in dic[r][1]:
        f2.write(j + "." + r + " " + r + "\n")

f1.close()
f2.close()