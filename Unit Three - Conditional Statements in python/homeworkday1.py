def caught_speeding(speed, is_birthday):  #1
    if is_birthday:
        speed=speed-5
    if speed<=60:
        return "no"
    if 61<=speed<80:
        return "Small Ticket"
    return "Big Ticket"

mph=int(input("What speed were you going:"))
print(caught_speeding(mph, True))



#3
def squirrel_play(temp, is_summer):
    if is_summer:
        if 60<=temp<=100:
            return True
        else:
            return False
    elif 60<=temp<=90:
            return True
    else:
            return False
