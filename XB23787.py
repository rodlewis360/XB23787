QuestionAndResponse = {'What is your name?' : 'XB23787', 'Do you like humans?' : ['No.']}
def XB23787(QuestionAndResponse):
   def most_common(lst):
       from collections import Counter
       data = Counter(lst)
       return max(lst, key=data.get)
   questionkeys = ['Do you like humans?']
   import random
   from time import sleep
   player = ''
   print("I am a chatbot, programmed to do your work.")
   sleep(1)
   print("Please use correct capitalization, punctuation, and grammar.")
   sleep(1)
   print("Type in q to quit.")
   sleep(1)
   print("Try asking me my name or personal traits!")
   sleep(1)
   print("I will automatically update myself as you go.")
   print("Now type in your question!")
   while player != 'q':
       player = input()
       if not player in QuestionAndResponse:
           print("Adding question to database...")
           QuestionAndResponse[player] = []
           questionkeys.append(player)
       else:
           print(most_common(QuestionAndResponse.get(player)))
       question = random.choice(questionkeys)
       print(question)
       player = input()
       print("Loging response into database...")
       a = QuestionAndResponse.get(question)
       a.append(player)
       QuestionAndResponse[question] = a
       print("I'm ready!")
       
       
       
