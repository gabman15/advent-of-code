###
# Day 1
###

def get_total_dist(list1, list2):
    slist1 = sorted(list1)
    slist2 = sorted(list2)
    dist = 0;
    for i in range(len(slist1)):
        dist = dist + abs(slist1[i] - slist2[i])
    return dist

def read_input_lists():
    list1 = []
    list2 = []
    while (True):
        try:
            x,y = input().split()
            list1.append(int(x))
            list2.append(int(y))
        except:
            break;
    return (list1,list2)

def times_appears(num, check_list):
    times = 0
    for i in check_list:
        if (num == i):
            times+=1
    return times

def find_similarity(list1, list2):
    similarity = 0
    for i in list1:
        similarity += (i * times_appears(i, list2))
    return similarity

if (__name__ == '__main__'):
    tlist1 = [3,4,2,1,3,3]
    tlist2 = [4,3,5,3,9,3]
    sim = find_similarity(tlist1,tlist2)
    print("test sim: " + str(sim))
    (list1, list2) = read_input_lists()
    sim = find_similarity(list1,list2)
    print("real sim: " + str(sim))
    
