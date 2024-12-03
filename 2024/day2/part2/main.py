input = open("big_input.txt")
reports = []
for line in input:
    reports.append(list(map(int, line.split())))

def check_report(report):
    is_increasing = report[0] < report[1]
    #print(report)
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
        if is_increasing:
            if report[i] > report[i + 1]:
                return False
        else:
            if report[i] < report[i + 1]:
                return False
    return True

safe_reports_count = 0
for report in reports:
    for i in range(len(report)):
        if check_report(report[:i] + report[i+1:]):
            safe_reports_count += 1
            break

print(safe_reports_count)
