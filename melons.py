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

class Melon(object):
    def get_base_price(self):
        #HOOK for later complicating things here
        return 5

class Watermelon(Melon):
    name = 'Watermelon' 
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price
        if qty >= 3:
            total_cost = total_cost * 0.75
        return total_cost

class Cantaloupe(Melon):
    name = 'Cantaloupe' 
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price

        if qty >= 5:
            total_cost = total_cost * 0.5

        return total_cost

class Casaba(Melon):
    name = 'Casaba' 
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price * 1.5 + 1
        return total_cost

class Sharlyn(Melon):
    name = 'Sharlyn' 
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price * 1.5
        return total_cost

class SantaClaus(Melon):
    name = 'Santa Claus' 
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price * 1.5
        return total_cost

class Christmas(Melon):
    name = 'Christmas' 
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter']
    

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price
        return total_cost

class HornedMelon(Melon):
    name = 'Horned Melon' 
    color = 'yellow'
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price * 1.5
        return total_cost

class Xigua(Melon):
    name = 'Xigua' 
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Summer']
    

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price * 1.5 * 2
        return total_cost

class Ogen(Melon):
    name = 'Ogen' 
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring','Summer']
    

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = self.get_base_price()
        total_cost = qty * price + 1
        return total_cost
