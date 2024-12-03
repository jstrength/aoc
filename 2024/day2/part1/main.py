input = open("big_input.txt")
reports = []
for line in input:
    reports.append(list(map(int, line.split())))

safe_reports_count = 0
for report in reports:
    is_increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            break
        if is_increasing:
            if report[i] > report[i + 1]:
                break
        else:
            if report[i] < report[i + 1]:
                break
        if i == len(report) - 2:
            safe_reports_count += 1

print(safe_reports_count)
