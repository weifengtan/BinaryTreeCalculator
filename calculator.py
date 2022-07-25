#
# DO NOT FORGET TO ADD COMMENTS!!!
#
from stack import Stack
from tree import BinaryTree, ExpTree

def infix_to_postfix(infix):
    stack = Stack()
    postfix = ''
    useless = ''

    # To set the order of the precedence 
    order = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

    for count, i in enumerate(infix):
        if i == '(' :
            stack.push(i)
        elif i in '^*/+-^' :
            if stack.peek() == '(' :    # if the top of the stack is ( then i just add it into stack 
                stack.push(i)
            else:               # if not then I go through the conditions where if precedence is higher or lower
                if stack.isEmpty() :
                    stack.push(i)
                elif (not stack.isEmpty() and order[i] > order[stack.peek()]):
                    stack.push(i)
                elif (not stack.isEmpty() and order[i] == order[stack.peek()]):
                    out = stack.pop()
                    if out in ('*/+-^'):
                        postfix += ' ' + out
                    else :
                        postfix += out
                    stack.push(i)
                # This test for if the order is smaller and pos out the operator and pushes new one in
                elif (not stack.isEmpty() and order[i] < order[stack.peek()]):
                    while (not stack.isEmpty()) :
                        if stack.peek() == '(' :
                            stack.push(i)
                        else:
                            if (order[i] < order[stack.peek()] ):
                                out = stack.pop()
                                if out in ('*/+-^'):
                                    postfix += ' ' + out
                                    stack.push(i)
                                else :
                                    postfix += out
                            else :
                                stack.push(i)
                                break
                        break
            
        elif i == ')' :         # if i is ) I push everything out until ( and then I stop and pop out (
            while (stack.peek() != '(' and not stack.isEmpty()) :
                out = stack.pop()
                if out in ('*/+-^'):
                    postfix += ' ' + out
                else :
                    postfix += out
            stack.pop()
        elif i == '.' :
            postfix += i
                
        else:                   # if it is just a number then I add it into the string.
                                # I had help from Michaels Pseudo Code when doing double digits
            if i.isnumeric():
                if infix[count-1].isnumeric():
                    postfix += i
                elif infix[count-1] == '.' :
                    postfix += i
                else :
                    postfix += ' ' + i
            
            
    while (not stack.isEmpty() and stack.peek() != '(' ) :  # This pushes everything out of the stack and into string. 
        out = stack.pop()
        if out in ('*/+-^'):
            postfix += ' ' + out
        else :
            postfix += out
    # made another one where it goes through the whole stack to double check for any missing operators. 
    while (not stack.isEmpty()) :  # This pushes everything out of the stack and into string. 
        out = stack.pop()
        if out == '(' :
            useless += out
        else:
            if out in ('*/+-^'):
                postfix += ' ' + out
            else :
                postfix += out

    
    return (postfix)        # return statement 
                    
def calculate(infix):
    # This function was pretty straight forward, convert it to postfix then split it which deletes the spaces
    # then make a tree out of the postfix, then evaluate the number and return. 
    postfix = infix_to_postfix(infix)
    postfix = postfix.split()
    num = ExpTree.make_tree(postfix)
    answer = num.evaluate(num)
    
    
    return answer

# a driver to test calculate module
if __name__ == '__main__':

    #infix_to_postfix('5+2*3')
    # test infix_to_postfix function
    #assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    #assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    #assert calculate('(5+2)*3') == 21.0
    #assert calculate('5+2*3') == 11.0
    print ("Welcome to Calculator Program!")
    
    leave = 0
    
    while leave != 1:
        user = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
        if user == 'q' or user == 'quit' :
            print ('Goodbye!')
            leave = 1 
        else:
            answer = float(calculate(user))
            print (answer)