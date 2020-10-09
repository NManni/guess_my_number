import random

MIN = 0
MAX = 1000

class guessmachine():

    def __init__(self):
        self.number_to_guess = rando.randint(MIN,MAX)
        self.number_of_attempt = 0

    def guess(self, num):
        self.number_of_attempt+=1
        if num < self.number_to_guess:
            return 'too low'
        elif num > self.number_to_guess:
            return 'too high'
        else :
            return 'found'


if __name__ == '__main__':
    guess_nachine = guessmachine()
    print('Hey! try to guess a number between %d and %d'%(MIN,MAX))

    while True :
        user_input = input('your guess?')
        try :
            user_attempt = int(user_input)
            result = guess_nachine.guess(user_attempt)
            if result == 'found':
                print('fantastic, you could find the number '
                'I had in mind %d attempts'% guess_nachine.number_of_attempt)
                break
            else:
                print(result)
        except ValueError:
            print ('you joker... that was not an integer')
