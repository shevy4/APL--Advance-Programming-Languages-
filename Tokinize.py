import ply.lex as lex

# tokens
tokens = (
    'LAMBDA',  # The lambda symbol '#'
    'DOT',  # The dot '.'
    'LPAREN',  # Left parenthesis '('
    'RPAREN',  # Right parenthesis ')'
    'VARIABLE',  # Variables
)

# Regular expression rules for simple tokens
t_LAMBDA = r'\#'
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# A regular expression rule with some action code to handle variables
def t_VARIABLE(t):
    r'[a-z]'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print(f"Illegal character found '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test data
data = '''
#x.(x y)
'''
lexer.input(data)

# Main
while True:
    tokens = []

    # Tokenize
    tok = lexer.token()
    # Exit when tokenized
    if not tok:
        break
    # Add to token list
    tokens.append(f"{tok.value} {tok.type}")

    print(tokens)
