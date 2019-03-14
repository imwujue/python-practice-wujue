year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))

months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
sum = 0
if 0 < month < 12:
    for i in range(0,month):
        sum = sum + months[i]
if 0 < day < months[month]:
    sum = sum + day
if (year%400 == 0) or (year%4==0 and year%400!=0):
    if month>2:
        sum += 1
print(sum)