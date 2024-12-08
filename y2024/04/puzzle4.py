###
# Day 4
###

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
UPLEFT = 4
UPRIGHT = 5
DOWNLEFT = 6
DOWNRIGHT = 7

def split_word_search(word_search):
    new_word_search = list()
    for line in word_search:
        new_word_search.append(list(line))
    return new_word_search

def check_letter(word_search, i, j, letter):
    return (word_search[i][j] == letter)

def check_bounds(word_search, i, j, direction):
    if (direction == UP):
        if (i == 0):
            return False
    elif (direction == DOWN):
        if (i == len(word_search) - 1):
            return False
    elif (direction == LEFT):
        if (j == 0):
            return False
    elif (direction == RIGHT):
        if (j == len(word_search[0]) - 1):
            return False
    elif (direction == UPLEFT):
        return (check_bounds(word_search, i, j, UP) and
                check_bounds(word_search, i, j, LEFT))
    elif (direction == UPRIGHT):
        return (check_bounds(word_search, i, j, UP) and
                check_bounds(word_search, i, j, RIGHT))
    elif (direction == DOWNLEFT):
        return (check_bounds(word_search, i, j, DOWN) and
                check_bounds(word_search, i, j, LEFT))
    elif (direction == DOWNRIGHT):
        return (check_bounds(word_search, i, j, DOWN) and
                check_bounds(word_search, i, j, RIGHT))
    return True

def find_word(word_search, i, j, word, direction):
    if (check_letter(word_search, i, j, word[0])):
        if (len(word) == 1):
            return True
        else:
            if (not check_bounds(word_search, i, j, direction)):
                return False
            if (direction == UP):
                return find_word(word_search, i-1, j, word[1:], direction)
            elif (direction == DOWN):
                return find_word(word_search, i+1, j, word[1:], direction)
            elif (direction == LEFT):
                return find_word(word_search, i, j-1, word[1:], direction)
            elif (direction == RIGHT):
                return find_word(word_search, i, j+1, word[1:], direction)
            elif (direction == UPLEFT):
                return find_word(word_search, i-1, j-1, word[1:], direction)
            elif (direction == UPRIGHT):
                return find_word(word_search, i-1, j+1, word[1:], direction)
            elif (direction == DOWNLEFT):
                return find_word(word_search, i+1, j-1, word[1:], direction)
            elif (direction == DOWNRIGHT):
                return find_word(word_search, i+1, j+1, word[1:], direction)
    return False

def find_mas(word_search, i, j):
    if (check_letter(word_search, i, j, "A")):
        if (check_bounds(word_search, i, j, DOWNRIGHT) and
            check_bounds(word_search, i, j, UPLEFT) and
            check_bounds(word_search, i, j, DOWNLEFT) and
            check_bounds(word_search, i, j, UPRIGHT)):
            return ((find_word(word_search, i-1, j-1, "MAS", DOWNRIGHT) or
                     find_word(word_search, i+1, j+1, "MAS", UPLEFT)) and
                    (find_word(word_search, i-1, j+1, "MAS", DOWNLEFT) or
                     find_word(word_search, i+1, j-1, "MAS", UPRIGHT)))
    return False

def look_for_words(word_search, word):
    num = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if (find_word(word_search, i, j, word, UP)):
                num+=1
            if (find_word(word_search, i, j, word, DOWN)):
                num+=1
            if (find_word(word_search, i, j, word, LEFT)):
                num+=1
            if (find_word(word_search, i, j, word, RIGHT)):
                num+=1
            if (find_word(word_search, i, j, word, UPLEFT)):
                num+=1
            if (find_word(word_search, i, j, word, UPRIGHT)):
                num+=1
            if (find_word(word_search, i, j, word, DOWNLEFT)):
                num+=1
            if (find_word(word_search, i, j, word, DOWNRIGHT)):
                num+=1
    return num

def look_for_mas(word_search):
    num = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if (find_mas(word_search, i, j)):
                num+=1
    return num        

def solution(word_search):
    word_search = split_word_search(word_search)
    # print(word_search[4])
    # print(find_word(word_search, 4, 0, "XMAS", UP))
    # print(find_word(word_search, 4, 0, "XMAS", DOWN))
    # print(find_word(word_search, 4, 0, "XMAS", LEFT))
    # print(find_word(word_search, 4, 0, "XMAS", RIGHT))
    return look_for_mas(word_search)
    
def read_input():
    word_search = list()
    while (True):
        try:
            word_search.append(input())
        except:
            break
    return word_search

if (__name__ == '__main__'):
    data = read_input()
    print(solution(data))
