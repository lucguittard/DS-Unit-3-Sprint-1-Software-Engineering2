import numpy as np
import pandas as pd
import random

class Product:

# Class Attribute (optional here)

# Instance Attribute/Initializer
    def __init__(
        self, name, price = 10, weight = 20, flammability = .5,
        identifier = random.randint(1000000,9999999)
        ):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

# instance method
    def stealability(self):
        value_ratio = self.price / self.weight
        if value_ratio < .5:
            return 'Not so stealable...'
        elif value_ratio >= .5 and value_ratio < 1:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

# instance method
    def explode(self):
        danger_ratio = self.flammability * self.weight
        if danger_ratio < 10:
            return '...fizzle.'
        elif danger_ratio >= 10 and danger_ratio < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


# Child Class (inheritance from Product)
class BoxingGlove(Product):

# Instance Attribute
    def __init__(self,weight = 10):
        self.weight = weight
        super().__init__(self,weight = 10)

# instance method
    def explode(self):
        return "...it's a glove."

# instance method
    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
            
