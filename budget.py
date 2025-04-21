import pandas as pd
from colorama import Fore, Back, Style
from datetime import datetime
import numpy as np


#declare run function
run=True
l= ["1","2","3","4","5"]


data={'date': [], 'category': [], 'amount': [], 'description': []}

def input_data(data):
    date_string= input("Enter date in YYYY-MM-DD format:")
    try:
        date_object = datetime.strptime(date_string, "%Y-%m-%d").date()
        data['date'].append(date_object)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        data['date'].append(np.nan)

    categories= ["food","travel","necessities"]
    c= input("Enter category <food|travel|necessities>:")
    if c.lower() in categories:
        data['category'].append(c.lower())
    else:
        print("Invalid category. Please use select from <food|travel|necessities>.")
        data['category'].append(np.nan)

    

    a= input("Enter amount:")

    try:
        data['amount'].append(float(a))
    except ValueError:
        print("Invalid amount value. Please enter a numeric value!")
        data['amount'].append(np.nan)
   

    desc= input("Enter description:")
    data['description'].append(desc)

def print_dict(data):
    df= pd.DataFrame(data)
    print(Fore.GREEN)
    print(df.dropna())
    print(Style.RESET_ALL, end="")

def data_to_CSV(data):
    df= pd.DataFrame(data)
    df.to_csv('expenses.csv', index=False)

#
#MAIN LOOP
#

while(run):
    print(Fore.YELLOW)
    print(
        ''' Select from the options:
            1. Add expense
            2. View expenses
            3. Track Budget
            4. Save expenses
            5. Exit
        '''
        )
    
    print(Style.RESET_ALL)
    print(Fore.MAGENTA, end="")
    print("Enter number for an option:", end="")

    print(Style.RESET_ALL, end="")
    o= input("")

    #SAVE n EXIT
    if (o==l[4]):
        run5=True
        #Ask whether you want to exit
        while(run5):
            print(Fore.YELLOW)
            p=input("Are you sure you want to EXIT? <y/n>")
            print(Style.RESET_ALL, end="")
            if (p=='y'):
                data_to_CSV(data)
                print(Fore.CYAN)
                print("\n\nYOUR EXPENSES HAVE BEEN SAVED!\n\n")
                print(Style.RESET_ALL, end="")
                run5=False
                run=False

            elif(p=='n'):
                run5=False
            else:
                print("Enter Valid Input")

    #Save expenses to CSV
    elif(o==l[3]):
        run4=True
        while(run4):
            print(Fore.YELLOW)
            p=input("Do you want to save expenses? <y/n>")
            print(Style.RESET_ALL, end="")
            if (p=='y'):
                data_to_CSV(data)
                print(Fore.CYAN)
                print("\n\nYOUR EXPENSES HAVE BEEN SAVED!\n\n")
                print(Style.RESET_ALL, end="")
            elif(p=='n'):
                run4=False
            else:
                print("\n\nEnter Valid Input\n\n")

    #TRack expenses

    elif(o==l[2]):

        #Enter total money they wat budget
        #
        print("Enter your monthly budget:",end="")
        print(Fore.YELLOW, end="")
        budget=int(input())

        df= pd.DataFrame(data)
        d=df.dropna()
        
        print(Style.RESET_ALL, end="")
        if budget>= d['amount'].sum():
            print("\n\nBALENCE REMAINING:", end="")
            print(Fore.GREEN, end="")
            print(budget-d['amount'].sum(), end= "\n\n")
            print(Style.RESET_ALL, end="")
        else:
            print(Fore.RED+"\n\nYOU HAVE EXCEEDED YOUR BUDGET!!!\n\n")
            print(Style.RESET_ALL, end="")
    #View expense
    elif(o==l[1]):
        #Viewing
        print_dict(data)
    
    #Add expense
    elif(o==l[0]):
        #Appending
        input_data(data)
    
    else:
        print(Fore.RED+"\n\nENTER A VALID OPTION OUT OF <1|2|3|4|5>!\n\n")
        print(Style.RESET_ALL, end="")