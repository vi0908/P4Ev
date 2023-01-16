def arithmetic_arranger(lista, second_argument = None):

    if len(lista) <= 5:
        
        operands_1 = ''
        operands_2 = ''
        lines = ''
        results = ''

        for operaciones in lista:
            elements = operaciones.split()
            operand_1 = elements[0]
            operator = elements[1]
            operand_2 = elements[2]

            if int(operand_1) >= int(operand_2) and len(operand_1) <= 4 :
    
                if operator == '+':
                    operation = str(int(operand_1) + int(operand_2))
                    operand_1 = operand_1.rjust(1,' ')
                    sign = '+ '
                    operand_2 = operand_2.rjust(len(operand_1),' ')
                    result = operation.rjust(len(operand_1)+2,' ')
                    line = '-'* (len(operand_1)+2)
                    expression_sum = str('   ' + operand_1 + '\n + ' + operand_2 + '\n ' + line + '\n ' + result  + '')

               
        
                elif operator == '-':
                    operation = str(int(operand_1) - int(operand_2))
                    operand_1 = operand_1.rjust(1,' ')
                    sign = '- '
                    operand_2 = operand_2.rjust(len(operand_1),' ')
                    result = operation.rjust(len(operand_1)+2, ' ')
                    line = '-'* (len(operand_1)+2)
                    expression_sub = '\n   ' + operand_1 + '\n - ' + operand_2 + '\n' + line + '\n ' + result + '\n'
               

                else:
                    operands_1 = ''
                    break


            elif int(operand_1) < int(operand_2) and len(operand_2) <=4 : 
    
                if operator == '+':
                    operation = str(int(operand_1) + int(operand_2))
                    operand_2 = operand_2.rjust(1,' ')
                    sign = '+ '
                    operand_1 = operand_1.rjust(len(operand_2),' ')
                    result = operation.rjust(len(operand_2)+2, ' ')
                    line = '-'* (len(operand_2)+2)
                    expression_sum = '\n   ' + operand_1 + '\n + ' + operand_2 + '\n' + line + '\n ' + result + '\n'
               
        
                elif operator == '-':
                    operation = str(int(operand_1) - int(operand_2))
                    operand_2 = operand_2.rjust(1,' ')
                    sign = '- '
                    operand_1 = operand_1.rjust(len(operand_2),' ')
                    result = operation.rjust(len(operand_2)+2, ' ')
                    line = '-'* (len(operand_2)+2)
                    expression_sub = '\n   ' + operand_1 + '\n - ' + operand_2 + '\n' + line + '\n ' + result + '\n'
               
        
                else:
                    operands_1 = ''
                    break
                

            else:  
                operands_2 = ''
                break

            operands_1 = operands_1 + operand_1 +  '        '
            operands_2 = operands_2 + sign +  operand_2 + '      '
            lines = lines + line + '      '
            results = results + result + '      '  



        if second_argument == None:
            print('\n    ' + operands_1 + '\n  ' + operands_2 + '\n  ' + lines + '\n  ')

        elif operands_1 == '':
            print("\nError: Operator must be '+' or '-'. \n")
        
        elif operands_2 == '':
            print('\nError: Numbers cannot be more than four digits.\n')
    
        else:
            print('\n    ' + operands_1 + '\n  ' + operands_2 + '\n  ' + lines + '\n  ' + results + '\n')

    else:
       print('\nError: Too many problems.\n')
    


arithmetic_arranger(['999 + 0', '999 - 1000','99999 + 9999', '4566 - 5', '8 + 9'], True)