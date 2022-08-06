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


    # Visit a parse tree produced by MyGrammerParser#method.
    def visitMethod(self, ctx:MyGrammerParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#arguments.
    def visitArguments(self, ctx:MyGrammerParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#attribute.
    def visitAttribute(self, ctx:MyGrammerParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#formal.
    def visitFormal(self, ctx:MyGrammerParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#expr.
    def visitExpr(self, ctx:MyGrammerParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#parenExpr.
    def visitParenExpr(self, ctx:MyGrammerParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#negationExpr.
    def visitNegationExpr(self, ctx:MyGrammerParser.NegationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#notExpr.
    def visitNotExpr(self, ctx:MyGrammerParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#isVoidExpr.
    def visitIsVoidExpr(self, ctx:MyGrammerParser.IsVoidExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#whileExpr.
    def visitWhileExpr(self, ctx:MyGrammerParser.WhileExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ifExpr.
    def visitIfExpr(self, ctx:MyGrammerParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#letExpr.
    def visitLetExpr(self, ctx:MyGrammerParser.LetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#initialExpr.
    def visitInitialExpr(self, ctx:MyGrammerParser.InitialExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#followingExpr.
    def visitFollowingExpr(self, ctx:MyGrammerParser.FollowingExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#declaration.
    def visitDeclaration(self, ctx:MyGrammerParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#multipleExpr.
    def visitMultipleExpr(self, ctx:MyGrammerParser.MultipleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#expr2.
    def visitExpr2(self, ctx:MyGrammerParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#methodCall.
    def visitMethodCall(self, ctx:MyGrammerParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#overwrite.
    def visitOverwrite(self, ctx:MyGrammerParser.OverwriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#changes.
    def visitChanges(self, ctx:MyGrammerParser.ChangesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#attrWrite.
    def visitAttrWrite(self, ctx:MyGrammerParser.AttrWriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#funCall.
    def visitFunCall(self, ctx:MyGrammerParser.FunCallContext):
        return self.visitChildren(ctx)



del MyGrammerParser