def arithmetic_arranger(problems,answer=False):

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

  #-- Problems displaying format , each line will be in an array 
  row_1 = []
  row_2 = []
  row_3 = []
  row_4 = []

  for i in range(len(operand_1)) :
    if len(operand_1[i]) > len(operand_2[i]) :
      row_1.append(" "*2 + operand_1[i])
    else : 
      row_1.append(" "*((len(operand_2[i]) - len(operand_1[i]))+2) + operand_1[i])

      
  for i in range(len(operand_2)) :
    if len(operand_2[i]) > len(operand_1[i]) :
      row_2.append(operator[i] + " " + operand_2[i])
    else : 
      row_2.append(operator[i] + " "*((len(operand_1[i])-len(operand_2[i]))+1) + operand_2[i])

  for i in range(len(operand_1)): 
    row_3.append("-"*(max(len(operand_1[i]),len(operand_2[i])+1))    

  if answer : 
    for i in range(len(operand_1)) :
      if operator[i] == '+' :
        result = str(int(operand_1) + int(operand_2))
      else : 
        result = str(int(operand_1) - int(operand_2))

      
    #return arranged_problems