from game_data import data
from art import logo, vs
import random

def random_number():
    random_choice = random.randint(0, len(data) - 1)
    return random_choice

def compare_result(question ,A , B,score) :
    if question  == 'A' :
        if A > B :
            return True
    elif question  == 'B' :
        if B > A :
            return True
    
    else : 
        return False

def game():
    score = 0
    is_finish = False
    x = random_number()
    while not is_finish :
    
        
        y = random_number()
        print(logo)
        print(f"Compare A: {data[x]['name']} , a {data[x]['description']}, from {data[x]['country']}.")
        compare_A = data[x]['follower_count']

        print(vs)

        print(f"Compare B: {data[y]['name']} , a {data[y]['description']}, from {data[y]['country']}.")
        compare_B = data[y]['follower_count']
        question = input("Who has more followers?! Type 'A' or 'B': ")
        clear()
        result = compare_result(question , compare_A , compare_B , score) 
        if result == True :
            x = y
            score += 1
            print(f"You're right! current score {score}")
            
        else :
            print(f"Sorry , that's wrong. Final score {score} ")
            is_finish = True
    
            

        

game()