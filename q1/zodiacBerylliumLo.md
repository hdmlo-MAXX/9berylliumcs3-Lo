## Chinese Zodiac

**Instructions**

Create a zodiacSectionLN.py file.  This file will contain your solutions to the requirements below:

a. Ask the user to enter a year of birth.  The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.
d. Otherwise determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.
e. CONSIDER only the year of birth.

---

## Python Code ('zoidiacBerylliumLo.py')

try:
    year = int(input("Enter your birth year: "))
    
except ValueError:
    print("Invalid Year, please enter a number.")
    exit()

if year < 1900:
    print("Invalid Year, it should be a year greater than or equal to 1900.")
    exit()

index = (year - 1900) % 12

zodiac = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

print(f"Your Chinese Zodiac Sign is: {zodiac[index]}")

---

