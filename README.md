SQLite CLI Running Tracker

This app tracks runs with an ID, Date, Miles Ran, Time (MM:SS), and additional Notes

There are 6 functions:

    1. addRun - creates a new run that is entered into a running.db (CREATE)

    2. viewRuns - displays all run entries in running.db (READ)

    3. runsLongerThan - displays all runs longer than a set distance in running.db(FILTERED QUERY)

    4. updateEntry - allows the user to update an entry item (UPDATE)

    5. deleteEntry - deletes a run entry with an inputted id (DELETE)

    6. quit - closes main.py 

There is a recurring menu that appears allowing the user to see what functions they can use.

Works entirely in the Command Line Interface! No external libraries needed

Runs are saved in running.db even after using quit function.
    
