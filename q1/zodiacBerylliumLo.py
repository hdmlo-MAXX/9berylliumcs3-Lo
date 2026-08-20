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