# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammerParser.

class MyGrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammerParser#IdentExpr.
    def visitIdentExpr(self, ctx:MyGrammerParser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DigitExpr.
    def visitDigitExpr(self, ctx:MyGrammerParser.DigitExprContext):
        return self.visitChildren(ctx)



del MyGrammerParser