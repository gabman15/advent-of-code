###
# Day 5
###

def process_input_data(input_data):
    in_rules = True
    order_rules_str = list()
    update_str = list()
    for line in input_data:
        if (line == ""):
            in_rules = False
        elif (in_rules):
            order_rules_str.append(line)
        else:
            update_str.append(line)
            
    updates = list()
    for update in update_str:
        updates.append(update.split(','))
    order_rules = list()
    for rule in order_rules_str:
        order_rules.append(rule.split('|'))
    return order_rules, updates

def verify_update_rule(update, rule):
    try:
        idx1 = update.index(rule[0])
        idx2 = update.index(rule[1])
        if (idx1 < idx2):
            return True
        else:
            return False
    except:
        return True

def verify_update(update, rules):
    for rule in rules:
        if (not verify_update_rule(update, rule)):
            return False
    return True

def verify_updates(updates, rules):
    valid_updates = list()
    for update in updates:
        if (verify_update(update, rules)):
            valid_updates.append(update)
    return valid_updates

def get_sum_middle_elt(updates):
    sum_middle = 0
    for update in updates:
        sum_middle += int(update[int(len(update)/2)])
    return sum_middle

def solution(input_data):
    order_rules, updates = process_input_data(input_data)
    return get_sum_middle_elt(verify_updates(updates, order_rules))
    
def read_input():
    input_data = list()
    while (True):
        try:
            input_data.append(input())
        except:
            break
    return input_data

if (__name__ == '__main__'):
    data = read_input()
    print(solution(data))
