from csv_operation import csv_reader
from sentiment import anlaysis


data2020 = csv_reader("2020file.csv", "data")
print(data2020[0], "#" * 10, data2020[1], "#" * 10, " \n", data2020[2])

print("-*-" * 10)
data2019 = csv_reader("2019file.csv", "data")
print(data2019[0], "#" * 10, data2019[1], "#" * 10, " \n", data2019[2])


print("-" * 10, "tweets:")
print(data2020[1][10], "\n", "#" * 10, "\n", data2019[1][10])


print("\n1. Heat comparison")
print(len(data2020), " VS ", len(data2019))

data2020full = csv_reader("2020_total_file.csv", "data")

print("\n2. sentiment anlaysis")
total_sentiment = 0

num_positive = 0
num_neural = 0
num_nagtive = 0

unwanted_chars = ".,-_ ()’"
wordfreq = {}
usernamefreq = {}

split = 101
pick_twlist = data2020full[0::split]
for tw in pick_twlist:
    text = tw[10]
    username = tw[8]
    print(text, "\n@@@username=", username, "\n")
    words, sentiment_tw = anlaysis(text)
    print(sentiment_tw)
    total_sentiment += sentiment_tw
    if sentiment_tw < 0:
        num_nagtive += 1
    if sentiment_tw == 0:
        num_neural += 1
    if sentiment_tw > 0:
        num_positive += 1
    # print('words=', words)
    for raw_word in words:
        word = raw_word.strip(unwanted_chars)
        if word not in wordfreq:
            wordfreq[word] = 0
        wordfreq[word] += 1

    if username not in usernamefreq:
        usernamefreq[username] = 0
    usernamefreq[username] += 1

print("tatal sentiment polarity:", total_sentiment)
print("everaget sentiment polarity:", total_sentiment / len(pick_twlist))
print(
    "number of (positive VS neural VS nagtive):",
    num_positive * split,
    num_neural * split,
    num_nagtive * split,
)

print("\n 3. related words related to this topic")
# print(wordfreq)
a1_sorted_keys = sorted(wordfreq, key=wordfreq.get, reverse=True)
for r in a1_sorted_keys:
    if wordfreq[r] > 1:
        print(r, wordfreq[r])

print("\n 4. username often posts related topics")
a2_sorted_keys = sorted(usernamefreq, key=usernamefreq.get, reverse=True)
for r in a2_sorted_keys:
    if usernamefreq[r] > 1:
        print(r, usernamefreq[r])
