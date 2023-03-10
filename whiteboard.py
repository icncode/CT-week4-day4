#Write a function that prompts the user for their birth month(represented as a number), and returns their birthstone.
#If they input an invalid month, tell them to try again
#Note, you do not need to make 12 if statements to solve this problem

stones={
    1:"Garnet",
    2:"Amethyst",
    3:"Aquamarine",
    4:"Diamond",
    5:"Emerald",
    6:"Pearl",
    7:"Ruby",
    8:"Peridot",
    9:"Sapphire",
    10:"Opal",
    11:"Topaz",
    12:"Turquoise"
}

def birthstone():
    month = 13
    while month not in stones:
        month = int(input("Please input birth month number: "))
    return stones[month]

print(birthstone())