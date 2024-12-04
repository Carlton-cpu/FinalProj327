# Define type effectiveness (simplified)
# 2.0 means strong, 0.5 means weak, 1.0 means neutral
"""empty defenitions and classes to be expounded on."""
def attacker_type():
def defender_type():
class pokemon1():
class pokemon2enemy():
type_chart = {
    "Fire": {"Fire": 1.0, "Water": 0.5, "Grass": 2.0},
    "Water": {"Fire": 2.0, "Water": 1.0, "Grass": 0.5},
    "Grass": {"Fire": 0.5, "Water": 2.0, "Grass": 1.0}
}

def get_type_effectiveness(attacker_type, defender_type):
    """
    Returns the type effectiveness multiplier based on attacker and defender types.
    """
    if attacker_type in type_chart and defender_type in type_chart[attacker_type]:
        return type_chart[attacker_type][defender_type]
    return 1.0  # Neutral effectiveness if type is not found

def calculate_win_probability(attacker_type, defender_type, attacker_level, defender_level):
    """
    Calculates the probability of winning based on type and level.
    
    Parameters:
    - attacker_type: Type of the attacking Pokémon (e.g., "Fire")
    - defender_type: Type of the defending Pokémon (e.g., "Water")
    - attacker_level: Level of the attacking Pokémon (1-100)
    - defender_level: Level of the defending Pokémon (1-100)
    
    Returns:
    - Probability of attacker winning (0.0 to 1.0)
    """
    # Get type effectiveness multiplier
    type_effectiveness = get_type_effectiveness(attacker_type, defender_type)
    
    # Calculate level influence (higher level has advantage)
    level_factor = attacker_level / (attacker_level + defender_level)
    
    # Combine type effectiveness and level factor for a win probability
    probability = type_effectiveness * level_factor
    
    # Cap probability between 0 and 1
    return min(max(probability, 0.0), 1.0)

# Example usage
attacker_type = "Fire"
defender_type = "Grass"
attacker_level = 50
defender_level = 40

win_probability = calculate_win_probability(attacker_type, defender_type, attacker_level, defender_level)
print(f"Chance of winning for {attacker_type} type (Level {attacker_level}) vs {defender_type} type (Level {defender_level}): {win_probability:.2f}")

# players and pokemon lineup 
players = { 
    "Player 1": {"type": "Fire", "level": 0-20},
    "Player 2": {"type": "Water", "level": 0-20},
    "Player 3": {"type": "Grass", "level": 0-20},
    "Player 4": {"type": "Fire", "level": 0-20},
}

def tournament 
    print("\begin the pokemon tournament!\n"

    # Round 1 
    print("round 1: Player 1 vs Player 2"
    Player 1_win_prob = calculate_win_probability(
        players["Player 1"]["type"], 
        players["Player 2"]["type"], 
        players["Player 1"]["level"], 
        players["Player 2"]["level"]
        )
        winner1 = "player 1" if player1__prob >= 0.5 else "player 2" 
        print(f"Winner: {winner1}\n")

        print("Round 1: Player 3 vs Player 4")
        player3_win_prob = calculate_win_probability(
            players["Player 3"]["type"], 
            players["Player 4"]["type"], 
            players["Player 3"]["level"], 
            players["Player 4"]["level"]  
         )   
         winner2 = "player 3" if player3_win_prob >= 0.5 else "player4"
         print(f"Winner: {winner2}\n")

          # final match 
          print "FInal Match: {} vs {}".Format(winner,winner))
          final_win_prob = calculate_win_probability(
             players[winner1]["type"], 
             players[winner2]["type"], 
             players[winner1]["level"], 
             players[winner2]["level"]
          )

          Champion = winner1 if final_win_prob >= 0.5 else winner2 
          print(f"Champion of pokemon tournament: {poekmon champion}")
          
