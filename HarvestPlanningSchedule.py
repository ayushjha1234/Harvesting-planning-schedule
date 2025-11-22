harvest_list = []
def add_crop():
    name = input("Enter crop name: ")
    date = input("Enter harvest date (DD-MM-YYYY): ")
    location = input("Enter field/location name: ")

    crop = {
        "name": name,
        "date": date,
        "location": location
    }
    harvest_list.append(crop)
    print("Crop added to harvest plan.\n")
def show_schedule():
    if not harvest_list:
        print("No crops in harvest plan.\n")
        return
    print("\n--- Harvest Schedule ---")
    for c in harvest_list:
        print("Crop:", c["name"])
        print("Harvest Date:", c["date"])
        print("Location:", c["location"])
        print("--------------------")
    print()
while True:
    print("1. Add Crop to Harvest Plan")
    print("2. View Harvest Schedule")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_crop()
    elif choice == "2":
        show_schedule()
    elif choice == "3":
        print("Exiting Harvest Planner.")
        break
    else:
        print("Invalid option.\n")
