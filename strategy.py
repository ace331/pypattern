#coding=utf-8

'''
# 策略模式
定义一组算法，每个都封装起来，并且他们之间可以互换。

## 个人理解：


## 优点：
1. 避免多重条件判断（而由调用方确定）
2. 扩展性好

## 缺点：
1. 类数量多，超过4个最好辅以其他模式
2. 所有策略需要对外暴露，上层要了解所使用的策略

## 适用场景：
1. 多个类只有算法行为上稍有不同
2. 算法需要自由切换

比如：计算器

python动态语言，不用像静态语言那样必须实现某个接口，只要有那个方法即可 
'''

# 这里不用那些猫猫狗狗的例子了，而是用在一些实际的场景
# 例1：docx文档处理的某一步有多种实现，比如python版，.net版，saas版，由不同的客户端自己来决定使用什么版本

# 接口
class DocxExtractor:
    def extract_paragraphs(self):
        raise NotImplementedError()

    def extract_tables(self):
        raise NotImplementedError()


# 不同实现
class PythonDocxExtractor(DocxExtractor):
    def extract_paragraphs(self):
        print('extract paragraphs by python')
        return []

    def extract_tables(self):
        print('extract tables by python')
        return []


class DotnetDocxExtractor(DocxExtractor):
    def extract_paragraphs(self):
        print('extract paragraphs by dotnet')
        return []

    def extract_tables(self):
        print('extract tables by dotnet')
        return []


class SaasDocxExtractor(DocxExtractor):
    def extract_paragraphs(self):
        print('extract paragraphs by saas')
        return []

    def extract_tables(self):
        print('extract tables by saas')
        return []


# 调用者
class ADC:
    def __init__(self, docxpath, extractor):
        self.docxpath = docxpath
        self.extractor = extractor

    def analysis(self):
        self.paragraphs = self.extractor.extract_paragraphs()
        self.tables = self.extractor.extract_tables()


# 不同情况的调用者
class WebServerADC(ADC):
    def __init__(self, docxpath):
        # ADC.__init__(self, docxpath, PythonDocxExtractor())
        super(WebServerADC, self).__init__(docxpath, PythonDocxExtractor())


class ClientADC(ADC):
    def __init__(self, docxpath):
        super(ClientADC, self).__init__(docxpath, DotnetDocxExtractor())


def main():
    web = WebServerADC('upload/demo.docx')
    web.analysis()

    client = ClientADC('local/demo.docx')
    client.analysis()

if __name__ == '__main__':
    main()
