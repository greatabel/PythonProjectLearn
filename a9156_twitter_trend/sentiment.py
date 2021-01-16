from textblob import TextBlob


def anlaysis(text):
    total = 0
    blob = TextBlob(text)
    blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                        #  ('threat', 'NN'), ('of', 'IN'), ...]

    blob.noun_phrases   # WordList(['titular threat', 'blob',
                        #            'ultimate movie monster',
                        #            'amoeba-like mass', ...])

    for sentence in blob.sentences:
        # print(sentence.sentiment.polarity)
        total += sentence.sentiment.polarity
    return total