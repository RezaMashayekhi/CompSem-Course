# Computational-Semantic-Course

Created a bilingual wordnet by doing parallel WSD.

BabelNet is a multilingual wordnet that has senses of words and their lemmas in different languages. 
In this project, we tried to create a bilingual (English-Persian) wordnet. We did WSD on both sides of bitext and aligned them. This gives us a bilingual wordnet.

However, doing WSD in Persian is not as easy as doing WSD in English since there are not many resources for Persian like English. Therefore, we had to 
create silver training dataset for Persian. For creating the Persian silver dataset, we translated the gold sense-annotated English dataset to Persian, then aligned them, and finally projected senses from English to Persian (translation is done only on the text of the English dataset not its senses).

| Data | Lexemes | 
| ------------- | ------------- | 
| WordNet  | 288024 | 
| Creeated dataset  | 10612 |

Since we only translated a small part of the English training dataset (Due to the price of translation and the time it takes for large texts), the generated Persian training dataseet is small and doesn't cover many of the senses in WordNet. 
The purpose of the project was learning the process and creating the bilingual WordNet and the low F1 due to lack of resources was not a concern.

Team members: Reza Mashayekhi and Mehrdad Yousefpoori Naeim 
