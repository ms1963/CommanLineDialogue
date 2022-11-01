# CommanLineDialogue
A small class to ask the user questions on the command line

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
    interaction.setLineCharacter(" ")
    answer = interaction.exec()
    if answer == None:
        print("I see, you don't wanna answer this question")
    else:
        print("You are " + str(answer))
    
```
