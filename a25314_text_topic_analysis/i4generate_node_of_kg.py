import json

# List of topic words
topic_words = [
    [['China', 0.04568844], ['South', 0.032654688], ['Sea', 0.018704137], ['US', 0.0051782276], 
     ['Sea.', 0.004937116], ['sea', 0.0038870985],  
     ['Sea,', 0.0038257875], ['Japan', 0.0028837628]], 
    [['China', 0.03188792], ['South', 0.02503358], ['Sea', 0.016786868],
     ['#SouthChinaSea', 0.0052225003],  ['south', 0.004137103], ['sea', 0.0039570634], 
     ['china', 0.0038088218], ['Taiwan', 0.003765828]], 
    [['China', 0.04005005], ['South', 0.029851014], ['Sea', 0.018130453], ['Taiwan', 0.0077272137], 
     ['Philippines', 0.004321567], ['Taiwan', 0.004051669], 
     ['Chinese', 0.0039930604], ['US', 0.003645211]]
]

print('i4')

# Convert topic words to JSON format
json_data = []
for words in topic_words:
    for i in range(len(words)):
        word1 = words[i][0]
        for j in range(i+1, len(words)):
            word2 = words[j][0]
            freq = round((words[i][1] + words[j][1]) * 100, 2)
            if freq > 20:
                freq = 20
            if freq < 1:
                freq = 5
            json_data.append({"word1": word1, "word2": word2, "freq": freq})

# Output JSON data with each item on a new line
with open('i4my_topic_words.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=None, separators=(',', ':'))


    f.write('\n')

