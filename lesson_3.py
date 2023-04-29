# First Assignment Boolean logic & Iterative Programming
#1. program for recommendation according to the weather forecast 

weather = int(input("How much is the todays' temperature in celcius? "))

if weather <= 6:
    print ("You should wear a pair of gloves")

elif weather <= 8:
    print ("You should wear your hat")

elif weather <= 10:
    print ("You should wear a scarf")

elif weather <= 12:
    print("Today you should wear a Jacket")

elif weather <= 25:
    print ("weather looks good")

else :
    print ("You should wear sunglasses")



# second method-  program for recommendation according to the weather forecast 

weather_S = int(input("How much is the todays' temperature in celcius? "))

if weather_S <=6:
     print ("You should wear a pair of gloves")

elif weather_S >6 and weather_S <= 8:
    print ("You should wear your hat")

elif weather_S >8 and weather_S <= 10:
    print ("You should wear a scarf")

elif weather_S > 10 and weather_S <=12:
    print ("Today you should wear a Jacket")

elif weather_S >12 and weather_S <= 25:
    print ("weather looks good")

else:
    print("You should wear sunglasses")



# 2. program for the probability of rain

rain = int(input("what is the probability of raining today? "))

if rain <50 :
    print ("No need to take your umbrella ")

elif rain >=50 and rain <100:
    print ("Its better to take umbrella")

elif rain == 100:
    print ("Definetly Take your umbrella ")

else: 
    print("wrong probability")
