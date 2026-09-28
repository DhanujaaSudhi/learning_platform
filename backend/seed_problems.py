import json

import models
from database import SessionLocal
from problem_engine import get_problem_details


PHASES = [
    (1, "Python Logic & Basics", [
        ("Numbers", ["Even or Odd", "Positive/Negative/Zero", "Largest of 2 Numbers", "Largest of 3 Numbers", "Swap Two Numbers", "Sum of Digits", "Reverse a Number", "Count Digits", "Palindrome Number", "Armstrong Number"]),
        ("Number Problems", ["Prime Number", "Print Primes in a Range", "Factorial", "Fibonacci Series", "GCD", "LCM", "Perfect Number", "Strong Number", "Automorphic Number", "Power of a Number"]),
        ("Pattern/Logic", ["Star Triangle", "Inverted Triangle", "Number Triangle", "Floyd's Triangle", "Pascal's Triangle", "Multiplication Table", "Sum of First N Numbers", "Sum of Squares", "Decimal to Binary", "Binary to Decimal"]),
    ]),
    (2, "Strings", [("Strings", ["Reverse String", "Check Palindrome", "Count Vowels/Consonants", "Count Words", "Count Characters", "Remove Spaces", "Remove Duplicate Characters", "Find Duplicate Characters", "First Non-Repeating Character", "First Repeating Character", "Character Frequency", "Check Anagram", "Check Pangram", "Check Substring", "Count Substring Occurrences", "Longest Word", "Shortest Word", "Reverse Words", "Reverse Each Word", "Capitalize Each Word", "String Compression", "Run-Length Encoding", "Replace Character", "Remove Special Characters", "Longest Common Prefix"])]),
    (3, "Arrays / Lists", [("Arrays / Lists", ["Find Maximum", "Find Minimum", "Find Second Largest", "Find Second Smallest", "Sum of Array", "Average", "Count Even/Odd", "Reverse Array", "Copy Array", "Remove Duplicates", "Frequency of Elements", "Find Duplicates", "Find Missing Number", "Find Repeating Number", "Move Zeros to End", "Move Negatives to One Side", "Rotate Left", "Rotate Right", "Merge Two Arrays", "Common Elements", "Union of Arrays", "Intersection", "Difference of Arrays", "Check Sorted Array", "Sort Without Built-In Sort", "Bubble Sort", "Selection Sort", "Insertion Sort", "Find Pair With Given Sum", "Find Triplet With Given Sum", "Maximum Difference", "Maximum Subarray Sum", "Kadane's Algorithm", "Leaders in Array", "Equilibrium Index"])]),
    (4, "Searching & Sorting", [("Searching", ["Linear Search", "Binary Search", "First Occurrence", "Last Occurrence", "Count Occurrences", "Search Insertion Position", "Search Rotated Array", "Find Minimum in Rotated Array", "Find Peak Element", "Square Root Using Binary Search"]), ("Sorting", ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Counting Sort", "Sort 0s, 1s, 2s", "Merge Sorted Arrays", "Kth Smallest", "Kth Largest", "Sort by Frequency", "Sort Strings by Frequency", "Meeting Room Sorting", "Minimum Platforms", "Largest Number From Array"])]),
    (5, "Hashing / Dictionary / Set", [("Hashing / Dictionary / Set", ["Character Frequency", "Element Frequency", "Two Sum", "Three Sum", "Four Sum", "First Unique Element", "Duplicate Detection", "Longest Consecutive Sequence", "Common Elements", "Subarray With Sum K", "Count Subarrays With Sum K", "Zero-Sum Subarray", "Longest Zero-Sum Subarray", "Group Anagrams", "Isomorphic Strings", "Word Pattern", "Happy Number", "Majority Element", "Top K Frequent Elements", "Find Missing/Repeated Number"])]),
    (6, "Two Pointers & Sliding Window", [("Two Pointers & Sliding Window", ["Two Sum Sorted Array", "Reverse Array Using Pointers", "Palindrome Using Pointers", "Remove Duplicates Sorted Array", "Move Zeros", "Container With Most Water", "Three Sum", "Four Sum", "Pair Closest to Target", "Merge Sorted Arrays", "Longest Substring Without Repeating Characters", "Longest Substring With K Distinct Characters", "Maximum Sum Subarray of Size K", "Minimum Size Subarray Sum", "Maximum Consecutive Ones", "Longest Repeating Character Replacement", "Permutation in String", "Find All Anagrams", "Minimum Window Substring", "Fruit Into Baskets", "Longest Subarray With at Most K Zeros", "Count Distinct Elements in Window", "Maximum of Every Window", "Minimum of Every Window", "Sliding Window Median"])]),
    (7, "Stack & Queue", [("Stack & Queue", ["Implement Stack", "Implement Queue", "Stack Using Queue", "Queue Using Stack", "Balanced Parentheses", "Remove Adjacent Duplicates", "Min Stack", "Next Greater Element", "Next Smaller Element", "Previous Greater Element", "Previous Smaller Element", "Stock Span", "Daily Temperatures", "Largest Rectangle Histogram", "Maximal Rectangle", "Evaluate Postfix", "Evaluate Prefix", "Infix to Postfix", "Decode String", "Circular Queue"])]),
    (8, "Linked List", [("Linked List", ["Create Linked List", "Traverse Linked List", "Insert at Beginning", "Insert at End", "Insert at Position", "Delete Node", "Search Node", "Reverse Linked List", "Find Middle Node", "Find Length", "Detect Cycle", "Find Cycle Start", "Remove Cycle", "Merge Two Sorted Lists", "Remove Duplicates", "Remove Nth Node From End", "Palindrome Linked List", "Intersection of Two Lists", "Add Two Numbers", "Rotate Linked List", "Reverse in Groups of K", "Sort Linked List", "Merge K Sorted Lists", "Copy List With Random Pointer", "Flatten Linked List"])]),
    (9, "Recursion & Backtracking", [("Recursion & Backtracking", ["Factorial Recursion", "Fibonacci Recursion", "Sum of N Numbers", "Reverse String Recursively", "Check Palindrome Recursively", "Power Recursively", "GCD Recursively", "Generate Binary Strings", "Generate Subsets", "Generate Permutations", "Combination Sum", "Letter Combinations", "Generate Parentheses", "N-Queens", "Sudoku Solver", "Rat in a Maze", "Word Search", "Combination Generation", "Subset Sum", "Partition Equal Subset", "Palindrome Partitioning", "Phone Keypad Combinations", "Josephus Problem", "Tower of Hanoi", "Word Break"])]),
    (10, "Trees & BST", [("Trees & BST", ["Create Binary Tree", "Preorder Traversal", "Inorder Traversal", "Postorder Traversal", "Level-Order Traversal", "Height of Tree", "Count Nodes", "Count Leaf Nodes", "Maximum Depth", "Minimum Depth", "Search in BST", "Insert in BST", "Delete From BST", "Validate BST", "Lowest Common Ancestor BST", "Lowest Common Ancestor Binary Tree", "Diameter of Tree", "Balanced Binary Tree", "Mirror Tree", "Symmetric Tree", "Left View", "Right View", "Top View", "Bottom View", "Zigzag Traversal", "Boundary Traversal", "Root-to-Leaf Paths", "Maximum Path Sum", "Serialize Tree", "Deserialize Tree"])]),
    (11, "Graphs", [("Graphs", ["Graph Representation", "BFS", "DFS", "Connected Components", "Number of Islands", "Flood Fill", "Cycle Detection Undirected", "Cycle Detection Directed", "Bipartite Graph", "Topological Sort BFS", "Topological Sort DFS", "Course Schedule", "Shortest Path BFS", "Dijkstra Algorithm", "Bellman-Ford", "Floyd-Warshall", "Minimum Spanning Tree", "Kruskal Algorithm", "Prim Algorithm", "Word Ladder", "Rotten Oranges", "Clone Graph", "Network Delay Time", "Number of Provinces", "Cheapest Flights"])]),
    (12, "Dynamic Programming", [("Dynamic Programming", ["Fibonacci DP", "Climbing Stairs", "House Robber", "House Robber II", "Coin Change", "Coin Change II", "0/1 Knapsack", "Unbounded Knapsack", "Subset Sum", "Equal Partition", "Longest Common Subsequence", "Longest Common Substring", "Edit Distance", "Longest Increasing Subsequence", "Matrix Chain Multiplication", "Egg Dropping Problem", "Boolean Parenthesization", "Minimum Path Sum", "Unique Paths With Obstacles", "Dungeon Game"])]),
    (13, "Advanced Arrays", [("Advanced Arrays", ["Product of Array Except Self", "Maximum Product Subarray", "Minimum Product Subarray", "Maximum Circular Subarray Sum", "Rearrange Positive and Negative Numbers", "Alternate Positive and Negative Numbers", "Find All Missing Numbers", "Find All Disappeared Numbers", "Find Duplicate Without Modifying Array", "Find Duplicate Using Floyd's Algorithm", "Majority Element II", "Find Median of Two Sorted Arrays", "Merge Overlapping Intervals", "Insert Interval", "Non-Overlapping Intervals", "Minimum Arrows to Burst Balloons", "Maximum Consecutive Sequence", "Trapping Rain Water", "Best Time to Buy and Sell Stock", "Best Time to Buy and Sell Stock II"])]),
    (14, "Advanced Strings", [("Advanced Strings", ["Longest Palindromic Substring", "Count Palindromic Substrings", "Longest Palindromic Subsequence", "Minimum Insertions for Palindrome", "Valid Palindrome II", "String Rotation Check", "String Is Subsequence", "Longest Repeating Subsequence", "Remove Duplicate Letters", "Smallest Window Containing Characters", "Word Frequency Sorting", "Reorganize String", "Custom String Sorting", "Compare Version Numbers", "Multiply Large Numbers as Strings", "Add Large Numbers as Strings", "Integer to Roman", "Roman to Integer", "String to Integer", "Integer to English Words"])]),
    (15, "Advanced Hashing", [("Advanced Hashing", ["Longest Subarray With Equal 0s and 1s", "Count Subarrays With Equal 0s and 1s", "Longest Subarray With Equal 0s, 1s and 2s", "Count Distinct Subarrays", "Subarray XOR Equals K", "Count Pairs With Given Difference", "Count Pairs With Given Sum", "Four Sum Using Hashing", "Is Array Subset of Another Array", "Is Array a Palindrome Using Hashing", "Find Duplicate Files", "Design Hash Set", "Design Hash Map", "LRU Cache", "LFU Cache", "Insert/Delete/GetRandom O(1)", "Randomized Collection", "Time-Based Key-Value Store", "Underground System", "Frequency Stack"])]),
    (16, "Advanced Stack & Queue", [("Advanced Stack & Queue", ["Largest Rectangle in Histogram", "Maximal Rectangle", "Sum of Subarray Minimums", "Sum of Subarray Ranges", "Remove K Digits", "Asteroid Collision", "Basic Calculator", "Basic Calculator II", "Basic Calculator III", "Simplify Unix Path", "Decode Nested String", "Remove Invalid Parentheses", "Online Stock Span", "Sliding Window Maximum", "Sliding Window Minimum", "First Negative Number in Every Window", "Design Circular Deque", "Design Priority Queue", "Implement Deque", "Celebrity Problem"])]),
    (17, "Advanced Linked List", [("Advanced Linked List", ["Reverse Linked List Recursively", "Reverse Alternate K Nodes", "Reverse Sublist", "Pairwise Swap Nodes", "Odd-Even Linked List", "Partition Linked List", "Sort 0s, 1s and 2s in Linked List", "Merge K Linked Lists", "Flatten Multilevel Linked List", "Clone Linked List With Random Pointer", "Add Two Linked-List Numbers", "Subtract Two Linked-List Numbers", "Multiply Two Linked-List Numbers", "Rotate Linked List by K", "Reorder Linked List", "Palindrome Linked List Using O(1) Space", "Intersection Without Extra Space", "Detect Cycle Using Floyd's Algorithm", "Remove Duplicate Nodes From Unsorted List", "Convert Sorted Linked List to BST"])]),
    (18, "Advanced Trees", [("Advanced Trees", ["Binary Tree Maximum Width", "Vertical Order Traversal", "Diagonal Traversal", "Morris Inorder Traversal", "Morris Preorder Traversal", "Iterative Tree Traversal", "Construct Tree From Preorder + Inorder", "Construct Tree From Inorder + Postorder", "Convert Sorted Array to BST", "Convert Sorted Linked List to BST", "Kth Smallest in BST", "Kth Largest in BST", "BST Iterator", "Recover Corrupted BST", "Two Sum in BST", "Range Sum in BST", "Convert BST to Greater Tree", "Flatten Binary Tree", "Serialize Binary Tree", "Deserialize Binary Tree", "Maximum Width of Binary Tree", "Path Sum", "Path Sum II", "Path Sum III", "House Robber III"])]),
    (19, "Advanced Graphs", [("Advanced Graphs", ["BFS Shortest Path", "DFS Path Finding", "Number of Connected Components", "Number of Islands", "Number of Distinct Islands", "Surrounded Regions", "Pacific Atlantic Water Flow", "Clone Graph", "Course Schedule I", "Course Schedule II", "Alien Dictionary", "Word Ladder", "Word Ladder II", "Minimum Genetic Mutation", "Network Delay Time", "Cheapest Flights Within K Stops", "Swim in Rising Water", "Path With Minimum Effort", "Shortest Path in Binary Matrix", "0-1 BFS", "Dijkstra With Adjacency List", "Bellman-Ford With Negative Edges", "Floyd-Warshall All-Pairs Shortest Path", "Strongly Connected Components", "Bridges in Graph"])]),
    (20, "Advanced Graphs / MST", [("Advanced Graphs / MST", ["Articulation Points", "Kosaraju Algorithm", "Tarjan Algorithm", "Kruskal MST", "Prim MST", "Minimum Cost to Connect Points", "Redundant Connection", "Redundant Directed Connection", "Accounts Merge", "Number of Provinces Using DSU", "Network Connection Operations", "Smallest String With Swaps", "Most Stones Removed", "Regions Cut by Slashes", "Satisfiability of Equations"])]),
    (21, "Advanced Dynamic Programming", [("Advanced Dynamic Programming", ["Climbing Stairs Variations", "Minimum Cost Climbing Stairs", "House Robber", "House Robber II", "House Robber III", "Coin Change", "Coin Change II", "0/1 Knapsack", "Unbounded Knapsack", "Rod Cutting", "Partition Equal Subset Sum", "Target Sum", "Last Stone Weight II", "Longest Increasing Subsequence", "Longest Decreasing Subsequence", "Longest Bitonic Subsequence", "Number of LIS", "Longest Common Subsequence", "Longest Common Substring", "Edit Distance", "Distinct Subsequences", "Interleaving Strings", "Word Break", "Palindrome Partitioning II", "Burst Balloons"])]),
    (22, "Hard DP / Interview Problems", [("Hard DP / Interview Problems", ["Matrix Chain Multiplication", "Egg Dropping Problem", "Boolean Parenthesization", "Minimum Path Sum", "Unique Paths With Obstacles", "Dungeon Game", "Maximum Rectangle in Binary Matrix", "Regular Expression Matching", "Wildcard Matching", "Traveling Salesman Problem"])]),
]


PHASE_ONE_CODE = {
    "Even or Odd": 'n = int(input("Enter a number: "))\n\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")',
    "Prime Number": 'n = int(input("Enter a number: "))\n\nif n <= 1:\n    print("Not Prime Number")\nelse:\n    is_prime = True\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            is_prime = False\n            break\n\n    if is_prime:\n        print("Prime Number")\n    else:\n        print("Not Prime Number")',
    "Positive/Negative/Zero": 'n = int(input("Enter a number: "))\n\nif n > 0:\n    print("Positive")\nelif n < 0:\n    print("Negative")\nelse:\n    print("Zero")',
    "Largest of 2 Numbers": 'a = int(input("Enter first number: "))\nb = int(input("Enter second number: "))\n\nif a > b:\n    print(a)\nelse:\n    print(b)',
    "Largest of 3 Numbers": 'a = int(input("Enter first number: "))\nb = int(input("Enter second number: "))\nc = int(input("Enter third number: "))\n\nif a >= b and a >= c:\n    print(a)\nelif b >= a and b >= c:\n    print(b)\nelse:\n    print(c)',
    "Swap Two Numbers": 'a = int(input("Enter first number: "))\nb = int(input("Enter second number: "))\n\na, b = b, a\nprint("a =", a)\nprint("b =", b)',
    "Sum of Digits": 'n = int(input("Enter a number: "))\ntotal = 0\n\nwhile n > 0:\n    digit = n % 10\n    total += digit\n    n //= 10\n\nprint(total)',
    "Reverse a Number": 'n = int(input("Enter a number: "))\nreverse = 0\n\nwhile n > 0:\n    digit = n % 10\n    reverse = reverse * 10 + digit\n    n //= 10\n\nprint(reverse)',
    "Count Digits": 'n = abs(int(input("Enter a number: ")))\ncount = 1 if n == 0 else 0\n\nwhile n > 0:\n    count += 1\n    n //= 10\n\nprint(count)',
    "Palindrome Number": 'n = int(input("Enter a number: "))\noriginal = n\nreverse = 0\n\nwhile n > 0:\n    reverse = reverse * 10 + n % 10\n    n //= 10\n\nif original == reverse:\n    print("Palindrome Number")\nelse:\n    print("Not Palindrome Number")',
    "Armstrong Number": 'n = int(input("Enter a number: "))\noriginal = n\npower = len(str(abs(n)))\ntotal = 0\n\nwhile n > 0:\n    digit = n % 10\n    total += digit ** power\n    n //= 10\n\nif original == total:\n    print("Armstrong Number")\nelse:\n    print("Not Armstrong Number")',
    "Print Primes in a Range": 'start = int(input("Enter start: "))\nend = int(input("Enter end: "))\n\nfor num in range(start, end + 1):\n    if num > 1:\n        is_prime = True\n        for i in range(2, int(num ** 0.5) + 1):\n            if num % i == 0:\n                is_prime = False\n                break\n        if is_prime:\n            print(num, end=" ")',
    "Factorial": 'n = int(input("Enter a number: "))\nfact = 1\n\nfor i in range(1, n + 1):\n    fact *= i\n\nprint(fact)',
    "Fibonacci Series": 'n = int(input("Enter number of terms: "))\na, b = 0, 1\n\nfor _ in range(n):\n    print(a, end=" ")\n    a, b = b, a + b',
    "GCD": 'a = int(input("Enter first number: "))\nb = int(input("Enter second number: "))\n\nwhile b:\n    a, b = b, a % b\n\nprint(a)',
    "LCM": 'a = int(input("Enter first number: "))\nb = int(input("Enter second number: "))\nx, y = a, b\n\nwhile y:\n    x, y = y, x % y\n\ngcd = x\nprint((a * b) // gcd)',
    "Perfect Number": 'n = int(input("Enter a number: "))\ntotal = 0\n\nfor i in range(1, n):\n    if n % i == 0:\n        total += i\n\nif total == n:\n    print("Perfect Number")\nelse:\n    print("Not Perfect Number")',
    "Strong Number": 'n = int(input("Enter a number: "))\noriginal = n\ntotal = 0\n\nwhile n > 0:\n    digit = n % 10\n    fact = 1\n    for i in range(1, digit + 1):\n        fact *= i\n    total += fact\n    n //= 10\n\nif total == original:\n    print("Strong Number")\nelse:\n    print("Not Strong Number")',
    "Automorphic Number": 'n = int(input("Enter a number: "))\nsquare = n * n\n\nif str(square).endswith(str(n)):\n    print("Automorphic Number")\nelse:\n    print("Not Automorphic Number")',
    "Power of a Number": 'base = int(input("Enter base: "))\nexponent = int(input("Enter exponent: "))\nresult = 1\n\nfor _ in range(exponent):\n    result *= base\n\nprint(result)',
    "Star Triangle": 'n = int(input("Enter rows: "))\n\nfor i in range(1, n + 1):\n    print("*" * i)',
    "Inverted Triangle": 'n = int(input("Enter rows: "))\n\nfor i in range(n, 0, -1):\n    print("*" * i)',
    "Number Triangle": 'n = int(input("Enter rows: "))\n\nfor i in range(1, n + 1):\n    for j in range(1, i + 1):\n        print(j, end=" ")\n    print()',
    "Floyd's Triangle": 'n = int(input("Enter rows: "))\nnum = 1\n\nfor i in range(1, n + 1):\n    for _ in range(i):\n        print(num, end=" ")\n        num += 1\n    print()',
    "Pascal's Triangle": 'n = int(input("Enter rows: "))\n\nfor i in range(n):\n    value = 1\n    print(" " * (n - i), end="")\n    for j in range(i + 1):\n        print(value, end=" ")\n        value = value * (i - j) // (j + 1)\n    print()',
    "Multiplication Table": 'n = int(input("Enter a number: "))\n\nfor i in range(1, 11):\n    print(n, "x", i, "=", n * i)',
    "Sum of First N Numbers": 'n = int(input("Enter a number: "))\ntotal = 0\n\nfor i in range(1, n + 1):\n    total += i\n\nprint(total)',
    "Sum of Squares": 'n = int(input("Enter a number: "))\ntotal = 0\n\nfor i in range(1, n + 1):\n    total += i * i\n\nprint(total)',
    "Decimal to Binary": 'n = int(input("Enter a decimal number: "))\n\nif n == 0:\n    print(0)\nelse:\n    binary = ""\n    while n > 0:\n        binary = str(n % 2) + binary\n        n //= 2\n    print(binary)',
    "Binary to Decimal": 'binary = input("Enter a binary number: ")\ndecimal = 0\n\nfor digit in binary:\n    decimal = decimal * 2 + int(digit)\n\nprint(decimal)',
}


PHASE_ONE_EXAMPLES = {
    "Even or Odd": ("10", "Even"),
    "Prime Number": ("11", "Prime Number"),
    "Positive/Negative/Zero": ("5", "Positive"),
    "Largest of 2 Numbers": ("2\n3", "3"),
    "Largest of 3 Numbers": ("2\n3\n1", "3"),
    "Swap Two Numbers": ("2\n3", "a = 3\nb = 2"),
    "Sum of Digits": ("123", "6"),
    "Reverse a Number": ("123", "321"),
    "Count Digits": ("12345", "5"),
    "Palindrome Number": ("121", "Palindrome Number"),
    "Armstrong Number": ("153", "Armstrong Number"),
    "Print Primes in a Range": ("1\n10", "2 3 5 7"),
    "Factorial": ("5", "120"),
    "Fibonacci Series": ("5", "0 1 1 2 3"),
    "GCD": ("12\n18", "6"),
    "LCM": ("4\n6", "12"),
    "Perfect Number": ("28", "Perfect Number"),
    "Strong Number": ("145", "Strong Number"),
    "Automorphic Number": ("25", "Automorphic Number"),
    "Power of a Number": ("2\n3", "8"),
    "Star Triangle": ("3", "*\n**\n***"),
    "Inverted Triangle": ("3", "***\n**\n*"),
    "Number Triangle": ("3", "1\n1 2\n1 2 3"),
    "Floyd's Triangle": ("3", "1\n2 3\n4 5 6"),
    "Pascal's Triangle": ("3", "1\n1 1\n1 2 1"),
    "Multiplication Table": ("5", "5 x 1 = 5"),
    "Sum of First N Numbers": ("5", "15"),
    "Sum of Squares": ("3", "14"),
    "Decimal to Binary": ("10", "1010"),
    "Binary to Decimal": ("1010", "10"),
}


def difficulty_for(phase, index):
    if phase <= 3:
        return "Medium" if index % 4 == 0 else "Easy"
    if phase <= 9:
        return "Hard" if index % 5 == 0 else "Medium"
    return "Hard"


def concepts_for(category, title):
    concepts = [category]
    title_lower = title.lower()
    if "sort" in title_lower:
        concepts.append("Sorting")
    if "search" in title_lower or "find" in title_lower:
        concepts.append("Searching")
    if "tree" in title_lower or "bst" in title_lower:
        concepts.append("Tree Traversal")
    if "graph" in title_lower or "path" in title_lower:
        concepts.append("Graph Traversal")
    if "dp" in title_lower or "subsequence" in title_lower or "knapsack" in title_lower:
        concepts.append("Dynamic Programming")
    if "window" in title_lower or "substring" in title_lower:
        concepts.append("Sliding Window")
    if "hash" in title_lower or "frequency" in title_lower:
        concepts.append("Hash Map")
    return concepts[:4]


def code_for(title):
    if title in PHASE_ONE_CODE:
        return PHASE_ONE_CODE[title]
    return f'''"""
Problem: {title}

This starter keeps input/output simple so you can focus on the algorithm.
Replace parse_input() and solve() with the exact logic for this problem.
"""


def parse_input():
    return input().strip()


def solve(data):
    return data


data = parse_input()
print(solve(data))
'''


def problem_record(problem_id, phase, category, title, index):
    concepts = concepts_for(category, title)
    details = get_problem_details(title, category, phase)
    return {
        "id": problem_id,
        "phase": phase,
        "category": category,
        "title": title,
        "difficulty": difficulty_for(phase, index),
        "description": details["description"],
        "concepts": json.dumps(concepts),
        "python_code": details["python_code"],
        "example_input": details["example_input"],
        "example_output": details["example_output"],
        "explanation": json.dumps(details["explanation"]),
        "dry_run": json.dumps(details["dry_run"]),
        "time_complexity": details["time_complexity"],
        "space_complexity": details["space_complexity"],
    }


def build_curriculum():
    flat_items = []
    for phase, _phase_name, groups in PHASES:
        index = 1
        for category, titles in groups:
            for title in titles:
                flat_items.append((phase, category, title, index))
                index += 1

    preferred_start = ["Even or Odd", "Prime Number"]
    ordered_items = []
    for preferred_title in preferred_start:
        ordered_items.extend(item for item in flat_items if item[2] == preferred_title)
    ordered_items.extend(item for item in flat_items if item[2] not in preferred_start)

    records = []
    for problem_id, (phase, category, title, index) in enumerate(ordered_items, start=1):
        records.append(problem_record(problem_id, phase, category, title, index))
    return records


def seed_problems():
    db = SessionLocal()
    try:
        records = build_curriculum()
        existing_by_id = {p.id: p for p in db.query(models.Problem).all()}
        for record in records:
            problem = existing_by_id.get(record["id"])
            if problem is None:
                problem = models.Problem(id=record["id"])
                db.add(problem)
            for key, value in record.items():
                setattr(problem, key, value)
        db.commit()
        return len(records)
    finally:
        db.close()


if __name__ == "__main__":
    total = seed_problems()
    print(f"Seeded {total} problems.")
