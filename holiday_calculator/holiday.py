#intro:
input("Welcome to my holiday calculator\nPress 'ENTER' to calculate your holiday cost:- ")

#all cities and respective prices:
cities = {"london": 250,
          "madrid": 175,
          "jeddah": 335,
          "california": 415,
          "tokyo": 510
          }


#get user inputs for:

#city flying to:
while True:
    try:
        city_flight = input("""
London: £250
Madrid: £175
Jeddah: £335
California: £415
Tokyo: £510

Please choose your flight from the list above:-""").lower()
        
        if city_flight in cities:
            break
        else:
            raise ValueError
    except:
        print("ERROR, NOT A VALID CITY")

#number of nights staying at hotel:
print("\nHotel cost: £150 per night")
while True:
    try:
        num_nights = int(input("Please enter the number of nights you will be staying at your hotel:- "))
        if num_nights >= 0:
            break
        else: 
            raise ValueError
    except:
        print("ERROR, NOT A VALID NUMBER\n")

#number of days taking rental:
print("\nCar rental cost: £19 per day")
while True:
    try:
        rental_days = int(input("Please enter the number of days that you will be hiring a car for:- "))
        if rental_days >= 0:
            break
        else: 
            raise ValueError
    except:
        print("ERROR, NOT A VALID NUMBER\n")

#caculate costs:
def hotel_cost(num):
    return 150*num 

def plane_cost(city):
    return cities[city] 

def car_rental(num):
    return 19*num 

def holiday_cost():
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total 

#main:
print(f"""
----------------------------------------------
Holiday cost breakdown:

Flight:
Destination; {city_flight}
Price; £{plane_cost(city_flight)}

Hotel:
Number of nights; {num_nights}
Price; £{hotel_cost(num_nights)}

Car rental:
Number of days; {rental_days}
Price; £{car_rental(rental_days)}

Total holiday cost: £{holiday_cost()}
----------------------------------------------
""")