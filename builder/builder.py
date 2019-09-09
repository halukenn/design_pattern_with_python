from abc import ABCMeta
from abc import abstractmethod


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def make_title(self, title):
        pass

    @abstractmethod
    def make_string(self, string):
        pass

    @abstractmethod
    def make_items(self, items):
        pass

    @abstractmethod
    def close(self):
        pass


class TextBuilder(Builder):

    def __init__(self):
        self.element_list = []

    def make_title(self, title):
        self.element_list.append('=========================')
        self.element_list.append('「' + title + '」')

    def make_string(self, string):
        self.element_list.append('■' + string)

    def make_items(self, items):
        for item in items:
            self.element_list.append('　・' + item)

    def close(self):
        self.element_list.append('=========================')

    def get_result(self):
        return '\n'.join(self.element_list)


class HtmlBuilder(Builder):

    def __init__(self, file_name):
        self.element_list = []
        self.file_name = file_name
        self.f = open(file_name + '.html', 'w')

    def __del__(self):
        self.f.close()

    def make_title(self, title):
        self.element_list.append(
            '<html><head><title>' + title + '</title></head><body>')
        self.element_list.append('<h1>' + title + '</h1>')

    def make_string(self, string):
        self.element_list.append('<p>' + string + '</p>')

    def make_items(self, items):
        self.element_list.append('<ul>')
        for item in items:
            self.element_list.append('<li>' + item + '</li>')
        self.element_list.append('</ul>')

    def close(self):
        self.element_list.append('</body></html>')

    def get_result(self):
        for elem in self.element_list:
            self.f.write(elem)
        return self.file_name


class Director:

    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.make_title('Greeting')
        self.builder.make_string('朝から昼にかけて')
        self.builder.make_items(['おはようございます', 'こんにちは'])
        self.builder.make_string('夜に')
        self.builder.make_items(['こんばんは', 'おやすみなさい', 'さようなら'])
        self.builder.close()

    def get_result(self):
        return self.builder.get_result()
