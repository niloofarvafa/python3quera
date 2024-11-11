import re


def check(inp, number):
    inp = inp.split("#")
    start = inp[0]
    end = inp[1]
    pattern = ""
    if len(start) != 0:
        pattern = pattern + "^" + start
    pattern = pattern + ".*"
    if len(end) != 0:
        pattern = pattern + end + "$"
    find = re.search(pattern, number)
    if find is not None:
        return True
    return False


def solve(problem):
    answer = ''
    problem = problem.split(" + ")
    num1 = problem[0]
    problem = problem[1].split(" = ")
    num2 = problem[0]
    res = problem[1]

    if '#' in num1:
        if check(num1, str(int(res) - int(num2))):
            answer = f'{(int(res) - int(num2))} + {num2} = {res}'
        else:
            answer = "-1"
    elif '#' in num2:
        if check(num2, str(int(res) - int(num1))):
            answer = f'{num1} + {int(res) - int(num1)} = {res}'
        else:
            answer = "-1"
    else:
        if check(res, str(int(num1) + int(num2))):
            answer = f'{num1} + {num2} = {int(num1) + int(num2)}'
        else:
            answer = "-1"
    return answer