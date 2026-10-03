import time
class wordscroll():
    def scrollIntro(arr):
        speed = 0.15
        factor = 0.75 / speed
        speed2 = factor * speed
        for i in range(1, len(arr)):
            print(arr[i])
            var = len(arr[i].split())
            if var >= 3:
                time.sleep(var * speed)    #0.2
            else:
                time.sleep(var * speed2)    #0.75
    def scrollword(string):
        arr = string.split("\n")
        wordscroll.scrollIntro(arr)
