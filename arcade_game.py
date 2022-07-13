"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    """Get point if touching ghost while power pellet active"""
    if power_pellet_active and touching_ghost:
        return True
    else:
        return False

def score(touching_power_pellet, touching_dot):
    """Get point if touching a power pellet or touching a dot"""
    if touching_power_pellet or touching_dot:
        return True
    else:
        return False

def lose(power_pellet_active, touching_ghost):
    """Lose if power pellet not active and touching a ghost"""
    if not power_pellet_active and touching_ghost:
        return True
    else:
        return False

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Win if you've eaten all dots, a power pellet is active, and not touching a ghost"""
    if not touching_ghost and power_pellet_active and has_eaten_all_dots:
        #could and should be changed to say if not lose and eaten all dots then win
        return True
    elif touching_ghost and power_pellet_active and has_eaten_all_dots:
        return True
    elif not touching_ghost and not power_pellet_active and has_eaten_all_dots:
        return True
    else:
        return False
