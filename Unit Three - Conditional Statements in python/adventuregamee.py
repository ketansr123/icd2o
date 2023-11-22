import random

def choose_team():
    print("Choose your Team:")
    print("1. Manchester United")
    print("2. Chelsea")
    print("3. Liverpool")
    team_name = input("Enter the exact name for one of these teams above to pick one of them (Include the caps):")
    
    while team_name not in ['Manchester United', 'Chelsea', 'Liverpool']:
        print("Invalid team name")
        team_name = input("Enter the exact name for one of these teams to pick one of them (Include the caps):")
    
    stamina = random.randint(50, 100)
    return team_name, stamina

def game_intro(team):
    intro1 = f"You are a player representing the team {team}. Your opponent is Manchester City."
    intro2 = "This is the Premier League final and the match will now begin."
    print(intro1)
    print(intro2)

def make_decision(stamina):
    print("The score is 0-0 but your team has an opportunity!")
    print("1. Shoot from far")
    print("2. Pass to teammate")
    decision = input("Enter the number for your decision: ")

    while decision not in ['1', '2']:
        print("Invalid number")
        decision = input("Enter the number for your decision: ")

    if decision == '1':
        print("You missed the shot badly and got a leg cramp.")
        print("-20 stamina")
        print("Fortunately, your teammate scored a header in the next 15 minutes but you lost stamina.")
        print("Score:1-0")
        stamina -= 20
    elif decision == '2':
        print("Your team got a goal. Great assist!")
        print("Score: 1-0")
    
    print("Erling Haaland from Man City scored a penalty.")
    print("Score: 1-1")
    print("You have been awarded a penalty. Choose a direction.")
    print("1. Top right")
    print("2. Bottom left")
    decision2 = input("Enter the number for your decision: ")

    if decision2 == '1':
        print("The goalkeeper saved it.")
        print("Haaland scored again in the last minute.")
        print("Your team lost 2-1")
        stamina -= 30
        return "Game over", stamina
    elif decision2 == '2':
        print("You scored the penalty!")
        print("You won the game 2-1")
        return "You win!", stamina

def finalresult(stamina):
    if stamina > 0:
        return f"Your final stamina was {stamina}"
        
    else:
        return "Your stamina reached zero and you passed out"
        
    
team, initial_stamina = choose_team()
game_intro(team)
result, final_stamina = make_decision(initial_stamina)
final_result = finalresult(final_stamina)
print(final_result)
