inputFileName = "English_blind_annotated.txt"
inputFileName2 = "Persian_blind_annotated.txt"
key_name = "en_blind_test_key.txt"
key2_name = "fa_blind_test_key.txt"

output = "en_blind_gold.txt"
output2 ="fa_blind_gold.txt"

with open ("../Output/Bitext/Blind_Sample/Annotated/" + inputFileName,"r") as f:
    en = f.read().splitlines()

with open ("../Output/Bitext/Blind_Sample/Annotated/" + inputFileName2 , "r") as f:
    fa = f.read().splitlines()

with open ("Java/Babel/" + key_name,"r") as f:
    key = f.read().splitlines()
with open ("Java/Babel/" + key2_name,"r") as f:
    key2 = f.read().splitlines()

f1 = open("Java/Babel/" + output, "w")
f2 = open("Java/Babel/" + output2, "w")

for k in key:
    line_n = int(k.split()[0].split(".")[2])
    f1.write(k.split()[0] + " " + en[line_n].split("#")[2] + "\n")

f1.close()

for k in key2:
    line_n = int(k.split()[0].split(".")[2])
    if(fa[line_n].split("#")[2] != ""):
        f2.write(k.split()[0] + " " + fa[line_n].split("#")[2] + "\n")
    print(fa[line_n].split("#")[0])
f2.close()