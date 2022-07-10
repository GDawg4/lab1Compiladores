# Generated from MyGrammer.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\t\4\2\t\2\3\2\3\2\5\2\7\n\2\3\2\2\2\3\2\2\2\2\b\2\6\3")
        buf.write("\2\2\2\4\7\7\4\2\2\5\7\7\3\2\2\6\4\3\2\2\2\6\5\3\2\2\2")
        buf.write("\7\3\3\2\2\2\3\6")
        return buf.getvalue()


class MyGrammerParser ( Parser ):

    grammarFileName = "MyGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "DIGIT", "IDENT", "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    DIGIT=1
    IDENT=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(MyGrammerParser.IDENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentExpr" ):
                listener.enterIdentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentExpr" ):
                listener.exitIdentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentExpr" ):
                return visitor.visitIdentExpr(self)
            else:
                return visitor.visitChildren(self)


    class DigitExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def DIGIT(self):
            return self.getToken(MyGrammerParser.DIGIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigitExpr" ):
                listener.enterDigitExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigitExpr" ):
                listener.exitDigitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigitExpr" ):
                return visitor.visitDigitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = MyGrammerParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 4
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammerParser.IDENT]:
                localctx = MyGrammerParser.IdentExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                localctx.atom = self.match(MyGrammerParser.IDENT)
                pass
            elif token in [MyGrammerParser.DIGIT]:
                localctx = MyGrammerParser.DigitExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 3
                localctx.atom = self.match(MyGrammerParser.DIGIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





