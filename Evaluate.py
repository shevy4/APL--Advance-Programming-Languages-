# Initialize variables to hold the evaluation results
reduced = []  # Stores the intermediate reduced expressions
steps = []  # Stores the steps of the reduction process
result = None  # Holds the final evaluation result


# Function to evaluate a lambda expression
def evaluate(expression):
    global result
    global reduced
    print("expression =", expression)
    try:
        for _ in range(len(expression)):

            if expression[_] == 'lambda':
                # Identify the input variable for the lambda expression
                input = expression[_ + 1]
            if isinstance(expression[_], tuple):
                body = expression[_]

                if body[0] == 'lambda':
                    # If the body is another lambda expression, perform substitution
                    reduced = sub(input, body)
                    steps.append(str(expression) + " -> " + str(reduced))
                    print("reduced =", reduced)
                    evaluate(reduced)

                elif body[0] == 'operator':
                    print("Operation")

                else:
                    const = False
                    for __ in range(1, len(body)):

                        # Check if the body contains a constant
                        if body[__][0] == 'const':
                            const = True
                            break

                    if not const:
                        try:
                            result = body[1][1] + body[2][1]
                        except IndexError:
                            result = body[1]

                    else:

                        # Perform substitution if the body contains variables
                        new_expression = sub(input, body)
                        steps.append(str(expression) + " -> " + str(new_expression))
                        evaluate(new_expression)

            elif expression[_] == 'const':
                try:

                    # Concatenate constants if present
                    result = str(expression[1]) + ' ' + str(expression[3])
                    break

                except IndexError:
                    result = expression[1]
                    break

            elif len(expression) == 1:
                result = expression
                break

    except TypeError:
        result = expression
        return result, steps

    return result, steps


# Function to perform substitution in lambda expressions
def sub(input, body):
    # Convert the body to a nested list
    new_body = convert_to_nested_list(body)
    for _ in range(1, len(new_body[2])):
        try:

            # Checks If The Body Of Function Contains Variables & Constants
            if new_body[2][_][0] == 'var':
                if new_body[2][_][1] == input:
                    for __ in range(len(new_body[2])):
                        if new_body[2][__][0] == 'const':
                            # Substitute variable with constant
                            new_body[2][_] = ['const', new_body[2][__][1]]
                            new_body[2][__] = ' '

                            # Clean & Convert back to nested tuple
                            new_body = clean_list(new_body)
                            return convert_to_nested_tuple(new_body)

                    for __ in range(len(new_body[2])):
                        if new_body[2][__][0] == 'var':
                            if new_body[2][__ + 1][0] == 'var':
                                return new_body[2][__][1] + new_body[2][__ + 1][1]
                            return new_body[2][__][1]

                else:
                    return convert_to_nested_tuple(new_body)

            # Checks If The Body Of Function Starts With Lambda
            else:
                if new_body[2][0] == 'lambda':
                    return convert_to_nested_tuple(new_body)
                const = False
                for __ in range(len(new_body)):
                    if new_body[__][0] == 'const':
                        const = True
                if not const:
                    if new_body[2][0] == 'var':
                        return new_body[2][1]
                else:
                    for __ in range(len(new_body)):
                        if new_body[__][0] == 'var':
                            if new_body[__][1] == input:
                                for count in range(len(new_body)):
                                    if new_body[count][0] == 'const':
                                        new_body[__] = ['const', new_body[count][1]]
                                        new_body[count] = " "
                                        break
                    new_body = clean_list(new_body)
                    new_body = convert_to_nested_tuple(new_body)
                    try:
                        return new_body[1] + new_body[2]
                    except IndexError:
                        return new_body[1]

        except TypeError:
            for __ in range(len(new_body)):
                if new_body[__][0] == 'var':
                    if new_body[__][1] == input:
                        return new_body[__ + 1][1]


# Converts nested tuples to nested lists
def convert_to_nested_list(data):
    if isinstance(data, tuple):
        return [convert_to_nested_list(item) for item in data]
    elif isinstance(data, list):
        return [convert_to_nested_list(item) for item in data]
    else:
        return data


# Cleans nested lists by removing empty strings
def clean_list(nested_list):
    if isinstance(nested_list, list):
        return [clean_list(item) for item in nested_list if item != " "]
    else:
        return nested_list


# Convert nested lists back to nested tuples
def convert_to_nested_tuple(data):
    if isinstance(data, list):
        return tuple(convert_to_nested_tuple(item) for item in data)
    elif isinstance(data, tuple):
        return tuple(convert_to_nested_tuple(item) for item in data)
    else:
        return data
