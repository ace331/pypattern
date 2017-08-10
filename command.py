'''
# 命令模式
将一个请求封装成一个对象（比起string，它包含了约束和实现方法在里面），从而简化客户端的调用，还可以排队请求/撤销/回滚等。

## 优点：
1. 解耦，调用者不用依赖接收者，只知道要执行的命令即可
2. 扩展性，方便扩展

## 缺点：
一个命令就要一个类

## 个人理解：
可以用命令来封装多个接收者的相互操作

'''


# 命令接口
class Command():
    def __init__(self){
        self.requirementGroup = RequirementGroup()
        self.pageGroup = PageGroup()
        self.codeGroup = CodeGroup()
    }

    def execute(self):
        raise NotImplementedError()


# 具体的命令
class AddRequirementCommand(Command):
    def execute(self):
        self.requirementGroup.add()
        self.requirementGroup.plan()


class DeletePageCommand(Command):
    def execute(self, page):
        self.requirementGroup.delete(page)
        self.pageGroup.delete(page)
        self.codeGroup.delete(page)
        self.requirementGroup.plan()


# 执行者（是不是有点多余）
class Invoker():
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def execute():
        self.command.execute()