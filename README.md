# keypad-phrase
Produce a memorable word that corresponds to a given numeric security code.

---

### Example A

`python word_selector.py --code 222377`

**Result:** 
```
['abbess', 'access']
```

---

### Example B

`python word_selector.py --code 46281227`

User maybe selects "access" as their code word.

**Result:** 
```
Disregarding unmappable digit '1' at index 4
['gnat', 'goat']
['bap', 'bar', 'bas', 'cap', 'car']
```

User maybe selects "goat-1-car" as their code word.

---

# Warning

Probability of finding matching words is entirely-dependent upon the length of your input word list, which is `/usr/share/dict/words` by default (standard Unix file). You are not guaranteed a match.

# Generate Input Data

If the standard Unix word file is not long enough, use http://app.aspell.net/create to configure and produce one to your liking.
