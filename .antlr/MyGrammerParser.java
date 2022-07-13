// Generated from /home/garoz/2022/20222/compiladores/lab0/MyGrammer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MyGrammerParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, CLASSKEY=4, INHERITSKEY=5, DIGIT=6, LOWER=7, UPPER=8, 
		TYPE=9, LETTERS=10, WHITESPACE=11;
	public static final int
		RULE_program = 0, RULE_classP = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classP"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "CLASSKEY", "INHERITSKEY", "DIGIT", "LOWER", 
			"UPPER", "TYPE", "LETTERS", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MyGrammer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MyGrammerParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	 
		public ProgramContext() { }
		public void copyFrom(ProgramContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ProgramExprContext extends ProgramContext {
		public ClassPContext meat;
		public Token end;
		public ClassPContext classP() {
			return getRuleContext(ClassPContext.class,0);
		}
		public ProgramExprContext(ProgramContext ctx) { copyFrom(ctx); }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			_localctx = new ProgramExprContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(4);
			((ProgramExprContext)_localctx).meat = classP();
			setState(5);
			((ProgramExprContext)_localctx).end = match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassPContext extends ParserRuleContext {
		public TerminalNode CLASSKEY() { return getToken(MyGrammerParser.CLASSKEY, 0); }
		public List<TerminalNode> TYPE() { return getTokens(MyGrammerParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(MyGrammerParser.TYPE, i);
		}
		public TerminalNode INHERITSKEY() { return getToken(MyGrammerParser.INHERITSKEY, 0); }
		public ClassPContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classP; }
	}

	public final ClassPContext classP() throws RecognitionException {
		ClassPContext _localctx = new ClassPContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classP);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(7);
			match(CLASSKEY);
			setState(8);
			match(TYPE);
			setState(11);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITSKEY) {
				{
				setState(9);
				match(INHERITSKEY);
				setState(10);
				match(TYPE);
				}
			}

			setState(13);
			match(T__1);
			setState(14);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r\23\4\2\t\2\4\3"+
		"\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\16\n\3\3\3\3\3\3\3\3\3\2\2\4\2\4"+
		"\2\2\2\21\2\6\3\2\2\2\4\t\3\2\2\2\6\7\5\4\3\2\7\b\7\3\2\2\b\3\3\2\2\2"+
		"\t\n\7\6\2\2\n\r\7\13\2\2\13\f\7\7\2\2\f\16\7\13\2\2\r\13\3\2\2\2\r\16"+
		"\3\2\2\2\16\17\3\2\2\2\17\20\7\4\2\2\20\21\7\5\2\2\21\5\3\2\2\2\3\r";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}