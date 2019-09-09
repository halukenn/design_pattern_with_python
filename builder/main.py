from builder import Director
from builder import TextBuilder
from builder import HtmlBuilder

if __name__ == "__main__":
    director = Director(TextBuilder())
    director.construct()
    print(director.get_result())

    director = Director(HtmlBuilder('builer_test'))
    director.construct()
    print(director.get_result())
