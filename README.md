# Graph Theory Project

**Name:** Krystian Opryszek

**Student ID:** G00366895

# Project Description
My Graph Theory project is about writing a program in Python 3 that takes a regular expression and a file as command line arguments, and outputs the number of matches for the regular expression within the file.

# Research

**Shunting-yard algorithm**

I was Introduced to Shunting-yard algorithm in week 6 of the course. As this was new to me, firstly I watched the video on Shunting-yard algorithm [Shunting-yard algorithm](https://web.microsoftstream.com/video/3f9dd01a-6ac9-4d65-b9b9-d6ef1ece8be8) which was available on Moodle. After watching the video I had some understanding of Shunting-yard algorithm which is a method of parsing mathematical expressions specified in infix notation. Video on Implementing the [Shunting-yard algorithm in Python (Part 1)](https://web.microsoftstream.com/video/04fbd7f8-8880-426e-bfb5-2e5478db497e) was really helpful as I ended up coding it on my machine which was great exercise to start with. 

In week 7 I followed a video on Implementing the [Shunting-yard algorithm in Python (Part 2)](https://web.microsoftstream.com/video/85152016-d320-4bbe-bfff-48baebcd59a6) and ended up finishing the full code. I didn’t really understand the context of converting from infix to postfix notation, so I found helpful [website](https://pediaa.com/difference-between-prefix-and-postfix/#Infix) in which I found the definition of infix and postfix and some great examples.

# Questions

- **Explain the difference between regular expressions in infix notation and those in postfix notation**

  [Infix notation](https://en.wikipedia.org/wiki/Infix_notation) is a popular notation for logical formulas and assertions.
  
  [Postfix notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation), often known as Reverse Polish notation or Polish postfix notation.

  The main difference between infix and postfix notation is that the infix notation places the operators between the operands, whereas the postfix notation places the operator after the operands.

  Humans can read and grasp infix notation more easily, but postfix notation is much more difficult to understand.

  Parentheses around groups of operands and operators are required in infix notation, unlike in postfix notation, to indicate the intended order in which operations are to be executed. As long as each operator has a fixed number of operands, no parentheses are required in postfix notation.

  In postfix notation when there are several operations, operators are assigned immediately following their second operands. Postfix notation has been shown to result in quicker calculations since it does not need parenthesizing expressions, requiring less operations to be performed to complete ordinary calculations.
  
  Examples of converting an Infix to postfix: 
  
  ![image](https://user-images.githubusercontent.com/57759154/125867388-80dc5a76-2d91-4a57-9ec3-e22ddef1ab39.png)


- **Explain how Thompson's construction for regular expressions works**

  [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction), commonly known as the McNaughton–Yamada–Thompson algorithm, turns postfix regular expressions into nondeterministic finite automaton (NFA) which is going to recognize patterns of text. Thompson's construction is an algorithm to construct an NFA from regular expression. NFA recognizes the same language as the regular expression.

  Thompson's construction may be thought of in terms of NFA’s fragments.
You presume that the regular expression is in postfix, the stack of fragments of the overall nondeterministic finite automaton (NFA) is created and the normal characters such as `“.” , “*“, and “|”` are pushed onto the stack. Special characters will be considered like operators, having the ability to pop of the stack and perform something with what’s pop from the stack.

  The one or two nondeterministic finite automaton (NFA) fragments on the stack are joined together to form a new start state, which is then joined with e arrows, and then from one or two NFA’s fragment get new NFA fragment and push that onto the stack.
  
  **Rules**
  
  The following images are from [Visualizing Thompson’s Construction Algorithm for NFAs, step-by-step](https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b)
  
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

  A non-regular language, often known as an irregular language, is one that cannot be defined by a regular expression. Non-regular languages outnumber regular languages by a significant amount. According to Kleene's theorem, no FA or TG may accept a non-regular language.
  
  The existence of non-regular languages is ensured by the fact that regular languages of any alphabet are countable, and we know that the set of all subsets of strings is not countable. Nonetheless, the goal of creating non-regular languages is to show that certain languages that are "computable" in some way are not regular.
  
  Pumping Lemma is a well-known theorem that uses the Pigeon Hole Principle to determine if a language is regular or not. However, the pumping lemma is a negative test; if a language does not meet it, we can be certain that it is not regular; if it does, the language may or may not be regular.
  
  The languages Palindrome is a examples of nonregular languages. A palindrome is a word, number, phrase, or other character sequence that reads the same backward as it does forward.


# Resources
https://en.wikipedia.org/wiki/Thompson%27s_construction

https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b

https://web.microsoftstream.com/video/d6d9a2d8-b23e-4abf-b1b7-af3a2d44b82f?referrer=https:%2F%2Flearnonline.gmit.ie%2F

https://en.wikipedia.org/wiki/Infix_notation

https://en.wikipedia.org/wiki/Reverse_Polish_notation

https://pediaa.com/difference-between-prefix-and-postfix/#Infix

https://slideplayer.com/slide/12946344/

https://www.geeksforgeeks.org/how-to-identify-if-a-language-is-regular-or-not/
