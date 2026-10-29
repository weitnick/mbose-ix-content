# Revision IV — Iterative Constructs and Nested Loops

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 4 |
| Title | Revision IV — Iterative Constructs and Nested Loops |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 1. Revision of Class IX syllabus: (viii) Iterative constructs in Java, (ix) Nested for loops |
| Exam weightage | Section A always has **"give the output and the number of times the loop runs"** (2 marks) and a **loop conversion** (for ↔ while ↔ do-while, 2 marks), plus MCQs on **entry/exit-controlled loops, infinite loops, break and continue**. Section B almost always has a **special-number program** (spy, pronic, EvenPal, Mark, buzz, SUPERSPY…) built on **digit extraction** (15 marks), and patterns and series appear inside overloading questions. |
| Syllabus scope | Need for loops; entry-controlled (for, while) and exit-controlled (do-while) loops; parts and variations of the for loop (multiple counters, missing parts, empty body/delay); finite and infinite loops; inter-conversion of loops; jump statements break and continue; nested for loops with rectangular and right-angled triangular patterns; series involving a single variable; digit-based number programs. Nested while and nested do-while loops are not in your exam. |
| In short | A revision of loops in Java, including for, while and do-while, nested loops, and controlling them with break and continue. |

> **Note on the text:** CISCE does not prescribe a textbook for ICSE Computer Applications. This chapter is written to the ICSE 2027 syllabus in its own words; its exam questions are the CISCE board papers of 2017–2026 and the specimen papers of 2024 and 2025, answered from CISCE's marking schemes wherever one has been published. **Every loop output and program in this chapter was compiled and run (Java 21).**
>
> **Exam note:** To count iterations, **trace a table** of the loop variable: write each value, test the condition, and stop when it is false. A **semicolon right after `for(…)`** makes the loop body **empty** — the loop still runs, then the next statement runs **once** with the final value (`for (k = 10; k >= 1; k -= 3);` leaves k = −2). A **do-while** runs **at least once**; a for/while whose condition is false at the start runs **zero times**. In a do-while → for conversion, keep the **same order** of statements inside the body. For digit programs: **last digit = n % 10**, **remove it with n = n / 10**, and keep a **copy** of n when you need it later.

---

## 1. Complete Lesson

### Why loops?

An **iterative construct (loop)** repeats a set of statements as long as a condition is true. Loops save writing the same statement many times — printing 1 to 100, adding marks of 40 students, or checking every digit of a number.

Each loop has: **initialisation** of a control variable, a **test condition**, the **body**, and an **update** of the control variable.

![Fig. 4.1 Entry- and exit-controlled loops](figures/ca_ch04_fig01_loops.png)

### The for loop (entry-controlled)

```java
for (initialisation; condition; update)
{
    body;
}
```
- **Initialisation** runs **only once**, at the start.
- The **condition** is tested **before every iteration**; when it is false the loop ends.
- The **update** runs after each iteration.

```java
for (int i = 1; i <= 5; i++)
    System.out.print(i + " ");      // 1 2 3 4 5
```

**Variations of the for loop**

| Variation | Example | Effect |
|---|---|---|
| Multiple counters | `for (k = 1, m = 5; k <= 10; k++, m++)` | Two variables initialised and updated together |
| Decreasing loop | `for (i = 10; i >= 1; i--)` | Counts down |
| Steps other than 1 | `for (i = 11; i <= 30; i += 2)` | 11, 13, …, 29 — **10 times** |
| Missing parts | `for (; i <= 10; )` | Initialisation and update written elsewhere |
| Empty body (**delay loop**) | `for (k = 10; k >= 1; k -= 3);` | Only the variable changes; used to cause a delay |
| Infinite | `for (;;)` or `for (int i = 2; i != 0; i -= 3)` | The condition never becomes false |

### The while loop (entry-controlled)

```java
initialisation;
while (condition)
{
    body;
    update;
}
```
Used when the number of repetitions is **not known in advance** — for example, "while the number is greater than 0, take off a digit".

### The do-while loop (exit-controlled)

```java
initialisation;
do
{
    body;
    update;
} while (condition);      // note the semicolon
```
The condition is tested **after** the body, so the body runs **at least once**.

| while | do-while |
|---|---|
| **Entry-controlled** — condition tested first | **Exit-controlled** — condition tested last |
| May execute **zero** times | Executes **at least once** |
| No semicolon after `while (condition)` | Ends with `while (condition);` |

**Example 1.** *(ICSE 2026, Q2(vi))* Give the output and how many times the loop runs: `int K = 1; do { K += 2; System.out.println(K); } while (K <= 6);`
**Solution:**

| K before body | K after `K += 2` (printed) | `K <= 6`? |
|---|---|---|
| 1 | 3 | true |
| 3 | 5 | true |
| 5 | 7 | false — stop |

Output **3, 5, 7** (each on a new line); the loop runs **3 times**.

### Finite and infinite loops

A **finite loop** ends after a fixed number of iterations. An **infinite loop** never ends because its condition never becomes false:

```java
for (int i = 5; i != 0; i -= 2)     // 5, 3, 1, -1, … never 0 — infinite
while (true) { … }                  // infinite unless a break ends it
```

### Inter-conversion of loops

The same task can be written with any loop. Keep the **initialisation**, **condition**, **body** and **update** in the same order.

```java
// for loop
for (k = 1, m = 5; k <= 10; k++, m++)
    System.out.println(k * m);

// while loop
k = 1; m = 5;
while (k <= 10)
{
    System.out.println(k * m);
    k++; m++;
}

// do-while loop (exit-controlled)
k = 1; m = 5;
do
{
    System.out.println(k * m);
    k++; m++;
} while (k <= 10);
```

**Example 2.** *(ICSE 2025, Q2(iv))* Convert into an exit-controlled loop: `int a, b; for (a = 10, b = 1; a >= 1; a -= 2) { b += a; b++; } System.out.print(b);`
**Solution:**
```java
int a = 10, b = 1;
do
{
    b += a;
    b++;
    a -= 2;
} while (a >= 1);
System.out.print(b);      // 36
```

### Jump statements: break and continue

| Statement | Effect | Example |
|---|---|---|
| **break** | **Ends the loop** at once; control goes to the statement after the loop | Stop searching once a factor is found |
| **continue** | **Skips the rest of the current iteration** and goes to the next one | Skip even numbers |
| return | Leaves the whole method (Chapter 6) | `return sum;` |

```java
for (int a = 1; a <= 10; a++)
{
    if (a % 2 == 0)
        continue;              // skip even values
    System.out.print(a + " ");  // 1 3 5 7 9
}
```

**Example 3.** *(ICSE 2017, Q2(d))* Give the output and the number of times the loop runs:
```java
int a, b;
for (a = 6, b = 4; a <= 24; a = a + 6)
{
    if (a % b == 0)
        break;
}
System.out.println(a);
```
**Solution:** a = 6: 6 % 4 ≠ 0; a = 12: 12 % 4 = 0 → break. Output **12**; the loop runs **2 times**.

### Nested for loops

A loop inside another loop. For each value of the **outer** loop, the **inner** loop runs completely. If the outer loop runs m times and the inner n times, the inner body runs **m × n** times. A clock is a real-life example: the minute hand completes 60 positions for each of the hour hand's 12.

**Rectangular pattern** (rows × columns):
```java
for (int i = 1; i <= 4; i++)
{
    for (int j = 1; j <= 5; j++)
        System.out.print(i + " ");
    System.out.println();
}
// 1 1 1 1 1
// 2 2 2 2 2
// 3 3 3 3 3
// 4 4 4 4 4
```

**Right-angled triangle** (the inner loop depends on the outer):
```java
for (int i = 1; i <= 4; i++)
{
    for (int j = 1; j <= i; j++)
        System.out.print("* ");
    System.out.println();
}
// *
// * *
// * * *
// * * * *
```
Use `for (int i = n; i >= 1; i--)` for an **inverted** triangle. A `break` or `continue` inside the inner loop affects **only the inner loop**.

### Series involving a single variable

Keep an **accumulator**, and build each **term** from the loop variable.

| Series | Term inside the loop |
|---|---|
| 1 + 2 + 3 + … + n | `s += i;` |
| 1 + 1/2 + 1/3 + … + 1/n | `s += 1.0 / i;` |
| x + x²/2 + x³/3 + … + xⁿ/n | `s += Math.pow(x, i) / i;` |
| x − x² + x³ − x⁴ … | add odd powers, subtract even powers |
| 1, 11, 111, 1111 … | `term = term * 10 + 1;` |
| 0, 7, 26, 63 … (i³ − 1) | `print(i * i * i - 1);` |
| 0 1 1 2 3 5 … (Fibonacci) | `c = a + b; a = b; b = c;` |

### Digit extraction — the heart of number programs

```java
int num = n;            // keep n safe; work on a copy
while (num > 0)
{
    int d = num % 10;   // last digit
    // use d: count, add, multiply, compare, reverse …
    num = num / 10;     // remove the last digit
}
```

| Task | Statement inside the loop |
|---|---|
| Count digits | `count++;` |
| Sum of digits | `sum += d;` |
| Product of digits | `prod *= d;` (start prod at 1) |
| Reverse | `rev = rev * 10 + d;` |
| Largest / smallest digit | `if (d > large) large = d;` |
| First digit | loop `while (first >= 10) first /= 10;` |

**Common special numbers in ICSE papers**

| Name | Rule | Example |
|---|---|---|
| **Palindrome** | equals its reverse | 121 |
| **Spy** | sum of digits = product of digits | 1124 (8 = 8) |
| **Armstrong** | sum of each digit raised to the number of digits = the number | 153, 1634 |
| **Pronic** | product of two consecutive integers | 42 = 6 × 7 |
| **Duck** | contains a zero (not at the start) | 103 |
| **Tech** (4-digit) | (first half + second half)² = the number | 3025 = (30 + 25)² |
| **EvenPal** | palindrome **and** even sum of digits | 121 |
| **Mark** | sum of squares of digits is even **and** ends in the same digit as the number | 246 → 56 |
| **Special buzz** | ends in 7 **and** digit sum divisible by 7 | 957 |
| **SUPERSPY** | sum of digits = number of digits | 1021 |
| **Prime** | exactly two factors | 29 |

### Summary of the chapter

- **Loops** repeat statements: initialisation, condition, body, update.
- **Entry-controlled:** for, while (may run 0 times). **Exit-controlled:** do-while (at least once; ends with `;`).
- **for** — initialisation once; variations: multiple counters, missing parts, steps, empty body (delay), infinite.
- **Conversion** between for, while and do-while keeps the same logic.
- **break** ends a loop; **continue** skips to the next iteration.
- **Nested for** — inner loop completes for each outer value; rectangles and right-angled triangles; m × n executions.
- **Series** with an accumulator; **digit programs** with % 10 and / 10 on a copy of n.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Explain the need for loops and the parts of a loop.
2. Write for, while and do-while loops and distinguish entry- and exit-controlled loops.
3. Trace loops to find their output and the number of iterations, including empty-body and infinite loops.
4. Convert a loop of one type into another.
5. Use break and continue correctly.
6. Write nested for loops for rectangular and right-angled triangular patterns.
7. Sum series involving a single variable.
8. Write digit-extraction programs for special numbers.

---

## 3. Detailed Section Explanations

### Section 1 — Trace, don't guess
A three-column table (value, condition, output) answers every "how many times" question. Watch the update and the boundary value.

### Section 2 — The invisible empty body
`for (…);` and `while (…);` loop with nothing inside. The next statement runs once, after the loop, with the final value of the variable.

### Section 3 — Copy before you chop
Digit extraction destroys the number (`num /= 10`). Keep the original in another variable to compare at the end (palindrome, Armstrong).

### Section 4 — Inner completes first
In a nested loop, the inner loop finishes all its rounds before the outer loop moves on — like the minute hand before the hour hand.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Loop (iterative construct) | A statement that repeats a block while a condition is true. |
| Iteration | One execution of the loop body. |
| Control variable | The variable that controls the loop. |
| Entry-controlled loop | A loop that tests the condition before the body (for, while). |
| Exit-controlled loop | A loop that tests the condition after the body (do-while). |
| Finite loop | A loop that ends after a fixed number of iterations. |
| Infinite loop | A loop whose condition never becomes false. |
| Delay loop | A loop with an empty body, used to pass time. |
| break | Ends a loop immediately. |
| continue | Skips the rest of the current iteration. |
| Nested loop | A loop inside another loop. |
| Accumulator | A variable that builds a total. |
| Counter | A variable that counts iterations or items. |
| Digit extraction | Taking digits from a number with % 10 and / 10. |
| Palindrome number | A number equal to its reverse. |
| Armstrong number | Equal to the sum of its digits raised to the number of digits. |
| Pronic number | The product of two consecutive integers. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| Entry-controlled loops | for and while |
| Exit-controlled loop | do-while (runs at least once) |
| Part of a for executed only once | Initialisation |
| `for (int i = 2; i != 0; i -= 3)` | Infinite |
| `for (k = 10; k >= 0; k--)` runs | 11 times |
| `for (int i = 11; i <= 30; i += 2)` runs | 10 times |
| `for (p = 4; p > 0; p -= 2); print(p); println(p);` | 00 |
| Loop with a false condition at the start | Runs 0 times (for/while) |
| Jump statements | break, continue (and return) |
| Construct for 10 side stretches | for |
| Clock hands | Nested loops |
| Last digit / remove last digit | n % 10 / n = n / 10 |
| Four-digit tech numbers | 2025, 3025, 9801 |

### 5.2 Memory aids

- **"For and While check at the door; Do goes in first"** — entry vs exit control.
- **"Mod takes, Divide shakes off"** — % 10 takes the last digit; / 10 removes it.
- **"Break leaves the room, Continue skips a turn."**

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- Java also has an enhanced for loop (`for (int x : arr)`) for arrays — not in the ICSE syllabus.
- A labelled break can end an outer loop from inside an inner one.
- Programs that loop forever on purpose — servers, games — use `while (true)` with a break or exit condition inside.

---

## 6. Person Profiles

### 6.1 Ada Lovelace (1815–1852)
An English mathematician who wrote what is regarded as the first published algorithm for Charles Babbage's Analytical Engine — to compute Bernoulli numbers — and described the idea of repeating a set of operations, an early form of a loop.

### 6.2 Srinivasa Ramanujan (1887–1920)
An Indian mathematician famous for his insight into numbers and series. The "taxicab number" 1729, the smallest number expressible as the sum of two cubes in two ways, is named after a conversation with G. H. Hardy — a favourite loop-and-digit puzzle for programmers.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Repetition with variation** — the same steps, a different value each time.
- **Stop conditions matter** — every loop needs a way out.
- **Numbers hide patterns** — digit loops reveal palindromes, Armstrong and spy numbers.

### 7.2 Real-life connections
- **Meghalaya:** a weekly rainfall report loops over seven days to total and average the rain recorded at Mawsynram.
- **Games:** a game loop keeps redrawing the screen until the player quits — a while loop with a break.
- **Banking:** compound interest year by year is a loop that multiplies the amount each time.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section A** (40 marks) has MCQs and 2-mark parts on tracing loops, counting iterations and converting loops; **Section B** (60 marks, any four of six programs) almost always includes a **digit-based special-number program**, and patterns and series appear in overloading programs.

### 8.1 Graded exercises — solutions

#### Exercise 4A — Tracing loops

**Q1.** How many times does `for (int i = 1; i <= 20; i += 3)` run, and what is i after the loop?
**Answer:** 7 times (1, 4, 7, 10, 13, 16, 19); i = 22 afterwards.

**Q2.** Give the output: `int n = 4279, d; while (n > 0) { d = n % 10; System.out.println(d); n = n / 100; }`
**Answer:** 9 and 2 on two lines — 4279 → 42 → 0.

**Q3.** Give the output: `int i; for (i = 5; i > 10; i++) System.out.println(i); System.out.println(i * 4);`
**Answer:** `20` — the loop runs zero times.

**Q4.** Is `while (true) { … }` always infinite?
**Answer:** No — a break inside it can end the loop (e.g. when x % 3 == 0).

#### Exercise 4B — Writing loops

**Q5.** Write a loop to print the multiplication table of 7 up to 7 × 10.
**Answer:** `for (int i = 1; i <= 10; i++) System.out.println("7 x " + i + " = " + 7 * i);`

**Q6.** Write statements to count the digits of n.
**Answer:** `int c = 0; for (int t = n; t > 0; t /= 10) c++;`

**Q7.** Write statements to reverse n.
**Answer:** `int rev = 0, t = n; while (t > 0) { rev = rev * 10 + t % 10; t /= 10; }`

**Q8.** Write a nested loop to print 1 / 1 2 / 1 2 3 / 1 2 3 4 / 1 2 3 4 5.
**Answer:** `for (int i = 1; i <= 5; i++) { for (int j = 1; j <= i; j++) System.out.print(j + " "); System.out.println(); }`

### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(ix) (1 mark) | [Picture: the earth spinning on its axis and revolving around the sun] The earth spins on its axis completing one rotation in a day. The earth revolves around the sun in 365 days to complete one revolution. What is the Java concept depicted in the given picture? (a) Array (b) Condition (c) Nested loop (d) While loop |
| ICSE 2026, Q2(i) (2 marks) | Rewrite the following program segment using a for loop. `int a = 5, b = 10; while (b > 0) { b -= 2; } System.out.println(a * b);` |
| ICSE 2026, Q2(vi) (2 marks) | Give the output of the following program segment and mention how many times the loop is executed. `int K = 1; do { K += 2; System.out.println(K); } while (K <= 6);` |
| ICSE 2026, Q6 (15 marks) | Write a program to accept a number and check if it is a Mark number or not. A number is said to be Mark when sum of the squares of each digit is an even number as well as the last digit of the sum and the last digit of the number given is same. Example: n = 246, sum = 2 x 2 + 4 x 4 + 6 x 6 = 56; 56 is an even number as well as last digit is 6 for both sum as well as the number. |
| ICSE 2026 Improvement, Q1(xiii) (1 mark) | Which statement is executed only once in a for statement? `for(initialisation; check; update) { body of the loop }` (a) Update (b) check (c) initialisation (d) body of the loop |
| ICSE 2026 Improvement, Q2(vi) (2 marks) | Give the output of the following program segment, also mention how many times the following loop is executed. `for (k = 10; k >= 1; k -= 3); System.out.println(k*5);` |
| ICSE 2026 Improvement, Q2(x) (2 marks) | Rewrite the following program segment using the exit controlled statement: `for (k = 1, m = 5; k <= 10; k++, m++) System.out.println(k*m);` |
| ICSE 2026 Improvement, Q4 (15 marks) | Define a class to accept a number and check if it is a Special buzz number or not. A number is a Special buzz number if it ends with 7 and the sum of the digits of the number is also divisible by 7. Example: 957 — the number ends with 7 and the sum of the digits (9 + 5 + 7 = 21) also is divisible by 7. |
| ICSE 2025, Q1(vii) (1 mark) | Select the infinite loop: (a) `for(int i=1;i<=10;i++)` (b) `for(int i=2; i!=0; i-=3)` (c) `for(int i=5; i<=5; i++)` (d) `for(int i=1; i>=1; i--)` |
| ICSE 2025, Q1(xii) (1 mark) | [Picture: a student doing a side stretch] A physical education teacher asks the students to do the side stretch as shown below, 10 times. Which programming construct the teacher uses? (a) if (b) switch (c) for (d) if else if |
| ICSE 2025, Q1(xiv) (1 mark) | Assertion (A): A clock is a real-life example of nested loops. Reason (R): The hour hand moves through 12 positions, while the minute hand moves through 60 positions within each hour. (a) Both (A) and (R) are true and (R) is a correct explanation of (A). (b) Both (A) and (R) are true and (R) is not a correct explanation of (A). (c) (A) is true and (R) is false. (d) (A) is false and (R) is true. |
| ICSE 2025, Q1(xvii) (1 mark) | Consider the program segment: `int p=0; for(p=4; p>0; p-=2); System.out.print(p); System.out.println(p);` The above statements will display: (a) 42 (b) 4200 (c) 0 0 (d) 00 |
| ICSE 2025, Q1(xx) (1 mark) | Consider the following program segment in which the statements are jumbled. Choose the correct order of statements to calculate and return the factorial of 4. `for (k=1; k<=4; k++)` → 1; `return fa;` → 2; `long fa = 1, k;` → 3; `fa*=k;` → 4. (a) 1, 2, 3, 4 (b) 3, 1, 4, 2 (c) 3, 1, 2, 4 (d) 1, 3, 2, 4 |
| ICSE 2025, Q2(iv) (2 marks) | Convert the given loop into exit controlled loop. `int a,b; for (a=10, b=1; a>=1; a-=2) { b+=a; b++; } System.out.print(b);` |
| ICSE 2025, Q8 (15 marks) | Define a class to accept a number. Check if the sum of the largest digit and the smallest digit is an even number or an odd number. Print appropriate messages. Sample Input: 6425, 3748. Largest digit: 6, 8. Smallest digit: 2, 3. Sample Output: Sum is even; Sum is odd. |
| ICSE 2025 Improvement, Q1(xix) (1 mark) | How many times the for statement given below is executed? `for (k = 10; k>=0; k--)` (a) 10 (b) 11 (c) 12 (d) 0 |
| ICSE 2025 Improvement, Q1(xx) (1 mark) | Consider the following program segment in which the statements are jumbled. Choose the correct order of the statements to return the sum of first 10 natural numbers. `for(i=1; i<=10; i++)` → 1; `return sum;` → 2; `int sum = 0, i;` → 3; `sum+=i;` → 4. (a) 1 2 3 4 (b) 3 4 1 2 (c) 1 4 2 3 (d) 3 1 4 2 |
| ICSE 2025 Improvement, Q2(iv) (2 marks) | Write the output of the following program segment: `for (int a=1; a<=10; a++) { if (a%2==0) continue; System.out.print(a+" "); }` |
| ICSE 2025 Improvement, Q2(vi) (2 marks) | Give the output of the following program segment and mention how many times the loop is executed. `int k = 100; while (k>=10) { System.out.println(k); k-=40; }` |
| ICSE 2025 Improvement, Q7 (15 marks) | Define a class to accept a number and check if the sum of the first digit and the last digit is an even number or an odd number. Example: N = 2396, N = 9316. First digit: 2, 9. Last digit: 6, 6. Sum: 8, 15. Output: Sum is even; Sum is odd. |
| ICSE 2025 specimen, Q1(x) (1 mark) | To execute a loop 10 times, which of the following is correct? (a) `for (int i=11;i<=30;i+=2)` (b) `for (int i=11;i<=30;i+=3)` (c) `for (int i=11;i<20;i++)` (d) `for (int i=11;i<=21;i++)` |
| ICSE 2025 specimen, Q2(v) (2 marks) | How many times will the following loop execute? Write the output of the code: `int x=10; while (true) { System.out.println(x++ * 2); if(x%3==0) break; }` |
| ICSE 2025 specimen, Q7 (15 marks) | Define a class to accept a number and check whether it is a SUPERSPY number or not. A number is called SUPERSPY if the sum of the digits equals the number of the digits. Example 1: Input 1021 — SUPERSPY number [sum of the digits = 1+0+2+1 = 4, number of digits = 4]. Example 2: Input 125 — Not a SUPERSPY number [1+2+5 is not equal to 3]. |
| ICSE 2024, Q1(xiii) (1 mark) | Which of the following are entry controlled loops? 1. for 2. while 3. do..while 4. switch (a) only 1 (b) 1 and 2 (c) 1 and 3 (d) 3 and 4 |
| ICSE 2024, Q2(iii) (2 marks) | Rewrite the following do while program segment using for: `x = 10; y = 20; do { x++; y++; } while (x<=20); System.out.println(x * y);` |
| ICSE 2024, Q2(iv) (2 marks) | Give the output of the following program segment. How many times is the loop executed? `for(x=10; x>20; x++) System.out.println(x); System.out.println(x*2);` |
| ICSE 2024, Q5 (15 marks) | Define a class to accept a number from user and check if it is an EvenPal number or not. (The number is said to be EvenPal number when number is palindrome number (a number is palindrome if it is equal to its reverse) and sum of its digits is an even number.) Example: 121 is a palindrome number; sum of the digits 1+2+1 = 4, which is an even number. |
| ICSE 2024 specimen, Q2(v) (2 marks) | How many times will the following loop execute? What value will be returned? `int x=2; int y=50; do { ++x; y-=x++; } while(x<=10); return y;` |
| ICSE 2024 specimen, Q2(vii) (2 marks) | Name any two jump statements. |
| ICSE 2024 specimen, Q7 (15 marks) | Define a class to accept a 3 digit number and check whether it is a duck number or not. Note: A number is a duck number if it has zero in it. Example 1: Input 2083 — Output: Invalid. Example 2: Input 103 — Output: Duck number. |
| ICSE 2023, Q1(vii) (1 mark) | State the type of loop in the given program segment: `for (int i = 5; i != 0; i -= 2) System.out.println(i);` (a) finite (b) infinite (c) null (d) fixed |
| ICSE 2023, Q2(iii) (2 marks) | Convert the following do…while loop to for loop: `int x=10; do { x--; System.out.print(x); } while (x>=1);` |
| ICSE 2023, Q2(vi) (2 marks) | Give the output of the following program segment: `int n = 4279; int d; while(n>0) { d=n%10; System.out.println(d); n=n/100; }` |
| ICSE 2020, Q2(e) (2 marks) | What is an infinite loop? Give an example. |
| ICSE 2020, Q3(e) (2 marks) | Give the output of the following program segment and mention how many times the loop will execute: `int k; for (k = 5; k <= 20; k += 7) if (k%6==0) continue; System.out.println(k);` |
| ICSE 2019, Q3(d) (2 marks) | Give the output of following code and mention how many times the loop will execute? `int i; for (i=5; i>=1; i--) { if (i%2 == 1) continue; System.out.print(i + " "); }` |
| ICSE 2019, Q9 (15 marks) | A tech number has even number of digits. If the number is split in two equal halves, then the square of sum of these halves is equal to the number itself. Write a program to generate and print all four digits tech numbers. Example: 3025 — square of sum of the halves = (30 + 25)² = (55)² = 3025 is a tech number. |
| ICSE 2018, Q2(b) (2 marks) | State the difference between while and do while loop. |
| ICSE 2018, Q3(j) (2 marks) | Give the output of the following program segment and also mention how many times the loop is executed: `int i; for (i = 5; i > 10; i++) System.out.println(i); System.out.println(i * 4);` |
| ICSE 2018, Q5 (15 marks) | Write a program to input a number and check and print whether it is a Pronic number or not. (Pronic number is the number which is the product of two consecutive integers.) Examples: 12 = 3 × 4, 20 = 4 × 5, 42 = 6 × 7 |
| ICSE 2017, Q2(d) (2 marks) | Give the output of the following program segment and also mention the number of times the loop is executed: `int a,b; for (a = 6, b = 4; a <= 24; a = a + 6) { if (a%b == 0) break; } System.out.println(a);` |
| ICSE 2017, Q3(d) (2 marks) | Convert following do-while loop into for loop. `int i = 1; int d = 5; do { d = d*2; System.out.println(d); i++; } while (i <= 5);` |
| ICSE 2017, Q3(i) (2 marks) | Analyze the given program segment and answer the following questions: `for (int i=3; i<=4; i++) { for (int j=2; j<i; j++) { System.out.print(""); } System.out.println("WIN"); }` (i) How many times does the inner loop execute? (ii) Write the output of the program segment. |
| ICSE 2017, Q5 (15 marks) | Write a program to accept a number and check and display whether it is a spy number or not. (A number is spy if the sum of its digits equals the product of its digits.) Example: consider the number 1124 — sum of the digits = 1 + 1 + 2 + 4 = 8; product of the digits = 1 × 1 × 2 × 4 = 8. |

**Solutions**

**2026 Q1(ix).** **(c) Nested loop** — 365 rotations happen within each revolution, like an inner loop inside an outer loop. *(Worked answer.)*

**2026 Q2(i).**
```java
int a = 5, b;
for (b = 10; b > 0; b -= 2)
{
}
System.out.println(a * b);     // 0
```
(The body is empty: b goes 10, 8, 6, 4, 2, 0; the output is 0.) *(Worked answer.)*

**2026 Q2(vi).** Output **3, 5, 7** (each on a new line); the loop executes **3 times** — K becomes 3, 5, 7 and stops when 7 <= 6 is false. *(Worked answer.)*

**2026 Q6.**
```java
import java.util.*;
class MarkNumber
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int num = n, sum = 0;
        while (num > 0)
        {
            int d = num % 10;
            sum = sum + d * d;          // sum of squares of the digits
            num = num / 10;
        }
        if (sum % 2 == 0 && sum % 10 == n % 10)
            System.out.println(n + " is a Mark number (sum = " + sum + ")");
        else
            System.out.println(n + " is not a Mark number (sum = " + sum + ")");
    }
}
```
Sample runs: `246 is a Mark number (sum = 56)`; `123 is not a Mark number (sum = 14)`. *(Worked answer.)*

**2026 Improvement Q1(xiii).** **(c) initialisation.** *(Worked answer.)*

**2026 Improvement Q2(vi).** The semicolon makes the body empty: k = 10, 7, 4, 1 (4 iterations), then k = −2 fails the test. Output **-10**; the loop executes **4 times**. *(Worked answer.)*

**2026 Improvement Q2(x).**
```java
k = 1; m = 5;
do
{
    System.out.println(k * m);
    k++;
    m++;
} while (k <= 10);
```
*(Worked answer.)*

**2026 Improvement Q4.**
```java
import java.util.*;
class SpecialBuzz
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int num = n, sum = 0;
        while (num > 0)
        {
            sum = sum + num % 10;
            num = num / 10;
        }
        if (n % 10 == 7 && sum % 7 == 0)
            System.out.println(n + " is a Special buzz number");
        else
            System.out.println(n + " is not a Special buzz number");
    }
}
```
Sample runs: `957 is a Special buzz number`; `147 is not a Special buzz number` (1 + 4 + 7 = 12). *(Worked answer.)*

**2025 Q1(vii).** **(b) `for(int i=2; i!=0; i-=3)`** — i takes 2, −1, −4 … and is never 0.

**2025 Q1(xii).** **(c) for.**

**2025 Q1(xiv).** **(a) Both (A) and (R) are true and (R) is a correct explanation of (A).**

**2025 Q1(xvii).** **(d) 00** — the empty loop leaves p = 0; print and println then show 0 and 0 together.

**2025 Q1(xx).** **(b) 3, 1, 4, 2** — `long fa = 1, k; for (k=1; k<=4; k++) fa*=k; return fa;`

**2025 Q2(iv).**
```java
int a = 10, b = 1;
do
{
    b += a;
    b++;
    a -= 2;
} while (a >= 1);
System.out.print(b);      // 36
```

**2025 Q8.** As in the scheme, start both largest and smallest at the last digit and compare every digit:
```java
import java.util.*;
class LargeSmall
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int large = n % 10, small = n % 10;     // start with the last digit
        while (n > 0)
        {
            int d = n % 10;
            if (d > large)
                large = d;
            if (d < small)
                small = d;
            n = n / 10;
        }
        System.out.println("Largest digit: " + large);
        System.out.println("Smallest digit: " + small);
        if ((large + small) % 2 == 0)
            System.out.println("Sum is even");
        else
            System.out.println("Sum is odd");
    }
}
```
Sample runs: 6425 → largest 6, smallest 2, **Sum is even**; 3748 → largest 8, smallest 3, **Sum is odd**.

**2025 Improvement Q1(xix).** **(b) 11** — k = 10, 9, …, 0. *(Worked answer.)*

**2025 Improvement Q1(xx).** **(d) 3 1 4 2** — `int sum = 0, i; for (i=1; i<=10; i++) sum+=i; return sum;` *(Worked answer.)*

**2025 Improvement Q2(iv).** `1 3 5 7 9` — continue skips the even values. (The paper printed `a<=10:a++`; it should be a semicolon.) *(Worked answer.)*

**2025 Improvement Q2(vi).** Output **100, 60, 20** (each on a new line); the loop runs **3 times** (k becomes −20). *(Worked answer.)*

**2025 Improvement Q7.**
```java
import java.util.*;
class FirstLast
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int last = n % 10;
        int first = n;
        while (first >= 10)          // keep removing digits until one is left
            first = first / 10;
        int sum = first + last;
        System.out.println("First digit: " + first);
        System.out.println("Last digit: " + last);
        System.out.println("Sum: " + sum);
        if (sum % 2 == 0)
            System.out.println("Sum is even");
        else
            System.out.println("Sum is odd");
    }
}
```
Sample runs: 2396 → 2 + 6 = 8, **Sum is even**; 9316 → 9 + 6 = 15, **Sum is odd**. *(Worked answer.)*

**2025 specimen Q1(x).** **(a) `for (int i=11;i<=30;i+=2)`** — 11, 13, …, 29.

**2025 specimen Q2(v).** The loop is executed **two times**; output **20** and **22**.

**2025 specimen Q7.** Count the digits (counter) and add them (accumulator), then compare:
```java
import java.util.*;
class SuperSpy
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int num = n, sum = 0, count = 0;
        while (num > 0)
        {
            sum = sum + num % 10;       // accumulator
            count++;                    // counter
            num = num / 10;
        }
        if (sum == count)
            System.out.println("SUPERSPY number");
        else
            System.out.println("Not a SUPERSPY number");
    }
}
```
Sample runs: 1021 → **SUPERSPY number**; 125 → **Not a SUPERSPY number**.

**2024 Q1(xiii).** **(b) 1 and 2.**

**2024 Q2(iii).**
```java
for (x = 10, y = 20; x <= 20; x++, y++);
System.out.println(x * y);     // 651
```

**2024 Q2(iv).** Output **20**; the loop is **not executed even once** (zero times).

**2024 Q5.** Reverse the number and add its digits in the same loop:
```java
import java.util.*;
class EvenPal
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int num = n, rev = 0, sum = 0;
        while (num > 0)
        {
            int d = num % 10;
            rev = rev * 10 + d;         // build the reverse
            sum = sum + d;
            num = num / 10;
        }
        if (rev == n && sum % 2 == 0)
            System.out.println(n + " is an EvenPal number");
        else
            System.out.println(n + " is not an EvenPal number");
    }
}
```
Sample runs: `121 is an EvenPal number`; `131 is not an EvenPal number` (sum 5 is odd).

**2024 specimen Q2(v).** The loop executes **5 times** and **returns 15**:

- Round 1: ++x gives 3; y -= x++ gives y = 47; x becomes 4.
- Round 2: ++x gives 5; y = 42; x = 6.
- Round 3: ++x gives 7; y = 35; x = 8.
- Round 4: ++x gives 9; y = 26; x = 10.
- Round 5: ++x gives 11; y = 15; x = 12, and 12 <= 10 is false.

*(Worked answer.)*

**2024 specimen Q2(vii).** **break** and **continue** (also return). *(Worked answer.)*

**2024 specimen Q7.**
```java
import java.util.*;
class Duck
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a 3 digit number: ");
        int n = sc.nextInt();
        if (n < 100 || n > 999)
            System.out.println("Invalid");
        else
        {
            int num = n;
            boolean hasZero = false;
            while (num > 0)
            {
                if (num % 10 == 0)
                {
                    hasZero = true;
                    break;              // one zero is enough
                }
                num = num / 10;
            }
            if (hasZero)
                System.out.println("Duck number");
            else
                System.out.println("Not a duck number");
        }
    }
}
```
Sample runs: 2083 → **Invalid** (not a 3-digit number); 103 → **Duck number**; 456 → Not a duck number. *(Worked answer.)*

**2023 Q1(vii).** **(b) infinite** — i takes 5, 3, 1, −1 … and never equals 0.

**2023 Q2(iii).** An equivalent for loop that keeps the same order (decrease, then print):
```java
for (int x = 10; x >= 1; )
{
    x--;
    System.out.print(x);       // 9876543210
}
```
(The scheme's `for (int x = 10; x >= 1; x--) System.out.print(x);` prints 10 down to 1 instead of 9 down to 0.)

**2023 Q2(vi).** Output **9** and **2** on two lines — 4279 → 42 → 0. *(Worked answer.)*

**2020 Q2(e).** An **infinite loop** is a loop whose **condition never becomes false**, so it never ends. Example: `for (int i = 1; i > 0; i++)` or `while (true) { … }` without a break. *(Worked answer.)*

**2020 Q3(e).** Only the if statement is inside the loop: k = 5, 12, 19 (3 iterations), then k = 26 ends the loop and the println runs once. Output **26**; the loop executes **3 times**. *(Worked answer.)*

**2019 Q3(d).** Output **4 2**; the loop executes **five times**.

**2019 Q9.**
```java
class Tech
{
    public static void main(String args[])
    {
        System.out.println("Four-digit tech numbers:");
        for (int x = 1000; x <= 9999; x++)
        {
            int first = x / 100;        // first half
            int second = x % 100;       // second half
            int s = first + second;
            if (s * s == x)
                System.out.println(x);
        }
    }
}
```
Output:
```
Four-digit tech numbers:
2025
3025
9801
```

**2018 Q2(b).**
- **while** is an **entry-controlled** loop; **do while** is **exit-controlled**.
- If the condition is false at the beginning, a **while** loop **never executes** (minimum 0 times); a **do while** loop **executes at least once** (minimum 1 time).

**2018 Q3(j).** Output **20**; the loop is **not executed even once**.

**2018 Q5.** Test consecutive products i × (i + 1) (the scheme also accepts checking with `(int) Math.sqrt(n)`):
```java
import java.util.*;
class Pronic
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int num = sc.nextInt();
        boolean found = false;
        for (int i = 0; i * (i + 1) <= num; i++)
        {
            if (i * (i + 1) == num)
            {
                System.out.println(num + " = " + i + " x " + (i + 1));
                found = true;
                break;
            }
        }
        if (found)
            System.out.println("Pronic number");
        else
            System.out.println("Not a pronic number");
    }
}
```
Sample runs: 42 → `42 = 6 x 7`, **Pronic number**; 40 → **Not a pronic number**.

**2017 Q2(d).** Output **12**; the loop is executed **2 times** (a = 6, then a = 12 when break runs). *(Worked answer.)*

**2017 Q3(d).**
```java
int d = 5;
for (int i = 1; i <= 5; i++)
{
    d = d * 2;
    System.out.println(d);     // 10 20 40 80 160
}
```
*(Worked answer.)*

**2017 Q3(i).** (i) The inner loop executes **3 times** in all (once when i = 3, twice when i = 4). (ii) Output — WIN printed twice, on two lines. *(Worked answer.)*

**2017 Q5.**
```java
import java.util.*;
class Spy
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int num = n, sum = 0, prod = 1;
        while (num > 0)
        {
            int d = num % 10;
            sum = sum + d;
            prod = prod * d;
            num = num / 10;
        }
        System.out.println("Sum = " + sum + ", Product = " + prod);
        if (sum == prod)
            System.out.println(n + " is a spy number");
        else
            System.out.println(n + " is not a spy number");
    }
}
```
Sample runs: 1124 → `Sum = 8, Product = 8`, **1124 is a spy number**. *(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) How many times does `for (int i = 1; i <= 100; i *= 3)` run? Give the values of i.
**Answer:** 5 times — 1, 3, 9, 27, 81.

**Q2.** (2 marks) Convert into a while loop: `for (int i = 10; i > 0; i -= 2) System.out.print(i);`
**Answer:** `int i = 10; while (i > 0) { System.out.print(i); i -= 2; }`

**Q3.** (2 marks) Is 1634 an Armstrong number? Show the working.
**Answer:** Yes — 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1 + 1296 + 81 + 256 = 1634.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 2 marks | Output and number of iterations (including empty-body loops and continue/break) | 8.2, Section 1 |
| 2 marks | Convert for ↔ while ↔ do-while | 8.2, Section 1 |
| MCQ | Entry vs exit control; infinite loop; executed once (initialisation); nested-loop picture | 8.2, 5.1 |
| 15 marks | Special-number program with digit extraction | 8.2, Section 11 |

---

## 9. MCQs with Explanations

### Loop basics (Q1–Q14)

**Q1.** A construct that repeats statements while a condition is true is a
- (a) loop
- (b) switch
- (c) class
- (d) package

**Answer:** (a) loop
**Explanation:** Also called an iterative construct.

**Q2.** Which are entry-controlled loops?
- (a) only for
- (b) for and while
- (c) for and do-while
- (d) do-while and switch

**Answer:** (b) for and while
**Explanation:** 2024 MS.

**Q3.** The exit-controlled loop in Java is
- (a) for
- (b) while
- (c) switch
- (d) do-while

**Answer:** (d) do-while
**Explanation:** The condition is tested after the body.

**Q4.** A do-while loop executes at least
- (a) zero times
- (b) twice
- (c) ten times
- (d) once

**Answer:** (d) once
**Explanation:** The body runs before the first test.

**Q5.** In a for statement, the part executed only once is the
- (a) update
- (b) condition
- (c) initialisation
- (d) body

**Answer:** (c) initialisation
**Explanation:** 2026 Improvement.

**Q6.** A while loop whose condition is false at the start runs
- (a) zero times
- (b) once
- (c) forever
- (d) twice

**Answer:** (a) zero times
**Explanation:** Entry-controlled.

**Q7.** The teacher asks for a side stretch 10 times. The construct used is
- (a) if
- (b) switch
- (c) for
- (d) if else if

**Answer:** (c) for
**Explanation:** 2025 MS.

**Q8.** A do-while loop ends with
- (a) a colon
- (b) the keyword end
- (c) a brace only
- (d) a semicolon after while (condition)

**Answer:** (d) a semicolon after while (condition)
**Explanation:** `} while (k <= 10);`

**Q9.** A loop whose condition never becomes false is
- (a) finite
- (b) nested
- (c) empty
- (d) infinite

**Answer:** (d) infinite
**Explanation:** It never ends.

**Q10.** Which is an infinite loop?
- (a) for(int i=1;i<=10;i++)
- (b) for(int i=2; i!=0; i-=3)
- (c) for(int i=5; i<=5; i++)
- (d) for(int i=1; i>=1; i--)

**Answer:** (b) for(int i=2; i!=0; i-=3)
**Explanation:** 2025 MS.

**Q11.** `for (int i = 5; i != 0; i -= 2)` is
- (a) finite
- (b) null
- (c) fixed
- (d) infinite

**Answer:** (d) infinite
**Explanation:** i is always odd (2023 MS).

**Q12.** A loop with an empty body used to waste time is a
- (a) delay loop
- (b) nested loop
- (c) switch loop
- (d) jump loop

**Answer:** (a) delay loop
**Explanation:** e.g. `for (i = 1; i <= 10000; i++);`

**Q13.** Which loop is best when the number of repetitions is not known in advance?
- (a) a fixed for loop only
- (b) nested for
- (c) switch
- (d) while

**Answer:** (d) while
**Explanation:** e.g. while the number is greater than 0.

**Q14.** Statement I: A for loop may have two counter variables. Statement II: Parts of a for statement may be left empty.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (a) Both statements are true
**Explanation:** `for (k = 1, m = 5; …)` and `for (;;)`.

### Counting iterations and outputs (Q15–Q34)

**Q15.** `for (k = 10; k >= 0; k--)` executes
- (a) 10 times
- (b) 11 times
- (c) 12 times
- (d) 0 times

**Answer:** (b) 11 times
**Explanation:** 10 down to 0.

**Q16.** The loop that executes exactly 10 times is
- (a) for (int i=11;i<=30;i+=2)
- (b) for (int i=11;i<=30;i+=3)
- (c) for (int i=11;i<20;i++)
- (d) for (int i=11;i<=21;i++)

**Answer:** (a) for (int i=11;i<=30;i+=2)
**Explanation:** 11, 13, …, 29.

**Q17.** `int p=0; for(p=4; p>0; p-=2); System.out.print(p); System.out.println(p);` displays
- (a) 42
- (b) 4200
- (c) 0 0
- (d) 00

**Answer:** (d) 00
**Explanation:** 2025 MS.

**Q18.** `int K = 1; do { K += 2; System.out.println(K); } while (K <= 6);` runs
- (a) 2 times
- (b) 6 times
- (c) 4 times
- (d) 3 times

**Answer:** (d) 3 times
**Explanation:** Prints 3, 5, 7.

**Q19.** `for (k = 10; k >= 1; k -= 3); System.out.println(k*5);` prints
- (a) 5
- (b) 50
- (c) 0
- (d) −10

**Answer:** (d) −10
**Explanation:** k ends at −2.

**Q20.** `int k = 100; while (k >= 10) { System.out.println(k); k -= 40; }` runs
- (a) 2 times
- (b) 4 times
- (c) 3 times
- (d) 1 time

**Answer:** (c) 3 times
**Explanation:** 100, 60, 20.

**Q21.** `for (x = 10; x > 20; x++) …; System.out.println(x*2);` runs the loop
- (a) zero times and prints 20
- (b) once and prints 22
- (c) ten times and prints 40
- (d) forever

**Answer:** (a) zero times and prints 20
**Explanation:** 2024 MS.

**Q22.** `int s = 0; for (int i = 1; i <= 5; i++) s += i;` gives s =
- (a) 10
- (b) 5
- (c) 15
- (d) 20

**Answer:** (c) 15
**Explanation:** 1 + 2 + 3 + 4 + 5.

**Q23.** `int i = 1; while (i < 10) i *= 2;` leaves i =
- (a) 8
- (b) 10
- (c) 16
- (d) 32

**Answer:** (c) 16
**Explanation:** 1, 2, 4, 8, 16.

**Q24.** `int x = 1; do { x++; } while (x < 1);` leaves x =
- (a) 2
- (b) 1
- (c) 0
- (d) an infinite loop

**Answer:** (a) 2
**Explanation:** The body runs once.

**Q25.** `int s = 0; for (int a = 1; a <= 10; a += 2) s += a;` gives s =
- (a) 25
- (b) 30
- (c) 55
- (d) 20

**Answer:** (a) 25
**Explanation:** 1 + 3 + 5 + 7 + 9.

**Q26.** `int f = 1; for (int a = 1; a <= 5; a++) f *= a;` gives f =
- (a) 15
- (b) 24
- (c) 5
- (d) 120

**Answer:** (d) 120
**Explanation:** 5! = 120.

**Q27.** `for (int a = 0; a < 5; a++); System.out.println("A");` prints A
- (a) five times
- (b) once
- (c) never
- (d) six times

**Answer:** (b) once
**Explanation:** The semicolon makes the loop body empty.

**Q28.** `int t = 5; while (t-- > 0);` leaves t =
- (a) 0
- (b) 5
- (c) −1
- (d) 1

**Answer:** (c) −1
**Explanation:** The last test (0 > 0) still decrements t.

**Q29.** `int m = 0; for (int a = 10; a > 0; a -= 3) m++;` gives m =
- (a) 3
- (b) 5
- (c) 10
- (d) 4

**Answer:** (d) 4
**Explanation:** 10, 7, 4, 1.

**Q30.** `int n = 4279; while (n > 0) { System.out.println(n % 10); n = n / 100; }` prints
- (a) 9 and 2
- (b) 9, 7, 2, 4
- (c) 4 and 7
- (d) 42 and 79

**Answer:** (a) 9 and 2
**Explanation:** 4279 → 42 → 0.

**Q31.** `int x=10; while(true) { System.out.println(x++ * 2); if (x%3==0) break; }` runs
- (a) once
- (b) twice
- (c) three times
- (d) forever

**Answer:** (b) twice
**Explanation:** Prints 20, 22 (2025 specimen MS).

**Q32.** The do-while `x = 10; y = 20; do { x++; y++; } while (x <= 20); System.out.println(x * y);` prints
- (a) 600
- (b) 620
- (c) 651
- (d) 682

**Answer:** (c) 651
**Explanation:** x = 21, y = 31.

**Q33.** `int x=2, y=50; do { ++x; y -= x++; } while (x <= 10);` returns y =
- (a) 15
- (b) 26
- (c) 5
- (d) 35

**Answer:** (a) 15
**Explanation:** 5 rounds: 47, 42, 35, 26, 15.

**Q34.** `int a, b; for (a=6, b=4; a<=24; a=a+6) { if (a%b==0) break; } System.out.println(a);` prints
- (a) 6
- (b) 18
- (c) 24
- (d) 12

**Answer:** (d) 12
**Explanation:** 12 % 4 == 0.

### break and continue (Q35–Q44)

**Q35.** The statement that ends a loop immediately is
- (a) continue
- (b) break
- (c) default
- (d) else

**Answer:** (b) break
**Explanation:** Control leaves the loop.

**Q36.** The statement that skips the rest of the current iteration is
- (a) break
- (b) return
- (c) continue
- (d) exit

**Answer:** (c) continue
**Explanation:** The loop goes on with the next iteration.

**Q37.** Which are jump statements?
- (a) break and continue
- (b) if and switch
- (c) for and while
- (d) case and default

**Answer:** (a) break and continue
**Explanation:** Also return.

**Q38.** `for (int a=1; a<=10; a++) { if (a%2==0) continue; System.out.print(a+" "); }` prints
- (a) 2 4 6 8 10
- (b) 1 3 5 7 9
- (c) 1 to 10
- (d) nothing

**Answer:** (b) 1 3 5 7 9
**Explanation:** Even values are skipped.

**Q39.** `for (int a = 1; a <= 10; a++) { if (a == 5) break; System.out.print(a); }` prints
- (a) 12345
- (b) 5
- (c) 1234
- (d) 678910

**Answer:** (c) 1234
**Explanation:** The loop stops at 5.

**Q40.** `int k = 0; while (k < 3) { k++; if (k == 2) continue; System.out.print(k); }` prints
- (a) 123
- (b) 12
- (c) 23
- (d) 13

**Answer:** (d) 13
**Explanation:** 2 is skipped.

**Q41.** `for (i=5; i>=1; i--) { if (i%2==1) continue; System.out.print(i+" "); }` prints
- (a) 5 3 1
- (b) 4 2
- (c) 5 4 3 2 1
- (d) nothing

**Answer:** (b) 4 2
**Explanation:** 2019 MS; the loop runs five times.

**Q42.** A break inside an inner loop
- (a) ends both loops
- (b) ends the program
- (c) ends only the inner loop
- (d) restarts the outer loop

**Answer:** (c) ends only the inner loop
**Explanation:** The outer loop continues.

**Q43.** `for (a=1;a<=3;a++) for (j=1;j<=3;j++) { if (j==2) break; System.out.print(a+""+j+" "); }` prints
- (a) 11 21 31
- (b) 11 12 13
- (c) 11 only
- (d) 11 12 21 22 31 32

**Answer:** (a) 11 21 31
**Explanation:** Each inner loop stops at j = 2.

**Q44.** `for (k = 5; k <= 20; k += 7) if (k % 6 == 0) continue; System.out.println(k);` prints
- (a) 5 12 19
- (b) 12
- (c) 19
- (d) 26

**Answer:** (d) 26
**Explanation:** The println is outside the loop (2020 Q3(e)).

### Loop conversion (Q45–Q52)

**Q45.** The do-while form of `for (k=1, m=5; k<=10; k++, m++) System.out.println(k*m);` puts the update
- (a) before the do
- (b) after the while
- (c) inside the body after the print
- (d) in the condition

**Answer:** (c) inside the body after the print
**Explanation:** Same order as the for loop.

**Q46.** Converting `do { x--; System.out.print(x); } while (x >= 1);` (x = 10) to a for loop must print
- (a) 10987654321
- (b) nothing
- (c) 1 to 10
- (d) 9876543210

**Answer:** (d) 9876543210
**Explanation:** The decrement comes before the print.

**Q47.** Converting a while loop to a for loop moves the initialisation into
- (a) the body
- (b) the condition
- (c) the update
- (d) the first part of for( ; ; )

**Answer:** (d) the first part of for( ; ; )
**Explanation:** for (init; condition; update).

**Q48.** `for (int i = 1, d = 5; i <= 5; i++) { d = d * 2; System.out.println(d); }` prints
- (a) 5 10 15 20 25
- (b) 2 4 6 8 10
- (c) 10 20 40 80 160
- (d) 10 20 30 40 50

**Answer:** (c) 10 20 40 80 160
**Explanation:** d doubles each time.

**Q49.** A do-while loop and a while loop give the same output whenever
- (a) the condition is true at the start
- (b) the condition is false at the start
- (c) never
- (d) the body is empty

**Answer:** (a) the condition is true at the start
**Explanation:** They differ only when the first test is false.

**Q50.** The exit-controlled version of `for (a=10, b=1; a>=1; a-=2) { b+=a; b++; }` prints b =
- (a) 30
- (b) 36
- (c) 31
- (d) 25

**Answer:** (b) 36
**Explanation:** 2025 MS.

**Q51.** `int a = 5, b; for (b = 10; b > 0; b -= 2) { } System.out.println(a * b);` prints
- (a) 0
- (b) 50
- (c) 10
- (d) 5

**Answer:** (a) 0
**Explanation:** b ends at 0.

**Q52.** Statement I: Every for loop can be written as a while loop. Statement II: A do-while always gives the same output as a while.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (c) Statement I is true, Statement II is false
**Explanation:** They differ when the condition starts false.

### Nested loops and patterns (Q53–Q62)

**Q53.** The earth spinning 365 times in one revolution round the sun shows a
- (a) nested loop
- (b) condition
- (c) array
- (d) while loop

**Answer:** (a) nested loop
**Explanation:** 2026 board MCQ.

**Q54.** A clock is an example of nested loops because
- (a) the hands never move
- (b) the minute hand completes 60 positions for each hour
- (c) the hour hand is faster
- (d) it is round

**Answer:** (b) the minute hand completes 60 positions for each hour
**Explanation:** 2025 MS.

**Q55.** If the outer loop runs 3 times and the inner loop 4 times, the inner body runs
- (a) 7 times
- (b) 4 times
- (c) 12 times
- (d) 3 times

**Answer:** (c) 12 times
**Explanation:** 3 × 4.

**Q56.** `for (a=1;a<=3;a++) for (j=1;j<=a;j++) c++;` (c = 0) gives c =
- (a) 3
- (b) 9
- (c) 4
- (d) 6

**Answer:** (d) 6
**Explanation:** 1 + 2 + 3.

**Q57.** In `for (i=3;i<=4;i++) for (j=2;j<i;j++) …`, the inner loop runs in all
- (a) 2 times
- (b) 3 times
- (c) 4 times
- (d) 5 times

**Answer:** (b) 3 times
**Explanation:** Once for i = 3, twice for i = 4 (2017).

**Q58.** To print a right-angled triangle of stars, the inner loop runs
- (a) from 1 to i
- (b) from 1 to 5 always
- (c) once
- (d) from i to 1 only

**Answer:** (a) from 1 to i
**Explanation:** Row i has i stars.

**Q59.** A rectangular pattern of 4 rows and 5 columns needs the inner loop to run
- (a) 4 times
- (b) i times
- (c) 5 times
- (d) 20 times

**Answer:** (c) 5 times
**Explanation:** Once per column.

**Q60.** To start each row of a pattern on a new line, use
- (a) System.out.print() after the inner loop
- (b) System.out.println() after the inner loop
- (c) break
- (d) continue

**Answer:** (b) System.out.println() after the inner loop
**Explanation:** Inside the outer loop.

**Q61.** An inverted triangle 1 2 3 4 / 1 2 3 / 1 2 / 1 needs the outer loop
- (a) for (i = 1; i <= 4; i++)
- (b) for (;;)
- (c) for (i = 0; i < 1; i++)
- (d) for (i = 4; i >= 1; i--)

**Answer:** (d) for (i = 4; i >= 1; i--)
**Explanation:** The row length decreases.

**Q62.** Which nested loops are NOT in the ICSE syllabus?
- (a) nested for
- (b) nested while and nested do-while
- (c) a for inside a for
- (d) loops for patterns

**Answer:** (b) nested while and nested do-while
**Explanation:** Only nested for is required.

### Digits and series (Q63–Q76)

**Q63.** The last digit of n is given by
- (a) n / 10
- (b) n * 10
- (c) n % 10
- (d) n - 10

**Answer:** (c) n % 10
**Explanation:** The remainder after dividing by 10.

**Q64.** The statement that removes the last digit of n is
- (a) n = n % 10;
- (b) n = n / 10;
- (c) n = n * 10;
- (d) n = n - 1;

**Answer:** (b) n = n / 10;
**Explanation:** Integer division drops it.

**Q65.** `int n = 12345, c = 0; while (n > 0) { n /= 10; c++; }` gives c =
- (a) 4
- (b) 15
- (c) 5
- (d) 1

**Answer:** (c) 5
**Explanation:** It counts the digits.

**Q66.** Reversing 470 with `rev = rev * 10 + n % 10` gives
- (a) 74
- (b) 470
- (c) 740
- (d) 47

**Answer:** (a) 74
**Explanation:** The leading zero disappears (074).

**Q67.** A number equal to its reverse is a
- (a) spy number
- (b) palindrome number
- (c) pronic number
- (d) duck number

**Answer:** (b) palindrome number
**Explanation:** e.g. 121.

**Q68.** 1124 is a spy number because
- (a) it is even
- (b) it has four digits
- (c) the sum of its digits equals the product of its digits
- (d) it is a palindrome

**Answer:** (c) the sum of its digits equals the product of its digits
**Explanation:** 8 = 8.

**Q69.** 42 is a pronic number because
- (a) 42 = 6 × 7
- (b) 4 + 2 = 6
- (c) it is even
- (d) 42 = 2 × 21

**Answer:** (a) 42 = 6 × 7
**Explanation:** Product of two consecutive integers.

**Q70.** The four-digit tech numbers are
- (a) 1001, 2002, 3003
- (b) 2025, 3025, 9801
- (c) 1634, 8208, 9474
- (d) 1124, 1412, 2114

**Answer:** (b) 2025, 3025, 9801
**Explanation:** e.g. (30 + 25)² = 3025.

**Q71.** 153 is an Armstrong number because
- (a) 1 + 5 + 3 = 9
- (b) 1 × 5 × 3 = 15
- (c) it is odd
- (d) 1³ + 5³ + 3³ = 153

**Answer:** (d) 1³ + 5³ + 3³ = 153
**Explanation:** Each digit raised to the number of digits.

**Q72.** A duck number (3 digits) is one that
- (a) contains a zero
- (b) ends in 7
- (c) is a palindrome
- (d) is prime

**Answer:** (a) contains a zero
**Explanation:** e.g. 103 (2024 specimen).

**Q73.** In a series 1 + 1/2 + 1/3 + … + 1/n, the term should be written as
- (a) 1 / i
- (b) 1.0 / i
- (c) i / 1
- (d) i * i

**Answer:** (b) 1.0 / i
**Explanation:** 1 / i is integer division (0 for i > 1).

**Q74.** The series 1, 11, 111, 1111 is generated by
- (a) term = term + 1;
- (b) term = term * 11;
- (c) term = term * 10 + 1;
- (d) term = term / 10;

**Answer:** (c) term = term * 10 + 1;
**Explanation:** 0 → 1 → 11 → 111.

**Q75.** The correct order to return the factorial of 4 is
- (a) 1, 2, 3, 4
- (b) 3, 1, 4, 2
- (c) 3, 1, 2, 4
- (d) 1, 3, 2, 4

**Answer:** (b) 3, 1, 4, 2
**Explanation:** Declare, loop, multiply, return (2025 MS).

**Q76.** `int p = 1; for (int a = 1; a <= 4; a++) p *= 2;` gives p =
- (a) 8
- (b) 16
- (c) 4
- (d) 32

**Answer:** (b) 16
**Explanation:** 2⁴.

---

## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** Distinguish between entry-controlled and exit-controlled loops.
**Answer:** An entry-controlled loop (for, while) tests the condition before the body and may run zero times.
An exit-controlled loop (do-while) tests it after the body and runs at least once.

**Q2.** Name the four parts of a loop.
**Answer:** Initialisation and the test condition.
The body and the update of the control variable.

**Q3.** Distinguish between break and continue.
**Answer:** break ends the loop immediately.
continue skips the rest of the current iteration and goes to the next one.

**Q4.** What is an infinite loop? Give an example.
**Answer:** A loop whose condition never becomes false, so it never ends.
`for (int i = 1; i > 0; i++)` or `while (true) { … }` with no break.

**Q5.** What is a delay loop?
**Answer:** A loop with an empty body that only counts, used to pass time.
`for (int i = 1; i <= 100000; i++);`

**Q6.** Distinguish between a finite and an infinite loop.
**Answer:** A finite loop stops after a fixed number of iterations.
An infinite loop never stops because its condition stays true.

**Q7.** What is a nested loop? How many times does the inner body run?
**Answer:** A loop placed inside another loop.
If the outer loop runs m times and the inner n times, the inner body runs m × n times.

**Q8.** When would you prefer a while loop to a for loop?
**Answer:** When the number of repetitions is not known in advance.
e.g. extracting digits while the number is greater than 0.

**Q9.** Write two variations of the for loop.
**Answer:** Two counters: `for (k = 1, m = 5; k <= 10; k++, m++)`.
Missing parts: `for (; i <= 10; )` or an empty body `for (…);`.

**Q10.** Why do digit programs work on a copy of the number?
**Answer:** The loop destroys the number (n = n / 10).
The original is needed at the end, e.g. to compare with the reverse.

**Q11.** State the use of `n % 10` and `n / 10` in number programs.
**Answer:** n % 10 gives the last digit.
n / 10 removes the last digit.

**Q12.** Why is `s += 1 / i;` wrong for 1 + 1/2 + 1/3 + …? Correct it.
**Answer:** 1 / i is integer division, which is 0 for i > 1.
Write `s += 1.0 / i;`

### Output and error questions (2 marks each)

**Q13.** Give the output and the number of iterations: `int i = 1; while (i < 10) i *= 2; System.out.println(i);`
**Answer:** `16`; the loop runs 4 times.
i takes 1, 2, 4, 8, then becomes 16.

**Q14.** Give the output: `int s = 0; for (int a = 1; a <= 10; a += 2) s += a; System.out.println(s);`
**Answer:** `25`
1 + 3 + 5 + 7 + 9.

**Q15.** Give the output: `for (int a = 0; a < 5; a++); System.out.println("A");`
**Answer:** `A` (printed once).
The semicolon gives the loop an empty body.

**Q16.** Give the output: `int k = 0; while (k < 3) { k++; if (k == 2) continue; System.out.print(k); }`
**Answer:** `13`
k = 2 is skipped by continue.

**Q17.** Give the output: `for (int a = 1; a <= 10; a++) { if (a == 5) break; System.out.print(a); }`
**Answer:** `1234`
break ends the loop when a is 5.

**Q18.** Give the value of t: `int t = 5; while (t-- > 0);`
**Answer:** `-1`
The final test 0 > 0 is false but still decrements t.

**Q19.** How many stars does this print? `for (int i = 1; i <= 3; i++) for (int j = 1; j <= i; j++) System.out.print("*");`
**Answer:** 6
1 + 2 + 3 stars.

**Q20.** Find the error: `int i = 1; while (i <= 5) System.out.println(i);`
**Answer:** i is never updated, so the loop is infinite (logical error).
Add `i++` inside braces: `while (i <= 5) { System.out.println(i); i++; }`

**Q21.** Give the output: `int rev = 0, n = 470; while (n > 0) { rev = rev * 10 + n % 10; n /= 10; } System.out.println(rev);`
**Answer:** `74`
The reverse 074 is stored as 74.

**Q22.** Give the output: `int x = 1; do { x++; } while (x < 1); System.out.println(x);`
**Answer:** `2`
A do-while runs once even though the condition is false.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; a sample run follows each.*

### Section B programs (15 marks each)

**Q1.** Write a program to accept a number and check whether it is an Armstrong number (the sum of each digit raised to the power of the number of digits equals the number), e.g. 153 = 1³ + 5³ + 3³ and 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴.
**Answer:**
```java
import java.util.*;
class Armstrong
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int digits = 0;
        for (int t = n; t > 0; t = t / 10)
            digits++;                       // count the digits
        int sum = 0;
        for (int t = n; t > 0; t = t / 10)
            sum = sum + (int) Math.pow(t % 10, digits);
        if (sum == n)
            System.out.println(n + " is an Armstrong number");
        else
            System.out.println(n + " is not an Armstrong number");
    }
}
```
Sample runs:
```
Enter a number: 153
153 is an Armstrong number

Enter a number: 1634
1634 is an Armstrong number

Enter a number: 154
154 is not an Armstrong number
```

**Q2.** Write a program to accept a number and check whether it is prime (exactly two factors). Also print all prime numbers up to 50 using nested loops.
**Answer:**
```java
import java.util.*;
class Primes
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int factors = 0;
        for (int i = 1; i <= n; i++)
            if (n % i == 0)
                factors++;
        System.out.println(n + (factors == 2 ? " is prime" : " is not prime"));
        System.out.print("Prime numbers up to 50: ");
        for (int x = 2; x <= 50; x++)       // nested loops
        {
            int f = 0;
            for (int i = 1; i <= x; i++)
                if (x % i == 0)
                    f++;
            if (f == 2)
                System.out.print(x + " ");
        }
        System.out.println();
    }
}
```
Sample run:
```
Enter a number: 29
29 is prime
Prime numbers up to 50: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

**Q3.** Write a program to print the first n terms of the Fibonacci series 0, 1, 1, 2, 3, 5, 8, …
**Answer:**
```java
import java.util.*;
class Fibonacci
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("How many terms? ");
        int n = sc.nextInt();
        int a = 0, b = 1;
        for (int i = 1; i <= n; i++)
        {
            System.out.print(a + " ");
            int c = a + b;          // next term
            a = b;
            b = c;
        }
        System.out.println();
    }
}
```
Sample run:
```
How many terms? 10
0 1 1 2 3 5 8 13 21 34
```

**Q4.** Write a program to accept n and x and print the sums of the series (a) 1 + 1/2 + 1/3 + … + 1/n (b) x + x²/2 + x³/3 + … + xⁿ/n.
**Answer:**
```java
import java.util.*;
class Series
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n and x: ");
        int n = sc.nextInt();
        double x = sc.nextDouble();
        double s1 = 0, s2 = 0;
        for (int i = 1; i <= n; i++)
        {
            s1 = s1 + 1.0 / i;                  // 1 + 1/2 + 1/3 + ... + 1/n
            s2 = s2 + Math.pow(x, i) / i;       // x + x^2/2 + ... + x^n/n
        }
        System.out.println("1 + 1/2 + ... + 1/" + n + " = " + s1);
        System.out.println("x + x^2/2 + ... + x^n/n = " + s2);
    }
}
```
Sample run:
```
Enter n and x: 4 2
1 + 1/2 + ... + 1/4 = 2.083333333333333
x + x^2/2 + ... + x^n/n = 10.666666666666666
```

**Q5.** Write a program to accept the number of rows n and print, using nested for loops: (a) a right-angled triangle of stars (b) an inverted number triangle 1 2 … n down to 1 (c) a rectangle of n rows and 5 columns showing the row number.
**Answer:**
```java
import java.util.*;
class Patterns
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++)            // pattern 1: right triangle of *
        {
            for (int j = 1; j <= i; j++)
                System.out.print("* ");
            System.out.println();
        }
        System.out.println();
        for (int i = n; i >= 1; i--)            // pattern 2: inverted numbers
        {
            for (int j = 1; j <= i; j++)
                System.out.print(j + " ");
            System.out.println();
        }
        System.out.println();
        for (int i = 1; i <= n; i++)            // pattern 3: rectangle of row numbers
        {
            for (int j = 1; j <= 5; j++)
                System.out.print(i + " ");
            System.out.println();
        }
    }
}
```
Sample run (n = 4):
```
*
* *
* * *
* * * *

1 2 3 4
1 2 3
1 2
1

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
```

**Q6.** Write a program to accept two positive integers and print their GCD (by Euclid's method, using a while loop) and their LCM (a × b ÷ GCD).
**Answer:**
```java
import java.util.*;
class GcdLcm
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two positive integers: ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int x = a, y = b;
        while (y != 0)                  // Euclid's method
        {
            int r = x % y;
            x = y;
            y = r;
        }
        int gcd = x;
        int lcm = a * b / gcd;
        System.out.println("GCD = " + gcd);
        System.out.println("LCM = " + lcm);
    }
}
```
Sample run:
```
Enter two positive integers: 12 18
GCD = 6
LCM = 36
```

---

## 12. Competency / Application Questions

**Q1. (Savings plan)** Asha saves ₹10 in week 1 and doubles the amount every week. Write a loop to find the week in which her weekly saving first exceeds ₹1000.
**Model answer:** `int w = 1, amt = 10; while (amt <= 1000) { amt *= 2; w++; } System.out.println(w);` — prints 8 (₹1280).

**Q2. (Attendance roll)** A teacher marks 40 students. Which loop is best, and why?
**Model answer:** A for loop — the number of repetitions (40) is known in advance.

**Q3. (PIN check)** An app must ask for a PIN at least once and keep asking while it is wrong. Which loop fits?
**Model answer:** A do-while loop — it runs the body (asking) at least once before testing.

**Q4. (Bug hunt)** `for (int i = 1; i <= 10; i++); { sum += i; }` does not compile. Why, and how should it be fixed?
**Model answer:** The semicolon ends the loop, so the block runs once after it, where i is out of scope. Remove the semicolon.

**Q5. (Seating plan)** A hall has 6 rows of 8 seats. Write nested loops to print seat numbers like R1S1 … R6S8.
**Model answer:** `for (int r = 1; r <= 6; r++) { for (int s = 1; s <= 8; s++) System.out.print("R" + r + "S" + s + " "); System.out.println(); }`

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** A do-while loop executes at least once.
**R:** The condition is tested after the body.
**Answer:** (c)
**Explanation:** Exit control.

**Q2.**
**A:** `for (int i = 2; i != 0; i -= 3)` is a finite loop.
**R:** i decreases by 3 each time.
**Answer:** (b)
**Explanation:** i is never 0, so it is infinite; R is true.

**Q3.**
**A:** continue does not end the loop.
**R:** continue only skips the rest of the current iteration.
**Answer:** (c)
**Explanation:** The loop goes on with the next iteration; break is the statement that ends it.

**Q4.**
**A:** A clock is a real-life example of nested loops.
**R:** The minute hand completes 60 positions for each position of the hour hand.
**Answer:** (c)
**Explanation:** 2025 MS.

**Q5.**
**A:** `for (x = 10; x > 20; x++)` executes zero times.
**R:** for is an entry-controlled loop.
**Answer:** (c)
**Explanation:** The condition is false at the start.

**Q6.**
**A:** 1634 is an Armstrong number.
**R:** while is an entry-controlled loop.
**Answer:** (d)
**Explanation:** Both true; unrelated.

**Q7.**
**A:** In digit programs, n % 10 gives the last digit.
**R:** The remainder on division by 10 is the units digit.
**Answer:** (c)
**Explanation:** e.g. 4279 % 10 = 9.

**Q8.**
**A:** `s += 1 / i;` correctly adds 1/2, 1/3 … to s.
**R:** Integer division drops the fractional part.
**Answer:** (b)
**Explanation:** 1 / i is 0 for i > 1; R is true.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The digit detective

> `int n = 1124, num = n, s = 0, p = 1; while (num > 0) { int d = num % 10; s += d; p *= d; num /= 10; }`

**(i)** How many times does the loop run?
**Answer:** 4.

**(ii)** What is s?
**Answer:** 8.

**(iii)** What is p?
**Answer:** 8.

**(iv)** What kind of number is 1124?
**Answer:** A spy number.

### Case 2 — The empty loop

> `int k; for (k = 10; k >= 1; k -= 3); System.out.println(k * 5);`

**(i)** What makes the loop body empty?
**Answer:** The semicolon after the for statement.

**(ii)** List the values of k for which the condition is true.
**Answer:** 10, 7, 4, 1.

**(iii)** What is the final value of k?
**Answer:** −2.

**(iv)** What is printed?
**Answer:** −10.

### Case 3 — The star triangle

> `for (int i = 1; i <= 4; i++) { for (int j = 1; j <= i; j++) System.out.print("* "); System.out.println(); }`

**(i)** How many rows are printed?
**Answer:** 4.

**(ii)** How many stars are in row 3?
**Answer:** 3.

**(iii)** How many stars are printed in all?
**Answer:** 10.

**(iv)** What does println() do here?
**Answer:** Moves to the next line after each row.

---

## 15. Revision Notes

### Chapter at a glance
- Loops repeat statements: initialisation, condition, body, update.
- for, while — entry-controlled (0 or more times); do-while — exit-controlled (at least once; ends with `;`).
- for — initialisation once; variations: multiple counters, missing parts, steps, empty body (delay), infinite.
- Conversions keep the same logic and order.
- break ends a loop; continue skips an iteration; return leaves a method.
- Nested for: inner completes for each outer value; m × n; rectangles (inner fixed) and triangles (inner up to i).
- Series: accumulator; use 1.0 for fractions; Math.pow for powers.
- Digits: d = n % 10; n = n / 10; work on a copy; count, sum, product, reverse, largest/smallest, first digit.
- Special numbers: palindrome, spy, Armstrong, pronic, duck, tech, EvenPal, Mark, buzz, SUPERSPY, prime.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| Forgetting the update in a while loop | The loop becomes infinite. |
| A semicolon after `for (…)` by accident | The body becomes empty. |
| Starting a product at 0 | Start prod (or factorial) at 1. |
| Losing n during digit extraction | Copy n first. |
| `1 / i` in a series | Use `1.0 / i`. |
| Counting do-while as zero runs | It always runs at least once. |
| Changing statement order when converting loops | Keep decrease-then-print order. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 4: Revision IV**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** Exit-controlled loop:
(a) for (b) while (c) do-while (d) switch

**2.** Part of a for executed once:
(a) update (b) condition (c) initialisation (d) body

**3.** `for (k = 10; k >= 0; k--)` runs:
(a) 10 (b) 11 (c) 12 (d) 0 times

**4.** Infinite loop:
(a) for(i=1;i<=10;i++) (b) for(i=2;i!=0;i-=3) (c) for(i=5;i<=5;i++) (d) for(i=1;i>=1;i--)

**5.** `int p=0; for(p=4;p>0;p-=2); System.out.print(p); System.out.println(p);` shows:
(a) 42 (b) 4200 (c) 0 0 (d) 00

**6.** Skips the rest of an iteration:
(a) break (b) continue (c) default (d) exit

**7.** Last digit of n:
(a) n / 10 (b) n % 10 (c) n * 10 (d) n - 10

**8.** Earth's rotations within a revolution:
(a) array (b) condition (c) nested loop (d) while loop

**9.** Statement I: A while loop may run zero times. Statement II: A do-while may run zero times.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

**10.** Four-digit tech numbers include:
(a) 3025 (b) 1634 (c) 1124 (d) 121

### Part I — Short answers (5 × 2 = 10)

**11.** Differentiate while and do-while. [2]

**12.** Give the output and the iterations: `int k = 100; while (k >= 10) { System.out.println(k); k -= 40; }` [2]

**13.** Convert into a do-while: `for (k = 1, m = 5; k <= 10; k++, m++) System.out.println(k*m);` [2]

**14.** Give the output: `for (int a = 1; a <= 10; a++) { if (a % 2 == 0) continue; System.out.print(a + " "); }` [2]

**15.** Give the output: `int K = 1; do { K += 2; System.out.println(K); } while (K <= 6);` [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** (i) Explain break and continue with examples. [4]
(ii) Write a program to check a spy number. [6]

**17.** (i) Give the output and iterations: `for (k = 5; k <= 20; k += 7) if (k % 6 == 0) continue; System.out.println(k);` [4]
(ii) Write a program to check an EvenPal number. [6]

**18.** (i) Write nested loops for the pattern 1 / 1 2 / 1 2 3 / 1 2 3 4. [4]
(ii) Write a program to print all four-digit tech numbers. [6]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | c | c | d | c | b |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | 4 | 8 | 8 | Spy number |
| 2 | The semicolon | 10, 7, 4, 1 | −2 | −10 |
| 3 | 4 | 3 | 10 | Moves to the next line |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | c | c | b | b | d | b | b | c | c | a |

**Part I, Q11–15 (2 marks each)**

**11.** Entry vs exit control (1); 0 vs at least 1 run (1).
**12.** 100, 60, 20 (1); 3 times (1).
**13.** Initialisation before do (1); print and updates in the body, `while (k <= 10);` (1).
**14.** `1 3 5 7 9` (2).
**15.** 3, 5, 7 (2).

**Part II (10 marks each)**

**16.** (i) Two definitions with examples (4). (ii) Input (1), digit loop with sum and product (3), comparison and output (2).

**17.** (i) Output 26 (2); 3 times (2). (ii) Input (1), reverse and sum in a loop (3), both conditions and output (2).

**18.** (i) Outer loop (1), inner loop to i (2), println (1). (ii) Loop 1000–9999 (2), halves (2), square check and print (2).
