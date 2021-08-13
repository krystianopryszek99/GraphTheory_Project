# Graph Theory Project
# Krystian Opryszek - G00366895

import argparse, textwrap

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

# Thompson's construction

class State:
    """ A state and it's arrows in Thompson's construction. """
    def __init__(self, label, arrows, accept):
        """ Label is the arrow  labels, arrows is a list of states to point to, accept is a boolean as to whether this is an accept state """
        self.label = label
        self.arrows = arrows
        self.accept = accept

    # Method that returns a set of states that are from the following this states and all its e arrows
    def followes(self):
        """ Returns sets of states that are from the following thus state and all its e arrows """
        # Include this state in the returned set
        states = {self}
        # if this state has e arrows
        if self.label is None: 
            # loop through this state's arrows
            for state in self.arrows:
                states = (states | state.followes())
        # returns the set of states
        return states

class NFA:
    """ A non-deterministic finite automaton """
    def __init__(self, start, end):
      # has a start and end state
      self.start = start
      self.end = end

    # method taking a self as first argument
    # method for matching 
    def match(self, s):
        """" Return True if the NFA mathces the string s """
        # list of previous states
        previous = self.start.followes()
        # loop through the string 
        for c in s:
            # start with an empty set 
            current = set()
            # loop through the previous states
            for state in previous:
                # check if there is a c arrow from state
                if state.label == c:
                    # add followes for next state
                    current = (current | state.arrows[0].followes())
            # replace previous with current
            previous = current
        # if the final state is in previous, return true
        return (self.end in previous)

def re_to_nfa(postfix):
    # A stack for NFA's
    stack = []
    # Loop through the postfix r.e left to right.
    for c in postfix:
        # Concatenation
        if c == '.':
            # Pop top NFA off stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Make accept state of NFA1 non-accept
            nfa1.end.accept = False
            # Make it point at start state of nfa2
            nfa1.end.arrows.append(nfa2.start)
            # Make a new NFA with nfa1's start state and nfa2's end state
            nfa = NFA(nfa1.start, nfa2.end)
            # Push to the stack
            stack.append(nfa)
        elif c == '|':
            # Pop top NFA off stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non-accept
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Make a new NFA 
            nfa = NFA(start, end)
            # Push to the stack
            stack.append(nfa)
        elif c =='*':
              # Pop one NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states
            start.arrows.append(nfa1.start)
            # And at the new end state
            start.arrows.append(end)
            # Make old accept state non-accept
            nfa1.end.accept = False
            # Make old end state point to new end state
            nfa1.end.arrows.append(end)
            # Make old accept state point to old start state
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA 
            nfa = NFA(start, end)
            # Push to the stack
            stack.append(nfa)
        else:
            # Create an NFA for the non-special character c
            # Create the end state
            end = State(None, [], True)
            # Create the start state
            start = State(c, [], False)
            # Point new start state at new end state
            start.arrows.append(end)
            # Create the NFA with the start and end state
            nfa = NFA(start, end)
            # Append the NFA to the NFA stack
            stack.append(nfa)
    
    # There should only be one NFA on the stack
    if len(stack) != 1:
        return None
    else:
        return stack[0] 

# User Input - takes in regular expression and file name 
# Allows only single regular expression and single file name 
# arg parser for --help and -h flags

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        _______________________________________
                How to run this program
        _______________________________________

        Program that takes a regular expression 
        and a file as command line arguments, 
        and outputs the number of matches for 
        the regular expression within the file

        Before you run the program, ensure you
        have "input.txt" in the same folder as 
        the script "rescript.py". 

        Run the program as follows:

        eg. python3 rescript.py a.b input.txt

        Program only accepts single file input 
        _______________________________________
        '''))

# takes regular expression
parser.add_argument('regexp', metavar='expression', type=str,
                    help='string for the search')

# takes file name
parser.add_argument('file', metavar='path', type=str,
                    help='name of the file')
args = parser.parse_args()

# Takes the file path and searches for the matches and returns the number of matches within that file 
with open(args.file, 'r') as fileSearcher:
    counter =0
    for line in fileSearcher:
        for word in line.split():
            infix = args.regexp
            postfix = shunt(infix)
            nfa = re_to_nfa(postfix)
            match = nfa.match(word)
            if match == True:
                #matches
                counter +=1

    # prints out the number of matches
    print(counter)