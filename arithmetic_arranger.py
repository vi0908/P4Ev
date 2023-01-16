def arithmetic_arranger(lista):
    for operaciones in lista:
        elements = operaciones.split()
        operand_1 = elements[0]
        operator = elements[1]
        operand_2 = elements[2]
        operations_vertical_format = list()

        if len(operand_1) >= len(operand_2) and len(operand_1) <= 4 :
            operand_1 = operand_1.rjust(1,' ')
            line = '-'* (len(operand_1)+4)
            operand_2 = operand_2.rjust(len(operand_1),' ')

            if operator == '+':
               operation = str(int(operand_1) + int(operand_2))
               result = operation.rjust(len(operand_1), ' ')
               expresison_sum = '\n   ' + operand_1 + '\n + ' + operand_2 + '\n' + line + '\n   ' + result + '\n'
               vertical_format = expresison_sum

            elif operator == '-':
               operation = str(int(operand_1) - int(operand_2))
               result = operation.rjust(len(operand_1), ' ')
               v = '\n   ' + operand_1 + '\n - ' + operand_2 + '\n' + line + '\n   ' + result + '\n'


            else:
                print('\nError: Operator must be (+) or (-) .\n')

        else:
            print('\nError: Numbers cannot be more than four digits.\n')

        operations_vertical_format = operations_vertical_format.append(vertical_format)
    print(operations_vertical_format)


arithmetic_arranger(['623 + 67'])
    
