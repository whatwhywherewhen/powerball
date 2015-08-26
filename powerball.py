import random
power_1 = range(1, 54)
power_2 = range(1, 43)
numbers = []
quantity = int(raw_input("How many sets of Powerball numbers would you like?"))
def repeat():
    global numbers
    numbers = random.sample(power_1, 5)
    numbers = sorted(numbers)
    number = random.choice(power_2)
    print "Your Numbers: " + " ".join([str(item) for item in numbers]) + "     Powerball:" + str(number)
for i in range(quantity):
    repeat()



