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
