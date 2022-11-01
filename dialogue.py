
# class Dialogue is used to obtain an answer from the user 
# on the command line 
# 
# Arguments:
# title:      is displayed at beginning of iteration 
# question:   question to displayed to the user 
# prompt:     command prompt to be used on the command line 
# hints:      additional hints to print on command line 
# ack:        the text printed when user successfully answers
# predicate:  lambda/function that checks the input for 
#             complying with the specification
# conversion: lambda/function that converts the user answer to the 
#             required type
    
class Dialogue:
    def __init__(self, title, question, prompt, hints, ack, predicate, conversion):
        self.title = title
        self.question = question
        self.prompt = prompt
        self.hints = hints
        self.ack = ack
        self.predicate = predicate
        self.conversion = conversion
        self.iters = 3
        self.char = ""
        
    def setRepetitions(self, count):
        assert count > 0, "Number must be greater than 0"
        self.iters = count
        
    def setLineCharacter(self, char): 
        self.char = char
        
    def drawBorder(self, length):
        size = len(self.char)
        if (len != 0 and len(self.char) != 0):
            for i in range(0,(length+1) // size): 
                print(self.char, end = "")
        print()
        
    def exec(self):
        maxsize = max(len(self.title), len(self.hints))
        if (maxsize != 0):
            self.drawBorder(maxsize)
            print(self.title)
            print(self.hints)
            self.drawBorder(maxsize)
        completed = False
        counter = 0
        value = None
        while not completed and counter < self.iters:
            try:
                print(self.question)
                # ask user with specified prompt
                answer = input(self.prompt)
                # call predicate on answer
                completed = self.predicate(answer)
                if not completed:
                    print("Invalid input")
                else:
                    # call conversion on answer
                    value = self.conversion(answer)
            # user interrupted by control-c
            except KeyboardInterrupt:
                print("interrupted by ctrl-c")
                return None
            except: # predicate or conversion failed
                if counter + 1 < self.iters:
                    print("Input error => try again!")
                completed = False
            finally:
                # increase counter after errors
                if not completed:
                    counter += 1
        if completed:
            # print acknowledgement for answering the question
            print(self.ack)
        return value
        

        


    
    
