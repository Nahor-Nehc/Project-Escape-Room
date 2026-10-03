from Components.wordscroll import wordscroll
import os

class f():
    def welcome():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        welcome = open(os.path.join("textfiles", "welcome.txt"), "r").read().split("//end")
        components = f.readFile(welcome)
        wordscroll.scrollIntro(components[0])
    def readFile(file):
        components = []
        for i in range(len(file)):
            part = file[i].split("\n")
            if part != [""]:
                if "" in part:
                    if part[0] ==    "":
                        part.pop(0)
                part.pop(-1)
                components.append(part)
        return components