
# coding: utf-8

# # <span style="color:teal;">CIS 211 Project 3:  Deck Class</span>

# ##### Due 11:00 P.M. Tuesday April 21

# ##### Reading:  Perkovic Sec 6.4--6.5 and 8.1--8.5

# ### <span style="color:teal">Setup</span>

# The project for this week looks at how to write classes that extend Python's builtin classes.  You will write the definition of a class named Deck that is a list of Card objects.
# 
# As you work on the project you will need to make Card objects, which means you have to execute an `import` statement that defines the Card class so it can be used by the code in this notebook.
# 
# There are two ways to create the file that contains the Card class:
# * run the notebook converter to export the code from the notebook you wrote for last week's class, and copy the exported Python code to the directory for this notebook
# * download a file named `Card.pyc` from Canvas and save the file in the same directory as this notebook
# 
# The `Card.pyc` file will work on any operating system, but it assumes you have Python 3.4.
# 
# After you have copied your Card class to the folder for this project execute this code cell:

# In[133]:

from Card import *
import random


# If the class is imported properly this expression should print a Card object:

# In[3]:

Card(0)


# ###  <span style="color:teal">1. &nbsp; Deck Class</span>

# Write the definition of a new class named Deck, where each instance of the class will be a list of 52 Card objects. When the constructor is called it should return a list of all 52 cards in order from 2♣ up through A♠.
# 
# ** Your class should be derived from Python's `list` class**.  See the lecture notes on the difference between "is-a" and "has-a".  Don't define a class that *has a list* as an attribute, define a class that *is a kind of list*.
# 
# Define three methods for your class:
# * `shuffle()` should rearrange the cards into a new random permutation (you can use a function named `shuffle` defined in Python's `random` library; see p. 197 in the textbook for an example).
# * `deal(n)` should remove the first `n` cards from the deck and return them in a list
# * `restore(a)` should add the cards in list `a` to the end of the deck
# 
# Here are some examples:
# <pre>
# >>> d = Deck()
# >>> len(d) 
# 52
# 
# >>> d
# [2♣, 3♣, 4♣, ... Q♠, K♠, A♠]
# 
# >>> d.shuffle()
# >>> d
# [Q♣, A♦, 7♦, 9♦, 8♦, 3♠, 8♠, ... 5♣, 9♣, K♦]
# 
# >>> h = d.deal(5) 
# >>> h
# [Q♣, A♦, 7♦, 9♦, 8♦]
# 
# >>> d
# [3♠, 8♠, ... 5♣, 9♣, K♦]
# 
# >>> len(d) 
# 47
# 
# >>> d.restore(h)
# >>> d
# [3♠, 8♠, ... 9♣, K♦, Q♣, A♦, 7♦, 9♦, 8♦]
# 
# >>> len(d)
# 52
# 
# >>> d.sort()
# >>> d
# [2♣, 3♣, 4♣, ... Q♠, K♠, A♠]
# </pre>

# <span style="color:blue">Note:</span> &nbsp; Make sure you understand why the last expression above worked. Why are you able to sort a deck of cards even though you did not define a sort method in your class?

# ##### <span style="color:red">Documentation:</span>

# === Describe your class in this markdown cell ===
# >>  '''
#     Card Class.  Inherits from Card class and List
#     Functions:
#     init
#     repr
#     shuffle
#     deal
#     restore
#     Is a list of 52 Card objects
#     '''

# ##### <span style="color:red">Code:</span>

# In[1]:

# Put your class definition in this code cell


class Deck(list):
    '''
    Card Class.  Inherits from Card class and List
    Functions:
    init
    repr
    shuffle
    deal
    restore
    Is a list of 52 card objects
    '''
    
    
    def __init__(self):
        '''
        Initialize a list of Card objects
        
        '''
        list.__init__(self)
        for i in range(52):
            self.append(Card(i))

    def __repr__(self):
        '''
        output array of card objects
        
        '''
        mylist=[]
        for i in self:
            if not isinstance(i, Card):
                raise Exception("{} {}. Index postition: {}--Please remove from card deck".format("invalid card: ",i,self.index(i)))
                self.remove(i)
            mylist.append(i)
        return str(mylist)
    def shuffle(self):
        '''
        
        Shuffles card list
        
        '''
        random.shuffle(self)
    def deal(self,num):
        '''
        Removes first n cards based on argument
        
        
        '''
        dealt_Hand=[]
        for i in range(num):
            dealt_Hand.append(self[i])
            self.remove(self[i])
        return dealt_Hand
    def restore(self,hand):
        '''
        Returns hand to end of Card deck list
        '''
        
        for card in hand:
            self.append(card)


# ##### <span style="color:red">Tests:</span>

# In[281]:

# Write Python code that tests your Deck class here (add more cells as needed)
d=Deck()
d.insert(0,"454htn")
d.deal


# In[ ]:




# ###  <span style="color:teal">2. &nbsp; PinochleDeck Class</span>

# Define a new class named PinochleDeck that has Deck as its base class. The game of Pinochle (pronounced "pea knuckle") uses only 9s and above, and there are two copies of each card. That means a Pinochle deck has 48 cards in all.  A new instance of your PinochleDeck class should be a sorted list of the 48 cards used in Pinochle. 
# 
# <pre>
# >>> d = PinochleDeck()
# >>> d
# [9♣, 9♣, 10♣, 10♣, ... Q♠, Q♠, K♠, K♠, A♠, A♠]
# 
# >>> d.shuffle()
# >>> h = d.deal(12)
# 
# >>> h.sort()
# >>> h
# [A♣, 9♦, 10♦, J♦, J♦, 9♥, A♥, A♥, 9♠, 10♠, K♠, A♠]
# </pre>

# The last example above uses the default sort order for Card objects, so the hand is sorted by suit, with clubs first, then diamonds, then hearts, and finally spades.

# ##### <span style="color:red">Documentation:</span>

# === Describe your class in this markdown cell ===
# >'''
#     PinochleDeck class.  Inherits from Deck Class and list
#     Is a list of 48 card objects rank 9-A each card appears twice
#     '''

# In[ ]:




# ##### <span style="color:red">Code:</span>

# In[240]:

# Put your class definition in this code cell
class PinochleDeck(Deck,list):
    '''
    PinochleDeck class.  Inherits from Deck Class and list
    Is a list of 48 card objects rank 9-A each card appears twice
    '''
    def __init__(self):
        '''
        Creates a deck of 48 cardo 9-A each card appears twice
        
        '''
        list.__init__(self)
        deck=[ Card(i) for i in range(52) ]
        for i in deck:
            if i._num[3]>= 7:
                self.append(i)
                self.append(i)


# ##### <span style="color:red">Tests:</span>

# In[243]:

# Write Python code that tests your PinochleDeck class here (add more cells as needed)x
d=PinochleDeck()
d


# ### <span style="color:teal">Extra Credit Ideas</span>

# If you want to earn extra credit points for this project try one of the extensions listed below (or feel free to invent other ways to extend the project).
# 
# <span style="color:red; font-weight:bold;">Important:</span>  To earn extra credit points make sure you fill in the following markup cell to explain what you did so the graders will look for your extensions when they grade your project:

# === Describe any extra credit here ===
#     > Created Exception error for repr method, raises error if object in array is not of type Card.
#     Output message :Invalid card: i index position n --Please remove from deck

# #####  Check for Invalid Methods

# Since the Deck class is a subclass of Python’s list class users can do anything to a Deck that they can do to a list, including some things they shouldn’t. For example, it’s easy to attach a string to the end of a deck of cards:
# <pre>
# >>> d
# [2♣, 3♣, 4♣, ... Q♠, K♠, A♠]
# 
# >>> d.append('howdy')
# >>> len(d)
# 53
# 
# >>> d.shuffle()
# >>> d
# [5♣, 'howdy', 2♣, J♠, ... 8♥, J♣, Q♦]
# </pre>
# 
# A function like `total` that expects a list of Card objects isn’t going to like that.
# Figure out what sorts of things you don’t want to happen with decks of cards and add code to your class definition that raises an error message when the method is invoked.

# ##### Check for Valid Cards

# Have the `restore` method check to make sure items being put back in the deck are Card objects.  Don't forget that BlackjackCard objects are a valid type of Card.

# ##### Permutation

# Write your own version of a function that makes a random permutation of a list and use it instead of random.shuffle (send e-mail to `conery@uoregon.edu` if you want some pointers to algorithms that make random permutations).

# ##### Deal Multiple Hands

# Add a second argument to the `deal` method that specifies the number of hands to deal.  If the argument is not passed deal one hand.  If it is a number return a list of that many hands.  For example, `deal(5)` will return a list of 5 cards, as usual, but `deal(5,2)` will return 2 hands with 5 cards each.
