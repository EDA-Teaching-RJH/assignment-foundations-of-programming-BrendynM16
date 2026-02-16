def init_database():
    """ Returns 4 lists pre-populated with initial data."""
    # These are my Parallel Lists, th index 0 in 'names' corresponds to Index 0 in 'ranks', etc.
    names = ["Jean-Luc Picard", "William Riker", "Data", "Geordi La Forge", "Deanna Troi"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lt. Commander", "Commander"]
    divs = ["Command", "Command", "Operations", "Engineering", "Sciences"]
    ids = ["1001", "1002", "1003", "1004", "1005"]
    return names, ranks, divs, ids

def display_menu():
    print("\n--- FLEET MANAGEMENT SYSTEM ---")
    print("1. Display Roster")
    print("2. Add Member")
    print("3. Remove Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    return input("Select Option: ")

def display_roster(names, ranks, divs, ids):
    print(f"{'ID':<6} {'Name':<20} {'Rank':<15} {'Division':<15}")
    print("-" * 60)
    # i will use range(len(names)) so 'i' represents the row number (0, 1, 2...) like that...
    for i in range(len(names)):
        print(f"{ids[i]:<6} {names[i]:<20} {ranks[i]:<15} {divs[i]:<15}")

def add_member(names, ranks, divs, ids):
    new_id = input("Enter new ID: ")
    
    if new_id in ids:
        print("Error: ID already exists.")
        return

    # We must append to All 4 lists to keep them parallel
    names.append(input("Enter Name: "))
    ranks.append(input("Enter Rank: "))
    divs.append(input("Enter Division: "))
    ids.append(new_id)
    print("Crew member added.")

def remove_member(names, ranks, divs, ids):
    target_id = input("Enter ID to remove: ")
    
    if target_id in ids:
        idx = ids.index(target_id)
        
        # Remove that index from alll lists
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Crew member removed.")
    else:
        print("ID not found.")

def update_rank(names, ranks, ids):
    target_id = input("Enter ID to update: ")
    if target_id in ids:
        idx = ids.index(target_id)
        print(f"Current rank for {names[idx]}: {ranks[idx]}")
        ranks[idx] = input("Enter new rank: ")
        print("Rank updated.")
    else:
        print("ID not found.")

def search_crew(names, ranks, divs, ids):
    term = input("Enter search term: ").lower()
    found = False
    print("\n--- Search Results ---")
    for i in range(len(names)):
        if term in names[i].lower():
            print(f"{ids[i]} - {names[i]} ({ranks[i]})")
            found = True
    if not found:
        print("No matches found.")

def filter_by_division(names, divs):
    target_div = input("Enter Division to filter (Command, Operations, Sciences): ")
    print(f"\n--- {target_div} Division ---")
    found = False
    for i in range(len(names)):
        if divs[i].lower() == target_div.lower():
            print(f"{names[i]}")
            found = True
    if not found:
        print("No crew found in that division.")

def calculate_payroll(ranks):
    total = 0
    for r in ranks:
        if r == "Captain":
            total += 1000
        elif r == "Commander":
            total += 800
        elif r == "Lt. Commander":
            total += 600
        elif r == "Lieutenant":
            total += 400
        elif r == "Ensign":
            total += 200
        else:
            total += 100
    print(f"Total Monthly Payroll: {total} Credits")

def count_officers(ranks):
    count = 0
    for r in ranks:
        if r == "Captain" or r == "Commander":
            count += 1
    print(f"Total High-Ranking Officers: {count}")

def main():
    # to load the data once at the start
    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu()
        
        if choice == "1":
            display_roster(names, ranks, divs, ids)
        elif choice == "2":
            add_member(names, ranks, divs, ids)
        elif choice == "3":
            remove_member(names, ranks, divs, ids)
        elif choice == "4":
            update_rank(names, ranks, ids)
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
        elif choice == "6":
            filter_by_division(names, divs)
        elif choice == "7":
            calculate_payroll(ranks)
        elif choice == "8":
            count_officers(ranks)
        elif choice == "9":
            print("Exiting system.")
            break
        else:
            print("Invalid option.")

# This line runs the main function when i press Play
if __name__ == "__main__":
    main()
