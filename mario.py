import time
print("""Answer all questions with either Y or N.
    Please pick a character out of:
    -Mario
    -Luigi
    -Waluigi
    -Toad
    -Koopa
    -Goomba""")
found=False
fail=False
count=1
while found==False:
    answer=input("Is your character a human? ")
    if answer=="y":
        answer=input("Is your character red? ")
        if answer=="y":
            print("Your character is Mario")
            found=True
        elif answer=="n":
            answer=input("Is your character green? ")
            if answer=="y":
                print("Your character is Luigi")
                found=True
            elif answer=="n":
                print("Your character is Waluigi")
                found=True
    elif answer=="n":
        answer=input("Is your character red? ")
        if answer=="y":
            print("Your character is Toad")
            found=True
        elif answer=="n":
            answer=input("Is your character green? ")
            if answer=="y":
                print("Your character is Koopa")
                found=True
            elif answer=="n":
                print("Your character is Goomba")
                found=True
    if found==False and count>20:
        print("I\'ve had enough.")
        for i in range(5,0,-1):
            print(i)
        found==True
        fail=True
    elif found==False and count>10:
        print("Stop.")
        count=count+1
    elif found==False and count>3:
        print("y or n.")
        count=count+1
    elif found==False:
        print("Answer with a y (yes) or n (no).")
        count=count+1
if count>3 and fail==False:
    print("It only took",count,"attempts to follow simple instructions!")
elif fail==False:
    input()