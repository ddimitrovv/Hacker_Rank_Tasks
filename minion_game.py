def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart_score = 0
    str_len = len(string)

    for index, char in enumerate(string):
        if char in vowels:
            kevin_score += str_len - index
        else:
            stuart_score += str_len - index
            
    if stuart_score > kevin_score :
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score :
        print(f"Kevin {kevin_score}")
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)