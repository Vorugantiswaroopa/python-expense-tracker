#create a list to store expenses
 
expenses=[]

def view_menu():
    
    print("1. add new expense")
    
    print("2. view all expenses")
    
    print("3. summarize the expenses")
    
    print("4. save the expenses")


def new_expense():
    try:
        
        amount=float(input("enter the expenditure : "))
    
        category=input("enter the context you spent money on : ")
    
        description = input("enter why you spent it : ")

        expenses.append({
        "amount" : amount ,
        "category" : category , 
        "description" : description 
        })
        
        print("expense added")
    
    except ValueError:
        print("invalid input of amount")
        
def view_expenses():
    
    if not expenses:
        
        print("there are no expenses to print")
        
    else:
        
        print("all expenses are as follows ")
         
        for expense in expenses:
            print(f"${expense['amount']} - {expense['category']} , {expense['description']}") 

def expense_summary():
    
    if not expenses:
        
        print("no expenses to summarize")
        
    summary={}
    
    for expense in expenses:
        
        category=expense['category']
        summary[category]=summary.get(category,0)+expense['amount']
 
    print("summary expense by category")
    
    for category,total in summary.items():
        print(f"{category} = ${total:.2f}")

def save_expenses():

    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(
                f"{expense['amount']}, {expense['category']}, {expense['description']}\n"
            )

    print("Expenses saved successfully")
    
while True:
    
    view_menu()
    choice=input("enter your choice :  ")
    
    if choice == '1':
        new_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        expense_summary()
    elif choice == '4':
        save_expenses()
    
    else:
        print("invalid option")
