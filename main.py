
import vlc
import time
import os
from os import walk
import easygui
from os import listdir
from os.path import isfile, join
import glob





# # Fns ---------------------------------------------------------------------------
# def playAll(dir):
#     # Play all chapters in a book
#     all_files = getAllFiles(dir)
#     for file in all_files:
#         file = join(dir, file)
#         player = vlc.MediaPlayer(file)
#         player.play()

# vlc.MediaPlayer()
# # def playTimer(x):
# # Play with a timer
# os.chdir("bible")
# def getAllFiles(dir):
#     foo = [f for f in listdir(dir) if isfile(join(dir, f))]
#     foo = sorted(foo, key = lambda x: x[:-3]) 
#     return(foo)


# # Put all books of Bible in order
# books = []
# for (dirpath, dirnames, filenames) in walk("."):
#     books.extend(dirnames)
#     break

# books = sorted(books, key = lambda x: x[:2]) 

# # Test getting all files in a dir
# # poo = getAllFiles("01_Genesis")
# # for i in poo:
# #     print(i)

# # Tie it all together
# full_playlist = []
# for book in books:
#     foo = getAllFiles(book)
#     full_playlist.append(foo)


# player = vlc.MediaPlayer("01_Genesis/40006 0_KJV_Bible-Matthew001.mp3")
# player.play()
# player.stop()
# player.get_state()
# def playyer(file):
#     """
#     Main fn to play a file
#     """
#     player = vlc.MediaPlayer(file)
#     # length = player.get_length() + 2
    
#     player.play()
    
#     # time.sleep(length/1000)
#     # player.stop()

# # playAll("02_Exodus")
# # time.sleep(900)

# # playyer("01_Genesis/01003 0_KJV_Bible-Genesis001.mp3")

# # media = easygui.fileopenbox(title="Choose media to open")
# # player = vlc.MediaPlayer(media)
# # # image = "bigles.gif"

while True:

    timerYN = easygui.buttonbox(title = "BiblePi", msg = "Play on timer or free play?", choices = ["Timer", "Freeplay"])
    media = easygui.buttonbox(title= "BiblePi", msg = "Pick a book", choices = [ "Matthew","Mark", "Luke", "John", "Acts",
            "Romans", "1Corin", "2Corin", "Galatians", "Ephesians", "Phil", "Coloss", "1Thess",
            "2Thess", "1Tim", "2Tim", "Titus", "Philemon", "Hebrews", "James", "1Peter", "2Peter",
            "1John", "2John", "3John" "Jude", "Revelation"])
    instance =  vlc.MediaPlayer("bible/" + media)

    while True:
        
        if timerYN == "Timer":
            playlen = easygui.buttonbox(title="BiblePi", msg="Play for how many minutes?", choices = ["5", "10", "20", "60"])
            playlen = int(playlen)
        
        choice = easygui.buttonbox(title="BiblePi",msg=f"Press Play to start\n\nMode = {timerYN}",choices=["Play","Pause","Stop","Start Over"])
        print(choice)
        if choice == "Play":
            instance.play()
        elif choice == "Pause":
            instance.pause()
        elif choice == "Stop":
            instance.stop()
        # elif choice == "Pick Book":
        #     media = easygui.buttonbox(title= "BiblePi", msg = "Pick a book", choices = [ "Matthew","Mark", "Luke", "John", "Acts",
        #     "Romans", "1Corin", "2Corin", "Galatians", "Ephesians", "Phil", "Coloss", "1Thess",
        #     "2Thess", "1Tim", "2Tim", "Titus", "Philemon", "Hebrews", "James", "1Peter", "2Peter",
        #     "1John", "2John", "3John" "Jude", "Revelation"])
        elif choice == "Start Over":
            break
        if timerYN == "Timer":
            time.sleep(playlen)
            instance.stop()
            timerYN = "Freeplay"    
        









# newtest = [ "Matthew","Mark", "Luke", "John", "Acts",
# "Romans", "1Corin", "2Corin", "Galatians", "Ephesians", "Phil.", "Coloss", "1Thess",
# "2Thess", "1Tim", "2Tim", "Titus", "Philemon", "Hebrews", "James", "1Peter", "2Peter",
# "1John", "2John", "3John" "Jude", "Revelation"]

# # Get the position of the choice
# [i for i,x in enumerate(newtest) if x == "John"]
