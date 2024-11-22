# Deathbringer

These programs generate a character for the Deathbringer RPG. Both these programs are commandline, text only programs, there is no fancy Windows GUI, this will not change. This is an offshoot project from a Basic program I wrote in the early 90's for making D&D characters.

 The Deathbringer RPG is availble at;

https://www.drivethrurpg.com/product/396879/Deathbringer-RPG?term=deathbringer

Deathbringer.bas:

I am no longer updating this code, all future updates will be done on deathbringer.py. This code differs from the rules in that it does not use point buy, but rather generates attributes randomly by rolling 4d6 and taking the best three, and using that number to determine the actual attribute ranging from -4 to +4.

Compiling:
This program was writen for Qbasic and can be compiled with QB64 or FreeBasic;

FreeBasic is available at https://www.freebasic.net/. To compile under FreeBasic, use the folowing;

fbc -lang qb deathbringer.bas -x deathbringer 

I am aware this is really bad code. I originally wrote this program back in the early 90's to roll up D&D characters. While I am capable of cleaning it up and making it into a decent program, I choose not to, I like the old school coding because it goes along with the old school feel of the Deathbringer RPG. 

Deathbringer.py:

This program does use the point buy system used in the RPG rules. I wrote this program with Python 3.11.2, it should work fine with any 3.x version, I will probably ignore the problem if it doesn't work on versions of Python other than what I am using. You will need Python to run this program, Python is free and open software, it is availble for download at Python.org. If you are not familar with Python, here is a quick guide on getting it installed in Windows. If you use Linux or Mac OS, it is already installed.

https://www.howtogeek.com/197947/how-to-install-python-on-windows/

If you are completely unfamilar with Python, it is a fairly easy programing language to learn. There are many good tutorials on the internet for learning the basics of Python. Below is an hour long Youtube video that gives you pretty much everything you need to know about Python to understand how this program works so you can start modifing it for you own purposes. One of my goals here was to build a simple enough code base where even someone with no Python experience can add thier own Classes, Backgrounds or Miseries just by looking at the code and doing a bit of copy/paste and modify work. I encourage everyone to copy this program, modify it and make it your own.

https://www.youtube.com/watch?v=kqtD5dpn9C8&t=1882s

Thank you to Dan "Professor Dungeon Master" Masters for creating the Deathbringer RPG, your hard work and creativity is appreciated.

https://www.patreon.com/DungeonCraftYouTube/posts

https://www.youtube.com/@DUNGEONCRAFT1

Legal Statement:
This Deathbringer Character Generator is an independent product and is not affiliated with Dan "Professor Dungeon Master" Masters. Deathbringer RPG © 2023 by Dan "Professor Dungeon Master" Masters.

MIT License:
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
