# Project 2: Final Project

<br>
<br>

## Assignment
---
- Create a super class from which other classes will inherit
- Create two sub classes with unique properties
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
  - Making sure the cash is properly being recorded as transactions take place
    - 
- Merchandise:
  - M
- Supplies:
  - M