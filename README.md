1. Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

Sample output:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
... etc up to 100

2. Given a letter print a diamond starting with 'A' with the supplied letter at the widest point.
 
This is the print diamond for 'E'.
 
....A....
...B.B...
..C...C..
.D.....D.
E.......E
.D.....D.
..C...C..
...B.B...
....A....
 
 
This is the print diamond for 'C'.
 
..A..
.B.B.
C...C
.B.B.
..A..
 
This is the print diamond for 'A'.
 
A
 
Note: These examples use dots in place of spaces only for readability.
Your diamond must contain spaces where there are dots.
3. A field of N x M squares is represented by N lines of exactly M characters each.
  o) The character '*' represents a mine.
  o) The character '.' represents no-mine.

Example input (a 3 x 4 mine-field of 12 squares, 2 of which are mines)

3 4
*...
..*.
....

Your task is to write a program to accept this input and produce as output a hint-field of identical dimensions where each square is a * for a mine or the number of adjacent mine-squares if the square does not contain a mine.

Example output (for the above input)
*211
12*1
0111
