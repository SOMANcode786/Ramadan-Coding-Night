import random 
print("Guess the number between 50 and 100")
number =random.randrange(50,100)

chance :int =5

counter:int=0

while counter <chance:
    counter +=1
    guess =int(input("Enter you guess nmber :"))

    if guess==number :
        print("You win")
        
        break
    else:
        print("You lose")
        print(f"You have {chance-counter} chances left")
    if guess<number:
         print("Guess a higher number")
    else:
         print("Guess a lower number")   
    
if counter==chance:
    print("You lose")
    print(f"The number was {number}")





