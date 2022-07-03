inputFileName = "new_fa_bitext_key.txt"
inputFileName2 = "fa_bitext_key_proj.txt"

with open ("Java/Babel/" + inputFileName,"r") as f:
    en = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    fa = f.read().splitlines()

u = 0
dic = {}
for l in en:
    id = l.split()[0].split(".")[-1]
    dic[id] = l
    if (l.split()[1] == "U"):
        u += 1
print(len(dic) - u)

u = 0
s = 0
for l in fa:
    id = l.split()[0].split(".")[-1]
    if (l.split()[1] == dic[id].split()[1]):
        s += 1
    if (l.split()[1] == "U"):
        u += 1
print(len(dic) - u)
print(s)

