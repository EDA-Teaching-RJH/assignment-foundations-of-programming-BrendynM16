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

def main():
    # to load the data once at the start
    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu()
        
        if choice == "9":
            print("Exiting system.")
            break
        else:
            print("Feature coming soon...")

# This line runs the main function when i press Play
if __name__ == "__main__":
    main()
