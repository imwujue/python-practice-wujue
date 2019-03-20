s = input("the first letter:")
if s == "M":
    print("Monday")
elif s == "W":
    print("Wednesday")
elif s == "F":
    print("Friday")
elif s == "T" or s == "S":
    c = input("the second letter:")
    if s == "T":
        if c == "u":
            print("Tuesday")
        elif c == "h":
            print("Thirday")
        else:
            print("error!")
    elif s == "S":
        if c == "a":
            print("Saturday")
        elif c == "u":
            print("Sunday")
        else:
            print("error!")
else:
    print("error!")