from Tokenize import tokenize
from Syntax import parse
from GUI import Run_GUI

# Old Test data
''''
data = '''
#x.#y.x y + y
'''
'''

# Test Data From GUI (Catch Nontype)

data = Run_GUI()
print("Code = ", data.strip())

# Tokenize the input data
tokens = tokenize(data)
print("Tokens:", tokens)

parsed_result = parse(data)
print("Parsed result:", parsed_result)

'''
#x.#y.x y + y

'''
