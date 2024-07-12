import ply.lex as lex

# Define tokens
tokens = (
    'LAMBDA',  # The lambda symbol '#'
    'DOT',  # The dot '.'
    'LPAREN',  # Left parenthesis '('
    'RPAREN',  # Right parenthesis ')'
    'VARIABLE',  # Variables
    'CONSTANT',  # Constants
    'OPERATOR',  # Operator
)

# Regular expression rules for simple tokens
t_LAMBDA = r'\#'
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CONSTANT = r'[0-9]+'
t_OPERATOR = r'[\+\-\*\/]'


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


# Main

def tokenize(data):
    lexer.input(data)
    token_list = []
    # Tokenize
    while True:
        tok = lexer.token()
        # Exit when tokenized
        if not tok:
            break
        # Add to token list
        token_list.append(f"{tok.value} {tok.type}")
    return token_list
