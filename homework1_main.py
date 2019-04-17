from homework1 import Question
class invalidAnswerError(Exception):
    pass
def getAns():
    invalid = True
    while (invalid):
        try:
            userAns = int(input('Enter your answer: '))
            if userAns not in range(1,5):
                raise invalidAnswerError
            invalid = False
            return userAns
        except (invalidAnswerError, ValueError):
            print('Error: enter a valid answer')
            continue

        
if __name__ == "__main__":
    print('Welcome to the Adventure Time Episode Quiz')
    for x in range(20):
        print('-', end = '')
    print('Match the epsiode description to the title of the episode.')
    
    questionList = []
    
    question1 = Question()
    question1.setPrompt('Princess Bubblegum accidentally made a potion thing that was supposes to bring people back alive, but turned them into zombies instead.')
    question1.setAns1('Wizard')
    question1.setAns2('What is Life?')
    question1.setAns3('Slumber Party Panic')
    question1.setAns4('Dungeon')
    question1.setAnsCorrect(3)
    questionList.append(question1)

    question2 = Question()
    question2.setPrompt("Marceline takes Finn and Jake's treehouse")
    question2.setAns1('Evicted!')
    question2.setAns2('Gut Grinder')
    question2.setAns3('Rainy Day Daydream')
    question2.setAns4('What Have You Done?')
    question2.setAnsCorrect(1)
    questionList.append(question2)

    question3 = Question()
    question3.setPrompt("Marceline and her ghost friends tricks Finn and Jake that they made them into vampires, but her ghost friends try to kill Finn and Jake.")
    question3.setAns1('The Real You')
    question3.setAns2('Death in Blossom')
    question3.setAns3('The Limit')
    question3.setAns4('Heat Signature')
    question3.setAnsCorrect(4)
    questionList.append(question3)

    question4 = Question()
    question4.setPrompt("A deer rampages in the candy kingdom, breaks Finn's Legs, and hits Jake's Head. Finn wakes up and Jake has gone crazy acting like it's his birthday.")
    question4.setAns1('No One Can Hear You')
    question4.setAns2('Wizard Battle')
    question4.setAns3('From Bad to Worse')
    question4.setAns4('The New Frontier')
    question4.setAnsCorrect(1)
    questionList.append(question4)

    question5 = Question()
    question5.setPrompt('Lady Ranicorn and Princess Bubblegum save Finn and Jake from Iceking')
    question5.setAns1('Return to the Nightosphere')
    question5.setAns2('In Your Footsteps')
    question5.setAns3('Lady and Peebles')
    question5.setAns4('Too Young')
    question5.setAnsCorrect(3)
    questionList.append(question5)

    question6 = Question()
    question6.setPrompt("BMO tries to solve the mystery of Finn's missing sock")
    question6.setAns1('Burning Low')
    question6.setAns2('Gotcha!')
    question6.setAns3('You Made Me')
    question6.setAns4('BMO Noire')
    question6.setAnsCorrect(4)
    questionList.append(question6)

    question7 = Question()
    question7.setPrompt("Ice King takes princess's body parts and Finn and Jake investigate")
    question7.setAns1('The Hard Easy')
    question7.setAns2('I Remember You')
    question7.setAns3('Princess Monster Wife')
    question7.setAns4('Two Sword')
    question7.setAnsCorrect(3)
    questionList.append(question7)

    question8 = Question()
    question8.setPrompt('Finn and Jake try to wake up Marceline by going into her memories, but after they do, her ex-bf tricked them into Marceline liking him again')
    question8.setAns1('Memory of a Memory')
    question8.setAns2('The Creeps')
    question8.setAns3('Orb')
    question8.setAns4('What Was Missing')
    question8.setAnsCorrect(1)
    questionList.append(question8)

    question9 = Question()
    question9.setPrompt('Finn tells lies cause to trouble between Ice King and Flame Princess.')
    question9.setAns1('Shh!')
    question9.setAns2('Frost and Fire')
    question9.setAns3('All Your Fault')
    question9.setAns4('Bad Little Boy')
    question9.setAnsCorrect(2)
    questionList.append(question9)

    question10 = Question()
    question10.setPrompt('Fern takes Finn to a dungeon to trap Finn, so Fern can become the real Finn')
    question10.setAns1('Three Buckets')
    question10.setAns2('The Wild Hunt')
    question10.setAns3('Son of Rap Bear')
    question10.setAns4('Come Along with Me')
    question10.setAnsCorrect(1)
    questionList.append(question10)

    playerNum = 1
    player1Score = 0
    player2Score = 0

    for questionNumber in range(len(questionList)):
        print('Player {}, here is your question: '.format(playerNum))
        print(questionList[questionNumber].askQuestion())
        if playerNum == 1:
            if getAns() == questionList[questionNumber].getAnsCorrect():
                print('Correct')
                player1Score += 1
                
            else:
                print('Incorrect')
            print('Player {} score: {}'.format(playerNum, player1Score))
            playerNum = 2
        elif playerNum == 2:
            if getAns() == questionList[questionNumber].getAnsCorrect():
                print('Correct')
                player2Score += 1

            else:
                print('Incorrect')
            print('Player {} score: {}'.format(playerNum, player2Score))
            playerNum = 1
    print('Final score:\nPlayer 1: {}\nPlayer 2: {}'.format(player1Score, player2Score))
    if player1Score == player2Score:
        print('Tie')
    elif player1Score > player2Score:
        print('Player 1 wins')
    elif player2Score > player1Score:
        print('Player 2 wins')
