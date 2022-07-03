from nltk.corpus import wordnet as wn
print(wn.synsets("football")[1].offset())
print(wn.synset_from_pos_and_offset('n', 3378765))

#print(wn.of2ss('00044946v'))