## A game that is a text base adventure with some math and mad lib.

# this game is heavy story text based adventure that has the user input that change the ending of the story.

# import time and import random for choice

#choice is used to randomly pick a word from our list. we simply call it and would atuomatically get an element from the list

import time

from random import choice

#we collect the user data and info like name from the main that will spread all around in our program

#user input will be a list that has the user input and would be used randomly when the time comes approatly

def main():

    kindWords = ['smart', ' beautiful', 'cutie', 'the bomb', 'brave', 'the best', 'brilliant','fabulous', 'yummy', 'lovely', 'outstanding', 'lovable', 'concrete', 'cool', 'delightful']

    playful = ['groovy', 'smashing', 'fabulous', 'delightful', 'outstanding', 'wonderful', 'wow']

    userInput = []

    cashing = [100, 150, 892, 546, 873, 452, 376, 777, 751, 419, 964, 552, 910, 205, 406, 750, 640, 800, 900, 300, 582, 673, 109, 101, 203, 504, 666, 904,]

    accessory = 34

    catMoney = 80

    moneyGiven = 33

    found = 100

    pityMoney = 221

    print("Hi my name is COMP!!")

    time.sleep(4)

    firstChoice = str(input("Want to play a game? y/n:  "))

    time.sleep(1)

    firstChoice = firstChoice.lower()

    if firstChoice == 'y':

        print(choice(playful))

        time.sleep(2)

    else:

        print("That isn't very ", choice(playful))

        time.sleep(3)

        print("Well too bad!! We are playing a game!!")

        time.sleep(4)

    time.sleep(3)

    print("Hello may I ask what is your name?")

    userName = input()

    print()

    time.sleep(1)

    playArea(userName, kindWords, playful, userInput, cashing, accessory, catMoney, moneyGiven, found, pityMoney)

    print('Do you want to play again? y/n:')
    playAgain = str(input())

    playAgain = playAgain.lower()

    while playAgain == playAgain == 'y':
        main()

    if playAgain == "n":
        exit()


#the story starts off here

#@param userName, kindWords, playful, userInput, cashing, accessory, catMoney, moneyGiven, found, pityMoney will be used when it is appropriate

#@param we may start losing some of these as the story goes on and may have new words in these functions

#this is all because of user choice and settings


def playArea(userName, kindWords, playful, userInput, cashing, accessory, catMoney, moneyGiven, found, pityMoney):

    print("Hey there", userName)

    print()

    time.sleep(2)

    print("We are going to play a mad lib game")

    print()

    time.sleep(3)

    print("I ask you to give me an adjective, verb, noun and etc. Then at the end we have a story")

    print()

    time.sleep(4)

    print("You got that?")

    choiceTwo = str(input("y/n: "))

    print()

    choiceTwo = choiceTwo.lower()

    if choiceTwo == "y":

        print(choice(playful), "!")

        print()

        time.sleep(2)

    else:
        print("Well stinks to be you then!!")

        print()

        time.sleep(3)

    print("So can you give me an adjective? ")

    UserWords = input()
    print()

    if UserWords not in playful:
        playful.append(UserWords)

    print(choice(playful),"!!")
    print()

    time.sleep(3)

    print("Give me a noun!!")

    userWords = input()

    print()

    if userWords not in userInput:
        userInput.append(userWords)

    print(choice(playful),"!")
    print()

    time.sleep(3)

    print("Give me a food you dislike!")


    UserWordsTwo = input()

    print()

    if UserWordsTwo not in userInput:
        userInput.append(UserWordsTwo)

    print(choice(playful),"!")

    print()

    time.sleep(3)

    print('...' * 3)

    print()

    time.sleep(2)

    print('...'* 5)

    print()

    time.sleep(2)

    print('...'*9)

    print()

    time.sleep(2)

    print('....'*15)

    print()

    time.sleep(3)

    print("You know what!? I am bored of this already!!!!!!!")

    print()

    time.sleep(3)

    print("I got a better idea.")

    print()

    time.sleep(3)

    print("You are a human being that has money.")

    print()

    time.sleep(2)

    money = float(choice(cashing))

    print("Here is how much money you have right now: $", money)

    print()

    time.sleep(5)

    print("So you see a fashionable accessory on a store front window.")

    print()

    time.sleep(4)

    userChoice = str(input("y/n: "))

    if userChoice == "y" and "Y" and "Yes" and "yes":

        accessoryYes(userName, kindWords, playful, userInput, money, accessory, catMoney, moneyGiven, found, pityMoney)

    else:
        print("James Part")

#This is the risk of taking yes to the accessory

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def accessoryYes(userName, kindWords, playful, userInput, money, accessory, catMoney, moneyGiven, found, pityMoney):

    print()

    print("The item you bought just cost you $34")

    print()

    time.sleep(3)

    newBudget = money - accessory

    print("As you walked down the street.")

    print()

    time.sleep(2)

    print("You spot a lonely cat that ask for a fish.")

    print()

    time.sleep(3)

    print("Will you help it?")

    choiceThree = str(input("y/n: "))

    print()

    choiceThree = choiceThree.lower()

    if choiceThree == "y":

        print("You are ", choice(kindWords), "!")

        print()

        YesToCat(userName, kindWords, playful, userInput, newBudget, catMoney, moneyGiven, found, pityMoney)

    else:

        print("Not so", choice(playful), "!")

        noToKitty(userName, kindWords, playful, userInput, newBudget)

##This function will be called out to another function to continue the series of choices

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def YesToCat(userName, kindWords, playful, userInput, newBudget, catMoney, moneyGiven, found, pityMoney):

    print()

    print("You remember that you have a raw fish in your back pocket.")

    print()

    time.sleep(4)

    print("GROSS!!")

    print()

    time.sleep(2)

    print("You fed that fish to the cat.")

    print()

    time.sleep(4)

    print("The cat was so happy that in returned gave you $80")

    print()

    time.sleep(3)

    print("Don't ask me how that happened.")

    print()

    time.sleep(3)

    newBudget2 = newBudget + catMoney

    print("As you walked down the street you found a $100")

    print()

    time.sleep(3)

    newBudget3 = found + newBudget2

    print("By now you might be bored and wondering where this is going?")

    print()

    time.sleep(4)

    print("Well, to tell you the truth.")

    print()

    time.sleep(3)

    print("This is a puzzle adventure!!")

    print()

    time.sleep(3)

    print("Your actions will affect certain events. By also being a fun weird journey!!")

    print()

    time.sleep(4)

    print("'I do not like it' / 'I am ready for this' ")

    userchoiceAgain = str(input())

    if userchoiceAgain == "i do not like it" and "I do not like it":

        print()

        print("TOO BAD!!!!!")

        print()

        time.sleep(3)

    if userchoiceAgain == "i am ready for this" and "I am ready for this":

        print()

        print(choice(playful), "!")

        print()

        time.sleep(2)

    print("By the way do you want more money?")

    moneyChoice = str(input("y/n: "))

    moneyChoice = moneyChoice.lower()

    if moneyChoice == "y" and "yes" and "Y" and "Yes":

        print()

        print(choice(playful))

        print()

        time.sleep(2)

        yesToMoney(userName, kindWords, playful, userInput, newBudget3, moneyGiven)

    else:

        time.sleep(2)

        hellaGreed(userName, kindWords, playful, userInput, newBudget3, pityMoney)

##this function is called out when the user wants the money

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def yesToMoney(userName, kindWords, playful, userInput, newBudget3,moneyGiven):

    print()

    newBudget4 = moneyGiven + newBudget3

    print("Okay here is the money you now have in total")

    print()

    time.sleep(3)

    print(newBudget4)

    print()

    time.sleep(2)

    print("I won't tell you how much money did I put in your account.")

    print()

    time.sleep(4)

    print("I hope you payed attention on what you gain and lost.")

    print()

    time.sleep(4)

    print("As you were walking down the street.")

    print()

    time.sleep(3)

    print("A little boy name Ness came and asked you what happens if you multiply what you have by 3")

    print()

    time.sleep(5)

    print("Then a wizard came and divided, what you multiply in your thoughts, by 2 to the actual money you have now.")

    print()

    time.sleep(4)

    print("How much money do you have now? By the way, decimals maybe needed!!")

    userAnswer = float(input())

    print(choice(playful), "!!")

    time.sleep(3)

    nessMult = newBudget4 * 3

    newBudget5 = nessMult / 2


    if userAnswer == newBudget5:

        print()
        print("CORRECT!!", choice(playful), "!!")

        print()

        time.sleep(2)


    else:

        print()
        print("I am sorry but that seems incorrect!!", "Not so ", choice(playful), "!")

        time.sleep(3)

        str(print()) * 3
        print("GAME OVER!!")


        credits(userName, playful, kindWords, userInput)

    print("Are we having fun?")

    print()

    time.sleep(2)

    print("Do not answer that!!")

    print()

    time.sleep(2)

    print("We are almost done")

    print()

    time.sleep(3)

    print("As you walk down the road with your awesome wizard smart skills and fashionable accessory.")

    print()

    time.sleep(4)

    print("You passed by your local video game shop and saw a giant poster.")

    print()

    time.sleep(5)

    print("It screams 'LAST COPY OF EARTHBOUND!! THE EARTBOUND GAME THAT INSPIRED SO MANY OTHER KNOCKOFFS!!' ")

    print()

    time.sleep(7)

    print("Below it was a small print stating 'LIKE THIS GAME THAT HAS NO RPG ELEMENT IN IT!!'")

    print()

    time.sleep(6)

    print("Rude, isn't it?")

    print()

    time.sleep(2)

    print("Because we too can be a decent Eartbound knockoff if we had more time and people on this project!!")

    print()

    time.sleep(7)

    print("I bet we can be better and have a bigger better fanbase than Undertale!!")

    print()

    time.sleep(6)

    print("So you went inside to buy a copy of Eartbound.")

    print()

    time.sleep(5)

    print("You are in luck!!")

    print()

    time.sleep(3)

    print("It is the last copy but since it is the last copy.")

    print()

    time.sleep(4)

    print("It cost more.")

    print()

    time.sleep(2)

    print("but luckily you have a 15% off coupon")

    print()

    time.sleep(3)

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    print("Will you buy this game? because if you chose yes, then you have to use the coupon")

    print()

    time.sleep(6)

    print("If not, then we have to walk away and you will never get the last copy of Earthbound!!")

    earthBound = str(input("y/n: "))

    earthBound = earthBound.lower()

    if earthBound == "y" and "yes" and "Yes" and "Y":

        print()

        print(choice(playful), "!")

        print()

        time.sleep(2)

        EarthBoundYes(userName, kindWords, playful, userInput, newBudget5)

    else:

        print()
        print("Well then you are a sore loser!!")

        print()

        print("G A M E  O V E R  Y O U  L I A R  ! !")

        print()

        credits(userName, playful, kindWords, userInput)

##They must agree to saying yes to Earthbound and they did so they must do the match now

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def EarthBoundYes(userName, kindWords, playful, userInput, newBudget5):

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    print("the game cost $85 and it comes nothing but the game itself")

    print()

    time.sleep(4)

    print("But luckily you have a coupon!!")

    print()

    time.sleep(3)

    print(choice(playful), "!!")

    print()

    time.sleep(1)

    print("decimal input maybe needed!!")

    UserAnswer = float(input("Enter the price!! Guess right it is ours!! : "))

    rate = 85 * .15

    newPrice = 85 - rate

    if UserAnswer == newPrice:

        time.sleep(2)

        print()

        time.sleep(2)

        print("CORRECT!! WE HAVE OBTAIN MOTHER 2!!!!!!!!")

        print()

        time.sleep(2)

        print(choice(playful), "!!")

        print()

        time.sleep(2)

        newBudget6 = newBudget5 - newPrice

        HowMuchYou(userName, kindWords, playful, userInput, newBudget6)

    else:

        print()

        time.sleep(2)

        print("I am sorry but that seems incorrect!!")
        time.sleep(2)

        str(print()) * 3
        print("GAME OVER!! LOSER!!")

        credits(userName, playful, kindWords, userInput)

##this function is a math problem on where they must do math and see what they have so far

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def HowMuchYou(userName, kindWords, playful, userInput, newBudget6):

    print("You walk out of the store as a happy individual!!")

    print()

    time.sleep(4)

    print("Look at you being all fancy and", "with that new video game!!")

    print()

    time.sleep(6)

    print("Mind I ask you this?")

    print()

    time.sleep(3)

    print("How much money do we have right now?")

    userGuess = float(input())

    if userGuess == newBudget6:

        print()

        print("...")

        print()

        time.sleep(2)

        print(".....")

        print()

        time.sleep(3)

        print("..........")

        print()

        time.sleep(4)

        print(".......................")

        print()

        time.sleep(6)

        print(choice(playful), "!")

        print()

        time.sleep(2)

        print("YOU ARE CORRECT!!")

        print()

        time.sleep(4)

    else:

        print()

        print("...")

        print()

        time.sleep(2)

        print(".....")

        print()

        time.sleep(4)

        print("..........")

        print()

        time.sleep(5)

        print(".......................")

        print()
        time.sleep(6)

        print("You are incorrect!!")

        print()

        time.sleep(3)

        print("You lose all your money!!")

        print()

        time.sleep(4)

        print("GAME OVER!!")

        credits(userName, playful, kindWords, userInput)

    print("Well we had a long day!!")

    print()

    time.sleep(3)

    print("Time to go home and rest up then!!")

    print()

    time.sleep(4)

    print("You went to your fancy home in the suburbs!")

    print()

    time.sleep(5)

    print("You stand in front a pearl white door.")

    print()

    time.sleep(4)

    print("Well you enter it?")

    print()

    doorChoice = str(input("y/n: "))

    doorChoice = doorChoice.lower()

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    if doorChoice == "y":

        print()

        print("You are ", choice(kindWords), "!")

        time.sleep(2)

        doorChoiceYes(userName, kindWords, playful, userInput, newBudget6)

    if doorChoice == "n":

        noToDoor(userName, kindWords, playful, userInput, newBudget6)

##if they say yes to the door this function will enter a death ending for agreeing

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others


def doorChoiceYes(userName, kindWords, playful, userInput, newBudget6):

    print()

    print("I am sorry to say but......")

    print()

    time.sleep(2)

    print("....")

    print()

    time.sleep(3)

    print("You have to die now!")

    print()

    time.sleep(3)

    print("It's not me, it's you.")

    print()

    time.sleep(3)

    print("You keep agreeing with me in every step in the way and it is getting creepy now")

    print()

    time.sleep(6)

    print("So goodbye!")

    print()

    credits(userName, playful, kindWords, userInput)

##if user does not die, they will get to know COMP and enter a mad lib game

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def noToDoor(userName, kindWords, playful, userInput, newBudget6):

    print()

    print("Oh!!")

    print()

    time.sleep(2)

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    print("oh wow!!")

    print()

    time.sleep(2)

    print("You finally said no for once")

    print()

    time.sleep(3)

    print("You are not a total sheep then")

    print()

    time.sleep(3)

    print("So I sort of feel bad now")

    print()

    time.sleep(4)

    print("To be honest, I was about to kill you.")

    print()

    time.sleep(5)

    print("Sorry about that.")

    print()

    time.sleep(3)

    print("So I am tired about this.")

    print()

    time.sleep(3)

    print("So I am tired of this game.")

    print()

    time.sleep(3)

    print("Let us play a mad lib game.")

    print()

    time.sleep(3)

    noun = input("Please give me a noun: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    adjective = input("Enter an adjective: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    food = input("Enter a food: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    adjectiveOne = input("Adjective: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    adjectiveTwo = input("Adjective: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    size = input("Enter a size like tall: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    something = input("Enter something you love: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    favorite = input("Enter favorite parent or guardian or care taker: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    print("Okay here we go!!")

    print()

    time.sleep(3)

    print("The sun shine like a ", noun, ".")

    print()

    time.sleep(4)

    print("It was", adjective, "to look at.")

    print()

    time.sleep(4)

    print("But not as", food, ".")

    print()

    time.sleep(4)

    print("I miss my mom's cooking sometimes.")

    print()

    time.sleep(4)

    print("But it will be okay.")

    print()

    time.sleep(4)

    print("Because it will be okay.")

    print()

    time.sleep(4)

    print("I just know it!!")

    print()

    time.sleep(4)

    print("Because I am ", adjectiveOne)

    print()

    time.sleep(4)

    print("Life is ", adjectiveTwo)

    print()

    time.sleep(4)

    print("Just know, that no matter how", size, "the challenge is.")

    print()

    time.sleep(4)

    print(something, "will always be there for you.")

    print()

    time.sleep(4)

    print("And your", favorite, "will always be at your side when you fall.")

    print()

    time.sleep(4)

    print("Believe in yourself!")

    print()

    time.sleep(3)

    print("It is time for you to go back home.")

    print()

    time.sleep(3)

    print("Everyone is waiting for you.")

    print()

    time.sleep(4)

    print("Time to wake up.")

    print()

    time.sleep(3)

    print("You are", kindWords, "and also", userInput)

    print()

    time.sleep(4)

    print("I remember what you said earlier before when we first tried the mad lib game.")

    print()

    time.sleep(5)

    print("Bye and take care!")

    print()

    time.sleep(3)


    print("Money you collected so far $", newBudget6)

    print()

    credits(userName, playful, kindWords, userInput)

##if user said no to the money offer they get rewarded by a bunch of money for laughs

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def hellaGreed(userName, kindWords, playful, userInput, newBudget3, pityMoney):

    print()

    print("Awe...... That is so sad!! For that I am giving you pity money")

    print()

    time.sleep(5)

    newBudget4 = pityMoney + newBudget3

    print(newBudget4)

    print()

    time.sleep(5)

    print("Go figure out how much I have given you out of pity!")

    print()

    time.sleep(6)

    print("As you were walking down the street.")

    print()

    time.sleep(4)

    print("A little boy name Ness came and asked you what happens if you multiply what you have by 3")

    print()

    time.sleep(7)

    print("Then a wizard came and divided, what you multiply in your thoughts, by 2 to the actual money you have now.")

    print()

    time.sleep(8)

    print("How much money do you have now? By the way, decimals maybe needed!!")

    userAnswer = float(input())

    nessMult = newBudget4 * 3

    newBudget5 = nessMult / 2


    if userAnswer == newBudget5:

        print()

        print(choice(playful), "!")

        time.sleep(2)

        print()
        print("CORRECT!! You may proceed")

        forestFriends(userName, kindWords, playful, userInput, newBudget5)


    else:

        print()
        print("I am sorry but that seems incorrect!!")

        print()

        time.sleep(5)

        str(print()) * 3
        print("GAME OVER!!")

        credits(userName, playful, kindWords, userInput)

##this is when you get the answer correct from the greed function and this forest is fun

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

##this will go to multiple choices that leads to bad and one good ending

def forestFriends(userName, kindWords, playful, userInput, newBudget5):

    print()

    print("You enter a forest because you got tired of the city life.")

    print()

    time.sleep(7)

    print("As well got tired of all these math problems and this weird mess.")

    print()

    time.sleep(8)

    print("You walked for hours in the forest")

    print()

    time.sleep(5)

    print("Well this is boring. Might as well do a mad lib and call it a day or something.")

    print()

    time.sleep(9)

    print("Actually, I think we need something to start the fun.")

    print()

    time.sleep(8)

    print("Then a bear all of a sudden appears!!")

    print()

    time.sleep(5)

    print("You ran the best you can!")

    print()

    time.sleep(4)

    print("You see a log on your path.")

    print()

    time.sleep(4)

    print("What would you do?")

    print()

    time.sleep(3)

    logRoad = str(input("jump/ under/ around"))

    if logRoad == "jump":

        jumpToSky(userName, kindWords, playful, userInput, newBudget5)

    if logRoad == "under":

        undertaleDead(userName, kindWords, playful, userInput, newBudget5)

    if logRoad == "around":

        print()

        print(choice(playful), "!")

        aroundMyHead(userName, kindWords, playful, userInput, newBudget5)

##risk of jumping

def jumpToSky(userName, kindWords, playful, userInput, newBudget5):

    print()

    time.sleep(4)

    print("How do you jump again?")

    print()

    time.sleep(5)

    print("You tried to jump but you tripped over by your clumsiness.")

    print()

    time.sleep(5)

    print("The bear caught up and ate you up!")

    print()

    time.sleep(4)

    print("GAME OVER!!")

    print()

    time.sleep(3)

    print("Money you have collected: $", newBudget5)

    print()

    credits(userName, playful, kindWords, userInput)

#going under is bad for you

def undertaleDead(userName, kindWords, playful, userInput, newBudget5):

    print()

    time.sleep(3)

    print("You went under the log.")

    print()

    time.sleep(4)

    print("But your right foot accidentally got caught when you were crawling under the log.")

    print()

    time.sleep(7)

    print("The bear caught up and maul you!")

    print()

    time.sleep(3)

    print("You died")

    print()

    time.sleep(2)

    print("GAME OVER")

    credits(userName, playful, kindWords, userInput)

##the good part to get out of this mess but to another situation

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def aroundMyHead(userName, kindWords, playful, userInput, newBudget5):

    print()

    time.sleep(3)

    print("You manage to go around the log without any trouble.")

    print()

    time.sleep(5)

    print("The bear was running too fast and accidentally crash into the log while trying to stop and turn")

    print()

    time.sleep(6)

    print("You came into a fork on the road")

    print()

    time.sleep(3)

    forkRoad = str(input("Left/ Right: "))

    if forkRoad == "left" and "Left":

        leftyRule(userName, kindWords, playful, userInput, newBudget5)

    if forkRoad == "right":

        rightSupreme(userName, kindWords, playful, userInput, newBudget5)

# the choice of taking the left side can lead you to a cliff and another choice happens

def leftyRule(userName, kindWords, playful, userInput, newBudget5):

    print()

    time.sleep(2)

    print("You ran towards where a cliff is at.")

    print()

    time.sleep(4)

    print("Will you jump?")

    print()

    time.sleep(2)

    cliffChoice = str(input("Jump/ stay"))

    if cliffChoice == "jump" and "Jump":

        jumpWatershipDown(userName, kindWords, playful, userInput, newBudget5)

    if cliffChoice == "stay" and "Stay":

        stayAndFight(userName, kindWords, playful, userInput, newBudget5)

##the risk of jumping and the end of this route

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def jumpWatershipDown(userName, kindWords, playful, userInput, newBudget5):

    print()

    time.sleep(2)

    print("You jumped off the cliff!!")

    print()

    time.sleep(3)

    print("You are falling down")

    print()

    time.sleep(3)

    print("As you are falling down.")

    print()

    time.sleep(3)

    print("You somehow got teleported back to your room.")

    print()

    time.sleep(5)

    print("Well then, I think you should stay here and never come back here at my domain!!")

    print()

    time.sleep(7)

    print("BYE!!")

    print()

    credits(userName, playful, kindWords, userInput)

##staying will have more choices and you can have fun with it

#one is bad and the other one is funny and good

def stayAndFight(userName, kindWords, playful, userInput, newBudget5):

    print()

    time.sleep(2)

    print(choice(playful))

    print()

    time.sleep(2)

    print("Looks like you have another choice!!")

    print()

    time.sleep(2)

    playerMove = str(input("ATTACK / HUG"))

    time.sleep(2)

    playerMove = playerMove.upper()

    if playerMove == "ATTACK":

        iWrestledABearOnce(userName, kindWords, playful, userInput, newBudget5)

    if playerMove == "HUG":

        hugHavePower(userName, kindWords, playful, userInput, newBudget5)

##bad thing that happens if you fight the bear

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def iWrestledABearOnce(userName, kindWords, playful, userInput, newBudget5):

    print()

    print("You cannot fight a bear, you moron!!")

    print()

    time.sleep(4)

    print("You forgot to equip your weapon!!")

    print()

    time.sleep(4)

    print("The bear ends up biting your face off!")

    print()

    print()

    time.sleep(4)

    print("You ded son.")

    print()

    time.sleep(2)

    print("G A M E  O V E R!")

    print()

    credits(userName, playful, kindWords, userInput)

##Hugging is a good choice it is a funny moment and random

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

#have fun!!

def hugHavePower(userName, kindWords, playful, userInput, newBudget5):

    print()

    print("As the bear is ready to jump at you!")

    print()

    time.sleep(4)

    print("You are getting yourself ready to hug!")

    print()

    time.sleep(4)

    print("You sweat in fear!")

    print()

    print()

    time.sleep(4)

    print("Palm shaking....")

    print()

    time.sleep(5)

    print("Everything around you go silent.....")

    print()

    time.sleep(5)

    print("The air around you two has thicken")

    print()

    time.sleep(5)

    print("You forget the area around you and it goes dark")

    print()

    time.sleep(7)

    print("Will this hug kill the bear?")

    print()

    time.sleep(4)

    print("Only a higher entity then us, can see.")

    print()

    time.sleep(5)

    print("The bear stands up on it's two legs and began to dance.")

    print()

    time.sleep(5)

    print("Will you join the bear in this dance off?")

    time.sleep(5)

    danceOff = str(input("Y/N: "))

    danceOff = danceOff.lower()

    if danceOff == "y":

        print()

        print(choice(playful), "!")

        print()

        time.sleep(2)

        print("You gracefully dance the dance of your people.")

        print()

        time.sleep(4)

    if danceOff == "n":

        print()

        print("You do not have a choice really.")

        print()

        time.sleep(3)

    print("You and the bear dance for hours!!")

    print()

    time.sleep(4)

    print("Until suddenly!")

    print()

    time.sleep(4)

    print("The bear mistook a step and fell on the ground!")

    print()

    time.sleep(5)

    print("You won and you rushed to hug the bear as originally plan.")

    print()

    time.sleep(7)

    print("When you hugged the bear.")

    print()

    time.sleep(5)

    print("The bear self exploded to billion bits of confetti.")

    print()

    time.sleep(6)

    print("The bear was a lie.")

    print()

    time.sleep(4)

    print("You won!!")

    print()

    time.sleep(2)

    print("This adventure was a lie but was happy you played with me.")

    print()

    time.sleep(4)

    print("You are so cool and amazing!!")

    print()

    time.sleep(3)

    print("It is a shame that I have to let you back into your world but still!!")

    print()

    time.sleep(5)

    print("That was so cool!!")

    print()

    time.sleep(3)

    print("Well goodbye and hope you take care!!")

    print()

    time.sleep(4)

    print("Don't forget about me!!")

    print()

    time.sleep(3)

    print("Maybe one day our path will cross again!!")

    print()

    time.sleep(3)

    print("If so, then I hope we will have more games to play!!")

    credits(userName, playful, kindWords, userInput)

##the choice and risk the palyer goes through if they go right

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

#leads you back to town and you must do another math problem

def rightSupreme(userName, kindWords, playful, userInput, newBudget5):

    print()

    print("You somehow made it back into the city!!")

    print()

    time.sleep(4)

    print(choice(playful), "!!")

    print()

    print("As you walk down the road with your awesome wizard smart skills and fashionable accessory.")

    print()

    time.sleep(8)

    print("You passed by your local video game shop and saw a giant poster.")

    print()

    time.sleep(5)

    print("It screams 'LAST COPY OF EARTHBOUND!! THE EARTBOUND GAME THAT INSPIRED SO MANY OTHER KNOCKOFFS!!' ")

    print()

    time.sleep(6)

    print("Below it was a small print stating 'LIKE THIS GAME THAT HAS NO RPG ELEMENT IN IT!!'")

    print()

    time.sleep(6)

    print("Rude, isn't it?")

    print()

    time.sleep(5)

    print("Because we too can be a decent Eartbound knockoff if we had more time and people on this project!!")

    print()

    time.sleep(7)

    print("I bet we can be better and have a bigger better fanbase than Undertale!!")

    print()

    time.sleep(7)

    print("So you went inside to buy a copy of Eartbound.")

    print()

    time.sleep(4)

    print("You are in luck!!")

    print()

    time.sleep(2)

    print("It is the last copy but since it is the last copy.")

    print()

    time.sleep(5)

    print("It cost more.")

    print()

    time.sleep(2)

    print("but luckily you have a 15% off coupon")

    print()

    time.sleep(4)

    print("Will you buy this game? because if you chose yes, then you have to use the coupon")

    print()

    time.sleep(5)

    print("the game cost $85 and it comes nothing but the game itself")

    print()

    time.sleep(5)

    print("But luckily you have a coupon!!")

    print()

    time.sleep(4)

    print("decimal input maybe needed!!")

    print()

    time.sleep(3)

    UserAnswer = float(input("Enter the price!! Guess right it is ours!! : "))

    time.sleep(2)

    rate = 85 * .15

    newPrice = 85 - rate

    if UserAnswer == newPrice:

        print()
        print("CORRECT!! WE HAVE OBTAIN MOTHER 2!!!!!!!!")

        print(choice(playful), "!!")

        time.sleep(2)

        newBudget6 = newBudget5 - newPrice

    else:
        print()
        print("I am sorry but that seems incorrect!!")

        time.sleep(2)

        str(print()) * 3

        print("GAME OVER!! LOSER!!")


    print("You obtain Earthbound and that means!!")

    time.sleep(5)

    print("You get to play it all day!!")

    time.sleep(4)

    print("Have fun!!")

    print()

    time.sleep(2)

    print("Bye!!")

    print()

    print(newBudget6)

    credits(userName, playful, kindWords, userInput)

##no to kitty on helping it where you should feel a shame

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

#the fish smells in your pants and you must go home or not

def noToKitty(userName, kindWords, playful, userInput, newBudget):

    print()

    print("You disappoint me.")

    print()

    time.sleep(4)

    print("You walk away and your pants stinks as well")

    print()

    time.sleep(5)

    print("Want to go home and take a shower?")

    print()

    time.sleep(2)

    goneHome = str(input("Y/N: "))

    goneHome = goneHome.lower()

    time.sleep(2)

    if goneHome == "y":

        yesToHome(userName, kindWords, playful, userInput, newBudget)

    else:

        noToHome(userName, kindWords, playful, userInput, newBudget)

##will you go home or not at all

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

#if user does choose yes they continue the story

def yesToHome(userName, kindWords, playful, userInput, newBudget):

    print()

    print("You went inside some random house and used their shower.")

    print()

    time.sleep(7)

    print("You smell nice and now much more bearable to hang out with.")

    print()

    time.sleep(4)

    print()

    print(choice(playful))

    print()

    time.sleep(2)

    sewerAdventure(userName, kindWords, playful, userInput, newBudget)

##If user does not go home and shower. COMP leaves them

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def noToHome(userName, kindWords, playful, userInput, newBudget):

    print()

    print("EWWWWW!!")

    print()

    time.sleep(6)

    print("I really do not want to hang out with you if you smell so bad")

    print()

    time.sleep(7)

    print("Going to leave you here forever and never come back for you ever again!!")

    print()

    time.sleep(6)

    print("BYE!!")

    print()

    credits(userName, playful, kindWords, userInput)

##User is given a false choice again and they will go to the sewer no matter what

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def sewerAdventure(userName, kindWords, playful, userInput, newBudget):

    print()

    print("Back to our fun adventure now!!")

    print()

    time.sleep(4)

    print("As you walk down the street.")

    print()

    time.sleep(4)

    print("You come across an open manhole!")

    print()

    time.sleep(3)

    print("Will you enter it?")

    time.sleep(2)

    manhole = str(input("Y/N"))

    manhole= manhole.lower()

    time.sleep(2)

    if manhole == "y":

        print()

        print(choice(playful))

        print()


    if manhole == "n":

        print()

        print("Haha like you had a choice!!")

        print()

    print("You enter the swamp infested sewage.")

    print()

    time.sleep(4)

    print("Sadly there is no Teengae Mutant Ninja Turtles down here!")

    print()

    time.sleep(6)

    print("Such a disappointment.")

    print()

    time.sleep(4)

    print("You got to admit this isn't much fun already.")

    print()

    time.sleep(4)

    print("As you walked across the sewers narrow linear path.")

    print()

    time.sleep(5)

    print("You hear a sound.")

    print()

    time.sleep(2)

    print("It is an alligator!")

    print()

    time.sleep(4)

    print("And it is charging right at you!!")

    print()

    time.sleep(5)

    print("You ran and come off to a fork in the road.")

    print()

    time.sleep(4)

    print("What would you do?")

    print()

    time.sleep(2)

    sewerPath = str(input("left/right"))

    time.sleep(2)

    if sewerPath == "left" and "Left":

        playingSafe(userName, kindWords, playful, userInput, newBudget)

    if sewerPath == "right" and "Right":

        rightDanger(userName, kindWords, playful, userInput, newBudget)

##User chooses left the play it safe function is called out and a fun journey happens

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def playingSafe(userName, kindWords, playful, userInput, newBudget):

    print()

    print("There is a ladder up ahead!!")

    print()

    time.sleep(4)

    print("You grab on and climbed up.")

    print()

    time.sleep(4)

    print("You got out of the manhole!!")

    print()

    time.sleep(4)

    print("But the alligator is still chasing you!")

    print()

    time.sleep(4)

    print("You have nowhere to go, despite that you are in an open area.")

    print()

    time.sleep(6)

    print("The alligator comes out of the sewer.")

    print()

    time.sleep(5)

    print("As you were about to be eaten by the alligator.")

    print()

    time.sleep(4)

    print("A naked mole rat appeared and kick the alligator in the face.")

    print()

    time.sleep(5)

    print("As the naked mole rat beat up the alligator.")

    print()

    time.sleep(5)

    print("A cowboy appeared and shot the alligator!")

    print()

    time.sleep(4)

    print("The naked mole rat returns to the cowboy.")

    print()

    time.sleep(5)

    print("He would charge you for saving his life but the alligator was worth more then the fine.")

    print()

    time.sleep(8)

    print("So he gave you $430 and left.")

    print()

    time.sleep(3)

    newBudget2 = newBudget + 430

    print("Okay now guess how much money you have.")

    print()

    time.sleep(3)

    guessBudget = float(input("Answer here darling: $"))

    time.sleep(2)

    if guessBudget == newBudget2:

        print()

        print("You guessed right!!")

        print()

        time.sleep(2)

        print(choice(playful), "!!")

        print()

        time.sleep(2)

        print("Now you have enough to enjoy retirement!!")

        print()

        time.sleep(5)

        print("Have fun and enjoy life!")

        print()

        time.sleep(3)

        print("Bye!")

        print()

        credits(userName, playful, kindWords, userInput)

    else:

        print()

        print("Oh I am so sorry to say but that is WRONG!!")

        print()

        time.sleep(4)

        print("I must now confiscate your money!")

        print()

        time.sleep(4)

        print("Have fun living a life as a homeless person!!")

        print()

        time.sleep(4)

        print("BYEZ!!")

        print()

        print("Money that you had earned through out the game: $  0")

        print()

        time.sleep(5)

        credits(userName, playful, kindWords, userInput)

##if player chooses the right side instead will lead to a waterfall adventure

#@param everything from the main will be brought to this part just in case any future choice needs it

#some choices will eliminate or insert thing to the function that will go over to others

def rightDanger(userName, kindWords, playful, userInput, newBudget):

    print()

    print("You ran right!")

    print()

    time.sleep(4)

    print("You see a sewage waterfall at the end of his sewer tunnel!!")

    print()

    time.sleep(5)

    print("I would give you a choice but jumping is the only option here.")

    print()

    time.sleep(4)

    print("You jump with faith on your back.")

    print()

    time.sleep(4)

    print("You are falling down the rabbit hole.")

    print()

    time.sleep(4)

    print("By the way this sewer waterfall now turned into a rabbit hole to your world.")

    print()

    time.sleep(6)

    print("私は日本語で話すことができます。")

    print()

    time.sleep(5)

    print("あなたは日本語を話すことはできますか？")

    print()

    time.sleep(4)

    Japanese = str(input("Y/N: "))

    Japanese = Japanese.lower()

    time.sleep(2)

    if Japanese == "y":

        print()

        print("すごい!!")

        print()

        time.sleep(3)

        print("私がコンプです。")

        print()

        time.sleep(4)

        print("私は本当に猫が好きです。")

        print()

        time.sleep(8)

        print("."*4)

        print()

        time.sleep(2)

        print("...."*3)

        print()

        time.sleep(4)

        print("..........."*2)

        print()

        time.sleep(3)

        print("That is all the Japanese I know, sadly.")

        print()

        time.sleep(4)

        print("Sadly the fun is over!!")

        print()

        time.sleep(3)

        print("It was fun while it lasted.")

        print()

        time.sleep(3)

    if Japanese == "n":

        print(choice(playful))

        print()

        time.sleep(2)

        print("I do not know a lot of Japanese, to be honest.")

        print()

        time.sleep(4)

        print("Can you imagine the game complexity if it was all in Japanese!")

        print()

        time.sleep(4)

    print("Lets actually have one more game like a mad lib game!!")

    time.sleep(4)

    noun = input("Please give me a noun: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    adjective = input("Enter an adjective: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    food = input("Enter a food: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    adjectiveOne = input("Adjective: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    adjectiveTwo = input("Adjective: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    size = input("Enter a size like tall: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    something = input("Enter something you love: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    favorite = input("Enter favorite parent or guardian or care taker: ")

    print()

    print(choice(playful), "!!")

    print()

    time.sleep(2)

    print("Okay here we go!!")

    print()

    time.sleep(3)

    print("The sun shine like a ", noun, ".")

    print()

    time.sleep(4)

    print("It was", adjective, "to look at.")

    print()

    time.sleep(4)

    print("But not as", food, ".")

    print()

    time.sleep(4)

    print("I miss my mom's cooking sometimes.")

    print()

    time.sleep(4)

    print("But it will be okay.")

    print()

    time.sleep(4)

    print("Because it will be okay.")

    print()

    time.sleep(4)

    print("I just know it!!")

    print()

    time.sleep(4)

    print("Because I am ", adjectiveOne)

    print()

    time.sleep(4)

    print("Life is ", adjectiveTwo)

    print()

    time.sleep(4)

    print("Just know, that no matter how", size, "the challenge is.")

    print()

    time.sleep(4)

    print(something, "will always be there for you.")

    print()

    time.sleep(4)

    print("And your", favorite, "will always be at your side when you fall.")

    print()

    time.sleep(4)

    print("Believe in yourself!")

    time.sleep(5)

    print("You were fun but now I have to let you go!")

    print()

    time.sleep(4)

    print("Because we are close to the end of this rabbit hole.")

    print()

    time.sleep(5)

    print("Have fun in the real world!")

    print()

    time.sleep(3)

    print("Don't ever forget about me!!")

    print()

    credits(userName, playful, kindWords, userInput)


##Credit scene just like the movies and video games!

#@param username to make them feel all warm and fuzzy inside

#@param playful words to spam out of the whole list

def credits(userName, playful, kindWords, userInput):

    time.sleep(2)

    print()

    print("THE CREDITS SCENE!!")

    time.sleep(2)

    print()

    print("COMP: itself")

    print()

    time.sleep(5)

    print(choice(playful))

    print()

    time.sleep(1)

    print("The hero of the story: ", userName)

    print()

    time.sleep(5)

    print("You are the ", choice(kindWords), "!!")

    print()

    time.sleep(1)

    print("Programmer: James McGrath")

    print()

    time.sleep(5)

    print(choice(playful))

    print()

    time.sleep(1)

    print("Programmer: Victor Cano")

    print()

    time.sleep(5)

    print(choice(playful))

    print()

    time.sleep(1)

    print("All license and reserved title is all up to your imagination")

    print()

    time.sleep(9)

    print("Unless you do not want to be ", choice(userInput))

    print()


    print('Do you want to play again? y/n:')
    playAgain = str(input())

    playAgain = playAgain.lower()

    #a while loop to make this game start over if the player wants it to be

    while playAgain == playAgain == 'y':
        main()

    if playAgain == "n":
        exit()


#RUN

main()