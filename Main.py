from Tokenize import tokenize
from Syntax import parse
from GUI import Run_GUI
from Parse import parse_result

# Old Test data
# x.#y.x y


# Test Data From GUI (Catch Nontype)

# data = Run_GUI()
data = '#x.x#y.y#z.z'
print("Code = ", data.strip())

# Tokenize the input data
tokens = tokenize(data)
print("Tokens:", tokens)

parsed_result = parse(data)
print("Parsed result:", parsed_result)
parse_result(parsed_result)
