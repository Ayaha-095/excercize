import re
from collections import Counter

from soupsieve.util import lower

all_words = []
with open('sample.txt', 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        line = line.replace('’', "'")
        pattern = r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?\b"
        s1 = re.findall(pattern, line)
        # if 'n' in s1:
        #     s1.remove('n')
        s1 = [word.lower() for word in s1]
        all_words.extend(s1)
all_words = sorted(all_words)
count = Counter(all_words)
word_dict = [{'単語': word, '回数': count} for word, count in count.items()]

with open('sample_word_count.txt', 'w', encoding='utf-8') as f:
    for i in word_dict:
        f.write(f"単語：{i['単語']},回数：{i['回数']}\n")
print(word_dict)
