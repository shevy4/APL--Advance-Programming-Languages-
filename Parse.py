def parse_result(parsed_result):
    try:
        '''
        if evaluate_inputoutput(parsed_result[1], parsed_result[2][1][1]):
            result = parsed_result[2][2]
        else:
            result = parsed_result[2][1]
            
            '''
        result = parsed_result
        print("~~~~~~~")

        if len(result[2]) > 2:

            while isinstance(result, tuple):
                print(result[1], " + ", result[2][1][1])
                if evaluate_inputoutput(result[1], result[2][1][1]):
                    print(result)
                    result = result[2][2]
                else:
                    result = result[2][1][1]
                    break

    except IndexError:
        print("PING")
        if evaluate_inputoutput(result[1], result[2][1]):
            print(result[2][1])
        else:
           print(result[2][1])

    #print(result)


def evaluate_inputoutput(input, output):
    if input == output:
        return 1
    else:
        return 0
