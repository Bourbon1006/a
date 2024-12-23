import numpy as np  # 导入NumPy库，通常用于数组和数学计算

# 创建一个包含从0到1（不包括1）以0.01为步长的数组
array1 = np.arange(0, 1, 0.01)
# 随机打乱数组1的顺序
np.random.shuffle(array1)
print("数组1:", array1)  # 输出数组1

# 设置随机数种子，以便于结果可复现（可选）
np.random.seed(0)

# 创建100个服从正态分布的随机数，均值为30，标准差为sqrt(1.2)
mean = 30
variance = 1.2
std_dev = np.sqrt(variance)  # 计算标准差

# 生成服从正态分布的随机数数组
array2 = np.random.normal(loc=mean, scale=std_dev, size=100)

# 输出结果
print("数组2:", array2)  # 输出数组2


# 创建一个包含100个1到50之间的等间隔数组
array3 = np.linspace(1, 50, num=100)
print("数组3:", array3)
# 对数组3进行随机打乱处理
np.random.shuffle(array3)

# 输出结果
print("数组3:", array3)  # 输出数组3


# 将数组1、数组2和数组3分别重塑为10x10的二维数组
array1_square = np.reshape(array1, (10, 10))
array2_square = np.reshape(array2, (10, 10))
array3_square = np.reshape(array3, (10, 10))

# 将数组1的对角线元素设置为0
np.fill_diagonal(array1_square, 0)
# 将数组2的对角线元素设置为10
np.fill_diagonal(array2_square, 10)
# 将数组3的对角线元素设置为100
np.fill_diagonal(array3_square, 100)

# 打印重塑后的数组
print(array1_square)  # 输出重塑后的数组1
print(array2_square)  # 输出重塑后的数组2
print(array3_square)  # 输出重塑后的数组3


# 数组的加法、减法、乘法和除法运算
jia = array1 + array2 + array3  # 数组相加
jian = array1 - array2 - array3  # 数组相减
chen = array1 * array2 * array3  # 数组相乘
# 数组相除，避免除以零的情况
chu = np.divide(array1, array2, out=np.zeros_like(array1), where=array2 != 0)

# 打印运算结果
print(jia)  # 输出加法结果
print(jian)  # 输出减法结果
print(chen)  # 输出乘法结果
print(chu)  # 输出除法结果


# 统计分析函数，用于计算数组的各种统计量
def analyze_array(arr):
    return {
        'max': np.max(arr),       # 最大值
        'min': np.min(arr),       # 最小值
        'median': np.median(arr), # 中位数
        'sum': np.sum(arr),       # 总和
        'var': np.var(arr),       # 方差
        'std': np.std(arr)        # 标准差
    }

# 计算数组1、数组2和数组3的统计量
stats1 = analyze_array(array1)
stats2 = analyze_array(array2)
stats3 = analyze_array(array3)

# 切片操作：分别取每个数组的前10个、中间10个和最后10个元素
def get_slices(array):
    first_10 = array[:10]  # 前10个元素
    middle_index = len(array) // 2
    middle_10 = array[middle_index - 5:middle_index + 5]  # 中间10个元素
    last_10 = array[-10:]  # 最后10个元素
    return first_10, middle_10, last_10
# 从每个数组中获取切片
slices1 = get_slices(array1)
slices2 = get_slices(array2)
slices3 = get_slices(array3)

result_matrix1 = np.array([slices1[0], slices1[1], slices1[2]])
result_matrix2 = np.array([slices2[0], slices2[1], slices2[2]])
result_matrix3 = np.array([slices3[0], slices3[1], slices3[2]])


# 打印切片结果矩阵
print(result_matrix1)  # 输出切片结果矩阵
print(result_matrix2)
print(result_matrix3)

combined_result = np.column_stack((result_matrix1, result_matrix2, result_matrix3))
np.savetxt('file3.txt', combined_result, fmt='%10.2f')#%10.2f   整体占10位，小数部分占两位

# 创建矩阵 A、B 和 C
A = np.ones((3, 3))      # 全 1 的矩阵
B = np.full((3, 3), 2)
D = np.twos((4, 4))   # 全 2 的矩阵
C = np.random.randint(0, 10, (3, 3))  # 随机整型数据的矩阵，范围在 0 到 10 之间

# 进行水平堆叠
horizontal_stack = np.hstack((A, B, C))

# 进行垂直堆叠
vertical_stack = np.vstack((A, B, C))

# 保存到文本文件
np.savetxt('file1.txt', horizontal_stack, fmt='%s')
np.savetxt('file2.txt', vertical_stack, fmt='%s')






