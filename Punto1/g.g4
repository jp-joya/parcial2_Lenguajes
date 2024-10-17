grammar g;

// Reglas del parser
expr:   expr op=('+'|'-') expr     # OperacionBinaria
    |   expr op=('*'|'/') expr     # OperacionMultiplicacionDivision
    |   COMPLEX                    # Complejo
    |   REAL                       # Real
    |   '(' expr ')'               # Parentesis
    ;

// Reglas del lexer
COMPLEX: [0-9]+ ('+'|'-') [0-9]+ 'j';  // Números complejos
REAL: [0-9]+('.'[0-9]+)?;              // Números enteros y decimales
WS: [ \t\r\n]+ -> skip;                // Ignorar espacios en blanco

