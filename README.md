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
