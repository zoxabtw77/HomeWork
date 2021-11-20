hrs = int(input('enter hours: '))
mins = int(input('enter minutes: '))
delta = int(input('enter delta hours: '))

if hrs >= 0 and 0 <= mins <= 59:
    new_hrs = (hrs + delta) % 24
    if new_hrs <= 9: new_hrs = '0' + str(new_hrs)
    if mins <= 9: mins = '0' + str(mins)
    print(f'{new_hrs}:{mins}') 