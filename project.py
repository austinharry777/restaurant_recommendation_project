from restaurantData import restaurant_data, types

import time #for sleep function

#dictionary comprehension of restaurant_data with keys of 'type', 'name', 'rating', 'price', 'address'
restaurant_dict = {i[0]:{'name':i[1], 'rating':i[2], 'price':i[3], 'address':i[4]} for i in restaurant_data}

run = True

def main_program():
    print("Welcome to Austin's Restaurant Database!")
    while run:
        print("1. Search by type of food")
        print("2. Search by name")
        print("3. Search by rating")
        print("4. Search by price")
        print("5. Search by address")
        print("6. Quit")
        choice = input("Enter a number: ")
        if choice == "1":
            select_type_of_food()
        elif choice == "2":
            select_name()
        elif choice == "3":
            select_rating()
        elif choice == "4":
            select_price()
        elif choice == "5":
            select_address()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")
            time.sleep(1)
            main_program()

def select_type_of_food():
    #select a type of restaurant with only a few letters
    type_of_food = input("Enter a type of food: ")
    type_of_food = type_of_food.lower()
    matching_types = []
    for i in types:
        if i.startswith(type_of_food):
            matching_types.append(i)
    if matching_types:
        print("Here are the restaurants of types containing", type_of_food)
        for i in restaurant_data:
            if i[0] in matching_types:
                data_presentation(i)
        

    else:
        print("No types found containing", type_of_food)
        print("------------------------")
        select_type_of_food()
    
    more()

def select_name():
    #select a restaurant name with only a few letters
    name = input("Enter a name: ")
    name = name.lower()
    matching_names = []
    for i in restaurant_data:
        if i[1].lower().startswith(name):
            matching_names.append(i[1])
    if matching_names:
        print("Here are the restaurants of names containing", name)
        for i in restaurant_data:
            if i[1] in matching_names:
                data_presentation(i)
                more()
    else:
        print("No names found containing", name)
        print("------------------------")
        select_name()

    more()

def select_rating():
    #select a rating
    rating = input("Enter a rating from 1 to 5: ")
    matching_ratings = []
    for i in restaurant_data:
        if i[2] == rating:
            matching_ratings.append(i[2])
    if matching_ratings:
        print("Here are the restaurants of ratings", rating)
        for i in restaurant_data:
            if i[2] in matching_ratings:
                data_presentation(i)
                
    else:
        print("No ratings found", rating)
        print("------------------------")
        select_rating()

    more()

def select_price():
    #select a price
    price = input("Enter a price from 1 to 5: ")
    matching_prices = []
    for i in restaurant_data:
        if i[3] == price:
            matching_prices.append(i[3])
    if matching_prices:
        print("Here are the restaurants of prices", price)
        for i in restaurant_data:
            if i[3] in matching_prices:
                data_presentation(i)
                
    else:
        print("No prices found", price)
        print("------------------------")
        select_price()

    more()

def select_address():
    #select an address with only a few letters
    address = input("Enter an address: ")
    address = address.lower()
    matching_addresses = []
    for i in restaurant_data:
        if i[4].lower().startswith(address):
            matching_addresses.append(i[4])
    if matching_addresses:
        print("Here are the restaurants of addresses containing", address)
        for i in restaurant_data:
            if i[4] in matching_addresses:
                data_presentation(i)
                
    else:
        print("No addresses found containing", address)
        print("------------------------")
        select_address()

    more()

def data_presentation(i):
#print the data in a nice way
    print(f"------------------------------\nType of food: {i[0].title()} \nRestaurant Name: {i[1]} \nRating: {i[2]} \nPrice: {i[3]} \nAddress: {i[4]}\n------------------------------")
    
def more():   
    choice = input("Would you like to see more? Press enter to continue or type 'q' to quit: ")
    if choice == "q":
        print("Goodbye!")
        exit()
        
main_program()

