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

### **Day 18: Bit++! (Codeforces 282A: Bit++)**
* **Problem Link:** [https://codeforces.com/problemset/problem/282/A](https://codeforces.com/problemset/problem/282/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a number `n`, followed by `n` statements. It initializes a counter `x` to 0. For each statement, it checks if a '+' character is present. If it is, the counter is incremented; otherwise, it is decremented.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the number of statements, as we iterate through each statement once.
    * **Space Complexity:** O(1), as the memory used for variables is constant and does not depend on the input size.
* **Key Learnings:** Focused on simple string checking and conditional logic to solve a problem with a counter. Practiced the standard Codeforces I/O format of reading a number and then looping that many times.

### **Day 19: The Domino Piling Problem! (Codeforces 50A: Domino Piling)**
* **Problem Link:** [https://codeforces.com/problemset/problem/50/A](https://codeforces.com/problemset/problem/50/A)
* **Solution Status:** Solved
* **Approach:** The solution calculates the maximum number of dominoes that can be placed on an M×N board. The problem can be solved with a single mathematical formula by dividing the total area of the board (M * N) by the area of a single domino (2).
* **Complexity:**
    * **Time Complexity:** O(1), as it involves a single arithmetic operation.
    * **Space Complexity:** O(1), as only a few constant variables are used.
* **Key Learnings:** Practiced identifying mathematical patterns in problems to find elegant and highly efficient solutions, rather than resorting to complex iterative or brute-force methods.

### **Day 20: Tackling a Translation Problem! (Codeforces 41A: Translation)**
* **Problem Link:** [https://codeforces.com/problemset/problem/41/A](https://codeforces.com/problemset/problem/41/A)
* **Solution Status:** Solved
* **Approach:** The solution reads two words, s and t. It checks if the second word t is identical to the first word s when s is reversed. This check is performed efficiently using Python's string slicing s[::-1] for reversal and direct comparison.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the strings. String reversal using slicing and subsequent comparison both take time proportional to the string's length.
    * **Space Complexity:** O(N), as string slicing s[::-1] creates a new reversed string in memory.
* **Key Learnings:** Reinforced efficient string manipulation techniques in Python, specifically string slicing for reversal. Practiced direct string comparison for equality.

### **Day 21: The Twins Problem! (Codeforces 160A: Twins)**
* **Problem Link:** [https://codeforces.com/problemset/problem/160/A](https://codeforces.com/problemset/problem/160/A)
* **Solution Status:** Solved
* **Approach:** The solution uses a greedy algorithm. It first calculates the total sum of all coins. To find the minimum number of coins with a sum strictly greater than half the total, it sorts the coins in descending order. It then iterates through the sorted coins, adding them to a running sum and counting them until the running sum exceeds half the total.
* **Complexity:**
    * **Time Complexity:** O(N log N), as the most time-consuming step is sorting the list of `n` coins.
    * **Space Complexity:** O(N), to store the list of coin values.
* **Key Learnings:** This problem was a great example of a greedy approach. It highlighted the importance of sorting as a pre-processing step to enable a greedy strategy that guarantees an optimal solution.

### **Day 22: The Queue at the School! (Codeforces 266B: Queue at the School)**
* **Problem Link:** [https://codeforces.com/problemset/problem/266/B](https://codeforces.com/problemset/problem/266/B)
* **Solution Status:** Solved
* **Approach:** This problem was solved by simulating the process of children swapping positions in a queue for `t` seconds. The algorithm iterates through the queue and swaps adjacent pairs of a boy followed by a girl. It's crucial to increment the inner loop's index by 2 after each swap to avoid multiple swaps of the same child in a single second.
* **Complexity:**
    * **Time Complexity:** O(n * t), as a loop of length `n` is executed `t` times.
    * **Space Complexity:** O(n), as the string representing the queue is stored in a list of characters.
* **Key Learnings:** Practiced simulation and handling state changes within a loop with a fixed number of iterations. This problem was a good reminder of how to carefully manage loop indices to ensure correct behavior.

### **Day 23: The Elephant's Journey! (Codeforces 617A: Elephant)**
* **Problem Link:** [https://codeforces.com/problemset/problem/617/A](https://codeforces.com/problemset/problem/617/A)
* **Solution Status:** Solved
* **Approach:** The solution employs a greedy algorithm to find the minimum number of steps to reach a point `x`. It repeatedly takes the largest possible step (5, 4, 3, 2, or 1) until the destination is reached, counting each step.
* **Complexity:**
    * **Time Complexity:** O(x), where x is the coordinate of the friend's house. The number of operations is proportional to the distance.
    * **Space Complexity:** O(1), as only a few variables are used to store the state.
* **Key Learnings:** Applied a greedy strategy to a simple optimization problem. The solution demonstrated that for a problem with a clear goal of minimization, always taking the largest possible step is an effective strategy.

### **Day 24: Soldier and Bananas! (Codeforces 546A: Soldier and Bananas)**
* **Problem Link:** [https://codeforces.com/problemset/problem/546/A](https://codeforces.com/problemset/problem/546/A)
* **Solution Status:** Solved
* **Approach:** The solution calculates the total cost of buying `w` bananas, where the cost of the `i`-th banana is `i * k`. The total money needed is then compared to the money the soldier has (`n`). If the calculated total cost is greater than `n`, the difference represents the amount the soldier has to borrow.
* **Complexity:**
    * **Time Complexity:** O(w), where w is the number of bananas, due to a loop to calculate the total cost.
    * **Space Complexity:** O(1), as only a few constant variables are used.
* **Key Learnings:** Practiced using a simple loop to calculate a running total and applying conditional logic to determine the final output. This problem reinforced the importance of translating problem logic into simple, direct code.

### **Day 25: The Word Problem! (Codeforces 59A: Word)**
* **Problem Link:** [https://codeforces.com/problemset/problem/59/A](https://codeforces.com/problemset/problem/59/A)
* **Solution Status:** Solved
* **Approach:** The solution iterates through the input string to count the number of uppercase and lowercase letters. Based on which count is greater or equal, it converts the entire string to either lowercase or uppercase and then prints the result.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the string, due to a single pass to count characters.
    * **Space Complexity:** O(N), as a new string is created for the final output.
* **Key Learnings:** Practiced basic string iteration and conditional logic. Used built-in string methods like `.isupper()`, `.islower()`, `.upper()`, and `.lower()` to solve the problem efficiently.

### **Day 26: The Dangerous Situation! (Codeforces 43A: Football)**
* **Problem Link:** [https://codeforces.com/problemset/problem/43/A](https://codeforces.com/problemset/problem/43/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a string representing a sequence of players with the ball. It then iterates through the string, checking for any consecutive substring of seven identical characters ('0's or '1's'). If such a substring is found, it's considered a "dangerous situation."
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the string, as we iterate through the string once to check for the dangerous pattern.
    * **Space Complexity:** O(1), as only a few variables are used to store the state.
* **Key Learnings:** Reinforced string iteration with slicing and careful handling of loop boundaries. This problem was a good exercise in pattern matching within a string.

### **Day 27: The Orange Cocktail! (Codeforces 200B: Drinks)**
* **Problem Link:** [https://codeforces.com/problemset/problem/200/B](https://codeforces.com/problemset/problem/200/B)
* **Solution Status:** Solved
* **Approach:** The solution calculates the average percentage of orange juice in a cocktail. Since equal proportions of each drink are mixed, the final concentration is simply the arithmetic mean of all the individual percentages. This is achieved by summing all percentages and dividing by the number of drinks.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the number of drinks, as we iterate through the list of percentages to calculate the sum.
    * **Space Complexity:** O(N), to store the list of `n` percentages in memory.
* **Key Learnings:** Practiced reading multiple integer inputs from a single line and applying a simple mathematical formula to solve a direct problem efficiently.

### **Day 28: Petya and Countryside! (Codeforces 35A: Petya and Countryside)**
* **Problem Link:** [https://codeforces.com/problemset/problem/35/A](https://codeforces.com/problemset/problem/35/A)
* **Solution Status:** Solved
* **Approach:** The solution iterates through each section of the garden as a potential watering source. For each section, it expands outwards (left and right) to count contiguous sections where the water will flow (i.e., the heights are non-increasing). The final answer is the maximum number of watered sections found from any starting point.
* **Complexity:**
    * **Time Complexity:** O(N^2), where N is the number of sections. The algorithm involves a nested loop, as for each section, we perform two passes of up to N steps each.
    * **Space Complexity:** O(N), as the list of heights is stored in memory.
* **Key Learnings:** Practiced iterating through all possible starting points for a problem and implementing nested loops with careful boundary checks. This problem was a good exercise in simulating a process to find an optimal outcome.

### **Day 29: Anton and Danik! (Codeforces 734A: Anton and Danik)**
* **Problem Link:** [https://codeforces.com/problemset/problem/734/A](https://codeforces.com/problemset/problem/734/A)
* **Solution Status:** Solved
* **Approach:** The solution reads the game outcomes as a string and uses Python's built-in `count()` method to efficiently determine the number of wins for Anton ('A') and Danik ('D'). A simple conditional check then compares the counts to determine the winner or declare a friendship.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the string, as the `count()` method performs a single pass.
    * **Space Complexity:** O(N), as the string of game outcomes is stored in memory.
* **Key Learnings:** Focused on simplifying code and improving efficiency by using built-in string methods instead of manual loops. This problem highlighted the importance of choosing the right tool for the job.

### **Day 30: Bear and Big Brother! (Codeforces 791A: Bear and Big Brother)**
* **Problem Link:** [https://codeforces.com/problemset/problem/791/A](https://codeforces.com/problemset/problem/791/A)
* **Solution Status:** Solved
* **Approach:** The solution employs a simple simulation loop. It repeatedly triples Bear Limak's weight and doubles his brother Bob's weight year by year, counting each year. The loop continues until Limak's weight is strictly greater than Bob's.
* **Complexity:**
    * **Time Complexity:** O(1), as the number of years required for Limak's weight to exceed Bob's is very small and constant given the problem constraints.
    * **Space Complexity:** O(1), as only a few constant variables are used to store the weights and the year count.
* **Key Learnings:** Practiced approaching problems using a simple simulation. This was a good reminder of how to use a `while` loop to model a process that continues until a specific condition is met.

### **Day 31: The Magnets Problem! (Codeforces 344A: Magnets)**
* **Problem Link:** [https://codeforces.com/problemset/problem/344/A](https://codeforces.com/problemset/problem/344/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a number `n` and then `n` magnet orientations. It iterates through the magnets, counting a new group whenever the current magnet's orientation is different from the previous one. A new group is formed when adjacent magnets repel each other, which occurs when their orientations are different.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the number of magnets, due to a single pass through the list of magnet orientations.
    * **Space Complexity:** O(N), as the list of magnet orientations is stored in memory.
* **Key Learnings:** Reinforced the importance of simple sequential comparison within a loop. This problem was a good exercise in translating a physical phenomenon (repelling magnets) into a straightforward logical condition.

### **Day 32: Nearly Lucky Numbers! (Codeforces 110A: Nearly Lucky Number)**
* **Problem Link:** [https://codeforces.com/problemset/problem/110/A](https://codeforces.com/problemset/problem/110/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a number as a string and iterates through its digits. It counts how many times the lucky digits '4' and '7' appear. The final result is determined by checking if this count is itself a lucky number (i.e., if the count is 4 or 7).
* **Complexity:**
    * **Time Complexity:** O(L), where L is the number of digits in the input number, as a single pass is performed over the string representation of the number.
    * **Space Complexity:** O(L), to store the number as a string.
* **Key Learnings:** Practiced basic string iteration and conditional logic. The problem was a good exercise in handling a two-part condition: first counting a specific set of digits, and then checking a condition on that count.

### **Day 33: Ultra-Fast Mathematician! (Codeforces 61A: Ultra-Fast Mathematician)**
* **Problem Link:** [https://codeforces.com/problemset/problem/61/A](https://codeforces.com/problemset/problem/61/A)
* **Solution Status:** Solved
* **Approach:** The solution reads two binary strings of the same length. It then iterates through them simultaneously, comparing the characters at each position. The resulting string is built digit by digit, where a '1' is placed if the corresponding digits in the input strings are different, and a '0' is placed if they are the same.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the strings, as the code performs a single pass over the input.
    * **Space Complexity:** O(N), as a new string of length N is created to store the output.
* **Key Learnings:** Practiced simultaneous iteration over two strings. This problem was a great exercise in translating a simple logical operation (XOR) into code and implementing it efficiently.

### **Day 34: The Presents Problem! (Codeforces 136A: Presents)**
* **Problem Link:** [https://codeforces.com/problemset/problem/136/A](https://codeforces.com/problemset/problem/136/A)
* **Solution Status:** Solved
* **Approach:** The solution reverses a given mapping. It reads `n` integers where the `i`-th number indicates who friend `i+1` gave a gift to. A new array is created, and the solution iterates through the original list, using the receiver's number as an index to store the giver's number.
* **Complexity:**
    * **Time Complexity:** O(N), as the code iterates through the list of `n` friends once.
    * **Space Complexity:** O(N), to store the resulting list of gift givers.
* **Key Learnings:** This problem was a good exercise in working with permutations and reversing mappings. It reinforced the importance of careful array indexing and translating problem logic into a clean implementation.

### **Day 36: Lucky Division! (Codeforces 122A: Lucky Division)**
* **Problem Link:** [https://codeforces.com/problemset/problem/122/A](https://codeforces.com/problemset/problem/122/A)
* **Solution Status:** Solved
* **Approach:** The solution pre-computes a list of all possible "lucky numbers" (numbers containing only the digits 4 and 7) within the given constraints. It then reads an integer `n` and checks if `n` is perfectly divisible by any number in the lucky numbers list.
* **Complexity:**
    * **Time Complexity:** O(1), as the number of lucky numbers to check is constant and small (a fixed list).
    * **Space Complexity:** O(1), to store the pre-computed list of lucky numbers.
* **Key Learnings:** Practiced a simple brute-force approach that is effective for problems with small constraints. This was a good reminder that a direct check can be more efficient than a complex algorithm when the search space is limited.

### **Day 37: HQ9+! (Codeforces 133A: HQ9+)**
* **Problem Link:** [https://codeforces.com/problemset/problem/133/A](https://codeforces.com/problemset/problem/133/A)
* **Solution Status:** Solved
* **Approach:** The solution reads a string representing a program. It then checks for the presence of specific characters ('H', 'Q', or '9') which, according to the problem, are the only instructions that produce output. The solution returns "YES" if any of these characters are found, and "NO" otherwise.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the length of the string, as the `in` operator performs a linear search.
    * **Space Complexity:** O(1), as the program does not use any data structures that scale with the input size.
* **Key Learnings:** Practiced using a simple and direct approach to check for the presence of multiple characters within a string. This problem was a good exercise in interpreting a problem's specific rules and translating them into a single, elegant conditional check.

### **Day 38: I_love_%username%! (Codeforces 155A: I_love_%username%)**
* **Problem Link:** [https://codeforces.com/problemset/problem/155/A](https://codeforces.com/problemset/problem/155/A)
* **Solution Status:** Solved
* **Approach:** The solution reads the number of contests `n` and a list of scores. It initializes `best` and `worst` scores with the first contest's score. It then iterates through the remaining scores, and for each score, it checks if it's strictly greater than the current `best` or strictly less than the current `worst`. If either condition is true, a counter for "amazing performances" is incremented, and the `best` or `worst` score is updated.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the number of contests, as the solution involves a single pass through the list of scores.
    * **Space Complexity:** O(N), to store the list of scores in memory.
* **Key Learnings:** Practiced efficiently tracking dynamic minimum and maximum values within a single loop. The problem was a good exercise in applying simple conditional logic and updating state variables to solve a sequential data problem.

### **Day 39: Arrival of the General! (Codeforces 118A: Arrival of the General)**
* **Problem Link:** [https://codeforces.com/problemset/problem/118/A](https://codeforces.com/problemset/problem/118/A)
* **Solution Status:** Solved
* **Approach:** The solution finds the first occurrence of the maximum height and the last occurrence of the minimum height in the line of soldiers. The total swaps required are calculated as the moves needed to bring the tallest soldier to the front plus the moves to bring the shortest soldier to the back. A special case is handled if the tallest soldier is originally to the right of the shortest, in which case one swap is counted for both.
* **Complexity:**
    * **Time Complexity:** O(N), as the solution involves three passes through the array: two to find the indices of the max and min values and one for the initial `max()` and `min()` calls.
    * **Space Complexity:** O(N), to store the list of soldier heights.
* **Key Learnings:** Practiced finding specific elements in an array and carefully handling edge cases. This problem was a great exercise in translating a logical, real-world scenario (swapping neighbors in a line) into a minimal-operations algorithm.

### **Day 40: George and Accommodation! (Codeforces 467A: George and Accommodation)**
* **Problem Link:** [https://codeforces.com/problemset/problem/467/A](https://codeforces.com/problemset/problem/467/A)
* **Solution Status:** Solved
* **Approach:** The solution reads the total number of rooms `n`. It then iterates `n` times, reading the current number of people `p` and the room's capacity `q` for each room. The code checks if the number of available spots (`q - p`) is 2 or greater. A counter is incremented for each room that meets this condition.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the number of rooms, as the code processes each room exactly once.
    * **Space Complexity:** O(1), as only a few variables are used to store the state during the loop.
* **Key Learnings:** Practiced a simple conditional counting loop, which is a fundamental programming pattern. The problem was a good exercise in translating a direct logical condition from the problem statement into a single `if` statement.

### **Day 41: Young Physicist! (Codeforces 69A: Young Physicist)**
* **Problem Link:** [https://codeforces.com/problemset/problem/69/A](https://codeforces.com/problemset/problem/69/A)
* **Solution Status:** Solved
* **Approach:** The solution reads the number of force vectors `n` and then iterates `n` times to read the `x`, `y`, and `z` components of each vector. It maintains a running sum for each of the three coordinates. For a body to be in equilibrium, the sum of all x, y, and z forces must be zero. A final check confirms that all three coordinate sums are zero.
* **Complexity:**
    * **Time Complexity:** O(N), where N is the number of force vectors. The code processes each vector's components once.
    * **Space Complexity:** O(1), as only a few variables are used to store the running sums and the input.
* **Key Learnings:** Practiced translating a real-world physics problem (equilibrium of forces) into a simple coding solution. The problem reinforced the importance of summing up components independently and applying a basic conditional check to solve a problem involving vectors.

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
