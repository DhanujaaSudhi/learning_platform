"""
Script to expand CURATED_PROBLEMS in problem_curated_data.py with more curated entries.
"""

EXTRA_CURATED = {
    "Positive/Negative/Zero": {
        "description": """🎯 What is this problem asking?
Determine whether a given number is Positive (greater than 0), Negative (less than 0), or Zero (exactly 0).

💡 Real-World Analogy (For Non-IT Beginners):
Think of a thermometer showing temperature:
• Above 0°C: Warm weather (Positive).
• Below 0°C: Freezing weather (Negative).
• Exactly 0°C: Freezing point (Zero).
Or think of your bank balance: having money is positive, owing debt is negative, and an empty account is zero!

📥 Example:
• Input: 5 → Output: Positive
• Input: -3 → Output: Negative
• Input: 0 → Output: Zero

🧠 Step-by-Step Logic (The Plan):
1. Ask the user for a number.
2. Check if `n > 0` → print "Positive".
3. Check if `n < 0` → print "Negative".
4. Otherwise → print "Zero".""",
        "python_code": """n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")""",
        "example_input": "5",
        "example_output": "Positive",
        "explanation": [
            {
                "line": 1,
                "code": "n = int(input(\"Enter a number: \"))",
                "explanation": "Input Collection: Asks the user to enter a number and converts it to an integer."
            },
            {
                "line": 2,
                "code": "if n > 0:",
                "explanation": "Positive Test: Checks if the number is greater than zero."
            },
            {
                "line": 3,
                "code": "elif n < 0:",
                "explanation": "Negative Test: If not positive, checks if the number is less than zero."
            },
            {
                "line": 4,
                "code": "else:",
                "explanation": "Zero Check: If a number is neither positive nor negative, it must be zero."
            }
        ],
        "dry_run": {
            "input": "5",
            "steps": [
                {"iteration": 1, "condition": "5 > 0", "result": "True", "variables": {"n": 5}, "explanation": "5 is greater than 0, prints 'Positive'."}
            ]
        },
        "time_complexity": "O(1) - Instant comparison",
        "space_complexity": "O(1) - Single variable"
    },
    "GCD": {
        "description": """🎯 What is this problem asking?
Find the Greatest Common Divisor (GCD) of two numbers — the largest number that divides both numbers evenly without leaving any remainder.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you have two rectangular rooms: one is 12 feet long and the other is 18 feet long.
You want to buy square floor tiles of the largest possible size that can tile both rooms perfectly without cutting any tiles.
Tiles of 1 ft work, 2 ft work, 3 ft work, and 6 ft work!
6 ft is the largest tile that works for both. So GCD(12, 18) = 6!

📥 Example:
• Input: 12, 18 → Output: 6

🧠 Step-by-Step Logic (The Plan - Euclidean Algorithm):
1. Take two numbers `a` and `b`.
2. While `b` is not zero:
   - Replace `a` with `b`, and replace `b` with the remainder `a % b`.
3. When `b` becomes 0, `a` holds the GCD!""",
        "python_code": """a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b:
    a, b = b, a % b

print(a)""",
        "example_input": "12\n18",
        "example_output": "6",
        "explanation": [
            {
                "line": 1,
                "code": "while b:",
                "explanation": "Euclidean Loop: Keeps running as long as 'b' is not zero. In Python, any non-zero number is treated as True."
            },
            {
                "line": 2,
                "code": "a, b = b, a % b",
                "explanation": "Remainder Step: Shifts 'b' into 'a', and sets 'b' to the remainder when the old 'a' is divided by the old 'b'. This shrinks the numbers very rapidly."
            },
            {
                "line": 3,
                "code": "print(a)",
                "explanation": "The Result: When 'b' reaches 0, 'a' contains the greatest common factor."
            }
        ],
        "dry_run": {
            "input": "a = 12, b = 18",
            "steps": [
                {"iteration": 1, "condition": "b = 18 != 0", "result": "12 % 18 = 12", "variables": {"a": 18, "b": 12}, "explanation": "a becomes 18, b becomes 12."},
                {"iteration": 2, "condition": "b = 12 != 0", "result": "18 % 12 = 6", "variables": {"a": 12, "b": 6}, "explanation": "a becomes 12, b becomes 6."},
                {"iteration": 3, "condition": "b = 6 != 0", "result": "12 % 6 = 0", "variables": {"a": 6, "b": 0}, "explanation": "a becomes 6, b becomes 0. Loop finishes. GCD is 6!"}
            ]
        },
        "time_complexity": "O(log(min(A, B))) - Logarithmic, extraordinarily fast",
        "space_complexity": "O(1) - Two variables only"
    },
    "LCM": {
        "description": """🎯 What is this problem asking?
Find the Least Common Multiple (LCM) of two numbers — the smallest positive number that is a multiple of both numbers.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine two blinking lighthouse lights:
• Light A blinks every 4 seconds.
• Light B blinks every 6 seconds.
When will both lights blink at the exact same second?
Light A blinks at: 4, 8, 12, 16...
Light B blinks at: 6, 12, 18...
Both blink together at 12 seconds! So LCM(4, 6) = 12.

📥 Example:
• Input: 4, 6 → Output: 12

🧠 Step-by-Step Logic (The Plan):
1. We know the famous mathematical formula: `LCM(a, b) = (a * b) // GCD(a, b)`.
2. First calculate GCD using Euclidean algorithm.
3. Then divide their product by the GCD to get LCM!""",
        "python_code": """a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd
print(lcm)""",
        "example_input": "4\n6",
        "example_output": "12",
        "explanation": [
            {
                "line": 1,
                "code": "x, y = a, b",
                "explanation": "Working Copies: Copies a and b into x and y so we can calculate GCD without modifying original values."
            },
            {
                "line": 2,
                "code": "while y: x, y = y, x % y",
                "explanation": "GCD Computation: Repeatedly calculates remainder until y reaches 0."
            },
            {
                "line": 3,
                "code": "lcm = (a * b) // gcd",
                "explanation": "LCM Formula: Multiplies a and b and divides by their GCD."
            }
        ],
        "dry_run": {
            "input": "a = 4, b = 6",
            "steps": [
                {"iteration": 1, "condition": "Calculate GCD(4, 6)", "result": "GCD = 2", "variables": {"gcd": 2}, "explanation": "GCD of 4 and 6 is 2."},
                {"iteration": 2, "condition": "(4 * 6) // 2", "result": "12", "variables": {"lcm": 12}, "explanation": "24 // 2 = 12. LCM is 12."}
            ]
        },
        "time_complexity": "O(log(min(A, B))) - Dominated by GCD calculation",
        "space_complexity": "O(1) - Constant memory"
    },
    "Multiplication Table": {
        "description": """🎯 What is this problem asking?
Print the multiplication table of a given number from 1 to 10.

💡 Real-World Analogy (For Non-IT Beginners):
Like calculating the cost of tickets: if 1 ticket is $5, how much do 2 tickets, 3 tickets, ..., up to 10 tickets cost?

📥 Example:
• Input: 5
• Output:
  5 x 1 = 5
  5 x 2 = 10
  ...
  5 x 10 = 50

🧠 Step-by-Step Logic (The Plan):
1. Ask user for a number `n`.
2. Count from `i = 1` to `10`.
3. In each round, multiply `n * i` and print formatted string.""",
        "python_code": """n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)""",
        "example_input": "5",
        "example_output": "5 x 1 = 5\\n5 x 2 = 10\\n5 x 3 = 15\\n5 x 4 = 20\\n5 x 5 = 25\\n5 x 6 = 30\\n5 x 7 = 35\\n5 x 8 = 40\\n5 x 9 = 45\\n5 x 10 = 50",
        "explanation": [
            {
                "line": 1,
                "code": "for i in range(1, 11):",
                "explanation": "Counting from 1 to 10: 'range(1, 11)' produces numbers 1, 2, 3 ... 10."
            },
            {
                "line": 2,
                "code": "print(n, \"x\", i, \"=\", n * i)",
                "explanation": "Formulas & Output: Multiplies n by the current multiplier i and displays the equation."
            }
        ],
        "dry_run": {
            "input": "5",
            "steps": [
                {"iteration": 1, "condition": "i = 1", "result": "5 x 1 = 5", "variables": {"i": 1, "product": 5}, "explanation": "Printed 5 x 1 = 5."},
                {"iteration": 2, "condition": "i = 2", "result": "5 x 2 = 10", "variables": {"i": 2, "product": 10}, "explanation": "Printed 5 x 2 = 10."},
                {"iteration": 3, "condition": "i = 10", "result": "5 x 10 = 50", "variables": {"i": 10, "product": 50}, "explanation": "Printed 5 x 10 = 50. Loop complete."}
            ]
        },
        "time_complexity": "O(1) - Always prints exactly 10 lines",
        "space_complexity": "O(1) - Only loop variable used"
    },
    "Star Triangle": {
        "description": """🎯 What is this problem asking?
Print a right-angled triangle pattern of asterisks (*) with `n` rows, where row 1 has 1 star, row 2 has 2 stars, row 3 has 3 stars, and so on.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine stacking wooden blocks or building a staircase:
Step 1 has 1 block.
Step 2 has 2 blocks.
Step 3 has 3 blocks.
Each step you walk up adds one more block!

📥 Example:
• Input: 3
• Output:
  *
  **
  ***

🧠 Step-by-Step Logic (The Plan):
1. Ask for number of rows `n`.
2. Count `i` from 1 up to `n`.
3. In Python, multiplying a string `\"*\" * i` repeats the character `i` times!
4. Print each row.""",
        "python_code": """n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print("*" * i)""",
        "example_input": "3",
        "example_output": "*\\n**\\n***",
        "explanation": [
            {
                "line": 1,
                "code": "for i in range(1, n + 1):",
                "explanation": "Row Counter: Steps through row numbers from 1 up to n."
            },
            {
                "line": 2,
                "code": "print(\"*\" * i)",
                "explanation": "String Multiplication: In Python, '*' * 3 creates '***'. This prints i stars on row i."
            }
        ],
        "dry_run": {
            "input": "3",
            "steps": [
                {"iteration": 1, "condition": "i = 1", "result": "*", "variables": {"i": 1}, "explanation": "Row 1: prints 1 star (*)."},
                {"iteration": 2, "condition": "i = 2", "result": "**", "variables": {"i": 2}, "explanation": "Row 2: prints 2 stars (**)."},
                {"iteration": 3, "condition": "i = 3", "result": "***", "variables": {"i": 3}, "explanation": "Row 3: prints 3 stars (***)."}
            ]
        },
        "time_complexity": "O(N^2) - Prints total of N*(N+1)/2 stars",
        "space_complexity": "O(1) - No extra data structures"
    },
    "Decimal to Binary": {
        "description": """🎯 What is this problem asking?
Convert a standard base-10 decimal number (like 10) into base-2 binary representation (like 1010) using only 0s and 1s.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine a row of light switches that can only be either OFF (0) or ON (1).
Each switch represents a power of 2: 8, 4, 2, 1.
To make the number 10:
Turn ON the 8 switch (1)
Leave OFF the 4 switch (0)
Turn ON the 2 switch (1)
Leave OFF the 1 switch (0)
The switch pattern is 1 0 1 0!

📥 Example:
• Input: 10 → Output: 1010

🧠 Step-by-Step Logic (The Plan):
1. If the number is 0, the binary is 0.
2. While `n > 0`:
   - Find remainder when divided by 2 (`n % 2`) — this is the next binary digit.
   - Attach this digit to the front of our binary string.
   - Halve the number using integer division `n //= 2`.
3. Print the binary string!""",
        "python_code": """n = int(input("Enter a decimal number: "))

if n == 0:
    print(0)
else:
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    print(binary)""",
        "example_input": "10",
        "example_output": "1010",
        "explanation": [
            {
                "line": 1,
                "code": "binary = str(n % 2) + binary",
                "explanation": "Prepend Bit: The remainder (n % 2) gives either 0 or 1. We attach it to the FRONT of our binary string because binary is read left-to-right."
            },
            {
                "line": 2,
                "code": "n //= 2",
                "explanation": "Halving: Divides n by 2 and throws away the remainder, moving to the next power of 2."
            }
        ],
        "dry_run": {
            "input": "10",
            "steps": [
                {"iteration": 1, "condition": "10 % 2 = 0", "result": "binary = '0'", "variables": {"n": 5, "binary": "0"}, "explanation": "Remainder is 0. n becomes 5."},
                {"iteration": 2, "condition": "5 % 2 = 1", "result": "binary = '10'", "variables": {"n": 2, "binary": "10"}, "explanation": "Remainder is 1. n becomes 2."},
                {"iteration": 3, "condition": "2 % 2 = 0", "result": "binary = '010'", "variables": {"n": 1, "binary": "010"}, "explanation": "Remainder is 0. n becomes 1."},
                {"iteration": 4, "condition": "1 % 2 = 1", "result": "binary = '1010'", "variables": {"n": 0, "binary": "1010"}, "explanation": "Remainder is 1. n becomes 0. Final binary is 1010."}
            ]
        },
        "time_complexity": "O(log2(N)) - Number of bits is proportional to log2 of N",
        "space_complexity": "O(log2(N)) - String to store the binary digits"
    }
}

import problem_curated_data
problem_curated_data.CURATED_PROBLEMS.update(EXTRA_CURATED)

# Re-serialize to file
with open("problem_curated_data.py", "w", encoding="utf-8") as f:
    f.write('"""\nCurated high-detail, non-IT friendly educational data for PySolve Academy.\n"""\n\nCURATED_PROBLEMS = ' + repr(problem_curated_data.CURATED_PROBLEMS) + '\n')

print(f"Total curated problems now: {len(problem_curated_data.CURATED_PROBLEMS)}")
