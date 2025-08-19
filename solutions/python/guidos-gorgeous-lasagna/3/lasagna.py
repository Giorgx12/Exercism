"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def preparation_time_in_minutes(number_of_layers):
    """questa è una nota
    """
    preparation = number_of_layers * PREPARATION_TIME
    return preparation
    return __doc__
    
def elapsed_time_in_minutes(number_of_layers, elapesed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    time = number_of_layers * 2 + elapesed_bake_time
    return time
    
#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(int):
    """
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_bake_time = int
    
    bake_time_remaining = 40 - elapsed_bake_time  
    return bake_time_remaining
    return __doc__



    

#  (you can copy and then alter the one from bake_time_remaining.)

    
