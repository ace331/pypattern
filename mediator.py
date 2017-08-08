'''
# 中介者模式
用一个中介对象封装一系列对象的交互，从而使其耦合松散，只关注自己。

## 优点：
1. 解耦
2. 大型项目可以分成多块，团队合作

## 缺点：
必然会使代码膨胀，逻辑复杂，不是那么直接

## 适用场景：
N个对象互相作用（N>2）
需要解耦切分成多个部分，以合作完成（比如mvc）

案例：mvc，或者三层中的ui层

## 个人理解:
中介者模式不是事件消息模型，面向client的方法都是由中介提供的，中介管的更多。
'''

# 写不下去了，这是个反例，各个子系统其实都是独当一面的，只是内部有些互相依赖的操作，这种情况还是用消息模型比较好

# 例：在我们的文档处理项目中，整个系统分为3大块：
## 标注系统：产生标注数据，供模型训练使用，并不断和数据仓库进行数据交换(这里就简单记为question和answer)
## 数据仓库：存储所有数据（标注和未标注及其他数据），训练并产生新模型
## 分析工具：使用模型进行数据分析，同时产生的用户数据反馈到数据仓库

class LabelSystem:
    def __init__(self, mediator):
        self.mediator = mediator

    def import_question(self, questions):
        pass

    def set_answer(self, answer):
        pass


class DWS:
    def __init__(self, mediator):
        self.mediator = mediator
        self.model = None
        self.questions = []
        self.answers = {}

    def insert_sentence(self, sentence):
        pass

    def get_sentence(self, sentence_id):
        pass

    def insert_answer(self, sentence_id, answer):
        pass

    def get_answer(self, sentence_id):
        pass

    def update_model(self):
        trainning = zip
        self.model = trainning(self.questions, self.answers)

    def get_model(self):
        return self.model


class Analyzer:
    def __init__(self, mediator):
        self.mediator = mediator

    def analysis(self, model, doc):
        return []


class Mediator:
    def __init__(self):
        self.label = LabelSystem(self)
        self.dws = DWS(self)
        self.analyzer = Analyzer(self)
        self.model = self.dws.get_model

    def analysis(self, doc):
        result = self.analyzer.analysis(self.model, doc)
        for (sentence, predict_answer) in result:
            self.dws.insert_answer(sentence)
        return result
    
#----------