import requests
import json
url = "https://nlp-translation.p.rapidapi.com/v1/translate"

headers = {
    'x-rapidapi-host': "nlp-translation.p.rapidapi.com",
    'x-rapidapi-key': "b1b5111fb0msh6acd29cc9144014p14cf7ajsn25fabecfd115"
    }

text = ""
s = ""
b = ""
lines = []
with open("../Data/texted_train.txt", "r") as f:
    lines = f.read().splitlines()

with open("../Data/normalized_texted_train.txt", "w") as f:
    for l in lines:
        s = ""
        for w in l.split():
            if(len(w) == 1 and w not in [".", ",", "?"] and not w.isalpha() or w in ["``", "\"\"", "\'\'"]):
                s = s
            else:
                s += w + " "
        f.write(s + "\n")

with open("../Data/normalized_texted_train.txt", "r") as f:
    lines = f.read().splitlines()

s = ""
nofr = 0
i = 0

for l in lines[4000:]:
    if (i == 1000):
        break
    text = l
    #print(l)
    #if (len(text) + len(l) + 2 >=1000):
    querystring = {"text": text, "to": "fa", "from": "en"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    d = json.loads(response.text)
    #print(response.text)
    #print(d["translated_text"]["fa"].split("."))
    s += d["translated_text"]["fa"] + "\n"
    nofr += 1
    print (i, nofr)
    #text = ""

    #text += l + " . "

    i += 1
'''
if len(text)>5:
    print(i)
    querystring = {"text": text, "to": "fa", "from": "en"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    d = json.loads(response.text)

    s += d["translated_text"]["fa"]
'''

with open("../Data/fa_texted_gold.txt", "w") as f:
    #for l in s.split("."):
    #    f.write(l+"\n")
    #print(s)
    f.write(s)



'''
text = "Chicago was also a welcome host : there , in 1921 , Prokofieff conducted the world_premiere of the Love for Three Oranges , and played the first performance of his Third Piano Concerto . # `` Uncle_Sam '' was , indeed , a rich uncle to Prokofieff , in those opulent , post-war victory years of peace and prosperity , bold speculations and extravaganzas , enjoyment and pleasure : `` The Golden Twenties '' . # We attended the premieres of his concertos , symphonies , and suites ; we studied , taught , and performed his piano_sonatas , chamber_music , gavottes , and marches ; we bought his records and played them in our schools and universities ."

querystring = {"text":text,"to":"fa","from":"en"}
response = requests.request("GET", url, headers=headers, params=querystring)

d = json.loads(response.text)
s = d["translated_text"]["fa"]

with open("../Data/translated.txt", "w") as f:
    for l in s.split("#"):
        f.write(l+"\n")
'''
