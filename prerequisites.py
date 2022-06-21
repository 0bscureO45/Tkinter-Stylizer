import random
from colorutils import *
import requisites as req

def color_type(color):
    """Check the type of the color.

    Args:
        color (str, tuple): The color.
    Returns:
        string: the type of the color
    """
    if type(color) == tuple:
        return "rgb"
    elif color[0] == "#":
        return "hex"
    else:
        return "web"

def color_convert(before, after_type):
    """Convert a color from one format to another.

    Args:
        before (str, tuple): The color before conversion.
        after (str, tuple): The color after conversion.
    Returns:
        tuple or string: the converted color
    """
    # getting the type of the color
    before_type = color_type(before)
    # checking the type of the color
    if before_type == after_type:
        return before
    elif before_type == "rgb":
        if after_type == "hex": return rgb_to_hex(before)
        elif after_type == "web": return rgb_to_web(before)
    elif before_type == "hex":
        if after_type == "rgb": return hex_to_rgb(before)
        elif after_type == "web": return hex_to_web(before)
    elif before_type == "web":
        if after_type == "rgb": return web_to_rgb(before)
        elif after_type == "hex": return web_to_hex(before)
    else:
        return f"{before} is not a valid color"



def get_image(path):
    """A function that returns a Pillow image from a path.

    Args:
        path (str): the path to the image.
    Returns:
        Pillow image: the image.
    """
    return req.Image.open(path)


def numbers_after_point(decimal_number: str):
    """Get the numbers after the decimal places of a float number.
    Args:
        decimal_number (float): The decimal number.
    Returns:
        str: the numbers after decimal points
    """
    # converting the number into a string
    decimal_number = str(decimal_number)
    # checking if it contains a decimal point
    if "." in decimal_number:
        # getting the index of the decimal point
        # getting the numbers after the decimal point
        return str(decimal_number[decimal_number.index(".") + 1:])
    else:
        return 0


def number_of_digits_after_point(decimal_number):
    """Get the number of digits after the decimal point of a float number.

    Args:
        decimal_number (float): The decimal number.
    Returns:
        int: the number of digits after decimal point
    """
    decimal_number = str(decimal_number)
    return len(numbers_after_point(decimal_number))


def float_range(start, stop=None, step=1.0, full=False):
    """An alternative to range() which allows floating point numbers.

    Args:
        start (float or int): The starting float or int value.
        stop (float or int, optional): The ending float or int value. Defaults to None.
        step (float or int, optional): The steps float or int value. Defaults to 1.
        full (bool, optional): If True then the range will include the start and stop values. Defaults to False. 
    Yields:
        an iterable: similar to range function
    """
    # converting start to float
    start = float(start)
    # if stop is not provided, then stop is equal to start
    if stop is None:
        stop = start + 0.0
        start = 0.0
    if full:
        stop += step

    count = 0
    while True:
        result = round(start + count * step,
                       number_of_digits_after_point(step))
        if step > 0 and result >= stop:
            break
        elif step < 0 and result <= stop:
            break
        yield result
        count += 1


def random_alphabet():
    """A random alphabet generator

    Returns:
        string: the chosen random alphabet
    """
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h",
                 "i", "j", "k", "l", "m", "n", "o", "p",
                 "q", "r", "s", "t", "u", "v", "w", "x",
                 "y", "z"]
    return random.choice(alphabets)


def random_number():
    """A random number generator

    Returns:
        int: the chosen random number
    """
    return str(random.randint(0, 9))


def random_special_key():
    """A random special key generator

    Returns:
        string: the chosen random special key
    """
    special_keys = ["@", "#", "$", "%", "&", "*"]
    return random.choice(special_keys)


def random_alphabet_s(length):
    """A random alphabet generator

    Args:
        length (int): the number of alphabets to be generated

    Returns:
        string: the chosen random alphabets string
    """
    result = ""
    for i in range(length):
        result += (random_alphabet())
    return result


def random_number_s(length):
    """A random number generator

    Args:
        length (int): the number of numbers to be generated

    Returns:
        int: the chosen random numbers
    """
    result = ""
    for i in range(length):
        result += (random_number())
    return result


def random_special_key_s(length):
    """A random special key generator

    Args:
        length (int): the number of special keys to be generated

    Returns:
        string: the chosen random special keys string
    """
    result = ""
    for i in range(length):
        result += (random_special_key())
    return result


def random_combination(length):
    """A random combination generator of alphabets, numbers and special keys

    Args:
        length (int): the number of letters in the combination to be generated

    Returns:
        string: the chosen random combination
    """
    result = ""
    for i in range(length):
        result += random.choice([random_alphabet(),
                                 random_number(),
                                 random_special_key()])
    return result


def custom_random_combination(length, alphabet, number, special_key):
    """A custom random combination generator of the specified types

    Args:
        length (int): the number of letters in the combination to be generated
        alphabet (int): the number of alphabets to be generated
        number (int): the number of numbers to be generated
        special_key (int): the number of special keys to be generated

    Returns:
        string: the chosen random combination
    """
    # the most 'thaka denne walla function'
    result = ""
    # returning "None Selected" if no option is selected
    if (not alphabet and not number and not special_key) or (length == 0):
        return "NONE"
    # returning length times the random alphabets if only alphabet is selected
    elif alphabet and not number and not special_key:
        return random_alphabet_s(length)
    # returning length times the random numbers if only number is selected
    elif not alphabet and number and not special_key:
        return random_number_s(length)
    # returning length times the random special keys if only special key is selected
    elif not alphabet and not number and special_key:
        return random_special_key_s(length)
    # returning the random_combination of all selected options
    elif alphabet and number and special_key:
        for iteration in range(length):
            result += random.choice([random_alphabet(),
                                     random_number(), random_special_key()])
        return result
    # returning the random_combination for two selected options
    # doesn't run correctly for one option
    else:
        # a bool to ensure only one character is added in an iteration
        # to avoid repetition of the same character
        character_added = False
        result = ""
        for iteration in range(length):
            if alphabet and not character_added and not result[-1:].isalpha():
                result += random_alphabet()
                character_added = True
            if number and not character_added and not result[-1:].isdigit():
                result += random_number()
                character_added = True
            if special_key and not character_added and result[-1:].isalnum():
                result += random_special_key()
                character_added = True
            # resetting the character_added bool to False
            character_added = False
        # returns the shuffled result
        shuffled = list(result)
        random.shuffle(shuffled)
        return ''.join(shuffled)
