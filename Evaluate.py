def parse_result(parsed_result):
    def beta_reduce(expr):

        if isinstance(expr, tuple):

            if expr[0] == 'lambda':
                print("input was = ", expr)
                input, body = expr[1], expr[2]

                #print("input =\n", input, "\nbody -\n", body[1])
                if input == body[1]:
                    return body
                else:
                    if len(body) == 2:
                        return body
                    else:
                        if expr[2][2][0] == 'lambda':
                            body = expr[2][2]
                            if input == expr[2][1][1]:
                                return body
                            else:
                                body = expr[2]
                                return body
                        else:
                            return expr[2]

            if expr[0] == 'var':
                print(expr)
                return expr

            if expr[0] == 'apply':
                func, arg = expr[1], expr[2]
                print("func = ", func, "arg = ", arg)
                if func[0] == 'lambda':
                    var, body = arg[1], func[2]
                    reduced_expr = substitute(body, var, arg)
                    print('reduced - \n', reduced_expr)
                    print(f"Reducing: ({func}) ({arg}) -> {reduced_expr}")
                    return reduced_expr
                else:
                    if func[0] == 'var':
                        arg, func = beta_reduce(expr[2]), expr[1]
                        print("func = ", func, "arg = ", arg)
                        if arg[0] == 'var':
                            if func[0] == 'var':
                                return arg
                            return func
                        else:
                            print("returning arg")
                            print(arg)
                            return arg

                    else:
                        return ('apply', beta_reduce(func), beta_reduce(arg))



            elif expr[0] == 'operator':
                return expr

    def substitute(body, var, value):
        print("Sub")
        if isinstance(body, tuple):
            if body[0] == 'var' and body[1] == var:
                return value
            elif body[0] == 'lambda':
                if body[1] == var:
                    return body
                else:
                    return ('lambda', body[1], substitute(body[2], var, value))
            else:
                return tuple(substitute(sub_expr, var, value) for sub_expr in body)
        else:
            return body

    current_expr = parsed_result
    count = 0
    while True:
        reduced_expr = beta_reduce(current_expr)
        if reduced_expr == current_expr:
            break
        print(f"Reduction step {count}: {current_expr} -> {reduced_expr}")
        current_expr = reduced_expr
        count += 1

    print("Final result:", current_expr)
