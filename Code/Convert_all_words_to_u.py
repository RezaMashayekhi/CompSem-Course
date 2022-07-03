s=""
with open("../../ims/All_words.txt", "r") as f:
    lines = f.read().splitlines()
    i = 0
    for l in lines:
        s += " " + l.split(" ")[1] + " " + "U" + "\n"

print(s)
o = open ("../../ims/All_words.txt" ,"w")
o.write(s)
o.close()