

def minion_game(string):
    # Filtering input problems
    string = string.upper()
    vowels = 'AEIOU'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    anagrams = []
    words_Player1 = []
    words_Player2 = []

    for index_1, letter_1 in enumerate(string):
        aux_word = ''
        aux_word += letter_1
        for index2, letter_2 in enumerate(string):
            if index_1 == index2:
                anagrams.append(aux_word)
                continue
            if index_1 > index2:
                continue
            aux_word += letter_2
            anagrams.append(aux_word)

    for word in anagrams:
        first_letter = word[0]
        if first_letter in vowels:
            words_Player1.append(word)
        elif first_letter in consonants:
            words_Player2.append(word)

    points_Player1 = len(words_Player1)
    points_Player2 = len(words_Player2)

    if points_Player1 > points_Player2:
        print(f'\nWINNER!\nPlayer1: {points_Player1}\n\n')
        return
    if points_Player2 > points_Player1:
        print(f'\nWINNER!\nPlayer2: {points_Player2}\n\n')
        return
    if points_Player2 == points_Player1:
        print(f'\nDraw\n')
        return

if __name__ == '__main__':
    word = input()
    minion_game(word)
