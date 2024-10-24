def exchange_money(budget, exchange_rate):

     
    return budget / exchange_rate
def get_change(budget, exchanging_value):
     
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return  denomination * number_of_bills


def get_number_of_bills(amount, denomination):
     return  amount // denomination
    
    
def get_leftover_of_bills(amount, denomination):
    
    number_b = amount // denomination
    amount_deno = number_b * denomination
    left = amount - amount_deno
    return left


def exchangeable_value(budget, exchange_rate, spread, denomination):


    
    new_exchange = (exchange_rate * (spread / 100)) + exchange_rate
    maximum_value =int( budget / new_exchange)
    number_Bmax = maximum_value // denomination
    new_value = number_Bmax * denomination
    return new_value
    

