alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m",
          "n","o","p","q","r","s","t","u","v","w","x","y","z",]
#It is encoded and decoded the same way

word=input("What would you like to encode/decode?") 
encode="" 
for i in range(0,len(word)):#Starts a loop that is the length of the
    convert=False           #word to go through each letter individually
    count=0
    while convert==False:  #loops until the current letter is either:
        print(count)       
        wordb=word[i].lower()
        if count==26:    #Not found, just adding the original letter 
            convert=True #to encode or,
            encode=encode+word[i]
        elif wordb==alphabet[count]: #It is found. This adds 13 to the current 
            convert=True             #count and if the total is over 25, subtracts
            new=count+13             #26 from it to prevent index errors. it then
            if new>25:               #finds the letter in the alphabet variable
                new=new-26
            letter=alphabet[new]
            if word[i].isupper():      #If the original letter is uppercase,
                letter=letter.upper()  #makes the new letter uppercase.
            encode=str(encode)+str(letter)
        elif wordb!=alphabet[count]: #if not found and not at 26, loops
            count=count+1            #and adds 1 to counter 
            print(wordb)
print(encode)
