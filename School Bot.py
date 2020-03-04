QuestionAndResponse = {'What is your name?' : 'XB23787', 
                       'Do you like humans?' : ['No.'],
                       'What is a hard drive?' : ['A hard drive is the main storage device on your computer.'],
                       'How does a hard drive work?' : ['There is a disc reader that reads the indents on the disc and then tells the computer the info.'],
                       'What is software?' : ['Software is everything stored on the hardware.'],
                       'How does software work?' : ['Software like me works because of code that is stored on the hard drive.  Going further, little switches do calculations in binary format to give the result.'],
                       'What is hardware?' : ['Hardware is anything that you can touch.'],
                       'How does hardware work?' : ['Hardware is a whole lot of things; you cant limit it to one.'],
                       'What is wireless?' : ['Wireless is anything that communicates without wires.  Wifi and Bluetooth are examples.'],
                       'How does wireless work?' : ['Wireless normally works by sending radio waves or waves outside of the visible electromagnetic spectrum.'],
                       'What is a smart phone?' : ['A smart phone is a phone capable of things besides calling and texing.'],
                       'How does a smartphone work?' : ['A smartphone is actually a mini computer, with most of the components of one, just minimized.'],
                       'What is RAM?' : ['RAM stands for Random Access Memory.  It holds recent actions, files, and other things.'],
                       'How does RAM work?' : ['RAM is actually a bunch of SD cards combined by a cicuit board.  SD cards are storage devices in your smartphone.'],
                       'What is a CPU?' : ['CPU stands for Central Processing Unit.  A CPU is the thing that processes everything on your computer.'],
                       'How does a CPU work?' : ['A CPU works by doing calculations with little microchips inside of it.  Each pin or connection is one switch.'],
                       'What is a GPU?' : ['GPU stands for Graphics Processing Unit.  Anything that appears on the screen goes through this first.'],
                       'How does a GPU work?' : ['A GPU is almost a mini computer, with its own circuit board and fans.'],
                       'What is a motherboard?' : ['A motherboard is the thing that holds all the parts together.'],
                       'How does a motherboard work?' : ['A motherboard is basically a circuit board.  It connects all the parts with circuits.'],
                       'What is a router?' : ['A router is a piece of hardware that routes data around the Internet and gets you to the Internet.'],
                       'How does a router work?' : ['A router works by taking signals, turning them into data, and then spitting them out to your computer and the rest of the Internet.'],
                       'What is the Internet?' : ['The internet is a wireless community in which multiple servers are running code and projecting it into the rest of the world.'],
                       'How does the Internet work?' : ['Internet gets to you through routers. Routers take Internet info and send it along.  They also help to find sites (or domains).  Servers are other computers that are always running the code for a site.  They are what keep the Internet out there, making it real.  The Internet is just a bunch of computers communicating with each other.'],
                       'What is the Cloud?' : ['The Cloud is the Internet.']}
def XB23787(QuestionAndResponse):
  for a in range(0, 20):
      print()
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
      else:
          print(most_common(QuestionAndResponse.get(text)))
