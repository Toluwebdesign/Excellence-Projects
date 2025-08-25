WORDS={"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GAP": 3}
def main():
    print ("Welcome to Spelling Bee!")
    print ("Your letters are: A I P C R  H G")
   
    if len(WORDS)>0:
        print (f"{len(WORDS)} words left!")
        guess = input ("Guess a word: ")

    if guess in WORDS.keys():
        points = WORDS.pop(guess)
        print (f"Good job! You scored {points} points.")

    if guess == "GRAPHIC":
        WORDS.clear ()
        print ("You've won! You guessed the special word")
main()                 