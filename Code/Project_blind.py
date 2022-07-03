inputFileName = "en_blind_test_key.txt"
inputFileName2 = "fa_blind_test_key.txt"
output = "fa_blind_test_key_proj.txt"

with open ("Java/Babel/" + inputFileName,"r") as f:
    en = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    fa = f.read().splitlines()

f = open("Java/Babel/" + output, "w")

for l in fa:
    id = l.split()[0].split(".")[2]
    for j in en:
        if j.split()[0].split(".")[2] == id:
            f.write(l.split()[0] + " " + j.split()[1] + "\n")

f.close()