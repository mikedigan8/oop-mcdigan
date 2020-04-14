# Project 3: Pattern Implementation

<br>
<br>

## Assignment
---
- Pick a design pattern and implement in a language of your choice
- Create tests to make sure the pattern is working properly

<br>

### Description of the Student Class
---
- There are three different constructors
  - Default:
    - Assigns the first and last name to "NONE"
    - Sets both the birth year and the ID to -1
  - No ID:
    - Assigns the first and last name and birth year to the given values
    - Sets the ID to -1
  - Including ID:
    - Assigns everything to the given values

<br>

### Description of the IteratorPattern Class
---
- MakeList:
  - A method to add several students to the students array list
- AddMoreStudents:
  - A method to add new students to the array list with no IDs
- TraverseArray:
  - A method that prints the elements in the array using an iterator
- ReverseTraverse:
  - A method that prints the list in reverse using a list iterator
- EachRemaining:
  - Uses the ForEachRemaining method of iterators to assign new ID values starting with the first student without an ID
- GetStudent:
  - Pass in an ID value and this method will return the student with that ID
- RemoveStudent:
  - Pass in an ID value and this method will delete that student from the list

<br>


## Tests Used
---
- testGetStudent:
  - Creates a list of students and makes sure I can get a student providing an ID
- testEachRemaining:
  - Tests that I can add more students without ID values and add some using the ForEachRemaining method
- testRemoveStudent
  - Makes sure that the RemoveStudent function infact does remove the correct student
  
  <br>
  
  ## Links for presentation:
  ---
  - [**YouTube Video**](https://youtu.be/HHFTBWZTV2E)
  - [**Slide Show**](https://docs.google.com/presentation/d/1F8mTK-zTXAjGml5EA6-v-S0cTOtOhOO2RYL3RNizG3g/edit?usp=sharing)
