#AeroRelief
#Where roads end, we begin
#UN 17 goals of sustainabilty
#Zero hunger
#Clean water and sanitation
#ake drones that can carry supplies for people who cannot get food/supplies as easily, can make a app/website that people can enter their location in, and drones can come to that location to deliver supplies/food. There can be a building/structure that hosts this idea, and the people who need supplies can go to that structure and enter location and ask. People who are at a location can go to our website/app and enter their location in the app/website, and from there a map can pop up that shows the clean water locations, so people know where clean water is, and where to get it.
# AeroRelief - Free Food & Clean Water Assistance

# AeroRelief - Free Food & Clean Water Assistance System for People in Need
# AeroRelief - Free Food & Clean Water Assistance System for People in Need

import folium
import time
import random
import webbrowser
from folium import plugins

# Function to simulate loading process
def display_loading(message, duration=2):
    """Simulates a loading process with a given message."""
    print(f"{message}...", end="", flush=True)
    time.sleep(duration)
    print(" ✅")

# Function to generate and save the interactive map with water locations
def generate_map_with_highlighted_water_locations(location):
    """Generate a map and highlight water locations near the given location."""
    print(f"\n🗺️ Generating map for {location} with highlighted clean water locations...")

    # Set the initial location (default coordinates for Botswana as an example)
    map_location = [21.1454, 27.2118]  # Coordinates of Botswana (can be changed)

    # Create a Folium map centered around the given coordinates
    m = folium.Map(location=map_location, zoom_start=7)

    # Example water locations with coordinates (for simulation)
    water_locations = [
        {"name": "Community Water Station #1", "coordinates": (21.1454, 27.2118)},
        {"name": "Public Well #3", "coordinates": (21.1230, 27.2330)},
        {"name": "River Purification Site #2", "coordinates": (21.1100, 27.2450)},
        {"name": "Emergency Water Tank #7", "coordinates": (21.1550, 27.2200)},
        {"name": "Local Water Distribution Center", "coordinates": (21.1300, 27.2400)}
    ]

    # Add water locations as markers on the map
    for water_location in water_locations:
        folium.Marker(
            location=water_location["coordinates"],
            popup=water_location["name"],
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    # Save the map as an HTML file
    map_filename = "clean_water_map.html"
    m.save(map_filename)

    print("\n📍 Map for clean water in your area has been generated and saved as 'clean_water_map.html'.")
    print("📲 Open the map in your browser now! We'll also send you a link.")

    return map_filename

# Simulate sending the map link
def send_map_link():
    """Simulate sending the generated map link to the user."""
    map_filename = "clean_water_map.html"
    print(f"\n🌍 Your map is ready! You can open the map at any time.")
    print(f"🔗 Here's the link to your map: {map_filename}")
    webbrowser.open(map_filename)

# Main Program
print("🌍 Welcome to AeroRelief - Free Food & Clean Water Assistance")
print("💙 If you or someone you know cannot afford food or clean water, we are here to help.")
print("🚁 Our drones deliver essential supplies directly to those in need.")

# Get user location (simulated as Botswana, Africa for this example)
location = input("\n📍 Enter your location (e.g., Botswana, Africa): ").strip()
if not location:
    print("❌ Error: Location cannot be empty. Please restart and enter a valid location.")
    exit()

# Simulate generating and sending the map with clean water locations
generate_map_with_highlighted_water_locations(location)

# Ask if the user needs free food
food_request = input("\n🍽️ Would you like free food delivered to your location? (yes/no): ").strip().lower()

if food_request == "yes":
    diet = input("\n🥗 Are you vegetarian or non-vegetarian? (vegetarian/non-vegetarian): ").strip().lower()

    if diet not in ["vegetarian", "non-vegetarian"]:
        print("❌ Invalid input. Please restart and enter either 'vegetarian' or 'non-vegetarian'.")
        exit()

    food_options = {
        "vegetarian": {
            "1": "Vegetable Rice Bowl",
            "2": "Lentil Soup with Bread",
            "3": "Mixed Salad with Nuts",
            "4": "Vegan Pasta",
            "5": "Grilled Tofu with Vegetables"
        },
        "non-vegetarian": {
            "1": "Chicken and Rice Meal",
            "2": "Beef Stew with Bread",
            "3": "Fish with Vegetables",
            "4": "Egg Omelette with Toast",
            "5": "Grilled Chicken Wrap"
        }
    }

    print("\n📦 Free Food Options:")
    for key, value in food_options[diet].items():
        print(f"{key}. {value}")

    selected_food_items = []
    food_quantities = {}

    while True:
        food_choice = input("\nEnter the number of the food item you need (or type 'done' to finish): ").strip()
        if food_choice.lower() == "done":
            break
        elif food_choice in food_options[diet]:
            quantity = input(f"How many of {food_options[diet][food_choice]} would you like? ").strip()
            if quantity.isdigit() and int(quantity) > 0:
                selected_food_items.append(food_options[diet][food_choice])
                food_quantities[food_options[diet][food_choice]] = int(quantity)
                print(f"✅ {quantity} x {food_options[diet][food_choice]} added to your request.")
            else:
                print("❌ Invalid quantity. Please enter a positive number.")
        else:
            print("❌ Invalid selection. Please enter a valid number from the list above.")

    if not selected_food_items:
        print("❌ No valid selections made. Please restart to place a request.")
        exit()

    print("\n📦 Your selected free food items:")
    for item in selected_food_items:
        print(f"✅ {item} x {food_quantities[item]}")

# Additional support options
medical_supplies = input("\n🩹 Do you need basic medical supplies (bandages, medicine, first-aid)? (yes/no): ").strip().lower()
hygiene_kits = input("🧼 Would you like a free hygiene kit (soap, toothpaste, sanitary products)? (yes/no): ").strip().lower()

# Provide emergency shelter info
print("\n🏠 If you need a place to stay, here are nearby shelters:")
shelters = ["Hope Refuge Center", "Safe Haven Shelter", "Community Housing Support"]
for shelter in shelters:
    print(f"✅ {shelter}")

# Provide job assistance info
print("\n💼 Looking for work? These organizations provide job training for free:")
jobs = ["WorkStart Initiative", "Skill Up Program", "Hope Employment Services"]
for job in jobs:
    print(f"✅ {job}")

# Simulating AI demand prediction for food shortages
display_loading("📊 Analyzing supply needs in your area", 3)
if random.choice([True, False]):
    print("🚨 High demand detected! We are prioritizing urgent cases first.")
else:
    print("📦 You are in a low-demand zone. Your request will be processed soon.")

# Drone dispatch process
display_loading("🚁 Preparing your free delivery")
display_loading("🔄 Drone is being dispatched", 2)

eta = random.randint(10, 30)
print(f"📍 Estimated time of arrival: {eta} minutes.")

# Simulate real-time tracking updates
statuses = [
    "🚁 Drone has taken off and is en route.",
    "📡 Drone is flying over checkpoints.",
    "📍 Drone is nearing your location. Please be ready to receive your free food and supplies."
]

for status in statuses:
    time.sleep(5)
    print(status)

# Final delivery confirmation
display_loading("\n✅ Your free food and supplies have arrived", 3)
print("🙏 Thank you for using AeroRelief. We are always here for those in need.")

# Encourage community support
print("\n💙 Want to support AeroRelief?")
print("🍽️ Restaurants can donate extra food.")
print("🚀 Volunteers can help deliver in areas drones cannot reach.")
print("💰 Donations help expand our services to more people.")
print("\n🌍 AeroRelief - Bringing hope, one free meal at a time.")

# Send map link to the user (simulate the action of opening the map in the browser)
send_map_link()

# Add confirmation for the request and reiterate next steps
print("\n💡 Your request is confirmed! A drone is on its way to deliver the following items:")
print(f"Food: {selected_food_items}")
print(f"Quantities: {food_quantities}")
print("📍 We are also working on providing clean water assistance at the highlighted locations.")

# Ask if they need any further help or if they would like to contact a volunteer
help_request = input("\n🔧 Do you need further assistance or contact a volunteer? (yes/no): ").strip().lower()

if help_request == "yes":
    print("📝 We will connect you with a volunteer shortly!")
else:
    print("👍 Thank you for using AeroRelief!")

# Ending note
print("\n🌟 We are always here to help. AeroRelief is working tirelessly to provide assistance to those who need it most.")
