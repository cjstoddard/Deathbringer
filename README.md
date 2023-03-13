# Deathbringer

This program randomly generates a character for the Deathbringer RPG, the full RPG is availble at;

https://www.drivethrurpg.com/product/396879/Deathbringer-RPG?term=deathbringer

This program differes from the rules in that it generates attributes randomly rather than using a point buy system. Later revisions will contain the point buy system as an option.

Compiling:
This program was writen for Qbasic and can be compiled with QB64 or FreeBasic;

FreeBasic is available at https://www.freebasic.net/. To compile under FreeBasic, use the folowing;

fbc deathbringer.bas -lang qb

QB64 is availble from https://qb64.com/. If you are using QB64, the first line of the program must be changed from Randomize (Timer, 3) to Randomize Timer. To compile under QB64, use the folowing;

qb64 -c deathbringer.bas

