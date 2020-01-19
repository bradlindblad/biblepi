import os
from os import walk
import easygui
from os import listdir
from os.path import isfile, join
import glob
import os
from os import listdir
from os import walk
from pydub import AudioSegment


# Put all books of Bible in order
os.chdir("bible")
books = []
for (dirpath, dirnames, filenames) in walk("."):
    books.extend(dirnames)
    break

books = sorted(books, key=lambda x: x[:2])


for book in books:

    # os.chdir(book)
    # Get all mp3 file names
    foo = [f for f in listdir(book) if isfile(join(book, f))]
    foo = sorted(foo, key=lambda x: x[:-3])

    os.chdir(book)
    playlist = AudioSegment.empty()
    for i in foo:
        i = AudioSegment.from_mp3(i)
        playlist += i
    filenamee = "/home/xps/Desktop/" + str(book)
    playlist.export(filenamee, format="mp3")
    print(book)
    os.chdir("..")
