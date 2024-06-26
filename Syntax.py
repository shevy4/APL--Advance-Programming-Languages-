from ply import yacc
from Tokenize import tokens


# Define grammar rules

def p_expression_lambda(p):
    """expression : LAMBDA VARIABLE DOT expression"""
    p[0] = ('lambda', p[2], p[4])


def p_expression_application(p):
    """expression : expression expression"""
    p[0] = ('apply', p[1], p[2])


def p_expression_variable(p):
    """expression : VARIABLE"""

    p[0] = ('var', p[1])


def p_expression_constant(p):
    """expression : CONSTANT"""
    p[0] = ('const', int(p[1]))


def p_expression_operator(p):
    """expression : expression OPERATOR expression"""

    p[0] = ('operator', p[2], p[1], p[3])


def p_expression_parenthesized(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]


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
