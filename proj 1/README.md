# Project 1 Python Composite

<br>
<br>

## Assignment
---
- The object should have different attributes and methods
- Run several tests to determine if the object functions as anticipated

<br>

## Description of the Guitar Class
---
- A guitar object has the following properties:
  - Strings
    - An integer representing the number of strings on the guitar
    - Can have any number of strings equal to or greater than zero
    - Zero strings implies the guitar is being restrung
    - There are several unique guitars with many more than six strings, this is why there is no upper bound on the string count
  - String gauge
    - An integer representing the thickness of the string
    - The thickness of the string is based off of the manufacturer's model description
  - String tuning
    - A string that allows for different tunings of the strings
    - Requires that there is only one note name for each string
    - Only accepts real notes (Ab, A, A#...etc.)
  - Volume
    - A double that describes the volume output of the guitar
    - Only accepts doubles from 0.0 to 10.0

## Tests Used
---
- Defaults:
  - Creating an instance of a guitar with no constructor arguments
  - Making sure that the default constructor applies the default values for all attributes
- Bad Values:
  - Creating an instance of a guitar with purposfully bad arguments
  - Making sure the object catches:
    - Negative string counts
    - Negative volumes
    - Volumes greater than ten
    - Acceptable tunings
- Specifics:
  - Creating an instance of a guitar with specific values
  - Making sure that the attributes can be changed with the setter methods