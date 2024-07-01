from Tokenize import tokenize
from Syntax import parse
from Evaluate import parse_result
from GUI import Run_GUI

# Old Test data
#data = #x.#y.x y + y


data = Run_GUI()
data = data.replace('(', '').replace(')','')

print("Code = ", data.strip())

# Tokenize the input data
tokens = tokenize(data)
print("Tokens:", tokens)

parsed_result = parse(data)
print("Parsed result:", parsed_result)
parse_result(parsed_result)
