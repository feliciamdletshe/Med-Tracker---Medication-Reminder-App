# import modules that are needed
import datetime # for time and date
import matplotlib.pyplot as plt # for the pie chart

# list for keeping medication records
medications = []

# function to add medication
def add_medication():
# dictionary for the user to enter the medication details
    medication = {
        "Name": input("Enter medication name:"), # The name of the medication
        "Dosage": input("Enter the dosage: "), # Guide of dosage
        "Time": input("Enter the time(HH:MM): "), # The time to take the medication
        "Days_left": int(input("How many days to take: ")), # Remaining days to take the medication
        "Last_reminded": None # Last date reminder initiated to none
        
    }

    medications.append(medication) # Add medication dictionary to the medications list
    print(f"{medication['Name']} added successfully!") # message

# function to check reminders when they are needed
def check_reminders():
    now = datetime.datetime.now() # Obtain current date and time
    current_time = now.strftime("%H:%M") # Take the current time as string in the HH:MM format
    today_date = now.date() # Take  the current date

# Looping medication that is stored
    for med in medications:
        reminder_time = med["Time"] #Time to take the medication
        
         # Check if current time is the same or later than the reminder time
        if current_time >=reminder_time and med["Days_left"]>0 and med["Last_reminded"] != today_date:
            # Display message with the dosage and medication name
            print(f"Reminder: Take {med['Dosage']} of {med['Name']} now!")
            med["Days_left"] -=1 #Reduce the days left to take medicine
            med["Last_reminded"] = today_date # Track reminder sent today

# function to display pie chart for days remaining of medication
def show_pie_chart():
    if not medications: # If no medication records found
        print("No medications to show.")
        return # exit the function
    
    # Separate medication names and days left
    names = [med["Name"] for med in medications]
    days_left = [med["Days_left"] for med in medications]

    if sum(days_left) == 0: # If medication has zero days left
        print("All medication is completed. No chart to show.")
        return # exit
    
    # Create pie chart
    plt.figure(figsize=(6,6)) # figure size
    plt.pie(days_left, labels=names, autopct="%1.1f%%", startangle=140) # Pie chart with lables
    plt.title("Remaining Days for Medications") # The title of the chart
    plt.show() # Show the chart

# Inifinte loop
while True:
    # Display menu and allow the user to get options
    option = input("\n1. Add Medication 2. Check Reminders 3. View Chart 4. Exit: ")
    if option == "1":
        add_medication() # Add new medication
    elif option == "2":
        check_reminders() # Call function to check and show reminders
    elif option =="3":
        show_pie_chart() # Call function to show pie chart
    elif option == "4":
        break # Exit the program
    else:
        print("Invalid option. Please select 1, 2, 3 or 4.") # Takes care of invalid inputs
    

    
    
    



