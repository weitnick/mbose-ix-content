# Revision III — Conditional Constructs in Java

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 3 |
| Title | Revision III — Conditional Constructs in Java |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 1. Revision of Class IX syllabus: (vii) Conditional constructs in Java |
| Exam weightage | Section A regularly asks to **convert** if-else ↔ ternary, if-else-if ↔ switch, and nested if ↔ logical operators (2 marks each), plus MCQs on **fall through**, **break**, **default** and the **data types allowed in switch**. Section B often has a **menu-driven program** using switch (15 marks), and almost every program uses if-else. |
| Syllabus scope | if, if-else, if-else-if ladder, nested if; switch-case with break and default, fall through; the ternary (conditional) operator; menu-driven programs; System.exit(0) to terminate a program. |
| In short | A revision of how Java programs make decisions with if, if-else and switch, including menu-driven programs. |

> **Note on the text:** CISCE does not prescribe a textbook for ICSE Computer Applications. This chapter is written to the ICSE 2027 syllabus in its own words; its exam questions are the CISCE board papers of 2017–2026 and the specimen papers of 2024 and 2025, answered from CISCE's marking schemes wherever one has been published. **Every program and output in this chapter was compiled and run (Java 21).**
>
> **Exam note:** A **switch** checks only **equality** with **constant case labels**; it works with **int, char, String, byte and short** — **not double, float, long or boolean** (Java rejects a `boolean` or `double` selector). Without **break**, control **falls through** to the next case. In a ternary, both branches must be **values**: write `System.out.println(x > y ? "Precious" : "Priceless");`, not `x > y ? System.out.println(…) : …`. When converting `if (code == 'g') … else if (code == 'G') …` with the same action, join the conditions with the OR operator in **one if**.

---

## 1. Complete Lesson

### Why conditional constructs?

Statements normally run one after another (**sequential flow**). A **conditional (decision-making) construct** lets a program **choose** which statements to run, depending on whether a condition is **true or false**. Conditions use **relational** (`>`, `==`, `!=` …) and **logical** (`&&`, OR, `!`) operators.

### The if statement

```java
if (condition)
    statement;            // runs only when the condition is true
```
Use braces `{ }` when more than one statement depends on the condition.

### The if-else statement

```java
if (marks >= 33)
    System.out.println("Pass");
else
    System.out.println("Fail");
```
Exactly **one** of the two blocks runs.

### The if-else-if ladder

Used to test **several conditions in order**; the **first true** condition's block runs and the rest are skipped. A final `else` handles "none of these".

```java
if (per >= 90)
    grade = 'A';
else if (per >= 75)
    grade = 'B';
else if (per >= 60)
    grade = 'C';
else
    grade = 'D';
```

### Nested if

An if inside another if. It can often be rewritten with **&&**:

```java
if (x > 5)
    if (x > y)
        System.out.println(x + y);
// same as
if (x > 5 && x > y)
    System.out.println(x + y);
```

**Dangling else:** an `else` belongs to the **nearest** unmatched `if`. Use braces to make the intended pairing clear.

**Example 1.** *(ICSE 2025 specimen, Q2(i))* Rewrite using a single if statement:
```java
if (code == 'g')
    System.out.println("GREEN");
else if (code == 'G')
    System.out.println("GREEN");
```
**Solution:**
```java
if (code == 'g' || code == 'G')
    System.out.println("GREEN");
```

### The ternary (conditional) operator

`variable = condition ? value1 : value2;` — if the condition is true the result is value1, otherwise value2. It is a compact form of a simple if-else that **produces a value**.

```java
tax = basic > 1200 ? 200 : 100;          // basic = 1500 gives tax = 200
String idStatus = age > 10 ? "Eligible" : "Not eligible";
int big = p > q ? (p > r ? p : r) : (q > r ? q : r);   // nested ternary: largest of three
```

**Example 2.** *(ICSE 2018, Q3(i))* Rewrite using the ternary operator:
```java
if (bill > 10000)
    discount = bill * 10.0/100;
else
    discount = bill * 5.0/100;
```
**Solution:** `discount = bill > 10000 ? bill * 10.0/100 : bill * 5.0/100;`

### The switch-case statement

```java
switch (expression)
{
    case constant1:
        statements;
        break;
    case constant2:
        statements;
        break;
    default:
        statements;      // runs when no case matches
}
```

**Rules**
1. The expression and the case labels must be of type **int, char, String, byte or short** (or their wrapper classes). **double, float, long and boolean are not allowed.**
2. Case labels must be **constants** and **unique**; only **equality** is checked.
3. **break** ends the switch. If it is missing, control **falls through** into the next case (the **fall-through** condition).
4. **default** is optional and can appear anywhere; it runs when no case matches.
5. Several case labels can share one block: `case 'c': case 'C': …`

**Fall through in action** (n = 10):
```java
switch (n)
{
    case 10: System.out.println(n * 2);   // prints 20
    case 4:  System.out.println(n * 4);   // falls through: prints 40
             break;
    default: System.out.println(n);
}
```

**Example 3.** *(ICSE 2018, Q3(f))* Convert into switch case:
```java
if (var == 1) System.out.println("good");
else if (var == 2) System.out.println("better");
else if (var == 3) System.out.println("best");
else System.out.println("invalid");
```
**Solution:**
```java
switch (var)
{
    case 1: System.out.println("good");
            break;
    case 2: System.out.println("better");
            break;
    case 3: System.out.println("best");
            break;
    default: System.out.println("invalid");
}
```

### if-else-if versus switch

| if-else-if | switch-case |
|---|---|
| Can test **ranges** and any **relational/logical** condition | Tests **only equality** with constant values |
| Works with **any data type** (including double, boolean, objects) | Works only with **int, char, String, byte, short** (and wrappers) |
| Each condition is evaluated in turn | Jumps directly to the matching case |
| No fall through | Falls through without break |

### Menu-driven programs and System.exit(0)

A **menu-driven program** shows a list of choices, reads the user's choice and performs the selected task — usually with **switch**, using **default** for an invalid choice.

`System.exit(0);` **terminates the whole program immediately** from any point (for example, an "Exit" option of a menu).

```java
System.out.println("1. Area of a circle");
System.out.println("2. Area of a square");
System.out.println("4. Exit");
int ch = sc.nextInt();
switch (ch)
{
    case 1: ... break;
    case 2: ... break;
    case 4: System.exit(0);
    default: System.out.println("Wrong choice");
}
```

**Example 4.** *(ICSE 2023, Q1(vi))* The absence of which statement leads to fall through situation in switch case statement? (a) continue (b) break (c) return (d) System.exit(0)
**Solution:** **(b) break.**

### Summary of the chapter

- **if** — run when true; **if-else** — one of two; **if-else-if ladder** — first true condition wins; **nested if** — if inside if (often `&&`).
- **Ternary** `c ? v1 : v2` — a compact if-else that gives a value.
- **switch** — equality only; int, char, String, byte, short; constant, unique labels; **break** prevents fall through; **default** for no match; shared labels.
- if-else-if vs switch — ranges and any type vs equality and limited types.
- **Menu-driven programs** use switch; **System.exit(0)** ends the program.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Write if, if-else, if-else-if and nested if statements.
2. Combine conditions with logical operators and replace nested ifs.
3. Use the ternary operator and convert between it and if-else.
4. Write switch statements with break, default and shared case labels, and predict fall-through output.
5. State the data types allowed in switch and convert between if-else-if and switch.
6. Write menu-driven programs and use System.exit(0).

---

## 3. Detailed Section Explanations

### Section 1 — Conditions are true or false
Every decision rests on a boolean condition. Relational operators make simple conditions; `&&` and OR join them.

### Section 2 — First true wins
In an if-else-if ladder, order matters: test the highest range first (90, then 75, then 60), or a high score will be caught by a lower test.

### Section 3 — switch needs break
Fall through is useful for shared actions (`case 'c': case 'C':`) but a bug when break is forgotten.

### Section 4 — Ternary gives a value
Use it when choosing between two values; use if-else when choosing between two actions.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Conditional construct | A statement that chooses what to run based on a condition. |
| Condition | A boolean expression that is true or false. |
| if-else-if ladder | A chain of conditions where the first true one runs. |
| Nested if | An if statement inside another if. |
| Dangling else | An else that pairs with the nearest unmatched if. |
| Ternary operator | The conditional operator ?: that selects one of two values. |
| switch-case | A multiple-branching statement that matches a value against constant labels. |
| case label | A constant in a switch that is compared with the expression. |
| break | Ends a switch (or loop) immediately. |
| default | The switch branch that runs when no case matches. |
| Fall through | Execution continuing into the next case when break is missing. |
| Menu-driven program | A program that performs the task chosen from a displayed menu. |
| System.exit(0) | A method call that terminates the program. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| Missing break causes | Fall through |
| Data type not allowed in switch | double (also float, long, boolean) |
| Allowed in switch | int, char, String, byte, short |
| switch checks | Only equality |
| Construct to choose one of several ice creams | switch |
| `if (a > b && b > c)` — largest is | a |
| `tax = basic > 1200 ? 200 : 100;` with basic = 1500 | 200 |
| Ternary operator is a | conditional operator |
| `boolean x = true; switch (x)` | Error — use `int x = 1;` |
| Statement that ends the program | System.exit(0) |
| Statement that leaves a switch | break |

### 5.2 Memory aids

- **"Break the fall"** — without break, a switch falls through.
- **"Switch can't float or double-check"** — no double, float, long or boolean.
- **"Ternary returns, if-else does"** — ternary gives a value; if-else performs actions.

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- Newer Java versions add an arrow form of switch (`case 1 -> …`) that never falls through.
- A switch on a String compares with equals(), so letter case matters.
- Compilers often turn a switch with many integer cases into a jump table, which can be faster than a long ladder.

---

## 6. Person Profiles

### 6.1 George Boole (1815–1864)
An English mathematician whose algebra of true and false ("Boolean algebra") underlies every condition a program tests — Java's boolean type is named after him.

### 6.2 Edsger W. Dijkstra (1930–2002)
A Dutch computer scientist who championed structured programming — building programs from sequence, selection (if, switch) and iteration rather than jumping about with goto statements.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Programs decide** — conditions turn data into choices.
- **Choose the right tool** — ranges need if-else-if; exact menu choices suit switch.
- **Readable code is correct code** — braces and clear ordering prevent dangling-else and fall-through bugs.

### 7.2 Real-life connections
- **Meghalaya:** an electricity bill calculator applies different rates to different slabs of units — an if-else-if ladder.
- **ATMs:** "1. Withdraw 2. Deposit 3. Balance 4. Exit" is a menu-driven program.
- **Exams:** grading by percentage bands is a ladder of conditions.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section A** (40 marks) has MCQs on switch and the ternary operator and 2-mark **conversion** questions; **Section B** (60 marks, any four of six programs) often includes a **menu-driven program** with switch, and nearly every program needs if-else.

### 8.1 Graded exercises — solutions

#### Exercise 3A — Conversions

**Q1.** Rewrite with a ternary operator: `if (a > b) z = 25; else z = 35;`
**Answer:** `z = a > b ? 25 : 35;`

**Q2.** Rewrite using if-else: `int max = p > q ? p : q;`
**Answer:** `int max; if (p > q) max = p; else max = q;`

**Q3.** Combine into one if: `if (x > 0) if (x < 10) System.out.println("digit");`
**Answer:** `if (x > 0 && x < 10) System.out.println("digit");`

**Q4.** Write a switch that prints "Vowel" for the characters a, e, i, o, u and "Not a vowel" otherwise.
**Answer:** `switch (ch) { case 'a': case 'e': case 'i': case 'o': case 'u': System.out.println("Vowel"); break; default: System.out.println("Not a vowel"); }`

#### Exercise 3B — Outputs

**Q5.** Give the output when k = 3: `switch (k) { default: System.out.println("D"); case 1: System.out.println("one"); break; case 2: System.out.println("two"); }`
**Answer:** D and one on two lines — default runs (no match), then falls through into case 1 until break.

**Q6.** Give the output: `int p = 5, q = 8, r = 3; int big = p > q ? (p > r ? p : r) : (q > r ? q : r); System.out.println(big);`
**Answer:** `8`

**Q7.** What is printed when marks = 72? `if (marks >= 90) System.out.println("A"); else if (marks >= 75) System.out.println("B"); else if (marks >= 60) System.out.println("C"); else System.out.println("D");`
**Answer:** `C`

**Q8.** Give the output when s = "two": `switch (s) { case "one": System.out.println(1); break; case "two": System.out.println(2); break; default: System.out.println(0); }`
**Answer:** `2`

### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(vi) (1 mark) | Read the if program segment given below: `if (a > b) z = 25; else z = 35;` Which one of the following is the correct conversion of the if program segment to ternary? (a) `z = a > b ? 35 : 25;` (b) `z = a > b ? 25 : 35;` (c) `z = a > b : 35 ? 25;` (d) `z = a > b : 25 ? 35;` |
| ICSE 2026, Q2(iv) (2 marks) | Users must be above 10 years to open a self-operated bank account. Write this logic using a ternary operator and store the result (the eligibility message) in a String variable named idStatus and print it. |
| ICSE 2026 Improvement, Q1(viii) (1 mark) | Consider the following program segment: `if (x > y) System.out.println("Precious"); else System.out.println("Priceless");` The equivalent statement for the above program segment with ternary operators is: (a) `x>y?System.out.println("Priceless"):System.out.println("Precious");` (b) `System.out.println(x>y?"Priceless":"Precious");` (c) `x>y?System.out.println("Precious"):System.out.println("Priceless");` (d) `System.out.println(x>y?"Precious":"Priceless");` |
| ICSE 2026 Improvement, Q2(vii) (2 marks) | Convert the following program segment using the Multiple branching statement: `if (a>=1&&a<=3) System.out.println("Moderate"); else System.out.println("Tough");` |
| ICSE 2025, Q1(xi) (1 mark) | Assertion (A): In switch case break statement avoids fall through. Reason (R): break statement helps to execute only one case at a time. (a) Both (A) and (R) are true and (R) is a correct explanation of (A). (b) Both (A) and (R) are true and (R) is not a correct explanation of (A). (c) (A) is true and (R) is false. (d) (A) is false and (R) is true. |
| ICSE 2025 Improvement, Q1(ii) (1 mark) | [Picture: a menu of ice creams to choose from] Which construct can be used to get only one of the required ice creams? (a) switch construct (b) while construct (c) do.. while construct (d) for construct |
| ICSE 2025 Improvement, Q1(xiii) (1 mark) | What is the output of the following Java code? `boolean flag = false; if (flag) { System.out.println("True"); } else { System.out.println("False"); }` (a) True (b) False (c) No output (d) Compilation error |
| ICSE 2025 Improvement, Q2(iii) (2 marks) | Convert the following switch case into if else if: `switch(x) { case 'T': case 't': System.out.print("Teacher"); break; default: System.out.print("Student"); }` |
| ICSE 2025 specimen, Q1(viii) (1 mark) | Which of the following is not true with regards to a switch statement? (a) checks for an equality between the input and the case labels (b) supports floating point constants (c) break is used to exit from the switch block (d) case labels are unique |
| ICSE 2025 specimen, Q2(i) (2 marks) | Rewrite the following code using single if statement. `if(code=='g') System.out.println("GREEN"); else if(code=='G') System.out.println("GREEN");` |
| ICSE 2025 specimen, Q2(iii) (2 marks) | A student executes the following program segment and gets an error. Identify the statement which has an error, correct the same to get the output as WIN. `boolean x = true; switch(x) { case 1: System.out.println("WIN"); break; case 2: System.out.println("LOOSE"); }` |
| ICSE 2024, Q1(vii) (1 mark) | `if (a>b&&b>c)` then largest number is: (a) b (b) c (c) a (d) wrong expression |
| ICSE 2024, Q1(xii) (1 mark) | Which of the following data type cannot be used with switch case construct? (a) int (b) char (c) String (d) double |
| ICSE 2024 specimen, Q2(iii) (2 marks) | The following code segment should print "You can go out" if you have done your homework (dh) and cleaned your room (cr). However, the code has errors. Fix the code so that it compiles and runs correctly. `boolean dh = True; boolean cr = true; if (dh && cr) System.out.println("You cannot go out"); else System.out.println("You can go out");` |
| ICSE 2023, Q1(vi) (1 mark) | The absence of which statement leads to fall through situation in switch case statement? (a) continue (b) break (c) return (d) System.exit(0) |
| ICSE 2023, Q1(xvi) (1 mark) | Consider the following program segment and select the output of the same when n = 10: `switch(n) { case 10: System.out.println(n*2); case 4: System.out.println(n*4); break; default: System.out.println(n); }` (a) 20 40 (b) 10 4 (c) 20, 40 (d) 10 10 |
| ICSE 2023, Q2(v) (2 marks) | Rewrite the following code using the if-else statement: `int m = 400; double ch = (m>300) ? (m / 10.0) * 2 : (m / 20.0) - 2;` |
| ICSE 2020, Q3(g) (2 marks) | Rewrite the following program segment using logical operators: `if (x > 5) if (x > y) System.out.println(x+y);` |
| ICSE 2020, Q3(h) (2 marks) | Convert the following if else if construct into switch case: `if (ch=='c' \|\| ch=='C') System.out.print("COMPUTER"); else if (ch=='h' \|\| ch=='H') System.out.print("HINDI"); else System.out.print("PHYSICAL EDUCATION");` |
| ICSE 2020, Q3(j) (2 marks) | Rewrite the following using ternary operator: `if (n1>n2) r = true; else r = false;` |
| ICSE 2020, Q8 (15 marks) | Write a menu driven program to perform the following operations as per user's choice: (i) To print the value of c = a² + 2ab, where a varies from 1.0 to 20.0 with increment of 2.0 and b = 3.0 is a constant. (ii) To display the following pattern using for loop: A / AB / ABC / ABCD / ABCDE. Display proper message for an invalid choice. |
| ICSE 2019, Q2(a) (2 marks) | Differentiate between if else if and switch-case statements. |
| ICSE 2019, Q3(c) (2 marks) | If the value of basic = 1500, what will be the value of tax after the following statement is executed? `tax = basic>1200 ? 200 : 100;` |
| ICSE 2019, Q5 (15 marks) | Using the switch-case statement, write a menu driven program to do the following: (a) To generate and print Letters from A to Z and their Unicode (Letters, Unicode: A 65, B 66, … Z 90). (b) Display the following pattern using iteration (looping) statement: 1 / 1 2 / 1 2 3 / 1 2 3 4 / 1 2 3 4 5 |
| ICSE 2018, Q3(f) (2 marks) | Convert the following if else if construct into switch case: `if (var==1) System.out.println("good"); else if (var==2) System.out.println("better"); else if (var==3) System.out.println("best"); else System.out.println("invalid");` |
| ICSE 2018, Q3(i) (2 marks) | Rewrite the following using ternary operator: `if (bill > 10000) discount = bill * 10.0/100; else discount = bill * 5.0/100;` |
| ICSE 2018, Q8 (15 marks) | Write a menu driven program to display the pattern as per user's choice. Pattern 1: ABCDE / ABCD / ABC / AB / A. Pattern 2: B / LL / UUU / EEEE. For an incorrect option, an appropriate error message should be displayed. |
| ICSE 2017, Q6 (15 marks) | Using switch statement, write a menu driven program for the following: (i) To find and display the sum of the series S = x¹ − x² + x³ − x⁴ + x⁵ … − x²⁰ (where x = 2). (ii) To display the following series: 1 11 111 1111 11111. For an incorrect option, an appropriate error message should be displayed. |

**Solutions**

**2026 Q1(vi).** **(b) `z = a > b ? 25 : 35;`** *(Worked answer.)*

**2026 Q2(iv).**
```java
String idStatus = age > 10 ? "Eligible" : "Not eligible";
System.out.println(idStatus);
```
*(Worked answer.)*

**2026 Improvement Q1(viii).** **(d) `System.out.println(x>y?"Precious":"Priceless");`** — the ternary must produce a value (a String) that println prints; println itself returns nothing, so (a) and (c) are invalid. *(Worked answer.)*

**2026 Improvement Q2(vii).** For an integer a, the values 1, 2 and 3 share one block:
```java
switch (a)
{
    case 1:
    case 2:
    case 3: System.out.println("Moderate");
            break;
    default: System.out.println("Tough");
}
```
*(Worked answer.)*

**2025 Q1(xi).** **(a) Both (A) and (R) are true and (R) is a correct explanation of (A).**

**2025 Improvement Q1(ii).** **(a) switch construct** — exactly one of several choices is selected. *(Worked answer.)*

**2025 Improvement Q1(xiii).** **(b) False.** *(Worked answer.)*

**2025 Improvement Q2(iii).**
```java
if (x == 'T' || x == 't')
    System.out.print("Teacher");
else
    System.out.print("Student");
```
*(Worked answer.)*

**2025 specimen Q1(viii).** **(b) supports floating point constants.**

**2025 specimen Q2(i).**
```java
if (code == 'g' || code == 'G')
    System.out.println("GREEN");
```

**2025 specimen Q2(iii).** Statement with error — `boolean x = true;` (switch cannot work on a boolean, and case 1 is not a boolean). To get the required output — **`int x = 1;`**

**2024 Q1(vii).** **(c) a.**

**2024 Q1(xii).** **(d) double.**

**2024 specimen Q2(iii).** `True` must be `true` (Java is case sensitive), and the two messages are the wrong way round:
```java
boolean dh = true;
boolean cr = true;
if (dh && cr)
    System.out.println("You can go out");
else
    System.out.println("You cannot go out");
```
*(Worked answer.)*

**2023 Q1(vi).** **(b) break.**

**2023 Q1(xvi).** **(a) 20 40** — case 10 prints 20 and, with no break, falls through to case 4, which prints 40 (each on its own line). *(Worked answer.)*

**2023 Q2(v).**
```java
int m = 400;
double ch;
if (m > 300)
    ch = (m / 10.0) * 2;
else
    ch = (m / 20.0) - 2;
```
(ch becomes 80.0.)

**2020 Q3(g).** `if (x > 5 && x > y) System.out.println(x + y);` *(Worked answer.)*

**2020 Q3(h).**
```java
switch (ch)
{
    case 'c':
    case 'C': System.out.print("COMPUTER");
              break;
    case 'h':
    case 'H': System.out.print("HINDI");
              break;
    default:  System.out.print("PHYSICAL EDUCATION");
}
```
*(Worked answer.)*

**2020 Q3(j).** `r = n1 > n2 ? true : false;` (or simply `r = n1 > n2;`). *(Worked answer.)*

**2020 Q8.**
```java
import java.util.*;
class Menu2020
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("1. Value of c = a*a + 2ab");
        System.out.println("2. Pattern A, AB, ABC ...");
        System.out.print("Enter your choice: ");
        int choice = sc.nextInt();
        switch (choice)
        {
            case 1:
                double b = 3.0, c;
                for (double a = 1.0; a <= 20.0; a = a + 2.0)
                {
                    c = a * a + 2 * a * b;
                    System.out.println("a = " + a + "\tc = " + c);
                }
                break;
            case 2:
                for (char last = 'A'; last <= 'E'; last++)
                {
                    for (char ch = 'A'; ch <= last; ch++)
                        System.out.print(ch);
                    System.out.println();
                }
                break;
            default:
                System.out.println("Invalid choice");
        }
    }
}
```
Sample run (choice 1, first lines; choice 2):
```
Enter your choice: 1
a = 1.0    c = 7.0
a = 3.0    c = 27.0
...
a = 19.0    c = 475.0

Enter your choice: 2
A
AB
ABC
ABCD
ABCDE
```
*(Worked answer.)*

**2019 Q2(a).** Any two:
- **if else if** can check a **range of values**; **switch** compares **only one value** (equality).
- **if else if** can check **relational and logical expressions**; **switch** checks **only equality**.
- **if else if** supports **primitive and composite** data types; **switch** supports only **int, char, String, byte and short** (and their wrappers).

(The scheme's list also printed long; Java does not allow a long, float, double or boolean switch.)

**2019 Q3(c).** **tax = 200** — 1500 > 1200 is true.

**2019 Q5.**
```java
import java.util.*;
class Menu2019
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("1. Letters A to Z with Unicode");
        System.out.println("2. Number pattern");
        System.out.print("Enter your choice: ");
        int choice = sc.nextInt();
        switch (choice)
        {
            case 1:
                System.out.println("Letters\tUnicode");
                for (char ch = 'A'; ch <= 'Z'; ch++)
                    System.out.println(ch + "\t" + (int) ch);
                break;
            case 2:
                for (int i = 1; i <= 5; i++)
                {
                    for (int j = 1; j <= i; j++)
                        System.out.print(j + " ");
                    System.out.println();
                }
                break;
            default:
                System.out.println("Invalid choice");
        }
    }
}
```
Sample run (choice 1, first lines; choice 2):
```
Enter your choice: 1
Letters    Unicode
A    65
B    66
...
Z    90

Enter your choice: 2
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
*(Worked answer.)*

**2018 Q3(f).**
```java
switch (var)
{
    case 1: System.out.println("good");
            break;
    case 2: System.out.println("better");
            break;
    case 3: System.out.println("best");
            break;
    default: System.out.println("invalid");
}
```

**2018 Q3(i).** `discount = bill > 10000 ? bill * 10.0/100 : bill * 5.0/100;` (the scheme printed 1000 in the condition; the question uses 10000).

**2018 Q8.** Following the scheme's steps (menu, choice, switch; substring for pattern 1; nested loops for pattern 2; default message):
```java
import java.util.*;
class Pattern2018
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("1. Pattern 1 (ABCDE ... A)");
        System.out.println("2. Pattern 2 (B, LL, UUU, EEEE)");
        System.out.print("Enter your choice: ");
        int choice = sc.nextInt();
        switch (choice)
        {
            case 1:
                String s = "ABCDE";
                for (int i = s.length(); i > 0; i--)
                    System.out.println(s.substring(0, i));
                break;
            case 2:
                String w = "BLUE";
                for (int i = 0; i < w.length(); i++)
                {
                    for (int j = 0; j <= i; j++)
                        System.out.print(w.charAt(i));
                    System.out.println();
                }
                break;
            default:
                System.out.println("Incorrect option");
        }
    }
}
```
Sample runs:
```
Enter your choice: 1
ABCDE
ABCD
ABC
AB
A

Enter your choice: 2
B
LL
UUU
EEEE
```

**2017 Q6.** The series adds odd powers and subtracts even powers of 2:
```java
import java.util.*;
class Menu2017
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("1. Sum of x - x^2 + x^3 - ... - x^20 (x = 2)");
        System.out.println("2. Series 1, 11, 111, 1111, 11111");
        System.out.print("Enter your choice: ");
        int choice = sc.nextInt();
        switch (choice)
        {
            case 1:
                int x = 2;
                double s = 0;
                for (int i = 1; i <= 20; i++)
                {
                    if (i % 2 == 1)
                        s = s + Math.pow(x, i);     // odd powers are added
                    else
                        s = s - Math.pow(x, i);     // even powers are subtracted
                }
                System.out.println("Sum = " + s);
                break;
            case 2:
                int term = 0;
                for (int i = 1; i <= 5; i++)
                {
                    term = term * 10 + 1;           // 1, 11, 111 ...
                    System.out.print(term + " ");
                }
                System.out.println();
                break;
            default:
                System.out.println("Incorrect option");
        }
    }
}
```
Sample runs:
```
Enter your choice: 1
Sum = -699050.0

Enter your choice: 2
1 11 111 1111 11111
```
*(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Rewrite using switch: `if (d == 1) s = "Mon"; else if (d == 2) s = "Tue"; else s = "Other";`
**Answer:** `switch (d) { case 1: s = "Mon"; break; case 2: s = "Tue"; break; default: s = "Other"; }`

**Q2.** (2 marks) Find the largest of a, b, c with one statement using nested ternary operators.
**Answer:** `int big = a > b ? (a > c ? a : c) : (b > c ? b : c);`

**Q3.** (2 marks) Why will `switch (price)` fail if price is a double? Suggest a fix.
**Answer:** switch does not accept double; use an if-else-if ladder (or switch on an int value).

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 2 marks | Convert if-else ↔ ternary; if-else-if ↔ switch; nested if → one if with && | 8.2, 8.1 |
| MCQ | Fall through and break; data type not allowed in switch; equivalent ternary | 8.2, 5.1 |
| 2 marks | Find and correct errors (boolean switch, True, swapped messages) | 8.2 |
| 15 marks | Menu-driven program with switch and default | 8.2, Section 11 |

---

## 9. MCQs with Explanations

### if, if-else and the ladder (Q1–Q16)

**Q1.** A construct that chooses which statements to run, based on a condition, is a
- (a) conditional construct
- (b) loop
- (c) package
- (d) data type

**Answer:** (a) conditional construct
**Explanation:** Also called a decision-making construct.

**Q2.** The condition of an if statement must give a
- (a) char
- (b) boolean value
- (c) String
- (d) double

**Answer:** (b) boolean value
**Explanation:** true or false.

**Q3.** In an if-else statement
- (a) exactly one block runs
- (b) neither block runs
- (c) both blocks always run
- (d) the else block runs first

**Answer:** (a) exactly one block runs
**Explanation:** The if block when true, else when false.

**Q4.** In an if-else-if ladder, the block that runs is the one with
- (a) the last true condition
- (b) the longest condition
- (c) every true condition
- (d) the first true condition

**Answer:** (d) the first true condition
**Explanation:** The rest are skipped.

**Q5.** `if (a>b && b>c)` — the largest number is
- (a) a
- (b) b
- (c) c
- (d) wrong expression

**Answer:** (a) a
**Explanation:** 2024 MS.

**Q6.** The output of `boolean flag = false; if (flag) System.out.println("True"); else System.out.println("False");` is
- (a) True
- (b) False
- (c) no output
- (d) a compilation error

**Answer:** (b) False
**Explanation:** flag is false.

**Q7.** An if statement placed inside another if is a
- (a) ladder
- (b) switch
- (c) nested if
- (d) ternary

**Answer:** (c) nested if
**Explanation:** Can often be rewritten with &&.

**Q8.** `if (x > 5) if (x > y) System.out.println(x+y);` is equivalent to
- (a) if (x > 5 && x > y) System.out.println(x+y);
- (b) if (x > 5 || x > y) System.out.println(x+y);
- (c) if (x > y) System.out.println(x+y);
- (d) if (!(x > 5)) System.out.println(x+y);

**Answer:** (a) if (x > 5 && x > y) System.out.println(x+y);
**Explanation:** Both conditions must be true.

**Q9.** With x = 5, `if (x > 3) if (x > 10) System.out.println("A"); else System.out.println("B");` prints
- (a) A
- (b) nothing
- (c) A and B
- (d) B

**Answer:** (d) B
**Explanation:** The else pairs with the nearest if (dangling else).

**Q10.** An else always pairs with
- (a) the first if in the program
- (b) the nearest unmatched if
- (c) the last switch
- (d) any if

**Answer:** (b) the nearest unmatched if
**Explanation:** Use braces to change the pairing.

**Q11.** `int y = 2; if (y > 5); System.out.println("Hi");` prints
- (a) nothing
- (b) an error
- (c) Hi
- (d) 2

**Answer:** (c) Hi
**Explanation:** The semicolon ends the if; the println always runs.

**Q12.** With marks = 72, a ladder testing ≥ 90 (A), ≥ 75 (B), ≥ 60 (C), else D gives
- (a) A
- (b) B
- (c) D
- (d) C

**Answer:** (d) C
**Explanation:** 72 first satisfies ≥ 60.

**Q13.** Which is the correct way to test that m lies between 10 and 20 (exclusive)?
- (a) if (m > 10 && m < 20)
- (b) if (10 < m < 20)
- (c) if (m > 10 || m < 20)
- (d) if (m > 10, m < 20)

**Answer:** (a) if (m > 10 && m < 20)
**Explanation:** Java cannot chain comparisons.

**Q14.** Rewriting `if (code=='g') …GREEN… else if (code=='G') …GREEN…` as one if uses
- (a) &&
- (b) the OR operator
- (c) !
- (d) %

**Answer:** (b) the OR operator
**Explanation:** Either character gives GREEN.

**Q15.** Statement I: An if-else-if ladder can test ranges. Statement II: An if-else-if ladder can test double values.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (a) Both statements are true
**Explanation:** Unlike switch.

**Q16.** `boolean dh = True;` gives an error because
- (a) boolean cannot be assigned
- (b) dh is a keyword
- (c) True is not a boolean literal; Java is case sensitive
- (d) a semicolon is missing

**Answer:** (c) True is not a boolean literal; Java is case sensitive
**Explanation:** Write true (2024 specimen).

### The ternary operator (Q17–Q28)

**Q17.** The ternary operator is written as
- (a) ?:
- (b) &&
- (c) ::
- (d) ==

**Answer:** (a) ?:
**Explanation:** condition ? value1 : value2.

**Q18.** The ternary form of `if (a > b) z = 25; else z = 35;` is
- (a) z = a > b ? 35 : 25;
- (b) z = a > b ? 25 : 35;
- (c) z = a > b : 35 ? 25;
- (d) z = a > b : 25 ? 35;

**Answer:** (b) z = a > b ? 25 : 35;
**Explanation:** 2026 board MCQ.

**Q19.** With basic = 1500, `tax = basic>1200 ? 200 : 100;` gives tax =
- (a) 100
- (b) 1200
- (c) 1500
- (d) 200

**Answer:** (d) 200
**Explanation:** 2019 MS.

**Q20.** The valid ternary equivalent of printing "Precious" if x > y, else "Priceless", is
- (a) x>y?System.out.println("Priceless"):System.out.println("Precious");
- (b) System.out.println(x>y?"Priceless":"Precious");
- (c) x>y?System.out.println("Precious"):System.out.println("Priceless");
- (d) System.out.println(x>y?"Precious":"Priceless");

**Answer:** (d) System.out.println(x>y?"Precious":"Priceless");
**Explanation:** The ternary must give a value.

**Q21.** `int n = 7; String s = n % 2 == 0 ? "Even" : "Odd";` gives s =
- (a) Even
- (b) Odd
- (c) 7
- (d) an error

**Answer:** (b) Odd
**Explanation:** 7 % 2 is 1.

**Q22.** `int p = 10, q = 20; int c = p > q ? p - q : q - p;` gives c =
- (a) −10
- (b) 30
- (c) 10
- (d) 20

**Answer:** (c) 10
**Explanation:** The positive difference.

**Q23.** `int p = 5, q = 8, r = 3; int big = p > q ? (p > r ? p : r) : (q > r ? q : r);` gives big =
- (a) 5
- (b) 3
- (c) 16
- (d) 8

**Answer:** (d) 8
**Explanation:** A nested ternary finding the largest.

**Q24.** With u = 50, `u > 100 ? "big" : u > 40 ? "medium" : "small"` gives
- (a) big
- (b) medium
- (c) small
- (d) an error

**Answer:** (b) medium
**Explanation:** The second condition is true.

**Q25.** `r = n1 > n2 ? true : false;` can be shortened to
- (a) r = n1 > n2;
- (b) r = true;
- (c) r = n1 + n2;
- (d) r = !n1;

**Answer:** (a) r = n1 > n2;
**Explanation:** The comparison already gives a boolean.

**Q26.** The ternary operator is best used to
- (a) repeat statements
- (b) choose between two values
- (c) define a class
- (d) read input

**Answer:** (b) choose between two values
**Explanation:** if-else chooses between actions.

**Q27.** The number of operands of the conditional operator is
- (a) one
- (b) two
- (c) three
- (d) four

**Answer:** (c) three
**Explanation:** Condition, value1, value2.

**Q28.** The ternary operator is classified as a
- (a) logical operator
- (b) arithmetic operator
- (c) relational operator
- (d) conditional operator

**Answer:** (d) conditional operator
**Explanation:** 2024 specimen.

### The switch statement (Q29–Q50)

**Q29.** The absence of which statement leads to fall through in switch?
- (a) continue
- (b) System.exit(0)
- (c) return
- (d) break

**Answer:** (d) break
**Explanation:** 2023 MS.

**Q30.** Which data type cannot be used with switch?
- (a) int
- (b) char
- (c) String
- (d) double

**Answer:** (d) double
**Explanation:** 2024 MS.

**Q31.** Which of these is NOT true of a switch statement?
- (a) It checks equality with the case labels
- (b) It supports floating point constants
- (c) break exits the switch
- (d) Case labels are unique

**Answer:** (b) It supports floating point constants
**Explanation:** 2025 specimen MS.

**Q32.** With n = 10, `switch(n) { case 10: println(n*2); case 4: println(n*4); break; default: println(n); }` prints
- (a) 20 and 40 on two lines
- (b) 20 only
- (c) 40 only
- (d) 10

**Answer:** (a) 20 and 40 on two lines
**Explanation:** Fall through into case 4.

**Q33.** The branch that runs when no case matches is
- (a) break
- (b) else
- (c) default
- (d) continue

**Answer:** (c) default
**Explanation:** It is optional.

**Q34.** A construct used to pick exactly one item from a menu of ice creams is
- (a) while
- (b) do-while
- (c) for
- (d) switch

**Answer:** (d) switch
**Explanation:** 2025 Improvement.

**Q35.** In switch, Java checks only for
- (a) equality
- (b) ranges
- (c) greater than
- (d) logical expressions

**Answer:** (a) equality
**Explanation:** Ranges need if-else-if.

**Q36.** `boolean x = true; switch(x) {…}` gives
- (a) WIN
- (b) a compile-time error
- (c) LOOSE
- (d) no output

**Answer:** (b) a compile-time error
**Explanation:** A boolean selector is not allowed (2025 specimen).

**Q37.** With a = 3, `switch(a) { case 1: print("one "); case 3: print("three "); case 5: print("five "); break; default: print("none"); }` prints
- (a) three
- (b) three five
- (c) one three five
- (d) none

**Answer:** (b) three five
**Explanation:** Falls through until break.

**Q38.** With g = 'B', `case 'A': print(10); break; case 'B': case 'C': print(20); break; default: print(0);` prints
- (a) 10
- (b) 0
- (c) 20
- (d) 1020

**Answer:** (c) 20
**Explanation:** 'B' shares the block with 'C'.

**Q39.** With w = 4, `case 1: case 2: println("low"); break; case 3: case 4: println("mid"); default: println("high");` prints
- (a) mid
- (b) high
- (c) low
- (d) mid and high

**Answer:** (d) mid and high
**Explanation:** No break after "mid".

**Q40.** With z = 9, `switch (z % 3)` with cases 0, 1 and default prints for case 0
- (a) zero
- (b) one
- (c) two
- (d) nothing

**Answer:** (a) zero
**Explanation:** 9 % 3 is 0.

**Q41.** With k = 3, `switch (k) { default: println("D"); case 1: println("one"); break; case 2: println("two"); }` prints
- (a) D only
- (b) D and one
- (c) one only
- (d) two

**Answer:** (b) D and one
**Explanation:** default can come first and still falls through.

**Q42.** Case labels in a switch must be
- (a) variables
- (b) ranges
- (c) unique constants
- (d) boolean expressions

**Answer:** (c) unique constants
**Explanation:** Duplicates are a compile error.

**Q43.** Which of these can be a switch expression type?
- (a) long
- (b) float
- (c) boolean
- (d) String

**Answer:** (d) String
**Explanation:** Also int, char, byte, short.

**Q44.** The correct switch for "Moderate" when a is 1, 2 or 3, else "Tough", uses
- (a) case 1-3:
- (b) case 1: case 2: case 3:
- (c) case a>=1 && a<=3:
- (d) case (1, 2, 3):

**Answer:** (b) case 1: case 2: case 3:
**Explanation:** Shared labels (2026 Improvement).

**Q45.** Statement I: break is used to exit a switch. Statement II: default must be the last branch.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (c) Statement I is true, Statement II is false
**Explanation:** default may appear anywhere.

**Q46.** A switch with a String expression compares the text with
- (a) the case-label strings exactly (letter case matters)
- (b) its first letter only
- (c) its length
- (d) its Unicode sum

**Answer:** (a) the case-label strings exactly (letter case matters)
**Explanation:** "two" does not match "Two".

**Q47.** An advantage of switch over if-else-if is that it
- (a) can test ranges
- (b) works with double
- (c) can test logical expressions
- (d) is neater for many exact-value choices

**Answer:** (d) is neater for many exact-value choices
**Explanation:** e.g. menus.

**Q48.** An advantage of if-else-if over switch is that it
- (a) can test ranges and any data type
- (b) never needs braces
- (c) falls through
- (d) uses case labels

**Answer:** (a) can test ranges and any data type
**Explanation:** switch tests equality only.

**Q49.** Assertion: break avoids fall through. Reason: break lets only one case execute. Choose:
- (a) Both true; R explains A
- (b) Both true; R does not explain A
- (c) A true, R false
- (d) A false, R true

**Answer:** (a) Both true; R explains A
**Explanation:** 2025 MS.

**Q50.** Which statement is used to leave a switch block?
- (a) continue
- (b) exit
- (c) break
- (d) stop

**Answer:** (c) break
**Explanation:** Control goes to the statement after the switch.

### Menus, System.exit and conversions (Q51–Q64)

**Q51.** A program that displays choices and performs the one selected is a
- (a) menu-driven program
- (b) nested loop
- (c) package
- (d) constructor

**Answer:** (a) menu-driven program
**Explanation:** Usually built with switch.

**Q52.** The statement that terminates the whole program at once is
- (a) break
- (b) return
- (c) continue
- (d) System.exit(0)

**Answer:** (d) System.exit(0)
**Explanation:** Used for an Exit option.

**Q53.** In a menu-driven program, an invalid choice is usually handled by
- (a) default
- (b) case 0
- (c) break
- (d) continue

**Answer:** (a) default
**Explanation:** It prints an error message.

**Q54.** Converting `switch(x){case 'T': case 't': print("Teacher"); break; default: print("Student");}` to if-else gives
- (a) if (x == 'T' && x == 't') …
- (b) if (x == 'T') … else if (x == 't') … only
- (c) if (x == 'T' || x == 't') print("Teacher"); else print("Student");
- (d) if (x != 'T') print("Teacher");

**Answer:** (c) if (x == 'T' || x == 't') print("Teacher"); else print("Student");
**Explanation:** Either letter gives Teacher.

**Q55.** Converting `double ch = (m>300) ? (m/10.0)*2 : (m/20.0)-2;` with m = 400 gives ch =
- (a) 18.0
- (b) 80.0
- (c) 40.0
- (d) 20.0

**Answer:** (b) 80.0
**Explanation:** 400/10.0 × 2.

**Q56.** In `switch (ch) { case 'c': case 'C': … }`, writing two labels together lets
- (a) both cases run twice
- (b) an error occur
- (c) either character run the same block
- (d) the switch be skipped

**Answer:** (c) either character run the same block
**Explanation:** Shared case labels.

**Q57.** Which can replace a long if-else-if chain testing `var == 1`, `var == 2`, `var == 3`?
- (a) a for loop
- (b) a ternary only
- (c) a constructor
- (d) a switch on var

**Answer:** (d) a switch on var
**Explanation:** 2018 Q3(f).

**Q58.** A semicolon placed directly after `if (condition)` makes the if
- (a) control nothing
- (b) control the next two statements
- (c) a loop
- (d) a switch

**Answer:** (a) control nothing
**Explanation:** The empty statement is the if's body.

**Q59.** A menu choice is usually read with
- (a) System.exit(0)
- (b) sc.nextInt()
- (c) Math.random()
- (d) break

**Answer:** (b) sc.nextInt()
**Explanation:** The number of the option.

**Q60.** To check that a year y is a leap year, the condition is
- (a) y % 4 == 0
- (b) y % 100 == 0
- (c) (y % 4 == 0 && y % 100 != 0) OR (y % 400 == 0)
- (d) y % 400 != 0

**Answer:** (c) (y % 4 == 0 && y % 100 != 0) OR (y % 400 == 0)
**Explanation:** 1900 is not a leap year; 2000 is.

**Q61.** Three sides a, b, c form a triangle only if
- (a) each pair's sum is greater than the third side
- (b) a == b == c
- (c) a + b + c > 0
- (d) a > b > c

**Answer:** (a) each pair's sum is greater than the third side
**Explanation:** a + b > c, b + c > a, a + c > b.

**Q62.** For a discount scheme of 5 % up to ₹2000, 10 % up to ₹5000 and 15 % above, a purchase of ₹4000 gets
- (a) 5 %
- (b) 15 %
- (c) 10 %
- (d) 20 %

**Answer:** (c) 10 %
**Explanation:** It falls in the second slab.

**Q63.** In `if (b == 0) println("Division by zero is not allowed"); else println(a / b);`, the if protects against
- (a) a syntax error
- (b) a logical error in the menu
- (c) dividing by zero
- (d) fall through

**Answer:** (c) dividing by zero
**Explanation:** A runtime problem for integers.

**Q64.** Statement I: A ternary operator can replace any switch. Statement II: A switch can replace an if-else-if that tests exact integer values.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (d) Statement I is false, Statement II is true
**Explanation:** Ternary picks between two values only.

### Mixed practice (Q65–Q76)

**Q65.** `int a = 5, b = 5; if (a == b) System.out.println("Equal");` prints
- (a) nothing
- (b) Equal
- (c) an error
- (d) 5

**Answer:** (b) Equal
**Explanation:** == compares values.

**Q66.** `if (x = 5)` in Java gives
- (a) true
- (b) false
- (c) a compile-time error
- (d) 5

**Answer:** (c) a compile-time error
**Explanation:** = assigns; an int is not a boolean.

**Q67.** The relational operator for "not equal to" is
- (a) <>
- (b) =!
- (c) !=
- (d) ~=

**Answer:** (c) !=
**Explanation:** == is "equal to".

**Q68.** In a grading ladder, testing `per >= 60` before `per >= 90` would
- (a) give grade C to a student with 95
- (b) work correctly
- (c) cause an error
- (d) skip all grades

**Answer:** (a) give grade C to a student with 95
**Explanation:** The first true condition wins.

**Q69.** `String result = (m1 >= 33 && m2 >= 33) ? "PASS" : "FAIL";` with m1 = 40, m2 = 30 gives
- (a) PASS
- (b) an error
- (c) 70
- (d) FAIL

**Answer:** (d) FAIL
**Explanation:** Both marks must be at least 33.

**Q70.** A menu offering "1. Add 2. Subtract 3. Exit" is best handled by a
- (a) nested loop
- (b) switch with three cases
- (c) class
- (d) package

**Answer:** (b) switch with three cases
**Explanation:** A menu-driven switch.

**Q71.** Which keyword is NOT used in a switch statement?
- (a) case
- (b) default
- (c) break
- (d) else

**Answer:** (d) else
**Explanation:** else belongs to if.

**Q72.** `char op = '*';` in a calculator switch selects
- (a) case '+'
- (b) case '-'
- (c) case '*'
- (d) default

**Answer:** (c) case '*'
**Explanation:** It matches the label exactly.

**Q73.** The output of `int a = 2; switch (a) { case 1: case 2: case 3: System.out.println("Moderate"); break; default: System.out.println("Tough"); }` is
- (a) Tough
- (b) Moderate and Tough
- (c) nothing
- (d) Moderate

**Answer:** (d) Moderate
**Explanation:** 2 matches; break stops.

**Q74.** Selecting one of two actions according to a condition is called
- (a) iteration
- (b) selection (branching)
- (c) sequence
- (d) recursion

**Answer:** (b) selection (branching)
**Explanation:** if-else and switch.

**Q75.** Which is a valid if statement?
- (a) if x > 5 then print
- (b) if (x > 5) System.out.println(x);
- (c) if [x > 5] System.out.println(x);
- (d) if x > 5: System.out.println(x);

**Answer:** (b) if (x > 5) System.out.println(x);
**Explanation:** The condition goes in round brackets.

**Q76.** The best construct for "if salary > 50000 tax 20 %, else if > 25000 tax 10 %, else 0 %" is
- (a) switch
- (b) a ternary with no condition
- (c) an if-else-if ladder
- (d) a do-while loop

**Answer:** (c) an if-else-if ladder
**Explanation:** Ranges need relational tests.

---

## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** Distinguish between if-else-if and switch-case.
**Answer:** if-else-if can test ranges and any relational or logical condition on any type.
switch tests only equality with constant labels, for int, char, String, byte and short.

**Q2.** What is fall through? How is it prevented?
**Answer:** When a case has no break, control continues into the next case.
It is prevented by writing break at the end of each case.

**Q3.** State two rules for case labels.
**Answer:** Case labels must be constants of the switch expression's type.
They must be unique (no two cases with the same value).

**Q4.** What is the use of default in a switch?
**Answer:** It runs when no case label matches the expression.
In a menu it displays a message for an invalid choice.

**Q5.** Distinguish between the ternary operator and if-else.
**Answer:** The ternary operator gives one of two values and fits in an expression.
if-else chooses between two blocks of statements (actions).

**Q6.** What is a nested if? Give an example.
**Answer:** An if statement placed inside another if.
`if (x > 0) if (x % 2 == 0) System.out.println("Positive even");`

**Q7.** What is a dangling else?
**Answer:** An else that could belong to more than one if.
Java pairs it with the nearest unmatched if; braces make the pairing clear.

**Q8.** What is a menu-driven program?
**Answer:** A program that displays a list of choices and carries out the one the user selects.
It is usually written with switch and a default for an invalid choice.

**Q9.** State the use of System.exit(0) and break.
**Answer:** System.exit(0) terminates the whole program.
break leaves the current switch (or loop).

**Q10.** Name two data types that can and two that cannot be used in a switch.
**Answer:** Can: int, char (also String, byte, short).
Cannot: double, boolean (also float, long).

**Q11.** Why can `if (10 < m < 20)` not be written in Java? Correct it.
**Answer:** 10 < m gives a boolean, which cannot be compared with 20.
Write `if (m > 10 && m < 20)`.

**Q12.** When would you choose an if-else-if ladder rather than switch?
**Answer:** When ranges or relational conditions must be tested (e.g. marks ≥ 75).
Or when the value is a double, boolean or long.

### Output and error questions (2 marks each)

**Q13.** Give the output when x = 5: `if (x > 3) if (x > 10) System.out.println("A"); else System.out.println("B");`
**Answer:** `B`
The else pairs with the inner if (x > 10), which is false.

**Q14.** Give the output when a = 3: `switch (a) { case 1: System.out.print("one "); case 3: System.out.print("three "); case 5: System.out.print("five "); break; default: System.out.print("none"); }`
**Answer:** `three five`
No break after case 3, so case 5 also runs.

**Q15.** Give the output when w = 4: `switch (w) { case 1: case 2: System.out.println("low"); break; case 3: case 4: System.out.println("mid"); default: System.out.println("high"); }`
**Answer:** mid and high on two lines.
Case 4 has no break, so default also runs.

**Q16.** Give the output: `int y = 2; if (y > 5); System.out.println("Hi");`
**Answer:** `Hi`
The semicolon ends the if; the println is a separate statement.

**Q17.** Find the error and correct: `boolean x = true; switch (x) { case 1: System.out.println("WIN"); }`
**Answer:** A switch cannot use a boolean selector (and case 1 is not boolean).
Write `int x = 1;`

**Q18.** Find the error and correct: `if (x = 5) System.out.println("Five");`
**Answer:** = assigns; the condition must be boolean (compile error).
Write `if (x == 5)`.

**Q19.** Give the output with u = 50: `String r = u > 100 ? "big" : u > 40 ? "medium" : "small"; System.out.println(r);`
**Answer:** `medium`
u > 100 is false; u > 40 is true.

**Q20.** Give the output: `int n = 7; System.out.println(n % 2 == 0 ? "Even" : "Odd");`
**Answer:** `Odd`
7 % 2 is 1.

**Q21.** Rewrite with if-else: `String msg = leap ? "a leap year" : "not a leap year";`
**Answer:** `String msg; if (leap) msg = "a leap year"; else msg = "not a leap year";`
The ternary chooses between two values.

**Q22.** Give the output when k = 3: `switch (k) { default: System.out.println("D"); case 1: System.out.println("one"); break; case 2: System.out.println("two"); }`
**Answer:** D and one on two lines.
default runs (no match) and falls through into case 1.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; a sample run follows each.*

### Section B programs (15 marks each)

**Q1.** A shop gives a discount on the purchase amount: up to ₹2000 — 5 %; ₹2001 to ₹5000 — 10 %; ₹5001 to ₹10000 — 15 %; above ₹10000 — 20 %. Write a program to accept the amount and print the rate, the discount and the net amount.
**Answer:**
```java
import java.util.*;
class Discount
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the purchase amount: ");
        double amt = sc.nextDouble();
        double rate;
        if (amt <= 2000)
            rate = 5;
        else if (amt <= 5000)
            rate = 10;
        else if (amt <= 10000)
            rate = 15;
        else
            rate = 20;
        double disc = amt * rate / 100;
        double net = amt - disc;
        System.out.println("Discount rate : " + rate + " %");
        System.out.println("Discount      : " + disc);
        System.out.println("Net amount    : " + net);
    }
}
```
Sample run:
```
Enter the purchase amount: 7500
Discount rate : 15.0 %
Discount      : 1125.0
Net amount    : 6375.0
```

**Q2.** Write a menu-driven calculator that accepts two numbers and an operator (+, −, *, /, %) and prints the result using switch. Print a message for division by zero and for an invalid operator.
**Answer:**
```java
import java.util.*;
class Calculator
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two numbers: ");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        System.out.print("Enter an operator (+ - * / %): ");
        char op = sc.next().charAt(0);
        switch (op)
        {
            case '+':
                System.out.println("Result = " + (a + b));
                break;
            case '-':
                System.out.println("Result = " + (a - b));
                break;
            case '*':
                System.out.println("Result = " + (a * b));
                break;
            case '/':
                if (b == 0)
                    System.out.println("Division by zero is not allowed");
                else
                    System.out.println("Result = " + (a / b));
                break;
            case '%':
                System.out.println("Result = " + (a % b));
                break;
            default:
                System.out.println("Invalid operator");
        }
    }
}
```
Sample runs:
```
Enter two numbers: 17 5
Enter an operator (+ - * / %): %
Result = 2.0

Enter two numbers: 8 0
Enter an operator (+ - * / %): /
Division by zero is not allowed
```

**Q3.** Write a program to accept three sides and check whether they can form a triangle; if so, print whether it is equilateral, isosceles or scalene.
**Answer:**
```java
import java.util.*;
class Triangle
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the three sides: ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        if (a + b > c && b + c > a && a + c > b)
        {
            if (a == b && b == c)
                System.out.println("Equilateral triangle");
            else if (a == b || b == c || a == c)
                System.out.println("Isosceles triangle");
            else
                System.out.println("Scalene triangle");
        }
        else
            System.out.println("These sides cannot form a triangle");
    }
}
```
Sample runs:
```
Enter the three sides: 5 5 8
Isosceles triangle

Enter the three sides: 2 3 9
These sides cannot form a triangle
```

**Q4.** Write a program to accept marks in three subjects, find the percentage and print the grade (≥ 90 A, ≥ 75 B, ≥ 60 C, ≥ 40 D, else E). Using a ternary operator, print PASS only if every subject has at least 33 marks, else FAIL.
**Answer:**
```java
import java.util.*;
class Grade
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter marks in three subjects (out of 100): ");
        int m1 = sc.nextInt();
        int m2 = sc.nextInt();
        int m3 = sc.nextInt();
        double per = (m1 + m2 + m3) / 3.0;
        char grade;
        if (per >= 90)
            grade = 'A';
        else if (per >= 75)
            grade = 'B';
        else if (per >= 60)
            grade = 'C';
        else if (per >= 40)
            grade = 'D';
        else
            grade = 'E';
        String result = (m1 >= 33 && m2 >= 33 && m3 >= 33) ? "PASS" : "FAIL";
        System.out.println("Percentage : " + Math.round(per * 100) / 100.0);
        System.out.println("Grade      : " + grade);
        System.out.println("Result     : " + result);
    }
}
```
Sample run:
```
Enter marks in three subjects (out of 100): 88 79 93
Percentage : 86.67
Grade      : B
Result     : PASS
```

**Q5.** Write a menu-driven program to find the area of a circle (3.14 r²), a square or a rectangle, with a fourth option that exits the program using System.exit(0) and a message for a wrong choice.
**Answer:**
```java
import java.util.*;
class Shapes
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("1. Area of a circle");
        System.out.println("2. Area of a square");
        System.out.println("3. Area of a rectangle");
        System.out.println("4. Exit");
        System.out.print("Enter your choice: ");
        int ch = sc.nextInt();
        switch (ch)
        {
            case 1:
                System.out.print("Enter the radius: ");
                double r = sc.nextDouble();
                System.out.println("Area = " + 3.14 * r * r);
                break;
            case 2:
                System.out.print("Enter the side: ");
                double s = sc.nextDouble();
                System.out.println("Area = " + s * s);
                break;
            case 3:
                System.out.print("Enter length and breadth: ");
                double l = sc.nextDouble();
                double b = sc.nextDouble();
                System.out.println("Area = " + l * b);
                break;
            case 4:
                System.out.println("Thank you");
                System.exit(0);         // ends the program immediately
            default:
                System.out.println("Wrong choice");
        }
    }
}
```
Sample runs:
```
Enter your choice: 1
Enter the radius: 7
Area = 153.86

Enter your choice: 4
Thank you
```

**Q6.** Write a program to accept a year and print whether it is a leap year (divisible by 4 but not by 100, or divisible by 400), and the number of days in February, using the ternary operator.
**Answer:**
```java
import java.util.*;
class LeapYear
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a year: ");
        int y = sc.nextInt();
        boolean leap = (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
        String msg = leap ? "a leap year" : "not a leap year";
        int febDays = leap ? 29 : 28;
        System.out.println(y + " is " + msg);
        System.out.println("February has " + febDays + " days");
    }
}
```
Sample runs:
```
Enter a year: 1900
1900 is not a leap year
February has 28 days

Enter a year: 2024
2024 is a leap year
February has 29 days
```

---

## 12. Competency / Application Questions

**Q1. (Electricity slabs)** A board charges ₹3 per unit for the first 100 units, ₹5 per unit for the next 100 and ₹7 per unit beyond 200. Write the if-else-if ladder for the bill b for u units.
**Model answer:** `if (u <= 100) b = u * 3; else if (u <= 200) b = 300 + (u - 100) * 5; else b = 800 + (u - 200) * 7;`

**Q2. (The ATM menu)** An ATM shows 1. Withdraw 2. Deposit 3. Balance 4. Exit. Which construct suits it, and what should option 4 and a wrong key do?
**Model answer:** A switch on the choice; case 4 calls System.exit(0); default prints "Invalid choice".

**Q3. (The bug report)** A grading program prints C for a student with 95 %. The ladder tests ≥ 60 first. Explain and fix.
**Model answer:** The first true condition wins, so 95 is caught by ≥ 60. Test from the highest range down: ≥ 90, then ≥ 75, then ≥ 60.

**Q4. (Vowel or consonant)** Write a switch that prints Vowel for a, e, i, o, u (small or capital) and Consonant for other letters.
**Model answer:** List all ten vowel labels together (`case 'a': case 'A': …`), print Vowel and break; default prints Consonant (after checking it is a letter).

**Q5. (Bus fare)** Children under 5 travel free; others pay ₹20. Write one statement using a ternary operator.
**Model answer:** `int fare = age < 5 ? 0 : 20;`

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** A switch cannot be used to test whether marks are between 60 and 75.
**R:** A switch checks only for equality with constant labels.
**Answer:** (c)
**Explanation:** Ranges need if-else-if.

**Q2.**
**A:** A switch on a double variable is allowed in Java.
**R:** A switch works with int, char and String.
**Answer:** (b)
**Explanation:** double is not allowed; R is true.

**Q3.**
**A:** Without break, the statements of the next case also run.
**R:** This is called fall through.
**Answer:** (c)
**Explanation:** R names the behaviour in A.

**Q4.**
**A:** `x > y ? System.out.println("P") : System.out.println("Q");` is a valid statement.
**R:** The ternary operator selects one of two values.
**Answer:** (b)
**Explanation:** println returns nothing, so this is invalid; R is true.

**Q5.**
**A:** default can be placed anywhere in a switch.
**R:** System.exit(0) terminates a program.
**Answer:** (d)
**Explanation:** Both true; unrelated.

**Q6.**
**A:** In an if-else-if ladder, at most one block runs.
**R:** Once a condition is true, the remaining conditions are skipped.
**Answer:** (c)
**Explanation:** First true wins.

**Q7.**
**A:** `if (x > 5) if (x > y) …` can be written as `if (x > 5 && x > y) …`.
**R:** Both conditions must be true for the statement to run.
**Answer:** (c)
**Explanation:** && joins them.

**Q8.**
**A:** `boolean ok = True;` compiles.
**R:** Java is case sensitive.
**Answer:** (b)
**Explanation:** It must be true; R is true.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The canteen menu

> A canteen kiosk shows "1. Tea 2. Coffee 3. Samosa 4. Exit". The program reads the choice and uses a switch; choice 4 ends the program; any other number prints "Invalid".

**(i)** What kind of program is this?
**Answer:** A menu-driven program.

**(ii)** Which statement ends the program for choice 4?
**Answer:** System.exit(0).

**(iii)** Which part of the switch prints "Invalid"?
**Answer:** default.

**(iv)** What happens if break is missing after case 1?
**Answer:** Fall through — case 2 also runs.

### Case 2 — Grading

> `if (p >= 90) g = 'A'; else if (p >= 75) g = 'B'; else if (p >= 60) g = 'C'; else g = 'D';`

**(i)** Name this construct.
**Answer:** if-else-if ladder.

**(ii)** What is g when p = 82?
**Answer:** B.

**(iii)** What is g when p = 45?
**Answer:** D.

**(iv)** Why can this not be written with switch directly?
**Answer:** It tests ranges; switch tests only equality.

### Case 3 — The ternary shortcut

> `int a = 12, b = 9, c = 15; int big = a > b ? (a > c ? a : c) : (b > c ? b : c);`

**(i)** Is a > b true or false?
**Answer:** True.

**(ii)** Which inner expression is evaluated?
**Answer:** a > c ? a : c.

**(iii)** What is big?
**Answer:** 15.

**(iv)** Name the operator used.
**Answer:** The ternary (conditional) operator.

---

## 15. Revision Notes

### Chapter at a glance
- if, if-else, if-else-if ladder (first true wins), nested if (often &&), dangling else (nearest if).
- Ternary `c ? v1 : v2` — gives a value; both branches must be values.
- switch — equality only; int, char, String, byte, short (not double, float, long, boolean); constant unique labels; break; default anywhere; shared labels; fall through.
- if-else-if vs switch — ranges and any type vs equality and limited types.
- Menu-driven programs with switch; System.exit(0) ends the program.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| Forgetting break in every case | Fall through runs the next case. |
| switch on a double or boolean | Use if-else-if; switch accepts int, char, String. |
| `if (x = 5)` | Use `==` for comparison. |
| `x > y ? System.out.println(…) : …` | Put the ternary inside println. |
| Testing low ranges first in a ladder | Test the highest range first. |
| `boolean b = True;` | Write `true`. |
| `if (10 < m < 20)` | `if (m > 10 && m < 20)`. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 3: Revision III**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** Missing break causes:
(a) fall through (b) an infinite loop (c) a syntax error (d) nothing

**2.** Not allowed in switch:
(a) int (b) char (c) String (d) double

**3.** Ternary form of `if (a > b) z = 25; else z = 35;`:
(a) z = a > b ? 35 : 25; (b) z = a > b ? 25 : 35; (c) z = a > b : 25 ? 35; (d) z = 25 ? a > b : 35;

**4.** `tax = basic > 1200 ? 200 : 100;` with basic = 1500:
(a) 100 (b) 200 (c) 1200 (d) 1500

**5.** Ends the program:
(a) break (b) continue (c) System.exit(0) (d) default

**6.** With n = 10, `switch(n){case 10: println(n*2); case 4: println(n*4); break;}` prints:
(a) 20 (b) 40 (c) 20 and 40 (d) 10

**7.** An else pairs with:
(a) the first if (b) the nearest unmatched if (c) any if (d) a switch

**8.** `if (a > b && b > c)` — largest:
(a) a (b) b (c) c (d) cannot tell

**9.** Statement I: switch tests ranges. Statement II: if-else-if can test ranges.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

**10.** `boolean flag = false; if (flag) println("True"); else println("False");` prints:
(a) True (b) False (c) nothing (d) error

### Part I — Short answers (5 × 2 = 10)

**11.** Differentiate if-else-if and switch (two points). [2]

**12.** Convert into switch: `if (var==1) …good… else if (var==2) …better… else …invalid…` [2]

**13.** Rewrite with logical operators: `if (x > 5) if (x > y) System.out.println(x+y);` [2]

**14.** Find and correct the error: `boolean x = true; switch(x) { case 1: … }` [2]

**15.** Give the output when w = 4 for the low/mid/high switch of Section 10, Q15. [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** (i) Explain fall through with an example. [4]
(ii) Write a menu-driven calculator for +, −, * and / with a default message. [6]

**17.** (i) Rewrite using ternary: `if (bill > 10000) discount = bill*10.0/100; else discount = bill*5.0/100;` and give the discount when bill = 12000. [4]
(ii) Write a program to classify a triangle from its three sides. [6]

**18.** (i) State four rules of the switch statement. [4]
(ii) Write a program to check a leap year. [6]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | b | d | c | c | b |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | Menu-driven | System.exit(0) | default | Fall through |
| 2 | if-else-if ladder | B | D | Ranges |
| 3 | True | a > c ? a : c | 15 | Ternary |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | a | d | b | b | c | c | b | a | d | b |

**Part I, Q11–15 (2 marks each)**

**11.** Any two differences (1 + 1).
**12.** switch with cases 1, 2 and default (1); breaks (1).
**13.** `if (x > 5 && x > y)` (2).
**14.** boolean not allowed (1); `int x = 1;` (1).
**15.** mid (1); high (1).

**Part II (10 marks each)**

**16.** (i) Definition (2), example (2). (ii) Input (1), switch with four cases (3), division check / default (2).

**17.** (i) Ternary statement (2); 1200.0 (2). (ii) Validity check (2), equilateral / isosceles / scalene (3), output (1).

**18.** (i) Any four rules (4). (ii) Input (1), condition with && and OR (3), output (2).
