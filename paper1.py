import random
from collections import Counter

str1 = ' 小明，13 '
str2 = ' 小黄，14 '
str3 = str1.replace('小明', '明亮').strip() + ' ' + str2.strip()

str4 = '%s %s %s' % (str1, str2, str3)


# 使用 % 连接形成 str4
str4 = '%s %s %s' % (str1.strip(), str2.strip(), str3)  # str4 = "小明，13 小黄，14 明亮，13 小黄，14"

# 格式化输出函数
def format_output(name, age):
    return f'姓名：{name}, age: {age}'

# 获取并输出 str1 中的姓名和年龄
name1, age1 = str1.strip().split('，')
print(format_output(name1, age1))

# 获取并输出 str2 中的姓名和年龄
name2, age2 = str2.strip().split('，')
print(format_output(name2, age2))

# 获取并输出 str3 中的姓名和年龄
name3, age3 = str3.split(' ')
name3, age3 = name3.split('，')  # 处理 str3 中的姓名和年龄
print(format_output(name3, age3))

# 获取并输出 str4 中的姓名和年龄
parts = str4.split(' ')  # 按空格分割 str4
for part in parts:
    name, age = part.split('，')  # 按中文逗号分割每个部分
    print(format_output(name, age))







list1 =  list(range(1,21,1))
list2 = [x for x in list1 if x%2!=0] + ([y for y in list1 if y%2==0])
print(list1)
print(list2)





# 学生姓名元组
name = ('小明', '小米', '小云', '小彤', '小博', '小磊', '小华', '小洁', '小刚', '小丽')

# 科目元组
subject = ('语文', '数学', '英语')

# 各学生的成绩元组
grade1 = (90, 67, 71)   # 小明的成绩
grade2 = (45, 23, 91)   # 小米的成绩
grade3 = (75, 87, 92)   # 小云的成绩
grade4 = (60, 92, 95)   # 小彤的成绩
grade5 = (77, 66, 88)   # 小博的成绩
grade6 = (99, 97, 89)   # 小磊的成绩
grade7 = (85, 78, 90)   # 小华的成绩
grade8 = (68, 74, 82)   # 小洁的成绩
grade9 = (56, 88, 77)   # 小刚的成绩
grade10 = (91, 85, 93)  # 小丽的成绩

# 将每个学生的成绩与科目打包成字典
dict1 = dict(zip(subject, grade1))   # 小明的成绩字典
dict2 = dict(zip(subject, grade2))   # 小米的成绩字典
dict3 = dict(zip(subject, grade3))   # 小云的成绩字典
dict4 = dict(zip(subject, grade4))   # 小彤的成绩字典
dict5 = dict(zip(subject, grade5))   # 小博的成绩字典
dict6 = dict(zip(subject, grade6))   # 小磊的成绩字典
dict7 = dict(zip(subject, grade7))   # 小华的成绩字典
dict8 = dict(zip(subject, grade8))   # 小洁的成绩字典
dict9 = dict(zip(subject, grade9))   # 小刚的成绩字典
dict10 = dict(zip(subject, grade10)) # 小丽的成绩字典

# 将所有学生的成绩字典打包到一个列表中
grade = []
for i in range(10):
    grade.append(dict(zip(subject, eval(f'grade{i+1}'))))
# grade = [dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10]

# 将学生姓名与他们的成绩字典打包成一个总字典
dictionary = dict(zip(name, grade))

# 创建一个字典以存储每个科目的所有成绩
subject_scores = {subj: [] for subj in subject}

# 打印学生成绩字典
print("学生成绩字典:")
print(dictionary)

# 遍历每个学生的成绩字典
for i in dictionary.values():
    # 遍历每个科目，将成绩添加到对应的科目列表中
    for subj in subject:
        print(i[subj])
        subject_scores[subj].append(i[subj])

# 遍历每个科目，计算并打印最高分、最低分和平均分
print("\n各科目成绩统计:")
for subj, score in subject_scores.items():
    print(f'\n{subj}的所有成绩: {score}')  # 打印当前科目的所有成绩
    maxscore = max(score)  # 计算最高分
    minscore = min(score)  # 计算最低分
    avgscore = sum(score) / len(score)  # 计算平均分
    print(f'{subj}的最高成绩：{maxscore}')  # 打印最高分
    print(f'{subj}的最低成绩：{minscore}')  # 打印最低分
    print(f'{subj}的平均成绩：{avgscore:.2f}')  # 打印平均分，保留两位小数
print("\n各学生成绩统计：")
for student,scores in dictionary.items():
    max_score = max(scores.values())
    min_score = min(scores.values())
    avg_score = sum(scores.values())/len(scores)
    sum_score = sum(scores.values())
    print(f'{student}的总成绩是{sum_score}，最高成绩是{max_score}，最低成绩是{min_score}，平均成绩是{avg_score:.2f}')
total_scores = {student: sum(scores.values()) for student, scores in dictionary.items()}
sorted_students = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_students)


tu1 = tuple(random.randint(1, 100) for _ in range(20))

count = Counter(tu1)

tu2 = tuple(x * 3 for x in tu1)

print("元组tu1:", tu1)
print("每个数字出现的次数:", count)
print("元组tu2:", tu2)





