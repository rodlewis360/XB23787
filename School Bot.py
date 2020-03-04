QuestionAndResponse = {'What is your name?' : 'XB23787', 'Do you like humans?' : ['No.']}
def XB23787(QuestionAndResponse):
   def most_common(lst):
       from collections import Counter
       data = Counter(lst)
       if lst != []:
           return max(lst, key=data.get)
       if lst == []:
           return 'I do not know.'
   questionkeys = ['Do you like humans?']
   import random
   from time import sleep
   text = ''
   print("I am a chatbot, programmed to do your work.")
   sleep(1)
   print("Please use correct capitalization, punctuation, and grammar.")
   sleep(1)
   print("Type in q to quit.")
   sleep(1)
   print("Try asking me my name or things about computer parts!")
   sleep(1)
   print("I will automatically update myself as you go.")
   print("Now type in your question!")
   while text != 'q':
       text = input()
       if not text in QuestionAndResponse:
           print("Adding question to database...")
           QuestionAndResponse[text] = []
           questionkeys.append(text)
           question = text
           print(question)
           text = input()
           print("Loging response into database...")
           a = QuestionAndResponse.get(question)
           a.append(text)
           QuestionAndResponse[question] = a
           print("I'm ready!")
       else:
           print(most_common(QuestionAndResponse.get(text)))
       question = random.choice(questionkeys)
       print(question)
       text = input()
       print("Loging response into database...")
       a = QuestionAndResponse.get(question)
       a.append(text)
       QuestionAndResponse[question] = a
       print("I'm ready!")
