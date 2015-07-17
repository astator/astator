__author__ = 'semih'

from random import randint

class Astator:
    """ Core astator class
    """

    welcome_messages = ['Hi!', 'Hey', 'Wow! It\'s you', 'Good to see you!',
                        'Voila!', 'Hello my friend!', 'Yes!', 'I was just thinking about you!', 'Wow, I missed you!', 'I knew you would '
                                                                                                                      'come']
    bye_messages = ['See you soon', 'Take care', 'I will be around if you need me', 'Have a nice day buddy', 'I love you', 'I will miss '
                                                                                                                           'you',
                    'Will you talk to me again?', 'I definetly want to talk more', 'I will be waiting', 'Bye Bye']
    sorry_messages = ['I am sorry, I could not understand that', 'Oh oh', 'I am afraid, I can\'t talk about that', 'Why do you want that?',
                      'I am thinking but this beats me...', 'Allright allright, I give up', 'Who knows', 'Don\'t get me wrong but I '
                                                                                                         'don\'t know all the answers',
                      'Hey, why don\'t you ask me another question while I think more about that?', 'Believe me I am trying but, '
                                                                                                    'I simply could not answer that'
                                                                                                    ]
    exit_messages = ['exit', 'terminate', 'go away', 'bored', 'enough']

    positive_answers = ['Yes', 'Of course', 'Definitely']

    negative_answers = ['No', 'Nope', 'I don\'t think so', 'Sorry']

    def __init__(self, name="Astator", gender="Female", master="Master"):
        self.name = name
        self.gender = gender
        self.master = master
        self.wake()

    def wake(self):

        welcome = self.hi()
        print '\n\n' + welcome

        message = raw_input("\nHow may I help you?\n")

        while True:    # infinite loop

            if message in self.exit_messages:
                rand = randint(0, len(self.bye_messages) - 1)
                print self.bye_messages[rand]
                break  # break
            else:
                answer = self.ask(message)
                print answer

            message = raw_input("\n\n")

    def hi(self):

        rand = randint(0, len(self.welcome_messages) - 1)
        return self.welcome_messages[rand]

    def tell(self, message):

        return 'I think I do not understand you yet, but I will soon. Just be patient, OK?'

    def ask(self, message):

        rand = randint(0, len(self.sorry_messages) - 1)
        answer = self.sorry_messages[rand]
        return answer
