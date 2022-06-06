### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #it should have ==
      return True
    else #missing a :
      return False
   

  dif highest_card(self, card1 card2): #there is a typo at dif which has to be def. Also missing a , between card1 and card2
  if card1.value > card2.value: #indentation is missing
    return card #it should be card1
  else:
    return card2
  


def cards_total(self, cards):
  total #total variable is declared without any value. It should have one like total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total #return shouldn't be inside the for loop so retotal needs to be turned into a string for the test to pass
  
```
