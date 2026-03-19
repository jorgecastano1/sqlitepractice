import sqlite3

# will be making a table that tracks running sessions
# columns: id (integer) , date (text), distance (real), time (minutes and seconds ), notes (text)
# 

con = sqlite3.connect("running.db")
cur = con.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS running (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            distance REAL,
            time TEXT,
            notes TEXT)
            ''')
            
con.commit()

def addRun():
    """Prompt the user to add a run"""
    print("\n Add the details of the run below!")
    date = input("Enter the date of the workout: (YYYY-MM-DD) ").strip()

    while True:
        try:
            distance = float(input("Enter the distance of the run in miles: ").strip())
            break
        except ValueError:
            print("Please enter a valid number for distance!")
        
    time = input("Enter the time of the workout: (MM:SS) ").strip()
    notes = input("Notes: (optional) ").strip()

    # Inserting the run into the database
    cur.execute(''' INSERT INTO running (date,distance, time, notes)
                VALUES (?,?,?,?)''', (date, distance, time, notes))
    con.commit()
    print("="*30)
    print("Run tracked successfully!")

def viewRuns():
    """Displays all the runs in the database"""
    cur.execute("SELECT * FROM running")
    runs = cur.fetchall()
    if not runs:
        print("="*30)
        print("\nNo runs tracked yet!")
    
    for run in runs:
        print("="*30)
        print(f"\nID: {run[0]}")
        print(f"Date: {run[1]}")
        print(f"Distance: {run[2]} miles")
        print(f"Time: {run[3]}")
        if run[4]:
            print(f"Notes: {run[4]}")
        else:
            print("Notes: None")

        print("="*30)

def runsLongerThan():
    """Displays all runs longer than x miles"""
    x = input("Input Distance Threshold: ")
    while True:
        try:
            if type(x) == str:
                threshold = float(x.strip())
            else:
                threshold = float(x)
            break
        except (ValueError, TypeError):
            print("="*30)
            print(f"/n Invalid Input! {x} is not a valid number.")
            x = input("Please input a valid distance in miles: ").strip()

    cur.execute("SELECT * FROM running WHERE distance > ?", (x,))
    runs = cur.fetchall()

    if not runs:
        print("="*30)
        print(f"\nNo runs longer than {x} miles!")
        return None
    
    else:
        print("="*30)
        print("ID", "|", "Date", "|", "Distance", "|", "Time", "|", "Notes")
        for run in runs:
            id = run[0]
            date = run[1]
            distance = run[2]
            time = run[3]
            if run[4]:
                notes = run[4]
            else:
                notes = None
        print("="*30)
        print(id, "|", date, "|", distance, "|", time, "|", notes)

    
def updateEntry():
    """ Updates Existing Entry, if no id provided prompt user"""
    id = input("Enter ID of Entry to Update: ")
    if id is None:
        while True:
            try:
                id = int(input("Enter Valid ID: ").strip())
                break
            
            except ValueError:
                print("="*30)
                print("Please Enter a Valid ID")

    cur.execute('SELECT * FROM running WHERE id = ?', (id,))
    run = cur.fetchone()
    if not run:
        print("No Run found with this ID")

    #Displays the current run
    print("="*30)
    print(f"Current Run ID: {run[0]}")
    print('='*30)
    print(f"1. Date: {run[1]}")
    print(f"2. Distance: {run[2]}")
    print(f"3. Time: {run[3]}")
    print(f"4. Notes: {run[4]}")
    print('='*30)

    while True:
        print("="*30)
        print("\nWhich field would you like to update?")
        print("1. Date")
        print("2. Distance")
        print("3. Time")
        print("4. Notes")
        print("5. Cancel")

        choice = input("Enter choice here (1-5): ").strip()

        if choice == "1":
            print("="*30)
            print(f"Current Date: {run[1]}")
            newDate = input(f"Input New Date (YYYY-MM-DD): " ).strip()

            if newDate:
                cur.execute('UPDATE running SET date = ? WHERE id = ?', (newDate, id))
                con.commit()
                print("="*30)
                print(f"Date of Entry {id} successfully updated!")

        elif choice == "2":
            print("="*30)
            print(f"Current Distance: {run[2]}")
            newDistance = input(f"Input New Distance (miles): ").strip()

            if newDistance:
                cur.execute('UPDATE running SET distance = ? WHERE id = ?', (newDistance, id))
                con.commit()
                print("="*30)
                print(f"Distance of Entry {id} successfully updated!")

        elif choice == "3":
            print("="*30)
            print(f"Current Time: {run[3]}")
            newTime = input(f"Input New Time (MM:SS): ").strip()

            if newTime:
                cur.execute('UPDATE running SET time = ? WHERE id = ?', (newTime, id))
                con.commit()
                print("="*30)
                print(f"Time of Entry {id} succesfully updated!")

        elif choice == "4":
            print("="*30)
            print(f"Current Notes: {run[4]}")
            newNote = input(f"Input New Note: ").strip()

            if newNote:
                cur.execute('UPDATE running SET notes = ? WHERE id = ?', (newNote, id))
                con.commit()
                print("="*30)
                print(f"Note of Entry {id} succesfully updated!")

        elif choice == "5":
            print("="*30)
            print("\nEntry Update cancelled.")
            break

        else:
            print("="*30)
            print("Invalid Choice. Please enter a number from 1-5.")
            continue

        cur.execute('SELECT * FROM running WHERE id = ?', (id,))
        updatedRun = cur.fetchone()


def deleteEntry():
    id = input("Enter ID # of Entry to Delete: ").strip()
    if id is None:
        while True:
            try:
                inputtedID = input("Enter ID # of Entry to Delete (Press Enter once to cancel)").strip()
                if not inputtedID:
                    print("="*30)
                    print("Deletion Canceled")
                    return None
                id = int(inputtedID)
                break
            except ValueError:
                print("="*30)
                print("Please enter a valid ID!")

    cur.execute("SELECT * FROM running WHERE id = ?", (id,))
    pulledRun = cur.fetchone()
    
    if not pulledRun:
        print("="*30)
        print("No Run found with inputted ID!")
        return None
    
    print("="*30)
    print("Run to delete:")
    print(f"ID: {pulledRun[0]}")
    print(f"Date: {pulledRun[1]}")
    print(f"Distance: {pulledRun[2]}")
    print(f"Time: {pulledRun[3]}")
    if pulledRun[4]:
        print(f"Notes: {pulledRun[4]}")
    else:
        print(f"Notes: {None}")
    print("="*30)

    while True:
        confirm = input(f"Please confirm deletion of Entry {id} (yes/no) ").strip().lower()

        if confirm in ['yes', 'y']:
            cur.execute("DELETE FROM running WHERE id = ?", (id,))
            con.commit()
            print("="*30)
            print(f"Run with ID {id} successfully deleted!")
            break
        elif confirm in ['no', 'n']:
            print("="*30)
            print("Deletion Cancelled!")
            break
        else:
            print("="*30)
            print("Please enter 'yes' or 'no'.")

    return None


def quit():
    print("="*30)
    print("GET AFTER IT!")
    print("="*30)
    con.close()
    exit()

while True:
    print('='*30)
    print("Running Tracker Menu !!")
    print("\nThese are the available functions:")
    print("1. addRun() - Add a new run to the database")
    print("2. viewRuns() - View all the runs in the database")
    print("3. runsLongerThan() - View all runs longer than inputted distance")
    print("4. updateEntry() - Update specific value in run entry")
    print("5. deleteEntry() - Delete run with specified entry ID")
    print("6. quit() - Exit Running Tracker")
    print("="*30)

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        addRun()
    elif choice == "2":
        viewRuns()
    elif choice == "3":
        runsLongerThan()
    elif choice == "4":
        updateEntry()
    elif choice == "5":
        deleteEntry()
    elif choice == '6':
        quit()
    else:
        print("Invalid choice! Please choose a number from 1-6")


    

        

