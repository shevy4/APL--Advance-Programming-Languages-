reduced = []
steps = []
result = None


def evaluate(expression):
    global result
    global reduced
    for _ in range(len(expression)):
        if expression[_] == 'lambda':
            input = expression[_ + 1]
        if isinstance(expression[_], tuple):
            body = expression[_]
            if body[0] == 'lambda':
                reduced = sub(input, body)
                #print(expression, " -> ", reduced)
                steps.append(str(expression) + " -> " + str(reduced))
                evaluate(reduced)

            else:
                #print(body[0], " != ", 'lambda (Single)')
                const = False
                for __ in range(1, len(body)):
                    if body[__][0] == 'const':
                        const = True
                        break
                if not const:
                    try:
                        #print(body[1][1] + body[2][1])
                        result = body[1][1] + body[2][1]
                    except IndexError:
                        #print("Single Abstraction")
                        #print(body[1])
                        result = body[1]
                else:
                    #print('Constant Found')
                    new_expression = sub(input, body)
                    #print(expression, ' -> ', new_expression)
                    steps.append(str(expression) + " -> " + str(new_expression))
                    evaluate(new_expression)
        elif expression[_] == 'const':
            try:
                #print(expression[1], expression[3])
                result = str(expression[1]) + ' ' + str(expression[3])
                break
            except IndexError:
                #print(expression[1])
                result = expression[1]
                break
    return result, steps


def sub(input, body):
    new_body = convert_to_nested_list(body)
    for _ in range(1, len(new_body[2])):
        try:
            if new_body[2][_][0] == 'var':
                if new_body[2][_][1] == input:
                    for __ in range(len(new_body[2])):
                        if new_body[2][__][0] == 'const':
                            new_body[2][_] = ['const', new_body[2][__][1]]
                            new_body[2][__] = ' '
                            new_body = clean_list(new_body)
                            return convert_to_nested_tuple(new_body)
                    for __ in range(len(new_body[2])):
                        if new_body[2][__][0] == 'var':
                            if new_body[2][__ + 1][0] == 'var':
                                return new_body[2][__][1] + new_body[2][__ + 1][1]
                            return new_body[2][__][1]
            else:
                if new_body[2][0] == 'lambda':
                    return convert_to_nested_tuple(new_body)
                #print("Not Nested")
                const = False
                for __ in range(len(new_body)):
                    if new_body[__][0] == 'const':
                        const = True
                if not const:
                    #print("No Constant")
                    if new_body[2][0] == 'var':
                        return new_body[2][1]
                else:
                    #print("Const Found")
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


def convert_to_nested_list(data):
    if isinstance(data, tuple):
        return [convert_to_nested_list(item) for item in data]
    elif isinstance(data, list):
        return [convert_to_nested_list(item) for item in data]
    else:
        return data


def clean_list(nested_list):
    if isinstance(nested_list, list):
        return [clean_list(item) for item in nested_list if item != " "]
    else:
        return nested_list


def convert_to_nested_tuple(data):
    if isinstance(data, list):
        return tuple(convert_to_nested_tuple(item) for item in data)
    elif isinstance(data, tuple):
        return tuple(convert_to_nested_tuple(item) for item in data)
    else:
        return data
