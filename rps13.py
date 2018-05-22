Some Useful Names
null = "null"
rock = "rock"
paper = "paper"
scissors = "scissors"

# A Thesaurus (implemented as a dictionary)
synonyms = {"rock": rock,
            "paper": paper,
            "scissors": scissors,
            "stone": rock,
            "vellum": paper,
            "shears": scissors}

# Final States
game_is_draw = "Game is a Draw"

playerA_wins = "Player A Wins"

playerB_wins =  "Player B Wins"

# Initial State
both_players_must_choose = "Both Players Must Choose"

# Transition States
playerA_must_choose = "Player A Must Choose"

playerB_must_choose = "Player B Must Choose"

# Transition Table (implemented as a dictionary)
transitions = {(null,    null): both_players_must_choose,
               (null,    rock): playerA_must_choose,
               (null,    paper): playerA_must_choose,
               (null,    scissors): playerA_must_choose,
               (rock,    null): playerB_must_choose,
               (rock,    rock): game_is_draw,
               (rock,    paper): playerB_wins,
               (rock,    scissors): playerA_wins,
               (paper,   null): playerB_must_choose,
               (paper,   rock): playerA_wins,
               (paper,   paper): game_is_draw,
               (paper,   scissors): playerB_wins,
               (scissors, null): playerB_must_choose,
               (scissors, rock): playerB_wins,
               (scissors, paper): playerA_wins,
               (scissors, scissors): game_is_draw}



# Simulate Initialization
playerA_choice = null
playerB_choice = null

# Simulate Players Choosing
playerA_choice = synonyms["stone"]
playerB_choice = synonyms["shears"]

# Main Logic
state = (playerA_choice, playerB_choice)
print(outcomes[state])