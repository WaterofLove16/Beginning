# Vending Machine code by Mutwale,

class Stocks:
    def __init__(self):
        self._instock = {} # drink brand -> price, amount

    def items(self): 
        # method to call out items (key -> value) in stock
        return self._instock

    def add_drink(self, drink:str, price:float):
        # Checks if stock is empty to add first item
        if len(self._instock) == 0:
            self._instock[drink] = {"price" : price, "amount" : 1}
            print (f"\n{drink} has been added!")
        
        # Checks if drink is in stock to avoid repetition
        elif drink not in self._instock: 
            for soda in list(self._instock):
                # Condition to avoid drinks with same prices
                if price == self._instock[soda]["price"]:
                    print(f"\n{soda} is already R{price}, please set a different price.")
                    return
            # Adds drink to stocks if all is good,
            self._instock[drink]= {"price" : price, "amount" : 1}
            print(f"\n{drink} has been added!")

        # Adds drink to stocks if stock is not empty,
        else:
            self._instock[drink]["amount"] += 1
            print(f"\n{drink} has been added!")
    
    def remove_drink(self, drink:str):
        # Checks if given drink is in stock for removal.
        if drink in self._instock: 
            # If there is no more (amount is 0), removes the brand from stock.
            self._instock[drink]["amount"] -= 1
            if self._instock[drink]["amount"] <= 0: 
                self._instock.pop(drink)
                return True
            else:
                return True

        # If stock is empty, returns message.
        elif len(self._instock) == 0:
            print("\nStock is empty, please refill.")

        # If drink is not in stock.
        else:
            print(f"\n{drink} not in stock.")
        
    def check_stock(self):
        # Returns either empty stock message or list of what is in stock.
        if len(self._instock) == 0:
            print ("\nNothing in stock. Please refill.")
        
        else:
            i = 1
            print("\nAvailable stocks:")
            print(" ")
            for stock in self._instock:
                print(f"{i}. {stock} R{self._instock[stock]['price']}, available : {self._instock[stock]['amount']}")
                i += 1

class Drinks:
    def __init__(self, brand:str):
        # Insert brand/drink with default price set to R0.0.
        self._brand = brand
        self._price = 0.0

    def brand(self):
        # Returns the drinks brand/name.
        return self._brand

    def set_price(self, price:float):
        # Sets a different price for the drink.
        self._price = price

    def check_price(self):
        # Returns the drinks current price.
        return self._price
    
    def __str__(self):
        # String representation of Drinks().
        return f"{self._brand} : R{self._price}"
    
class Credits:
    def __init__(self):
        # Sets total amount of credits.
        self._totalamount = 0.0 

    def to_cent(self, amount:float):
        # Converts rands to cents.
        return int(round(amount*100)) 

    def increase_credits(self, amount:float):
        # Convert everything to cents for better comparison.
        max_amount = self.to_cent(10000.0)
        given_amount = self.to_cent(amount)
        total_amount = self.to_cent(self._totalamount)

        # Checks if total credits is smaller than maxed ammount to see if credits can be added.
        if total_amount < max_amount:
            # Checks if given amount doesn't cause total amount to cross maxed amount.
            if (total_amount + given_amount) <= max_amount:
                self._totalamount += (given_amount/100) # Adds to total if all boxes are checked as rands.
            
            else:
                print("\nInserted credits is too high.")
        else:
            print("\nYou have reached maximum possible credits.")    
    
    def decrease_credits(self, amount:float):
        # Convert everything to cents for better comparison.
        given_amount = self.to_cent(amount)
        total_amount = self.to_cent(self._totalamount)

        # Checks if total credits is larger than 0 to see if credits can be removed.
        if total_amount > 0:
            # Checks if given amount doesn't cross past 0.
            if total_amount >= given_amount:
                self._totalamount -= (given_amount/100) # removes to total if all boxes are checked as rands.
            
            else:
                print("\nInserted credits is too high.")
        else:
            print("\nYou have no more credits.") 
        
    def balance(self): 
        # returns current total amount.
        return self._totalamount
    
    def can_afford(self, price:float): 
        # Convert everything to cents for better comparison.
        given_price = self.to_cent(price)
        total_amount = self.to_cent(self._totalamount)

        # This checks if the buyer can afford the drink.
        if given_price <= total_amount:
            return True
        
        else:
            return False
        
    def __str__(self):
        # String representation of Credits.
        return f"R {self._totalamount}"
    
class VendingMachine:
    def __init__(self):
        self._available = {} # Type of brand -> item number
        self._stock = Stocks() # Create a stock supply for machine
        self._current_credits = Credits() # Create wallet for the buyer
        self._bought = [] # stores bought drinks

    def get_drink(self, code:str):
        # Searches for drink that has the specific item number.
        for key in self._available:
            if self._available[key] == code:
                return key
        return None

    def add_to_available(self, drink:str):
        if len(self._available) == 0:
            self._available[drink] = "D1"

        elif drink not in self._available:
            # Adds drink's respective item number.
            last_drink = next(reversed(self._available))
            no = int(self._available[last_drink][1:]) + 1
            self._available[drink] = f"D{no}"

    def remove_from_available(self, drink:str):
        # Removes drink if no longer in stock.
        if drink not in self._stock.items():
            self._available.pop(drink)
    
    def is_valid(self, user_input:str)-> bool:
        # Checks if user input is valid
        try:
            # Turns input into float, if error occurs goes to except.
            amount = float(user_input)

            # Checks if positive, if not return False.
            if amount < 0.0:
                print("\nPlease insert a positive amount...")
                return False
            
            return True
            
        except ValueError:
            print("\nPlease insert a valid input.")
            return False
    
    def yes_no_prompt(self, prompt:str)-> bool:
        attempt = 0 

        while True:
            decision = input(prompt + " (y/n) : ").strip().lower() # Prints out prompt and accepts input. Removes spaces and turns to lower case when needed.

            if decision == "y":
                return True # Choice to returns to previous
            
            elif decision == "n":
                return False # Choice to continues with current action in menu
            
            else:
                attempt +=1 # Counts how many invalid options were made
                if attempt >= 3:
                    print("\nToo many invalid attempts.")
                    return True # If too many attempts are done, exit menu
                print("\nPlease input y or n.") # Loop continues for retrying
    
    def stocks_menu(self):
        loop = 0
        while True:
            self._stock.check_stock()
            print("\n---- STOCKS ----")
            print("1. Add drink")
            print("2. Remove drink")
            print("3. Return to menu")
            option = input("\nPick an option : ")

            if option == "1":
                # runs add_drinks if option 1 is choosen.
                self.add_drinks() 

            elif option == "2":
                # runs removes_drinks if option 2 is choosen.
                self.remove_drinks() 

            elif option == "3":
                # breaks loop which results to returning to previous menu if option 3 is choosen.
                break 

            else: 
                # Measures in case an invalid attempt is done. If done too many times, exits menu.
                loop += 1
                if loop >= 3:
                    print("\nToo many invalid attemps.")
                    break
                print("\nInvalid input. Please pick the option's number (e.g. 3)")
                continue

    def add_drinks(self):
        while True: 
            # Input required information. 
            print("\nAdding drink...")
            brand_input = input("Please enter drink (Coke) : ")
            price_input = input("Please enter price (12.50) : R")

            # Checks if given price is valid.
            if self.is_valid(price_input):
                # Creates a drink and adds it to stock. If new, adds it to menu.
                drink = Drinks(brand_input)
                drink.set_price(float(price_input))
                price = drink.check_price()
            
                self._stock.add_drink(drink.brand(), price)
                self.add_to_available(drink.brand())

            else:
                continue

            # Asks if buyer wants to return to previous menu.
            if self.yes_no_prompt("\nBack to previous menu?"):
                break

            else:
                continue
        
    def remove_drinks(self):
        while True: 
            # Input required information.
            print("\nRemoving drink...") 
            brand_input = input("\nPlease enter drink (Coke) : ")

            # Removes drink from stock and if empty, removes from menu.
            if self._stock.remove_drink(brand_input):
                self.remove_from_available(brand_input)
                if brand_input in self._stock.items():
                    print(f"\n{brand_input} has been removed. {self._stock._instock[brand_input]['amount']} left.")
                else:
                    print(f"\n{brand_input} has been removed. None left.")


            # Asks if buyer wants to return to previous menu.
            if self.yes_no_prompt("\nBack to previous menu?"):
                break

            else:
                continue
                
    def credits_menu(self):
        loop = 0
        while True:
            # Shows current avaliable credits and options.
            wallet = self._current_credits.balance()
            print(f"\nAvaliable credits : R{wallet}")
            print("1. Add credit") 
            print("2. Decrease credit")
            print("3. Return to menu")
            option = input("\nPick an option : ")

            if option == "1":
                # runs add_credit if option 1 is choosen.
                self.add_credit(self._current_credits)

            elif option == "2":
                # runs remove_credit if option 2 is choosen.
                self.remove_credits(self._current_credits)

            elif option == "3":
                # breaks loop which results to returning to previous menu if option 3 is choosen.
                break

            else: 
                # Measures in case an invalid attempt is done. If done too many times, exits menu.
                loop += 1
                if loop >= 3:
                    print("\nToo many invalid attemps.")
                    break
                print("\nInvalid input. Please pick the option's number (e.g. 3)")
                continue

    def add_credit(self, credit:float):
        while True:
            # Buyer enters desired amount.
            print("\nIncreasing credits...")
            user_input = input("Please insert amount (e.g. 2.50) : R").strip().lower()

            # Ensures buyer entered valid amount before increasing credits.
            if self.is_valid(user_input):
                # Converts input to float and adds to wallet
                amount = float(user_input)
                credit.increase_credits(amount)
            
            else:
                continue
            
            # Asks if buyer wants to return to previous menu.
            if self.yes_no_prompt("\nReturn to previous menu?"):
                break

            else:
                continue

    def remove_credits(self, credit:float):
        while True:
            # Buyer enters desired amount.
            print("\nDecreasing credits...")
            user_input = input("Please insert amount (2.50) : R").strip().lower()

            # Ensures buyer entered valid amount before decreasing credits.
            if self.is_valid(user_input):
                # Converts input to float and adds to wallet
                amount = float(user_input)
                credit.decrease_credits(amount)
            
            else:
                continue
            
            # Asks if buyer wants to return to previous menu.
            if self.yes_no_prompt("\nReturn to previous menu?"):
                break

            else:
                continue

    def drinks_options(self):
        # Lists out all available drinks for purchase.
        print("\n **** DRINKS ****")
        for soda in self._available:
            price = self._stock._instock[soda]["price"]
            print(f"{self._available[soda]} : {soda} -> R{price}")

    def drinks_menu(self):
        loop = 0
        while True:
            print("\n1. Check bought drink(s)")
            print("2. Buy drink")
            print("3. Return to main menu")
            option = input("Pick an option : ")

            if option == "1":
                # Checks what drinks where bought if option 1 is choosen.
                print("\nBought drinks :")
                for drink in self._bought:
                    print(f"\n{drink}")

            elif option == "2":
                # Buys drinks if option 2 is choosen.
                self.buying_drinks()

            elif option == "3":
                break

            else: 
                # Measures in case an invalid attempt is done. If done too many times, exits menu.
                loop += 1
                if loop >= 3:
                    print("\nToo many invalid attemps.")
                    break
                print("\nInvalid input. Please pick the option's number (e.g. 3)")
                continue

    def buying_drinks(self):
        while True:
            self.drinks_options()
            choice = input("\nPick a drink! (e.g. D1) : ").strip()

            if choice[0] == "D" and choice[1:].isdigit(): # Checks if valid code is entered
                if choice in self._available.values(): # Checks if drink is in stock
                    drink = self.get_drink(choice)
                    drink_price = self._stock._instock[drink]["price"]
                    credit = self._current_credits

                    if credit.can_afford(drink_price): # Sees if buyer can afford
                        credit.decrease_credits(drink_price) # Spends money
                        self._bought.append(drink) # Adds to bought-drink list
                        self._stock.remove_drink(drink) # Decreases quantity from stocks
                        self.remove_from_available(drink) # If no longer in stocks, remove from menu
                        print(f"\n{drink} was bought!")

                    else:
                        print("\nInsufficient funds. Please add credits.")
                else:
                    print("\nDrink not in stock.")
            else:
                print("\nPlease enter a valid code (e.g D1)")

            # Returns to previous menu
            if self.yes_no_prompt("\nReturn to previous menu?"):
                break
            else:
                continue


def show_menu():
    print("\n==== MENU ====")
    print("\n1. Check available stocks")
    print("2. Check available credits")
    print("3. Drinks!")
    print("4. Exit menu")

def main():
    machine = VendingMachine()
    loop = 0

    while True:
        show_menu()
        choice = input("\nPick an option : ")

        if choice == "1":
            machine.stocks_menu()

        elif choice == "2":
            machine.credits_menu()

        elif choice == "3":
            machine.drinks_menu()

        elif choice == "4":
            print("\nThank you for using the vending machine. Have a pleasant day!")
            break

        else:
            loop += 1
            if loop >= 3:
                print("\nToo many invalid attemps")
                break
            print("\nPlease input a valid option.")
            
if __name__ == "__main__" : main()
            