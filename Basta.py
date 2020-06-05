# Codecademy Basta Fazoolin' project

class Menu:
	# name = str, items = {str:float}, start_time = int, end_time = int
	def __init__(self, name, items, start_time, end_time):
		self.name=name
		self.items=items
		self.start_time=start_time
		self.end_time=end_time

	def __repr__(self):
		return("The {name} menu is available from {start}:00 until {end}:00.".format(name=self.name,start=self.start_time,end=self.end_time))

	def calculate_bill(self, purchased_items):
		total=0
		for item in purchased_items:
			total += self.items[item]
		return total


class Franchise:
	# address = str, menus = [Menu,...,...]
	def __init__(self, address, menus):
		self.address = address
		self.menus = menus

	def __repr__(self):
		return("This branch is at {address}".format(address=self.address))

	def available_menus(self,time):
		menu_list=[]
		for menu in self.menus:
			if time>=menu.start_time and time<=menu.end_time:
				menu_list.append(menu.name)
		return menu_list


class Business:
	# name = str, franchises = [Franchise,...,...]
	def __init__(self, name, franchises):
		self.name = name
		self.franchises = franchises

brunch = Menu("Brunch",{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},11,16)
early_bird = Menu("Early-bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00},15,18)
dinner = Menu("Dinner",{'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,},17,23)
kids = Menu("Kids",{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00},11,21)

#print(brunch)
#print(brunch.calculate_bill(["pancakes","home fries","coffee"]))
#print(early_bird.calculate_bill(["salumeria plate","mushroom ravioli (vegan)"]))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, kids, dinner])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, kids, dinner])

#print (flagship_store)
#print(flagship_store.available_menus(15))

basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Creating Arepa business needs menu, franchise, and business instances
arepas_menu = Menu("Arepas", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},10,20)
arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])
take_a_arepa = Business("Take a' Arepa",[arepas_place])