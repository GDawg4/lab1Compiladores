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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, WHITESPACE=17, 
		IFKEY=18, LOOPEY=19, ELSEKEY=20, THENKEY=21, WHILEKEY=22, CLASSKEY=23, 
		INHERITSKEY=24, FIKEY=25, INKEY=26, LETKEY=27, NEWKEY=28, POOLKEY=29, 
		ISVOIDKEY=30, NOTKEY=31, TRUEKEY=32, FALSEKEY=33, TRUE=34, FALSE=35, INTEGERS=36, 
		TYPE=37, ID=38, ANYSET=39, ALPHANUMERIC=40, OBJECT=41, DIGIT=42, LOWER=43, 
		UPPER=44, LETTERS=45, STRING=46, COMMENTS=47;
	public static final int
		RULE_program = 0, RULE_classP = 1, RULE_feature = 2, RULE_feature1 = 3, 
		RULE_feature2 = 4, RULE_formal = 5, RULE_expr = 6, RULE_expr2 = 7, RULE_id2 = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classP", "feature", "feature1", "feature2", "formal", "expr", 
			"expr2", "id2"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'", "'('", "','", "')'", "':'", "'<-'", "'+'", 
			"'-'", "'*'", "'/'", "'<'", "'='", "'@'", "'.'", null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "WHITESPACE", "IFKEY", "LOOPEY", "ELSEKEY", 
			"THENKEY", "WHILEKEY", "CLASSKEY", "INHERITSKEY", "FIKEY", "INKEY", "LETKEY", 
			"NEWKEY", "POOLKEY", "ISVOIDKEY", "NOTKEY", "TRUEKEY", "FALSEKEY", "TRUE", 
			"FALSE", "INTEGERS", "TYPE", "ID", "ANYSET", "ALPHANUMERIC", "OBJECT", 
			"DIGIT", "LOWER", "UPPER", "LETTERS", "STRING", "COMMENTS"
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
		public ClassPContext meat;
		public Token end;
		public ClassPContext classP() {
			return getRuleContext(ClassPContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			((ProgramContext)_localctx).meat = classP();
			setState(19);
			((ProgramContext)_localctx).end = match(T__0);
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
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
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
			setState(21);
			match(CLASSKEY);
			setState(22);
			match(TYPE);
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITSKEY) {
				{
				setState(23);
				match(INHERITSKEY);
				setState(24);
				match(TYPE);
				}
			}

			setState(27);
			match(T__1);
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(28);
				feature();
				setState(29);
				match(T__0);
				}
				}
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(36);
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

	public static class FeatureContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MyGrammerParser.ID, 0); }
		public Feature1Context feature1() {
			return getRuleContext(Feature1Context.class,0);
		}
		public Feature2Context feature2() {
			return getRuleContext(Feature2Context.class,0);
		}
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_feature);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(ID);
			setState(41);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				{
				setState(39);
				feature1();
				}
				break;
			case T__6:
				{
				setState(40);
				feature2();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
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

	public static class Feature1Context extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(MyGrammerParser.TYPE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public Feature1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature1; }
	}

	public final Feature1Context feature1() throws RecognitionException {
		Feature1Context _localctx = new Feature1Context(_ctx, getState());
		enterRule(_localctx, 6, RULE_feature1);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			match(T__3);
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(44);
				formal();
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(45);
					match(T__4);
					setState(46);
					formal();
					}
					}
					setState(51);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(54);
			match(T__5);
			setState(55);
			match(T__6);
			setState(56);
			match(TYPE);
			setState(57);
			match(T__1);
			setState(58);
			expr();
			setState(59);
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

	public static class Feature2Context extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(MyGrammerParser.TYPE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Feature2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature2; }
	}

	public final Feature2Context feature2() throws RecognitionException {
		Feature2Context _localctx = new Feature2Context(_ctx, getState());
		enterRule(_localctx, 8, RULE_feature2);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(T__6);
			setState(62);
			match(TYPE);
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__7) {
				{
				setState(63);
				match(T__7);
				setState(64);
				expr();
				}
			}

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

	public static class FormalContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MyGrammerParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(MyGrammerParser.TYPE, 0); }
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(ID);
			setState(68);
			match(T__6);
			setState(69);
			match(TYPE);
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

	public static class ExprContext extends ParserRuleContext {
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public Id2Context id2() {
			return getRuleContext(Id2Context.class,0);
		}
		public TerminalNode IFKEY() { return getToken(MyGrammerParser.IFKEY, 0); }
		public TerminalNode WHILEKEY() { return getToken(MyGrammerParser.WHILEKEY, 0); }
		public TerminalNode LETKEY() { return getToken(MyGrammerParser.LETKEY, 0); }
		public TerminalNode NEWKEY() { return getToken(MyGrammerParser.NEWKEY, 0); }
		public TerminalNode ISVOIDKEY() { return getToken(MyGrammerParser.ISVOIDKEY, 0); }
		public TerminalNode NOTKEY() { return getToken(MyGrammerParser.NOTKEY, 0); }
		public TerminalNode TRUE() { return getToken(MyGrammerParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(MyGrammerParser.FALSE, 0); }
		public TerminalNode INTEGERS() { return getToken(MyGrammerParser.INTEGERS, 0); }
		public TerminalNode STRING() { return getToken(MyGrammerParser.STRING, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(71);
				id2();
				}
				break;
			case IFKEY:
				{
				setState(72);
				match(IFKEY);
				}
				break;
			case WHILEKEY:
				{
				setState(73);
				match(WHILEKEY);
				}
				break;
			case LETKEY:
				{
				setState(74);
				match(LETKEY);
				}
				break;
			case NEWKEY:
				{
				setState(75);
				match(NEWKEY);
				}
				break;
			case ISVOIDKEY:
				{
				setState(76);
				match(ISVOIDKEY);
				}
				break;
			case NOTKEY:
				{
				setState(77);
				match(NOTKEY);
				}
				break;
			case TRUE:
				{
				setState(78);
				match(TRUE);
				}
				break;
			case FALSE:
				{
				setState(79);
				match(FALSE);
				}
				break;
			case T__3:
				{
				setState(80);
				match(T__3);
				}
				break;
			case INTEGERS:
				{
				setState(81);
				match(INTEGERS);
				}
				break;
			case STRING:
				{
				setState(82);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(85);
			expr2();
			setState(87);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(86);
				match(T__5);
				}
				break;
			}
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

	public static class Expr2Context extends ParserRuleContext {
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ID() { return getToken(MyGrammerParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(MyGrammerParser.TYPE, 0); }
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
	}

	public final Expr2Context expr2() throws RecognitionException {
		Expr2Context _localctx = new Expr2Context(_ctx, getState());
		enterRule(_localctx, 14, RULE_expr2);
		int _la;
		try {
			setState(113);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(109);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__8:
				case T__9:
				case T__10:
				case T__11:
				case T__12:
				case T__13:
					{
					setState(89);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(90);
					expr();
					}
					break;
				case T__14:
				case T__15:
					{
					setState(93);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__14) {
						{
						setState(91);
						match(T__14);
						setState(92);
						match(TYPE);
						}
					}

					setState(95);
					match(T__15);
					setState(96);
					match(ID);
					setState(97);
					match(T__3);
					setState(106);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << IFKEY) | (1L << WHILEKEY) | (1L << LETKEY) | (1L << NEWKEY) | (1L << ISVOIDKEY) | (1L << NOTKEY) | (1L << TRUE) | (1L << FALSE) | (1L << INTEGERS) | (1L << ID) | (1L << STRING))) != 0)) {
						{
						setState(98);
						expr();
						setState(103);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==T__4) {
							{
							{
							setState(99);
							match(T__4);
							setState(100);
							expr();
							}
							}
							setState(105);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						}
					}

					setState(108);
					match(T__5);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(111);
				expr2();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
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

	public static class Id2Context extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MyGrammerParser.ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public Id2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id2; }
	}

	public final Id2Context id2() throws RecognitionException {
		Id2Context _localctx = new Id2Context(_ctx, getState());
		enterRule(_localctx, 16, RULE_id2);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(ID);
			setState(129);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__7:
				{
				{
				setState(116);
				match(T__7);
				setState(117);
				expr();
				}
				}
				break;
			case T__3:
				{
				setState(118);
				match(T__3);
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << IFKEY) | (1L << WHILEKEY) | (1L << LETKEY) | (1L << NEWKEY) | (1L << ISVOIDKEY) | (1L << NOTKEY) | (1L << TRUE) | (1L << FALSE) | (1L << INTEGERS) | (1L << ID) | (1L << STRING))) != 0)) {
					{
					setState(119);
					expr();
					setState(124);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
					while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
						if ( _alt==1 ) {
							{
							{
							setState(120);
							match(T__4);
							setState(121);
							expr();
							}
							} 
						}
						setState(126);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
					}
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61\u0086\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3"+
		"\2\3\2\3\3\3\3\3\3\3\3\5\3\34\n\3\3\3\3\3\3\3\3\3\7\3\"\n\3\f\3\16\3%"+
		"\13\3\3\3\3\3\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\7\5\62\n\5\f\5\16\5"+
		"\65\13\5\5\5\67\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6D\n"+
		"\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b"+
		"V\n\b\3\b\3\b\5\bZ\n\b\3\t\3\t\3\t\3\t\5\t`\n\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\7\th\n\t\f\t\16\tk\13\t\5\tm\n\t\3\t\5\tp\n\t\3\t\3\t\5\tt\n\t\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\7\n}\n\n\f\n\16\n\u0080\13\n\5\n\u0082\n\n\5"+
		"\n\u0084\n\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2\13\20\2\u0096\2\24"+
		"\3\2\2\2\4\27\3\2\2\2\6(\3\2\2\2\b-\3\2\2\2\n?\3\2\2\2\fE\3\2\2\2\16U"+
		"\3\2\2\2\20s\3\2\2\2\22u\3\2\2\2\24\25\5\4\3\2\25\26\7\3\2\2\26\3\3\2"+
		"\2\2\27\30\7\31\2\2\30\33\7\'\2\2\31\32\7\32\2\2\32\34\7\'\2\2\33\31\3"+
		"\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35#\7\4\2\2\36\37\5\6\4\2\37 \7\3\2"+
		"\2 \"\3\2\2\2!\36\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$&\3\2\2\2%#\3"+
		"\2\2\2&\'\7\5\2\2\'\5\3\2\2\2(+\7(\2\2),\5\b\5\2*,\5\n\6\2+)\3\2\2\2+"+
		"*\3\2\2\2,\7\3\2\2\2-\66\7\6\2\2.\63\5\f\7\2/\60\7\7\2\2\60\62\5\f\7\2"+
		"\61/\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\67\3\2\2\2\65"+
		"\63\3\2\2\2\66.\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\7\b\2\29:\7\t\2\2"+
		":;\7\'\2\2;<\7\4\2\2<=\5\16\b\2=>\7\5\2\2>\t\3\2\2\2?@\7\t\2\2@C\7\'\2"+
		"\2AB\7\n\2\2BD\5\16\b\2CA\3\2\2\2CD\3\2\2\2D\13\3\2\2\2EF\7(\2\2FG\7\t"+
		"\2\2GH\7\'\2\2H\r\3\2\2\2IV\5\22\n\2JV\7\24\2\2KV\7\30\2\2LV\7\35\2\2"+
		"MV\7\36\2\2NV\7 \2\2OV\7!\2\2PV\7$\2\2QV\7%\2\2RV\7\6\2\2SV\7&\2\2TV\7"+
		"\60\2\2UI\3\2\2\2UJ\3\2\2\2UK\3\2\2\2UL\3\2\2\2UM\3\2\2\2UN\3\2\2\2UO"+
		"\3\2\2\2UP\3\2\2\2UQ\3\2\2\2UR\3\2\2\2US\3\2\2\2UT\3\2\2\2VW\3\2\2\2W"+
		"Y\5\20\t\2XZ\7\b\2\2YX\3\2\2\2YZ\3\2\2\2Z\17\3\2\2\2[\\\t\2\2\2\\p\5\16"+
		"\b\2]^\7\21\2\2^`\7\'\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\22\2\2bc\7"+
		"(\2\2cl\7\6\2\2di\5\16\b\2ef\7\7\2\2fh\5\16\b\2ge\3\2\2\2hk\3\2\2\2ig"+
		"\3\2\2\2ij\3\2\2\2jm\3\2\2\2ki\3\2\2\2ld\3\2\2\2lm\3\2\2\2mn\3\2\2\2n"+
		"p\7\b\2\2o[\3\2\2\2o_\3\2\2\2pq\3\2\2\2qt\5\20\t\2rt\3\2\2\2so\3\2\2\2"+
		"sr\3\2\2\2t\21\3\2\2\2u\u0083\7(\2\2vw\7\n\2\2w\u0084\5\16\b\2x\u0081"+
		"\7\6\2\2y~\5\16\b\2z{\7\7\2\2{}\5\16\b\2|z\3\2\2\2}\u0080\3\2\2\2~|\3"+
		"\2\2\2~\177\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0081y\3\2\2\2\u0081"+
		"\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083v\3\2\2\2\u0083x\3\2\2\2\u0084"+
		"\23\3\2\2\2\22\33#+\63\66CUY_ilos~\u0081\u0083";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}