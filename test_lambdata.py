"""Basic Unit Tests for Lambda pacckage"""

from random import randint
import pytest 
import lambdata as ld 
from lambdata import examples

def test_incrament_int():
    """Making sure increment works for positive int"""
    x0 = 0
    y0 = ld.increment(x0)
    assert y0 == 1

    x1 = 100
    y1 = ld.increment(x1)
    assert y1 == 101

def test_incrament_neg_int():
    """Making sure increment works for neg int"""
    x0 = -1
    y0 = ld.increment(x0)
    assert y0 == 0

def test_incrament_float():
    """Making sure increment works for positive floats"""
    x0 = 10.5
    y0 = ld.increment(x0)
    assert y0 == 11.5

def test_incrament_neg_float():
    """Making sure increment works for neg floats"""
    x0 = -1.5
    y0 = ld.increment(x0)
    assert y0 == -0.5

def test_colors():
    """Testing that colors contains correcct items"""
    assert 'Cyan' in ld.COLORS
    assert 'Mauve' in ld.COLORS
    assert 'Blue' in ld.COLORS
    assert 'Brown' not in ld.COLORS

def test_num_colors():
    """Testing the number of elements in COLORS"""
    assert len(ld.COLORS) == 4

# Testing examples.py
user1 = examples.Social(name='Nick', location='Arizona')
user2 = examples.Social(name='Devin', location='Ohio', upvotes=250)


def test_social_constructor():
    """Testting that social works properly"""
    assert user1.name.lower() == 'nick'
    assert user2.name.lower() == 'devin'

    assert user1.location.lower() == 'arizona'
    assert user2.location.lower() == 'ohio'

    assert user1.upvotes == 0
    assert user2.upvotes == 250

def test_unpopular():
    """Testing if popular function works"""
    assert isinstance(user1.is_popular(), bool)
    assert isinstance(user2.is_popular(), bool)
    assert not user1.is_popular()
    assert user2.is_popular()

def test_social_types():
    assert isinstance(user1.name, str)
    assert isinstance(user1.location, str)
    assert isinstance(user1.upvotes, int)
    