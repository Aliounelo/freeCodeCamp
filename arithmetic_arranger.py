def arithmetic_arranger(problems,answer = False):

  #-- Different arrays for our datas
  operand_1 = []
  operand_2 = [] 
  operator = []
  
  #-- Check if the number of problem is inferior to 5
  if len(problems) > 5 : 
    return "Error: Too many problems."

  #-- Split the problem and put each part into an array
  for operation in problems : 
    part = operation.split()
    operator.append(part[1])
    operand_1.append(part[0])
    operand_2.append(part[2])
    
  #-- Check if the operators are different of '*' and '/'
  if "*" in operator or "/" in operator: 
    return "Error: Operator must be '+' or '-'."

  #-- Check if the operands are digits
  for i in range(len(operator)):
    if not (operand_1[i].isdigit() and operand_2[i].isdigit()) :
      return "Error: Numbers must only contain digits."
      
  #-- Number of digits limitation (max 4)
  for i in range(len(operator)) :
    if len(operand_1[i]) > 4 or len(operand_2[i]) > 4 :
      return "Error: Numbers cannot be more than four digits."


  row_1 = []
  row_2 = []
  row_3 = []
  row_4 = []

  
        
    #return arranged_problems