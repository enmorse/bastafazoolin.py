# Created three classes to represent the restaurant
# Basta Fazoolin' with My Heart.

# One class to represent four different menus at four
# different times, a brunch menu, an early bird menu,
# a dinner menu, and a kids

# One class to represent the expansion of Basta Fazoolin'
# with My Heart and its growing franchise, and to present
# a string representation of each new installments address,
# as well as, the available menu at any given time.

# One class to represent a new business under the franchise
# of Basta Fazoolin' with My Heart named Take a’ Arepa
# with an entirely new menu and time of operation.

import datetime as dt


class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f'The {self.name} menu is avaliable from ' \
               f'{self.start_time:%I:%M %p} to {self.end_time:%I:%M %p}.'

    def calculate_bill(self, purchased_items):
        bill = 0

        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]

        return bill


class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f'The address is {self.address}'

    def available_menus(self, time):
        available_menus = []

        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)

        return available_menus


class Business:

    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return f'{self.name} {self.franchises}'


brunch_menu = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50,
}

b_start_time = dt.time(11, 00)
b_end_time = dt.time(16, 00)

# brunch_start_time = f'{b_start_time:%I:%M %p}'
# print(brunch_start_time)
# brunch_end_time = f'{b_end_time:%I:%M %p}'
# print(brunch_end_time)

# brunch = Menu('brunch', brunch_menu, brunch_start_time,
# brunch_end_time)
brunch = Menu('brunch', brunch_menu, b_start_time,
              b_end_time)
# print(brunch)

# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))


early_bird_menu = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
}

e_start_time = dt.time(15, 00)
e_end_time = dt.time(18, 00)

# early_bird_start_time = f'{e_start_time:%I:%M %p}'
# print(early_bird_start_time)
# early_bird_end_time = f'{e_end_time:%I:%M %p}'
# print(early_bird_end_time)

# early_bird = Menu('early bird', early_bird_menu,
# early_bird_start_time, early_bird_end_time)
early_bird = Menu('early bird', early_bird_menu,
                  e_start_time, e_end_time)
# print(early_bird)

# print(early_bird.calculate_bill(['salumeria plate',
# 'mushroom ravioli (vegan)']))


dinner_menu = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}

d_start_time = dt.time(17, 00)
d_end_time = dt.time(23, 00)

# dinner_start_time = f'{d_start_time:%I:%M %p}'
# print(dinner_start_time)
# dinner_end_time = f'{d_end_time:%I:%M %p}'
# print(dinner_end_time)

# dinner = Menu('dinner', dinner_menu, dinner_start_time,
# dinner_end_time)
dinner = Menu('dinner', dinner_menu, d_start_time, d_end_time)
# print(dinner)


kids_menu = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}

k_start_time = dt.time(11, 00)
k_end_time = dt.time(21, 00)

# kids_menu_start_time = f'{k_start_time:%I:%M %p}'
# print(kids_menu_start_time)
# kids_menu_end_time = f'{k_end_time:%I:%M %p}'
# print(kids_menu_end_time)

# kids = Menu('kids', kids_menu, kids_menu_start_time,
# kids_menu_end_time)
kids = Menu('kids', kids_menu, k_start_time, k_end_time)
# print(kids)


arepas_menu = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}

arepas_start_time = dt.time(10, 00)
arepas_end_time = dt.time(20, 00)

# arepas_menu_start_time = f'{arepas_start_time:%I:%M %p}'
# print(arepas_menu_start_time)
# arepas_menu_end_time = f'{arepas_end_time:%I:%M %p}'
# print(arepas_menu_end_time)

arepas = Menu('arepas', arepas_menu, arepas_start_time,
              arepas_end_time)
# print(arepas)

menus = [brunch, early_bird, dinner, kids, arepas]

flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street',
                            menus)

satellite_restaurants = [flagship_store, new_installment]

arepas_place = Franchise('189 Fitzgerald Avenue', menus)
# print(arepas_place)

# print(flagship_store.available_menus(dt.time(12, 00)))
# print(flagship_store.available_menus(dt.time(17, 00)))


businesses = Business('Basta Fazoolin\' with my Heart',
                      satellite_restaurants)
# print(businesses)

arepa_business = Business('Take a\' Arepa', [arepas_place])
print(arepa_business.franchises[0].menus[4])
