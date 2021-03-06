# Graph Theory Project

**Name:** Krystian Opryszek

**Student ID:** G00366895

# Project Description
My Graph Theory project is about writing a program in Python 3 that takes a regular expression and a file as command line arguments, and outputs the number of matches for the regular expression within the file.

# User manual

Firstly clone this repository on your machine 

1. `git clone https://github.com/krystianopryszek99/GraphTheory_Project2021.git`
2. `cd GraphTheory_Project2021`
3. `python3 rescript.py -h`

Further instruction are given when running the code

Program accepts `--help` and `-h` flags which are specified as a command line arguments which explain how to use the program.

![image](https://user-images.githubusercontent.com/57759154/130155723-41a7ad52-a81a-472c-a831-f1ac463bb1f5.png)

# Explanation of the algorithm

The program is developed to take regular expression and file as a command line arguments and outputs the number of matches within that file. 

**Shunting-yard algorithm**

The shunting yard algorithm converts infix expression to postfix expression. The shunt function starts with an empty postfix and stack that is required in the shunting-yard. Inside of the main for loop there is another for loop that checks if it's a digit, if it is it will push it to the output. If you get an operator, it checks if the stack is empty. If there is nothing, it pushes the operator onto the stack and if there is something on the stack it empties the stack until it's false and push the operator to the stack.

**Thompson's construction**

The Thompson's construction creates the NFA from postfix. The Thompson's construction has two classes, one for State and NFA. The NFA has a start state and end state both pointing at the State. The function re_to_nfa that will run through the postfix notation and turn it into NFA. The State class, all of the arrows coming from the state have the same label. In the function re_to_nfa keeps a list of NFA, and checks if it's concatenation character, or character, star character and if it's not anyone of them it, it will presume it???s just a regular character not a operator.

**Match method**

The match method returns true only if the NFA instance matches the string, in this case it will only return true if it matches the string s. The list current lists the previous states which is equal to self.start whcih means it starts in the start state. The method followes that returns a set of states that are taken from the following state and all its e arrow. If the state has e arrows and label is None, it will loop through this state's arrows and returns the set of states.

**Command line arguments**

Argparse allows the program to accept command line arguments and allows the program to create help flags which are used to explain how the program works. The program accepts regular expression and single file. The help flags accepts both `-h` and `--help` commands. Args parser is an easy and sufficient way to write user-friendly command-line interfaces. 

# Research

**Argparse**

In week 4 I was introduced to argparse which deals with command line arguments in Python. Firstly I watched the video on [argsparser](https://web.microsoftstream.com/video/49044275-f5d9-442d-938f-c3005aa911f4?referrer=https://learnonline.gmit.ie/) which was available to us on moodle. After completing the lab, I wanted to find out more about argsparser so I did some research and found great examples on [docs.python](https://docs.python.org/3/library/argparse.html). 

**Shunting-yard algorithm**

I was Introduced to Shunting-yard algorithm in week 6 of the course. As this was new to me, firstly I watched the video on Shunting-yard algorithm [Shunting-yard algorithm](https://web.microsoftstream.com/video/3f9dd01a-6ac9-4d65-b9b9-d6ef1ece8be8) which was available on Moodle. After watching the video I had some understanding of Shunting-yard algorithm which is a method of parsing mathematical expressions specified in infix notation. Video on Implementing the [Shunting-yard algorithm in Python (Part 1)](https://web.microsoftstream.com/video/04fbd7f8-8880-426e-bfb5-2e5478db497e) was really helpful as I ended up coding it on my machine which was great exercise to start with. 

In week 7 I followed a video on Implementing the [Shunting-yard algorithm in Python (Part 2)](https://web.microsoftstream.com/video/85152016-d320-4bbe-bfff-48baebcd59a6) and ended up finishing the full code. I didn???t really understand the context of converting from infix to postfix notation, so I found helpful [website](https://pediaa.com/difference-between-prefix-and-postfix/#Infix) in which I found the definition of infix and postfix and some great examples.

**Thompson???s Construction and more of Shunting yard algorithm**

In week 8 we looked at regular expression operations, Thompson???s construction, and more of the Shunting yard algorithm. The regular expression operations were: or operation `???|???` , the concatenation  `???.???` operation, and the Kleene star `???*???`. Firstly I watched the first video which was on [or operation](https://web.microsoftstream.com/video/1f0c5fb1-1a29-43a7-a7f6-9dfb73a5e26d) which was very helpful, then I watched the video on [concatenation operation](https://web.microsoftstream.com/video/6ec2eba7-b0d9-4682-a680-02cad14ef913), and finally I watched the video on [Kleene star](https://web.microsoftstream.com/video/d8971793-ac18-4245-9a0f-f90b0721aeff) which I found much more difficult to understand. 
Then I started looking at the Thompson???s construction, which I found very interesting in the way it turns postfix into non-deterministic finite automata which recognizes patterns of text. From the previous week, we continued from where we left on the shunting yard algorithm and made a few small changes.

**Thompson???s construction in code**

In week 9 we started to look more into developing a python script for Thompson???s construction. Firstly, I watched the video on [Thompson???s construction by hand](https://web.microsoftstream.com/video/634e1883-ad11-447f-971a-cb7965355c13) as I had difficulty understanding how it works. After re-watching the video a couple of times, I finally had a better understanding on Thompson???s construction and was ready to start coding it, with the help of the video on [Thompson???s construction in code](https://web.microsoftstream.com/video/4012d43a-bb46-4ceb-8aa9-2ae598539a32). Then I tried to complete the code myself, but I found it very difficult, so I followed the video along and was capable of complete the code.

**Match function** 

In week 12  we looked at the match and followes function that is the final chapter of Thompson???s construction. Firstly I watched the lecture on [Reviewing NFA matching by hand](https://web.microsoftstream.com/video/0f3d8f6f-68c9-42d0-9449-b7f868888efe) and [Sketching out the match function](https://web.microsoftstream.com/video/8fe195b7-f7c3-4265-86bc-7ff2c367eee9) in which we created tests to help us grasp on how the NFA matching function works. 
Then I followed the video on [NFAs: Code to follow the e arrows](https://web.microsoftstream.com/video/59770e5a-2fed-4575-a4eb-0fd691b77d54) in which we develop code to match strings on the NFA. At the start I didn???t really understand how the match function works so I re-watched the video [NFAs: Code to follow the e arrows](https://web.microsoftstream.com/video/59770e5a-2fed-4575-a4eb-0fd691b77d54) to get a better understanding. 

# Questions

- **Explain the difference between regular expressions in infix notation and those in postfix notation**

  [Infix notation](https://en.wikipedia.org/wiki/Infix_notation) is a popular notation for logical formulas and assertions. . Infix notation is distinct from function notation, in which a function's name denotes a certain action and it???s arguments are the operands.
  
  [Postfix notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation), often known as Reverse Polish notation or Polish postfix notation was invented to reduce computer memory access and make the use of the stack to evaluate expressions.

  The main difference between infix and postfix notation is that the infix notation places the operators between the operands <operand> <operator> <operand>, whereas the postfix notation places the operator after the operands <operand> <operand> <operator>. 

  Humans can read and grasp infix notation more easily, but postfix notation is much more difficult to understand. Postfix does not require brackets to indicate the order of evaluation, making them easier for machines to evaluate.

  Parentheses around groups of operands and operators are required in infix notation, unlike in postfix notation, to indicate the intended order in which operations are to be executed. As long as each operator has a fixed number of operands, no parentheses are required in postfix notation. An operator with a higher precedence level accepts its operands before an operator with a lower precedence level in infix notation. 

  In postfix notation when there are several operations, operators are assigned immediately following their second operands. Postfix notation has been shown to result in quicker calculations since it does not need parenthesizing expressions, requiring less operations to be performed to complete ordinary calculations.
  
  Examples of converting an Infix to postfix: 
  
  ![image](https://user-images.githubusercontent.com/57759154/125867388-80dc5a76-2d91-4a57-9ec3-e22ddef1ab39.png)


- **Explain how Thompson's construction for regular expressions works**

  [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction), commonly known as the McNaughton???Yamada???Thompson algorithm, turns postfix regular expressions into nondeterministic finite automaton (NFA) which is going to recognize patterns of text. Thompson's construction is an algorithm to construct an NFA from regular expression. NFA recognizes the same language as the regular expression.

  Thompson's construction may be thought of in terms of NFA???s fragments.
You presume that the regular expression is in postfix, the stack of fragments of the overall nondeterministic finite automaton (NFA) is created and the normal characters such as `???.??? , ???*???, and ???|???` are pushed onto the stack. Special characters will be considered like operators, having the ability to pop of the stack and perform something with what???s pop from the stack.

  The one or two nondeterministic finite automaton (NFA) fragments on the stack are joined together to form a new start state, which is then joined with e arrows, and then from one or two NFA???s fragment get new NFA fragment and push that onto the stack.
  
  The algorithm works in a predefined sequence, breaking down an expression into its component subexpressions, from which the NFA is built using a set of rules. Thompson's construction algorithm is one of several for constructing NFAs from regular expressions.  Kleene's approach, in contrast to Thompson's, converts a finite automaton into a regular expression.
  
  **Rules**
  
  The following images are from [Visualizing Thompson???s Construction Algorithm for NFAs, step-by-step](https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b)
  
  **#1.** Empty regular expression, single NFA fragment
  ![image](https://user-images.githubusercontent.com/57759154/125359462-33c85800-e362-11eb-91cb-79f5417ff2a3.png)
  
  **#2.** Symbol regular expression, nfa to recognize a character e.g A or B 
  ![image](https://user-images.githubusercontent.com/57759154/125359496-42af0a80-e362-11eb-86ad-ef39ef0d0b22.png)
  
  **#3.** Union expression, pop two fragments from the stack
  ![image](https://user-images.githubusercontent.com/57759154/125359522-493d8200-e362-11eb-87ad-581442cbd3c2.png)
  
  **#4.** A concatenation expression, joining one nfa to another nfa.
  
  ![image](https://user-images.githubusercontent.com/57759154/125359537-50649000-e362-11eb-852f-6259b3f4171b.png)
  
  **#5.** A closure/Kleene star expression, pop a fragment from the stack and push the following:
  
  ![image](https://user-images.githubusercontent.com/57759154/125359560-5a868e80-e362-11eb-9ffb-5ea84032da95.png)

- **Explain what is meant by the term irregular language in the context of regular expressions**

  A non-regular language, often known as an irregular language, is one that cannot be defined by a regular expression. Non-regular languages outnumber regular languages by a significant amount. According to Kleene's theorem, no Finite Automaton (FA) or Transition Graph (TG) may accept a non-regular language. 
  
  The Finite State Machine (FSM) is a Finite Automaton (FA) that chooses whether to accept or reject a string. There are two types of FA's, Non-deterministic (NFA) and Deterministic (DFA). A Transition Graph is made up of three components: a finite number of states, an alphabet of potential inputs, and a finite number of transitions that demonstrate how to go from one state to another.
  
  The existence of non-regular languages is ensured by the fact that regular languages of any alphabet are countable, and we know that the set of all subsets of strings is not countable. Nonetheless, the goal of creating non-regular languages is to show that certain languages that are "computable" in some way are not regular.
  
  Pumping Lemma is a well-known theorem that uses the Pigeon Hole Principle to determine if a language is regular or not, but it cannot be used to prove that a language is regular. The pumping lemma is used to prove the non-regularity of a language via contradiction. However, the Pumping Lemma is a negative test, if a language does not meet it, we can be certain that it is not regular, if it does, the language may or may not be regular.
  
  The languages Palindrome is a examples of nonregular languages. A palindrome is a word, number, phrase, or other character sequence that reads the same backward as it does forward.


# Resources
https://en.wikipedia.org/wiki/Thompson%27s_construction

https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b

https://web.microsoftstream.com/video/d6d9a2d8-b23e-4abf-b1b7-af3a2d44b82f?referrer=https:%2F%2Flearnonline.gmit.ie%2F

https://en.wikipedia.org/wiki/Infix_notation
  
https://pediaa.com/difference-between-prefix-and-postfix/#Infix

https://en.wikipedia.org/wiki/Reverse_Polish_notation
  
https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b

https://slideplayer.com/slide/12946344/
  
https://www.cs.wcupa.edu/rkline/fcs/re-pump.html

https://www.geeksforgeeks.org/how-to-identify-if-a-language-is-regular-or-not/
  
https://slidetodoc.com/4-b-lexical-analysis-finite-automata-finite-automata/
  
https://slideplayer.com/slide/9604318/
