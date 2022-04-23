# SynText README
<h2>SynText Information</h2>
- SynText is a simple python mod for https://replit.com ONLY as it uses extensions not in python but only on https://replit.com
- https://replit.com/@DotAccount/SynText-Engine-demo is the demo link if you need it
- simple use just get the file in your repl and in **main.py** or somewhere else do

```py
import synText as text # replace synText with your file name
```
*its that simple*

<h2>SynText Syntax</h2>
<h3>Text Manipulation</h3>

- shakeText(text, length, delay, amount) shows 
text that shakes rapidly (clears everything on screen)
- jumpText(text,length,delay,amount) basically the same as shake text but vertical instead of horizontal
- coloredText(text,r,g,b) creates a new coloredText object (like a string but colored)
- playFrames(array) uses arrays like so

```py
  [
    ["Text", nextFrameDelay],
    ["New Text", nextFrameDelay],
  ]
```

<h3>Interactiveness</h3>

- keyDown(keyString) pretty simple "a" is the a key, "d"  is the d key, you get it

<h3>File Manipulation</h3>

- fileData(fileString) pretty simple, just reads file data (txt, json, whatever really)
- strToJson(string) pretty simple as well, turns a string into a json (may be broken for some reason though so)
- overwriteFile(fileString,data) simply rewrites a file you made
