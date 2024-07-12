from ply import yacc
from Tokenize import tokens

error = None


# Define grammar rules

def p_expression_lambda(p):
    """expression : LAMBDA VARIABLE DOT expression"""

    p[0] = ('lambda', p[2], p[4])


def p_expression_application(p):
    """expression : expression expression"""
    p[0] = (p[1], p[2])


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
    """expression : OPERATOR expression expression"""

    p[0] = ('operator', p[1], p[2], p[3])




# Handle parsing errors
def p_error(p):
    global error
    if p:
        error = "Syntax error at token" + str({p.type}) + ":" + str({p.value})

    else:
        error = "Syntax error at EOF"


# Create the parser
parser = yacc.yacc()


# Parse the given code
def parse(code):
    result = parser.parse(code)
    if result:
        return result
    else:
        return "Parser error \n" + error
