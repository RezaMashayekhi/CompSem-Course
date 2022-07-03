o = open ("Java/Babel/lemma_u.txt" ,"w")
with open("../../ims/All_words.txt", "r") as f:
    lines = f.read().splitlines()
    i = 0
    for l in lines:
        if(l.split(" ")[2] == "U"):
            o.write(l.split(" ")[1] + "#" + l.split(" ")[1].split(".")[0] + "\n")
        i += 1