class Question:

    def __init__(self, prompt  = '', ans1 = '', ans2 = '', ans3 = '', ans4 = '', ansCorrect = 0):
        self.__prompt = prompt
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__ansCorrect = ansCorrect

    def __str__(self):
        return str(self.__prompt)

    def getPrompt(self):
        return self.__prompt

    def getAns1(self):
        return self.__ans1

    def getAns2(self):
        return self.__ans2

    def getAns3(self):
        return self.__ans3

    def getAns4(self):
        return self.__ans4

    def getAnsCorrect(self):
        return self.__ansCorrect
    
    def setPrompt(self, question):
        self.__prompt = question

    def setAns1(self, ans):
        self.__ans1 = ans
    
    def setAns2(self, ans):
        self.__ans2 = ans

    def setAns3(self, ans):
        self.__ans3 = ans
    
    def setAns4(self, ans):
        self.__ans4 = ans
    
    def setAnsCorrect(self, ans):
        self.__ansCorrect = ans

    def askQuestion(self):
        return ('{}\n1. {}\n2. {}\n3. {}\n4. {}'.format(self.__prompt, self.__ans1, self.__ans2, self.__ans3, self.__ans4))
    


    
    
    