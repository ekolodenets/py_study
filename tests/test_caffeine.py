
from codewars.caffeine import caffeine


def test_caffeine():
    caf = caffeine("latte", 0)
    assert caf == "You haven't even had coffee today!"

def test_caffeine_d():
    caf = caffeine("decaf", 25)
    assert caf == "You haven't even had coffee today!"

def test_caffeine_e():
    caf = caffeine("espresso", 6)
    assert caf == "Only decaf for you now!"

def test_caffeine_m():
    caf = caffeine("mocha", 1)
    assert caf == "The doctor won't be worried yet!"

def test_caffeine_de():
    caf = caffeine("double espresso", 2)
    assert caf == "You can have 2 more shots then no more!"

def test_caffeine_l():
    caf = caffeine("latte", 5)
    assert caf == "You can only have an espresso, latte or a decaf now"