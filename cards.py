
# coding: utf-8

# # <span style="color:teal;">CIS 211 Project 2:  Card Class</span>

# ##### Due 11:00 P.M. Tuesday April 14

# ##### Reading:  Perkovic Sec 6.4--6.5 and 8.1--8.2

# The next project this term explores *inheritance*, one of the fundamental concepts of object-oriented programming.

# ###  <span style="color:teal">1. &nbsp; Card Class</span>

# Write the definition of a new class named Card, where each instance of the class will be a single playing card.
# 
# The constructor should take an integer id between 0 and 51 to specify which card to make. Cards 0 to 12 are clubs, 13 to 25 diamonds, 26 to 38 hearts, and 39 to 51 spades, as shown in this table:
# <table>
#   <tr>
#     <th width="50"> &nbsp; </th>
#     <th width="35">2</th>
#     <th width="35">3</th>
#     <th width="35">4</th>
#     <th width="35">5</th>
#     <th width="35">6</th>
#     <th width="35">7</th>
#     <th width="35">8</th>
#     <th width="35">9</th>
#     <th width="35">10</th>
#     <th width="35">J</th>
#     <th width="35">Q</th>
#     <th width="35">K</th>
#     <th width="35">A</th>
#   </tr>
#   <tr>
#     <th> ♣ </th>
#     <td>0</td>
#     <td>1</td>
#     <td>2</td>
#     <td>3</td>
#     <td>4</td>
#     <td>5</td>
#     <td>6</td>
#     <td>7</td>
#     <td>8</td>
#     <td>9</td>
#     <td>10</td>
#     <td>11</td>
#     <td>12</td>
#   </tr>
#   <tr>
#     <th> ♦ </th>
#     <td>13</td>
#     <td>14</td>
#     <td>15</td>
#     <td>16</td>
#     <td>17</td>
#     <td>18</td>
#     <td>19</td>
#     <td>20</td>
#     <td>21</td>
#     <td>22</td>
#     <td>23</td>
#     <td>24</td>
#     <td>25</td>
#   </tr>
#   <tr>
#     <th> ♥ </th>
#     <td>26</td>
#     <td>27</td>
#     <td>28</td>
#     <td>29</td>
#     <td>30</td>
#     <td>31</td>
#     <td>32</td>
#     <td>33</td>
#     <td>34</td>
#     <td>35</td>
#     <td>36</td>
#     <td>37</td>
#     <td>38</td>
#   </tr>
#   <tr>
#     <th> ♠ </th>
#     <td>39</td>
#     <td>40</td>
#     <td>41</td>
#     <td>42</td>
#     <td>43</td>
#     <td>44</td>
#     <td>45</td>
#     <td>46</td>
#     <td>47</td>
#     <td>48</td>
#     <td>49</td>
#     <td>50</td>
#     <td>51</td>
#   </tr>
# </table>

# The class should have three methods in addition to the constructor:
# * `rank()` should return a number between 0 and 12, where a 2 has rank 0 and an ace has rank 12
# * `suit()` should return the suit number, with clubs = 0, diamonds = 1, hearts = 2, and spades = 3
# * `points()` should return 4 if the card is an ace, 3 if it’s a king, 2 if it’s a queen, 1 if it’s a jack, and 0 otherwise
# 
# You also need to define two special methods:
# * the `__repr__` method should return a string based on the card's rank and suit
# * the `__lt__` operator should compare cards according to their ids.

# The string returned by `__lt__` should start with the card's name, as shown in the column labels in the table above.  For example, if the rank is 0 (first column) the card's name is `'2'`, and if the rank is 10 the card name is `Q`.  All the names are one-letter strings except for rank 8, which has the name `10`.
# 
# Following the name of the card there should be a one-letter suit symbol.  Since we're using IPython you can simply copy and paste the symbols from the table above when your write your code that adds suit symbols, or you can use the following Unicode escapes:
# <pre>
# ♣ = \u2663    ♦ = \u2666    ♥ = \u2665    ♠ = \u2660
# </pre>

# Here are some examples from an interactive Python session that show how to make and use a Card object:
# <pre>
# >>> x = Card(35)
# >>> x
# J♥
# 
# >>> x.suit()
# 2
# 
# >>> x.rank()
# 9
# 
# >>> x.points()
# 1
# </pre>

# <span style="color:blue">Style Points:</span> &nbsp; When you write the `rank` and `suit` methods don't forget we have an aversion to long chains of `if-elif` statements.

# ##### <span style="color:red">Documentation:</span>

# === Describe your class in this markdown cell ===
#     >>>Card Class
#     >>>init:self, num)
#     >>>Functions: 
#     >>>repr
#     >>>suit
#     >>>rank
#     >>>__lt__
#     >>points

# ##### <span style="color:red">Code:</span>

# In[8]:

# Put your class definition in this code cell
class Card:
    '''
    Card Class
    init:self, num)
    Functions: 
    repr
    suit
    rank
    __lt__
    points
    
    
    
    '''
    # dict tuple guide:0=rank 1=suit in num (clubs = 0, diamonds = 1, hearts = 2, and spades = 3), 2=suit unicode, 3=rank in num value
    test={2:0}
    rank_dict={0:(2,0,'\u2663',0),1:(3,0,'\u2663',1),2:(4,0,'\u2663',2),3:(5,0,'\u2663',3),4:(6,0,'\u2663',4),5:(7,0,'\u2663',5),6:(8,0,'\u2663',6),7:(9,0,'\u2663',7),8:(10,0,'\u2663',8),9:("J",0,'\u2663',9),10:("Q",0,'\u2663',10),11:("K",0,'\u2663',11),12:("A",0,'\u2663',12),13:(2,1,'\u2666',0),14:(3,1,'\u2666',1),15:(4,1,'\u2666',2),16:(5,1,'\u2666',3),17:(6,1,'\u2666',4),18:(7,1,'\u2666',5),19:(8,1,'\u2666',6),20:(9,1,'\u2666',7),21:(10,1,'\u2666',8),22:("J",1,'\u2666',9),23:("Q",1,'\u2666',10),24:("K",1,'\u2666',11),25:("A",1,'\u2666',12),26:(2,2,'\u2665',0),27:(3,2,'\u2665',1),28:(4,2,'\u2665',2),29:(5,2,'\u2665',3),30:(6,2,'\u2665',4),31:(7,2,'\u2665',5),32:(8,2,'\u2665',6),33:(9,2,'\u2665',7),34:(10,2,'\u2665',8),35:("J",2,'\u2665',9),36:("Q",2,'\u2665',10),37:("K",2,'\u2665',11),38:("A",2,'\u2665',12),39:(2,3,'\u2660',0),40:(3,3,'\u2660',1),41:(4,3,'\u2660',2),42:(5,3,'\u2660',3),43:(6,3,'\u2660',4),44:(7,3,'\u2660',5),45:(8,3,'\u2660',6),46:(9,3,'\u2660',7),47:(10,3,'\u2660',8),48:("J",3,'\u2660',9),49:("Q",3,'\u2660',10),50:("K",3,'\u2660',11),51:("A",3,'\u2660',12)}
    def __init__(self, num):
        '''
        arguments: self, num
        return none
        
        '''
        self._num=Card.rank_dict.get(num) 
    #def suit(self):
    def __repr__ (self):
        '''
        Arguments: self
        return: card rank, unicode character of suit
        '''
        return "{}{}".format(self._num[0],self._num[2])
    def suit (self):
        '''
        arguments: self
        return: suit rank 0-4
        '''
        return self._num[1]
    def rank(self):
        '''
        arguments: self
        return: value 0-12
        '''
        return self._num[3]
    def __lt__(self, other):
        '''
        Arguments: self, other
        Return boolean
        '''
        return self._num[3]<other._num[3]
         
        return self_rank<other._num[0]
    def points (self):
        '''
        Arguments: self
        return: value 0-4
        
        '''
        if self._num[0]=="A":
            return 4
        if self._num[0]=="K":
            return 3
        if self._num[0]=="Q":
            return 2
        if self._num[0]=="J":
            return 1
        else:                      


            return 0


# 
# 
# 
# 
# 
# 
# 
# 
# 
# ##### <span style="color:red">Tests:</span>

# In[21]:




# After you implement your constructor you can execute the following expression, which uses list comprehension to make a complete deck of cards:

# In[22]:

#deck = [ Card(i) for i in range(52) ]


# Now you can print the deck to see if all the cards are there:

# In[23]:

#print(deck)


# Use the following code cell plus any additional cells you want to test the methods of your Card class:

# In[ ]:

# Write Python code that tests your Card class here (add more cells as needed)


# ###  <span style="color:teal">2. &nbsp; BlackjackCard Class</span>

# Define a second new class called BlackjackCard. The new class should use Card as its base class. Overload the `points` method so that aces have 11 points, face cards (J, Q, K) have 10 points, and other cards have their natural value (10, 9, 8, *etc.* down to 2).
# 
# You should also overload the `__lt__` operator so BlackjackCards are compared only by their rank, with aces highest, then kings, queens, *etc.*

# <pre>
# >>> y = BlackjackCard(38) 
# 
# >>> y
# A♥
# 
# >>> y.points()
# 11
# 
# >>> z = BlackjackCard(39)
# 
# >>> z
# 2♠
# 
# >>> z.points()
# 2
# 
# >>> y < z
# False
# </pre>

# <span style="color:blue">Style Points:</span> &nbsp; Can you figure out how to have `__lt__` use the code you already wrote to compute the rank of a card?

# ##### <span style="color:red">Documentation:</span>

# === Describe your class in this markdown cell ===
#   >>>
#   BlackjackCard Class, Card class inherited
#     redefined function: points (returns value 2-11)

# ##### <span style="color:red">Code:</span>

# In[24]:

# Put your class definition in this code cell
class BlackjackCard(Card):
    '''
    BlackjackCard Class, Card class inherited
    redefined function: points (returns value 2-11)
    
    '''
    def points(self):
        '''
        Arguments: self
        return: value 2-11
        
        '''
        if self._num[0]=="A":
            return 11
        if self._num[0]=="Q" or self._num[0]=="J" or self._num[0]=="K":
            return 10
        else:
            return self._num[0]


# ##### <span style="color:red">Tests:</span>

# In[25]:

#A=BlackjackCard(12)
#K=BlackjackCard(11)
#Q=BlackjackCard(10)
#J=BlackjackCard(9)
#ten=BlackjackCard(7)
#A
#K
#Q
#J
#ten
#print(A.points(),'\n',K.points(),'\n',Q.points(),'\n',J.points(),ten.points())


# After you implement the constructor for the new class, execute this expression to make a complete deck of blackjack cards:

# In[26]:

#bj_deck = [ BlackjackCard(i) for i in range(52) ]
#deck = [ Card(i) for i in range(52) ]


# Use the following code cell plus any additional cells you want to print the new deck (it should look exactly like the previous deck) and test the methods of your Card class:

# In[27]:

# Write Python code that tests your BlackjackCard class here (add more cells as needed)
#from random import sample
#bjhand = sample(bj_deck,2)
#hand=sample(deck,2)

#print(bjhand, " ", hand)


# ### <span style="color:teal">3. &nbsp; The `total` Function</span>

# Write a function called `total` that will compute the sum of the number of points in a hand (a list of Card objects).

# To make a hand to test `total` use a function named `sample` from Python's `random` library.  This example assumes the list named `deck` contains 52 Card objects:
# <pre>
# >>> from random import sample
# 
# >>> hand = sample(deck, 5)
# >>> hand
# [5♦, 3♦, K♠, J♠, 9♣]
# 
# >>> total(hand)
# 4
# </pre>

# In the example above the total is 4 because kings are worth 3 points and jacks are worth 1.

# The same function should also be able to compute the total number of points in a hand made from BlackjackCard objects:
# <pre>
# >>> bj_hand = sample(bj_deck,3) 
# >>> bj_hand
# [7♦, Q♦, 9♥]
# 
# >>> total(bj_hand)
# 26
# </pre>

# ##### <span style="color:red">Documentation:</span>

# === Describe your function in this markdown cell ===
# >>>Arguments: list of Card or Blackjack cards based on deck selected
#     Returns: Total number of points in accordance to points function of which deck is used
#     

# ##### <span style="color:red">Code:</span>

# In[28]:

# Put your function definition in this code cell
def total(hand):
    '''
    Arguments: list of Card or Blackjack cards based on deck selected
    Returns: Total number of points in accordance to points function of which deck is used
    '''
    total=0
    for card in hand:
        total+=card.points()
    return total
        


# ##### <span style="color:red">Tests:</span>

# In[29]:

# Write Python code that tests your function here (add more cells as needed)
#total(bjhand)


# ### <span style="color:teal">Extra Credit Ideas</span>

# If you want to earn extra credit points for this project try one of the extensions listed below (or feel free to invent other ways to extend the project).
# 
# <span style="color:red; font-weight:bold;">Important:</span>  To earn extra credit points make sure you fill in the following markup cell to explain what you did so the graders will look for your extensions when they grade your project:

# === Describe any extra credit here ===
# >> Accepts argument of class to create deck based on class given

# In[20]:

def new_deck(className):
    '''
    Prints new deck of either normal card deck or blackjack card deck based on parameter
    Arguments: className
    Prints:Deck
    
    '''
    if className=="Card":
        deck = [ Card(i) for i in range(52) ]
    elif className=="BlackjackCard":
        deck = [ BlackjackCard(i) for i in range(52) ]
    print(deck)


# In[1]:

def new_deck(className):
    '''
    Prints new deck of either normal card deck or blackjack card deck based on parameter
    Arguments: className
    Prints:Deck
    
    '''
  
    deck = [ className(i) for i in range(52) ]
    print(deck)


# In[3]:

#new_deck(5)


# #####  Validate the Argument Passed to Constructors

# Have the Card constructor check to make sure the card ID argument is between 0 and 51 and raise an exception otherwise.

# ##### Allow Strings or Integers to be Passed to Constructors

# Can you figure out how to allow users to pass either a card ID or a string with a specified rank and suit to the Card constructor?  For example, to create the ace of spades the call could be either `Card(51)` or `Card(‘A♠’)`. 
# 
# If you get this working, will the new technique for specifying cards be inherited by the BlackjackCard class, or do you have to add some additional code to the BlackjackCard constructor?

# ##### Write a `new_deck` Function

# Write a function named `new_deck` that takes the name of a class as an argument and returns a list of 52 card objects of that type:
# <pre>
# >>> deck = new_deck(Card)
# >>> bj_deck = new_deck(BlackjackCard)
# </pre>
