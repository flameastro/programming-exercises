# Create a combat function that takes the player's current health and the amount of damage received, and returns the player's new health. Health can't be less than 0.

def combat(health, damage):
    hp = health - damage
    return hp if hp > 0 else 0


if __name__ == "__main__":
    print(combat(100, 20))  # 80
    print(combat(100, 50))  # 50
    print(combat(100, 100))  # 0