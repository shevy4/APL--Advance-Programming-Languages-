from Tokenize import tokenize
from Syntax import parse
from GUI import Run_GUI

# Old Test data
''''
data = '''
#x.(x)
'''
'''

# Test Data From GUI (Catch Nontype)

data = Run_GUI()
print("Code = ", data.strip())

# Tokenize the input data
tokens = tokenize(data)

parsed_result = parse(data)
<<<<<<< Updated upstream
print("Parsed result:", parsed_result)
=======
print("Parsed result:", parsed_result)

'''
#x.#y.x y + y

'''
>>>>>>> Stashed changes
