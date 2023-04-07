def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Number of problems > 5"

    arranged_problems = ""
    top_row = ""
    bottom_row = ""
    line_row = ""
    answer_row = ""

    for problem in problems:
        
        components = problem.split()
        operand_one = components[0]
        operator = components[1]
        operand_two = components[2]

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are valid
        if not operand_one.isdigit and operand_two.isdigit:
            return "Error: Operand one is not a digit"
        if operand_two.isdigit and not operand_one.isdigit:
            return "Error: Operand two is not a digit"
        if not operand_one.isdigit() or not operand_two.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand_one) > 4 or len(operand_two) > 4:
            return "Error: Numbers cannot contain more than four digits."

        if operator == '+':
            answer = int(operand_one) + int(operand_two)
        elif operator == '-':
            answer = int(operand_one) - int(operand_two)
        else:
            return "Error: invalid operator type"

        width = max(len(operand_one), len(operand_two)) + 2
        top_row += operand_one.rjust(width) + "    "
        bottom_row += operator + " " + operand_two.rjust(width-2) + "    "
        line_row += "-" * width + "    "
        answer_row += str(answer).rjust(width) + "    " if show_answers else ""

    arranged_problems = top_row.rstrip() + "\n" + bottom_row.rstrip() + "\n" + line_row.rstrip()
    if show_answers:
        arranged_problems += "\n" + answer_row.rstrip()

    return arranged_problems
