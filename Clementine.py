from time import sleep
from colorama import colorama_text

# D = Decision
# S1D = Season 1 Decision
# S2D = Season 2 Decision
# S3D = Season 3 Decision
# S4D = Season 4 Decision

S1D1 = int(0)
S1D2 = int(0)
S2D1 = int(0)
S2D2 = int(0)
S3D1 = int(0)
S3D2 = int(0)
S4D1 = int(0)
S4D2 = int(0)
choicesimported = int(0)
cachoicesimported = int(0)


while True:
    print("CLEMENTINE & AJ")
    print("Episode 1: Where The Flowers Grow")

    D = ("0")
    while True:
        D1 = input("""
0: Info
1: Import Choices
2: Credits
3: Start
                

{: """)
        print("_________________________________________________________________________")
        print(" ")
        if D1 == ("2"):
            print("test")
            print("_________________________________________________________________________")
            print(" ")
        if D1  == ("3"):
            print("{:Start")
            print("A 21 year old clementine sits on the back of a worn bunk ")
            input(" ")
            while True:
                print("You are going on a trip. You can only have space for one item. What do you grab for AJ?")
                print("1: Disco Toys")
                print("2: Coloring Book")
                print("3: Comic Book")
                print("4: Dictionary")
                print(" ")
                print("_________________________________________________________________________")
                print(" ")
                S4D1 = input("{: ")
                print(" ")
                print("_________________________________________________________________________")
                print(" ")
                S4D1 = int(S4D1)
                if S4D1 == (1):
                    print(" ")
                    print("Your Story Is Changing...")
                    print("_________________________________________________________________________")
                    print(" ")
                    print("Clementine: AJ needs something to play with. Hopefully its not too childish for him. ")
                    print("_________________________________________________________________________")
                    print(" ")
                    break
                if S4D1 == (2):
                    print(" ")
                    print("Your Story Is Changing...")
                    print("_________________________________________________________________________")
                    print(" ")
                    print("Clementine: He'll like this one. Hes come so far as an artist. Just like Tenn... ")
                    print("_________________________________________________________________________")
                    print(" ")
                    break
                if S4D1 == (3):
                    print(" ")
                    print("Your Story Is Changing...")
                    print("_________________________________________________________________________")
                    print(" ")
                    print("Clementine: AJ always liked the superheroes in this one.")
                    print("_________________________________________________________________________")
                    print(" ")
                    break
                if S4D1 == (4):
                    print(" ")
                    print("Your Story Is Changing...")
                    print("_________________________________________________________________________")
                    print(" ")
                    print("Its good for him to practice his words. Hope it's not too boring for him...")
                    print("_________________________________________________________________________")
                    print(" ")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")
                print("")
            print("Clementine; Alright. It's finally time to head out")

                
                    
                    

        if D1 == ("0"):
            print("{:Info")
            print("""
Clementine & AJ
                  
Episode 1: Where The Flowers Grow
                  
I cant add costum decision for every decision in season 4 unfortuantly. The assumed lore is James Dying, And Luis/Violet surviving and Tenn dying
                  
                  
There is no cloud saving. its reccomended to do each episode in one sitting.
                  
                  
Clem & AJ set off on settling old bussiness.""")
            print("_________________________________________________________________________")
            print(" ")
        if D1 == ("1"):
            print("{:Import Choices")


            print("_________________________________________________________________________")
            print(" ")
            while True:
                S1D1 = input("""In Season 1, did Lee grab christa or omids hand?
1: Omid
2: Christa
            
 
{: """)
                S1D1 = int(S1D1)
                if S1D1 == (1) or S1D1 == (2):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")
            print("_________________________________________________________________________")
            print(" ")
            while True:
                S1D2 = input("""Did you Shoot, or leave Lee?
1: Shoot
2: Leave
 
 
{: """)
                S1D2 = int(S1D2)
                if S1D2 == (1) or S1D2 == (2):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")
            print("_________________________________________________________________________")
            print(" ")
 
            print("_________________________________________________________________________")
            print(" ")
            while True:
                S2D1 = input("""Did you distract, or run away from the scavangers surronding Christa in Season 2?
1: Distract
2: Run Away
 
 
{: """)
                S2D1 = int(S2D1)
                if S2D1 == (1) or S2D1 == (2):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")

            print("_________________________________________________________________________")
            print(" ")
            print("_________________________________________________________________________")
            print(" ")
            while True:
                S2D2 = input("""What ending did you get in Season 2?
1: Wellington
2: Kenny
3: Jane
4: Alone
                         
                         
{: """)
                S2D2 = int(S2D2)
                if S2D2 == (1) or S2D2 == (2) or S2D2 == (3) or S2D2 == (4):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")

            print("_________________________________________________________________________")
            print(" ")
            while True:
                S3D1 = input("""Who lived at the end of Season 3?
1: Gabe
2: Kate
3: Gabe & David
4: Kate & David
5: Gabe & Kate
                         
                         
{: """)
                S3D1 = int(S3D1)
                if S3D1 == (1) or S3D1 == (2) or S3D1 == (3) or S3D1 == (4) or S3D1 == (5):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")

            print("_________________________________________________________________________")
            print(" ")
            while True:
                S3D2 = input(""" Who survived in season 3?
1: Lingard & Max & Conrad
2: Lingard & Max
3: Lingard & Conrad
4: Max & Conrad
5: Max
6: Conrad
7: Lingard
8: Nobody

                         
{: """)
                S3D2 = int(S3D2)
                if S3D2 == (1) or S3D2 == (2) or S3D2 == (3) or S3D2 == (4) or S3D2 == (5) or S3D2 == (6) or S3D2 == (7) or S3D2 == (8):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")

            print("_________________________________________________________________________")
            print(" ")
            while True:
                S4D1 = input("""What did you teach Aj the best?
1: Family
2: Survival
3: Voice
4: Happiness
                         
                         
{: """)
                S4D1 = int(S4D1)
                if S4D1 == (1) or S4D1 == (2) or S4D1 == (3) or S4D1 == (4):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")

            print("_________________________________________________________________________")
            print(" ")
            while True:
                S4D2 = input("""Did Lilly live at the end of season 4?
1: Yes.
2: No
                         
                         
{: """)
                S4D2 = int(S4D2)
                if S4D2 == (1) or S4D2 == (2):
                    print(" ")
                    print("Correct")
                    print("_________________________________________________________________________")
                    break
                else:
                    print(" ")
                    print("Invalid Input")
                    print("_________________________________________________________________________")

            print("_________________________________________________________________________")
            print(" ")
            print("All Decisions Imported. Generating Unique Code Now...")
            sleep(1)
            print("Keep sure to save this code!")
            sleep(4)
            choicesimported = S1D1 + S1D2*10 + S2D1*100 + S2D2*1000 + S3D1*10000 + S3D2*100000 + S4D1*1000000 + S4D2*10000000
            choicesimported = int(choicesimported)
            print("_________________________________________________________________________")
            print(" ")
            print("Your Past Decisions Code Is: ")
            print(choicesimported)
            sleep(4)
            print(" ")
            print("Directing back to main menu...")
            print("_________________________________________________________________________")
            print(" ")