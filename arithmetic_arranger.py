def make_err(message):
    return 'Error: ' + message

def check_problem(problem):
    operand1, operator, operand2 = problem.split()
    is_operator_correct = operator == '+' or operator == '-'
    are_operands_numbers = operand1.isdigit() and operand2.isdigit()
    are_operands_correct_length = len(operand1) <= 4 and len(operand2) <= 4

    if(not is_operator_correct):
        return [False, make_err("Operator must be '+' or '-'.")]
    elif (not are_operands_numbers):
        return [False, make_err('Numbers must only contain digits.')]
    elif (not are_operands_correct_length):
        return [False, make_err('Numbers cannot be more than four digits.')]
    else:
        return [True, '']

def get_answer(num1, operator, num2):
    if (operator == '-'):
        return num1 - num2
    else:
        return num1 + num2

def arithmetic_arranger(problems, add_sum=False):
    split_problems = []
    lines = ['', '', '', '']

    if len(problems) > 5:
        return make_err('Too many problems.')
    for problem in problems:
        is_problem_correct, err_message = check_problem(problem)
        if (not is_problem_correct):
            return err_message
        
        operand1, operator, operand2 = problem.split()
        split_problems.append((int(operand1), operator, int(operand2)))
    
    for (num1, operator, num2)  in split_problems:
        problem_width = len(str(max(num1, num2))) + 2

        lines[0] += '{0}    '.format(str(num1).rjust(problem_width))
        lines[1] += '{0} {1}    '.format(operator, str(num2).rjust(problem_width - 2))
        lines[2] += '{0}    '.format('-' * problem_width)
        lines[3] +='{0}    '.format(str(get_answer(num1, operator, num2)).rjust(problem_width))

    if (not add_sum):
        lines.pop()
    return '\n'.join([line.rstrip() for line in lines])


print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
