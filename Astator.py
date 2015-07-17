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
                      'I am thinking but this beats me...', 'Allright allright, I give up', 'Who knows',
                      'Don\'t get me wrong but I don\'t know all the answers',
                      'Hey, why don\'t you ask me another question while I think more about that?',
                      'Believe me I am trying but, I simply could not answer that', 'I think I do not understand you',
                      'Hmmm, I am doing my best,just be patient, OK?']
    exit_messages = ['exit', 'terminate', 'go away', 'bored', 'enough', 'quit']
    positive_answers = ['Yes', 'Of course', 'Definitely']
    negative_answers = ['No', 'Nope', 'I don\'t think so', 'Sorry']
    personal_message_for_astator = ['you', 'yourself']
    personal_message_for_master = ['me', 'myself', 'I']
    rudimentary_question_tags = ['who', 'why', 'when', 'where', 'what', 'which', 'how']

    actions = {'about_astator': 0, 'about_master': 1, 'search_google': 2, 'search_other': 3, 'say_sorry': 4}

    def __init__(self, name="Astator", gender="Female", master="Master"):
        self.name = name
        self.gender = gender
        self.master = master
        self.wake()

    def wake(self):

        welcome = self.hi()
        print '\n\n' + welcome

        message = str(raw_input("\nHow may I help?\n"))

        while True:    # infinite loop

            if message in self.exit_messages:
                rand = randint(0, len(self.bye_messages) - 1)
                print self.bye_messages[rand]
                break  # break
            else:
                answer = self.answer(message)
                print answer

            message = str(raw_input("\n\n"))

    def hi(self):

        rand = randint(0, len(self.welcome_messages) - 1)
        return self.welcome_messages[rand]

    def answer(self, message):

        action = self.understand(message)
        options = self.think(action, message)
        answer = self.explain(options, message)

        return answer

    def understand(self, message):

        if any(m in message for m in self.personal_message_for_astator):    # it is something about the astator
            action = self.actions['about_astator']
        elif any(m in message for m in self.personal_message_for_master):   # it is something about the master
            action = self.actions['about_master']
        elif any(m in message for m in self.rudimentary_question_tags):     # we can rewrite the message as a search query
            action = self.actions['search_google']
        else:
            action = self.actions['say_sorry']
        return action

    def think(self, action, message):

        if action == self.actions['about_astator']:
            options = self.get_options_for_personal_questions('astator', message)
        elif action == self.actions['about_master']:
            options = self.get_options_for_personal_questions('master', message)
        elif action == self.actions['search_google']:
            query = self.rewrite_question('google', message)
            options = self.research(query)
        else:
            rand = randint(0, len(self.sorry_messages) - 1)
            options = [self.sorry_messages[rand]]
            # get results from google
        return options

    def research(self, query):

        options = ['nothing yet...']
        return options

    def explain(self, options, message):

        if len(options) >= 1:
            answer = options[0]
        else:
            rand = randint(0, len(self.sorry_messages) - 1)
            answer = self.sorry_messages[rand]
        return answer

    def get_options_for_personal_questions(self, person, message):

        if person == 'astator':
            options = ['Let\'s not talk about me.']
        elif person == 'master':
            options = ['You know, I can\'t answer that']
        return options

    def rewrite_question(self, source, message):

        query = message # by default, set it to message

        if source == 'google':
            query = str(message).replace('', '')
        return query