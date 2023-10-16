def answer():
    print("\"y\" or \"n\"?")
    ans=input(">")
    while ans!="y" and ans!="n":
        print("\"y\" or \"n\"?")
        ans=input(">")
    return ans

print("Does it stand on four legs?")
ans=answer()
if ans=="y":
    print("Does it have spikes on its back?")
    ans=answer()
    if ans=="y":
        print("Does it have a club on its tail?")
        ans=answer()
        if ans=="y":
            print("Its an ankylosaurus.")
            print("Its a herbivore, so you are safe.")
        else:
            print("Its a stegosaurus.")
            print("Its a herbivore, so you are safe.")
    else:
        print("Does it have a long neck?")
        ans=answer()
        if ans=="y":
            print("Its a brachiosaurus.")
            print("It is a herbivore, so you are safe.")
        else:
            print("Its a triceratops.")
            print("It is a herbivore, so you are safe.")
else:
    print("Is it small?")
    ans=answer()
    if ans=="y":
        print("Its an raptor.")
        print("Its a carnivore, so you should run.")
    else:
        print("Does it have a fan shape on its back?")
        ans=answer()
        if ans=="y":
            print("Its a spinosaurus.")
            print("It is a carnivore, so you should run.")
        else:
            print("Its a t-rex.")
            print("It is a carnivore, so you should run.")
