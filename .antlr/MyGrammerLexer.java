// Generated from /home/garoz/2022/20222/compiladores/lab0/MyGrammer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MyGrammerLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, CLASSKEY=4, INHERITSKEY=5, DIGIT=6, LOWER=7, UPPER=8, 
		TYPE=9, LETTERS=10, WHITESPACE=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "A", "B", "C", "D", "E", "F", "G", "H", "I", 
			"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 
			"X", "Y", "Z", "CLASSKEY", "INHERITSKEY", "DIGIT", "LOWER", "UPPER", 
			"TYPE", "LETTERS", "WHITESPACE"
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


	public MyGrammerLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyGrammer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r\u00ab\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3"+
		"\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16"+
		"\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25"+
		"\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34"+
		"\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3"+
		" \3 \3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\6$\u00a0\n$\r$\16$\u00a1\3"+
		"%\3%\5%\u00a6\n%\3&\3&\3&\3&\2\2\'\3\3\5\4\7\5\t\2\13\2\r\2\17\2\21\2"+
		"\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2"+
		"\65\2\67\29\2;\2=\6?\7A\bC\tE\nG\13I\fK\r\3\2 \4\2CCcc\4\2DDdd\4\2EEe"+
		"e\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2"+
		"NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4"+
		"\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\62;\3\2c|\3\2C\\"+
		"\5\2\13\f\17\17\"\"\2\u0093\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2=\3\2"+
		"\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2"+
		"\2K\3\2\2\2\3M\3\2\2\2\5O\3\2\2\2\7Q\3\2\2\2\tS\3\2\2\2\13U\3\2\2\2\r"+
		"W\3\2\2\2\17Y\3\2\2\2\21[\3\2\2\2\23]\3\2\2\2\25_\3\2\2\2\27a\3\2\2\2"+
		"\31c\3\2\2\2\33e\3\2\2\2\35g\3\2\2\2\37i\3\2\2\2!k\3\2\2\2#m\3\2\2\2%"+
		"o\3\2\2\2\'q\3\2\2\2)s\3\2\2\2+u\3\2\2\2-w\3\2\2\2/y\3\2\2\2\61{\3\2\2"+
		"\2\63}\3\2\2\2\65\177\3\2\2\2\67\u0081\3\2\2\29\u0083\3\2\2\2;\u0085\3"+
		"\2\2\2=\u0087\3\2\2\2?\u008d\3\2\2\2A\u0096\3\2\2\2C\u0098\3\2\2\2E\u009a"+
		"\3\2\2\2G\u009c\3\2\2\2I\u00a5\3\2\2\2K\u00a7\3\2\2\2MN\7=\2\2N\4\3\2"+
		"\2\2OP\7}\2\2P\6\3\2\2\2QR\7\177\2\2R\b\3\2\2\2ST\t\2\2\2T\n\3\2\2\2U"+
		"V\t\3\2\2V\f\3\2\2\2WX\t\4\2\2X\16\3\2\2\2YZ\t\5\2\2Z\20\3\2\2\2[\\\t"+
		"\6\2\2\\\22\3\2\2\2]^\t\7\2\2^\24\3\2\2\2_`\t\b\2\2`\26\3\2\2\2ab\t\t"+
		"\2\2b\30\3\2\2\2cd\t\n\2\2d\32\3\2\2\2ef\t\13\2\2f\34\3\2\2\2gh\t\f\2"+
		"\2h\36\3\2\2\2ij\t\r\2\2j \3\2\2\2kl\t\16\2\2l\"\3\2\2\2mn\t\17\2\2n$"+
		"\3\2\2\2op\t\20\2\2p&\3\2\2\2qr\t\21\2\2r(\3\2\2\2st\t\22\2\2t*\3\2\2"+
		"\2uv\t\23\2\2v,\3\2\2\2wx\t\24\2\2x.\3\2\2\2yz\t\25\2\2z\60\3\2\2\2{|"+
		"\t\26\2\2|\62\3\2\2\2}~\t\27\2\2~\64\3\2\2\2\177\u0080\t\30\2\2\u0080"+
		"\66\3\2\2\2\u0081\u0082\t\31\2\2\u00828\3\2\2\2\u0083\u0084\t\32\2\2\u0084"+
		":\3\2\2\2\u0085\u0086\t\33\2\2\u0086<\3\2\2\2\u0087\u0088\5\r\7\2\u0088"+
		"\u0089\5\37\20\2\u0089\u008a\5\t\5\2\u008a\u008b\5-\27\2\u008b\u008c\5"+
		"-\27\2\u008c>\3\2\2\2\u008d\u008e\5\31\r\2\u008e\u008f\5#\22\2\u008f\u0090"+
		"\5\27\f\2\u0090\u0091\5\21\t\2\u0091\u0092\5+\26\2\u0092\u0093\5\31\r"+
		"\2\u0093\u0094\5/\30\2\u0094\u0095\5-\27\2\u0095@\3\2\2\2\u0096\u0097"+
		"\t\34\2\2\u0097B\3\2\2\2\u0098\u0099\t\35\2\2\u0099D\3\2\2\2\u009a\u009b"+
		"\t\36\2\2\u009bF\3\2\2\2\u009c\u009f\5E#\2\u009d\u00a0\5I%\2\u009e\u00a0"+
		"\5A!\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1"+
		"\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2H\3\2\2\2\u00a3\u00a6\5C\"\2\u00a4"+
		"\u00a6\5E#\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6J\3\2\2\2\u00a7"+
		"\u00a8\t\37\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\b&\2\2\u00aaL\3\2\2\2"+
		"\6\2\u009f\u00a1\u00a5\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}