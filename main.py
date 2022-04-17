def arithmetic_arranger(equations, calculate=False):
    space = " "
    dash = "-"
    if len(equations) > 5:
        return "Error: Too many problems."

    line_one = ""
    line_two = ""
    line_three = ""
    line_four = ""


    for number in range(len(equations)):
        items = equations[number].split(" ")
        if items[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        try:
            first_num = int(items[0])
            second_num = int(items[2])

            if len(items[0]) > 4 or len(items[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                length = max(len(items[0]), len(items[2])) + 2
                line_one += space * (length - len(items[0]))
                line_one += items[0] + space

                line_two += items[1]
                line_two += space * (length - len(items[2]) - 1)
                line_two += items[2] + space

                line_three += dash * length
                line_three += space

                if items[1] == "+":
                    result = first_num + second_num
                elif items[1] == "-":
                    result = first_num - second_num
                
                line_four += space * (length - len(str(result)))
                line_four += str(result)
                line_four += space
        except:
            return "Error: Numbers must only contain digits"
    
    print(line_one + "\n" + line_two + "\n" + line_three)
    if(calculate):
        print(line_four)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)