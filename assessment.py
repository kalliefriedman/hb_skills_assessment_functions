"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.


def is_hometown(town_name):
    """Takes one string input and returns boolean of True or False depending on if input matches commparison string"""

    if town_name.lower() == "santa barbara":
        return True
    else:
        return False

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def first_and_last(first, last):
    """Takes two string inputs and combines them to return one string"""

    return first + " " + last

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.


def where_are_you_from(town_name, first, last):
    """Takes three string inputs and prints a string depending on a conditional statement. Returns nothing."""

    full_name = first_and_last(first, last)
    if (is_hometown(town_name)) is True:
        print "Hi %s we're from the same place!" % (full_name)
    else:
        print "Hi %s, where are you from?" % (full_name)


###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Takes one string input and returns a boolean of True or False depending on if variable is within fruit list."""

    fruits_list = ['strawberry', 'cherry', 'blackberry']
    if fruit.lower() in fruits_list:
        return True
    else:
        return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Takes on string input and returns shipping cost"""

    if is_berry(fruit) is True:
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Takes input of one list and one number and returns a new list combining all values."""

    new_lst = lst
    new_lst.append(num)
    return new_lst



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_price, state_abbrev, tax_percent) = .05):

    """Takes input of one price, one string, and one float and returns a float value of total price."""
    #  Could've put state-specific variables of price, etc. up here so they could be more easily identified and changed.
    total_price = base_price + (base_price * tax_percent)
    if state_abbrev.upper() == "CA":
        total_price = total_price + (total_price * .03)
    if state_abbrev.upper() == "PA":
        total_price = total_price + 2
    if state_abbrev.upper() == "MA":
        if base_price < 100:
            total_price = total_price + 1
        else:
            total_price = total_price + 3
    return total_price


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def append_to_list(lst, *args):
    """Takes in a list and then arbitrary number of arguments, returning the extended list"""
    lst.extend(args)
    return lst

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def takes_in_word(word):
    """Takes in a string and calls a function on that string, returning the original string and the result of calling function on string."""

    multiply_by_3_result = multiply_by_3(word)
    return word, multiply_by_3_result

def multiply_by_3(word):
    """Takes in a string and returns the result of that word times three."""

    return word * 3


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
