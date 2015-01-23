"""This file should have our melon-type classes in it."""
""" TO DO:
Define a class for each melon type that we sell. 

Add attributes for things like their name/color/imported/shape/seasons

Add a pricing method

Incorporate discounts
"""
#price info:
# Melons cost $5
# Casabas and Ogens is $1/each more
# Imported melons cost 1.5 times as much
# Square melons cost 2 times as much

# discounts:
# If you buy 3 or more Watermelons, you get all of them at 75% off
# If you buy 5 or more Cantaloupes, you get them all at half price 

class Watermelon(object):
    name = 'Watermelon' 
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price
        if qty >= 3:
            total_cost = total_cost * 0.75
        return total_cost

class Cantaloupe(object):
    name = 'Cantaloupe' 
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price

        if qty >= 5:
            total_cost = total_cost * 0.5

        return total_cost

class Casaba(object):
    name = 'Casaba' 
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price * 1.5 + 1
        return total_cost

class Sharlyn(object):
    name = 'Sharlyn' 
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price * 1.5
        return total_cost

class SantaClaus(object):
    name = 'Santa Claus' 
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price * 1.5
        return total_cost

class Christmas(object):
    name = 'Christmas' 
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price
        return total_cost

class HornedMelon(object):
    name = 'Horned Melon' 
    color = 'yellow'
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price * 1.5
        return total_cost

class Xigua(object):
    name = 'Xigua' 
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Summer']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price * 1.5 * 2
        return total_cost

class Ogen(object):
    name = 'Ogen' 
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring','Summer']
    price = 5.0

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        total_cost = qty * self.price + 1
        return total_cost
