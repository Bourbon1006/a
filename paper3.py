import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 选择支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
file_path = r'D:\教学工作\课程\python数据处理课程\2024\上机相关\chengji.xlsx'
# 读取 Excel 文件中的四个班级数据
df1 = pd.read_excel(file_path, sheet_name='1', index_col=0)
df2 = pd.read_excel(file_path, sheet_name='2', index_col=0)
df3 = pd.read_excel(file_path, sheet_name='3', index_col=0)
df4 = pd.read_excel(file_path, sheet_name='4', index_col=0)

# 添加班级前缀到姓名列
df1['姓名'] = ['1-' + col for col in df1['姓名']]
df2['姓名'] = ['2-' + col for col in df2['姓名']]
df3['姓名'] = ['3-' + col for col in df3['姓名']]
df4['姓名'] = ['4-' + col for col in df4['姓名']]

# 定义函数统计成绩等级
def tongji(dataframe):
    # 初始化计数器
    counts = {
        '优秀': 0,
        '良好': 0,
        '中等': 0,
        '及格': 0,
        '不及格': 0
    }

    # 统计各个等级的学生人数
    for score in dataframe['考试总']:
        if score >= 90:
            counts['优秀'] += 1
        elif 80 <= score <= 89:
            counts['良好'] += 1
        elif 70 <= score <= 79:
            counts['中等'] += 1
        elif 60 <= score <= 69:
            counts['及格'] += 1
        else:
            counts['不及格'] += 1

    # 计算总人数
    total_students = len(dataframe)

    # 计算百分比
    percentages = {key: (value / total_students) * 100 for key, value in counts.items()}

    # 输出结果
    print("成绩统计:")
    for grade, count in counts.items():
        print(f"{grade}: {count}人, 百分比: {percentages[grade]:.2f}%")
    return counts


# 统计每个班级的成绩等级
counts1 = tongji(df1)
counts2 = tongji(df2)
counts3 = tongji(df3)
counts4 = tongji(df4)

def tongji2(dataframe):
    max_index = dataframe['考试总'].idxmax()
    min_index = dataframe['考试总'].idxmin()
    mean_value = dataframe['考试总'].mean()
    std_value = dataframe['考试总'].std()
    print(f'全班最高分: {dataframe.loc[max_index, '姓名']},最低分：{dataframe.loc[min_index, '姓名']},平均分：{mean_value},标准差{std_value}')

tongji2(df1)
tongji2(df2)
tongji2(df3)
tongji2(df4)


# 整合数据用于饼图
data = {
    '班级1': counts1,
    '班级2': counts2,
    '班级3': counts3,
    '班级4': counts4
}

# 创建饼图
fig1, axs1 = plt.subplots(2, 2, figsize=(12, 10))
axs1 = axs1.flatten()  # 将 2D 数组展平为 1D 数组，方便迭代

# 绘制每个班级的饼图
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for i, (class_name, counts) in enumerate(data.items()):
    axs1[i].pie(counts.values(), labels=counts.keys(), colors=colors,
                autopct='%1.1f%%', startangle=140, pctdistance=0.85)
    axs1[i].set_title(class_name)
    axs1[i].text(0, -1.2, f'{class_name} 成绩分布', ha='center', va='center', fontsize=12, color='black')



# 调整饼图布局并显示
plt.tight_layout()
plt.show()

# 创建直方图
fig2, axs2 = plt.subplots(figsize=(10, 6))

# 准备直方图的数据
labels = list(data.keys())
excellent = [counts['优秀'] for counts in data.values()]
good = [counts['良好'] for counts in data.values()]
average = [counts['中等'] for counts in data.values()]
pass_count = [counts['及格'] for counts in data.values()]
fail = [counts['不及格'] for counts in data.values()]

# 设置条形图的宽度和位置
bar_width = 0.15
x = np.arange(len(labels))

# 绘制直方图
axs2.bar(x, excellent, width=bar_width, label='优秀', color='#ff9999')
axs2.bar(x + bar_width, good, width=bar_width, label='良好', color='#66b3ff')
axs2.bar(x + 2 * bar_width, average, width=bar_width, label='中等', color='#99ff99')
axs2.bar(x + 3 * bar_width, pass_count, width=bar_width, label='及格', color='#ffcc99')
axs2.bar(x + 4 * bar_width, fail, width=bar_width, label='不及格', color='#c2c2f0')

# 设置直方图的标签和标题
axs2.set_xlabel('班级')
axs2.set_ylabel('人数')
axs2.set_title('成绩分布直方图')
axs2.set_xticks(x + 2 * bar_width)  # 设置x轴刻度
axs2.set_xticklabels(labels)  # 设置x轴标签
axs2.legend()  # 显示图例


# 调整直方图布局并显示
plt.tight_layout()
plt.show()









