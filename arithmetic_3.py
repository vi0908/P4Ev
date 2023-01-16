def arithmetic_arranger(problems, second_argument = None):
  operands_1 = ''
  operands_2 = ''
  results = ''
  lines = ''

  if len(problems) > 5:
    return "Error: Too many problems."
    
  for problem in problems:
    operaciones = problem.split()
    operand_1 = operaciones[0]
    operator = operaciones [1]
    operand_2 = operaciones[2]

    try:
      operand_1 = str(int(operand_1))
      operand_2 = str(int(operand_2))
                    
    except:
      return "Error: Numbers must only contain digits."
      
    if len(operand_1) > 4 or len(operand_2) > 4:
      return "Error: Numbers cannot be more than four digits."
      
    if operator == '+' or operator == '-':
      
      if operator == '+':
        result = str(int(operand_1) + int(operand_2))
      else:
        result = str(int(operand_1) - int(operand_2))
        
      largo = max(len(operand_1), len(operand_2)) + 2
      up = operand_1.rjust(largo,' ')
      down = operator + operand_2.rjust(largo - 1, ' ')
      line = '-' * largo
      res = str(result).rjust(largo)
      
      if problem != problems[-1]:
        operands_1 = operands_1 + up + '    '
        operands_2 = operands_2 + down + '    '
        lines = lines + line + '    '
        results = results + res + '    '
              
      else:
        operands_1 = operands_1 + up 
        operands_2 = operands_2 + down 
        lines = lines + line 
        results = results + res 

    else:
      return "Error: Operator must be '+' or '-'."
      
    #operands_1.rstrip()
    #operands_2.rstrip()
    #lines.rstrip()

  if second_argument == None:
    arranged_problems = operands_1 + '\n' + operands_2 + '\n' + lines
    return arranged_problems
    
    
  else:
    #results.rstrip()
    arranged_problems = operands_1 + '\n' + operands_2 + '\n' + lines + '\n' + results

    
    return arranged_problems  
        
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

#https://replit.com/@EyckVanJan/boilerplate-arithmetic-formatter-8?v=1

