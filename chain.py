
'''

# 责任链模式
有多个对象来处理不同状态的请求，把他们连城一条链，从而避免发送者和接收者之间的耦合。

## 优点
请求和处理分开，请求者不用知道谁来处理，处理者不用知道请求的全貌（前面的handler可能处理部分信息）。
二者解耦，责任链可以方便地扩展拆解

## 缺点
责任链的遍历/递归可能会影响性能，不建议很长。（python可以尾递归？）

## 个人理解
可以用来动态决定由谁来处理，或者依次由几个handler来处理。

'''

# 例：一个文档处理过程会经历若干个过程，中间还可能中断等待人为的操作再启动。

# handler基类，定义了分配方法和接口
class Handler:
    def __init__(self, aim_status):
        self.aim_status = aim_status
        self.next = None

    def execute(self, doc):
        to_next = True
        if self.aim_status == doc.status:
            to_next, response = analysis(doc)
            print(response)

        if to_next:
            if self.next:
                self.next.analysis(doc)
            else:
                print('not set next')
        else:
            print('handle finish')

    def analysis(self):
        raise NotImplementedError()


# 各分步实现
class P100(Handler):
    def __init__(self):
        super.__init__(0)
    
    def analysis(self, doc):
        doc.status = 10
        return True, "提取了文档内容"


class P200(Handler):
    def __init__(self):
        super.__init__(10)
    
    def analysis(self, doc):
        doc.status = 20
        return True, "分析内容"


class P300(Handler):
    def __init__(self):
        super.__init__(20)
    
    def analysis(self, doc):
        doc.status = 30
        return True, "生成报告"

# 
class 