# Episode 8: Project - Personal Diary App
# Using file handling to build a diary that saves your entries!

import json
import os
from datetime import datetime

def load_diary():
    """Load diary entries from file"""
    if os.path.exists("diary.json"):
        try:
            with open("diary.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    return []

def save_diary(entries):
    """Save diary entries to file"""
    with open("diary.json", "w") as file:
        json.dump(entries, file, indent=4)

def add_entry(entries):
    """Add a new diary entry"""
    print("\n=== NEW DIARY ENTRY ===")
    title = input("Enter title: ")
    content = input("Enter your thoughts: ")
    
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "title": title,
        "content": content
    }
    
    entries.append(entry)
    save_diary(entries)
    print("Entry saved successfully!")

def view_entries(entries):
    """View all diary entries"""
    if not entries:
        print("\nNo entries found. Start writing!")
        return
    
    print("\n=== YOUR DIARY ===")
    for i, entry in enumerate(entries, 1):
        print(f"\n{i}. {entry['title']}")
        print(f"   Date: {entry['date']}")
        print(f"   {entry['content']}")
        print("-" * 50)

def view_recent(entries, count=5):
    """View recent entries"""
    if not entries:
        print("\nNo entries found.")
        return
    
    recent = entries[-count:]  # Last N entries
    print(f"\n=== RECENT {count} ENTRIES ===")
    for i, entry in enumerate(recent, 1):
        print(f"\n{i}. {entry['title']}")
        print(f"   Date: {entry['date']}")
        print(f"   {entry['content'][:50]}...")  # First 50 characters
        print("-" * 50)

def search_entries(entries):
    """Search entries by keyword"""
    if not entries:
        print("\nNo entries to search.")
        return
    
    keyword = input("\nEnter keyword to search: ").lower()
    found = []
    
    for entry in entries:
        if keyword in entry["title"].lower() or keyword in entry["content"].lower():
            found.append(entry)
    
    if found:
        print(f"\nFound {len(found)} entry/entries:")
        for i, entry in enumerate(found, 1):
            print(f"\n{i}. {entry['title']}")
            print(f"   Date: {entry['date']}")
            print(f"   {entry['content']}")
            print("-" * 50)
    else:
        print(f"No entries found with keyword '{keyword}'")

def delete_entry(entries):
    """Delete a diary entry"""
    if not entries:
        print("\nNo entries to delete.")
        return
    
    view_entries(entries)
    try:
        index = int(input("\nEnter entry number to delete: ")) - 1
        if 0 <= index < len(entries):
            deleted = entries.pop(index)
            save_diary(entries)
            print(f"Entry '{deleted['title']}' deleted!")
        else:
            print("Invalid entry number!")
    except ValueError:
        print("Please enter a valid number!")

def export_to_text(entries):
    """Export diary to a text file"""
    if not entries:
        print("\nNo entries to export.")
        return
    
    filename = input("Enter filename (e.g., my_diary.txt): ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    with open(filename, "w") as file:
        file.write("=== PERSONAL DIARY ===\n\n")
        for entry in entries:
            file.write(f"Date: {entry['date']}\n")
            file.write(f"Title: {entry['title']}\n")
            file.write(f"Content: {entry['content']}\n")
            file.write("-" * 50 + "\n\n")
    
    print(f"Diary exported to {filename}!")

def diary_app():
    """Main diary application"""
    print("=== PERSONAL DIARY APP ===")
    print("Your thoughts, saved forever!")
    
    entries = load_diary()
    
    while True:
        print("\nOptions:")
        print("1. Add new entry")
        print("2. View all entries")
        print("3. View recent entries")
        print("4. Search entries")
        print("5. Delete entry")
        print("6. Export to text file")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ")
        
        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            view_recent(entries)
        elif choice == "4":
            search_entries(entries)
        elif choice == "5":
            delete_entry(entries)
        elif choice == "6":
            export_to_text(entries)
        elif choice == "7":
            print("Goodbye! Your diary is saved.")
            break
        else:
            print("Invalid choice! Try again.")

# Run the diary app
if __name__ == "__main__":
    diary_app()
