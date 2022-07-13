# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammerParser#ProgramExpr.
    def enterProgramExpr(self, ctx:MyGrammerParser.ProgramExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#ProgramExpr.
    def exitProgramExpr(self, ctx:MyGrammerParser.ProgramExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#classP.
    def enterClassP(self, ctx:MyGrammerParser.ClassPContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#classP.
    def exitClassP(self, ctx:MyGrammerParser.ClassPContext):
        pass



del MyGrammerParser