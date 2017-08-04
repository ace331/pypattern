#coding=utf-8

'''
# 建造者模式
用已有（或外部提供）的方法，以不同的组合构建一个对象。（也可以和策略模式混合起来）

## 个人理解：
基类实现所有的逻辑，子类只是组合调用  
其实最简单的三层结构，就是BLL组合调用DAL，UI组合调用BLL

## 优点：
1. 封装，实现封装在基类，子类只关心顺序即可，并且基类方法可以复用
2. 高层互相独立，互不影响

## 缺点：
 

## 适用场景：
高层比较复杂，有多种组合情况，顺序会影响结果
'''

'''
场景：
有一个word文档处理的功能，可以文档格式转换，从文档中提取 文字/表格/公式/因果关系，并分析 错别字/数据矛盾/公式计算结果

这里需要有处理 word/pdf（需要先转换成word）文件的免费（只取数据）和收费版本（数据+关系）

'''
# 基类
class WordAnalyzer:
    def __init__(self):
        self.commands = []

    def __pdf2word(self):
        print('将pdf转换为word文件')

    def __extract_data(self):
        print('提取文字/表格数据')

    def __extract_relation(self):
        print('提取数据关系和因果关系')

    def __analysis_data(self):
        print('分析数据')

    def __analysis_relation(self):
        print('分析关系')

    def set_commands(self, commands):
        self.commands = commands

    def analysis(self, filepath):
        for command in commands:
            print(command)


# 创造者(这里一个builder中共用了一个analyser)
class WordAnalyzerBuilder:
    def __init__(self):
        self.analyzer = WordAnalyzer()

    def build_word_free_analyzer(self):
        self.analyzer.set_commands(['extract_data', 'analysis_data'])
        return self.analyzer

    def build_word_charged_analyzer(self):
        self.analyzer.set_commands(['extract_data', 'extract_relation', 'analysis_data', 'analysis_relation'])
        return self.analyzer

    def build_pdf_free_analyzer(self):
        self.analyzer.set_commands(['pdf2word', 'extract_data', 'analysis_data'])
        return self.analyzer

    def build_pdf_charged_analyzer(self):
        self.analyzer.set_commands(['pdf2word', 'extract_data', 'extract_relation', 'analysis_data', 'analysis_relation'])
        return self.analyzer

# 调用
builder = WordAnalyzerBuilder()
builder.build_pdf_charged_analyzer().analysis('/upload/1.pdf')

# PS：书上要再复杂一些，基类是接口和run的实现，具体的实现可以有多种（产品），每种产品需要一个builder来生成各种不同的版本