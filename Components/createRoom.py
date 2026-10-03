import tkinter as tk
import os

Password = "123"
Pword = "321"

fields = 'What room number adding?', 'Item name', 'Can do:', 'Can Take?', 'Message when taken', 'What you read (or False)', 'Reaction to message (or None)', 'Can recall?', 'What felt when touched', 'code to unlock', 'Message when unlocked'

rooms = os.listdir("Rooms in progress")
    

class roomFunctions():
  class item():
    def fetch(entries):
      for entry in entries:
        if entry == entries[0]:
          Room = open(os.path.join("Rooms in progress", "room" + str(entry[1].get()) + ".txt"), "a")
        else:
          if entry[1].get() != "":
            Room.write("\n")
            Room.write(entry[1].get())
            field = entry[0]
            text  = entry[1].get()
            print('%s: "%s"' % (field, text))
          else:
            field = entry[0]
            if entry[1].get() == entries[-3] or (field == fields[9] and field == fields[10]):
              break
            else:
              Room.write("\nPLACEHOLDER")
      Room.write("\n//end")
      Room.close()
    
    def fetchpasswords(entries):
      if entries[0][1].get() == Pword and entries[1][1].get() == "":
        return True
      else:
        return False


    def makeform(root, fields):
      entries = []
      for field in fields:
          row = tk.Frame(root)
          lab = tk.Label(row, width=len(fields[0]), text=field, anchor='w')
          ent = tk.Entry(row)
          row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
          lab.pack(side=tk.LEFT)
          ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
          entries.append((field, ent))
      return entries

    def main():
      root = tk.Tk()
      ents = roomFunctions.item.makeform(root, fields)
      root.bind('<Return>', (lambda event, e=ents: roomFunctions.items.fetch(e)))   
      b1 = tk.Button(root, text='Save',
                    command=(lambda e=ents: roomFunctions.item.fetch(e)))
      b1.pack(side=tk.LEFT, padx=5, pady=5)
      b2 = tk.Button(root, text='Quit', command=root.quit)
      b2.pack(side=tk.LEFT, padx=5, pady=5)
      root.mainloop()


    def ask(password = None):
      if password == Password:
        roomFunctions.item.main()
        return False
      else:
        print("Command cannot be found")