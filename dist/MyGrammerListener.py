# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammerParser#program.
    def enterProgram(self, ctx:MyGrammerParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#program.
    def exitProgram(self, ctx:MyGrammerParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#classP.
    def enterClassP(self, ctx:MyGrammerParser.ClassPContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#classP.
    def exitClassP(self, ctx:MyGrammerParser.ClassPContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#feature.
    def enterFeature(self, ctx:MyGrammerParser.FeatureContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#feature.
    def exitFeature(self, ctx:MyGrammerParser.FeatureContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#method.
    def enterMethod(self, ctx:MyGrammerParser.MethodContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#method.
    def exitMethod(self, ctx:MyGrammerParser.MethodContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#arguments.
    def enterArguments(self, ctx:MyGrammerParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#arguments.
    def exitArguments(self, ctx:MyGrammerParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#attribute.
    def enterAttribute(self, ctx:MyGrammerParser.AttributeContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#attribute.
    def exitAttribute(self, ctx:MyGrammerParser.AttributeContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#formal.
    def enterFormal(self, ctx:MyGrammerParser.FormalContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#formal.
    def exitFormal(self, ctx:MyGrammerParser.FormalContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#expr.
    def enterExpr(self, ctx:MyGrammerParser.ExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#expr.
    def exitExpr(self, ctx:MyGrammerParser.ExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#parenExpr.
    def enterParenExpr(self, ctx:MyGrammerParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#parenExpr.
    def exitParenExpr(self, ctx:MyGrammerParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#negationExpr.
    def enterNegationExpr(self, ctx:MyGrammerParser.NegationExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#negationExpr.
    def exitNegationExpr(self, ctx:MyGrammerParser.NegationExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#notExpr.
    def enterNotExpr(self, ctx:MyGrammerParser.NotExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#notExpr.
    def exitNotExpr(self, ctx:MyGrammerParser.NotExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#isVoidExpr.
    def enterIsVoidExpr(self, ctx:MyGrammerParser.IsVoidExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#isVoidExpr.
    def exitIsVoidExpr(self, ctx:MyGrammerParser.IsVoidExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#whileExpr.
    def enterWhileExpr(self, ctx:MyGrammerParser.WhileExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#whileExpr.
    def exitWhileExpr(self, ctx:MyGrammerParser.WhileExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#ifExpr.
    def enterIfExpr(self, ctx:MyGrammerParser.IfExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#ifExpr.
    def exitIfExpr(self, ctx:MyGrammerParser.IfExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#letExpr.
    def enterLetExpr(self, ctx:MyGrammerParser.LetExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#letExpr.
    def exitLetExpr(self, ctx:MyGrammerParser.LetExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#initialExpr.
    def enterInitialExpr(self, ctx:MyGrammerParser.InitialExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#initialExpr.
    def exitInitialExpr(self, ctx:MyGrammerParser.InitialExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#followingExpr.
    def enterFollowingExpr(self, ctx:MyGrammerParser.FollowingExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#followingExpr.
    def exitFollowingExpr(self, ctx:MyGrammerParser.FollowingExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#declaration.
    def enterDeclaration(self, ctx:MyGrammerParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#declaration.
    def exitDeclaration(self, ctx:MyGrammerParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#multipleExpr.
    def enterMultipleExpr(self, ctx:MyGrammerParser.MultipleExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#multipleExpr.
    def exitMultipleExpr(self, ctx:MyGrammerParser.MultipleExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#expr2.
    def enterExpr2(self, ctx:MyGrammerParser.Expr2Context):
        pass

    # Exit a parse tree produced by MyGrammerParser#expr2.
    def exitExpr2(self, ctx:MyGrammerParser.Expr2Context):
        pass


    # Enter a parse tree produced by MyGrammerParser#methodCall.
    def enterMethodCall(self, ctx:MyGrammerParser.MethodCallContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#methodCall.
    def exitMethodCall(self, ctx:MyGrammerParser.MethodCallContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#overwrite.
    def enterOverwrite(self, ctx:MyGrammerParser.OverwriteContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#overwrite.
    def exitOverwrite(self, ctx:MyGrammerParser.OverwriteContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#changes.
    def enterChanges(self, ctx:MyGrammerParser.ChangesContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#changes.
    def exitChanges(self, ctx:MyGrammerParser.ChangesContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#attrWrite.
    def enterAttrWrite(self, ctx:MyGrammerParser.AttrWriteContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#attrWrite.
    def exitAttrWrite(self, ctx:MyGrammerParser.AttrWriteContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#funCall.
    def enterFunCall(self, ctx:MyGrammerParser.FunCallContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#funCall.
    def exitFunCall(self, ctx:MyGrammerParser.FunCallContext):
        pass



del MyGrammerParser