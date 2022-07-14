import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor


def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]

  
class MyVisitor(MyGrammerVisitor):
    def visitProgramExpr(self, ctx):
        # value = ctx.getText()
        # return int(value)
        print('ProgramExpr')
        print('Text', self.visit(ctx.meat))
        return

    def visitClassP(self, ctx):
        # return self.visit(ctx.expr())
        print('ClassP')
        return ctx.getText()

    def visitFeature(self, ctx):
        print('Feature1')
        return

    def visitFeature1(self, ctx):
        print('Feature')
        return

    def visitFeature2(self, ctx):
        print('Feature1')
        return

    def visitFormal(self, ctx):
        print('Feature2')
        return

    def visitExpr(self, ctx):
        print('Expr')
        return

    def visitExpr2(self, ctx):
        print('Expr2')
        return

    def visitId2(self, ctx):
        print('Id2')
        return


if __name__ == "__main__":
    while 1:
        data =  InputStream(input(">>> "))
        # lexer
        lexer = MyGrammerLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = MyGrammerParser(stream)
        tree = parser.program()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(tree)
        print(Trees.toStringTree(tree, None, parser))
