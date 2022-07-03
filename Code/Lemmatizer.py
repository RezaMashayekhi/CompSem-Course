from __future__ import unicode_literals
from hazm import *

normalizer = Normalizer()
print(normalizer.normalize('اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند'))

print(word_tokenize('ولی برای پردازش، جدا بهتر نیست؟'))
lemmatizer = Lemmatizer()
print(lemmatizer.lemmatize('می‌روم'))
'رفت#رو'

tagger = POSTagger(model='resources/postagger.model')
l = tagger.tag(word_tokenize('ما بسیار کتاب می‌خوانیم'))
