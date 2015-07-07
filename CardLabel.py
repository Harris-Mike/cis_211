#
# The CardLabel class defines a label that has the image of a playing card.
# It was designed for the Blackjack GUI project in CIS 211.
#
# This file contains an additional class named CardTextLabel that is a 
# workaround for an apparent bug in IPython 3.0 that prevents images from
# being displayed.

# John Conery
# CIS 211
# Spring 2015

from tkinter import *

class CardLabel(Label):
    """
    A CardLabel is a Tk Label that displays an image of a playing card.
    """
    
    def __init__(self, parent):
        "The default image for a new label is the back of a card"
        Label.__init__(self, parent, image=CardLabel.back_image)

    image_directory = './cardimages/'
        
    @staticmethod
    def load_images():
        "Get the card images from files, save them in a list (a class variable)"
        CardLabel.images = [PhotoImage(file=CardLabel.image_directory + "card{}.gif".format(i)) for i in range(52)]
        CardLabel.back_image = PhotoImage(file=CardLabel.image_directory + "back-blue.gif")
        CardLabel.blank_image = PhotoImage(file=CardLabel.image_directory + "blank.gif")
        
    def display(self, side='back', id=0):
        """
        Change the label to show a new side of a card. If showing the
        front side the id parameter specifies which image (otherwise
        that parameter is ignored).
        """
        if side == 'back':
            self.configure(image=CardLabel.back_image)
        elif side == 'front':
            self.configure(image=CardLabel.images[id])
        else:
            self.configure(image=CardLabel.blank_image)

from Card import *

class CardTextLabel(CardLabel):
    """
    A CardLabel that shows a card as text instead of an image.
    """

    def __init__(self, parent):
        "The default image for a new label is the back of a card"
        Label.__init__(self, parent, text='?', height=3, width=5, font=('Helvetica', 24))
        
    @staticmethod
    def load_images():
        CardTextLabel.images = [ repr(Card(i)) for i in range(0,52) ] 
        
    def display(self, side='back', id=0):
        """
        Change the label to show a new side of a card. If showing the
        front side the id parameter specifies which image (otherwise
        that parameter is ignored).
        """
        if side == 'back':
            self.configure(text='?')
        elif side == 'front':
            self.configure(text=CardTextLabel.images[id])
        else:
            self.configure(text='')

