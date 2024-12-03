###
# Day 3
###

import re

def list_instructions(ins):
    list_ins = re.findall("(mul\(\d{1,3},\d{1,3}\))",ins)
    return list_ins

def list_instructions_cond(ins):
    list_ins = re.findall("(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))",ins)
    return list_ins

def run_instructions(ins):
    sum = 0
    for i in ins:
        x,y = i[4:-1].split(',',1)
        print(x + " * " + y)
        sum += (int(x) * int(y))
    return sum

def run_instructions_cond(ins):
    sum = 0
    do = True
    for i in ins:
        if (i == "do()"):
            do = True
        elif (i == "don't()"):
            do = False
        elif (do):
            x,y = i[4:-1].split(',',1)
            print(x + " * " + y)
            sum += (int(x) * int(y))
    return sum
    
def solution(ins):
    list_ins = list_instructions(ins)
    return run_instructions(list_ins)

def solution2(ins):
    list_ins = list_instructions_cond(ins)
    return run_instructions_cond(list_ins)

def read_input():
    instructions = ""
    while (True):
        try:
            instructions += input()
        except:
            break
    return instructions

if (__name__ == '__main__'):
    data = read_input()
    print(solution2(data))
