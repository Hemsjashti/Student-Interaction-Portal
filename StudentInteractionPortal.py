# Student Interaction Portal 
# ---------------------------------------------
# DATA STORAGE
# ---------------------------------------------
accounts = {}

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

academics = {
    "CSE": ["DSA", "Python", "DBMS"],
    "ECE": ["Circuits", "Signals", "Embedded Systems"],
    "MECH": ["Thermodynamics", "Fluid Mechanics", "Manufacturing"]
}

clubs = [
    "Robotics Club",
    "NrithyaSparsh",
    "Saptaswara",
    "Chakravyuha",
    "Avinya",
    "Drishya",
    "Prachurya",
    "Relu"
]

events = [
    ("Tech Fest", "January"),
    ("Sports Meet", "February"),
    ("Cultural Night", "March")
]

seniors = {
    "Rahul": "CSE",
    "Ananya": "ECE",
    "Vikram": "MECH"
}


# ---------------------------------------------
# FILE HANDLING
# ---------------------------------------------
def load_accounts():
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    username, password = line.split(",", 1)
                    accounts[username] = password
    except FileNotFoundError:
        pass


def save_accounts():
    with open("accounts.txt", "w") as file:
        for username, password in accounts.items():
            file.write(f"{username},{password}\n")


# ---------------------------------------------
# RULES
# ---------------------------------------------
def show_rules():
    print("\n=== RULES & REGULATIONS ===")
    rules = [
        "1. Respect all students and seniors.",
        "2. No abusive language.",
        "3. Follow academic integrity.",
        "4. Participate actively in events.",
        "5. Maintain discipline inside campus."
    ]
    for rule in rules:
        print(rule)


# ---------------------------------------------
# AUTHENTICATION
# ---------------------------------------------
def sign_up():
    print("\n=== SIGN UP ===")
    username = input("Create username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if username in accounts or username == ADMIN_USERNAME:
        print("Username already exists.")
        return

    password = input("Create password: ")
    confirm = input("Confirm password: ")

    if password != confirm:
        print("Passwords do not match.")
        return

    accounts[username] = password
    save_accounts()
    print("Account created successfully!")


def sign_in():
    print("=== SIGN IN ===")
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Admin login successful!")
        admin_dashboard()
        return

    if username in accounts and accounts[username] == password:
        print(f"Login successful! Welcome, {username}")
        student_portal(username)
    else:
        print("Invalid username or password.")


def forgot_password():
    print("=== FORGOT PASSWORD ===")
    username = input("Enter your username: ").strip()

    if username not in accounts:
        print("Username not found.")
        return

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    accounts[username] = new_password
    save_accounts()
    print("Password updated successfully!")


# ---------------------------------------------
# CHAT WITH SENIORS
# ---------------------------------------------
def chat_with_seniors():
    print("\n=== CHAT WITH SENIORS ===")

    for name, dept in seniors.items():
        print(f"- {name} ({dept})")

    choice = input("Enter senior name to chat: ").strip()

    if choice not in seniors:
        print("Senior not found.")
        return

    name = input("Enter your name: ").strip() or "Student"

    print(f"\nChat started with {choice}. Type 'bye' to exit.")

    while True:
        msg = input(f"{name}: ").lower()

        if msg == "bye":
            print(f"{choice}: Goodbye!")
            break
        elif msg in ["hi", "hello"]:
            print(f"{choice}: Hello {name}!")
        elif "library" in msg:
            print(f"{choice}: Library is open from 8 AM to 10 PM.")
        elif "hostel food" in msg:
            print(f"{choice}: Hostel food is average.")
        elif "events" in msg or "fest" in msg:
            print(f"{choice}: Tech Fest is in January.")
        elif "help" in msg:
            print(f"{choice}: Ask about library, hostel food, events, sports, and academics.")
        else:
            print(f"{choice}: Thanks for your message! I'll help you with that.")


# ---------------------------------------------
# INFORMATION MODULES
# ---------------------------------------------
def show_academics():
    print("\n=== ACADEMICS INFORMATION ===")
    for dept, subjects in academics.items():
        print(f"{dept}: {', '.join(subjects)}")


def show_clubs():
    print("\n=== CLUBS AVAILABLE ===")
    for club in clubs:
        print("-", club)


def show_events():
    print("\n=== UPCOMING EVENTS ===")
    for event, month in events:
        print(f"{event} - {month}")


# ---------------------------------------------
# CLUB JOINING
# ---------------------------------------------
def join_club(username):
    print("=== JOIN A CLUB ===")

    for club in clubs:
        print("-", club)

    choice = input("Enter club name to join: ").strip()

    if choice not in clubs:
        print("Club not found.")
        return

    role = input("Enter role (member/leader): ").strip().lower()

    if role == "member":
        print(f"You have joined {choice} as a member!")
    elif role == "leader":
        print(f"You applied for the leadership role in {choice}.")
    else:
        print("Invalid role.")


# ---------------------------------------------
# ADMIN DASHBOARD
# ---------------------------------------------
def admin_dashboard():
    while True:
        print("\n=== ADMIN DASHBOARD ===")
        print("1. View All Users")
        print("2. View Feedback")
        print("3. Delete User")
        print("4. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\nRegistered Users:")
            if not accounts:
                print("No users found.")
            else:
                for user in accounts:
                    print("-", user)

        elif choice == "2":
            print("=== STUDENT FEEDBACK ===")
            try:
                with open("feedback.txt", "r") as file:
                    feedbacks = file.readlines()

                if not feedbacks:
                    print("No feedback available.")
                else:
                    for feedback in feedbacks:
                        print(feedback.strip())
            except FileNotFoundError:
                print("No feedback file found.")

        elif choice == "3":
            username = input("Enter username to delete: ").strip()

            if username in accounts:
                del accounts[username]
                save_accounts()
                print("User deleted successfully.")
            else:
                print("User not found.")

        elif choice == "4":
            print("Admin logged out.")
            break

        else:
            print("Invalid choice.")


# ---------------------------------------------
# STUDENT PORTAL
# ---------------------------------------------
def student_portal(username):
    while True:
        print("\n--- STUDENT PORTAL ---")
        print("1. Rules & Regulations")
        print("2. Chat with Seniors")
        print("3. Academics Info")
        print("4. Clubs Info")
        print("5. Join a Club")
        print("6. Events Info")
        print("7. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_rules()
        elif choice == "2":
            chat_with_seniors()
        elif choice == "3":
            show_academics()
        elif choice == "4":
            show_clubs()
        elif choice == "5":
            join_club(username)
        elif choice == "6":
            show_events()
        elif choice == "7":
            print(f"Logged out. Goodbye, {username}!")
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------
# MAIN MENU
# ---------------------------------------------
def main_menu():
    while True:
        print("\n=== STUDENT INTERACTION PORTAL ===")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Forgot Password")
        print("4. Rules & Regulations")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            show_rules()
        elif choice == "5":
            print("Exiting portal.")
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------
# PROGRAM START
# ---------------------------------------------
load_accounts()
main_menu()