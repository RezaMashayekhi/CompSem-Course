inputFileName = "fa_blind_test_key_proj.txt"
inputFileName2 = "fa_blind_test_key_proj_f.txt"


with open ("Java/Babel/" + inputFileName,"r") as f:
    id = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    lemma = f.read().splitlines()


s =""
for i in range(len(id)):
    s += id[i].split()[0] + " " + lemma[i].split()[1] + "\n"

print(s)
f = open("Java/Babel/" +inputFileName2, "w")
f.write(s)
f.close()


