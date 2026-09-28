"""
Curated high-detail, non-IT friendly educational data for PySolve Academy.
Each entry provides:
- A non-technical description with real-world everyday analogy
- Clean, executable Python code
- Default sample input and expected output
- Detailed step-by-step line-by-line explanations
- Concrete multi-step dry runs tracing variables
"""

CURATED_PROBLEMS = {
    "Reverse a Number": {
        "description": """🎯 What is this problem asking?
You are given a whole number (for example: 123), and your task is to flip the order of its digits so that the last digit becomes the first, resulting in 321.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you wrote the numbers "1", "2", and "3" on separate playing cards laid out in a row on a table.
To reverse them, you pick up the rightmost card ('3') and place it on a new row first.
Next, you pick up the next card ('2') and place it right after '3'.
Finally, you take the last card ('1') and put it at the end.
Your new row now reads: 3 2 1!
In computer programming, we do the exact same card-picking using two simple math tricks:
1. `% 10` (Remainder Division) grabs the last digit.
2. `// 10` (Integer Division) throws away the last digit.

📥 Example:
• Input: 123
• Output: 321

🧠 Step-by-Step Logic (The Plan):
1. Start with an empty result bucket: `reverse = 0`.
2. As long as our number has digits left (greater than 0):
   a. Snip off the last digit using `n % 10`.
   b. Slide our accumulated reversed number to the left (multiply by 10) and glue on the new digit.
   c. Remove the last digit from the original number using `n //= 10`.
3. When the original number becomes 0, print the reversed number!""",
        "python_code": """n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)""",
        "example_input": "123",
        "example_output": "321",
        "explanation": [
            {
                "line": 1,
                "code": "n = int(input(\"Enter a number: \"))",
                "explanation": "Asking for User Input: 'input()' waits for the user to type a value (e.g. '123') as text. 'int()' converts that text into an actual numerical integer so we can perform math on it, and stores it in variable 'n'."
            },
            {
                "line": 2,
                "code": "reverse = 0",
                "explanation": "The Result Bucket: Creates a variable named 'reverse' starting at 0. This is our empty container where we will build up the backwards number digit-by-digit."
            },
            {
                "line": 3,
                "code": "while n > 0:",
                "explanation": "The Repetition Loop: Tells Python to keep repeating the indented lines below as long as 'n' is greater than 0. Each round of the loop processes one single digit."
            },
            {
                "line": 4,
                "code": "digit = n % 10",
                "explanation": "Peeling the Last Digit: The percent sign (%) is the modulus operator. Dividing any number by 10 leaves the exact last digit as remainder! For 123, 123 % 10 gives 3."
            },
            {
                "line": 5,
                "code": "reverse = reverse * 10 + digit",
                "explanation": "Assembling the Backwards Number: Multiplying our existing reversed number by 10 shifts its digits one spot to the left (e.g., 3 becomes 30), and adding 'digit' places the new digit into the ones spot. (0 * 10 + 3 = 3, next round: 3 * 10 + 2 = 32)."
            },
            {
                "line": 6,
                "code": "n //= 10",
                "explanation": "Discarding the Used Digit: The double-slash (//) is integer division. Dividing by 10 cuts off the rightmost digit. For 123, 123 // 10 leaves 12. In the next round, 12 // 10 leaves 1, and 1 // 10 leaves 0."
            },
            {
                "line": 7,
                "code": "print(reverse)",
                "explanation": "Showing the Answer: Once the while loop finishes because 'n' reached 0, Python prints the completed reversed number (321) to the screen."
            }
        ],
        "dry_run": {
            "input": "123",
            "steps": [
                {
                    "iteration": 1,
                    "condition": "n > 0 (123 > 0)",
                    "result": "True",
                    "variables": {"n": 12, "digit": 3, "reverse": 3},
                    "explanation": "Extracted last digit 3 (123 % 10). reverse becomes (0 * 10) + 3 = 3. Removed last digit from n (123 // 10 = 12)."
                },
                {
                    "iteration": 2,
                    "condition": "n > 0 (12 > 0)",
                    "result": "True",
                    "variables": {"n": 1, "digit": 2, "reverse": 32},
                    "explanation": "Extracted last digit 2 (12 % 10). reverse becomes (3 * 10) + 2 = 32. Removed last digit from n (12 // 10 = 1)."
                },
                {
                    "iteration": 3,
                    "condition": "n > 0 (1 > 0)",
                    "result": "True",
                    "variables": {"n": 0, "digit": 1, "reverse": 321},
                    "explanation": "Extracted last digit 1 (1 % 10). reverse becomes (32 * 10) + 1 = 321. Removed last digit from n (1 // 10 = 0)."
                },
                {
                    "iteration": 4,
                    "condition": "n > 0 (0 > 0)",
                    "result": "False",
                    "variables": {"reverse": 321},
                    "explanation": "Condition is False because n is now 0. Loop terminates. Final reversed number 321 is output."
                }
            ]
        },
        "time_complexity": "O(log10(N)) - Time taken is proportional to the number of digits",
        "space_complexity": "O(1) - Uses a single variable to store the reversed number"
    },
    "Even or Odd": {
        "description": """🎯 What is this problem asking?
Determine whether a given whole number is Even (can be divided into two equal groups with nothing left over) or Odd (leaves 1 left over when paired up).

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you have a bag of candies and two children.
If you can divide all the candies between the two children so each gets the exact same amount with ZERO candies left over, the number is Even (like 2, 4, 6, 8, 10...).
If there is 1 lonely candy left over that cannot be paired, the number is Odd (like 1, 3, 5, 7, 9...).

📥 Example:
• Input: 10 → Output: Even
• Input: 7 → Output: Odd

🧠 Step-by-Step Logic (The Plan):
1. Ask the user for a number.
2. Check the remainder when dividing the number by 2 using `% 2`.
3. If remainder is 0, print "Even".
4. Otherwise, print "Odd".""",
        "python_code": """n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")""",
        "example_input": "10",
        "example_output": "Even",
        "explanation": [
            {
                "line": 1,
                "code": "n = int(input(\"Enter a number: \"))",
                "explanation": "Reading Input: Prompts the user to type a number, converts that text into an integer, and saves it in variable 'n'."
            },
            {
                "line": 2,
                "code": "if n % 2 == 0:",
                "explanation": "The Even Test: The '%' operator calculates the remainder after dividing by 2. If 'n % 2 == 0', it means the number divides perfectly by 2 with 0 left over, so it is Even."
            },
            {
                "line": 3,
                "code": "    print(\"Even\")",
                "explanation": "Action for Even: If the condition above was true, Python prints 'Even' and skips the rest."
            },
            {
                "line": 4,
                "code": "else:",
                "explanation": "The Fallback: If the remainder was not 0 (meaning there was 1 left over), Python jumps here."
            },
            {
                "line": 5,
                "code": "    print(\"Odd\")",
                "explanation": "Action for Odd: Prints 'Odd' on the screen."
            }
        ],
        "dry_run": {
            "input": "10",
            "steps": [
                {
                    "iteration": 1,
                    "condition": "10 % 2 == 0",
                    "result": "True",
                    "variables": {"n": 10, "remainder": 0},
                    "explanation": "10 divided by 2 is 5 with remainder 0. Condition (0 == 0) is True, so 'Even' is printed."
                }
            ]
        },
        "time_complexity": "O(1) - Instantaneous single arithmetic check",
        "space_complexity": "O(1) - Only one variable stored"
    },
    "Prime Number": {
        "description": """🎯 What is this problem asking?
Check if a given number is a Prime Number. A prime number is a number greater than 1 that can ONLY be divided evenly by 1 and by itself.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you are organizing a team of dancers into a rectangular formation on stage (with at least 2 rows and 2 columns).
If you have 6 dancers, you can arrange them into 2 rows of 3 (so 6 is NOT prime).
If you have 8 dancers, you can make 2 rows of 4 (NOT prime).
If you have 7 dancers, you CANNOT arrange them into any rectangular formation other than a single straight line of 7! Numbers like 2, 3, 5, 7, 11, 13 are Primes.

📥 Example:
• Input: 11 → Output: Prime Number
• Input: 9 → Output: Not Prime Number (since 3 x 3 = 9)

🧠 Step-by-Step Logic (The Plan):
1. Numbers less than or equal to 1 are never prime.
2. For numbers 2 and above, test if any number from 2 up to the square root of n divides it evenly.
3. If any number divides it with remainder 0, it's NOT prime (break out of loop).
4. If no divisor was found, celebrate — it's a Prime Number!""",
        "python_code": """n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime Number")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")""",
        "example_input": "11",
        "example_output": "Prime Number",
        "explanation": [
            {
                "line": 1,
                "code": "n = int(input(\"Enter a number: \"))",
                "explanation": "Collects the number from the user and stores it in variable 'n'."
            },
            {
                "line": 2,
                "code": "if n <= 1:",
                "explanation": "Rule Check: By mathematical definition, prime numbers must be strictly greater than 1. So 0, 1, or negative numbers are rejected immediately."
            },
            {
                "line": 3,
                "code": "is_prime = True",
                "explanation": "Innocent Until Proven Guilty: We assume the number is prime by setting a boolean flag 'is_prime' to True, then look for evidence that it is not."
            },
            {
                "line": 4,
                "code": "for i in range(2, int(n ** 0.5) + 1):",
                "explanation": "Efficient Trial Division: We check potential divisors starting at 2 up to the square root of n. (If a number has a factor, at least one factor must be less than or equal to its square root, saving huge time!)."
            },
            {
                "line": 5,
                "code": "    if n % i == 0:",
                "explanation": "Divisibility Test: If 'n' divides cleanly by 'i' with remainder 0, then 'i' is a factor."
            },
            {
                "line": 6,
                "code": "        is_prime = False; break",
                "explanation": "Caught: Since we found a factor other than 1 and n, the number cannot be prime. We set 'is_prime = False' and immediately exit the loop."
            },
            {
                "line": 7,
                "code": "if is_prime: print(\"Prime Number\") else: print(\"Not Prime Number\")",
                "explanation": "Final Verdict: Checks our flag. If still True, prints 'Prime Number', otherwise prints 'Not Prime Number'."
            }
        ],
        "dry_run": {
            "input": "11",
            "steps": [
                {
                    "iteration": 1,
                    "condition": "i = 2, 11 % 2 == 0",
                    "result": "False",
                    "variables": {"n": 11, "i": 2, "remainder": 1},
                    "explanation": "11 / 2 gives remainder 1. Not divisible."
                },
                {
                    "iteration": 2,
                    "condition": "i = 3, 11 % 3 == 0",
                    "result": "False",
                    "variables": {"n": 11, "i": 3, "remainder": 2},
                    "explanation": "11 / 3 gives remainder 2. Loop finishes because limit int(11**0.5) is 3. is_prime remains True!"
                }
            ]
        },
        "time_complexity": "O(sqrt(N)) - Only checks numbers up to the square root of N",
        "space_complexity": "O(1) - Uses a single boolean flag and loop counter"
    },
    "Palindrome Number": {
        "description": """🎯 What is this problem asking?
Check if a number reads exactly the same forwards and backwards. For example, 121 reversed is still 121 (so it IS a Palindrome), but 123 reversed is 321 (NOT a Palindrome).

💡 Real-World Analogy (For Non-IT Beginners):
Think of words like "MADAM", "RADAR", or the date "12-02-2021".
No matter whether you read from left to right or right to left, the characters are identical.
It's like looking into a symmetrical mirror!

📥 Example:
• Input: 121 → Output: Palindrome Number
• Input: 123 → Output: Not Palindrome Number

🧠 Step-by-Step Logic (The Plan):
1. Keep a backup copy of the original number (`original = n`).
2. Reverse the digits of `n` using `% 10` and `// 10` (just like in Reverse a Number).
3. Compare the reversed number with the backup `original`.
4. If they match, it's a Palindrome!""",
        "python_code": """n = int(input("Enter a number: "))
original = n
reverse = 0

while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")""",
        "example_input": "121",
        "example_output": "Palindrome Number",
        "explanation": [
            {
                "line": 1,
                "code": "original = n",
                "explanation": "Saving a Backup: Because the while loop below will chop off digits until n becomes 0, we must save a copy of the starting number in 'original' so we can compare it later."
            },
            {
                "line": 2,
                "code": "reverse = reverse * 10 + n % 10; n //= 10",
                "explanation": "Digit Flipping: Each iteration extracts the last digit (n % 10), attaches it onto 'reverse', and removes it from 'n'."
            },
            {
                "line": 3,
                "code": "if original == reverse:",
                "explanation": "The Comparison: Checks if the reversed number equals the original untouched starting number."
            }
        ],
        "dry_run": {
            "input": "121",
            "steps": [
                {
                    "iteration": 1,
                    "condition": "n > 0 (121 > 0)",
                    "result": "True",
                    "variables": {"n": 12, "reverse": 1},
                    "explanation": "Extracted digit 1. reverse = 1, remaining n = 12."
                },
                {
                    "iteration": 2,
                    "condition": "n > 0 (12 > 0)",
                    "result": "True",
                    "variables": {"n": 1, "reverse": 12},
                    "explanation": "Extracted digit 2. reverse = 1*10 + 2 = 12, remaining n = 1."
                },
                {
                    "iteration": 3,
                    "condition": "n > 0 (1 > 0)",
                    "result": "True",
                    "variables": {"n": 0, "reverse": 121},
                    "explanation": "Extracted digit 1. reverse = 12*10 + 1 = 121, remaining n = 0."
                },
                {
                    "iteration": 4,
                    "condition": "original == reverse (121 == 121)",
                    "result": "True",
                    "variables": {"original": 121, "reverse": 121},
                    "explanation": "The reversed number matches original! Prints 'Palindrome Number'."
                }
            ]
        },
        "time_complexity": "O(log10(N)) - Time taken to reverse the digits",
        "space_complexity": "O(1) - Only stores a couple of integers"
    },
    "Armstrong Number": {
        "description": """🎯 What is this problem asking?
An Armstrong number (also known as a Narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
For example: 153 has 3 digits.
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153! Since 153 == 153, it is an Armstrong number!

💡 Real-World Analogy (For Non-IT Beginners):
Imagine a family of 3 people whose family reputation score is 153.
If each member boosts their personal score by raising it to the power of 3 (the family size), and the sum of their boosted scores brings you right back to 153, this family has the rare "Armstrong harmony"!

📥 Example:
• Input: 153 → Output: Armstrong Number
• Input: 123 → Output: Not Armstrong Number (1^3 + 2^3 + 3^3 = 36 != 123)

🧠 Step-by-Step Logic (The Plan):
1. Find how many digits the number has (count of digits = power).
2. Peel each digit one by one.
3. Multiply each digit by itself 'power' times (digit ** power) and add to total.
4. If total equals the original number, it's an Armstrong Number!""",
        "python_code": """n = int(input("Enter a number: "))
original = n
power = len(str(abs(n)))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10

if original == total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")""",
        "example_input": "153",
        "example_output": "Armstrong Number",
        "explanation": [
            {
                "line": 1,
                "code": "power = len(str(abs(n)))",
                "explanation": "Determining Family Size (Number of Digits): Converts the number into text (str) so we can count how many digits it has (len). For 153, power = 3."
            },
            {
                "line": 2,
                "code": "total += digit ** power",
                "explanation": "Power and Sum: '**' raises the digit to the power (e.g. 5 ** 3 = 125), and adds it to our running total."
            },
            {
                "line": 3,
                "code": "if original == total:",
                "explanation": "Verification: Compares our calculated sum with the original starting number."
            }
        ],
        "dry_run": {
            "input": "153",
            "steps": [
                {
                    "iteration": 1,
                    "condition": "digit = 3",
                    "result": "3 ** 3 = 27",
                    "variables": {"total": 27, "n": 15},
                    "explanation": "Added 3^3 (27) to total. Remaining n is 15."
                },
                {
                    "iteration": 2,
                    "condition": "digit = 5",
                    "result": "5 ** 3 = 125",
                    "variables": {"total": 152, "n": 1},
                    "explanation": "Added 5^3 (125) to total (27 + 125 = 152). Remaining n is 1."
                },
                {
                    "iteration": 3,
                    "condition": "digit = 1",
                    "result": "1 ** 3 = 1",
                    "variables": {"total": 153, "n": 0},
                    "explanation": "Added 1^3 (1) to total (152 + 1 = 153). Loop ends."
                }
            ]
        },
        "time_complexity": "O(log10(N)) - Iterates through each digit of the number",
        "space_complexity": "O(1) - Constant memory"
    },
    "Factorial": {
        "description": """🎯 What is this problem asking?
Compute the Factorial of a number n (written as n!).
The factorial is the product of all positive whole numbers from 1 up to n.
For example: 5! = 5 × 4 × 3 × 2 × 1 = 120.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you have 5 different books and you want to know how many different ways you can arrange them side-by-side on a bookshelf.
For the 1st spot, you have 5 choices.
For the 2nd spot, you have 4 choices left.
For the 3rd spot, 3 choices.
For the 4th spot, 2 choices.
For the last spot, only 1 choice.
Total arrangements = 5 × 4 × 3 × 2 × 1 = 120 arrangements!

📥 Example:
• Input: 5 → Output: 120

🧠 Step-by-Step Logic (The Plan):
1. Start with an accumulator `fact = 1` (because multiplying by 1 keeps numbers intact).
2. Count from 1 up to `n`.
3. At each step, multiply `fact` by the current number.
4. When done, print `fact`.""",
        "python_code": """n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)""",
        "example_input": "5",
        "example_output": "120",
        "explanation": [
            {
                "line": 1,
                "code": "fact = 1",
                "explanation": "The Multiplier Base: We initialize 'fact' to 1. (Note: Never initialize to 0 for multiplication, because 0 times anything is 0!)."
            },
            {
                "line": 2,
                "code": "for i in range(1, n + 1):",
                "explanation": "The Counting Loop: 'range(1, n + 1)' steps through every whole number from 1, 2, 3 ... up to 'n' inclusive."
            },
            {
                "line": 3,
                "code": "    fact *= i",
                "explanation": "Multiplication Step: Multiplies our current product by 'i' and stores the new product back into 'fact'."
            }
        ],
        "dry_run": {
            "input": "5",
            "steps": [
                {"iteration": 1, "condition": "i = 1", "result": "1 * 1 = 1", "variables": {"i": 1, "fact": 1}, "explanation": "fact = 1 * 1 = 1"},
                {"iteration": 2, "condition": "i = 2", "result": "1 * 2 = 2", "variables": {"i": 2, "fact": 2}, "explanation": "fact = 1 * 2 = 2"},
                {"iteration": 3, "condition": "i = 3", "result": "2 * 3 = 6", "variables": {"i": 3, "fact": 6}, "explanation": "fact = 2 * 3 = 6"},
                {"iteration": 4, "condition": "i = 4", "result": "6 * 4 = 24", "variables": {"i": 4, "fact": 24}, "explanation": "fact = 6 * 4 = 24"},
                {"iteration": 5, "condition": "i = 5", "result": "24 * 5 = 120", "variables": {"i": 5, "fact": 120}, "explanation": "fact = 24 * 5 = 120. Loop finishes."}
            ]
        },
        "time_complexity": "O(N) - Performs N multiplications",
        "space_complexity": "O(1) - Only stores the running product"
    },
    "Fibonacci Series": {
        "description": """🎯 What is this problem asking?
Print the first n numbers of the famous Fibonacci sequence.
The sequence starts with 0 and 1, and every subsequent number is found by adding the previous two numbers together:
0, 1, 1, 2, 3, 5, 8, 13, 21...

💡 Real-World Analogy (For Non-IT Beginners):
This sequence is everywhere in nature!
Count the petals on a daisy, the spirals on a sunflower, or the scales of a pinecone — nature almost always grows using Fibonacci numbers.
Think of it like a relay race: runner A hands off to runner B, and the next runner's distance is the sum of both runners' distances!

📥 Example:
• Input: 5 → Output: 0 1 1 2 3

🧠 Step-by-Step Logic (The Plan):
1. Start with the first two numbers: `a = 0` and `b = 1`.
2. For each of the `n` terms:
   a. Print `a`.
   b. Slide forward: `a` becomes `b`, and `b` becomes the sum `a + b`.""",
        "python_code": """n = int(input("Enter number of terms: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b""",
        "example_input": "5",
        "example_output": "0 1 1 2 3 ",
        "explanation": [
            {
                "line": 1,
                "code": "a, b = 0, 1",
                "explanation": "The Starting Seeds: Sets the first two terms of the sequence: 'a = 0' and 'b = 1'."
            },
            {
                "line": 2,
                "code": "print(a, end=\" \")",
                "explanation": "Printing on the Same Line: Outputs the current term 'a' followed by a space instead of jumping to a new line."
            },
            {
                "line": 3,
                "code": "a, b = b, a + b",
                "explanation": "Simultaneous Slide: Simultaneously moves 'a' to the next position 'b', and calculates the new term 'a + b' for 'b'."
            }
        ],
        "dry_run": {
            "input": "5",
            "steps": [
                {"iteration": 1, "condition": "print 0", "result": "a=0", "variables": {"a": 1, "b": 1}, "explanation": "Printed 0. Next a becomes 1, b becomes 0+1=1."},
                {"iteration": 2, "condition": "print 1", "result": "a=1", "variables": {"a": 1, "b": 2}, "explanation": "Printed 1. Next a becomes 1, b becomes 1+1=2."},
                {"iteration": 3, "condition": "print 1", "result": "a=1", "variables": {"a": 2, "b": 3}, "explanation": "Printed 1. Next a becomes 2, b becomes 1+2=3."},
                {"iteration": 4, "condition": "print 2", "result": "a=2", "variables": {"a": 3, "b": 5}, "explanation": "Printed 2. Next a becomes 3, b becomes 2+3=5."},
                {"iteration": 5, "condition": "print 3", "result": "a=3", "variables": {"a": 5, "b": 8}, "explanation": "Printed 3. All 5 terms printed!"}
            ]
        },
        "time_complexity": "O(N) - Generates each number in a single step",
        "space_complexity": "O(1) - Only keeps track of the last two values"
    },
    "Reverse String": {
        "description": """🎯 What is this problem asking?
Take a piece of text (string) such as "hello" and write it backwards so it becomes "olleh".

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you are spelling out words with magnetic refrigerator letters.
To flip the word "CAT", you take the rightmost letter 'T' and place it first on a new line. Then you take 'A', then 'C'. You get "TAC"!
In Python, we can do this instantly using slicing (`s[::-1]`) or a simple loop.

📥 Example:
• Input: hello → Output: olleh

🧠 Step-by-Step Logic (The Plan):
1. Ask the user for a word or phrase.
2. In Python, `s[::-1]` tells Python: "Walk through the entire string from end to beginning with a step of -1".
3. Print the reversed text!""",
        "python_code": """s = input("Enter a string: ")
reversed_s = s[::-1]
print(reversed_s)""",
        "example_input": "hello",
        "example_output": "olleh",
        "explanation": [
            {
                "line": 1,
                "code": "s = input(\"Enter a string: \")",
                "explanation": "Input Collection: Reads whatever word or sentence the user types and stores it in variable 's'."
            },
            {
                "line": 2,
                "code": "reversed_s = s[::-1]",
                "explanation": "Python's Slice Magic: The slice syntax '[start:stop:step]' with step '-1' instructs Python to step backwards through the entire string from right to left, returning the fully inverted string."
            },
            {
                "line": 3,
                "code": "print(reversed_s)",
                "explanation": "Displays the reversed word on the screen."
            }
        ],
        "dry_run": {
            "input": "hello",
            "steps": [
                {"iteration": 1, "condition": "Take character index 4", "result": "'o'", "variables": {"char": "o"}, "explanation": "Rightmost letter 'o' placed first."},
                {"iteration": 2, "condition": "Take character index 3", "result": "'l'", "variables": {"char": "l"}, "explanation": "Next letter 'l' attached: 'ol'."},
                {"iteration": 3, "condition": "Take character index 2", "result": "'l'", "variables": {"char": "l"}, "explanation": "Next letter 'l' attached: 'oll'."},
                {"iteration": 4, "condition": "Take character index 1", "result": "'e'", "variables": {"char": "e"}, "explanation": "Next letter 'e' attached: 'olle'."},
                {"iteration": 5, "condition": "Take character index 0", "result": "'h'", "variables": {"char": "h"}, "explanation": "First letter 'h' attached last: 'olleh'."}
            ]
        },
        "time_complexity": "O(N) - Copies N characters into the new reversed string",
        "space_complexity": "O(N) - Memory for the new reversed string"
    },
    "Check Palindrome": {
        "description": """🎯 What is this problem asking?
Check if a given string reads the exact same forwards and backwards, ignoring case.
For example, "racecar" or "madam" backwards is still "racecar" and "madam".

💡 Real-World Analogy (For Non-IT Beginners):
Imagine looking at a word in a hand mirror. If the reflection in the mirror shows the exact same sequence of letters as the original word, it's a Palindrome!

📥 Example:
• Input: racecar → Output: Palindrome
• Input: python → Output: Not Palindrome

🧠 Step-by-Step Logic (The Plan):
1. Clean the string (convert to lowercase so 'Madam' matches 'madam').
2. Compare the string with its reversed version.
3. If they are equal, it's a Palindrome; otherwise, it's not.""",
        "python_code": """s = input("Enter a string: ").strip().lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")""",
        "example_input": "racecar",
        "example_output": "Palindrome",
        "explanation": [
            {
                "line": 1,
                "code": "s = input(...).strip().lower()",
                "explanation": "Standardizing Text: Removes surrounding accidental spaces (strip) and converts all letters to lowercase so capitalization differences don't cause false mismatches."
            },
            {
                "line": 2,
                "code": "if s == s[::-1]:",
                "explanation": "Mirror Check: Compares the forward string 's' with its reversed twin 's[::-1]'."
            },
            {
                "line": 3,
                "code": "    print(\"Palindrome\")",
                "explanation": "Output: If identical, prints 'Palindrome', otherwise 'Not Palindrome'."
            }
        ],
        "dry_run": {
            "input": "racecar",
            "steps": [
                {"iteration": 1, "condition": "Compare forwards vs backwards", "result": "'racecar' == 'racecar'", "variables": {"s": "racecar", "reverse": "racecar"}, "explanation": "Both match character by character. Result is Palindrome!"}
            ]
        },
        "time_complexity": "O(N) - Compares N characters",
        "space_complexity": "O(N) - Holds the reversed copy"
    },
    "Find Maximum": {
        "description": """🎯 What is this problem asking?
Given a list of numbers, find the single largest (maximum) number in the entire list.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine a group of people standing in a line and you want to find the tallest person.
You look at the first person and say: "You are the tallest so far!"
Then you walk to the second person. If they are taller, they become your new champion!
If they are shorter, you keep your previous champion.
By the time you reach the end of the line, whoever holds the title is guaranteed to be the tallest person overall!

📥 Example:
• Input: 10 45 23 89 12 → Output: 89

🧠 Step-by-Step Logic (The Plan):
1. Assume the very first number is the maximum champion (`max_val = nums[0]`).
2. Walk through every remaining number in the list:
   - If the current number is bigger than `max_val`, update `max_val` to this new number.
3. Print `max_val`!""",
        "python_code": """nums = list(map(int, input("Enter numbers separated by space: ").split()))

max_val = nums[0]
for num in nums[1:]:
    if num > max_val:
        max_val = num

print(max_val)""",
        "example_input": "10 45 23 89 12",
        "example_output": "89",
        "explanation": [
            {
                "line": 1,
                "code": "nums = list(map(int, input(...).split()))",
                "explanation": "Reading Multiple Numbers: Takes space-separated numbers typed by user, splits them by spaces, converts each into an integer, and stores them in list 'nums'."
            },
            {
                "line": 2,
                "code": "max_val = nums[0]",
                "explanation": "Initial Champion: We start by assuming the very first number 'nums[0]' is our biggest so far."
            },
            {
                "line": 3,
                "code": "for num in nums[1:]:",
                "explanation": "Challenger Tour: Loops through every other number in the list from the second number onward."
            },
            {
                "line": 4,
                "code": "if num > max_val: max_val = num",
                "explanation": "Dethroning: If a challenger is strictly greater than our current champion, it claims the crown as the new 'max_val'."
            }
        ],
        "dry_run": {
            "input": "10 45 23 89 12",
            "steps": [
                {"iteration": 1, "condition": "Start with nums[0] = 10", "result": "max_val = 10", "variables": {"max_val": 10}, "explanation": "Initial champion is 10."},
                {"iteration": 2, "condition": "num = 45 > 10", "result": "True", "variables": {"max_val": 45}, "explanation": "45 is larger than 10. New champion is 45."},
                {"iteration": 3, "condition": "num = 23 > 45", "result": "False", "variables": {"max_val": 45}, "explanation": "23 is not larger than 45. max_val stays 45."},
                {"iteration": 4, "condition": "num = 89 > 45", "result": "True", "variables": {"max_val": 89}, "explanation": "89 is larger than 45. New champion is 89."},
                {"iteration": 5, "condition": "num = 12 > 89", "result": "False", "variables": {"max_val": 89}, "explanation": "12 is smaller than 89. max_val remains 89."}
            ]
        },
        "time_complexity": "O(N) - Visits each element in the list exactly once",
        "space_complexity": "O(1) - Stores one variable for the maximum"
    },
    "Linear Search": {
        "description": """🎯 What is this problem asking?
Search for a specific target value in a list by checking every element from left to right until you find it.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you lost your keys in your house.
You check Drawer #1. Not there.
You check Drawer #2. Not there.
You check Drawer #3. Found them!
You searched linearly, one item after another in sequence, until you located your target.

📥 Example:
• Input:
  List: 10 20 30 40 50
  Target: 30
• Output: Found at index 2

🧠 Step-by-Step Logic (The Plan):
1. Start at index 0.
2. Check if the element at the current index matches the target.
3. If yes, print the index and stop!
4. If you reach the end without finding it, print "Not Found".""",
        "python_code": """nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

found_index = -1
for i in range(len(nums)):
    if nums[i] == target:
        found_index = i
        break

if found_index != -1:
    print(f"Found at index {found_index}")
else:
    print("Not Found")""",
        "example_input": "10 20 30 40 50\n30",
        "example_output": "Found at index 2",
        "explanation": [
            {
                "line": 1,
                "code": "found_index = -1",
                "explanation": "Search Flag: Initialized to -1 (meaning 'Not yet found'). In Python, valid list indices start at 0, so -1 cleanly represents absence."
            },
            {
                "line": 2,
                "code": "for i in range(len(nums)):",
                "explanation": "Sequential Scanner: Goes through each index from 0 to len(nums)-1 one by one."
            },
            {
                "line": 3,
                "code": "if nums[i] == target: found_index = i; break",
                "explanation": "Target Hit: If the current element matches what we're looking for, we save the index 'i' and break out of the loop early so we don't waste time checking the rest."
            }
        ],
        "dry_run": {
            "input": "10 20 30 40 50 | target: 30",
            "steps": [
                {"iteration": 1, "condition": "nums[0] == 30 (10 == 30)", "result": "False", "variables": {"i": 0, "val": 10}, "explanation": "Index 0 is 10, does not match 30."},
                {"iteration": 2, "condition": "nums[1] == 30 (20 == 30)", "result": "False", "variables": {"i": 1, "val": 20}, "explanation": "Index 1 is 20, does not match 30."},
                {"iteration": 3, "condition": "nums[2] == 30 (30 == 30)", "result": "True", "variables": {"i": 2, "val": 30}, "explanation": "Match found at index 2! Loop terminates."}
            ]
        },
        "time_complexity": "O(N) - In the worst case, checks every element in the list",
        "space_complexity": "O(1) - No extra memory needed"
    },
    "Binary Search": {
        "description": """🎯 What is this problem asking?
Quickly find a target number in an ALREADY SORTED list by repeatedly cutting the search area in half.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine looking for a word in a 1,000-page printed dictionary.
Do you start at page 1 and read every single page? Of course not!
You open the dictionary directly to the middle (page 500).
If your word starts with "T" and page 500 is "M", you know for a fact your word MUST be in the second half.
You discard pages 1 through 500 completely!
Then you split the remaining 500 pages in half.
In just 10 quick checks, you can find any word among a million pages!

📥 Example:
• Input:
  List: 2 4 6 8 10 12 14 16
  Target: 10
• Output: Found at index 4

🧠 Step-by-Step Logic (The Plan):
1. Set two boundaries: `left = 0` (start) and `right = last index`.
2. While `left <= right`:
   a. Find the middle index: `mid = (left + right) // 2`.
   b. If `nums[mid] == target`, we found it!
   c. If target is bigger than `nums[mid]`, target must be in the right half: set `left = mid + 1`.
   d. If target is smaller than `nums[mid]`, target must be in the left half: set `right = mid - 1`.
3. If boundaries cross without finding it, target isn't in the list.""",
        "python_code": """nums = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))

left = 0
right = len(nums) - 1
found_index = -1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        found_index = mid
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if found_index != -1:
    print(f"Found at index {found_index}")
else:
    print("Not Found")""",
        "example_input": "2 4 6 8 10 12 14 16\n10",
        "example_output": "Found at index 4",
        "explanation": [
            {
                "line": 1,
                "code": "left, right = 0, len(nums) - 1",
                "explanation": "Search Window Boundaries: 'left' points to the very first item, and 'right' points to the very last item of our searchable window."
            },
            {
                "line": 2,
                "code": "mid = (left + right) // 2",
                "explanation": "Finding the Center: Divides the window in half to inspect the middle element directly."
            },
            {
                "line": 3,
                "code": "if nums[mid] == target: found_index = mid; break",
                "explanation": "Bullseye: If the middle element is our target, we are done immediately."
            },
            {
                "line": 4,
                "code": "elif nums[mid] < target: left = mid + 1",
                "explanation": "Discarding the Left Half: Since the list is sorted and the middle value is smaller than what we want, the target can ONLY live in the right half. We move 'left' past 'mid'."
            },
            {
                "line": 5,
                "code": "else: right = mid - 1",
                "explanation": "Discarding the Right Half: Middle value is too big, so target can only live in the left half. We move 'right' before 'mid'."
            }
        ],
        "dry_run": {
            "input": "[2, 4, 6, 8, 10, 12, 14, 16] | target: 10",
            "steps": [
                {"iteration": 1, "condition": "left=0, right=7", "result": "mid=3 (val=8)", "variables": {"mid": 3, "val": 8}, "explanation": "Middle is 8. Since 8 < 10, discard left half. New left = 4."},
                {"iteration": 2, "condition": "left=4, right=7", "result": "mid=5 (val=12)", "variables": {"mid": 5, "val": 12}, "explanation": "Middle is 12. Since 12 > 10, discard right half. New right = 4."},
                {"iteration": 3, "condition": "left=4, right=4", "result": "mid=4 (val=10)", "variables": {"mid": 4, "val": 10}, "explanation": "Middle is 10. Exactly matches target! Found at index 4."}
            ]
        },
        "time_complexity": "O(log N) - Halves the search area at every step (extremely fast)",
        "space_complexity": "O(1) - Only uses two pointers"
    },
    "Bubble Sort": {
        "description": """🎯 What is this problem asking?
Sort an unsorted list of numbers in ascending order from smallest to largest using Bubble Sort.

💡 Real-World Analogy (For Non-IT Beginners):
Think of air bubbles underwater in a fish tank: the biggest bubbles rise to the surface fastest!
In Bubble Sort, we compare side-by-side neighbors:
If the left neighbor is bigger than the right neighbor, they swap places.
As we sweep across the list, the largest number 'bubbles up' to the very end of the list on the first pass.
We repeat this until every number settles into its proper sorted place.

📥 Example:
• Input: 5 1 4 2 8 → Output: 1 2 4 5 8

🧠 Step-by-Step Logic (The Plan):
1. Loop through the list `n` times.
2. In each round, compare adjacent items `nums[j]` and `nums[j+1]`.
3. If `nums[j] > nums[j+1]`, swap them!
4. If no swaps happened in a round, the list is already fully sorted!""",
        "python_code": """nums = list(map(int, input("Enter numbers: ").split()))
n = len(nums)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
    if not swapped:
        break

print(*nums)""",
        "example_input": "5 1 4 2 8",
        "example_output": "1 2 4 5 8",
        "explanation": [
            {
                "line": 1,
                "code": "for i in range(n):",
                "explanation": "Pass Counter: Each full pass ensures at least one more element reaches its final sorted destination at the end of the list."
            },
            {
                "line": 2,
                "code": "for j in range(0, n - i - 1):",
                "explanation": "Neighbor Comparison: Walks through adjacent pairs. We subtract 'i' because the last 'i' elements are already in their final sorted spots!"
            },
            {
                "line": 3,
                "code": "nums[j], nums[j + 1] = nums[j + 1], nums[j]",
                "explanation": "The Swap: If the left neighbor is greater than the right neighbor, swap them so the smaller number comes first."
            },
            {
                "line": 4,
                "code": "if not swapped: break",
                "explanation": "Smart Optimization: If an entire pass completes without a single swap, the list is already sorted! We can stop immediately."
            }
        ],
        "dry_run": {
            "input": "[5, 1, 4, 2, 8]",
            "steps": [
                {"iteration": 1, "condition": "Compare 5 and 1", "result": "Swap", "variables": {"arr": [1, 5, 4, 2, 8]}, "explanation": "5 > 1, so swap 5 and 1."},
                {"iteration": 2, "condition": "Compare 5 and 4", "result": "Swap", "variables": {"arr": [1, 4, 5, 2, 8]}, "explanation": "5 > 4, so swap 5 and 4."},
                {"iteration": 3, "condition": "Compare 5 and 2", "result": "Swap", "variables": {"arr": [1, 4, 2, 5, 8]}, "explanation": "5 > 2, so swap 5 and 2."},
                {"iteration": 4, "condition": "Compare 5 and 8", "result": "No swap", "variables": {"arr": [1, 4, 2, 5, 8]}, "explanation": "5 < 8, keep order. Largest element 8 is at end."}
            ]
        },
        "time_complexity": "O(N^2) - Compares pairs across nested loops",
        "space_complexity": "O(1) - Swaps numbers directly inside the list"
    },
    "Two Sum": {
        "description": """🎯 What is this problem asking?
Given a list of numbers and a target sum, find the two numbers (or their positions) that add up to the target.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you are at a grocery store checkout with a $10 gift card and want to buy exactly 2 items that cost $10 together.
You pick up a box of cereal costing $4.
You immediately know what you need to look for: $10 - $4 = $6!
Instead of wandering down every aisle checking pairs, you keep a quick notebook (Hash Map) of items you've seen.
As soon as you see a $6 carton of milk, you say: "Aha! $4 and $6 make $10!"

📥 Example:
• Input:
  List: 2 7 11 15
  Target: 9
• Output: Indices: [0, 1] (because 2 + 7 = 9)

🧠 Step-by-Step Logic (The Plan):
1. Create an empty dictionary/hashmap `seen = {}` to store numbers and their indices.
2. For each number in the list:
   a. Calculate the missing partner: `complement = target - num`.
   b. If `complement` is already in our notebook `seen`, we found our winning pair!
   c. Otherwise, write down the current number and its index in `seen` for future partners to find.""",
        "python_code": """nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

seen = {}
result = None

for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        result = [seen[complement], i]
        break
    seen[num] = i

if result:
    print(f"Indices: {result}")
else:
    print("No pair found")""",
        "example_input": "2 7 11 15\n9",
        "example_output": "Indices: [0, 1]",
        "explanation": [
            {
                "line": 1,
                "code": "seen = {}",
                "explanation": "The Memory Notebook: A dictionary where key = number seen, value = index where it was found."
            },
            {
                "line": 2,
                "code": "for i, num in enumerate(nums):",
                "explanation": "Enumerated Loop: Gives us both the position 'i' and the value 'num' at each step."
            },
            {
                "line": 3,
                "code": "complement = target - num",
                "explanation": "The Missing Partner: What number would we need to add to 'num' to reach our 'target'?"
            },
            {
                "line": 4,
                "code": "if complement in seen:",
                "explanation": "Instant Memory Lookup: Checks in O(1) instantaneous time if we already passed the missing partner earlier in our walk."
            },
            {
                "line": 5,
                "code": "seen[num] = i",
                "explanation": "Remembering for Later: If partner not yet seen, save current number in 'seen' so later elements can find it."
            }
        ],
        "dry_run": {
            "input": "[2, 7, 11, 15] | target: 9",
            "steps": [
                {"iteration": 1, "condition": "num = 2, complement = 9 - 2 = 7", "result": "7 in seen? False", "variables": {"seen": {2: 0}}, "explanation": "7 not yet seen. Saved {2: 0}."},
                {"iteration": 2, "condition": "num = 7, complement = 9 - 7 = 2", "result": "2 in seen? True!", "variables": {"result": [0, 1]}, "explanation": "2 was seen at index 0! Pair found at indices [0, 1]."}
            ]
        },
        "time_complexity": "O(N) - Only loops through the array once thanks to the hash map",
        "space_complexity": "O(N) - Stores seen numbers in the hash map"
    },
    "Balanced Parentheses": {
        "description": """🎯 What is this problem asking?
Determine whether every opening bracket `(`, `{`, `[` in a string has a corresponding correctly matched and closed bracket in the right order (e.g., `"{[()]}"` is valid, but `"{[(])}"` is invalid).

💡 Real-World Analogy (For Non-IT Beginners):
Imagine stacking colorful nesting bowls.
If you open a big green bowl `{`, then a medium blue bowl `[`, then a tiny yellow bowl `(`, you MUST close the tiny yellow bowl first `)` before you can put the lid on the blue bowl `]`, and finally the green bowl `}`.
If you try to close the big green bowl before closing the tiny yellow bowl, the lids won't fit!
In programming, we use a **Stack** (Last-In, First-Out) to remember the last opened bracket.

📥 Example:
• Input: {[()]} → Output: Balanced
• Input: {[(])} → Output: Not Balanced

🧠 Step-by-Step Logic (The Plan):
1. Create an empty `stack = []`.
2. Define matching pairs: `')' matches '(', '}' matches '{', ']' matches '['`.
3. For each character:
   a. If it's an opening bracket `( { [`, push it onto the top of the stack.
   b. If it's a closing bracket `) } ]`:
      - If the stack is empty, there is no opener! (Not balanced).
      - Pop the top bracket off the stack. If it doesn't match, (Not balanced).
4. At the end, if the stack is completely empty, all brackets were matched!""",
        "python_code": """s = input("Enter brackets string: ")

stack = []
bracket_map = {')': '(', '}': '{', ']': '['}
is_balanced = True

for char in s:
    if char in bracket_map.values():
        stack.append(char)
    elif char in bracket_map.keys():
        if not stack or stack.pop() != bracket_map[char]:
            is_balanced = False
            break

if is_balanced and len(stack) == 0:
    print("Balanced")
else:
    print("Not Balanced")""",
        "example_input": "{[()]}",
        "example_output": "Balanced",
        "explanation": [
            {
                "line": 1,
                "code": "stack = []",
                "explanation": "The Plate Stack: A list where we push opened brackets onto the top and pop the most recent one off."
            },
            {
                "line": 2,
                "code": "if char in bracket_map.values(): stack.append(char)",
                "explanation": "Pushing Opener: When an opening bracket like '{' or '[' appears, push it onto our stack."
            },
            {
                "line": 3,
                "code": "if not stack or stack.pop() != bracket_map[char]:",
                "explanation": "Closing Check: When a closer like '}' appears, remove the top opened bracket. If nothing was opened or the wrong bracket was on top, it's invalid."
            },
            {
                "line": 4,
                "code": "if is_balanced and len(stack) == 0:",
                "explanation": "Final Verification: If every opened bracket was closed and nothing is left stranded on the stack, it's Balanced!"
            }
        ],
        "dry_run": {
            "input": "{[()]}",
            "steps": [
                {"iteration": 1, "condition": "char = '{'", "result": "Push '{'", "variables": {"stack": ["{"]}, "explanation": "Opened '{', added to stack."},
                {"iteration": 2, "condition": "char = '['", "result": "Push '['", "variables": {"stack": ["{", "["]}, "explanation": "Opened '[', added to stack."},
                {"iteration": 3, "condition": "char = '('", "result": "Push '('", "variables": {"stack": ["{", "[", "("]}, "explanation": "Opened '(', added to stack."},
                {"iteration": 4, "condition": "char = ')'", "result": "Pop '(' matches ')'", "variables": {"stack": ["{", "["]}, "explanation": "Closing ')' matches top '('. Removed."},
                {"iteration": 5, "condition": "char = ']'", "result": "Pop '[' matches ']'", "variables": {"stack": ["{"]}, "explanation": "Closing ']' matches top '['. Removed."},
                {"iteration": 6, "condition": "char = '}'", "result": "Pop '{' matches '}'", "variables": {"stack": []}, "explanation": "Closing '}' matches top '{'. Stack is clean!"}
            ]
        },
        "time_complexity": "O(N) - Inspects each character once",
        "space_complexity": "O(N) - In worst case, stack holds N brackets"
    },
    "Kadane's Algorithm": {
        "description": """🎯 What is this problem asking?
Given a list of numbers containing both positive and negative integers, find the contiguous subarray (a slice of connected numbers) that produces the maximum possible sum.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you are tracking your daily business profits and losses:
+5, -2, +7, -10, +6.
As you look at consecutive streaks of days, if your cumulative streak ever drops into a negative deficit (e.g. -3 overall), there is no point carrying that baggage into future days!
You cut your losses, reset your streak to 0, and start a fresh streak on the next day.
This brilliant reset intuition is Kadane's Algorithm!

📥 Example:
• Input: -2 1 -3 4 -1 2 1 -5 4 → Output: 6 (The subarray [4, -1, 2, 1] gives 4 + (-1) + 2 + 1 = 6)

🧠 Step-by-Step Logic (The Plan):
1. Start `max_so_far = nums[0]` and `current_sum = 0`.
2. For each number in the list:
   a. Add it to `current_sum`.
   b. If `current_sum > max_so_far`, update `max_so_far`.
   c. If `current_sum < 0`, reset `current_sum = 0` (discard negative baggage).
3. Print `max_so_far`!""",
        "python_code": """nums = list(map(int, input("Enter numbers: ").split()))

max_so_far = nums[0]
current_sum = 0

for num in nums:
    current_sum += num
    if current_sum > max_so_far:
        max_so_far = current_sum
    if current_sum < 0:
        current_sum = 0

print(max_so_far)""",
        "example_input": "-2 1 -3 4 -1 2 1 -5 4",
        "example_output": "6",
        "explanation": [
            {
                "line": 1,
                "code": "max_so_far = nums[0]; current_sum = 0",
                "explanation": "Initialization: 'max_so_far' records the highest subarray sum found anywhere. 'current_sum' tracks the current ongoing streak."
            },
            {
                "line": 2,
                "code": "current_sum += num",
                "explanation": "Extending the Streak: Adds the current day's number to our active subarray streak."
            },
            {
                "line": 3,
                "code": "if current_sum > max_so_far: max_so_far = current_sum",
                "explanation": "New Record: If our active streak beats the historical best, update 'max_so_far'."
            },
            {
                "line": 4,
                "code": "if current_sum < 0: current_sum = 0",
                "explanation": "Cutting Losses: If our active streak becomes negative, carrying it into the future will only drag down future numbers. Reset to 0!"
            }
        ],
        "dry_run": {
            "input": "[-2, 1, -3, 4, -1, 2, 1, -5, 4]",
            "steps": [
                {"iteration": 1, "condition": "num = -2", "result": "current_sum = -2 < 0 -> reset", "variables": {"current_sum": 0, "max_so_far": -2}, "explanation": "Negative sum reset to 0."},
                {"iteration": 2, "condition": "num = 1", "result": "current_sum = 1 > -2", "variables": {"current_sum": 1, "max_so_far": 1}, "explanation": "Record updated to 1."},
                {"iteration": 3, "condition": "num = -3", "result": "current_sum = -2 < 0 -> reset", "variables": {"current_sum": 0, "max_so_far": 1}, "explanation": "Streak dipped below zero, reset."},
                {"iteration": 4, "condition": "num = 4", "result": "current_sum = 4 > 1", "variables": {"current_sum": 4, "max_so_far": 4}, "explanation": "New record: 4."},
                {"iteration": 5, "condition": "num = -1, 2, 1", "result": "current_sum reaches 6", "variables": {"current_sum": 6, "max_so_far": 6}, "explanation": "Subarray [4, -1, 2, 1] hits peak sum of 6!"}
            ]
        },
        "time_complexity": "O(N) - Solves the problem in a single blazing fast pass",
        "space_complexity": "O(1) - Only two numbers stored"
    },
    "Swap Two Numbers": {
        "description": """🎯 What is this problem asking?
Swap the values of two variables so that what was in 'a' goes into 'b', and what was in 'b' goes into 'a'.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you are holding an Apple in your left hand and an Orange in your right hand.
You want to switch them so the Orange is in your left hand and the Apple is in your right hand.
In Python, you can swap them instantly in a single move (`a, b = b, a`) just like crossing your arms!

📥 Example:
• Input: a = 2, b = 3
• Output: a = 3, b = 2

🧠 Step-by-Step Logic (The Plan):
1. Take values for a and b.
2. Swap their values using `a, b = b, a`.
3. Print the swapped results!""",
        "python_code": """a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("a =", a)
print("b =", b)""",
        "example_input": "2\n3",
        "example_output": "a = 3\nb = 2",
        "explanation": [
            {
                "line": 1,
                "code": "a = int(input(...)); b = int(input(...))",
                "explanation": "Input Collection: Stores the first number in variable 'a' and the second number in variable 'b'."
            },
            {
                "line": 2,
                "code": "a, b = b, a",
                "explanation": "Simultaneous Tuple Swap: Python evaluates the right side (b, a) first in memory and then assigns it to (a, b) at the exact same moment without needing a temporary third variable."
            },
            {
                "line": 3,
                "code": "print(\"a =\", a); print(\"b =\", b)",
                "explanation": "Displaying Swapped Values: Outputs the new value of 'a' and the new value of 'b'."
            }
        ],
        "dry_run": {
            "input": "a = 2, b = 3",
            "steps": [
                {"iteration": 1, "condition": "Before swap", "result": "a = 2, b = 3", "variables": {"a": 2, "b": 3}, "explanation": "Initial inputs."},
                {"iteration": 2, "condition": "Execute a, b = b, a", "result": "a = 3, b = 2", "variables": {"a": 3, "b": 2}, "explanation": "Values are swapped!"}
            ]
        },
        "time_complexity": "O(1) - Single instant assignment",
        "space_complexity": "O(1) - No extra memory"
    },
    "Sum of Digits": {
        "description": """🎯 What is this problem asking?
Add together all the individual digits of a number. For example, for 123, add 1 + 2 + 3 = 6.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine you open your piggy bank and empty out coins of values 1, 2, and 3 cents.
You count them together: 1 + 2 + 3 = 6 cents total!
In Python, we peel each coin (digit) from the number using `% 10` and add it to our piggy bank total.

📥 Example:
• Input: 123 → Output: 6

🧠 Step-by-Step Logic (The Plan):
1. Start `total = 0`.
2. While `n > 0`:
   a. Extract last digit: `digit = n % 10`.
   b. Add `digit` to `total`.
   c. Remove last digit: `n //= 10`.
3. Print `total`!""",
        "python_code": """n = int(input("Enter a number: "))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)""",
        "example_input": "123",
        "example_output": "6",
        "explanation": [
            {
                "line": 1,
                "code": "total = 0",
                "explanation": "Running Total: An empty accumulator that starts at 0 to collect the sum of digits."
            },
            {
                "line": 2,
                "code": "digit = n % 10",
                "explanation": "Peeling the Digit: Remainder operator gives the rightmost digit."
            },
            {
                "line": 3,
                "code": "total += digit",
                "explanation": "Adding to Sum: Adds the peeled digit into our running sum."
            },
            {
                "line": 4,
                "code": "n //= 10",
                "explanation": "Trimming: Chops off the used digit from the original number."
            }
        ],
        "dry_run": {
            "input": "123",
            "steps": [
                {"iteration": 1, "condition": "n = 123 > 0", "result": "digit = 3", "variables": {"total": 3, "n": 12}, "explanation": "Added 3 to total. Remaining n is 12."},
                {"iteration": 2, "condition": "n = 12 > 0", "result": "digit = 2", "variables": {"total": 5, "n": 1}, "explanation": "Added 2 to total (3 + 2 = 5). Remaining n is 1."},
                {"iteration": 3, "condition": "n = 1 > 0", "result": "digit = 1", "variables": {"total": 6, "n": 0}, "explanation": "Added 1 to total (5 + 1 = 6). Remaining n is 0. Loop ends."}
            ]
        },
        "time_complexity": "O(log10(N)) - Visits each digit once",
        "space_complexity": "O(1) - Only stores the running total"
    },
    "Count Digits": {
        "description": """🎯 What is this problem asking?
Count how many digits make up a given number. For example, 12345 has 5 digits.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine looking at a car's odometer or a digital clock. You count how many digit boxes are illuminated.
Or think of peeling petals off a daisy: every time you remove a digit, you click your handheld tally counter by 1 until no digits remain!

📥 Example:
• Input: 12345 → Output: 5

🧠 Step-by-Step Logic (The Plan):
1. If the number is 0, the digit count is 1.
2. Otherwise, start `count = 0`.
3. While `n > 0`:
   - Increment `count` by 1.
   - Remove the last digit using `n //= 10`.
4. Print `count`!""",
        "python_code": """n = abs(int(input("Enter a number: ")))
count = 1 if n == 0 else 0

while n > 0:
    count += 1
    n //= 10

print(count)""",
        "example_input": "12345",
        "example_output": "5",
        "explanation": [
            {
                "line": 1,
                "code": "n = abs(int(input(...)))",
                "explanation": "Absolute Value: 'abs()' makes sure negative signs like -123 don't confuse the counter (both -123 and 123 have 3 digits)."
            },
            {
                "line": 2,
                "code": "count = 1 if n == 0 else 0",
                "explanation": "Zero Edge Case: The number 0 has exactly 1 digit. For all other numbers, we start counting from 0."
            },
            {
                "line": 3,
                "code": "count += 1; n //= 10",
                "explanation": "Tally and Cut: Every loop iteration counts 1 digit and strips it off with integer division by 10."
            }
        ],
        "dry_run": {
            "input": "12345",
            "steps": [
                {"iteration": 1, "condition": "n = 12345 > 0", "result": "count = 1", "variables": {"n": 1234, "count": 1}, "explanation": "Counted digit 5. Remaining: 1234."},
                {"iteration": 2, "condition": "n = 1234 > 0", "result": "count = 2", "variables": {"n": 123, "count": 2}, "explanation": "Counted digit 4. Remaining: 123."},
                {"iteration": 3, "condition": "n = 123 > 0", "result": "count = 3", "variables": {"n": 12, "count": 3}, "explanation": "Counted digit 3. Remaining: 12."},
                {"iteration": 4, "condition": "n = 12 > 0", "result": "count = 4", "variables": {"n": 1, "count": 4}, "explanation": "Counted digit 2. Remaining: 1."},
                {"iteration": 5, "condition": "n = 1 > 0", "result": "count = 5", "variables": {"n": 0, "count": 5}, "explanation": "Counted digit 1. Remaining: 0. Final count is 5!"}
            ]
        },
        "time_complexity": "O(log10(N)) - Runs once per digit",
        "space_complexity": "O(1) - Single counter integer"
    },
    "Largest of 2 Numbers": {
        "description": """🎯 What is this problem asking?
Compare two numbers and determine which one is bigger.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine two children on a seesaw or comparing the price of two shirts on sale to find the more expensive one.
If the first shirt costs $25 and the second costs $15, $25 is the larger amount!

📥 Example:
• Input: 25, 15 → Output: 25

🧠 Step-by-Step Logic (The Plan):
1. Ask for two numbers `a` and `b`.
2. If `a > b`, print `a`.
3. Otherwise, print `b`!""",
        "python_code": """a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
else:
    print(b)""",
        "example_input": "25\n15",
        "example_output": "25",
        "explanation": [
            {
                "line": 1,
                "code": "if a > b:",
                "explanation": "Comparison: Tests if 'a' is strictly greater than 'b'."
            },
            {
                "line": 2,
                "code": "print(a) else: print(b)",
                "explanation": "Outcome: If 'a' wins, print 'a'. If 'b' is bigger or both are equal, print 'b'."
            }
        ],
        "dry_run": {
            "input": "a = 25, b = 15",
            "steps": [
                {"iteration": 1, "condition": "25 > 15", "result": "True", "variables": {"a": 25, "b": 15}, "explanation": "25 is greater than 15. Prints 25."}
            ]
        },
        "time_complexity": "O(1) - Instant comparison",
        "space_complexity": "O(1) - Only stores the two numbers"
    },
    "Largest of 3 Numbers": {
        "description": """🎯 What is this problem asking?
Given three numbers, find the single largest among them.

💡 Real-World Analogy (For Non-IT Beginners):
Imagine a podium race with 3 athletes. The gold medal goes to the athlete who ran faster than both other competitors!

📥 Example:
• Input: 10, 30, 20 → Output: 30

🧠 Step-by-Step Logic (The Plan):
1. If `a` is greater than or equal to both `b` and `c`, `a` is largest.
2. Else if `b` is greater than or equal to both `a` and `c`, `b` is largest.
3. Otherwise, `c` must be the largest!""",
        "python_code": """a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)""",
        "example_input": "10\n30\n20",
        "example_output": "30",
        "explanation": [
            {
                "line": 1,
                "code": "if a >= b and a >= c:",
                "explanation": "Testing Candidate 'a': 'and' requires both conditions to be true: 'a' must beat 'b' AND 'a' must beat 'c'."
            },
            {
                "line": 2,
                "code": "elif b >= a and b >= c:",
                "explanation": "Testing Candidate 'b': If 'a' wasn't the biggest, check if 'b' beats both rivals."
            },
            {
                "line": 3,
                "code": "else: print(c)",
                "explanation": "Default Winner: If neither 'a' nor 'b' won, 'c' is crowned the winner."
            }
        ],
        "dry_run": {
            "input": "a = 10, b = 30, c = 20",
            "steps": [
                {"iteration": 1, "condition": "10 >= 30 and 10 >= 20", "result": "False", "variables": {"a": 10}, "explanation": "10 is not bigger than 30."},
                {"iteration": 2, "condition": "30 >= 10 and 30 >= 20", "result": "True", "variables": {"b": 30}, "explanation": "30 beats both 10 and 20! Winner is 30."}
            ]
        },
        "time_complexity": "O(1) - Fixed comparisons",
        "space_complexity": "O(1) - Three variables"
    }
}

