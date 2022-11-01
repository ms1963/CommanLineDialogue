# Command Line Dialogue (for Python)
A small class to ask the user questions on the command line.

As I often have to implement user interactions such as asking questions in command line programs, I just developed a primitive class Dialogue. Dialogue also intercepts keyboard interrupts (control-C) to prevent program abortion. 



The exec()-function expects the following arguments:

+ title: the title to be printed by Dialogue
+ hints: additional information to be printed by Dialogue
+ question: the question or statement to print
+ ack: the message printed if the user submitten a valid answer
+ predicate:  predicate()-function is used by Dialogue to check wether the input is correct
+ conversion: conversion() - function is used to convert the user answer to a  target type

It returns the value (calculated by conversion() on valid user input, or None if the dialog was closed by control-c, the user did not provide a valid answer within the repetitions.

In addition the following methods are provided:

+ setRepetitions(): how often should the Dialogue repeat until the dialogue is closed
+ setLineCharacter(): what character should be used to draw lines above and below title resp. hints. Per default " " is used



Demo code for usage:
```
    interaction = Dialogue( title = "Question of the day", 
                            prompt = "% ", 
                            question = "How old are you?", 
                            hints = "(you should lie)", 
                            ack = "Thanks for your answer",  
                            predicate = lambda x: int(x) in range(0, 100), 
                            conversion = lambda x: int(x)
                         )
                            
    interaction.setRepetitions(2)
    interaction.setLineCharacter("=")
    answer = interaction.exec()
    if answer == None:
        print("I see, you don't wanna answer this question")
    else:
        print("You are " + str(answer) + " years old")
    
```


Example dialogue:
```
================================
Question of the day
(age must be between 0 and 100)
================================
How old are you?
% u
Input error => try again!
How old are you?
% 887
Invalid input
How old are you?
% 18
Thanks for your answer
You are 18 years old
>>> 
```
