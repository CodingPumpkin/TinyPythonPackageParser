
# TinyPythonPackageParser
## Motivation
I wrote this code for a test task as well as another one of my repos. I was still struggling with tcl and so the code still looks and feels messy. But I still think that it's not a bad example of what I can do with a language after dedicating a couple of days to getting to know it. I made a Python version (to gain a little confidence mostly but also to draft some of the algorithms I might need to validate input) and then I wrote a tcl version.

## Installation
You can run python version with your interpreter.
>python tiny_python_packege_parser.py

If you want to run tcl version you'll need to make the file executable and run it as
> ./tiny_python_packege_parser.tcl

Or you can run it with your interpreter, for instance:
> tclsh tiny_python_packege_parser.tcl
## Usage
The parser accepts a package of data. The package is a string formatted as:
> #PKG_TYPE#PKG_MESSAGE 

The program recognizes two types of packages "M" package and "SD" package. M package expects the message to be any string. SD package expects message to contain certain tokens in certain order. You can find some examples of the inputs in the "tests" file. Both tcl and python scripts parse all of the tests given here. Note that python script is more stable.

## Example
1) Input: 
> #M#Hello World!

Output:
```
	Packege type: M
Data:
	packege_type: M
	message: Hello World!
```
2) Input:
> #SD#04012011;135515;5544.6025;N;03739.6834;E;35;215;110;7

Output:
```
Packege type: SD
Data:
	packege_type: SD
	date: 04012011
	time: 135515
	lat1: 5544.6025
	lat2: N
	lon1: 3739.6834
	lon2: E
	speed: 35.0
	course: 215
	height: 110.0
	sats: 7.0
```
