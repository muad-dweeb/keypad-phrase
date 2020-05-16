# keypad-phrase
Produce a memorable word that corresponds to a given numeric security code.

## Usage

`python word_selector.py --code 222377`

**Result:** 
```
['abbess', 'access']
```

`python word_selector.py --code 46281227`

User maybe selects "access" as their code word.

**Result:** 
```
Disregarding unmappable digit '1' at index 4
['gnat', 'goat']
['bap', 'bar', 'bas', 'cap', 'car']
```

User maybe selects "goat-1-car" as their code word.
