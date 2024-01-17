MAXYPH is a competitive turn-based moba war simulator game set in the late 1700s but with futuristic weapons and also AI generated realism/surrealism.

Not it isn't!  It's a goddamned puzzle game!

![image](https://github.com/Nhawdge/maxyph/assets/32605887/be723b2a-55e7-44d7-90cb-5dea5972bff3)

# [Play Here](https://maxyph.com)

**The Rules/Ethos of The Game**
- six words enter, one score leaves
- - your score is based on the number of unique characters used in your six words.  Max score is a theoretical 25 as the top row can have 5 unique characters, but each of the following 5 rows can only have a maximum of 4 due to 'orange box' inheritance.
- words must be valid, English 5 letter words
- the starting instance of the game will have the 'orange box' value populated for the first row, and the empty orange boxes in the other rows.
- when you enter a valid word in the topmost clear row, the row below has its 'orange box' populated by the value directly above it.
- 'orange box' values from previous rows may not be used again in the puzzle.
- you may 'surrender' at any time and take your current score if you get stuck.



**Prototype folder**:
- the maxyph_proto_gen.py will generate 100 initial puzzle states that are "valid" in a puzzles.json file.
- validity is determined by if the first row can be solved with at least 5 valid words from the word bank.
- the prototype also has a brute force alphabetical order solver
- the prototype can also score the results
- next intent is to append this to the json puzzle input states so that we can provide a players score vs a 'bot' score.



[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/X8X4TGANN)

