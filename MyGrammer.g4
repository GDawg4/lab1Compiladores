grammar MyGrammer;

/*PARSER RULES*/
program  
    :   (meat=classP end=';')+;

classP
    :   CLASSKEY name=TYPE (INHERITSKEY inheritName=TYPE)? '{' features '}'
;

features:
    feature*
;

feature  
    :   name=ID
    (
        featureMethod=method
    |   featureAttr=attribute
    )
    ';'
;

method
    :   '(' argumentList=arguments ')' ':' returnType=TYPE '{' mainExpr=expr '}'
;

arguments
    : (formal (',' formal)*)?
;

attribute
    :   ':' typeName=TYPE ('<-' attrExpr=expr)?
;

formal
    :   name=ID ':' typeName=TYPE;

expr
    :
    (
            calls=overwrite
        |   selfE = 'self'
        |   stringE = STRING
        |   ifE = ifExpr
        |   whileE = whileExpr
        |   let = letExpr
        |   newDeclaration = declaration
        |   isVoid = isVoidExpr
        |   notE = notExpr
        |   boolE = boolExpr
        |   parenE = parenExpr
        |   innerExpr=multipleExpr
        |   negation = negationExpr
        |   intE = INTEGERS
    )
    (nextExpr=operations| )
;

boolExpr:
        trueE = 'true'
        |   falseE = 'false'
;

parenExpr
    : '(' expr ')'
;

negationExpr
    : '~' expr
;

notExpr
    : NOTKEY expr
;

isVoidExpr
    : ISVOIDKEY expr
;

whileExpr
    : (WHILEKEY cond=expr LOOPKEY mainExpr=expr POOLKEY)
;

ifExpr
    : (IFKEY cond=expr THENKEY thenExpr=expr ELSEKEY elseExpr=expr FIKEY)
;

letExpr
    : (LETKEY initial=initialExpr (',' initialExpr)* INKEY mainExpr=expr)
;
initialExpr
    : name=ID ':' typeName=TYPE ('<-' actualExpr=expr)?
;

declaration
    : NEWKEY typeName=TYPE
;

multipleExpr
    : '{' (expr ';')+ '}'
;

operations
    :   
    (
        (
                PLUS
            |   MINUS
            |   STAR 
            |   SLASH 
            |   lower = LOWERTHAN
            |   greater = GREATERTHAN
            |   equal = EQUALS
            |   lowerE = LOWEREQUAL
            |   greaterE = GREATEREQUAL
        )
        rightSide = expr
        | mCall = methodCall
    ) operations #NotEmpty
    | #Escape
;

methodCall
    : heritage=atOperator? '.' methodName=ID '(' (expr (',' expr)*)? ')'
;

atOperator
    : '@' parentName=TYPE
;

overwrite
    : 
        name=ID
        (
        attr=attrWrite
        |   fun=funCall
        |
    )
;

attrWrite
    :
        ('<-' attrInner=expr)
;

funCall
    :
        '(' (expr(',' expr)*)? ')'
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
GREATERTHAN     : '>';
EQUALS          : '=';
LOWEREQUAL      : '<=';
GREATEREQUAL    : '>=';

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

INTEGERS        : DIGIT+;
ID              : LETTERS(UPPER|LOWER|'_'|DIGIT)*;
OBJECT          : LOWER(LETTERS|DIGIT)+;
ALPHANUMERIC    : (DIGIT|LETTERS);

DIGIT           : [0-9];
LOWER           : [a-z];
UPPER           : [A-Z];

LETTERS         : (LOWER|UPPER);
STRING          : '"' ANYSET* '"';

fragment ANYSET : (LETTERS|DIGIT|'\''|'.'|'('|')'|':'|','|'*'|'-'|'_'|'>'|'?'|'/'|[ \r]|'='|'\\')+;

WHITESPACE      : [ \t\r\n]+ -> skip;