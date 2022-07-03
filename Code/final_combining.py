inputFileName = "bn_senses.txt"
inputFileName2 = "u_to_bn.txt"
output = "en_gold_key_gen.txt"

with open ("Java/Babel/" + inputFileName,"r") as f:
    wl = f.read().splitlines()
with open ("Java/Babel/" + inputFileName2 , "r") as f:
    ul = f.read().splitlines()

f = open("Java/Babel/" +output, "w")

for w in wl:
    if (w.split()[1] == "U"):
        flag = 0
        for u in ul:
            if (u.split("#")[0] == w.split()[0] and u.split("#")[2] != "U"):
                f.write(w.split()[0] + " " + u.split("#")[2] + "\n")
                flag = 1
                break
        if (flag == 0):
            f.write(w.split()[0] + " " + "U" + "\n")
    else:
        f.write(w + "\n")


