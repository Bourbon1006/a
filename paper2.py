import numpy as np  # 导入NumPy库，通常用于数组和数学计算
l1 =list(range(1,5))
print('l1=:',l1)
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
slices1 = [array1[:10], array1[45:55], array1[-10:]]
slices2 = [array2[:10], array2[45:55], array2[-10:]]
slices3 = [array3[:10], array3[45:55], array3[-10:]]

# 组合切片结果为一个3x30的矩阵
results = np.array([
    np.concatenate(slices1),  # 将切片结果合并为一维数组
    np.concatenate(slices2),
    np.concatenate(slices3)
])

# 打印切片结果矩阵
print(results)  # 输出切片结果矩阵

matrix1 = np.arange(1,10)
re = np.reshape(matrix1, (3, 3))

print(re.max())

