# Initialize variables to hold the evaluation results
reduced = []  # Stores the intermediate reduced expressions
steps = []  # Stores the steps of the reduction process
result = None  # Holds the final evaluation result


# Function to evaluate a lambda expression
def evaluate(expression):
    print("expression : ", expression)
    global result
    global reduced
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
                    print("Reduced : ", reduced)

                    steps.append(str(expression) + " -> " + str(reduced))
                    evaluate(reduced)

                elif isinstance(body, tuple):

                    if expression[0] == 'lambda':
                        reduced = sub(input, body)
                        print("PING")
                        steps.append(str(expression) + " -> " + str(reduced))
                        result = reduced
                        evaluate(result)

                    if expression[0] == 'operator':

                        # Evaluate the operator expression and set reduced

                        left_operand = expression[2][1]
                        right_operand = expression[3][1]
                        operator = expression[1]

                        print(left_operand, operator, right_operand)

                        if operator == '+':
                            if isinstance(left_operand, str) or isinstance(right_operand, str):
                                reduced = str(left_operand) + " " + str(operator) + " " + str(right_operand)
                            else:
                                reduced = left_operand + right_operand

                        elif operator == '-':
                            if isinstance(left_operand, str) or isinstance(right_operand, str):
                                reduced = str(left_operand) + " " + str(operator) + " " + str(right_operand)
                            else:
                                reduced = left_operand - right_operand

                        elif operator == '*':
                            if isinstance(left_operand, str) or isinstance(right_operand, str):
                                reduced = str(left_operand) + " " + str(operator) + " " + str(right_operand)
                            else:
                                reduced = left_operand * right_operand

                        elif operator == '/':
                            if isinstance(left_operand, str) or isinstance(right_operand, str):
                                reduced = str(left_operand) + " " + str(operator) + " " + str(right_operand)
                            else:
                                reduced = left_operand / right_operand

                        steps.append(str(expression) + " -> " + str(reduced))
                        print("Returning...", reduced)
                        result = reduced
                        return reduced, steps

                    try:
                        reduced = expression[0][1] + " " + expression[1][1]
                        steps.append(str(expression) + " -> " + str(reduced))
                        result = reduced
                        return reduced, steps
                    except IndexError:
                        pass

                elif expression[0] == 'lambda':
                    print("subbing because of lambda")
                    result = sub(input, body)
                    print("reduced : ", result)
                    steps.append(str(expression) + " -> " + str(result))
                    break

                else:
                    try:
                        if body[3]:
                            print("...")
                    except IndexError:
                        try:
                            result = str(expression[0][1]) + " " + str(expression[1][1])
                            steps.append(str(expression) + " -> " + str(result))
                            return result, steps
                        except IndexError:
                            pass
                        steps.append(str(expression) + " -> " + str(body))
                        reduced = body
                        return reduced, steps

                    steps.append(str(expression) + " -> " + str(reduced))

                    return reduced, steps

            elif expression[_] == 'const':
                try:

                    # Concatenate constants if present
                    result = str(expression[1]) + ' ' + str(expression[3])
                    steps.append(str(expression) + " -> " + str(result))
                    break

                except IndexError:
                    result = expression[1]
                    steps.append(str(expression) + " -> " + str(result))
                    break

    except TypeError:
        result = expression
        steps.append(str(expression) + " -> " + str(result))
        return result, steps

    return result, steps


# Function to perform substitution in lambda expressions
def sub(input, body):
    global constants
    temp_input = None

    # Convert the body to a nested list
    new_body = convert_to_nested_list(body)
    h = flatten_list(new_body)
    for _ in range(len(h)):
        if h[_] == input:
            temp_input = True
            break
    if not temp_input:
        return body

    if input is None:
        new_body = flatten_list(new_body)
        for _ in range(0, len(new_body), 2):
            new_body[_] = " "
        new_body = clean_list(new_body)
        temp = ''
        for _ in range(len(new_body)):
            temp = temp + ' ' + str(new_body[_])

        return temp

    if any(constants):
        pass
    else:
        constants = Check_Const(new_body)

    if new_body[0] == "operator":
        if temp_input and not any(constants):
            return body
        new_body_copy = convert_to_nested_list(body)
        elements = 0
        for _ in range(2, len(h), 2):
            elements += 1
        if elements < 3:
            return convert_to_nested_tuple(new_body_copy)

        else:
            for _ in range(len(h)):
                if h[_] == 'var':
                    if h[_ + 1] == input:
                        h[_] = "const"
                        h[_ + 1] = h[7]
                        h[6] = ''
                        h[7] = ''

        h = clean_list(h)
        h = convert_to_nested_list(h)
        h[2] = [h[2], h[3]]
        h[3] = " "
        h[4] = [h[4], h[5]]
        h[5] = " "
        try:
            if h[6]:
                pass
        except IndexError:
            pass
        h = clean_list(h)
        return convert_to_nested_tuple(h)

    reset_const_flag()
    if any(constants):
        new_body = clean_list(change_const(new_body, input))
        reset_const_flag()
        try:
            new_body[2] = flatten_list(new_body[2])
            for _ in range(0, len(new_body[2]), 2):
                new_body[2][_] = [str(new_body[2][_]), str(new_body[2][_ + 1])]
                new_body[2][_ + 1] = " "
        except IndexError:
            new_body = flatten_list(new_body)
            for _ in range(len(new_body)):
                if new_body[_] == "lambda":
                    pass
            for _ in range(0, len(new_body), 2):
                new_body[_] = str(new_body[_]), str(new_body[_ + 1])
                new_body[_ + 1] = " "
            new_body = clean_list(new_body)
            return new_body

        new_body = clean_list(new_body)
        if constants:
            temp = sub(new_body[1], new_body[2])
            return temp

        new_body = convert_to_nested_tuple(new_body)
        return new_body
    else:
        return convert_to_nested_tuple(new_body)


def reset_const_flag():
    global const_flag
    const_flag = False


def change_const(nested_list, input):
    global const_flag
    if isinstance(nested_list, list):
        for index in range(len(nested_list)):
            if isinstance(nested_list[index], list):
                change_const(nested_list[index], input)
            else:
                if nested_list[index] == 'var':
                    if not const_flag:
                        if nested_list[index + 1] == input:
                            nested_list[index] = 'const'
                            nested_list[index + 1] = constants[0]
                            constants.pop(0)
                            const_flag = True

    return nested_list


const_flag = False
constants = []


def Check_Const(nested_list):
    global const_flag
    if isinstance(nested_list, list):
        for index in range(len(nested_list)):
            if isinstance(nested_list[index], list):
                Check_Const(nested_list[index])
            else:
                if nested_list[index] == 'const':
                    constants.append(nested_list[index + 1])
                    nested_list[index] = ' '
                    nested_list[index + 1] = ' '

    return constants


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
        cleaned_list = [clean_list(item) for item in nested_list if clean_list(item)]
        return [item for item in cleaned_list if item != []]
    else:
        return nested_list if nested_list != " " else None


# Convert nested lists back to nested tuples
def convert_to_nested_tuple(data):
    if isinstance(data, list):
        return tuple(convert_to_nested_tuple(item) for item in data)
    elif isinstance(data, tuple):
        return tuple(convert_to_nested_tuple(item) for item in data)
    else:
        return data


# Flattens Nested Lists
def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list
