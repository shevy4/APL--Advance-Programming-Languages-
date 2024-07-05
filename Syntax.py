import time

from ply import yacc
from Tokenize import tokens

variables = []
error = None


# Define grammar rules

def p_expression_lambda(p):
    """expression : LAMBDA VARIABLE DOT expression"""
    p[0] = ('lambda', p[2], p[4])


def p_expression_application(p):
    """expression : expression expression"""
    if isinstance(p[1], tuple) and p[1][0] == 'body':
        # If the first expression is already a body, append to it
        p[0] = ('body', *p[1][1:], p[2])
    elif isinstance(p[2], tuple) and p[2][0] == 'body':
        # If the second expression is already a body, append the first expression
        p[0] = ('body', p[1], *p[2][1:])
    else:
        p[0] = ('body', p[1], p[2])


def p_expression_parens(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_expression_variable(p):
    """expression : VARIABLE"""
    p[0] = ('var', p[1])


def p_expression_constant(p):
    """expression : CONSTANT"""
    p[0] = ('const', int(p[1]))


def p_expression_operator(p):
    """expression : expression OPERATOR expression"""
    p[0] = ('operator', p[2], p[1], p[3])


def p_expression_body(p):
    """expression : expression expression expression"""
    if p[1][0] == 'lambda' and p[2][0] == 'lambda' and p[3][0] == 'const':
        p[0] = ('body', p[1], p[2], p[3])
    else:
        p[0] = ('body', p[1], p[2], p[3])


def p_expression_inputs(p):
    """expression : expression expression expression expression"""
    if p[1][0] == 'lambda' and p[2][0] == 'lambda' and p[3][0] == 'const' and p[4][0] == 'const':
        p[0] = (p[1][0], p[1][1], (p[1][2], p[3]), p[2], p[4])
    else:
        p[0] = ('body', p[1], p[2], p[3], p[4])


def p_error(p):
    global error
    if p:
        #print(f"Syntax error at token {p.type}: '{p.value}'")
        error = "Syntax error at token" + str({p.type}) + ":" + str({p.value})

    else:
        #print("Syntax error at EOF")
        error = "Syntax error at EOF"

parser = yacc.yacc()


def parse(code):
    result = parser.parse(code)
    if result:
        return result
    else:
        return "Parser error \n" + error
