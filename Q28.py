def count(age,num):
    if num == 1:
        return age
    else:
        return count(age,num-1)+2

print(count(10,5))