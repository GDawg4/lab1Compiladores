grammar MyGrammer;

/*PARSER RULES*/
program  
    :   meat=classP end=';';

classP
    :   CLASSKEY TYPE (INHERITSKEY TYPE)? '{' (feature)* '}'
;

feature  
    :   ID 
    ( 
        feature1 
    |   feature2
    )
    ';'
;

feature1
    :   '(' (formal (',' formal)*)? ')' ':' TYPE '{' expr '}'
;

feature2 
    :   ':' TYPE ('<-' expr)?
;

formal
    :   ID ':' TYPE;

expr
    : 
    (
            id2
        |   (IFKEY expr THENKEY expr ELSEKEY expr FIKEY)
        |   (WHILEKEY expr LOOPKEY expr POOLKEY)
        |   (LETKEY ID ':' TYPE ('<-' expr)? (',' ID ':' TYPE ('<-' expr)?)* INKEY expr)
        |   NEWKEY TYPE
        |   (ISVOIDKEY expr)
        |   NOTKEY 
        |   'true' 
        |   'false' 
        |   '(' expr ')'
        |   INTEGERS 
        |   STRING
        |   ('{' (expr ';')+ '}')
        |   '~' expr
    ) 
    expr2 (')')?
;

expr2
    :   
    (
        (
                PLUS
            |   MINUS
            |   STAR 
            |   SLASH 
            |   LOWERTHAN
            |   EQUALS
            |   LOWEREQUAL
        ) 

        expr 
        | ('@' TYPE)? '.' ID '(' (expr (',' expr)*)? ')' 
    ) expr2
    |
;

id2
    : 
        ID 
    (   
        ('<-' expr)
    |   '(' (expr(',' expr)*)? 
    |
    )
;


/*TOKENS & KEYWORDS*/
fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];


COMMENTS        : (('--' (ANYSET)* [\n]) | ('(*' (ANYSET)* '*)')) -> skip;

PLUS            : '+';
MINUS           : '-';
STAR            : '*';
SLASH           : '/';
LOWERTHAN       : '<';
EQUALS          : '=';
LOWEREQUAL      : '<=';

IFKEY           : I F;
LOOPKEY         : L O O P;
ELSEKEY         : E L S E;
THENKEY         : T H E N;
WHILEKEY        : W H I L E;
CLASSKEY        : C L A S S;
INHERITSKEY     : I N H E R I T S;
FIKEY           : F I;
INKEY           : I N;
LETKEY          : L E T;
NEWKEY          : N E W;
POOLKEY         : P O O L;
ISVOIDKEY       : I S V O I D;
NOTKEY          : N O T;

TYPE            : UPPER(LETTERS|DIGIT|'_')*;

ID              : (UPPER|LOWER|'_'|DIGIT)+;
OBJECT          : LOWER(LETTERS|DIGIT)+;
ALPHANUMERIC    : (DIGIT|LETTERS);

DIGIT           : [0-9];
LOWER           : [a-z];
UPPER           : [A-Z];
INTEGERS        : DIGIT+;

LETTERS         : (LOWER|UPPER);
STRING          : '"' ANYSET* '"';

fragment ANYSET : (LETTERS|DIGIT|'\''|'.'|'('|')'|':'|','|'*'|'-'|'_'|'>'|'?'|'/'|[ \r]|'='|'\\')+;

WHITESPACE      : [ \t\r\n]+ -> skip;