
<p align='center'>
<img src="https://github.com/bradlindblad/biblepi/blob/master/static/biblepi.png?raw=true" alt="BiblePi" ></a>
</p>


# A Python Program for Playing the New Testament on a Raspberry Pi

<p align='center'>
<a href="https://github.com/bradlindblad/biblepi"><img src="https://pyup.io/repos/github/bradlindblad/biblepi/shield.svg" alt="PyUp" height="18"></a> <a href="https://github.com/bradlindblad/biblepi"><img src="https://pyup.io/repos/github/bradlindblad/biblepi/python-3-shield.svg" alt="PyUp" height="18"></a> 
</p>


## What is it
A simple python program to read a random book from the New Testament to you and your family. The program is based on the [easygui](https://github.com/robertlugg/easygui) package by Robert Lugg and the popular VLC package. You have the option of setting a timer to read for a given interval (great to put you or your kids to sleep), or to freeplay until you pause or stop the player. 

## Installation
```
git clone https://github.com/bradlindblad/biblepi
```

Then install requirements

```
pip install -r requirements.txt
```

## Hardware
The idea is to have a small computer to simply read the bible to you whenever you want. I installed Ubuntu Mate 18.04 personally onto a Raspberry Pi3. I found it very difficult to get audio output working with the Raspbian Buster image, which is why I would recommend Ubuntu Mate.

I attached a 5" touchscreen to the Pi for a simply interface to the program, which works flawlessly.

## Usage
Making sure you are in the root of the directory, run:

```
python3 main.py
```

If you're on Windows, run

```
python main.py
```