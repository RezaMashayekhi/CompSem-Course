inputFileName = "All_words.txt"
outputFileName = "wn_senses.txt"
with open ("../../ims/" + inputFileName,"r") as f:
    lines = f.read().splitlines()
with open ("../Data/index.sense.txt", "r") as f:
    index = f.read().splitlines()

f = open ("Java/Babel/" + outputFileName,"w")

dic = {}
for line in index:
        #if(line.split("%")[0] in dic):
        dic[line.split()[0]] = line.split()[1]

# ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
#1    NOUN
#2    VERB
#3    ADJECTIVE
#4    ADVERB
#5    ADJECTIVE SATELLITE
pos = {"1":"n", "2":"v", "3":"a", "4":"r", "5":"a"}

for i in range(len(lines)):
    print(lines[i])
    if (lines[i].split()[1] != "U"):
        lines[i] = lines[i].split()[0] + " " +"wn:" + dic[lines[i].split()[1]] + pos[lines[i].split()[1].split("%")[1][0]]
    f.write(lines[i] + "\n")
f.close()
