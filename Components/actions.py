from Components.wordscroll import wordscroll

keysinternal = ["help", "lookat", "take", "read", "recall", "touch", "exitcode", "unlock"]

keysinfo = ["help: Gives a list of actions", "help: Tells you more about each action", "lookat: Tells you what you can do with the object", "read: Reads whatever is written on the object", "touch: Touches object, may cause changes", "exitcode: Use the code to exit the room", "unlock: Use this to open locked objects (do not use on the lock itself, use this action on the object that is locked)", "answer: This functions the same way as unlock"]

keys = ["help", "help <action>", "lookat <object>", "read <object>", "touch <object>", "exitcode <code>", "unlock <object> with <code/key>", "answer <object> with <answer>"]

class actions():
  def start(x):
    global components
    components = x

  def debug():
    print(components)


  def help(item = None):
    print("OBJECTS IN ROOMS 1-3 HAVE ALL OBJECTS IN BOLD\n")
    print("Actions:\n")
    if item == None:
      for i in range(0, len(keys)):
        print(keys[i])
        print(keysinfo[i])
        for i in range(0, len(keysinfo[i])):
          print("-", end = "")
        print("-------")
    else:
      actionfound = False
      for i in range(len(keysinternal)):
        if item == keysinternal[i]:
          print(keysinfo[i])
          actionfound = True
      if actionfound == False:
        print("Action cannot be found")
    return False


  def observe(item = None):
    if item == None:
      print("Please specify item wanted to observe")
    else:
      found = False
      for i in range(len(components)):
        if components[i][0] == item:
          print("You can " + components[i][1] + " this object")
          found = True
      if found == False:
        print("This object isn't here...")
      return False


  def take(inventory, item = None):
    if item == None:
      print("Please specify item wanted to take")
    else:
      for i in range(len(components)):
        if components[i][0] == item:
          print(components[i][3])
          if components[i][2] == "True":
            inventory.append(components[i][0])
      return False, inventory


  def read(item = None):
    if item == None:
      print("Please specify item wanted to read")
    else:
      for i in range(len(components)):
        if components[i][0] == item:
          if components[i][4] !=  "False":
            print(components[i][4])
            if components[i][5] != "None":
              print("\n" + components[i][5])
          elif components[i][4] == "False":
            print("\nYou can't read this item")
      return False


  def recall(item = None):
    if item == None:
      print("Please specify what you want to recall")
    else:
      for i in range(len(components)):
        if components[i][0] == item:
          if components[i][6] !=  "False":
            print(components[i][4])
      return False


  def touch(item = None):
    if item == None:
      print("Please specify what you want to touch")
    else:
      for i in range(len(components)):
        if components[i][0] == item:
          if components[i][7] !=  "False":
            print(components[i][7])
      return False


  def exitcode(code = None):
    if code == None:
      print("Please specify code")
    else:
      found = False
      for i in range(len(components)):
        if components[i][1] == code:
          wordscroll.scrollIntro(components[i+1])
          found = True
          return True
      if found == False:
        wordscroll.scrollword("The door light goes red. It stays closed.\nSigh, you have to try again")
        return False


  def unlock(inventory, key, item = None):
    if item == None:
      print("Please specify the code/key")
    else:
      unlockThis = ""
      correct = False
      for i in range(len(components)):
        if components[i][0] == item:
          unlockThis = i
          break
      if unlockThis != "" and len(components[unlockThis]) == 10:
        if components[unlockThis][8] == key:
          print(components[unlockThis][9])
          correct = True




      else:
        print("You can't unlock this item")
        correct = True
      if correct == False:
        print("The code was wrong or the key isn't correct")


  def answer(key, item = None):
    if item == None:
      print("Please specify the code/key")
    else:
      correct = False
      for i in range(len(components)):
        if components[i][0] == item:
          unlockThis = i
          break
      if len(components[unlockThis]) == 10:
        if components[unlockThis][8] == key:
          print(components[unlockThis][9])
          correct = True
      else:
        print("You can't answer this object")
        correct = True
      if correct == False:
        print("The answer was wrong")
