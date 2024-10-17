grammar g;

program: statement* EOF ;

statement
    : expr ';'                          # expressionStatement
    | ID '=' expr ';'                    # assignmentStatement
    | 'fft' '(' ID ')' ';'               # fftStatement
    ;

expr
    : 'Π' '(' expr '/' expr ')'         # rectangularPulse
    | 'Λ' '(' expr '/' expr ')'         # triangularPulse
    | 'sign' '(' expr ')'               # signFunction
    | 'u' '(' expr ')'                  # unitStepFunction
    | 'δ' '(' expr ')'                  # diracDelta
    | 'cos' '(' expr ')'                # cosineFunction
    | 'sin' '(' expr ')'                # sineFunction
    | expr '+' expr                     # addition
    | expr '-' expr                     # subtraction
    | expr '*' expr                     # multiplication
    | expr '/' expr                     # division
    | '(' expr ')'                      # parenthesizedExpression
    | INT                               # integer
    | FLOAT                             # float
    | ID                                # variableReference
    ;

ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
INT    : [0-9]+ ;
FLOAT  : [0-9]+'.'[0-9]* ;
WS     : [ \t\r\n]+ -> skip ;

