web_server = 0.99999

pc = 0.8
print('''web server down's probability is:
        1 - 0.99999  = 0.00001
        one old pc down's probability is:
        1 - 0.8 = 0.2
        set x is the amount of the pc, when all x amount of pc is down, the pc cluster is down
        0.2^^x = 0.00001
        we want to know x:
    ''')

import math

print('-'*20, '\nx = math.log(0.00001, 0.2) ')
x = math.log(0.00001, 0.2)
print('x=', x)

print('Q3_a:')
print(int(x)+1, 'pc is needed')

# 需要8台, 计算过程如下：

# web server down's probability is:
#         1 - 0.99999  = 0.00001
#         one old pc down's probability is:
#         1 - 0.8 = 0.2
#         set x is the amount of the pc, when all x amount of pc is down, the pc cluster is down
#         0.2^^x = 0.00001
#         we want to know x:
    
# -------------------- 
# x = math.log(0.00001, 0.2) 
# x= 7.153382790366966
# 8  is needed

print('Q3_b:')
print(''' Because the layers are connected in series, overall reliability is the product of 3 layers:
''')
overall = 0.99999 * 0.9999 * 0.999
print(overall, " so it's 99.8890110999% in overall reliability ")