'''
# 原型模式
由原型实例拷贝出另一个对象，而不是从构造函数开始

## 优点：
1. 二进制拷贝，通常比从分配资源构造对象简单一些
2. 摆脱构造函数

## 缺点：
1. 逃避了构造函数的束缚

'''

# 例：句子标注时，同一个句子要求3个人分别标注，并且其实是在预测答案的基础上进行修改的
import copy
new_list = copy.copy(existing_list)
new_list_of_dicts = copy.deepcopy(existing_list_of_dicts)