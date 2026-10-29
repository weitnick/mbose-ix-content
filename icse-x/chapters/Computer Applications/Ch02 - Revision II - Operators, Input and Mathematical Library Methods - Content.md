# Revision II — Operators, Input in Java and Mathematical Library Methods

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 2 |
| Title | Revision II — Operators, Input in Java and Mathematical Library Methods |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 1. Revision of Class IX syllabus: (iv) Operators in Java, (v) Input in Java, (vi) Mathematical library methods |
| Exam weightage | Every Section A has an **"evaluate the expression"** part with `++`/`--` and a shorthand operator (2 marks), a **"write the Java expression"** part (2 marks), **Math method outputs** (ceil, floor, round, pow, sqrt, max, min) and MCQs on **operator types, precedence, Scanner methods and types of errors**. |
| Syllabus scope | Forms of operators (unary, binary, ternary); arithmetic, relational, logical, assignment, increment/decrement and shorthand operators; counters and accumulators; precedence and associativity; prefix and postfix; the `new` and dot operators; `print()` and `println()`. Initialisation, parameters and input through the Scanner class; syntax, runtime and logical errors; comments. Package java.lang and the Math methods pow, sqrt, cbrt, ceil, floor, round, abs, max, min, random; writing Java expressions. |
| In short | A revision of Java operators, how to take input from the user, and using Math library methods for calculations. |

> **Note on the text:** CISCE does not prescribe a textbook for ICSE Computer Applications. This chapter is written to the ICSE 2027 syllabus in its own words; its exam questions are the CISCE board papers of 2017–2026 and the specimen papers of 2024 and 2025, answered from CISCE's marking schemes wherever one has been published. **Every expression and output in this chapter was checked by running it (Java 21).**
>
> **Exam note:** In **`x op= expression`** Java **first saves the old value of x**, then evaluates the right side **from left to right** (applying every `++` and `--` as it goes), and only then combines: `x = old x op (right side)`. **Prefix** (`++x`) changes first and uses the new value; **postfix** (`x++`) uses the old value, then changes. **Integer division drops the fraction** (`7/2` is 3, `2/3` is 0) — the cause of many "logical error" questions. **Math.ceil/floor/sqrt/pow/cbrt return double** (write 4.0, not 4); **Math.round returns a whole number** (long). In Java expressions write every multiplication sign: `b*b - 4*a*c`, not `b2 - 4ac`.

---

## 1. Complete Lesson

### Operators and their forms

An **operator** is a symbol that performs an operation on one or more **operands** (values or variables). In `a + b`, `+` is the operator and `a`, `b` are operands.

| Form | Number of operands | Examples |
|---|---|---|
| **Unary** | One | `++x`, `x--`, `-a`, `!found` |
| **Binary** | Two | `a + b`, `a > b`, `a && b`, `x = 5` |
| **Ternary** | Three | `a > b ? a : b` |

**Example 1.** *(ICSE 2019, Q1(b))* Write a difference between unary and binary operator.
**Solution:** A **unary** operator works on a **single operand** (e.g. `++a`); a **binary** operator works on **two operands** (e.g. `a + b`).

### Types of operators

| Type | Operators | Result | Example |
|---|---|---|---|
| **Arithmetic** | `+` `-` `*` `/` `%` | number | `17 / 5` is 3; `17 % 5` is 2 |
| **Relational** | `<` `>` `<=` `>=` `==` `!=` | true / false | `a >= b` |
| **Logical** | `&&` (AND) `\|\|` (OR) `!` (NOT) | true / false | `a > 0 && b > 0` |
| **Assignment** | `=` | stores a value | `x = 10` |
| **Shorthand (compound) assignment** | `+=` `-=` `*=` `/=` `%=` | `x += 2` means `x = x + 2` | `s += n` |
| **Increment / decrement** | `++` `--` | adds / subtracts 1 | `i++`, `--j` |
| **Conditional (ternary)** | `?:` | one of two values | `max = a > b ? a : b` |
| **new** | `new` | creates an object (dynamic memory) | `Scanner sc = new Scanner(System.in);` |
| **Dot** | `.` | invokes a member of a class or object | `Math.sqrt(x)`, `sc.nextInt()` |

**`/` and `%`:** `/` gives the **quotient** and `%` the **remainder**. With two integers `/` is **integer division** (`7/2` = 3); with a double it is real division (`7.0/2` = 3.5). The sign of `%` follows the first operand: `-17 % 5` = −2.

**Logical operators** — `&&` is true only if **both** sides are true; `||` is true if **either** side is true; `!` reverses. Java stops early (**short-circuit**): in `a != 0 && b / a > 2`, the division is skipped when a is 0.

**Counters and accumulators**
- A **counter** increases by a **fixed amount**, usually 1, to **count** something: `c = c + 1;` or `c++`.
- An **accumulator** **adds varying values** to build a **total**: `sum = sum + n;` or `s += n`. In `c = c + (x * d + e);`, **c** is the accumulator.

### Increment and decrement — prefix and postfix

| Form | Meaning | Example (x = 5) |
|---|---|---|
| **Prefix** `++x` / `--x` | **Change first, then use** the new value | `y = ++x;` → x = 6, y = 6 |
| **Postfix** `x++` / `x--` | **Use the old value, then change** | `y = x++;` → y = 5, x = 6 |

```java
int lives = 5;
System.out.print(lives--);   // prints 5, then lives becomes 4
System.out.print(lives);     // prints 4
// output: 54
```

### Precedence and associativity

**Precedence** decides which operator is applied first; **associativity** decides the order among operators of equal precedence.

| Priority | Operators | Associativity |
|---|---|---|
| 1 (highest) | Postfix `x++` `x--` | left to right |
| 2 | Unary `++x` `--x` `+` `-` `!` and casts `(int)` | right to left |
| 3 | Multiplicative `*` `/` `%` | left to right |
| 4 | Additive `+` `-` | left to right |
| 5 | Relational `<` `>` `<=` `>=` | left to right |
| 6 | Equality `==` `!=` | left to right |
| 7 | Logical AND `&&` | left to right |
| 8 | Logical OR `\|\|` | left to right |
| 9 | Ternary `?:` | right to left |
| 10 (lowest) | Assignment `=` `+=` `-=` `*=` `/=` `%=` | right to left |

`*`, `/` and `%` have **equal** precedence and are applied **left to right**: `42 / 6 % 2` = `7 % 2` = **1**; `7 * 8 % 3` = `56 % 3` = **2**. In `a + b % c * d - e` the **%** is applied first (it is the leftmost of the highest-priority operators). Brackets override everything.

**Example 2.** *(ICSE 2025 specimen, Q1(iv))* Identify the operator that gets the highest precedence while evaluating `a + b % c * d - e`: (a) + (b) % (c) − (d) *
**Solution:** **(b) %** — `%` and `*` rank above `+` and `−`, and between them the leftmost (`%`) is applied first.

### Evaluating expressions step by step

**Method:** (1) for `x op= …`, note the **old value of x**; (2) go **left to right** through the right side, replacing each operand by its value at that moment and updating variables for `++`/`--`; (3) apply precedence to the numbers; (4) combine with the old value of x.

**Example 3.** *(ICSE 2018, Q3(b))* What is the value of y after evaluating `y += ++y + y-- + --y;` when `int y = 8`?
**Solution:**
- Old value of y = **8**.
- `++y` → y becomes 9, value **9**; `y--` → value **9**, y becomes 8; `--y` → y becomes 7, value **7**.
- Right side = 9 + 9 + 7 = 25; y = 8 + 25 = **33**.

**Example 4.** *(ICSE 2023, Q2(ii))* Evaluate `x *= --x + x++ + x;` when x = 4.
**Solution:** Old x = 4. `--x` → **3** (x = 3); `x++` → **3** (x = 4); `x` → **4**. x = 4 × (3 + 3 + 4) = **40**.

### Output: print() and println()

- `System.out.print(…)` prints and **stays on the same line**.
- `System.out.println(…)` prints and **moves to the next line**.

```java
System.out.print("BEST ");
System.out.println("OF LUCK");
// output: BEST OF LUCK   (one line)
```

### Input in Java

Data can reach a program in three ways:

| Way | When the data is given | Example |
|---|---|---|
| **Initialisation** | **Before execution** — written in the program | `int a = 10;` |
| **Parameters** | **At the time of execution** — passed to a method (e.g. typed in BlueJ's method-call box) | `void area(double l, double b)` |
| **Input stream (Scanner)** | **During execution** — typed by the user | `int n = sc.nextInt();` |

**The Scanner class** (package `java.util`):

```java
import java.util.*;            // or import java.util.Scanner;
...
Scanner sc = new Scanner(System.in);
```

| Method | Reads |
|---|---|
| `nextShort()` | a short |
| `nextInt()` | an int |
| `nextLong()` | a long |
| `nextFloat()` | a float |
| `nextDouble()` | a double |
| `next()` | **one word** (stops at a space) |
| `nextLine()` | **a whole line, including spaces** |
| `next().charAt(0)` | **one character** (the first character of the next word) |

**Example 5.** *(ICSE 2023, Q1(iii))* The Scanner class method used to accept words with space: (a) next() (b) nextLine() (c) Next() (d) nextString()
**Solution:** **(b) nextLine()**.

### Types of errors

| Error | When it is found | Examples |
|---|---|---|
| **Syntax (compile-time) error** | By the **compiler**, before the program runs — the rules of the language are broken | Missing semicolon; misspelt keyword; using a variable before giving it a value; `int y = Double.parseDouble(x);` (type mismatch) |
| **Runtime error** | **While the program runs** — it stops abnormally | Integer division by zero; typing a word when a number is expected; using an array index that does not exist |
| **Logical error** | The program runs but gives a **wrong result** | `f = 0` before multiplying for a factorial; `a = 1/2 * b * h` (always 0); `Math.pow(m, 2/3)` (always 1.0) |

**Example 6.** *(ICSE 2025, Q2(vii))* John wrote this method for the surface area of a cone, A = πrl where l = √(r² + h²):
```java
double area(double r, double h)
{
    double l, a;
    a = 22.0/7*r*l;
    l = Math.sqrt(r*r+h*h);
    return a;
}
```
Specify the type of error, correct it and write the program error-free.
**Solution:** **Syntax (compile-time) error** — `l` is used before it is given a value. Calculate `l` first:
```java
double l, a;
l = Math.sqrt(r*r + h*h);
a = 22.0/7*r*l;
return a;
```

### Comments

Comments are notes for people reading the program; the compiler ignores them.
- **Single-line comment:** `// text`
- **Multi-line comment:** `/* text over several lines */`
- **Documentation comment:** `/** … */` (used to produce documentation)

### Mathematical library methods

The **Math class** is in the default package **java.lang**, so no import is needed; its methods are **static** and are called with the class name: `Math.sqrt(x)`.

| Method | Returns | Type returned | Example → result |
|---|---|---|---|
| `Math.pow(x, y)` | x raised to the power y | double | `Math.pow(2, 3)` → 8.0 |
| `Math.sqrt(x)` | square root | double | `Math.sqrt(16)` → 4.0 |
| `Math.cbrt(x)` | cube root | double | `Math.cbrt(125)` → 5.0 |
| `Math.ceil(x)` | smallest whole number **≥ x** (rounds **up**) | double | `Math.ceil(4.2)` → 5.0; `Math.ceil(-4.7)` → −4.0 |
| `Math.floor(x)` | largest whole number **≤ x** (rounds **down**) | double | `Math.floor(7.9)` → 7.0; `Math.floor(-4.7)` → −5.0 |
| `Math.round(x)` | nearest whole number (.5 goes **up**) | long (int for a float) | `Math.round(6.6)` → 7; `Math.round(-2.5)` → −2 |
| `Math.abs(a)` | absolute (positive) value | same as a | `Math.abs(-7)` → 7 |
| `Math.max(a, b)` | the larger | wider type of a, b | `Math.max(-7, -5)` → −5 |
| `Math.min(a, b)` | the smaller | wider type of a, b | `Math.min(-2.83, -5.83)` → −5.83 |
| `Math.random()` | a random number **0.0 ≤ r < 1.0** | double | `(int)(Math.random()*6) + 1` → 1 to 6 |

![Fig. 2.1 ceil, floor and round](figures/ca_ch02_fig01_ceil_floor_round.png)

**Mixing results:** `Math.round(6.6) + Math.ceil(3.4)` = 7 + 4.0 = **11.0** (a long plus a double gives a double).

**Example 7.** *(ICSE 2018, Q3(c))* Give the output of: (i) `Math.floor(-4.7)` (ii) `Math.ceil(3.4) + Math.pow(2, 3)`
**Solution:** (i) **−5.0** (ii) 4.0 + 8.0 = **12.0**.

### Writing Java expressions

| Mathematical expression | Java expression |
|---|---|
| ax⁵ + bx³ + c | `a * Math.pow(x, 5) + b * Math.pow(x, 3) + c` |
| √(b² − 4ac) | `Math.sqrt(b * b - 4 * a * c)` |
| (a + b)ˣ | `Math.pow(a + b, x)` |
| (p + q)² | `Math.pow(p + q, 2)` or `(p + q) * (p + q)` |
| ∛x + √y | `Math.cbrt(x) + Math.sqrt(y)` |
| absolute value of (x² + 2xy) | `Math.abs(x * x + 2 * x * y)` |
| √(3x + x²) ÷ (a + b) | `Math.sqrt(3 * x + x * x) / (a + b)` |
| m^(2/3) | `Math.pow(m, 2.0 / 3)` — **not** `2 / 3`, which is 0 |

**Example 8.** *(ICSE 2024, Q2(i))* Write the Java expression for the absolute value of (a + b) divided by √(a² + b²).
**Solution:** `Math.abs(a + b) / Math.sqrt(a * a + b * b)`

### Summary of the chapter

- **Operators** — unary, binary, ternary; arithmetic, relational, logical, assignment, shorthand, increment/decrement, ternary, `new`, dot.
- **Integer division** drops the fraction; `%` gives the remainder.
- **Counters** add a fixed amount; **accumulators** add varying values.
- **Prefix** changes then uses; **postfix** uses then changes. In `x op= e`, the old x is saved first.
- **Precedence:** postfix > unary > `* / %` > `+ -` > relational > equality > `&&` > `||` > `?:` > assignment.
- **print** stays on the line; **println** moves to the next.
- **Input:** initialisation, parameters, Scanner (`nextInt`, `nextDouble`, `next`, `nextLine`, `next().charAt(0)`).
- **Errors:** syntax (compiler), runtime (while running), logical (wrong answer). **Comments:** `//`, `/* */`, `/** */`.
- **Math** (java.lang): pow, sqrt, cbrt, ceil, floor (all double); round (long); abs, max, min (argument type); random (0.0 to below 1.0).

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Classify operators by form and by type and use each correctly.
2. Distinguish `/` from `%`, counters from accumulators, and prefix from postfix.
3. Apply precedence and associativity to evaluate expressions, including shorthand assignments with `++` and `--`.
4. Use print() and println() and predict output.
5. Accept input with the Scanner class and choose the right method.
6. Identify syntax, runtime and logical errors and correct them.
7. Use the Math methods and state the type each returns.
8. Convert mathematical formulas into Java expressions.

---

## 3. Detailed Section Explanations

### Section 1 — Old value first
The single most useful rule for "evaluate" questions: in `x += …`, `x *= …`, the left-hand x keeps its **old** value even if the right side changes x.

### Section 2 — Integers divide differently
`5 / 2` is 2, `1 / 2` is 0, `2 / 3` is 0. Whenever a formula has a fraction, make one operand a double (`1.0 / 2`, `2.0 / 3`).

### Section 3 — Math returns doubles
Except round (and abs, max, min, which follow their arguments), Math methods return double — so `Math.sqrt(16)` prints **4.0**.

### Section 4 — Read errors like the examiner
A missing semicolon or a variable used before assignment stops compilation (syntax); a wrong formula gives a wrong answer (logical); bad input or division by zero crashes the run (runtime).

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Operator | A symbol that performs an operation on operands. |
| Operand | A value or variable on which an operator acts. |
| Unary operator | An operator with one operand. |
| Binary operator | An operator with two operands. |
| Ternary operator | The conditional operator ?: with three operands. |
| Relational operator | Compares two values and gives true or false. |
| Logical operator | Combines conditions: &&, the OR operator, !. |
| Shorthand operator | Compound assignment such as += or *=. |
| Prefix | ++ or -- written before the variable: change, then use. |
| Postfix | ++ or -- written after the variable: use, then change. |
| Counter | A variable increased by a fixed amount to count. |
| Accumulator | A variable that adds up varying values. |
| Precedence | The order in which operators are applied. |
| Associativity | The direction of evaluation among equal-precedence operators. |
| new operator | Creates an object, allocating memory dynamically. |
| Dot operator | Accesses a member of a class or object. |
| Scanner | A java.util class for reading input during execution. |
| Syntax error | A violation of language rules found by the compiler. |
| Runtime error | An error that stops a program while it runs. |
| Logical error | An error that gives a wrong result. |
| Comment | A note in the program ignored by the compiler. |
| Math class | A java.lang class of mathematical methods. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| `&&` is a | logical operator |
| `>=` gives a | relational expression |
| `?:` is the | conditional (ternary) operator |
| `42 / 6 % 2` | 1 |
| `7 * 8 % 3` | 2 |
| `3 + 7 / 2` | 6 (division first) |
| `Math.pow(36, 6/5)` | 36.0 (6/5 is 1) |
| `Math.sqrt(Math.ceil(15.3))` | 4.0 |
| `Math.ceil(5.4) + Math.ceil(4.5)` | 11.0 |
| `Math.round(Math.ceil(-8.8))` | −8 |
| `Math.max(-7, Math.min(-5, -4))` | −5 |
| Method returning a whole number | Math.round |
| Scanner method for a sentence | nextLine() |
| Reading a char | next().charAt(0) |
| Missing semicolon | Syntax error |
| `f = 0` in a factorial | Logical error (use f = 1) |
| Package of Math | java.lang |

### 5.2 Memory aids

- **"Pre = pay first, Post = pay later"** — prefix changes before use, postfix after.
- **"Old x first"** — in `x op= …`, the old value of x is locked in.
- **Precedence ladder** — brackets → postfix/unary → `* / %` → `+ -` → comparisons → AND before OR → `?:` → assignment (last).
- **"Ceil is the ceiling (up), floor is the floor (down)"**.

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- `Math.random()` is pseudo-random: the numbers come from a formula, which is good enough for games but not for passwords.
- Java also has bitwise and shift operators (`&`, `|`, `^`, `<<`, `>>`) — excluded from the ICSE syllabus.
- Floating-point arithmetic is approximate: `Math.pow(8, 2.0/3)` prints 3.9999999999999996, not exactly 4.

---

## 6. Person Profiles

### 6.1 John Napier (1550–1617)
A Scottish mathematician who invented logarithms, which turned multiplication and powers into addition — the ideas behind methods like Math.pow that computers still use.

### 6.2 Grace Hopper (1906–1992)
An American computer scientist and naval officer who built one of the first compilers and helped create COBOL. A popular story from her team describes finding an actual moth in a computer — an early "bug".

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Order matters** — the same symbols give different answers with different precedence or prefix/postfix.
- **Types shape results** — integer and real arithmetic behave differently.
- **Programs talk to people** — Scanner brings input in, print/println send results out.

### 7.2 Real-life connections
- **Meghalaya:** a rain-gauge program for Cherrapunji (Sohra) can use an accumulator to total daily rainfall and a counter to count rainy days.
- **Shopping:** a bill uses `*` for quantity × price, `+=` to build the total and Math.round to round paise.
- **Games:** `Math.random()` rolls dice and shuffles cards.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section A** (40 marks, compulsory) = **Question 1**: twenty MCQs and **Question 2**: ten 2-mark parts; **Section B** (60 marks) = any four of six programs. Every Section A has an **"evaluate"** part and a **"write the Java expression"** part from this chapter, plus Math-method outputs; Section B programs use Scanner input and Math methods throughout.

### 8.1 Graded exercises — solutions

#### Exercise 2A — Operators and expressions

**Q1.** Evaluate `int r = k++ * 2 + --k;` when k = 3. What are r and k?
**Answer:** k++ gives 3 (k = 4); --k gives 3 (k = 3); r = 3 × 2 + 3 = 9; k = 3.

**Q2.** Evaluate `q += q++ + ++q;` when q = 10.
**Answer:** Old q = 10; q++ → 10 (q = 11); ++q → 12; q = 10 + 22 = 32.

**Q3.** Give the values of `17 % 5`, `-17 % 5` and `17 / 5`.
**Answer:** 2, −2 and 3.

**Q4.** What is the value of `5 > 3 && 2 > 4 || !(1 == 1)`?
**Answer:** false — true && false is false; !(true) is false; false OR false is false.

#### Exercise 2B — Input and Math methods

**Q5.** Give the output of `Math.round(2.5)`, `Math.round(-2.5)` and `Math.round(-2.6)`.
**Answer:** 3, −2 and −3.

**Q6.** Give the output of `Math.max(3, 7.5)` and `Math.cbrt(-27)`.
**Answer:** 7.5 and −3.0.

**Q7.** Write a statement to read a person's full name (with a space) into a String n using a Scanner sc.
**Answer:** `String n = sc.nextLine();`

**Q8.** Write the Java expression for the volume of a sphere, (4/3)πr³, using 3.14 for π.
**Answer:** `4.0 / 3 * 3.14 * Math.pow(r, 3)` — 4.0 avoids integer division.

### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(iii) (1 mark) | In a statement `c = c + (x * d + e);` which variable is an accumulator? (a) d (b) c (c) e (d) x |
| ICSE 2026, Q1(v) (1 mark) | What is the output of the statement `Math.pow(36, 6/5);`? (a) 36.0 (b) 1.0 (c) 73.71 (d) 6.0 |
| ICSE 2026, Q1(xii) (1 mark) | Assertion (A): The result of the Java expression `3 + 7/2` is 6. Reason (R): According to the hierarchy of operators in Java, addition is done first followed by division. (a) (A) is true and (R) is false. (b) (A) is false and (R) is true. (c) Both (A) and (R) are true and (R) is the correct explanation of (A). (d) Both (A) and (R) are true, but (R) is not the correct explanation of (A). |
| ICSE 2026, Q2(ii) (2 marks) | Evaluate the Java expression: `x = a * b % (++c) + (++a) + (--b);` if a = 7, b = 8, c = 2 |
| ICSE 2026, Q2(iii) (2 marks) | Write the Java expression to find the sum of cube root of x and the absolute value of y. |
| ICSE 2026, Q2(vii) (2 marks) | The following program segment calculates and displays the factorial of a number. [Example: Factorial of 5 is 1 x 2 x 3 x 4 x 5 = 120] `int p, n = 5, f = 0; for (p = n; p > 0; p--) f *= p; System.out.println(f);` Name the type of error if any; correct the statement to get the desired output. |
| ICSE 2026 Improvement, Q1(i) (1 mark) | What is the result of the expression: `7 * 8 % 3`? (a) 18 (b) 2 (c) 0 (d) 28 |
| ICSE 2026 Improvement, Q1(xiv) (1 mark) | Fill in the blank in the following java statement. `Scanner ob = new Scanner(System.in); char ch = ______;` (a) `ob.nextLine()` (b) `ob.next().charAt()` (c) `ob.next().charAt(0)` (d) `ob.next().charat(0)` |
| ICSE 2026 Improvement, Q1(xviii) (1 mark) | Assertion (A): Math methods are a part of the package java.lang. Reason (R): Math method should be prefixed with the class name. (a) (A) is true and (R) is false. (b) (A) is false and (R) is true. (c) Both (A) and (R) are true. (d) Both (A) and (R) are false. |
| ICSE 2026 Improvement, Q2(i) (2 marks) | Evaluate the following java expression: `x -= x++ + ++x - x + x;` when x = 7 |
| ICSE 2026 Improvement, Q2(ii) (2 marks) | Sam was asked to calculate the value of m raised to the power of 2/3. She wrote the following code and the code resulted in 1.0 irrespective of the value of m. State the type of the error, correct the code to obtain the correct answer: `System.out.println(Math.pow(m, 2/3));` |
| ICSE 2026 Improvement, Q2(iii) (2 marks) | Write the java expression for the following: Assign the sum of square root of M and the square of N to an appropriate variable. |
| ICSE 2025, Q1(iv) (1 mark) | The output of `42/6%2` is: (a) 1 (b) 10 (c) 2 (d) 0 |
| ICSE 2025, Q1(viii) (1 mark) | The output of `Math.max(-7, Math.min(-5, -4))` is: (a) –5 (b) –4 (c) –7 (d) error |
| ICSE 2025, Q2(i) (2 marks) | Write the java expression to find the product of square root of P and the square root of Q using the methods of Math class. |
| ICSE 2025, Q2(vii) (2 marks) | John was asked to write a Java code to calculate the surface area of a cone, A = πrl where l = √(r² + h²). He wrote: `class area { double area(double r, double h) { double l, a; a = 22.0/7*r*l; l = Math.sqrt(r*r+h*h); return a; } }` Specify the type of the error in the above program, correct and write the program to be error free. |
| ICSE 2025 Improvement, Q1(iv) (1 mark) | The Math method which returns int value is: (a) round() (b) cbrt() (c) ceil() (d) random() |
| ICSE 2025 Improvement, Q1(vii) (1 mark) | What is the output of the code snippet given below? `int lives = 5; System.out.print(lives--); System.out.print(lives);` (a) 4 3 (b) 5 4 (c) 5 3 (d) 4 4 |
| ICSE 2025 Improvement, Q1(xvi) (1 mark) | `System.out.println(Math.round(Math.ceil(-8.8)));` will result in: (a) 8.0 (b) –8.0 (c) –9 (d) –8 |
| ICSE 2025 Improvement, Q2(i) (2 marks) | Write Java expression for the following: x¹⁰ + y¹⁰ |
| ICSE 2025 Improvement, Q2(ii) (2 marks) | Evaluate the given expression when x = 4: `x *= --x + x-- + x;` |
| ICSE 2025 specimen, Q1(iv) (1 mark) | Identify the operator that gets the highest precedence while evaluating the given expression: `a + b % c * d - e` (a) + (b) % (c) – (d) * |
| ICSE 2025 specimen, Q1(vi) (1 mark) | The output of the following code is: `System.out.println(Math.ceil(6.4)+Math.floor(-1-2));` (a) 3.0 (b) 4 (c) 3 (d) 4.0 |
| ICSE 2025 specimen, Q1(xvii) (1 mark) | A student executes the following code to increase the value of a variable 'x' by 2. He has written the following statement, which is incorrect: `x = +2;` What will be the correct statement? A. `x += 2;` B. `x = 2;` C. `x = x + 2;` (a) Only A (b) Only C (c) All the three (d) Both A and C |
| ICSE 2025 specimen, Q2(ii) (2 marks) | Evaluate the given expression when the value of a = 2 and b = 3: `b *= a++ - ++b + ++a; System.out.println("a= " + a); System.out.println("b= " + b);` |
| ICSE 2025 specimen, Q2(iv) (2 marks) | Write the Java expression for ∛x + √y. |
| ICSE 2024, Q1(viii) (1 mark) | What is the output of `Math.ceil(5.4)+Math.ceil(4.5)`? (a) 10.0 (b) 11.0 (c) 12.0 (d) 9.0 |
| ICSE 2024, Q1(xx) (1 mark) | Which of the following mathematical methods returns only an integer? (a) Math.ceil(n) (b) Math.sqrt(n) (c) Math.floor(n) (d) Math.round(n) |
| ICSE 2024, Q2(i) (2 marks) | Write Java expression for: [the absolute value of (a + b), divided by √(a² + b²)] |
| ICSE 2024, Q2(ii) (2 marks) | Evaluate the expression when x is 4: `x += x++ * ++x % 2;` |
| ICSE 2024 specimen, Q1(ii) (1 mark) | The expression which uses `>=` operator is known as: (a) relational (b) logical (c) arithmetic (d) assignment |
| ICSE 2024 specimen, Q1(iii) (1 mark) | Ternary operator is a: (a) logical operator (b) arithmetic operator (c) relational operator (d) conditional operator |
| ICSE 2024 specimen, Q1(vi) (1 mark) | The method of Scanner class used to accept a double value is: (a) nextInt() (b) nextDouble() (c) next() (d) nextInteger() |
| ICSE 2024 specimen, Q1(viii) (1 mark) | The output of `Math.round(6.6) + Math.ceil(3.4)` is: (a) 9.0 (b) 11.0 (c) 10.0 (d) 11 |
| ICSE 2024 specimen, Q1(ix) (1 mark) | Name the type of error, if any in the following statement: `System.out.print("HELLO")` (a) logical (b) no error (c) runtime (d) syntax |
| ICSE 2024 specimen, Q2(i) (2 marks) | Write the Java expression for (p + q)² |
| ICSE 2024 specimen, Q2(ii) (2 marks) | Evaluate the expression when the value of x = 2: `x = x++ + ++x + x;` |
| ICSE 2024 specimen, Q2(iv) (2 marks) | Sam executes the following program segment and the answer displayed is zero irrespective of any non zero values are given. Name the error. How the program can be modified to get the correct answer? `void triangle(double b, double h) { double a; a = 1/2 * b * h; System.out.println("Area=" + a); }` |
| ICSE 2023, Q1(ii) (1 mark) | Identify the type of operator `&&`: (a) ternary (b) unary (c) logical (d) relational |
| ICSE 2023, Q1(iii) (1 mark) | The Scanner class method used to accept words with space: (a) next() (b) nextLine() (c) Next() (d) nextString() |
| ICSE 2023, Q1(v) (1 mark) | What value will `Math.sqrt(Math.ceil(15.3))` return? (a) 16.0 (b) 16 (c) 4.0 (d) 5.0 |
| ICSE 2023, Q1(xv) (1 mark) | Missing a semicolon in a statement is what type of error? (a) Logical (b) Syntax (c) Runtime (d) No error |
| ICSE 2023, Q2(i) (2 marks) | Write the Java expression for (a + b)ˣ. |
| ICSE 2023, Q2(ii) (2 marks) | Evaluate the expression when the value of x = 4: `x *= --x + x++ + x;` |
| ICSE 2020, Q1(e) (2 marks) | What is an operator? Name any two types of operators used in Java. |
| ICSE 2020, Q3(a) (2 marks) | Write a Java expression for the following: √(b² − 4ac) |
| ICSE 2020, Q3(b) (2 marks) | Evaluate the following if the value of x = 7, y = 5: `x += x++ + x + ++y` |
| ICSE 2020, Q3(i) (2 marks) | Give the output of the following: (i) `Math.pow(36, 0.5) + Math.cbrt(125)` (ii) `Math.ceil(4.2) + Math.floor(7.9)` |
| ICSE 2019, Q1(b) (2 marks) | Write a difference between unary and binary operator. |
| ICSE 2019, Q2(c) (2 marks) | What are the various types of errors in Java? |
| ICSE 2019, Q3(a) (2 marks) | Write a Java expression for the following: [the absolute value of (x² + 2xy)] |
| ICSE 2019, Q3(f) (2 marks) | Give the output of the following: `Math.sqrt(Math.max(9, 16))` |
| ICSE 2019, Q3(h) (2 marks) | Evaluate the following expression if the value of x = 2, y = 3 and z = 1: `v = x + --z + y++ + y` |
| ICSE 2018, Q2(c) (2 marks) | `System.out.print("BEST "); System.out.println("OF LUCK");` Choose the correct option for the output of the above statements: (i) BEST OF LUCK (on one line) (ii) BEST and OF LUCK on two lines |
| ICSE 2018, Q3(a) (2 marks) | Write a Java expression for the following: √(3x + x²) ÷ (a + b) |
| ICSE 2018, Q3(b) (2 marks) | What is the value of y after evaluating the expression given below? `y += ++y + y-- + --y;` when `int y = 8` |
| ICSE 2018, Q3(c) (2 marks) | Give the output of the following: (i) `Math.floor(-4.7)` (ii) `Math.ceil(3.4) + Math.pow(2, 3)` |
| ICSE 2017, Q1(b) (2 marks) | Name the operators listed below: (i) `<` (ii) `++` (iii) `&&` (iv) `?:` |
| ICSE 2017, Q1(d) (2 marks) | Write one difference between `/` and `%` operator. |
| ICSE 2017, Q3(a) (2 marks) | Write a Java expression for the following: ax⁵ + bx³ + c |
| ICSE 2017, Q3(b) (2 marks) | What is the value of x1 if x = 5? `x1 = ++x - x++ + --x` |
| ICSE 2017, Q3(g) (2 marks) | What are the values stored in variables r1 and r2: (i) `double r1 = Math.abs(Math.min(-2.83, -5.83));` (ii) `double r2 = Math.sqrt(Math.floor(16.3));` |
| ICSE 2017, Q3(j) (2 marks) | What is the difference between the Scanner class functions next() and nextLine()? |

**Solutions**

**2026 Q1(iii).** **(b) c** — c adds up the varying values of x*d + e. *(Worked answer.)*

**2026 Q1(v).** **(a) 36.0** — `6/5` is integer division (1), so the value is 36¹ = 36.0. *(Worked answer.)*

**2026 Q1(xii).** **(a) (A) is true and (R) is false** — `7/2` is done first (3), then 3 + 3 = 6; division has higher precedence than addition. *(Worked answer.)*

**2026 Q2(ii).** a × b % (++c) = 56 % 3 = **2** (c = 3); ++a = **8**; --b = **7**. **x = 2 + 8 + 7 = 17.** *(Worked answer.)*

**2026 Q2(iii).** `Math.cbrt(x) + Math.abs(y)` *(Worked answer.)*

**2026 Q2(vii).** **Logical error** — f starts at 0, so every product is 0. Correct: `int p, n = 5, f = 1;` (the output becomes 120). *(Worked answer.)*

**2026 Improvement Q1(i).** **(b) 2** — `*` and `%` are applied left to right: 56 % 3 = 2. *(Worked answer.)*

**2026 Improvement Q1(xiv).** **(c) `ob.next().charAt(0)`.** *(Worked answer.)*

**2026 Improvement Q1(xviii).** **(c) Both (A) and (R) are true** — Math is in java.lang, and its static methods are called with the class name, e.g. `Math.sqrt(x)`. *(Worked answer.)*

**2026 Improvement Q2(i).** Old x = **7**. `x++` → **7** (x = 8); `++x` → **9** (x = 9); `- x` → 9; `+ x` → 9. Right side = 7 + 9 − 9 + 9 = 16. **x = 7 − 16 = −9.** *(Worked answer.)*

**2026 Improvement Q2(ii).** **Logical error** — `2/3` is integer division, giving 0, and m⁰ = 1.0. Correct: `System.out.println(Math.pow(m, 2.0/3));` *(Worked answer.)*

**2026 Improvement Q2(iii).** `double s = Math.sqrt(M) + N * N;` (or `Math.pow(N, 2)`). *(Worked answer.)*

**2025 Q1(iv).** **(a) 1** — 42/6 = 7; 7 % 2 = 1.

**2025 Q1(viii).** **(a) –5** — Math.min(−5, −4) = −5; Math.max(−7, −5) = −5. (The scheme also accepted (d).)

**2025 Q2(i).** `Math.sqrt(P) * Math.sqrt(Q)` (also accepted: `Math.pow(P, 1.0/2) * Math.pow(Q, 1.0/2)`, `Math.sqrt(P * Q)`).

**2025 Q2(vii).** **Syntax (compile-time) error** — l is used before it is assigned (also accepted as logical). Correct:
```java
class area
{
    double area(double r, double h)
    {
        double l, a;
        l = Math.sqrt(r*r + h*h);
        a = 22.0/7*r*l;
        return a;
    }
}
```

**2025 Improvement Q1(iv).** **(a) round()** — it returns a whole number (int for a float argument, long for a double); the others return double. *(Worked answer.)*

**2025 Improvement Q1(vii).** **(b) 5 4** — the output is `54`: postfix prints 5, then lives is 4. *(Worked answer.)*

**2025 Improvement Q1(xvi).** **(d) –8** — Math.ceil(−8.8) = −8.0; Math.round(−8.0) = −8. *(Worked answer.)*

**2025 Improvement Q2(i).** `Math.pow(x, 10) + Math.pow(y, 10)` *(Worked answer.)*

**2025 Improvement Q2(ii).** Old x = **4**. `--x` → **3** (x = 3); `x--` → **3** (x = 2); `x` → **2**. **x = 4 × (3 + 3 + 2) = 32.** *(Worked answer.)*

**2025 specimen Q1(iv).** **(b) %.**

**2025 specimen Q1(vi).** **(d) 4.0** — 7.0 + (−3.0).

**2025 specimen Q1(xvii).** **(d) Both A and C.**

**2025 specimen Q2(ii).** **a = 4, b = 6** — old b = 3; a++ → 2 (a = 3); ++b → 4; ++a → 4 (a = 4); b = 3 × (2 − 4 + 4) = 6.

**2025 specimen Q2(iv).** `Math.cbrt(x) + Math.sqrt(y)`

**2024 Q1(viii).** **(b) 11.0** — 6.0 + 5.0.

**2024 Q1(xx).** **(d) Math.round(n).**

**2024 Q2(i).** `Math.abs(a+b) / Math.sqrt(a*a+b*b)`

**2024 Q2(ii).** **x = 4** — old x = 4; x++ → 4 (x = 5); ++x → 6; 4 × 6 % 2 = 24 % 2 = 0; x = 4 + 0 = 4.

**2024 specimen Q1(ii).** **(a) relational.** *(Worked answer.)*

**2024 specimen Q1(iii).** **(d) conditional operator.** *(Worked answer.)*

**2024 specimen Q1(vi).** **(b) nextDouble().** *(Worked answer.)*

**2024 specimen Q1(viii).** **(b) 11.0** — Math.round(6.6) = 7 (a long) + 4.0 = 11.0 (a double). *(Worked answer.)*

**2024 specimen Q1(ix).** **(d) syntax** — the semicolon is missing. *(Worked answer.)*

**2024 specimen Q2(i).** `Math.pow(p + q, 2)` or `(p + q) * (p + q)` *(Worked answer.)*

**2024 specimen Q2(ii).** `x++` → **2** (x = 3); `++x` → **4** (x = 4); `x` → **4**. **x = 2 + 4 + 4 = 10.** *(Worked answer.)*

**2024 specimen Q2(iv).** **Logical error** — `1/2` is integer division (0), so the area is always 0. Correct: `a = 1.0/2 * b * h;` (or `a = 0.5 * b * h;`). *(Worked answer.)*

**2023 Q1(ii).** **(c) logical.**

**2023 Q1(iii).** **(b) nextLine().**

**2023 Q1(v).** **(c) 4.0** — Math.ceil(15.3) = 16.0; √16.0 = 4.0.

**2023 Q1(xv).** **(b) Syntax.** *(Worked answer.)*

**2023 Q2(i).** `Math.pow(a + b, x)`

**2023 Q2(ii).** **x = 40** — x = x × (--x + x++ + x) = 4 × (3 + 3 + 4).

**2020 Q1(e).** An **operator** is a **symbol that performs an operation on operands** (e.g. + adds). Types (any two): **arithmetic, relational, logical, assignment**, increment/decrement, ternary. *(Worked answer.)*

**2020 Q3(a).** `Math.sqrt(b*b - 4*a*c)` *(Worked answer.)*

**2020 Q3(b).** Old x = **7**. `x++` → **7** (x = 8); `x` → **8**; `++y` → **6**. **x = 7 + (7 + 8 + 6) = 28.** *(Worked answer.)*

**2020 Q3(i).** (i) 6.0 + 5.0 = **11.0** (ii) 5.0 + 7.0 = **12.0** *(Worked answer.)*

**2019 Q1(b).** A **unary** operator works on a **single operand**; a **binary** operator works on **two operands**.

**2019 Q2(c).** **Syntax error, logical error, runtime error.**

**2019 Q3(a).** `Math.abs(x*x + 2*x*y)` or `Math.abs(Math.pow(x, 2) + 2*x*y)`

**2019 Q3(f).** **4.0**

**2019 Q3(h).** **v = 9** — 2 + 0 + 3 + 4 (--z gives 0; y++ gives 3, then y is 4).

**2018 Q2(c).** **(i) BEST OF LUCK** — print() does not move to a new line.

**2018 Q3(a).** `Math.sqrt(3*x + x*x) / (a + b)` or `Math.sqrt(3*x + Math.pow(x, 2)) / (a + b)`

**2018 Q3(b).** **33** — 8 + (9 + 9 + 7).

**2018 Q3(c).** (i) **−5.0** (ii) **12.0**

**2017 Q1(b).** (i) **relational** (ii) **increment** (unary arithmetic) (iii) **logical** (iv) **ternary (conditional)**. *(Worked answer.)*

**2017 Q1(d).** `/` gives the **quotient** of a division (`7 / 2` = 3); `%` gives the **remainder** (`7 % 2` = 1). *(Worked answer.)*

**2017 Q3(a).** `a * Math.pow(x, 5) + b * Math.pow(x, 3) + c` *(Worked answer.)*

**2017 Q3(b).** `++x` → **6**; `x++` → **6** (x = 7); `--x` → **6**. **x1 = 6 − 6 + 6 = 6.** *(Worked answer.)*

**2017 Q3(g).** (i) **r1 = 5.83** — Math.min gives −5.83, Math.abs makes it 5.83. (ii) **r2 = 4.0** — Math.floor(16.3) = 16.0, √16.0 = 4.0. *(Worked answer.)*

**2017 Q3(j).** **next()** reads **one word** (up to a space); **nextLine()** reads the **whole line, including spaces**. *(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Evaluate `s /= 3; s %= 4;` when `int s = 20`.
**Answer:** s = 20 / 3 = 6; then 6 % 4 = 2.

**Q2.** (2 marks) Give the output of `Math.ceil(-4.2)`, `Math.floor(4.9)` and `Math.abs(-7.5)`.
**Answer:** −4.0, 4.0 and 7.5.

**Q3.** (2 marks) Write the Java expression for the simple interest PRT ÷ 100 and for the hypotenuse √(a² + b²).
**Answer:** `p * r * t / 100` and `Math.sqrt(a * a + b * b)`.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 2 marks | Evaluate `x op= …` with `++`/`--` (old value first) | 8.2, Section 1 |
| 2 marks | Write the Java expression (pow, sqrt, cbrt, abs) | 8.2, Section 1 |
| MCQ / 2 marks | Outputs of ceil, floor, round, max, min, pow; integer division (`6/5`, `2/3`, `1/2`) | 8.2, Fig. 2.1 |
| MCQ | Type of operator; precedence; Scanner methods; type of error | 8.2, 5.1 |

---

## 9. MCQs with Explanations

### Operators and their types (Q1–Q14)

**Q1.** An operator that works on a single operand is
- (a) unary
- (b) binary
- (c) ternary
- (d) relational

**Answer:** (a) unary
**Explanation:** e.g. ++a, -a, !flag.

**Q2.** The operator `&&` is a
- (a) ternary operator
- (b) unary operator
- (c) logical operator
- (d) relational operator

**Answer:** (c) logical operator
**Explanation:** 2023 MS.

**Q3.** An expression using `>=` is a
- (a) logical expression
- (b) assignment expression
- (c) arithmetic expression
- (d) relational expression

**Answer:** (d) relational expression
**Explanation:** It compares two values.

**Q4.** The ternary operator is also called the
- (a) logical operator
- (b) arithmetic operator
- (c) relational operator
- (d) conditional operator

**Answer:** (d) conditional operator
**Explanation:** ?: chooses one of two values.

**Q5.** In `c = c + (x * d + e);` the accumulator is
- (a) c
- (b) d
- (c) e
- (d) x

**Answer:** (a) c
**Explanation:** It adds up varying values.

**Q6.** A variable increased by 1 each time to count items is a
- (a) accumulator
- (b) counter
- (c) constant
- (d) literal

**Answer:** (b) counter
**Explanation:** c++ or c = c + 1.

**Q7.** The operator that creates an object by allocating memory is
- (a) the dot operator
- (b) new
- (c) ?:
- (d) %

**Answer:** (b) new
**Explanation:** Scanner sc = new Scanner(System.in);

**Q8.** In `Math.sqrt(x)`, the dot operator is used to
- (a) multiply
- (b) end a statement
- (c) invoke a member of the Math class
- (d) compare values

**Answer:** (c) invoke a member of the Math class
**Explanation:** It accesses methods and variables.

**Q9.** The value of `17 % 5` is
- (a) 3
- (b) 3.4
- (c) 2
- (d) 5

**Answer:** (c) 2
**Explanation:** % gives the remainder.

**Q10.** With a negative first operand, the remainder `-17 % 5` works out to
- (a) 2
- (b) 3
- (c) −3
- (d) −2

**Answer:** (d) −2
**Explanation:** The sign follows the first operand.

**Q11.** The correct way to increase x by 2 is
- (a) only x += 2;
- (b) only x = x + 2;
- (c) all of x += 2; x = 2; x = x + 2;
- (d) both x += 2; and x = x + 2;

**Answer:** (d) both x += 2; and x = x + 2;
**Explanation:** 2025 specimen MS; x = +2 just stores 2.

**Q12.** `(5 > 3) || (10 / 0 > 1)` gives
- (a) an error
- (b) false
- (c) true
- (d) 0

**Answer:** (c) true
**Explanation:** Short-circuit: the right side is never evaluated.

**Q13.** The value of `true && !false || false` is
- (a) true
- (b) false
- (c) an error
- (d) 1

**Answer:** (a) true
**Explanation:** true && true = true; true OR false = true.

**Q14.** Which of these is a shorthand (compound) assignment operator?
- (a) ==
- (b) *=
- (c) &&
- (d) !=

**Answer:** (b) *=
**Explanation:** x *= 3 means x = x * 3.

### Precedence and arithmetic (Q15–Q28)

**Q15.** The output of `42/6%2` is
- (a) 1
- (b) 10
- (c) 2
- (d) 0

**Answer:** (a) 1
**Explanation:** Left to right: 7 % 2.

**Q16.** The result of `7 * 8 % 3` is
- (a) 18
- (b) 2
- (c) 0
- (d) 28

**Answer:** (b) 2
**Explanation:** 56 % 3.

**Q17.** The value of `3 + 7/2` is
- (a) 5
- (b) 6.5
- (c) 6
- (d) 5.0

**Answer:** (c) 6
**Explanation:** 7/2 = 3 first.

**Q18.** In `a + b % c * d - e`, the operator applied first is
- (a) +
- (b) *
- (c) −
- (d) %

**Answer:** (d) %
**Explanation:** 2025 specimen MS.

**Q19.** The value of `5 + 3 * 2 - 4 / 2` is
- (a) 9
- (b) 14
- (c) 6
- (d) 7

**Answer:** (a) 9
**Explanation:** 5 + 6 − 2.

**Q20.** The value of `10 % 3 + 10 / 3` is
- (a) 3
- (b) 4
- (c) 4.33
- (d) 5

**Answer:** (b) 4
**Explanation:** 1 + 3.

**Q21.** The value of `15 / 4 * 4 + 15 % 4` is
- (a) 16
- (b) 12
- (c) 15
- (d) 18

**Answer:** (c) 15
**Explanation:** 3 × 4 + 3.

**Q22.** `(double)(7 / 2)` gives
- (a) 3.5
- (b) 4.0
- (c) 3
- (d) 3.0

**Answer:** (d) 3.0
**Explanation:** 7/2 = 3 before the cast.

**Q23.** After `int y = 6; y *= 2 + 3;` y is
- (a) 15
- (b) 30
- (c) 17
- (d) 12

**Answer:** (b) 30
**Explanation:** y = 6 × (2 + 3).

**Q24.** After `int n = 10; n -= 3 * 2;` n is
- (a) 4
- (b) 14
- (c) 7
- (d) 16

**Answer:** (a) 4
**Explanation:** 10 − 6.

**Q25.** Among these, the operator with the lowest precedence is
- (a) *
- (b) +
- (c) &&
- (d) =

**Answer:** (d) =
**Explanation:** Assignment is applied last.

**Q26.** The associativity of the assignment operator is
- (a) left to right
- (b) right to left
- (c) top to bottom
- (d) random

**Answer:** (b) right to left
**Explanation:** a = b = 5 assigns b first.

**Q27.** `Math.pow(36, 6/5)` gives
- (a) 36.0
- (b) 1.0
- (c) 73.71
- (d) 6.0

**Answer:** (a) 36.0
**Explanation:** 6/5 is 1.

**Q28.** `a = 1/2 * b * h;` always gives 0 because
- (a) b is negative
- (b) 1/2 is integer division, which is 0
- (c) * is wrong
- (d) h is not declared

**Answer:** (b) 1/2 is integer division, which is 0
**Explanation:** Use 1.0/2 (2024 specimen).

### Prefix and postfix (Q29–Q40)

**Q29.** `int lives = 5; System.out.print(lives--); System.out.print(lives);` displays
- (a) 54
- (b) 43
- (c) 53
- (d) 44

**Answer:** (a) 54
**Explanation:** Postfix uses 5, then lives is 4.

**Q30.** After `int a = 10; int b = a++ + ++a;` b is
- (a) 21
- (b) 20
- (c) 22
- (d) 23

**Answer:** (c) 22
**Explanation:** 10 + 12.

**Q31.** After `int x = 5; x = x++ * 2;` x is
- (a) 12
- (b) 11
- (c) 6
- (d) 10

**Answer:** (d) 10
**Explanation:** 5 × 2 is assigned after the increment.

**Q32.** `x *= --x + x++ + x;` with x = 4 gives
- (a) 40
- (b) 36
- (c) 44
- (d) 30

**Answer:** (a) 40
**Explanation:** 4 × (3 + 3 + 4) — 2023 MS.

**Q33.** `y += ++y + y-- + --y;` with y = 8 gives
- (a) 24
- (b) 33
- (c) 35
- (d) 32

**Answer:** (b) 33
**Explanation:** 8 + (9 + 9 + 7) — 2018 MS.

**Q34.** `x += x++ * ++x % 2;` with x = 4 gives
- (a) 28
- (b) 5
- (c) 4
- (d) 0

**Answer:** (c) 4
**Explanation:** 4 + (24 % 2) — 2024 MS.

**Q35.** `x = x++ + ++x + x;` with x = 2 gives
- (a) 8
- (b) 9
- (c) 11
- (d) 10

**Answer:** (d) 10
**Explanation:** 2 + 4 + 4.

**Q36.** `v = x + --z + y++ + y` with x = 2, y = 3, z = 1 gives
- (a) 9
- (b) 10
- (c) 8
- (d) 7

**Answer:** (a) 9
**Explanation:** 2 + 0 + 3 + 4 — 2019 MS.

**Q37.** After `int k = 5; k += k++;` k is
- (a) 11
- (b) 10
- (c) 6
- (d) 12

**Answer:** (b) 10
**Explanation:** Old k (5) + 5.

**Q38.** After `int i = 3; i = i++ + i++;` i is
- (a) 8
- (b) 6
- (c) 7
- (d) 9

**Answer:** (c) 7
**Explanation:** 3 + 4.

**Q39.** `x -= x++ + ++x - x + x;` with x = 7 gives
- (a) −9
- (b) 9
- (c) −2
- (d) 16

**Answer:** (a) −9
**Explanation:** 7 − (7 + 9 − 9 + 9).

**Q40.** After `int p = 4; int q = p-- - --p;` the values are
- (a) q = 0, p = 3
- (b) q = 1, p = 2
- (c) q = 2, p = 2
- (d) q = 2, p = 3

**Answer:** (c) q = 2, p = 2
**Explanation:** 4 − 2; p ends at 2.

### Input, output and errors (Q41–Q52)

**Q41.** The Scanner method used to accept words with spaces is
- (a) next()
- (b) nextLine()
- (c) nextWord()
- (d) nextString()

**Answer:** (b) nextLine()
**Explanation:** 2023 MS.

**Q42.** The Scanner method used to accept a double value is
- (a) nextInt()
- (b) next()
- (c) nextDouble()
- (d) nextInteger()

**Answer:** (c) nextDouble()
**Explanation:** 2024 specimen.

**Q43.** To read a single character into ch using Scanner ob, write
- (a) ob.nextLine()
- (b) ob.next().charAt()
- (c) ob.charAt(0)
- (d) ob.next().charAt(0)

**Answer:** (d) ob.next().charAt(0)
**Explanation:** First character of the next word.

**Q44.** The Scanner class belongs to the package
- (a) java.util
- (b) java.lang
- (c) java.io
- (d) java.awt

**Answer:** (a) java.util
**Explanation:** import java.util.*;

**Q45.** Giving values to a method when it is called, in BlueJ, is input through
- (a) initialisation
- (b) parameters
- (c) Scanner
- (d) comments

**Answer:** (b) parameters
**Explanation:** Data supplied at the time of execution.

**Q46.** Missing a semicolon in a statement is a
- (a) logical error
- (b) runtime error
- (c) syntax error
- (d) no error

**Answer:** (c) syntax error
**Explanation:** Found by the compiler.

**Q47.** Dividing an integer by zero during a run causes a
- (a) syntax error
- (b) logical error
- (c) comment
- (d) runtime error

**Answer:** (d) runtime error
**Explanation:** The program stops abnormally.

**Q48.** A factorial program with `f = 0` printing 0 has a
- (a) logical error
- (b) syntax error
- (c) runtime error
- (d) no error

**Answer:** (a) logical error
**Explanation:** It runs but gives a wrong result.

**Q49.** `System.out.print("BEST "); System.out.println("OF LUCK");` prints
- (a) BEST and OF LUCK on two lines
- (b) nothing
- (c) OF LUCK BEST
- (d) BEST OF LUCK on one line

**Answer:** (d) BEST OF LUCK on one line
**Explanation:** print() stays on the line — 2018 MS.

**Q50.** A multi-line comment is written as
- (a) // … //
- (b) <!-- … -->
- (c) /* … */
- (d) ## … ##

**Answer:** (c) /* … */
**Explanation:** // is for one line.

**Q51.** Using a variable before giving it a value is a
- (a) runtime error
- (b) syntax (compile-time) error
- (c) logical error only
- (d) comment

**Answer:** (b) syntax (compile-time) error
**Explanation:** 2025 cone question.

**Q52.** Data written into the program before it runs is supplied by
- (a) initialisation
- (b) parameters
- (c) the Scanner class
- (d) the keyboard

**Answer:** (a) initialisation
**Explanation:** e.g. int a = 10;

### Mathematical library methods (Q53–Q68)

**Q53.** The Math class belongs to the package
- (a) java.util
- (b) java.io
- (c) java.lang
- (d) java.math.util

**Answer:** (c) java.lang
**Explanation:** No import needed.

**Q54.** `Math.sqrt(Math.ceil(15.3))` returns
- (a) 16.0
- (b) 16
- (c) 5.0
- (d) 4.0

**Answer:** (d) 4.0
**Explanation:** √16.0 — 2023 MS.

**Q55.** `Math.ceil(5.4) + Math.ceil(4.5)` is
- (a) 10.0
- (b) 11.0
- (c) 12.0
- (d) 9.0

**Answer:** (b) 11.0
**Explanation:** 6.0 + 5.0 — 2024 MS.

**Q56.** The Math method that returns a whole-number type is
- (a) Math.round()
- (b) Math.ceil()
- (c) Math.floor()
- (d) Math.sqrt()

**Answer:** (a) Math.round()
**Explanation:** It returns long (int for a float).

**Q57.** `Math.round(Math.ceil(-8.8))` gives
- (a) 8.0
- (b) −8.0
- (c) −9
- (d) −8

**Answer:** (d) −8
**Explanation:** ceil gives −8.0; round gives −8.

**Q58.** `Math.ceil(6.4) + Math.floor(-1-2)` gives
- (a) 3.0
- (b) 4
- (c) 3
- (d) 4.0

**Answer:** (d) 4.0
**Explanation:** 7.0 − 3.0.

**Q59.** `Math.max(-7, Math.min(-5, -4))` gives
- (a) −5
- (b) −4
- (c) −7
- (d) 5

**Answer:** (a) −5
**Explanation:** max(−7, −5).

**Q60.** `Math.floor(-4.7)` gives
- (a) −4.0
- (b) −5.0
- (c) −4.7
- (d) 4.0

**Answer:** (b) −5.0
**Explanation:** Rounds down.

**Q61.** `Math.round(4.5)` and `Math.round(4.49)` give
- (a) 4 and 4
- (b) 5 and 5
- (c) 5 and 4
- (d) 4.5 and 4.49

**Answer:** (c) 5 and 4
**Explanation:** .5 rounds up.

**Q62.** `Math.pow(36, 0.5) + Math.cbrt(125)` gives
- (a) 11.0
- (b) 11
- (c) 41.0
- (d) 23.0

**Answer:** (a) 11.0
**Explanation:** 6.0 + 5.0.

**Q63.** `Math.abs(Math.min(-2.83, -5.83))` gives
- (a) −5.83
- (b) 2.83
- (c) 5.83
- (d) −2.83

**Answer:** (c) 5.83
**Explanation:** min is −5.83; abs makes it positive.

**Q64.** `Math.random()` returns a value r such that
- (a) 0 ≤ r ≤ 1
- (b) 1 ≤ r ≤ 10
- (c) −1 < r < 1
- (d) 0.0 ≤ r < 1.0

**Answer:** (d) 0.0 ≤ r < 1.0
**Explanation:** Never exactly 1.0.

**Q65.** `Math.max(-3.5, -3)` gives
- (a) −3
- (b) −3.5
- (c) −3.0
- (d) 3.5

**Answer:** (c) −3.0
**Explanation:** The wider type (double) is returned.

**Q66.** `Math.pow(2, -1)` gives
- (a) −2.0
- (b) 0.5
- (c) 2.0
- (d) −0.5

**Answer:** (b) 0.5
**Explanation:** 2⁻¹ = ½.

**Q67.** `System.out.println("A " + Math.sqrt(25) + Math.cbrt(8));` prints
- (a) A 7.0
- (b) A 5.02.0
- (c) A 7
- (d) A 52

**Answer:** (b) A 5.02.0
**Explanation:** After a string, + joins text.

**Q68.** `Math.pow(m, 2/3)` always gives 1.0 because
- (a) m is negative
- (b) pow cannot take fractions
- (c) 2/3 is integer division, which is 0
- (d) of a syntax error

**Answer:** (c) 2/3 is integer division, which is 0
**Explanation:** Use 2.0/3 (2026 Improvement).

### Java expressions (Q69–Q76)

**Q69.** The Java expression for √(b² − 4ac) is
- (a) Math.sqrt(b2 - 4ac)
- (b) Math.sqrt(b*b - 4*a*c)
- (c) sqrt(b*b - 4*a*c)
- (d) Math.sqrt b*b - 4*a*c

**Answer:** (b) Math.sqrt(b*b - 4*a*c)
**Explanation:** Every product needs *.

**Q70.** The Java expression for (a + b)ˣ is
- (a) Math.pow(a + b, x)
- (b) Math.pow(x, a + b)
- (c) (a + b) ^ x
- (d) a + b * x

**Answer:** (a) Math.pow(a + b, x)
**Explanation:** 2023 MS.

**Q71.** The Java expression for ∛x + √y is
- (a) Math.sqrt(x) + Math.cbrt(y)
- (b) Math.pow(x, 3) + Math.pow(y, 2)
- (c) Math.cbrt(x + y)
- (d) Math.cbrt(x) + Math.sqrt(y)

**Answer:** (d) Math.cbrt(x) + Math.sqrt(y)
**Explanation:** 2025 specimen MS.

**Q72.** The Java expression for ax⁵ + bx³ + c is
- (a) a*Math.pow(x, 5) + b*Math.pow(x, 3) + c
- (b) ax5 + bx3 + c
- (c) Math.pow(a*x, 5) + Math.pow(b*x, 3) + c
- (d) a*x*5 + b*x*3 + c

**Answer:** (a) a*Math.pow(x, 5) + b*Math.pow(x, 3) + c
**Explanation:** Only x is raised to the power.

**Q73.** The product of the square roots of P and Q is
- (a) Math.sqrt(P + Q)
- (b) Math.sqrt(P) * Math.sqrt(Q)
- (c) Math.pow(P*Q, 2)
- (d) Math.sqrt(P) + Math.sqrt(Q)

**Answer:** (b) Math.sqrt(P) * Math.sqrt(Q)
**Explanation:** 2025 MS.

**Q74.** The sum of the cube root of x and the absolute value of y is
- (a) Math.cbrt(x) * Math.abs(y)
- (b) Math.sqrt(x) + Math.abs(y)
- (c) Math.cbrt(x) + Math.abs(y)
- (d) Math.cbrt(x + y)

**Answer:** (c) Math.cbrt(x) + Math.abs(y)
**Explanation:** 2026 board.

**Q75.** The expression x¹⁰ + y¹⁰ in Java is
- (a) x^10 + y^10
- (b) Math.pow(x + y, 10)
- (c) x*10 + y*10
- (d) Math.pow(x, 10) + Math.pow(y, 10)

**Answer:** (d) Math.pow(x, 10) + Math.pow(y, 10)
**Explanation:** ^ is not a power operator in Java.

**Q76.** Statement I: In Java, `x^2` gives x squared. Statement II: `Math.pow(x, 2)` gives x squared as a double.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (d) Statement I is false, Statement II is true
**Explanation:** ^ is a bitwise operator, not a power.

---

## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** Distinguish between `/` and `%`.
**Answer:** `/` gives the quotient (`17 / 5` = 3 for integers).
`%` gives the remainder (`17 % 5` = 2).

**Q2.** Distinguish between prefix and postfix increment.
**Answer:** Prefix (`++x`) increases x first and then uses the new value.
Postfix (`x++`) uses the old value first and then increases x.

**Q3.** Distinguish between a counter and an accumulator.
**Answer:** A counter increases by a fixed amount (usually 1) to count: `c++`.
An accumulator adds varying values to build a total: `sum += n`.

**Q4.** Name the three forms of operators with an example of each.
**Answer:** Unary (`++a`), binary (`a + b`).
Ternary (`a > b ? a : b`).

**Q5.** State the use of the `new` operator and the dot operator.
**Answer:** `new` creates an object by allocating memory, e.g. `new Scanner(System.in)`.
The dot operator invokes a member of a class or object, e.g. `Math.sqrt(x)`.

**Q6.** Distinguish between `print()` and `println()`.
**Answer:** print() displays output and keeps the cursor on the same line.
println() displays output and moves to the next line.

**Q7.** Distinguish between `next()` and `nextLine()`.
**Answer:** next() reads one word, stopping at a space.
nextLine() reads the whole line including spaces.

**Q8.** Name the three ways of giving input to a program.
**Answer:** Initialisation (before execution) and parameters (at execution).
Input stream / Scanner (during execution).

**Q9.** Distinguish between syntax and logical errors.
**Answer:** A syntax error breaks the rules of Java and is found by the compiler (missing semicolon).
A logical error lets the program run but gives a wrong result (f = 0 in a factorial).

**Q10.** What is a runtime error? Give an example.
**Answer:** An error that occurs while the program runs and stops it abnormally.
Example: integer division by zero; entering a word when nextInt() expects a number.

**Q11.** State the return types of Math.ceil(), Math.round() and Math.random().
**Answer:** Math.ceil() returns double; Math.random() returns double (0.0 to below 1.0).
Math.round() returns a whole number (long for a double argument).

**Q12.** Why is `Math.pow(m, 2/3)` wrong for m raised to the power 2/3? Correct it.
**Answer:** 2/3 is integer division, giving 0, so the result is always 1.0 (logical error).
Write `Math.pow(m, 2.0/3)`.

### Output and error questions (2 marks each)

**Q13.** Give the values of a and b after `int a = 10; int b = a++ + ++a;`
**Answer:** b = 22, a = 12
a++ gives 10 (a = 11); ++a gives 12.

**Q14.** Evaluate `q += q++ + ++q;` when q = 10.
**Answer:** q = 32
Old q = 10; q++ gives 10 (q = 11); ++q gives 12; 10 + 22 = 32.

**Q15.** Give the output of `Math.round(2.5)` and `Math.round(-2.5)`.
**Answer:** `3` and `-2`
.5 always rounds up (towards the larger number).

**Q16.** Give the output of `System.out.println(15 / 4 * 4 + 15 % 4);`
**Answer:** `15`
15 / 4 = 3; 3 × 4 = 12; 15 % 4 = 3; 12 + 3 = 15.

**Q17.** Identify the error type and correct: `double avg = (8 + 7) / 2;` prints 7.0 instead of 7.5.
**Answer:** Logical error — (8 + 7) / 2 is integer division.
Write `double avg = (8 + 7) / 2.0;`

**Q18.** Give the output of `Math.floor(-0.5)` and `Math.round(-0.5)`.
**Answer:** `-1.0` and `0`
floor rounds down; round takes .5 up to 0.

**Q19.** Give the output: `char c = 'A'; c += 2; System.out.println(c);`
**Answer:** `C`
The shorthand operator adds 2 to the code (67) and keeps the type char.

**Q20.** Give the output: `System.out.println(7.0 / 2 + " " + (double)(7 / 2));`
**Answer:** `3.5 3.0`
7.0 / 2 is real division; 7 / 2 is 3 before the cast.

**Q21.** Write Java expressions for (a) the volume of a cylinder, πr²h, using 3.14 (b) (a + b) ÷ (a − b).
**Answer:** (a) `3.14 * r * r * h` (or `3.14 * Math.pow(r, 2) * h`)
(b) `(a + b) / (a - b)` — the brackets are essential.

**Q22.** Give the output of `Math.min(4, 4.0)` and `Math.abs(-0.5)`.
**Answer:** `4.0` and `0.5`
min returns the wider type (double); abs keeps the type.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; a sample run follows each.*

### Section B programs (15 marks each)

**Q1.** Write a program to accept three integers and print their sum, their average (as a real number), the largest and smallest using Math.max() and Math.min(), and the range (largest − smallest).
**Answer:**
```java
import java.util.*;
class ThreeNumbers
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter three integers: ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int sum = a + b + c;
        double avg = sum / 3.0;                     // 3.0 gives a real average
        int largest = Math.max(a, Math.max(b, c));  // nested Math methods
        int smallest = Math.min(a, Math.min(b, c));
        System.out.println("Sum      = " + sum);
        System.out.println("Average  = " + avg);
        System.out.println("Largest  = " + largest);
        System.out.println("Smallest = " + smallest);
        System.out.println("Range    = " + (largest - smallest));
    }
}
```
Sample run:
```
Enter three integers: 12 45 7
Sum      = 64
Average  = 21.333333333333332
Largest  = 45
Smallest = 7
Range    = 38
```

**Q2.** Write a program to accept the coefficients a, b, c of a quadratic equation and print its real roots using Math.sqrt(), or a message if the roots are not real.
**Answer:**
```java
import java.util.*;
class Quadratic
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a, b and c of ax^2 + bx + c = 0: ");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        double d = b * b - 4 * a * c;               // discriminant
        if (d >= 0)
        {
            double r1 = (-b + Math.sqrt(d)) / (2 * a);
            double r2 = (-b - Math.sqrt(d)) / (2 * a);
            System.out.println("Discriminant = " + d);
            System.out.println("Root 1 = " + r1);
            System.out.println("Root 2 = " + r2);
        }
        else
            System.out.println("Discriminant = " + d + ": the roots are not real");
    }
}
```
Sample runs:
```
Enter a, b and c of ax^2 + bx + c = 0: 1 -5 6
Discriminant = 1.0
Root 1 = 3.0
Root 2 = 2.0

Enter a, b and c of ax^2 + bx + c = 0: 1 2 5
Discriminant = -16.0: the roots are not real
```

**Q3.** Write a program to accept the three sides of a triangle and print its area by Heron's formula, area = √(s(s − a)(s − b)(s − c)) where s = (a + b + c)/2, also rounded to a whole number and to two decimal places.
**Answer:**
```java
import java.util.*;
class Heron
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the three sides of a triangle: ");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        double s = (a + b + c) / 2;                          // semi-perimeter
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        System.out.println("Semi-perimeter = " + s);
        System.out.println("Area           = " + area);
        System.out.println("Area (rounded) = " + Math.round(area));
        System.out.println("Area (2 d.p.)  = " + Math.round(area * 100) / 100.0);
    }
}
```
Sample run:
```
Enter the three sides of a triangle: 5 6 7
Semi-perimeter = 9.0
Area           = 14.696938456699069
Area (rounded) = 15
Area (2 d.p.)  = 14.7
```

**Q4.** Write a program to accept a student's full name, section (a single letter) and marks in three subjects, and print the total, the percentage rounded to two decimal places and the highest mark. Use nextLine() for the name and next().charAt(0) for the section.
**Answer:**
```java
import java.util.*;
class MarkSheet
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter full name: ");
        String name = sc.nextLine();            // nextLine() keeps the space
        System.out.print("Enter section: ");
        char sec = sc.next().charAt(0);         // first character of a word
        System.out.print("Enter marks in English, Maths and Science: ");
        int e = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int total = e + m + s;
        double percent = total * 100.0 / 300;
        System.out.println("Name       : " + name);
        System.out.println("Section    : " + sec);
        System.out.println("Total      : " + total);
        System.out.println("Percentage : " + Math.round(percent * 100) / 100.0);
        System.out.println("Highest    : " + Math.max(e, Math.max(m, s)));
    }
}
```
Sample run:
```
Enter full name: Anika Lyngdoh
Enter section: B
Enter marks in English, Maths and Science: 78 92 85
Name       : Anika Lyngdoh
Section    : B
Total      : 255
Percentage : 85.0
Highest    : 92
```

**Q5.** Write a program using Math.random() to simulate the throw of a die (1–6), a lucky number from 1 to 100 and the toss of a coin (0 or 1).
**Answer:**
```java
class Dice
{
    public static void main(String args[])
    {
        double r = Math.random();                   // 0.0 <= r < 1.0
        int dice = (int) (r * 6) + 1;               // 1 to 6
        int lucky = (int) (Math.random() * 100) + 1; // 1 to 100
        int coin = (int) (Math.random() * 2);       // 0 or 1
        System.out.println("Random value  : " + r);
        System.out.println("Dice shows    : " + dice);
        System.out.println("Lucky number  : " + lucky);
        System.out.println("Coin (0 = head, 1 = tail): " + coin);
    }
}
```
Sample run (the values change every run):
```
Random value  : 0.23567204479420123
Dice shows    : 2
Lucky number  : 11
Coin (0 = head, 1 = tail): 0
```

**Q6.** Write a program to accept the volume of a cube and print its side (Math.cbrt), surface area (6 × side²), diagonal (side × √3), and the side rounded up and down.
**Answer:**
```java
import java.util.*;
class Cube
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the volume of a cube: ");
        double vol = sc.nextDouble();
        double side = Math.cbrt(vol);               // side = cube root of volume
        double surface = 6 * Math.pow(side, 2);
        double diagonal = side * Math.sqrt(3);
        System.out.println("Side         = " + side);
        System.out.println("Surface area = " + surface);
        System.out.println("Diagonal     = " + diagonal);
        System.out.println("Side rounded up   = " + Math.ceil(side));
        System.out.println("Side rounded down = " + Math.floor(side));
    }
}
```
Sample run:
```
Enter the volume of a cube: 50
Side         = 3.6840314986403864
Surface area = 81.43252849784719
Diagonal     = 6.380929732329262
Side rounded up   = 4.0
Side rounded down = 3.0
```

---

## 12. Competency / Application Questions

**Q1. (The cashier's bill)** A shop sells pens at ₹12.50 each. Write the statements to read the quantity q, compute the bill b and round it to the nearest rupee.
**Model answer:** `int q = sc.nextInt(); double b = q * 12.50; long r = Math.round(b);`

**Q2. (Exam average gone wrong)** `int total = 251; double avg = total / 3;` prints 83.0, but the true average is 83.67. Explain and fix.
**Model answer:** total / 3 is integer division (83). Write `total / 3.0` or `(double) total / 3`.

**Q3. (Which method?)** Name the Math method to: (a) round a price of 99.6 up to 100 (b) find the bigger of two scores (c) find the side of a square plot from its area.
**Model answer:** (a) Math.ceil (or Math.round) (b) Math.max (c) Math.sqrt.

**Q4. (Counting rainy days)** A loop reads daily rainfall r in mm for Sohra. Write the statements that count rainy days (r > 0) and total the rain.
**Model answer:** `if (r > 0) days++;` (counter) and `total += r;` (accumulator).

**Q5. (A dice game)** Why does `(int)(Math.random() * 6) + 1` never give 7?
**Model answer:** Math.random() is always below 1.0, so Math.random() × 6 is below 6.0; the cast gives 0–5, and adding 1 gives 1–6.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** `3 + 7/2` evaluates to 6.
**R:** Division has higher precedence than addition, and 7/2 is integer division.
**Answer:** (c)
**Explanation:** 3 + 3.

**Q2.**
**A:** `Math.sqrt(16)` returns 4.
**R:** Math.sqrt() returns a double.
**Answer:** (b)
**Explanation:** It returns 4.0; R is true.

**Q3.**
**A:** In `y += ++y;` with y = 8, the result is 17.
**R:** The old value of y is saved before the right side is evaluated.
**Answer:** (c)
**Explanation:** 8 + 9.

**Q4.**
**A:** nextLine() can read a name with a space.
**R:** next() reads only one word.
**Answer:** (d)
**Explanation:** Both true; R describes a different method.

**Q5.**
**A:** A missing semicolon is a logical error.
**R:** Logical errors give wrong results without stopping the program.
**Answer:** (b)
**Explanation:** It is a syntax error; R is true.

**Q6.**
**A:** `(5 > 3) || (10 / 0 > 1)` does not cause an error.
**R:** With OR, Java skips the second condition when the first is true.
**Answer:** (c)
**Explanation:** Short-circuit evaluation.

**Q7.**
**A:** Math.round() returns a whole number.
**R:** Math is in the java.lang package.
**Answer:** (d)
**Explanation:** Both true; unrelated.

**Q8.**
**A:** `Math.pow(m, 2/3)` gives m raised to the power 2/3.
**R:** 2/3 evaluates to 0 in Java.
**Answer:** (b)
**Explanation:** It gives 1.0; use 2.0/3.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — Evaluate carefully

> `int x = 4; x *= --x + x++ + x;`

**(i)** What value does --x give?
**Answer:** 3.

**(ii)** What value does x++ give?
**Answer:** 3.

**(iii)** What is the last x on the right side?
**Answer:** 4.

**(iv)** What is the final value of x?
**Answer:** 40.

### Case 2 — The canteen bill

> A program reads the number of samosas n with `sc.nextInt()` and the price 12.5, computes `double bill = n * 12.5;` and prints `Math.round(bill)`.

**(i)** Which class reads n?
**Answer:** Scanner.

**(ii)** Which package must be imported?
**Answer:** java.util.

**(iii)** For n = 3, what is bill?
**Answer:** 37.5.

**(iv)** What does Math.round(bill) print?
**Answer:** 38.

### Case 3 — The broken area

> `double a = 1/2 * b * h;` prints 0.0 for every triangle.

**(i)** What type of error is this?
**Answer:** Logical error.

**(ii)** What is the value of 1/2 in Java?
**Answer:** 0.

**(iii)** Correct the statement.
**Answer:** `double a = 1.0/2 * b * h;` (or 0.5 * b * h).

**(iv)** For b = 6 and h = 4, what does the corrected statement give?
**Answer:** 12.0.

---

## 15. Revision Notes

### Chapter at a glance
- Operators: unary, binary, ternary; arithmetic, relational, logical, assignment, shorthand, increment/decrement, ternary, new, dot.
- `/` quotient (integer division drops fractions), `%` remainder (sign of the first operand).
- Counter (fixed step) vs accumulator (running total).
- Prefix: change then use; postfix: use then change; in `x op= e` the old x is saved first.
- Precedence: postfix > unary > `* / %` > `+ -` > relational > equality > AND > OR > ?: > assignment; `* / %` left to right.
- print vs println.
- Input: initialisation, parameters, Scanner (`nextInt`, `nextDouble`, `next`, `nextLine`, `next().charAt(0)`), java.util.
- Errors: syntax, runtime, logical; comments `//`, `/* */`, `/** */`.
- Math (java.lang): pow, sqrt, cbrt, ceil, floor → double; round → long; abs, max, min → argument type; random → 0.0 ≤ r < 1.0.
- Expressions: write every `*`; use Math.pow for powers; brackets for fractions.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| `Math.sqrt(16)` = 4 | It is 4.0 (double). |
| Using the new x on the left of `x += …` | The old value of x is used. |
| `7 / 2` = 3.5 | Integer division: 3. |
| `x^2` for x squared | Use `Math.pow(x, 2)` or `x * x`. |
| `b2 - 4ac` | `b*b - 4*a*c`. |
| Missing semicolon called a logical error | It is a syntax error. |
| `Math.round(-2.5)` = −3 | It is −2 (.5 rounds up). |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 2: Revision II**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** `42/6%2` gives:
(a) 1 (b) 10 (c) 2 (d) 0

**2.** `&&` is a:
(a) relational (b) logical (c) arithmetic (d) ternary operator

**3.** Scanner method for a sentence:
(a) next() (b) nextLine() (c) nextInt() (d) nextString()

**4.** `Math.ceil(5.4) + Math.ceil(4.5)`:
(a) 10.0 (b) 11.0 (c) 12.0 (d) 9.0

**5.** Missing semicolon:
(a) logical (b) runtime (c) syntax (d) no error

**6.** `int lives = 5; System.out.print(lives--); System.out.print(lives);` prints:
(a) 43 (b) 54 (c) 53 (d) 44

**7.** Method returning a whole number:
(a) Math.round (b) Math.ceil (c) Math.floor (d) Math.sqrt

**8.** `Math.max(-7, Math.min(-5, -4))`:
(a) −5 (b) −4 (c) −7 (d) 5

**9.** Statement I: `1/2` is 0 in Java. Statement II: `1.0/2` is 0.5.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

**10.** The accumulator in `c = c + (x * d + e);`:
(a) d (b) c (c) e (d) x

### Part I — Short answers (5 × 2 = 10)

**11.** Evaluate `x *= --x + x++ + x;` when x = 4. [2]

**12.** Write the Java expressions for √(b² − 4ac) and (a + b)ˣ. [2]

**13.** Give the output: `Math.floor(-4.7)` and `Math.ceil(3.4) + Math.pow(2, 3)`. [2]

**14.** Distinguish next() and nextLine(). [2]

**15.** Name the type of error and correct: `int f = 0; for (p = 5; p > 0; p--) f *= p;` [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** (i) Evaluate `y += ++y + y-- + --y;` when y = 8. [4]
(ii) Write a program to accept three integers and print their average and the largest using Math.max. [6]

**17.** (i) Explain precedence and associativity with an example. [4]
(ii) Write a program to print the real roots of a quadratic equation. [6]

**18.** (i) State the return types of pow, round, max(int, double) and random. [4]
(ii) Write a program to find the area of a triangle by Heron's formula. [6]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | d | b | c | d | b |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | 3 | 3 | 4 | 40 |
| 2 | Scanner | java.util | 37.5 | 38 |
| 3 | Logical | 0 | 1.0/2 * b * h | 12.0 |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | a | b | b | b | c | b | a | a | a | b |

**Part I, Q11–15 (2 marks each)**

**11.** 4 × (3 + 3 + 4) (1); 40 (1).
**12.** `Math.sqrt(b*b - 4*a*c)` (1); `Math.pow(a + b, x)` (1).
**13.** −5.0 (1); 12.0 (1).
**14.** One word (1); whole line with spaces (1).
**15.** Logical error (1); f = 1 (1).

**Part II (10 marks each)**

**16.** (i) Old y 8 (1); 9, 9, 7 (2); 33 (1). (ii) Input (1), sum / 3.0 (2), nested Math.max (2), output (1).

**17.** (i) Definitions (2), example such as `42/6%2` = 1 (2). (ii) Input (1), discriminant (2), roots with Math.sqrt (2), message (1).

**18.** (i) double, long, double, double (1 each). (ii) Input (1), s (2), Math.sqrt formula (2), output (1).
