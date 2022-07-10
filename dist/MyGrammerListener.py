# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammerParser#IdentExpr.
    def enterIdentExpr(self, ctx:MyGrammerParser.IdentExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#IdentExpr.
    def exitIdentExpr(self, ctx:MyGrammerParser.IdentExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#DigitExpr.
    def enterDigitExpr(self, ctx:MyGrammerParser.DigitExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#DigitExpr.
    def exitDigitExpr(self, ctx:MyGrammerParser.DigitExprContext):
        pass



del MyGrammerParser