from csv_operation import csv_reader
from sentiment import anlaysis
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

from gensim.corpora import Dictionary
from gensim.models import LdaModel
from gensim.parsing.preprocessing import remove_stopwords

# 定义停用词和需要过滤的单词
# stop_words = set(stopwords.words('english'))
extra_stop_words = ['co', 'https']


data2020 = csv_reader("2021tw.csv", "data")
# print(data2020[0], "#" * 10, data2020[1], "#" * 10, " \n", data2020[2])

corpus = []

# split = 21
# pick_twlist = data2020[0::split]
pick_twlist = data2020[1:2000]
for tw in pick_twlist:
    text = tw[10]
    username = tw[8]
    print(text, "\n@@@username=", username, "\n")
    if text != 'tweet':
   		corpus.append(text)

print(len(corpus))
print(corpus[0:2])
# 文本数据

# 创建 CountVectorizer 对象
vectorizer = CountVectorizer(stop_words=extra_stop_words)


# 对文本数据进行预处理，得到词频矩阵
X = vectorizer.fit_transform(corpus)



# 创建 LatentDirichletAllocation 对象
lda = LatentDirichletAllocation(n_components=5, random_state=0)

# 对词频矩阵进行主题建模
lda.fit(X)

# 输出主题模型中的单词和主题分布
feature_names = vectorizer.get_feature_names()
for topic_idx, topic in enumerate(lda.components_):
    message = "Topic #%d: " % topic_idx
    message += " ".join([feature_names[i] for i in topic.argsort()[:-10 - 1:-1]])
    print(message, '\n')

'''
Topic #0: china sea south chinese us taiwan kong hong amp islands 

Topic #1: china sea south us maritime indonesia training southchinasea center building 

Topic #2: china sea south us india southchinasea chinese new taiwan conduct 

Topic #3: china sea south us war military philippines southchinasea navy award 

Topic #4: china sea south southchinasea beijing amp satellite island amti every 


'''



'''
主题关联分析是一种从文本数据中自动识别并提取出相关主题之间的关系的技术。
使用 gensim 库进行主题建模和主题关联分析。
何使用 gensim 库实现主题关联分析
方便我们后续构建知识图谱
'''

# 创建词典，并过滤掉常用单词
stopwords = set(['in', 'to', 'of', 'and', 'the','The', 'China'])
dictionary = Dictionary([remove_stopwords(doc).split() for doc in corpus if remove_stopwords(doc)])

# 创建词袋模型
bow_corpus = [dictionary.doc2bow(remove_stopwords(doc).split()) for doc in corpus if remove_stopwords(doc)]

# 创建 LDA 模型
lda_model = LdaModel(bow_corpus, num_topics=3, id2word=dictionary, passes=10)

# 获取主题词，并过滤掉常用单词
topic_words = {topic_id: [word for word in words if word not in stopwords] for topic_id, words in lda_model.show_topics(formatted=False)}

# 获取包含选定次单词的主题列表
term_topics = {dictionary.token2id["china"]: lda_model.get_term_topics(dictionary.token2id["china"], minimum_probability=0.001)}

# 输出主题词和包含特定词的主题列表
print("Topic words:")
for topic_id, words in topic_words.items():
    print("Topic #{}: {}".format(topic_id, words))

print("Term topics:")
for term_id, topics in term_topics.items():
    print("Term {}: {}".format(dictionary[term_id], [(topic_id, prob) for topic_id, prob in topics]))

'''
Topic words:
Topic #0: [('China', 0.04568844), ('South', 0.032654688), ('Sea', 0.018704137), ('US', 0.0051782276), ('Sea.', 0.004937116), ('The', 0.0049365982), ('sea', 0.0038870985), ('-', 0.0038327142), ('Sea,', 0.0038257875), ('&amp;', 0.0028837628)]
Topic #1: [('China', 0.03188792), ('South', 0.02503358), ('Sea', 0.016786868), ('The', 0.0064823385), ('#SouthChinaSea', 0.0052225003), ('I', 0.004264642), ('south', 0.004137103), ('sea', 0.0039570634), ('china', 0.0038088218), ('Sea.', 0.003765828)]
Topic #2: [('China', 0.04005005), ('South', 0.029851014), ('Sea', 0.018130453), ('Sea.', 0.0077272137), ('The', 0.006598889), ('Philippines', 0.004321567), ('Sea,', 0.004051669), ('I', 0.0040498003), ('Chinese', 0.0039930604), ('US', 0.003645211)]
Term topics:
Term china: [(0, 0.001797251), (1, 0.0037795447), (2, 0.0015984015)]


'''
