# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# # Create a new chat bot named Charlie
# chatbot = ChatBot('Charlie')

# trainer = ListTrainer(chatbot)

# trainer.train([
#     "你需要帮助吗？",
#     "当然，我正在定航班去爱尔兰",
#     "你的航班已经定好."
# ])

# # Get a response to the input text 'I would like to book a flight.'
# response = chatbot.get_response('我正想定一个航班.')

# print(response)


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# ChatterBot是使用Python构建的基于机器学习的对话对话框引擎，它使得可以基于已知对话的集合生成响应。
# ChatterBot的语言独立设计使其可以接受任何语言的培训。
# 通过搜索与输入匹配的最接近的已知语句来选择最接近的匹配响应，然后根据机器人与之通信的人发出每个响应的频率，将最有可能的响应返回给该语句。

Chinese_bot = ChatBot('Ron Obvious')
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(Chinese_bot)
# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.chinese")


# # 测试一下
# question = '亲，在吗'
# print(question)
# response = Chinese_bot.get_response(question)
# print(response)
# print("\n")
# question = '有红色的吗？'
# print(question)
# response = Chinese_bot.get_response(question)
# print(response)
