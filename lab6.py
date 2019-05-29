#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list


class Stack:
	#Create a New Empty Stack
	def __init__(self):
		self.__S = []
	#Display the Stack

	def __str__(self):
		return str(self.__S)
	#Add a new element to top of stack

	def push(self, x):
		self.__S.append(x)
	#Remove the top element from stack

	def pop(self):
		return self.__S.pop()
	#See what element is on top of stack
	#Leaves stack unchanged

	def top(self):
		return self.__S[-1]
#postfix
def postfix(exp):
    stack = Stack()
    operators = ['+', '-', '*', '/']
    
    for c in exp.split(' '):
        try:
            stack.push(float(c))    
        except:
            pass
        if c in operators:
            input1 = float(stack.pop())
            input2 = float(stack.pop())
            if c == '+':
                output = float(input1 + input2)
            elif c == '-':
                output = float(input1 - input2)
            elif c == '*':
                output = float(input1 * input2)
            elif c == '/':
                output = float(input2 / input1)
            stack.push(output)   
    return output


#Main program
if __name__ == "__main__":
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit.")
    userInput = input("Enter expression:\n")

    while(userInput.lower() != 'exit'):
        print(postfix(userInput))
        userInput = input("Enter expression:\n")


