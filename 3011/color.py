"""Color"""

c1 = input()
c2 = input()

if {c1 , c2} == {"Red", "Yellow"}:
    print("Orange")
elif {c1 , c2} == {"Red" , "Blue"}:
    print("Violet")
elif {c1 , c2} == { "Yellow" , "Blue"}:
    print("Green")
elif {c1 , c2} == { "Red"}:
    print("Red")
elif {c1 , c2} == { "Yellow"}:
    print("Yellow")
elif {c1 , c2} == { "Blue"}:
    print("Blue")
else:
    print("Error")
