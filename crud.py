# Simple CRUD program using Python

# In-memory data store (dictionary) to simulate a database
data_store = {}

def create_entry(key, value):
    """Create a new entry in the data store."""
    if key in data_store:
        print(f"Error: Entry with key '{key}' already exists.")
    else:
        data_store[key] = value
        print(f"Entry added: {key} -> {value}")

def read_entry(key):
    """Read an entry from the data store."""
    if key in data_store:
        print(f"Entry found: {key} -> {data_store[key]}")
    else:
        print(f"Error: Entry with key '{key}' not found.")

def update_entry(key, value):
    """Update an existing entry in the data store."""
    if key in data_store:
        data_store[key] = value
        print(f"Entry updated: {key} -> {value}")
    else:
        print(f"Error: Entry with key '{key}' not found.")

def delete_entry(key):
    """Delete an entry from the data store."""
    if key in data_store:
        del data_store[key]
        print(f"Entry deleted: {key}")
    else:
        print(f"Error: Entry with key '{key}' not found.")

def show_all_entries():
    """Show all entries in the data store."""
    if data_store:
        print("Current Entries:")
        for key, value in data_store.items():
            print(f"{key} -> {value}")
    else:
        print("Data store is empty.")

# Menu-driven interface
def menu():
    while True:
        print("\nChoose an operation:")
        print("1. Create Entry")
        print("2. Read Entry")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Show All Entries")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            create_entry(key, value)
        elif choice == '2':
            key = input("Enter key to read: ")
            read_entry(key)
        elif choice == '3':
            key = input("Enter key to update: ")
            value = input("Enter new value: ")
            update_entry(key, value)
        elif choice == '4':
            key = input("Enter key to delete: ")
            delete_entry(key)
        elif choice == '5':
            show_all_entries()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
