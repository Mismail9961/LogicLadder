What are Data Types : 
Data types are the things we store in Variables and it defines what data type variables are.
Python has built-in data types for different kinds of data.

Numbers :
Integer || Float || Complex : 
- All the numbers excluding decimal places and fraction.
- All the decimal numbers and fraction values are Float.
- Numbers with real and imaginary parts are complex.

Strings : 
Strings - This is used to store anything in python, literally anything that are available on your keyboard.You have to use quotes to store anything and it will be considered as string. You can use double Quotes (“”) or single quotes (‘’) to store both works same.

Boolean : 
Boolean - Theres nothing much to say this is the data type which will and always give the result of True and False.

How Strings work : 
- You know what strings are but you must also know string take more space than other data types like int, float etc.
- This happens because String stores every character with their own Unicode.
- is a universal character encoding standard that assigns a unique number (code point) to every character, regardless of language.
- Like “A” unicode is 65 and “ ” this emoji unicode is 128522, you can check them by using ord() function in python and convert them back using chr() function.

String Indexing : 
- You must have thought there are so many characters in a string but can you access everyone.
- Yes thats possible using indexing. Indexing starts from 0 and goes till the number of characters you have.
- There is negative indexing as well and it starts from -1, but the starting position is from the back of the string
- eg - a = “Hello” print(a[0]) ==> output - “H
- eg - a = “Hello” print(a[-1]) ==> output - “o”


| Concept         | Example                  |
| --------------- | ------------------------ |
| `f"{}"`         | `f"{name} is {age} yrs"` |
| `text[::-1]`    | Reverses string          |
| `len(text)`     | Length of string         |
| `**`            | Power (2 \*\* 3 = 8)     |
| `==`, `!=`, `>` | Comparison operators     |


String Slicing : 
- You know how to access characters in string. But there are slicing option as well.
- Slicing means cutting out a slice from string and this is also done using index values
- So here we have start , stop and steps position and keep a note if we use stop at 4 it will slice till 3 only.

Type conversion : 
- For understanding type conversion you have to look at these 4 things

int() float() str() bool()

- There are more functions like this but these are 4 main
function, looking at these functions you can guess these are
used to convert one data type to another
3 eg a = 12
a = str(a)
print(a) ==> “12” (a will be converted to string)

Type conversion types : 
-There are 2 types of conversion and . Implicit Explicit

Implicit :
In this python automatically
converts data from one data
type to another.
-You have already seen the example beforeh
eg - a = 12
print(a/2)
-Clearly we had the data type as int but after dividing python automatically converted the data type to float. output - 6.

Explicit :
-In this we as a user use in build functions to convert one data type to another
You have seen the example at
previous page.
int() Integer
float() Float
complex() Complex
str() String
list() List
tuple() Tuple
set() Set
dict() Dictionary
bool() Boolean