###########################################
import math


#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively
class Patient:
    def __init__(self, name : str, symptoms : list[str]):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}


#
# 1.2)
# Create a method called "add_test"
# which takes two parameters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

    def add_test(self, test_name: str, result: bool):
        self.tests[test_name] = result    
#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and increases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']
    def has_covid(self):
        if "covid" in self.tests:
            if self.tests["covid"] is True:
                return .99
            else:
                return 0.01
        else:
            probability = 0.05
            for symptom in ['fever', 'cough', 'anosmia']:
                if symptom in self.symptoms:
                    probability += 0.1
            return probability

######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" of the card.
# The class should store both as attributes.

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

import random

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suitx, valuex) for suitx in suits for valuex in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            print('Empty deck.')
            return None
        topcard = self.cards.pop(0)
        print(f"{topcard.suit}, {topcard.value}")
        return topcard


###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimeter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.
from abc import ABCMeta, abstractmethod

class PlaneFigure(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def compute_perimeter(self):
        raise NotImplementedError

    @abstractmethod
    def compute_surface(self):
        raise NotImplementedError

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.
class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.side1 = c1
        self.side2 = c2
        self.height = h

    def compute_perimeter(self):
        return self.base + self.side1 + self.side2

    def compute_surface(self):
        return 0.5*self.base*self.height

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.
class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.length = a
        self.width = b

    def compute_perimeter(self):
        return 2*(self.length + self.width)

    def compute_surface(self):
        return self.length * self.width

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.
class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return math.pi*2*self.radius

    def compute_surface(self):
        return math.pi*self.radius**2
