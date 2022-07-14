# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammerParser.

class MyGrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammerParser#program.
    def visitProgram(self, ctx:MyGrammerParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#classP.
    def visitClassP(self, ctx:MyGrammerParser.ClassPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#feature.
    def visitFeature(self, ctx:MyGrammerParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#feature1.
    def visitFeature1(self, ctx:MyGrammerParser.Feature1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#feature2.
    def visitFeature2(self, ctx:MyGrammerParser.Feature2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#formal.
    def visitFormal(self, ctx:MyGrammerParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#expr.
    def visitExpr(self, ctx:MyGrammerParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#expr2.
    def visitExpr2(self, ctx:MyGrammerParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#id2.
    def visitId2(self, ctx:MyGrammerParser.Id2Context):
        return self.visitChildren(ctx)



del MyGrammerParser