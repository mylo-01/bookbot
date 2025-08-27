# BookBot?

BookBot is a command-line Python program that analyzes text files (books) to count words and characters.  
It was created as part of the Boot.dev Python course.

## Overview
BookBot reads a `.txt` file and provides:
- Total word count.
- Frequency count of alphabetic characters (sorted from most to least frequent).

### The repository includes three sample books:
- `frankenstein.txt`
- `mobydick.txt`
- `prideandprejudice.txt`

## Project Structure
python_bootdev_bookbot/
│── main.py # Entry point of the program
│── stats.py # Helper functions for word/character analysis
│── frankenstein.txt # Sample book
│── mobydick.txt # Sample book
│── prideandprejudice.txt # Sample book
│── README.md # Project documentation


## Installation
Clone the repository:
git clone https://github.com/username/python_bootdev_bookbot.git
cd python_bootdev_bookbot
No additional dependencies are required beyond Python 3.

## Usage
Run the program with:
python3 main.py <path_to_book>

## Example:
python3 main.py frankenstein.txt
Sample Output
diff
Copiar código
============ BOOKBOT ============
Analyzing book found at frankenstein.txt...
----------- Word Count ----------
Found 78112 total words
--------- Character Count -------
e: 46043
t: 30365
a: 23642
...
============= END ===============