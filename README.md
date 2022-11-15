# keybOardSC
An OSC (open sound control) keyboard controller

This little script/app receives osc commands on a selected port,
and converts them to keyboard keypresses and keycombo's.

For now only keybOardSC-powerpoint can be compiled with
```
pyinstaller keybOardSC-powerpoint.py -w
```
in to an OSX app but the scripts should work on OSX, Windows and linux.

General osc messages examples:
```
/keycombo "command+space"           # can send key combo's with: shift, control, alt/option , command/winkey/superkey
/keycombo "shift+option+k"
/text "hello there, this is a text string"
```

Powerpoint specific commands:
```
/start                              # open first dia in fullscreen
/start/selected                     # open selected dia in fullscreen
/view                               # open fullscreen presenter view
/presenter                          # open fullscreen presenter view
/slide "5"                          # goes to the slide number, works only in presentation mode. (in this case slide 5)
/next                               # next slide, works only in presentation mode.
```
Vista R3 specific is in the making.


Python3.9 - Dependencies used:
```
Keyboard, 
Pyside6, 
pythonosc,
pyinstaller
```
