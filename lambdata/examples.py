"""Module 2 OOPExample Module"""

class BareMin:
    pass

class Complex:
    """
    This is a class with a real and imaginary attribute
    """
    def __init__(self, real, imag):
        """
        Constructor for complex numbers
        """
        self.r = real
        self.i = imag

    def add(self, complex_other):
        """
        Adds two ccomplex objects together
        """
        self.r += complex_other.r
        self.i += complex_other.i
    
    def __repr__(self):
        return '({},{})'.format(self.r, slef.i)

    


# complex_num_1 = Complex(3, -5)

# complex_num_2 = Complex(2, 6)


class Social:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = str(location)
        self.upvotes = upvotes

    def recieve_upvotes(self, nun_upvotes):
        self.upvotes += nun_upvotes

    def is_popular(self):
        return self.upvotes > 100
    
