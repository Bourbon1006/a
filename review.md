# 复习

## 字符串操作

初始化用例

+ a = '  hello world  '
+ c = 123

### 格式化

#### % 使用方法

`b = 'hello %s %d' % (a, c)`

#### .format()方法

`b = 'hello {} {}'.format(a, c)`

#### f'string'方法

`b = f'hello {a} {c}'`

### split，join，strip

#### split： 分割字符串，返回一个列表

`a.split(' ') #['hello', 'world']` 参数默认为空格

#### join： 将列表中的元素以指定字符连接起来

`' ',join(a) #'hello world'`

#### strip： 去除字符串首尾的空格,可以在前面加l以及r，去除左边或者右边的空格

`a.strip() #'hello world'` 默认去除空格，想要去除其他的，需要在括号中加参数,用''来指定要去除的字符


## 列表

初始化用例

+ a = [1,3,4,5,6,7,8,9,10]
+ b = [222]

### insert，append，extend

#### index:

`a.index(3)` #1

#### insert： 在指定位置插入元素

`a.insert(1,2)` #[1,2,3,4,5,6,7,8,9,10]

#### append： 在列表末尾添加元素

`a.append(11)` #[1,2,3,4,5,6,7,8,9,10,11]

#### extend： 将一个列表中的元素添加到另一个列表中

`a.extend(b)` #[1,2,3,4,5,6,7,8,9,10,222]

### del

`del a[1]` #[1,3,4,5,6,7,8,9,10,222]

### 平方列表

```python
x = []
for i in range(10):
    x.append(i ** 2)
print(x) #[0,1,4,9,16,25,36,49,64,81]
``` 
## 字典

初始化用例

+ a = {'name':'xiaoming','age':18}

### 遍历 for ，items ，values

#### for

```python
for key in a:
    print(key)
#name
#age   只输出键
```

#### values

```python
for key in a.values():
    print(key)
#xiaoming
#18  只输出值
```

#### items

```python
for key in a.items():
    print(key)
#('name', 'xiaoming')
#('age', 18)  直接输出键值对
```

### __len__()

```python
print(a.__len__()) #2
```

## numpy

初始化用例

+ a = np.array([1,2,3,4,5,6,7,8,9,10])

### reshape()

```python
a = a.reshape(2,5)
print(a)
#[[1,2,3,4,5]
#[6,7,8,9,10]]   2 * 5的矩阵
```

### linspace()

```python
a = np.linspace(1,10,10)
print(a)
#[1,2,3,4,5,6,7,8,9,10]  1到10之间的10个数
```

### arange()

```python
a = np.arange(1,10,2)
print(a)
#[1,3,5,7,9]  1到10之间的数，步长为2
```

### np.random.shuffle()

```python
b = np.random.shuffle(a)
print(b)
#[3,1,5,7,9]  随机打乱数组
```
### np.flip()

```python
b = np.flip(a)
print(b) 
#反转，亦可以使用[::-1]实现
```
### np.random.rand

```python
b = np.random.rand(3,3,3) # 3*3*3的随机数组，小于1
b = np.random.randint(1,10,(3,3,3)) # 3*3*3的随机数组，1到10的
```

### np.eye()

```python
b = np.eye(3) # 3*3的单位向量
#[[1 0 0]
# [0 1 0]
# [0 0 1]]
```

### np.sort()

```python
import numpy as np

a = np.random.rand(10)

print(np.sort(a))
# 随机数组从大到小排序

a = np.random.rand(3,3,3)

print(np.sort(a.flatten()))  # 拆分成一维数组排序
print(np.sort(a,axis=0)) # 按列排序
print(np.sort(a,axis=1)) # 按行排序
```

## pandas

初始化用例
import pandas as pd

a = pd.Series([1,2,3,4,5,6,7,8,9,10])
b = pd.DataFrame({'name':['xiaoming','xiaohong','xiaoli'],'age':[18,19,20]})

### tocsv()
    
```python
b.to_csv('test.csv')
#导出csv文件
```

### read_csv()

```python
c = pd.read_csv('test.csv')
#读取csv文件
```

### df.drop_duplicates()

```python
b.drop_duplicates()
#去除重复的name
```

## matplotlib()

### 折线图

```python
plt.plot(x, y, marker='o')
plt.show()
```

### 柱状图

```python
plt.bar(x, y)
plt.show()
```
### 直方图

```python
plt.hist(x, bins=5)
plt.show()
```

## 爬虫

### urllib
import urllib.request

```python
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
status = response.getcode()
print(status)
```
+ 200：请求成功。
+ 404：请求的资源未找到。
+ 500：服务器内部错误。

## 文本处理

### jieba

### nblk

## 题型

### 选择  30 

### 填空（代码分析）  20 20 

### 程序编程题 30