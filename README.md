# Deathbringer

This program randomly generates a character for the Deathbringer RPG, the full RPG is availble at;

https://www.drivethrurpg.com/product/396879/Deathbringer-RPG?term=deathbringer

This program differs from the rules in that it does not use point buy, but rather generates attributes randomly by rolling 4d6 and taking the best three, and using that number to determine the actual attribute ranging from -4 to +4. I may add the point buy system as an option later.

Compiling:
This program was writen for Qbasic and can be compiled with QB64 or FreeBasic;

FreeBasic is available at https://www.freebasic.net/. To compile under FreeBasic, use the folowing;

fbc -lang qb deathbringer.bas -x binaries/deathbringer 

QB64 is availble from https://qb64.com/. If you are using QB64 or have downloaded Qbasic from the internet, the first line of the program must be changed from Randomize (Timer, 3) to Randomize Timer. To compile under QB64, use the folowing;

qb64 -c deathbringer.bas

Notes:

I am aware this is really bad code. I originally wrote this program back in the early 90's to roll up D&D characters. While I am capable of cleaning it up and making it into a decent program, I choose not to, I like the old school coding because it goes along with the old school feel of the Deathbringer RPG.

At some point I will add pre compiled Windows and Linux binaries for those who do not want to go to the trouble of downloading and installing QB64 or FreeBasic. Sorry OS X users, I do not own a Mac, you are on your own.

Thank you to Professor Dungeon Master for creating the Deathbringer RPG, your hard work and creativity is appreciated.

https://www.patreon.com/DungeonCraftYouTube/posts

https://www.youtube.com/@DUNGEONCRAFT1

Disclaimer: This software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a paticular purpose and nonifringment. In no event shall the author or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
