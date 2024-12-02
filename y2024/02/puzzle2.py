###
# Day 2
###

def check_safe(report):
    if (len(report) < 2):
        return True
    if (report[0] == report[1]):
        return False
    incr = report[0] < report[1]
    print(f"{0}: {report[0]}")        
    if (incr):
        for i in range(len(report)-1):
            print(f"{i+1}: {report[i+1]}")
            if (report[i] == report[i+1]):
                return False
            if (report[i] > report[i+1]):
                return False
            if ((report[i+1] - report[i]) > 3):
                return False
    else:
        for i in range(len(report)-1):
            print(f"{i+1}: {report[i+1]}")
            if (report[i] == report[i+1]):
                return False
            if (report[i] < report[i+1]):
                return False
            if ((report[i] - report[i+1]) > 3):
                return False
    return True

def check_safe_damper(report):
    if (len(report) < 2):
        return True
    if (report[0] == report[1]):
        return problem_damper(report, 0)
    incr = report[0] < report[1]
    print(f"{0}: {report[0]}")
    if (incr):
        for i in range(len(report)-1):
            print(f"{i+1}: {report[i+1]}")
            if (report[i] == report[i+1]):
                return problem_damper(report, i)
            if (report[i] > report[i+1]):
                return problem_damper(report, i)
            if ((report[i+1] - report[i]) > 3):
                return problem_damper(report, i)
    else:
        for i in range(len(report)-1):
            print(f"{i+1}: {report[i+1]}")
            if (report[i] == report[i+1]):
                return problem_damper(report, i)
            if (report[i] < report[i+1]):
                return problem_damper(report, i)
            if ((report[i] - report[i+1]) > 3):
                return problem_damper(report, i)
    return True

def problem_damper(report, index):
    r1 = report.copy()
    r2 = report.copy()
    r3 = report.copy()
    r4 = report.copy()
    r1.pop(index)
    r2.pop(index+1)
    r3.pop(0)
    r4.pop(1)
    return (check_safe(r1) or check_safe(r2) or check_safe(r3) or check_safe(r4))

def num_safe(reports):
    num = 0
    for r in reports:
        if (check_safe(r)):
            num+=1
    return num
def num_safe_damper(reports):
    num = 0
    for r in reports:
        if (check_safe_damper(r)):
            num+=1
    return num

def read_input_levels():
    reports = []
    while (True):
        try:
            str_report = input().split()
            report = []
            for s in str_report:
                report.append(int(s))
            reports.append(report)
        except:
            break
    return reports

if (__name__ == '__main__'):
    reports = read_input_levels()
    print(num_safe_damper(reports))
    #print(check_safe_damper([10, 13, 11, 9, 6]))
    # while(True):
    #     reports = read_input_levels()
    #     print(num_safe_damper(reports))
