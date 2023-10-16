# Microprocessor Simulation

The Microprocessor Simulation is a Python program designed to mimic the operations of a microprocessor based on a set of predefined commands and values. This simulation allows you to gain insights into how a microprocessor processes instructions and produces results. It's a valuable tool for learning about the fundamental operations of a processor and understanding how it handles different instructions.

## How It Works
A program for this microprocessor consists of a sequence of operations and values. The processor performs each operation on the values, one after the other. A simplified example might look like this:
```sh
add 8 16
mul 10 3
or 1 0
nand 1 1
```

At each step, the processor executes an operation and produces an output value. For the above program, the output at each step would be:
```sh
24
30
1
0
```

## Processor Operations
The Microprocessor Simulation supports various operations, each with a specific function:

| Operation 	| Description                           	| Sample       	| Output 	|
|-----------	|---------------------------------------	|--------------	|--------	|
| noop      	| Does nothing and prints an empty line          	| noop         	|        	|
| add       	| Adds two integer arguments                       	| add 3 140    	| 143    	|
| mul       	| Multiplies two integer arguments                    	| mul 10 21    	| 210    	|
| gt        	| Checks if the first integer is greater than the second	| gt 3 10      	| 0      	|
| or        	| Performs a logical OR operation                            	| or 6 0       	| 1      	|
| nand      	| Performs a logical NAND operation           	| nand 1 1     	| 0      	|
| min       	| Finds the minimum value among two or more integers   	| min 14 8 103 	| 8      	|
| shift     	| Shifts an integer left by a specified number of bits        	| shift 8 2    	| 32     	|
| invalid     | Represents an invalid operation                | not an op     | invalid operation not an op |

**Note**:
- All of the operations are defined for integer arguments. Floats or other 
    arguments are invalid.
- Most operations take exactly two arguments.
- `noop` takes no argument
- The logical `or` and `nand` operations always print out a `0` or `1`, no matter
    their inputs. 0 is treated as false, any other number is treated as true.
- `shift` takes the bit representation of its argument, and moves the bits left,
    with the number of places to shift given by the second argument. So, 8
    (00001000) gets shifted left by 2 to become 32 (00100000).
- If the processor encounters an invalid operation, it should print an error 
    message and stop.

## Usage
1. Run the Script:
Execute the script by running the following command:
```python main.py```

2. Process a Program:
You can create your own program or use one of the provided sample programs. The program will be processed, and the output will be displayed.

Sample Programs:
To run a sample program, use the following command:
```python main.py sample1.txt```

## Testing
As you develop your program, you can test your functions with sample inputs to ensure they provide the expected results. The automated tests included will also check the correctness of your program by running sample operations and programs, ensuring the functions produce the correct outputs.

## Hints
To create this program effectively, consider breaking down the problem into smaller functions, each responsible for a specific task. This modular approach will make the code more manageable and easier to debug. Additionally, remember that Python has built-in functions with names like `or` and `min`, so you should use different names for your functions to avoid conflicts.