import random

def game(comp,you):
    if comp==you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you == 'w':
            return False
        elif you == 's':
            return True

print("computer turn:snake(s),water(w)or(gun)g")

a = random.randint(1,3)
if a == 1:
    comp ='s'

elif a == 2:
    comp ='w'

elif a == 3:
    comp = 'g'

you = input("you chose snake(s),water(w)or gun(g)")

a = game(comp,you)
print(f"computer choose {comp}")
print(f"you choose {you}")

if a==None:
    print("you both take tie")

elif a:
    print("you win")

else:
    print("you losse")











































































