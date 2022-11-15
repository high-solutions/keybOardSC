# keybOardSC
An OSC (open sound control) keyboard controller

This little script/app receives osc commands on a selected port,
and converts them to keyboard keypresses and keycombo's.

For now only keybOardSC-powerpoint is compiled in to an osX app but the scripts should work on osX, Windows and linux.

General osc messages examples:
/keycombo "command+space"
/keycombo "shift+option+k"
/text "hello there, this is a text string"

Powerpoint specific commands:
/start #open first dia in fullscreen
/start/selected #open selected dia in fullscreen
/view #open fullscreen presenter view
/presenter #open fullscreen presenter view
/slide "5" #goes to the slide number, works only in presentation mode.
/next #next slide, works only in presentation mode.

Vista R3 specific is in the making.


Python3.9
Dependencies used:
Keyboard
Pyside6
