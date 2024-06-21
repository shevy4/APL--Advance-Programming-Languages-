from ply import yacc
from Tokenize import tokens

variables = []


# Define grammar rules

def p_expression_lambda(p):
    """expression : LAMBDA VARIABLE DOT LPAREN expression RPAREN
                  | LAMBDA VARIABLE DOT expression
                  | expression expression
                  | VARIABLE

                  """
    if len(p) == 2:
        print(p[1][0])
        p[0] = ('variable', p[1])




    elif len(p) == 5 and p[1] == '#':
        print("PING 5")
        for _ in range(len(p)):
            print(p[_])
        p[0] = ('lambda', p[2], (p[4]))
        print(p[0])
        print(variables)

    elif len(p) == 7:
        print("PING")
        p[0] = ('lambda', p[2], ('variable', p[4]))

    elif len(p) == 4:
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
