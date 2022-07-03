import os

directory = os.fsencode("../../ims/Results/")

with open("../../ims/All_words.txt", "w") as f:

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #print(filename)
        if (filename != ".DS_Store"):
            ff = open("../../ims/Results/" + filename, "r")
            for l in ff.read().splitlines():
                print(l.split()[0].split(".")[0])
                f.write(l + "\n")



