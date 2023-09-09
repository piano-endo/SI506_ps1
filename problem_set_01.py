# START PROBLEM SET 1
print("Problem Set 1 \n")

# PROBLEM 01
print("\nPROBLEM 01")

# 1frita_batidos = "Frita Batidos"
# zingerman's Delicatessen = "Zingerman's Delicatessen"
# nypd = New York Pizza Depot
hopcat = "HoPcAT"
fleetwood_diner = "Fleetwood Diner"
# tomukun_noodle_bar = "Tomukun Noodle Bar
jerk_pit = "JaMAIcaN JERk PIt"
# mama satto = "Mama Satto"
hola_seoul = "Hola Seoul"
# @shalimar = "Shalimar"

cottage_inn = "Cottage Inn Pizza"
print(cottage_inn)

madras_masala = "Madras Masala"
print(madras_masala)

# PROBLEM 02
print("\nPROBLEM 02")

hopcat_all_lower = hopcat.lower()
print(f"all_lower: {hopcat_all_lower}")

jerk_pit_all_upper = jerk_pit.upper()
print(f"all_upper: {jerk_pit_all_upper}")

madras_masala_count_m = madras_masala.count('m')
print(f"number of letter m: {madras_masala_count_m}")

has_diner = fleetwood_diner.endswith("Diner")
print(has_diner)

starts_seoul = hola_seoul.startswith("Seoul")
print(starts_seoul)

comment = "Truly authentic Jamaican food&drinks"
updated_comment = comment.replace("&"," and ")
print(f"updated comment: {updated_comment}")

# PROBLEM 03
print("\nPROBLEM 03")

num_chars = len(updated_comment)
print(f"number of characters: {num_chars}")

restaurants = [
    "Frita Batidos",
    "Zingerman's Delicatessen",
    "New York Pizza Depot",
    "Hopcat",
    "Fleetwood Diner",
    "Tomukun Noodle Bar",
    "Jamaican Jerk Pit",
    "Mama Satto",
    "Hola Seoul",
    "Shalimar",
    "Cottage Inn Pizza",
    "Madras Masala",
]

print(type(restaurants))

num_restaurants = len(restaurants)
print(f"number of restaurants: {num_restaurants}")

# PROBLEM 04
print("\nPROBLEM 04")
plain_cheese_pizza = 18.99
garlic_knots = 6.99
soda = 7.00
oreo_cookie_shake = 10.49
white_pizza = 22.25
mozzarella_sticks = 17.99
total_price = (4*plain_cheese_pizza)+(5*garlic_knots)+(2*soda)+(5*oreo_cookie_shake)+(white_pizza)+(2*mozzarella_sticks)
print(f"total price: {total_price}")

total_bill = (total_price) + (total_price*0.06) + (total_price*0.15)
print(f"total bill: {total_bill}")

each_pay = total_bill/6

print(f"each person pays: {each_pay}")

# PROBLEM 05
print("\nPROBLEM 05")

# TODO: Create f-string
print(f"Someone said \'{updated_comment}\' on Yelp for the restaurant {jerk_pit_all_upper}.")

# PROBLEM 06
print("\nPROBLEM 06")

# TODO: Create multiline string
restaurants_multiline = """
{}
""".format("\n".join(restaurants))
print(restaurants_multiline)

# END PROBLEM SET
