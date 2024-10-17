grammar g;

// Reglas principales
program : statement+ ;
statement : mapStmt | filterStmt | expr NEWLINE ;

mapStmt    : 'MAP' '(' function ',' iterable ')' ;
filterStmt : 'FILTER' '(' function ',' iterable ')' ;

function   : ID ;
iterable   : '[' exprList ']' | '(' exprList ')' ;

exprList   : expr (',' expr)* ;
expr       : NUMBER | STRING | ID | functionCall ;

functionCall : ID '(' exprList ')' ;

// Tokens básicos
ID         : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER     : [0-9]+ ;
STRING     : '"' .*? '"' ;
NEWLINE    : '\r'? '\n' ;
WS         : [ \t]+ -> skip ;

