# Graph Theory Project
# Krystian Opryszek - G00366895

# Shunting yard

def shunt(infix):
    """Convert infix expressions to postfix."""
    # The eventual output
    postfix = ""
    # The shunting yard operator stack
    stack = ""
    # Operator precedence
    prec = {'*': 100, '.': 90, '|': 80}
    # loop through the input a character at a time
    for c in infix:
        # c is an operator.
        if c in {'*', '.', '|'}:
            # check what is on the stack
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append operator at top of stack to output
                postfix = postfix + stack[-1]
                # Remove operator from stack - it's like pop
                stack = stack[:-1]
        # Push c to stack
            stack = stack + c
            # if '(' push to operator stack
        elif c == '(':
            # Push c to stack
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Append operator at top of stack to output
                postfix = postfix + stack[-1]
                # Remove operator from stack - it's like pop
                stack = stack[:-1]
            # Remove open bracket from stack
            stack = stack[:-1]
            # c is an non special
        else:
            # Push it to the output
            postfix = postfix + c

    # Empty the operator stack.
    while len(stack) != 0:
        # Append operator at top of stack to output
        postfix = postfix + stack[-1]
        # Remove operator from stack - it's like pop
        stack = stack[:-1]
    # Return the postfix version of infix
    return postfix

infix = "3+4*(2-1)"
postfix = "3421-*+"

print(f"infix:  {infix}")
print(f"shunt:  {shunt(infix)}")
print(f"postfix:    {postfix}")