class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    return len(self.stack)==0 


  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    if not self.isEmpty():
      self.stack.pop(-1)


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    self.stack.append(operations)


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    operators=['+','-','*','/']
    count,digitcount=0
    for character in expression:
      if character in operators:
        count+=1
      elif character.isdigit():
        digitcount+=1
      else:
        return False
    if count<digitcount:
      return True

  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    str=list(self.expression)
    n=len(str)
    sta=[]
    for i in range(n):
      if str[i].isdigit():
        sta.append(int(str[i]))
      elif str[i]=='+':
        a=sta.pop()
        b=sta.pop()
        sta.append(int(a)+int(b))
      elif str[i]=='-':
        a=sta.pop()
        b=sta.pop()
        sta.append(int(a)-int(b))
      elif str[i]=='*':
        a=sta.pop()
        b=sta.pop()
        sta.append(int(a)*int(b))
      elif str[i]=='/':
        a=sta.pop()
        b=sta.pop()
        sta.append(int(a)/int(b))
     return sta.pop()

# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
