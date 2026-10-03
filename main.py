import os
from Components.actions import actions
from Components.wordscroll import wordscroll
from Components.randomfunctions import f
from Components.createRoom import roomFunctions



def main():

  rooms = os.listdir("Rooms")


  dictT = {
    "debug" : actions.debug,
    "help" : actions.help,
    "lookat" : actions.observe,
    #"take" : actions.take,
    "read" : actions.read,
    #"recall" : actions.recall,
    "touch" : actions.touch,
    "exitcode" : actions.exitcode,
    "unlock" : actions.unlock,
    "answer" : actions.answer,
    "create" : roomFunctions.item.ask,
  }

  #----------------------------- user inputs

  f.welcome()

  i = True
  while i == True:
    roomError = False
    room = input(f"\n\nWhat room number do you want to do? (between 1 and {len(rooms)})\n>>> ")
    if room != "create":
      try:
        int(room)
      except:
        print("That isn't a number")
        roomError = True
      if roomError == False:
        if 1 <= int(room) <= len(rooms):
          i = False
          room = int(room)
    #else:
      #roomFunctions.item.ask("1398")


 #----------------------------- open rooms and initiate


  for i in range(room, len(rooms)+1):

    Room = open(os.path.join("Rooms", "room" + str(i) + ".txt"), "r").read().split("//end")

    inventory = ["key4r9i"]

    components = f.readFile(Room)

    wordscroll.scrollIntro(components[0])

    actions.start(components)

    gameloop = True

#-----------------------------gameloop; logic to call functions

    while gameloop == True: #gameloop
      commandTrue = False
      while commandTrue == False: #is input a command?
        command = input("\n>>> ").lower().split()
        if len(command) > 0: # if user enters nothing
          for i in dictT.keys(): # for each command
            if command[0] == str(i): # if user enters a string
              
              if command[0] == "unlock":
                if len(command) == 4:
                  dictT[i](inventory, command[3], command[1])
                  commandTrue = True
                else:
                  print("Please format the command the same way as in help message")

              elif command[0] == "answer":
                if len(command) == 4:
                  dictT[i](command[3], command[1])
                  commandTrue = True
                else:
                  print("Please format the command the same way as in help message")

              # elif command[0] == "take":
              #   if len(command) == 2:
              #     completed, inventory = dictT[i](inventory, command[1])
              #     commandTrue = True
              #   else:
              #     print("Please input better")

              elif len(command) == 2:
                completed = dictT[i](command[1])
                commandTrue = True
                if completed == True:
                  gameloop = False
                  
              else:
                dictT[i]()
                commandTrue = True
        else:
          print("Please enter something")
          commandTrue = True
        if commandTrue == False:
          print("Command cannot be found")

#if __name__ == "__main__":
#  main()


main()



