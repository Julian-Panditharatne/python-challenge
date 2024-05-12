# *U of T SCS Bootcamp* Python Challenge

This challenge is broken down to two parts:

1. **PyBank**
2. **PyPoll**

## PyBank Challenge

This challenge involves creating a Python script to analyze the financial records in a csv file called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
The challenge is to calculate each of the following values:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

Then, the script should both print the analysis to the terminal and export a text file with the results.

## PyPoll Challenge

This challenge involves creating a Python script to analyze the set of poll data given in a csv file called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate".
The challenge is to analyze the votes and calculate each of the following values:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

Then, the script should both print the analysis to the terminal and export a text file with the results.

---

## Repo Files and Folders

There are two folders for each of two parts of this challenge.

Each folder has the following content:

- A file called **main.py**: the main script to run for each analysis.
- A *Resources* folder that contains the CSV files used:
  - **budget_data.csv** in PyBank's *Resources* folder
  - **election_data.csv** in PyPoll's *Resources* folder.
- An *analysis* folder that contains the text file named **results.txt**, which has the results from running the **main.py** script.

---

## References

Elson, S. (2012, October 31). *Get key by value in dictionary* (D. Casas-Orozco, Ed.). Stack Overflow. <https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary?page=1&tab=scoredesc#tab-top>

Python Software Foundation. (2020). *csv — CSV File Reading and Writing — Python 3.8.1 documentation*. Python.org. <https://docs.python.org/3/library/csv.html>

Python Software Foundation. (2024a, May 11). *5. Data Structures.* Python Documentation. <https://docs.python.org/3/tutorial/datastructures.html#tut-listcomps>. 5.1.3. List Comprehensions.

Python Software Foundation. (2024b, May 11). *5. Data Structures.* Python Documentation. <https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences>. 5.3. Tuples and Sequences.

Python Software Foundation. (2024c, May 11). *5. Data Structures.* Python Documentation. <https://docs.python.org/3/tutorial/datastructures.html#sets>. 5.4. Sets.

Python Software Foundation. (2024d, May 11). *5. Data Structures — Python 3.9.0 documentation.* Python Documentation. <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>. 5.5. Dictionaries.

Python Software Foundation. (2024e, May 11). *5. Data Structures — Python 3.9.7 documentation.* Python Documentation. <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>. 5.1. More on Lists.

Python Software Foundation. (2024f, May 11). *7. Input and Output.* Python Documentation. <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>. 7.2. Reading and Writing Files.

Python Software Foundation. (2024g, May 11). *Built-in functions.* Python Documentation. <https://docs.python.org/3/library/functions.html#open>. open(file, mode=“r”, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None).

Python Software Foundation. (2024h, May 11). *Built-in functions.* Python Documentation. <https://docs.python.org/3/library/functions.html#sorted>. sorted(iterable, /, *, key=None, reverse=False).

Python Software Foundation. (2024i, May 11). *Built-in Functions — Python 3.11.0 documentation.* Python Documentation. <https://docs.python.org/3/library/functions.html#print>. print(*objects, sep=’ “, end=”\n’, file=None, flush=False).

Python Software Foundation. (2024j, May 11). *Built-in types.* Python Documentation. <https://docs.python.org/3/library/stdtypes.html#tuple>. class tuple([iterable]).

Python Software Foundation. (2024k, May 11). *Built-in types.* Python Documentation. <https://docs.python.org/3/library/stdtypes.html#list>. class list([iterable]).

Python Software Foundation. (2024l, May 11). *Built-in types.* Python Documentation. <https://docs.python.org/3/library/stdtypes.html#typesseq-common>. Common Sequence Operations.

Python Software Foundation. (2024m, May 11). *Built-in Types — Python 3.10.2 documentation.* Python Documentation. <https://docs.python.org/3/library/stdtypes.html#range>. class range(start, stop[, step]).

Python Software Foundation. (2024n, May 11). *Built-in types — Python 3.11.0 documentation.* Python Documentation. <https://docs.python.org/3/library/stdtypes.html#dict>. class dict(**kwargs).

Python Software Foundation. (2024o, May 11). *io — Core tools for working with streams.* Python Documentation. <https://docs.python.org/3/library/io.html#io-overview>
