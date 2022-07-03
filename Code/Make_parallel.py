with open ("../Data/fa_texted_train.txt", "r") as f:
    fa = f.read().splitlines()
with open ("../Data/texted_train.txt", "r") as f:
    en = f.read().splitlines()
with open ("../Data/parallel.txt", "w") as f:
    for i in range(len(fa)):
        f.write(en[i] + " ||| " + fa[i] + "\n")

