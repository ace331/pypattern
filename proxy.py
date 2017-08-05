'''
# 代理模式
提供一个代理，控制某个对象的访问  
代理的功能是限制和修饰  

有几种模式：
1. 普通代理，最正常的模式，用户用代理类执行方法。（装饰模式？）
2. 强制代理，真实对象提供getproxy方法，并要求只能由代理来访问。
3. 动态代理，事先不用明确代理的对象，使用反射的方法执行业务对象的方法，统一加上某些处理

优点：
1. 职责清晰，业务类只关心业务，访问控制/日志记录/异常处理等由代理完成
2. 扩展，在某对象的基础上进行限制或修饰

日常举例：
python的装饰器
'''

# 例1：文档处理的每个阶段会输出avro格式数据结果（作为后续操作的输入），同时在web段还需要把它们写入数据，这时创建一个avrowriter的代理，实现写入数据库的操作
# PS：感觉优点牵强，直接用一个子类就好了

# 接口
class AvroWriterInterface:
    def write_sentence(self, sentence):
        raise NotImplementedError

    def write_table(self, table):
        raise NotImplementedError

# 业务类
class AvroWriter(AvroWriterInterface):
    def __init__(self, doc_id, doc_file):
        self.doc_id = doc_id
        self.doc_file = doc_file
        self.output_file = doc_file + ".o101"

    def write_sentence(self, sentence):
        print("write sentence '{}' to {}".format(sentence, self.output_file))

    def write_table(self, table):
        print("write table '{}' to {}".format(table, self.output_file))

# 代理类
class AvroDbWriter(AvroWriterInterface)
    def __init__(self, writer):
        self.writer = writer

    def write_sentence(self, sentence):
        self.writer.write_sentence(sentence)
        print('and write sentence to db')

    def write_table(self, table):
        self.writer.write_table(table)
        print('and write table to db')

# 使用场景
docx = '/upload/1.docx'
avro_writer = AvroWriter(1, docx)
avrodb_writer = AvroDbWriter(avro_writer)
avro_writer.write_sentence('Hello')
avro_writer.write_table('<table>Hello</table>')


# 例2：机器学习过程中，需要人为对文档数据标注，这里可以把标注过程和人员管理部分分离开来，即
# 标注：记录文档中的数据/关系
# 管理：记录标注人的工作量/正确率等
# PS，编的
        