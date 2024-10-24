    if power_pellet_active == True and touching_ghost == True:
        return (True)
    else:
        return False
def score(touching_power_pellet, touching_dot):
 
    if touching_power_pellet  == True or touching_dot == True:
        return True
    else:
        return False
     
    
def lose(power_pellet_active, touching_ghost):

    if power_pellet_active == False and touching_ghost == True:
        return True
    else:
        return  False
        

