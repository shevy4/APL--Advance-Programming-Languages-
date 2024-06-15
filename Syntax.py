from ply import yacc
from Tokenize import tokens


# Define grammar rules

def p_expression_lambda(p):
    """expression : LAMBDA VARIABLE DOT VARIABLE
                  | LAMBDA VARIABLE DOT LPAREN VARIABLE RPAREN"""

    # | LAMBDA VARIABLE DOT LPAREN VARIABLE RPAREN"""
    if len(p) < 6:
        p[0] = ('lambda', p[2])
    else:
        p[0] = ('lambda', p[5])


def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}: '{p.value}'")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()


def parse(code):
    result = parser.parse(code)
    if result:
        return result
    else:
        print("Parser error")
