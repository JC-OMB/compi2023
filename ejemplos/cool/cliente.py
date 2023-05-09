from antlr4 import *
from antlr.coolLexer import coolLexer
from antlr.coolParser import coolParser
from antlr.coolListener import coolListener
import sys


class MyListener(coolListener):
    #def enterKlass(self, ctx: coolParser.KlassContext):
        #if ctx.TYPE(0).getText() == 'Object':
            #raise Exception('Object illegal')

    def enterKlass(self, ctx: coolParser.KlassContext):
        if ctx.TYPE(1).getText() == 'String':
            raise Exception('illegal inheritance on the class')


def main(argv):
    parser = coolParser(CommonTokenStream(coolLexer(FileStream(argv))))
    tree = parser.program()

    myListener = MyListener()

    walker = ParseTreeWalker()
    walker.walk(myListener, tree)


if __name__ == '__main__':
    main('../../resources/semantic/input/inheritsstring.cool')
    #main('../../resources/semantic/input/redefinedobject.cool')
