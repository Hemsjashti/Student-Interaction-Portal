#-------------------------
#Password Masking
#-------------------------
def masked_input(prompt):
    try:
        import msvcrt
        print(prompt, end="", flush=True)
        password = ""
        while True:
            ch = msvcrt.getch()
            if ch in (b"\r", b"\n"):
                print()
                break
            elif ch == b"\x08":
                if password:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)
            else:
                try:
                    password += ch.decode("utf-8")
                    print("*", end="", flush=True)
                except UnicodeDecodeError:
                    pass
        return password
    except Exception:
        return input(prompt)


#-------------------------
# Data Structures & Initialization
#-------------------------

accounts = {}
profiles = {}

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

academics = {
    "CSE": ["DSA", "Python", "DBMS"],
    "ECE": ["Circuits", "Signals", "Embedded Systems"],
    "MECH": ["Thermodynamics", "Fluid Mechanics", "Manufacturing"]
}

clubs = ["Robotics Club", "NrithyaSparsh", "Saptaswara", "Chakravyuha", "Avinya", "Drishya", "Prachurya", "Relu"]
events = [("Tech Fest", "January"), ("Sports Meet", "February"), ("Cultural Night", "March")]
seniors = {"Rahul": "CSE", "Ananya": "ECE", "Vikram": "MECH"}


#-------------------------
# Accounts section
#-------------------------

def load_accounts():
    try:
        with open("accounts.txt", "r") as f:
            for line in f:
                if line.strip():
                    u, p = line.strip().split(",", 1)
                    accounts[u] = p
    except FileNotFoundError:
        pass

def save_accounts():
    with open("accounts.txt", "w") as f:
        for u, p in accounts.items():
            f.write(f"{u},{p}\n")

def load_profiles():
    try:
        with open("profiles.txt", "r") as f:
            for line in f:
                if line.strip():
                    u, name, dept, year, email, phone = line.strip().split(",", 5)
                    profiles[u] = {"name": name, "dept": dept, "year": year, "email": email, "phone": phone}
    except FileNotFoundError:
        pass


#-------------------------
# Profile Management
#-------------------------


def save_profiles():
    with open("profiles.txt", "w") as f:
        for u, p in profiles.items():
            f.write(f"{u},{p['name']},{p['dept']},{p['year']},{p['email']},{p['phone']}\n")

def edit_profile(username):
    print("\n=== EDIT PROFILE ===")
    profiles[username] = {
        "name": input("Full Name: "),
        "dept": input("Department: "),
        "year": input("Year of Study: "),
        "email": input("Email: "),
        "phone": input("Phone Number: "),
    }
    save_profiles()
    print("Profile saved successfully!")

def view_profile(username):
    print("\n=== MY PROFILE ===")
    if username not in profiles:
        print("Profile not created yet.")
        return
    p = profiles[username]
    for label, key in [("Name", "name"), ("Department", "dept"), ("Year", "year"), ("Email", "email"), ("Phone", "phone")]:
        print(f"{label}: {p[key]}")

#-------------------------
#Rules
#-------------------------

def show_rules():
    print("\n=== RULES & REGULATIONS ===")
    for rule in [
        "1. Respect all students and seniors.",
        "2. No abusive language.",
        "3. Follow academic integrity.",
        "4. Participate actively in events.",
        "5. Maintain discipline inside campus."
    ]:
        print(rule)

#-------------------------
# Main Functionalities
#-------------------------

def sign_up():
    print("\n=== SIGN UP ===")
    username = input("Create username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username in accounts or username == ADMIN_USERNAME:
        print("Username already exists.")
        return
    password = masked_input("Create password: ")
    confirm = masked_input("Confirm password: ")
    if not password:
        print("Password cannot be empty.")
        return
    if password != confirm:
        print("Passwords do not match.")
        return
    accounts[username] = password
    save_accounts()
    print("Account created successfully!")

def sign_in():
    print("\n=== SIGN IN ===")
    username = input("Enter username: ").strip()
    password = masked_input("Enter password: ")
    if not password:
        print("Password cannot be empty.")
        return
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
    print("\n=== FORGOT PASSWORD ===")
    username = input("Enter your username: ").strip()
    if username not in accounts:
        print("Username not found.")
        return
    new_password = masked_input("Enter new password: ")
    confirm = masked_input("Confirm new password: ")
    if not new_password:
        print("Password cannot be empty.")
        return
    if new_password != confirm:
        print("Passwords do not match.")
        return
    accounts[username] = new_password
    save_accounts()
    print("Password updated successfully!")


#-------------------------
# Chat with Seniors
#-------------------------


def chat_with_seniors():
    print("\n=== CHAT WITH SENIORS ===")
    names = list(seniors.keys())
    for i, name in enumerate(names, 1):
        print(f"{i}. {name} ({seniors[name]})")
    choice = input("Enter senior number to chat: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(names)):
        print("Invalid choice.")
        return
    senior = names[int(choice) - 1]
    your_name = input("Enter your name: ").strip() or "Student"
    print(f"\nChat started with {senior}. Type 'bye' to exit.")
    while True:
        msg = input(f"{your_name}: ")
        if msg == "bye":
            print(f"{senior}: Goodbye!")
            break
        elif msg in ("hi", "hello"):
            print(f"{senior}: Hello {your_name}!")
        elif "library" in msg:
            print(f"{senior}: Library is open from 8 AM to 10 PM.")
        elif "hostel food" in msg:
            print(f"{senior}: Hostel food is average.")
        else:
            print(f"{senior}: Thanks for your message! I'll help you with that.")


#-------------------------
# Academics, Clubs & Events
#-------------------------

def show_academics():
    print("\n=== ACADEMICS INFORMATION ===")
    for dept, subjects in academics.items():
        print(f"{dept}: {', '.join(subjects)}")

def show_clubs():
    print("\n=== CLUBS AVAILABLE ===")
    for i, club in enumerate(clubs, 1):
        print(f"{i}. {club}")

def show_events():
    print("\n=== UPCOMING EVENTS ===")
    for event, month in events:
        print(f"{event} - {month}")

def join_club(username):
    print("\n=== JOIN A CLUB ===")
    show_clubs()
    choice = input("Enter club number to join: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(clubs)):
        print("Invalid choice.")
        return
    club = clubs[int(choice) - 1]
    role = input("Enter role (member/leader): ").strip()
    if role == "member":
        print(f"You have joined {club} as a member!")
    elif role == "leader":
        print(f"You applied for the leadership role in {club}.")
    else:
        print("Invalid role.")


#-------------------------
# Admin Dashboard
#-------------------------

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
            for user in accounts:
                print("-", user)
            if not accounts:
                print("No users found.")
        elif choice == "2":
            print("\n=== STUDENT FEEDBACK ===")
            try:
                with open("feedback.txt", "r") as f:
                    lines = f.readlines()
                if lines:
                    for line in lines:
                        print(line.strip())
                else:
                    print("No feedback available.")
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

#-------------------------
# Student Portal
#-------------------------

def student_portal(username):
    while True:
        print("\n--- STUDENT PORTAL ---")
        print("1. Rules & Regulations")
        print("2. Chat with Seniors")
        print("3. Academics Info")
        print("4. Clubs Info")
        print("5. Join a Club")
        print("6. Events Info")
        print("7. View Profile")
        print("8. Edit Profile")
        print("9. Submit Feedback")
        print("10. Logout")

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
            view_profile(username)
        elif choice == "8":
            edit_profile(username)
        elif choice == "9":
            submit_feedback(username)
        elif choice == "10":
            print(f"Logged out. Goodbye, {username}!")
            break
        else:
            print("Invalid choice.")

#-------------------------
# Feedback Submission
#-------------------------


def submit_feedback(username):
    print("\n=== SUBMIT FEEDBACK ===")

    feedback = input("Enter your feedback: ").strip()

    if feedback == "":
        print("Feedback cannot be empty.")
        return

    with open("feedback.txt", "a") as file:
        file.write(f"{username}: {feedback}\n")

    print("Thank you! Your feedback has been submitted.")

#-------------------------
# Main Menu
#-------------------------

def main_menu():
    while True:
        print("\n=== STUDENT INTERACTION PORTAL ===")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            print("Exiting portal.")
            break
        else:
            print("Invalid choice.")

load_accounts()
load_profiles()
main_menu()
