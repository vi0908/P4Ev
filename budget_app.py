import math

class Category:

    def __init__(self, category):

        self.name = category
        self.fund = 0
        self.withdrawal= 0
        self.ledger = list()

    def __repr__(self):

        title = self.name.center(30, "*")
        ledger_list = ""
        ledger = self.ledger
        total = ("Total:{fund: .2f}").format(fund = self.fund)
        
        for element in ledger:
            amounts = "{amounts: .2f}".format(amounts = element["amount"])

            if len(element["description"]) < 24:
                descriptions = element["description"] + amounts.rjust(30 - len(element["description"]), ' ') + '\n'
                ledger_list += descriptions
            else:
                descriptions = (element["description"])[:23] + amounts.rjust(7, ' ') + '\n'
                ledger_list += descriptions
        
        objects_print = title + '\n' + ledger_list + total

        return objects_print
    
    def deposit (self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.fund += amount
        return self.ledger
        
    
    def withdraw (self, amount, description = ""):

        if (self.fund - amount) >=0 :
            self.fund -= amount
            self.withdrawal += amount
            self.ledger.append({"amount": (amount * -1), "description": description})
            return self.ledger, True
        
        
        else:
            return False 

    def get_balance(self):
        return self.fund

    def transfer(self, amount, budget_category):
        if amount <= self.fund:
            budget_category.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + budget_category.name)
            self.withdrawal += amount
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount <= self.fund:
            return True
        else:
            return False

   
            
def create_spend_chart(categories):
    total_expenses = 0 
    number_bar = 0
    percentages = {}

    for category in categories:
        total_expenses += category.withdrawal
    
    for number in range (0,11):
        number *= 10 
        percentages[number] = percentages.get(number, '')
    
    for category in categories:

        porcentaje = math.trunc((category.withdrawal / total_expenses ) * 100)
       

        while number_bar <= 100 and porcentaje >= 0:
            
            percentages[number_bar] = percentages.get(number_bar,) + 'o  '
            number_bar += 10
            porcentaje -= 10
        
        number_bar = 0

    percentages = sorted(percentages.items())[::-1]
    ordered_perecentages = ''
    
    for k,v in percentages:
        k = str(k) + '|'
        ordered_perecentages = ordered_perecentages + k.rjust(5-len(k),' ') + '   ' + v + ' \n '

    ordered_categories = {}
    name_categories = []

    for category in categories:
        name_categories.append(category.name)
    
    max_ind = len(max(name_categories, key = len))
   

    for category in categories:

        ind = 0

        if len(category.name) < max_ind:

            while len(category.name) > ind:
                ordered_categories[ind] = ordered_categories.get(ind, '') + category.name[ind] + '  '
                ind+=1
            while ind < max_ind:
                ordered_categories[ind] = ordered_categories.get(ind, '') + ' ' + '  '
                ind+=1
        else: 
            while len(category.name) > ind:
                ordered_categories[ind] = ordered_categories.get(ind, '') + category.name[ind] + '  '
                ind+=1

    ordered_names = ''

    for va in ordered_categories.values():
        ordered_names = ordered_names + va + '\n     '

    line = '-' * (len(categories)*3 + 1)

    spend_chart = 'Percentage spent by category\n' + ordered_perecentages + '    ' + line + '\n     ' + ordered_names

    return(spend_chart)


         
        
    
    
    
    










food = Category("Food")
entertainment = Category("Entertainment")
business = Category ("Business")




food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))