grammar KobraV2;

programa: instruccion* EOF;

instruccion
    : declaracion
    | asignacion
    | impresion
    | si_stmt
    | while_stmt
    | for_stmt
    | expresion_stmt
    ;

bloque: '{' instruccion* '}';

declaracion: TIPO ID ('=' expresion)? ';';
asignacion: ID '=' expresion ';';
impresion: 'IMPRIMIR' '(' expresion ')' ';';

si_stmt: 'SI' '(' expresion ')' bloque ('SINO' bloque)?;
while_stmt: 'MIENTRAS' '(' expresion ')' bloque;
for_stmt: 'PARA' '(' asignacion_for ';' expresion ';' asignacion_for ')' bloque;
asignacion_for: ID '=' expresion;
expresion_stmt: expresion ';';

expresion
    : expresion op=('Y' | 'O') expresion                  # OpLogica
    | expresion op=('==' | '!=') expresion                # OpIgualdad
    | expresion op=('<' | '>' | '<=' | '>=') expresion    # OpRelacional
    | expresion op=('+' | '-') expresion                  # OpAditiva
    | expresion op=('*' | '/') expresion                  # OpMultiplicativa
    | '(' expresion ')'                                   # Parentesis
    | ID                                                  # Variable
    | INT                                                 # Entero
    | FLOAT                                               # Flotante
    | STRING                                              # Cadena
    | BOOL_LIT                                            # Booleano
    ;

// --- LEXER ---

// CAMBIO: Tipos en Español
TIPO: 'ENTERO' | 'FLOTANTE' | 'CADENA' | 'BOOLEANO';

// CAMBIO: Booleanos en Español
BOOL_LIT: 'VERDADERO' | 'FALSO';

SI: 'SI';
SINO: 'SINO';
MIENTRAS: 'MIENTRAS';
PARA: 'PARA';
IMPRIMIR: 'IMPRIMIR';

Y: 'Y';
O: 'O';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ~["]* '"';
COMENTARIO: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;