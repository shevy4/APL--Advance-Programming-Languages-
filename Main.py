from Tokenize import tokenize
from Syntax import parse

# Test data
data = '''
#x.(x)
'''
print("Code = ", data.strip())

# Tokenize the input data
tokens = tokenize(data)

parsed_result = parse(data)
print("Parsed result:", parsed_result)