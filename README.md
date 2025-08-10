# 🚀 Teachers' Day Challenge 2025 - VIT Bhopal

---

Welcome to my GitHub repository for the **Teachers' Day Challenge 2025**, an initiative by **PAT Cell VIT Bhopal**! This challenge is a 43-day coding journey, running from July 25th to September 5th (Teachers' Day), focused on consistency, growth, and upskilling in Data Structures and Algorithms (DSA).

As a proud Lion of VIT Bhopal, I'm dedicating time each day to practice problem-solving, build confidence for technical interviews, and contribute to our vibrant coding community.

## About the Challenge

The Teachers' Day Challenge offers two tracks:
* **Beginner Track:** 43 problems
* **Advanced Track:** 86 problems (2 problems per day)

I'm committed to tackling problems from Beginner track to sharpen my DSA skills and maintain daily coding consistency. 

"Success is the sum of small efforts, repeated day in and day out." This challenge perfectly embodies that philosophy, and I'm excited to see the progress each day brings.

## My Progress 📈

Here, you'll find my solutions to the daily problems. I'll be updating this repository regularly with my code.

### Day 1 (July 25)
* **Beginner Track:** LeetCode 1295: Find Numbers with Even Number of Digits

### Day 2 (July 26)
* **Beginner Track:** LeetCode 412: Fizz Buzz

### Day 3 (July 27)
* LeetCode 125: Valid Palindrome
    * **Note:** Solved using Python's `re.sub` for string cleaning. Observed a performance difference: a direct `return` statement for the palindrome check yielded ~3ms runtime, compared to ~6ms when using an explicit `if-else` block for the same logic.

### Day 4 (July 28)
* LeetCode 1: Two Sum
    * **Note:** Solved using the Hash Map approach for optimal efficiency. While other methods like brute-force or two-pointers (after sorting) exist, the hash map offers a clean O(n) average-time complexity. You'll find both the code and detailed notes on this problem's various solutions in this repository.

### **Day 5: Unraveling Roman Numerals! (LeetCode 13: Roman to Integer)**
* **Problem Link:** [https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)
* **Solution Status:** Solved
* **Approach:** Implemented a single-pass iteration from left to right. Utilized a hash map (dictionary) to store Roman symbol-to-integer mappings. The core logic involved checking the next character's value: if the current symbol's value was less than the next, it signified a subtractive case (e.g., IV, IX), otherwise it was additive.
* **Complexity:**
    * **Time Complexity: O(N)**, where N is the length of the Roman numeral string, due to a single pass.
    * **Space Complexity: O(1)**, as the symbol-to-value map is of fixed size.
* **Key Learnings:** Reinforcement of handling conditional logic within a loop for sequential parsing problems. Confirmed the efficiency of hash maps for constant-time lookups.

### **Day 6: Balancing Brackets! (LeetCode 20: Valid Parentheses)**
* **Problem Link:** [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)
* **Solution Status:** Solved
* **Approach:** Used a stack data structure along with a mapping dictionary. Iterated through the string: pushed opening brackets onto the stack. For closing brackets, checked if the stack was empty or if the popped element didn't match the expected opening bracket.
* **Complexity:**
    * **Time Complexity: O(N)**, where N is the length of the input string, as each character is processed once.
    * **Space Complexity: O(N)**, in the worst case, the stack might store all opening brackets (e.g., "(((").
* **Key Learnings:** Solidified understanding of stack's Last-In-First-Out (LIFO) principle. Practiced using stacks for matching and parsing problems, a common pattern in DSA.

### **Day 7: First Dive into Codeforces! (Codeforces 4A: Watermelon)**
* **Problem Link:** [https://codeforces.com/problemset/problem/4/A](https://codeforces.com/problemset/problem/4/A)
* **Solution Status:** Solved
* **Approach:** This problem required checking if a given even weight `w` (greater than 2) can be split into two even numbers. The solution involved a simple modulo operation (`w % 2 == 0`) and ensuring `w` is not equal to 2, as 2 cannot be split into two positive even numbers.
* **Complexity:**
    * **Time Complexity: O(1)**, as it involves a single arithmetic operation and a comparison.
    * **Space Complexity: O(1)**, using only a few constant variables.
* **Key Learnings:** Initiated problem-solving on Codeforces. Reinforced the importance of edge cases (like `w=2`) even in seemingly simple problems. Great warm-up for the new platform!

### **Day 8: Mastering the 'Way Too Long Words' Problem! (Codeforces 71A: Way Too Long Words)**
* **Problem Link:** [https://codeforces.com/problemset/problem/71A](https://codeforces.com/problemset/problem/71A)
* **Solution Status:** Solved
* **Approach:** The solution reads a number `n`, followed by `n` words. For each word, it checks its length. If the length is greater than 10, it prints an abbreviation consisting of the first character, the length minus 2, and the last character. Otherwise, it prints the word as is.
* **Complexity:**
    * **Time Complexity: O(L)**, where L is the length of a given word. The process is repeated for each of the `n` words.
    * **Space Complexity: O(L)**, where L is the length of the longest word, as we need to store each word in memory for processing.
* **Key Learnings:** Focused on string manipulation and conditional logic. Practiced the standard Codeforces I/O format (reading `n`, then looping `n` times to read and process input).

### **Day 9: Solving as a Team! (Codeforces 231A: Team)**
* **Problem Link:** [https://codeforces.com/problemset/problem/231/A](https://codeforces.com/problemset/problem/231/A)
* **Solution Status:** Solved
* **Approach:** The problem involves reading an integer `n` followed by `n` lines of input, with each line containing three integers. My solution reads each line, sums the three integers, and if the sum is 2 or greater, it increments a counter. Finally, it prints the total count of problems that can be solved.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the number of problems. We loop through each problem once, performing a constant number of operations inside the loop.
    * **Space Complexity:** O(1), as the memory used for variables is constant and does not depend on the input size.
* **Key Learnings:** Practiced reading multiple integer inputs from a single line using `input().split()` and `map()`. Solidified understanding of simple counting loops and conditional logic.

### **Day 10: Advancing to the Next Round! (Codeforces 158A: Next Round)**
* **Problem Link:** [https://codeforces.com/problemset/problem/158/A](https://codeforces.com/problemset/problem/158/A)
* **Solution Status:** Solved
* **Approach:** The solution reads `n` and `k`, followed by a list of `n` scores. It then identifies the score of the k-th place finisher (at index `k-1`) as the benchmark. It iterates through the list of scores, counting every participant whose score is both greater than 0 and greater than or equal to the benchmark score.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the number of participants, as we iterate through the list of scores once to find the qualified count.
    * **Space Complexity:** O(N), as we store the list of `n` scores in memory.
* **Key Learnings:** Solidified parsing multiple inputs from a single line (`input().split()`). Practiced using array indexing to establish a benchmark and applying multiple logical conditions within a loop.

### **Day 11: Simplifying Strings! (Codeforces 118A: String Task)**
* **Problem Link:** [https://codeforces.com/problemset/problem/118/A](https://codeforces.com/problemset/problem/118/A)
* **Solution Status:** Solved
* **Approach:** The solution reads an input string. It iterates through each character of the string. If a character is not a vowel (case-insensitive), it appends a dot '.' followed by the lowercase version of the consonant to a result list. Finally, it joins the elements of the result list to form the output string.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the input string, as we iterate through each character once.
    * **Space Complexity:** O(N), in the worst case, the `result` list can have up to 2N elements (if the input string contains no vowels).
* **Key Learnings:** Practiced iterating through strings and applying conditional logic to characters. Reinforced the use of string methods like `.lower()` and the concept of building a new string character by character (or using a list and then joining). This was an easy problem focusing on basic string manipulation.

### **Day 12: Petya and Strings! (Codeforces 112A: Petya and Strings)**
* **Problem Link:** [https://codeforces.com/problemset/problem/112/A](https://codeforces.com/problemset/problem/112/A)
* **Solution Status:** Solved
* **Approach:** The solution reads two strings, converts them to lowercase to ensure case-insensitive comparison, and then uses standard Python comparison operators to determine their lexicographical order. It prints -1, 1, or 0 based on whether the first string is lexicographically smaller, larger, or equal to the second.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the strings. The comparison operation iterates through the strings once.
    * **Space Complexity:** O(N), as we need to store both input strings and their lowercase versions in memory.
* **Key Learnings:** Practiced case-insensitive string manipulation and reinforced the behavior of Python's built-in lexicographical string comparison. This was an easy problem that tested a fundamental string operation.

### **Day 13: Making Maths Helpful! (Codeforces 339A: Helpful Maths)**
* **Problem Link:** [https://codeforces.com/problemset/problem/339/A](https://codeforces.com/problemset/problem/339/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a string representing a sum. It first removes all '+' signs from the string, then sorts the remaining single-digit numbers. Finally, it joins the sorted numbers back together with '+' signs in between.
* **Complexity:**
    * **Time Complexity:** O(N log N), where N is the number of terms in the sum. The dominant operation is sorting the numbers.
    * **Space Complexity:** O(N), as a new list of numbers is created to perform the sorting.
* **Key Learnings:** Practiced using built-in Python string methods like `.replace()` and `.join()` along with list sorting to solve a problem elegantly. This was a great example of how to break down a string manipulation problem into smaller, manageable steps.

### **Day 14: Capitalizing Words! (Codeforces 281A: Word Capitalization)**
* **Problem Link:** [https://codeforces.com/problemset/problem/281/A](https://codeforces.com/problemset/problem/281/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a single word, converts its first character to uppercase using the `.upper()` method, and then concatenates it with the rest of the string using slicing (`s[1:]`).
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the string, as slicing and concatenation operations take time proportional to the string's length.
    * **Space Complexity:** O(N), as a new string is created to store the capitalized word.
* **Key Learnings:** Practiced fundamental string indexing, slicing, and manipulation, reinforcing the immutability of strings in Python and the use of built-in methods for simple tasks.

### **Day 15: Boy or Girl! (Codeforces 236A: Boy or Girl)**
* **Problem Link:** [https://codeforces.com/problemset/problem/236/A](https://codeforces.com/problemset/problem/236/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a username string and converts it into a set to automatically count the number of unique characters. It then checks if the size of the set is even or odd to determine the output.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the username string. Creating a set from a string requires iterating through all characters once.
    * **Space Complexity:** O(K), where K is the number of distinct characters in the username. The space is used to store the unique characters in the set.
* **Key Learnings:** Reinforced the efficiency of using a `set` to find the number of distinct elements in a collection. This was a straightforward problem that tested the understanding of basic data structures.

### **Day 16: The Beautiful Matrix! (Codeforces 263A: Beautiful Matrix)**
* **Problem Link:** [https://codeforces.com/problemset/problem/263/A](https://codeforces.com/problemset/problem/263/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a 5x5 matrix to find the single '1'. It then calculates the Manhattan distance (the sum of the absolute differences of the coordinates) from the '1' to the center of the matrix, which is at `(3, 3)`. This distance represents the minimum number of moves required.
* **Complexity:**
    * **Time Complexity:** O(1), as the matrix size is fixed at 5x5, making the number of operations constant.
    * **Space Complexity:** O(1), as the memory required to store the matrix and variables is constant.
* **Key Learnings:** Practiced matrix traversal and manipulation, focusing on finding a specific element. Applied the concept of Manhattan distance to solve a problem requiring a minimum number of moves. This was a good challenge to reinforce logic within a fixed data structure.

### **Day 17: Stones on the Table! (Codeforces 266A: Stones on the Table)**
* **Problem Link:** [https://codeforces.com/problemset/problem/266/A](https://codeforces.com/problemset/problem/266/A)
* **Solution Status:** Solved
* **Approach:** This problem was solved using two different methods.
    * **Method 1 (Iterative):** A single pass through the string was performed, comparing each character to its immediate predecessor. A counter was incremented whenever adjacent characters were identical.
    * **Method 2 (Stack-based):** A stack was used to store unique, non-adjacent stones. The algorithm iterated through the string, pushing stones onto the stack only if they were different from the top element. The number of stones that were not pushed represents the number of removals.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the string, as both approaches involve a single pass.
    * **Space Complexity:** O(1) for the iterative method, and O(N) in the worst case for the stack-based method (if all stones are different).
* **Key Learnings:** Reinforcement of basic string traversal with conditional logic. The stack approach provided a great opportunity to practice using data structures to solve a problem with an alternative, and often more robust, method.

---

### My Commitment

A special thanks to our Placement Director, **Shriram R**, for his constant motivation and guidance. His dedication truly helps us all aim higher and dream bigger.

I'm Parshv Modi, and I'm committed to continuous learning, challenging myself, and growing as a developer.

---

## Stay Connected!

Feel free to explore my solutions, provide feedback, or even share your own progress. Let's inspire and encourage each other as a team!

You can follow my journey and get daily updates on LinkedIn: **https://www.linkedin.com/in/parshv-modi/**

Original Challenge Link: https://teachers-day-vitb.vercel.app/

---

**#TeachersDay #MissionDrGViswanathan #VITBhopal #VITBhopalUniversity #VIT #Upskill #BuildingSkills #CodingChallenge #GrowthMindset #LeetCode #DSA #TeachersDayChallenge #PATCell #AdvancedTrack #BeginnerTrack #CodeEveryday #Consistency #GratitudeThroughGrowth**
