from csv_operation import csv_reader
from sentiment import anlaysis


data2020 = csv_reader("2020file.csv", "data")
print(data2020[0], "#" * 10, data2020[1], "#" * 10, " \n", data2020[2])

print("-*-" * 10)
data2019 = csv_reader("2019file.csv", "data")
print(data2019[0], "#" * 10, data2019[1], "#" * 10, " \n", data2019[2])

print('-'*10, 'tweets:')
print(data2020[1][10], '\n', '#'*10, '\n', data2019[1][10])


print("1. Heat comparison")
print(len(data2020), " VS ", len(data2019))


print('2. sentiment anlaysis')
total_sentiment = 0

num_positive = 0
num_neural = 0
num_nagtive = 0

pick_twlist = data2020[0::10]
for tw in pick_twlist:
    text = tw[10]
    print(text, '\n')
    sentiment_tw = anlaysis(text)
    print(sentiment_tw)
    total_sentiment += sentiment_tw
    if sentiment_tw < 0:
        num_nagtive += 1
    if sentiment_tw == 0:
        num_neural += 1
    if sentiment_tw > 0:
        num_positive += 1

print('tatal sentiment polarity:', total_sentiment)
print('everaget sentiment polarity:', total_sentiment/len(pick_twlist))
print('number of (positive VS neural VS nagtive):', num_positive, num_neural, num_nagtive)
