weather = input("Give weather: ")
time_of_the_day ="night"

if weather == "sunny":
    if time_of_the_day == "day":
        print("play with car")
    else:
        print("play video games")

elif weather == "rainy":
    print("play with paper boat")

elif weather == "snowy":
    if time_of_the_day == "night":
        print("play with teddybear")
    else:
        print("play with snowman")

else:
    print("go to bed")

#print("enjoy the weekend")