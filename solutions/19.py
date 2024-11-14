days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sunday_count = 0

weekday = 1 #tuesday 1st jan 1901
year = 1901

for i in range(100):
    if year%4==0:
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    
    for month in days_in_month:
        weekday = (weekday + month)%7
        if weekday==6:
            sunday_count+=1
    year += 1

print(sunday_count)