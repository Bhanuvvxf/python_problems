#Shape Classifier

#shape = ("circle",100)
#shape = ("rectangle",200,100)
#shape = ("square",100)
shape = ("hi")

match shape:
    case ("circle",x):
        print(f"It's a circle with radius {x} . ")
    case ("rectangle",x,y):
        print(f"It's a reactangle with width {x} and length {y} . ")
    case ("square",x):
        print(f"It's a square with side {x} . ")
    case _:
        print("Others.")