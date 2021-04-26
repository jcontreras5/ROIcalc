from IPython.display import clear_output

class real_estate:
    def __init__(self):
         self.values={
             'income':{
                 'rental':0,
                 'misc': 0
             },
             'expenses':{
                 'tax':0,
                 'insurance':0,
                 'utilities':0,
                 'HOA':0,
                 'landscaping':0,
                 'repairs':0,
                 'capex':0,
                 'property management':0,
                 'mortgage':0,
                 'misc':0
             },
             'cashflow':{
                 'total income(monthly)':0,
                 'total expenses(monthly)':0,
                 'total cashflow':0
             },
             'cash on cash':{
                 'down payment':0,
                 'closing cost':0,
                 'rehab budget':0,
                 'total investment':0
             }
         }

#prompts to add income criterium    
    def add_income(self):
        
        while True:
            prompt_i = input("""This is the income portion of the calculator. We will assess your income with some prompts.
            \nEnter 'b' anytime to go back to main prompt. Press enter to continue.\n""" )
            if prompt_i.lower() == "b":
                break
            else:
                prompt_i1 = input("What is your monthly rental income? Pleaser enter a dollar amount.\n")
                self.values['income']["rental"] = int(prompt_i1)
                prompt_i2 = input("If you have any miscellaneous income ,please enter a monthly dollar amount.(default value will be 0 if nothing entered)")
                if prompt_i2.lower() == "":
                    pass
                else:
                    self.values['income']["misc"] = int(prompt_i2)
            break
        global monthly_total_income
        monthly_total_income = sum(self.values['income'].values())
        print(f'\n Your  monthly income is ${monthly_total_income}')
        

#prompts to add expense criterium                            
    def add_expenses(self):
        
        while True:
            prompt_e = input("""This is the expense portion of the calculator. We will assess your expenses with some prompts.
            \nEnter 'b' anytime to go back to main prompt. Press enter to continue.\n""" )
    
            if prompt_e.lower() == "b":
                break

            else:
                prompt_e1 = input("What is your monthly expense on taxes? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e1.lower() == "":
                    pass
                elif prompt_e1.lower() == "b":
                    break
                else:
                    self.values['expenses']["tax"] = int(prompt_e1)

                prompt_e2 = input("What is your monthly expense on insurance? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e2.lower() == "":
                    pass
                elif prompt_e2.lower() == "b":
                    break
                else:
                    self.values['expenses']["insurance"] = int(prompt_e2)
                
                prompt_e3 = input("What is your monthly expense on utilities? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e3.lower() == "":
                    pass
                elif prompt_e3.lower() == "b":
                    break
                else:
                    self.values['expenses']["utilities"] = int(prompt_e3)

                prompt_e4 = input("What is your monthly expense on HOA? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e4.lower() == "":
                    pass
                elif prompt_e4.lower() == "b":
                    break
                else:
                    self.values['expenses']["HOA"] = int(prompt_e4)

                prompt_e5 = input("What is your monthly expense on landscaping? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e5.lower() == "":
                    pass
                elif prompt_e5.lower() == "b":
                    break
                else:
                    self.values['expenses']["landscaping"] = int(prompt_e5)

                prompt_e6 = input("What is your monthly expense on capex? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e6.lower() == "":
                    pass
                elif prompt_e6.lower() == "b":
                    break
                else:
                    self.values['expenses']["capex"] = int(prompt_e6)

                prompt_e7 = input("What is your monthly expense on property management? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e7.lower() == "":
                    pass
                elif prompt_e7.lower() == "b":
                    break
                else:
                    self.values['expenses']["property management"] = int(prompt_e7)

                prompt_e8 = input("What is your monthly expense on mortgage? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e8.lower() == "":
                    pass
                elif prompt_e8.lower() == "b":
                    break
                else:
                    self.values['expenses']["mortgage"] = int(prompt_e8)

                prompt_e9 = input("Do you have any miscellaneous expenses? Pleaser enter a monthly dollar amount. (default value will be 0 if left blank. )\n")
                if prompt_e9.lower() == "":
                    pass
                elif prompt_e9.lower() == "b":
                    break
                else:
                    self.values['expenses']["misc"] = int(prompt_e9)

                break
            global monthly_total_expenses
            monthly_total_expenses = sum(self.values['expenses'].values())
            print(f'Your  monthly expense is ${monthly_total_expenses}')
            return monthly_total_expenses

#calculates cashflow base on income-expenses
    def cashflowcalc(self):
        monthly_total_cashflow = monthly_total_income - monthly_total_expenses
        global annual_total_cashflow
        annual_total_cashflow = monthly_total_cashflow*12
        print(f'Your annual total cashflow is ${annual_total_cashflow}')
        return annual_total_cashflow

#prompts to add cash on cash criterium
    def add_cash_on_cash(self):
        
        while True:
            prompt_coc= input("""This is the cash on cash portion of the calculator. We will assess your investments with some prompts.
            \nEnter 'b' anytime to go back to main prompt. Press enter to continue.\n""" )

            if prompt_coc.lower() == "b":
                break

            else:
                prompt_coc1 = input("What was your down payment? Please enter a dollar amount.(default value will be 0 if left blank. )")
                if prompt_coc1.lower() == "":
                    pass
                elif prompt_coc1.lower() == "b":
                    break
                else:
                    self.values['cash on cash']["down payment"] = int(prompt_coc1)

                prompt_coc2 = input("What was your closing cost ? Please enter a dollar amount.(default value will be 0 if left blank. )")
                if prompt_coc2.lower() == "":
                    pass
                elif prompt_coc2.lower() == "b":
                    break
                else:
                    self.values['cash on cash']["closing cost"] = int(prompt_coc2)

                prompt_coc3 = input("What was your rehab budget ? Please enter a dollar amount.(default value will be 0 if left blank. )")
                if prompt_coc3.lower() == "":
                    pass
                elif prompt_coc3.lower() == "b":
                    break
                else:
                    self.values['cash on cash']["rehab budget"] = int(prompt_coc3)

                global total_investment
                total_investment= sum(self.values['cash on cash'].values())
                return total_investment

    def ROI_ratio(self):
        ROI= annual_total_cashflow/total_investment
        print(f' Your ROI based on the responses you entered is {ROI}')


                

def calc():
    """parameter should be name of property"""
    
    Water_Tower = real_estate()
    active=True

    while active:
        prompt=input("Welcome to the ROI calculator.We will begin by asking you a series of questions to calculate your ROI on your property.\nEnter 'q' anytime to quit. Press Enter to continue.\n")

        if prompt.lower() == 'q':
            print("Thanks for using the ROI calculator")
            active = False

        else: 
            Water_Tower.add_income()
            Water_Tower.add_expenses()
            Water_Tower.cashflowcalc()
            Water_Tower.add_cash_on_cash()
            Water_Tower.ROI_ratio()

calc()

            
        
        


