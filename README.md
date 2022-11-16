# keybOardSC
![kOSC_wit](https://user-images.githubusercontent.com/65037030/202287227-b4f08bf8-f9af-4fae-8874-c086fe87a868.png)

An OSC (open sound control) keyboard controller

This little script/app receives osc commands on a selected port,
and converts them to keyboard keypresses and keycombo's.

For now only keybOardSC-powerpoint is compiled with
```
pyinstaller keybOardSC-powerpoint.py --icon=img/kOSC_wit.png --add-data=img/kOSC.png:. --add-data=img/kOSC_wit.png:.  -w
```
In to an OSX app but the scripts should work on OSX, Windows and linux. 
You can find the app here:
https://drive.google.com/drive/folders/1rWGJPP05VfSm9tgMf3DJFovzWrA7SOMl?usp=sharing

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
