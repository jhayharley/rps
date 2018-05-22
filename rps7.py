print("""___hello welcome___""")

p1 = int(input("What is player 1's request \n\n\n\n"))
p2 = int(input("What is player 2's request \n\n\n\n"))
cho = list([1,2,3])
ko = list([5,6,4])

if cho.index(p1) == ko.index(p2):
    print("Draw")

if cho.index(p1) == (ko.index(p2) +1)%3:
    print("Player 2 wins")

if ko.index(p2) == (cho.index(p1) +1)%3:
    print("Player 1 wins")

if p1 not in cho or p2 not in ko:
    print("Invalid Value")