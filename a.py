import numpy as np

# 创建一个从0到100的序列
sequence = np.arange(101)

# 计算最小值
min_value = np.min(sequence)

# 计算第25个百分位数
percentile_25 = np.percentile(sequence, 25)

# 计算中位数
median = np.median(sequence)

# 计算最大值
max_value = np.max(sequence)

# 输出结果
print(f"最小值: {min_value}")
print(f"第25个百分位数: {percentile_25}")
print(f"中位数: {median}")
print(f"最大值: {max_value}")
