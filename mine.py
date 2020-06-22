import os
import spacy
import numpy as np
import matplotlib.pyplot as plt

from googletrans import Translator
tl = Translator()

pos = ['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SPACE', 'SYM', 'VERB', 'X', '']
realName = ['adjective', 'adposition', 'adverb', 'auxiliary verb', 'coordinating conjunction', 'determiner', 'interjection', 'noun', 'numeral', 'particle', 'pronoun', 'proper noun', 'punctuation', 'subordinating conjunction', 'space', 'symbol', 'verb', 'other', 'unknown']
vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

data = dict(zip(pos, vals))

print("Loading NLP package.")
nlpFR = spacy.load("fr_core_news_sm")
nlpEN = spacy.load("en_core_web_sm")
print("NLP package loaded.\n")

def read(fileName):
    print("\nReading file.")
    with open(fileName, 'r') as file:
        read = file.read().replace('\n', '')
    print("File read.\n")
    return read

def process(text, nlp):
    print("Processing text.")
    doc = nlp(text)
    for token in doc:
        cur = token.pos_
        name = token.text
        data[cur] += 1
    print("Text processed.\n")

    return dict(zip(realName, data.values()))

def display(present, language):
    y_pos = np.arange(len(present.keys()))
    plt.style.use('dark_background')
    plt.bar(y_pos, present.values(), align='center', alpha=0.5)
    plt.xticks(y_pos, present.keys(), rotation=60)
    plt.ylabel('Instances')
    plt.title(str(language) + ' Part of Speech Usage')
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    plt.tight_layout(pad = 1)
    plt.show()


englishVersion = read('littlePrince.txt')
frenchVersion = read('petitPrince.txt')
english = process(englishVersion, nlpEN)
french = process(frenchVersion, nlpFR)

artificial = ""

splitFrench = frenchVersion.split()
currentString = ""

for i in range(0, len(splitFrench)):
    if len(currentString) + len(splitFrench[i]) < 5000:
        currentString += " " + splitFrench[i]
    else:
        artificial += tl.translate(currentString, dest = 'en', src = 'fr').text
        currentString = ""
artificial += tl.translate(currentString, dest = 'en', src = 'fr').text
print(artificial)


display(english, "English")
display(french, "French")

artificial = process(artificial, nlpEN)
display(artificial, "Artificial")






# file = open("all.txt", "r")
#
# contents = f.readlines()
#
# all = []
#
#
#
# for line in contents:
#     stuff = line.split("|")
#     if (len(stuff) == 4):
#
#         if stuff[0] == "1":
#             stuff[0] = True
#         else:
#             stuff[0] = False
#         stuff[1] = re.sub('^[\w]*;.;', '', stuff[1])
#
#         stuff[2] = pd.to_datetime(stuff[2])
#
#         stuff[3] = re.sub('\n$', '', stuff[3])
#         all.append(stuff)
#
# print("Parsing Done")
#
# df = pd.DataFrame(all, columns=['fromMe', 'name', 'date', 'text'])
#
# df = df.astype({'name': 'string'}).astype({'text': 'string'})
#
# df.drop_duplicates(subset=['fromMe', 'date', 'text'], inplace=True)
# subset = df[df['text'].str.contains("dog|Dog")]
#
# subset.groupby(subset["date"].dt.dayofyear)['date'].count().plot(kind="bar", title="Messages by Day", legend=False)
# plt.xlabel("Day of Year")
# plt.ylabel("# of Messages")
# plt.show()
#
# subset.groupby(subset["date"].dt.day)['date'].count().plot(kind="bar", title="Messages by Day of Month", legend=False)
# plt.xlabel("Day of Month")
# plt.ylabel("# of Messages")
# plt.show()
#
# subset.groupby(subset["date"].dt.dayofweek)['date'].count().plot(kind="bar", title="Messages by Day of Week", legend=False)
# plt.xlabel("Day of Week")
# plt.ylabel("# of Messages")
# plt.show()
#
# subset.groupby(subset["date"].dt.hour)['date'].count().plot(kind="bar", title="Messages by Hour", legend=False)
# plt.xlabel("Hour of Day")
# plt.ylabel("# of Messages")
# plt.show()
#
# subset.groupby(subset["date"].dt.minute)['date'].count().plot(kind="bar", title="Messages by Minute", legend=False)
# plt.xlabel("Minute of Hour")
# plt.ylabel("# of Messages")
# plt.show()
