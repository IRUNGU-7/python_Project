EXPECTED_BAKE_TIME =  40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    """gives the baking time remaining """


    return int(EXPECTED_BAKE_TIME - elapsed_bake_time)
    print(bake_time_remaining. __doc__)



def preparation_time_in_minutes(number_of_layers):
    """gives the preparation time  based on th number of layers"""
    PT = PREPARATION_TIME * number_of_layers
    return PT
    print (preparation_time_in_minutes. __doc__)
    




def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """gives the sum of the elapsed time together with the preparation """
    return ((PREPARATION_TIME * number_of_layers) + elapsed_bake_time)
    print (elapsed_time_in_minutes. __doc__)
    





