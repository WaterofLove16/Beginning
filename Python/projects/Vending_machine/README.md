# Vending-Machine OOP code
 ## Quick summary:

 This code implements the basic functions of a vending machine with the usage of Object Oriented Programming. The goal of the code was to mimic real world vending machine but in a more simple and readable form. The code doesn't have a UI meaning all interactions are done on the terminal.

 ## Classes and functions used:
1. `VendingMachine() -> class`
   #### Used for:
   - Creating and displaying menus
   - Coordinates relations and actions between the other classes
   - interacting with buyer

   #### Design choie:
   The `VendingMachine()` was impleted to focus on user interaction and using the other classes to fulfill given actions. This allows each class to handle their respective data while `VendingMachine` just validates and call them around.

2. `Stocks() -> class`
   #### Used for:
   - Adding and removing drinks
   - Creating a stock list
   - Managing quantity of stocks

   #### Design choice:
   `Stocks()` was implemented as a dictionary with the drinks brand as the key and another dictionary containing it's price and quantity as the value. This allows for simple verification of same prices and increase/decrease of the specific drink.

3. `Drinks() -> class`
   #### Used for:
   - Storing the drinks data
   - Calling the required data

   #### Design choice:
   I used the class `Drinks()` instead of just using strings because accessing data for a specific drinks becomes more simple. Each drink will have their respective brand name and price and can be called out if needed.

4. `Credits() -> class`
   #### Used for:
   - Adding/increasing and removing/decreasing credits.
   - Converting floats to int for better comparison
   - Checking balance and affordability

   #### Design choice:
   `Credits()` is responsible for the increase and decrease of credits which is needed to buy drinks. A "convert to cents" method is used to change the the floats(rands) into ints(cents) to avoid errors in float comparisons. It also has a method to check whether the buyer has enough credits to buy the drink.

5. `show_menu() -> function`
   #### Used for:
   - Shows main menu

   #### Design choice:
   `show_menu()` is a funtion instead of a class because there is no data to store/munipulate. It's sole purpose is to print the main menu.

## Interactions between classes:
### `VendingMachine()` and `Stocks()`

  In `VendingMachine()`, `Stocks()` is used as an instance variable which acts as the machines stock area. With this, the user can add, remove and check available stocks from the `VendingMachine()` class. The vending machine handles the input and `Stocks()` handles the background process.

### `VendingMachine()` and `Credits()`

  `VendingMachine()` also has `Credits()` as an instance variable which serves as the buyers wallet. This allows for a new wallet for each run (The wallet resets to R0.0). This also allows the buyer to munipulate the amount of credits they have and use it to buy drinks.

### `VendingMachine()` and `Drinks()`

  These two classes don't have much interaction as `VendingMachine()` just handles collecting the rquired data and moving it to another class or method.

### `Stocks()` and `Drinks()`

  Once `Drinks()` recieves it's required data from `VendingMachine()`, it is then used in `Stock()` in order to keep track of the type and amunt of drinks in stock. `Stocks()` also ensures that different drinks don't have the same price and the same drink doesn't have different price sets unless the price needs to be changed.

## Assumptions and Simplification:

- All prices are converted to cents internally to avoid floating-point errors.
- User input goes through validation using loops and exception handling.
- No graphical interface was implemented (command-line only).
- There are limited amount of invalid attempts allowed for inputs
- Unlimited capacity of stocks can be added
- Can not get a refund

## Improvements if more time was allocated:

1. Better refund funtion
2. Implement an admin vs user mode
3. Better error messages
4. More restrictions on amount of drinks
5. Better user interactions in stocks and credits

## Conclusion:
This project help me with
- Better understanding of OOP (specifically Encapsulation)
- Handling dictionary errors
- Class responsibilty
- Safer data handling
- Better understanding on how to use loops and conditions for comparison and mutation
