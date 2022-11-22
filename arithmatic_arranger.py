def arithmetic_arranger(exp_lst):
    for exp in exp_lst:
        exp = exp.split()
        if len(exp) != 3:
            return "Error: Too many or too few arguments."
        if exp[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not exp[0].isdigit() or not exp[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(exp[0]) > 4 or len(exp[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if len(exp_lst) > 5:
            return "Error: Too many problems."
        if not exp[0].isdigit() or not exp[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(exp[0]) > 4 or len(exp[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if exp[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if exp[1] == '+':
            result = int(exp[0]) + int(exp[2])
            print(' ' * (len(exp[2]) - 1),exp[0])
            print(exp[1], exp[2])
            print('-' * (max(len(exp[0]), len(exp[2])) + 2))
            print(result)
            print('-' * (max(len(exp[0]), len(exp[2])) + 2))
            print("\n")
       

        elif exp[1] == '-':

            result = int(exp[0]) - int(exp[2])
            print(' ' * (len(exp[2]) - 1),exp[0])
            print(exp[1], exp[2])
            print('-' * (max(len(exp[0]), len(exp[2])) + 2))
            print(result)
            print('-' * (max(len(exp[0]), len(exp[2])) + 2))
            print("\n")
         

if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
    