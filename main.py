from datetime import datetime
import os

class DuplicateVisitorError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()

def get_last_visitor():
    if not os.path.exists(FILENAME):
        return None

    with open(FILENAME, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        return None

    last_line = lines[-1]
    name, timestamp = last_line.split(" | ")
    return name, timestamp

def add_visitor(visitor_name):
    last = get_last_visitor()

    # Duplicate visitor check only
    if last:
        last_name, _ = last
        if visitor_name == last_name:
            raise DuplicateVisitorError("Duplicate visitor not allowed")

    # Append visitor with timestamp
    timestamp = datetime.now().isoformat()
    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name} | {timestamp}\n")

def main():
    ensure_file()
    name = input("Enter visitor's name: ")
    try:
        add_visitor(name)
        print("Visitor added successfully!")
    except DuplicateVisitorError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
