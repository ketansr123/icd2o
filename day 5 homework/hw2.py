walllength=float(input("What is the length of one of the 4 walls of your house? (meters)"))
wallwidth=float(input("What is the width of one wall outside your house"))
height=float(input("How high is your house in meters?"))
cost=float(input("How much does one brick cost?"))
bricklength=float(input("What is the length of one brick?"))
brickwidth=float(input("What is the width of one brick?"))
brickheight=float(input("What is the height of one brick?"))
totallength=walllength/bricklength
totalwidth=wallwidth/brickwidth
totalheight=height/brickheight
bricksneeded=totallength*totalwidth*totalheight
costofbricks=bricksneeded*cost
print(f"The amount of bricks needed is {bricksneeded} and the cost of the bricks needed is {costofbricks}")
