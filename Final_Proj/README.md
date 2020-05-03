# Project 2: Final Project

<br>
<br>

## Assignment
---
- Create an object oriented hierarchy
- Use OOP concepts like polymorphism and inheritance
- Implement a design pattern

<br>

## Description of the Assets Class
---
- A company has to keep track of several different assets along their course of business
- The assets class allows the company to keep track of:
  - Cash on hand
  - Accounts receivable
  - Supplies
    - Things that will be used and later expensed
    - General office supplies
  - Internal inventory
    - Items that will be depreciated
    - Expensive machenary or technology
  - Merchandise
    - Sellable goods
      - Must be finished goods to be sold
      - Purchasing more of these goods will increase in process merchandise
- This asset class acts as a proxy for the inventory class
- There are instances of the inventory class within assets, but not accessed directly

<br>

### Description of the Inventory Class
---
- For maintaining internal inventory
- All inventory has:
  - A name
  - Purchase price
  - Quantity

<br>

### Description of the Supplies Class
---
- For maintaining office supplies
- All supplies have:
  - The same features as the inventory class
  - The amount in use
  - The amount available (total quantity - amount in use)
- To expense a supply it must be in use

<br>

### Description of the Merchendise Class
---
- For maintaining sellable goods
- All merchandise have:
  - The same features as the inventory class
  - The amount of finished sellable goods
  - The amount of in process goods (total quantity - sellable goods)
- To sell a piece of merchandise the good must be finished

<br>

## Tests Used
---
- Initializer:
  - Making sure that the assets class initializer is properly working
- Inventory:
  - Making sure the cash and inventory accounts are being properly recorded as transactions take place
  - The transactions:
    - Set up two accounts for internal inventory, computer and chairs
    - Purchase more chairs
- Supplies:
  - Making sure the cash and supplies accounts are being properly recorded as transactions take place
  - The transactions:
    - Set up two accounts for the supplies, pens and sticky notes
    - Put some of the pens and sticky notes to use
    - Expense some of the pens and sticky notes
    - Buy more pens
- Merchandise:
  - Making sure the cash, accounts receivable, and merchandise accounts are all being properly recorded
  - The Transactions:
    - Set up two accounts for the merchandise, bread and cookies
    - Sell some of the bread and cookies
    - Move some of the in process goods to finished product
    - Sell bread on credit and cookies on cash
    - Collect some of the accounts receivable
    - Change the selling price of the bread
    - Buy in process materials for bread and cookies
    - Move some of the in process bread to finished product
    - Sell some of the bread