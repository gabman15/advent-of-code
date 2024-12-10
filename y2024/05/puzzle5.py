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

def get_incorrect_updates(updates, rules):
    incorrect_updates = list()
    for update in updates:
        if (not verify_update(update, rules)):
            incorrect_updates.append(update)
    return incorrect_updates

def get_applicable_rules(update, rules):
    a_rules = list()
    for rule in rules:
        try:
            idx1 = update.index(rule[0])
            idx2 = update.index(rule[1])
            a_rules.append(rule)
        except:
            continue
    return a_rules

def get_applicable_rules_page(update, rules, page):
    update_with_page = update.copy()
    update_with_page.append(page)
    a_rules = get_applicable_rules(update_with_page, rules)
    
    for rule in a_rules:
        if (rule[0] != page and rule[1] != page):
            a_rules.remove(rule)
    return a_rules

def get_relevant_pages(rules):
    pages = set()
    for rule in rules:
        pages.add(rule[0])
        pages.add(rule[1])
    return pages

# def fix_update_rule(update, rule):
#     if (verify_update_rule(update, rule)):
#         return update
#     print(f"applying rule: {rule} on {update}")
#     update.remove(rule[0])
#     update.insert(update.index(rule[1]), rule[0])
#     return update

def get_right_rules(rules, page):
    right_rules = list()
    for rule in rules:
        if (rule[1] == page):
            right_rules.append(rule[0])
    return right_rules

def get_left_rules(rules, page):
    left_rules = list()
    for rule in rules:
        if (rule[0] == page):
            left_rules.append(rule[1])
    return left_rules

def get_max_index(update, nums):
    max_ind = 0
    for n in nums:
        ind = update.index(n)
        if (ind > max_ind):
            max_ind = ind
    return max_ind

def get_min_index(update, nums):
    min_ind = len(update) - 1
    for n in nums:
        ind = update.index(n)
        if (ind < min_ind):
            min_ind = ind
    return min_ind

def fix_update(update, rules):
    a_rules = get_applicable_rules(update, rules)
    # print(f"Fixing {update} with {a_rules}")
    pages = update.copy()
    update.clear()
    for p in pages:
        # print(f"Inserting {p} into {update}")
        a_rules = get_applicable_rules_page(update, rules, p)
        if (len(a_rules) > 0):
            left_rules = get_left_rules(a_rules, p)
            right_rules = get_right_rules(a_rules, p)
            if (len(right_rules) > 0):
                max_ind = get_max_index(update, right_rules)
                update.insert(max_ind+1, p)
            else:
                min_ind = get_min_index(update, left_rules)
                update.insert(min_ind, p)
        else:
            update.append(p)
    return update

def fix_updates(updates, rules):
    fixed_updates = list()
    for update in updates:
        fixed_updates.append(fix_update(update, rules))
    return fixed_updates

def get_sum_middle_elt(updates):
    sum_middle = 0
    for update in updates:
        sum_middle += int(update[int(len(update)/2)])
    return sum_middle

def solution(input_data):
    order_rules, updates = process_input_data(input_data)
    return get_sum_middle_elt(verify_updates(updates, order_rules))

def solution2(input_data):
    order_rules, updates = process_input_data(input_data)
    incorrect_updates = get_incorrect_updates(updates, order_rules)
    # print(incorrect_updates)
    fixed_updates = fix_updates(incorrect_updates, order_rules)
    # print(fixed_updates)
    return get_sum_middle_elt(fixed_updates)
    
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
    print(solution2(data))
