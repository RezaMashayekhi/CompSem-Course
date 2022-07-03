inputFileName = "en_blind_test_key.txt"
inputFileName2 = "English_blind_annotated.txt"
output = "en_blind_gold.txt"

with open ("Java/Babel/" + inputFileName,"r") as f:
    ge = f.read().splitlines()
with open ("../Output/Bitext/Blind_Sample/Annotated/" + inputFileName2 , "r") as f:
    go = f.read().splitlines()

f = open("/Users/reza/Documents/University/Grad/CompSem/Assignments/1/Data/" + output, "w")
for l in ge:
    id = l.split()[0]
    f.write(id + " " + go[int(id.split(".")[2])].split("#")[2] + "\n")
f.close()