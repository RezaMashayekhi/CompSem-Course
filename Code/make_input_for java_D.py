o = open ("Java/Babel/lemma_u_d.txt" ,"w")
with open("Java/Babel/fa_blind_test_key_proj.txt", "r") as f:
    lines = f.read().splitlines()
    i = 0
    for l in lines:
        o.write(l.split(" ")[0].split(".")[0] + "#" + l.split(" ")[1] + "\n")
        i += 1