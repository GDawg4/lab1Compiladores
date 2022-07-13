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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("\r\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\2\2\4\2")
        buf.write("\4\2\2\2\n\2\6\3\2\2\2\4\t\3\2\2\2\6\7\5\4\3\2\7\b\7\3")
        buf.write("\2\2\b\3\3\2\2\2\t\n\7\4\2\2\n\13\7\b\2\2\13\5\3\2\2\2")
        buf.write("\2")
        return buf.getvalue()


class MyGrammerParser ( Parser ):

    grammarFileName = "MyGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CLASSKEY", "DIGIT", "LOWER", 
                      "UPPER", "TYPE", "LETTERS", "WHITESPACE" ]

    RULE_program = 0
    RULE_classP = 1

    ruleNames =  [ "program", "classP" ]

    EOF = Token.EOF
    T__0=1
    CLASSKEY=2
    DIGIT=3
    LOWER=4
    UPPER=5
    TYPE=6
    LETTERS=7
    WHITESPACE=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramExprContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.ProgramContext
            super().__init__(parser)
            self.meat = None # ClassPContext
            self.end = None # Token
            self.copyFrom(ctx)

        def classP(self):
            return self.getTypedRuleContext(MyGrammerParser.ClassPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramExpr" ):
                listener.enterProgramExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramExpr" ):
                listener.exitProgramExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramExpr" ):
                return visitor.visitProgramExpr(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = MyGrammerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            localctx = MyGrammerParser.ProgramExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            localctx.meat = self.classP()
            self.state = 5
            localctx.end = self.match(MyGrammerParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.asdf = None # Token

        def CLASSKEY(self):
            return self.getToken(MyGrammerParser.CLASSKEY, 0)

        def TYPE(self):
            return self.getToken(MyGrammerParser.TYPE, 0)

        def getRuleIndex(self):
            return MyGrammerParser.RULE_classP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassP" ):
                listener.enterClassP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassP" ):
                listener.exitClassP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassP" ):
                return visitor.visitClassP(self)
            else:
                return visitor.visitChildren(self)




    def classP(self):

        localctx = MyGrammerParser.ClassPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classP)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(MyGrammerParser.CLASSKEY)
            self.state = 8
            localctx.asdf = self.match(MyGrammerParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





