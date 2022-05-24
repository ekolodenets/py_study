'''
Andy LOVES coffee, he's totally addicted. Unfortunately he drinks too much so the doctor has advised he only drinks 6 espresso shots a day.
Andy only drinks one type of coffee a day, and each have the following number of espresso shots in them:

espresso = 1 shot
double espresso = 2 shots
flat white = 2 shots
latte = 1 shot
mocha = 2 shots
decaf = 0 shot

Challenge:
Create a function that returns the following:
If Andy has consumed no shots return "You haven't even had coffee today!"
If Andy has had less than 4 shots return "The doctor won't be worried yet!"
If Andy has had 4 shots return "You can have 2 more shots then no more!"
If Andy has had 5 shots return "You can only have an espresso, latte or a decaf now"
If Andy has had 6 or more shots return "Only decaf for you now!"

'''

def caffeine(coffee, number):
    d = {'espresso': 1, 'double espresso': 2, 'flat white': 2, 'latte': 1, 'mocha': 2, 'decaf': 0}
    cof = d[coffee]*number
    if cof == 0:
        return "You haven't even had coffee today!"
    elif cof < 4:
        return "The doctor won't be worried yet!"
    elif cof == 4:
        return "You can have 2 more shots then no more!"
    elif cof == 5:
        return "You can only have an espresso, latte or a decaf now"
    elif cof >= 6:
        return "Only decaf for you now!"





# print(caffeine("latte", 5))
# assert (caffeine("latte", 0) == "You haven't even had coffee today!")
# assert (caffeine("decaf", 25) == "You haven't even had coffee today!")
# assert (caffeine("espresso", 6) == "Only decaf for you now!")
# assert (caffeine("mocha", 1) == "The doctor won't be worried yet!")