# Java Programming

| Field | Value |
|---|---|
| Board | MBOSE (Meghalaya Board of School Education) |
| Class | X |
| Subject | Computer Science |
| Chapter | Object-Oriented Programming II (Java) · Chapter 12 |
| Title | Java Programming |
| Textbook source | *Click Start 10 – Computer Science for Schools* (Cambridge University Press). The book was not available; see the note below. |
| Exam weightage | **Java** (Chapters 11–12) carries about **18–22 of 80 marks**. A 5-mark Java program, and an output or debugging question, come from this chapter every year. |
| Syllabus scope | Primitive and non-primitive data types; variables and constants; operators and compound assignment; string joining with +; steps to evaluate expressions; input with Scanner; output with print and println; sequence, selection and repetition; if, switch; for, while and do-while loops; standard programs; output and debugging questions |
| In short | Learn to write Java programs that take input, do calculations, make decisions and repeat steps with loops. |

> **Note on the text:** The Click Start 10 textbook was not available. This chapter is written from the MBOSE SSLC Computer Science papers of 2022–2026. Every Java program, output, debugging and evaluation question in those papers is solved in Section 8.1, using the exact code printed in the papers.
>
> **Before this chapter:** Java's operators, if, switch and loops work almost exactly like C++ (Chapters 9–10). This chapter shows the Java forms and the few differences.

---

## 1. Complete Lesson

### Data types
#### Foundation first (from Chapters 3 and 8)

- **Memory units:** 1 byte = 8 bits. With *n* bits you can make $2^n$ patterns, so 16 bits (2 bytes) give $2^{16} = 65{,}536$ patterns.
- **C++ data types:** `int`, `float`, `double`, `char`, `bool`, `void` (Chapter 8). Java's primitive types are close cousins, with fixed sizes on every computer.
- A **class** is a blueprint and an **object** is an instance made from it (Chapter 8).

| Java type | Size | Holds |
|---|---|---|
| `byte` | 1 byte | small whole numbers (−128 to 127) |
| `short` | 2 bytes | whole numbers |
| `int` | 4 bytes | whole numbers (the usual choice) |
| `long` | 8 bytes | very large whole numbers |
| `float` | 4 bytes | decimals, about 7 digits |
| `double` | 8 bytes | decimals, about 15 digits (the usual choice) |
| `char` | 2 bytes | one Unicode character |
| `boolean` | — | true or false |

A **data type** tells the **kind of value** a variable can store and how much memory it uses. Java has two groups.

![Fig. 12.1 Data types in Java](figures/cs_ch12_fig01_types.png)

**1. Primitive data types** — the **eight built-in types**, which store simple values directly:

![Fig. 12.2 The eight primitive data types](figures/cs_ch12_fig02_sizes.png)

- `char` uses **2 bytes** because Java uses **Unicode**, so a char can hold any of **65,536 characters (0 to 65,535)** from all the world's scripts.
- A `float` value is written with `f` (`7.5f`); a `long` value with `L`.
- `boolean` holds only **true** or **false** (not 1 or 0, as in C++).

**Why Java's char is 2 bytes.** C++ used 1 byte, enough for the 256 ASCII-style codes of English. Java was made for the whole world, so it uses **Unicode**, which also covers Hindi, Bengali, Assamese and other scripts. Two bytes give 65,536 codes, numbered 0 to 65,535.

**Why sizes are fixed in Java.** In C++ an `int` may be 2 or 4 bytes depending on the compiler. In Java an `int` is always 4 bytes, on every machine — one more reason the same program behaves the same everywhere.

**2. Non-primitive (reference) data types** — **classes and objects, arrays, String and interfaces**. A reference variable does not hold the object itself: **its value is either a reference (the address of an object) or `null`** (refers to nothing).

```java
String name = "Bari";     // name holds a reference to a String object
String city = null;       // city refers to nothing yet
int[] marks = new int[5]; // an array is also a reference type
```

**Why "reference"?** A primitive variable is a box holding the value itself (`int age = 15;` — the 15 is in the box). An object can be large, so a reference variable holds only the **address** where the object is kept — like a slip of paper with a house address rather than the house itself. If the slip is blank, its value is `null`: it refers to nothing.

#### Worked examples

**Example 1 (basic — SSLC 2024, Q1(h); SSLC 2026, Q24; SSLC 2025, Q22).** (a) The char data type in Java stores characters in the range … (b) The value assigned to non-primitive or reference-type data is either … (c) Reference-type data types, including objects and arrays, are …

*Solution.* (a) **0 to 65,535** (Unicode). (b) A **reference** (the address of an object) **or null**. (c) **Non-primitive** data types.

**Example 2 (board level — SSLC 2023, Q5(b)).** Define data type. Name two primitive data types supported by Java. (2 marks)

*Model answer.* A **data type** tells the kind of value a variable can store and how much memory it uses. Two primitive data types: **int** (whole numbers, 4 bytes) and **double** (decimal numbers, 8 bytes). (Others: byte, short, long, float, char, boolean.)

**Why this scores:** the definition (1 mark) and two correct primitive types with what they hold (1 mark).

**Example 3 (a twist).** What does this program print?

```java
public class Types
{
    public static void main(String[] args)
    {
        char ch = 'A';
        ch++;
        int code = ch;
        boolean ok = 10 > 3;
        System.out.println(ch);
        System.out.println(code);
        System.out.println(ok);
    }
}
```

*Solution.* **Output:**

```
B
66
true
```

`ch++` moves 'A' (code 65) to the next character, 'B'. Storing ch in an int gives its code, 66. `10 > 3` gives the boolean value **true** — not 1, as in C++.

#### Doubts cleared

**Q. Why must a float be written as `7.5f`?**
In Java a decimal such as 7.5 is a `double` by default. `float f = 7.5;` is an error ("possible lossy conversion"); write `7.5f`.

**Q. Is String a primitive type?**
No. String is a class, so it is a non-primitive (reference) type.

**Q. Can a boolean hold 1 or 0?**
No. In Java a boolean holds only `true` or `false`.

**Q. How many primitive types does Java have?**
Eight: byte, short, int, long, float, double, char, boolean.

#### Mistakes to avoid

- Giving char as 1 byte in Java. It is 2 bytes.
- Writing `bool` (the C++ name). Java uses `boolean`.
- Listing String or arrays as primitive types.

#### Check yourself

1. How many bytes does a Java int take?
2. Name two non-primitive data types.
3. What is the default type of the literal 3.5 in Java?

**Answers:** 1. 4. 2. Any two of classes/objects, arrays, String, interfaces. 3. `double`.

### Variables and constants

- A **variable** is declared with its type: `int age;`, and may be initialised at once: `int age = 15;`.
- A **constant** is declared with **`final`**: `final double PI = 3.14159;` — its value cannot change.
- Identifier rules are the same as in C++ (letters, digits, `_` and `$`; not starting with a digit; not a keyword); Java is **case-sensitive**.

**Why `final`?** Some values must never change while a program runs — the value of pi, the number of days in a week, the pass mark. Declaring them `final` lets the compiler stop any line that tries to change them by mistake. By custom, constant names are written in CAPITALS (`PI`, `PASS_MARK`) so that they stand out.

#### Worked examples

**Example 1 (basic).** Declare: (a) an int `roll` with value 21; (b) a double `price` with value 45.5; (c) a char `section` with value 'B'.

*Solution.* (a) `int roll = 21;` (b) `double price = 45.5;` (c) `char section = 'B';`

**Example 2 (board level).** Write a Java program that uses a constant PI = 3.14 to find the area of a circle of radius 10.

*Solution.*

```java
public class Circle
{
    public static void main(String[] args)
    {
        final double PI = 3.14;
        int r = 10;
        double area = PI * r * r;
        System.out.println("Area = " + area);
    }
}
```

**Output:** `Area = 314.0` — Java prints a double with at least one decimal place.

**Example 3 (a twist).** What happens if the program above has the line `PI = 3.14159;` after the declaration?

*Solution.* It does not compile. The compiler reports an error such as "cannot assign a value to final variable PI", because a `final` variable cannot be changed once it has a value.

#### Doubts cleared

**Q. Do I have to give a final variable its value in the same line?**
It must be given exactly once, and it is clearest to do it in the declaration.

**Q. Is `Age` the same variable as `age`?**
No. Java is case-sensitive.

**Q. What if I use a variable inside main before giving it a value?**
Java refuses to compile: "variable might not have been initialized". It is stricter than C++, which allows garbage values.

#### Mistakes to avoid

- Writing `const` (the C++ keyword) for a Java constant. Java uses `final`.
- Starting a variable name with a digit, such as `2ndMark`.

#### Check yourself

1. Which keyword makes a constant in Java?
2. Declare a constant `MAX` of type int with value 100.
3. Is `total marks` a valid variable name?

**Answers:** 1. `final`. 2. `final int MAX = 100;` 3. No — it has a space.

### Operators in Java

Java has the same operators as C++ (Chapter 9): arithmetic `+ - * / %`, relational `< > <= >= == !=`, logical `&& || !`, assignment `=`, increment and decrement `++ --`, and the conditional operator `? :`. The differences:
- **Relational and logical expressions give `true` or `false`**, so `System.out.println(5 > 3);` prints **true**.
- **`+` joins (concatenates) strings.** When one operand is a String, the other is turned into text and joined to it.

**Why `+` behaves in two ways.** `+` looks at its two operands. If both are numbers, it adds. If either one is a String, it **joins** them as text. Because Java works left to right, `"Sum=" + 2 + 3` first makes the String "Sum=2", and then joins 3 to it. Put brackets round a sum you want worked out first.

| Expression | Result | Why |
|---|---|---|
| `"Sum=" + 2 + 3` | `Sum=23` | left to right: "Sum=2", then "Sum=23" |
| `"Sum=" + (2 + 3)` | `Sum=5` | brackets first |
| `2 + 3 + "x"` | `5x` | 2 + 3 is done first, then joined |
| `'A' + "" + 'z'` | `Az` | the empty string makes it text |
| `'A' + 1` | `66` | a char used in arithmetic is its code |

**Compound assignment operators** combine an arithmetic operator with `=`:

| Operator | Example | Same as | If a = 10 |
|---|---|---|---|
| `+=` | `a += 5;` | `a = a + 5;` | 15 |
| `-=` | `a -= 5;` | `a = a - 5;` | 5 |
| `*=` | `a *= 5;` | `a = a * 5;` | 50 |
| `/=` | `a /= 5;` | `a = a / 5;` | 2 |
| `%=` | `a %= 3;` | `a = a % 3;` | 1 |

#### Worked examples

**Example 1 (basic).** What is printed by `System.out.println(17 / 5);`, `System.out.println(17 % 5);` and `System.out.println(7 > 3);`?

*Solution.* `3` (integer division), `2` (remainder) and `true` (relational expressions give true or false in Java).

**Example 2 (board level — SSLC 2023, Q16(c)).** Explain the compound assignment operators in Java. (5 marks)

*Model answer.* A compound assignment operator combines an arithmetic operator with the assignment operator `=`. It works out the operation using the variable's present value and stores the result back in the same variable. With a = 10:
1. `+=` — `a += 5;` means `a = a + 5;` → 15.
2. `-=` — `a -= 5;` means `a = a - 5;` → 5.
3. `*=` — `a *= 5;` means `a = a * 5;` → 50.
4. `/=` — `a /= 5;` means `a = a / 5;` → 2.
5. `%=` — `a %= 3;` means `a = a % 3;` → 1.
They make programs shorter; the whole right side is worked out first, so `a *= b + 1` means `a = a * (b + 1)`.

**Why this scores:** the meaning (1 mark) and the five operators, each with its long form and result (about 1 mark each, counting the summary of all five).

**Example 3 (a twist).** What does this print?

```java
public class Join
{
    public static void main(String[] args)
    {
        System.out.println("Total: " + 10 + 20);
        System.out.println(10 + 20 + " total");
        System.out.println("A" + 'B' + 1);
        System.out.println('A' + 'B' + "1");
    }
}
```

*Solution.* **Output:**

```
Total: 1020
30 total
AB1
1311
```

- Line 1: a String comes first, so 10 and then 20 are joined as text.
- Line 2: 10 + 20 = 30 is done first (both numbers), then joined.
- Line 3: "A" is a String, so 'B' and 1 are joined: AB1.
- Line 4: 'A' + 'B' are two chars, so they are **added** as codes (65 + 66 = 131), and then "1" is joined: 1311.

#### Doubts cleared

**Q. Does Java have the `? :` operator?**
Yes, exactly as in C++: `int max = (a > b) ? a : b;`.

**Q. Do `++` and `--` work the same as in C++?**
Yes — prefix changes then uses; postfix uses then changes.

**Q. Can I use `==` to compare two Strings?**
For numbers and characters use `==`. For Strings, `==` does not compare the text reliably; Java uses `a.equals(b)` for that.

#### Mistakes to avoid

- Expecting `"Sum=" + 2 + 3` to print Sum=5. Use brackets: `"Sum=" + (2 + 3)`.
- Writing that relational operators give 1 or 0 in Java. They give true or false.
- Writing `=+` instead of `+=`.

#### Check yourself

1. What does `"x" + 4 + 4` give?
2. What does `4 + 4 + "x"` give?
3. With b = 9, what is b after `b %= 4;`?

**Answers:** 1. x44. 2. 8x. 3. 1.

### Steps to evaluate an expression

Java follows the same precedence as C++: **brackets**, then **unary** operators, then **`*`, `/`, `%` from left to right**, then **`+`, `-` from left to right**, and **assignment last**.

**Example:** `x = y / 4 + (3 - z * 3);` with y = 20, z = 2:
1. Inside the brackets, `z * 3` = 6.
2. `3 - 6` = −3.
3. `y / 4` = 5.
4. `5 + (−3)` = 2.
5. x = **2**.

**Why write the steps.** In "write the steps to evaluate" questions, the marks are for the **order**, not only the final value. Number each step, name the operator used, and give the result after each step.

> **In the exam, write:** one numbered step per operator, in precedence order, ending with "assign to …". If values are given, show the value after each step.

#### Worked examples

**Example 1 (basic — SSLC 2023, Q5(d)).** Write the steps to evaluate `a = x + 2 * y - (x / y);`, and find a when x = 10, y = 3 (both int).

*Solution.*
1. Brackets: `x / y` = 10 / 3 = 3 (integer division).
2. Multiplication: `2 * y` = 6.
3. Addition: `x + 6` = 16.
4. Subtraction: 16 − 3 = 13.
5. Assign: **a = 13**.

**Example 2 (board level — SSLC 2022, Q5(d)).** Write the steps to evaluate `y = a * b % 2 / (c + d);`, and find y when a = 3, b = 5, c = 0, d = 1.

*Solution.*
1. Brackets: `c + d` = 1.
2. `*`, `%` and `/` have equal precedence, so left to right: `a * b` = 15.
3. `15 % 2` = 1.
4. `1 / 1` = 1.
5. Assign: **y = 1**.

**Example 3 (a twist).** Find the values: `double p = 7 / 2;` and `double q = 7 / 2.0;`

*Solution.* p = **3.0** — `7 / 2` is worked out first as integer division (3), and only then stored as a double. q = **3.5** — one operand is a decimal, so the division is a decimal division.

#### Doubts cleared

**Q. Is the precedence in Java different from C++?**
No — the same order: brackets, unary, `* / %`, `+ -`, relational, logical, assignment.

**Q. When two operators have the same level, which goes first?**
The one on the left (left-to-right associativity), except assignment, which goes right to left.

**Q. Does integer division happen in Java too?**
Yes. Two ints give an int quotient: 10 / 3 = 3.

#### Mistakes to avoid

- Doing `x + 2` before `2 * y`.
- Forgetting integer division in `x / y`.
- Leaving out the final "assign" step.

#### Check yourself

1. Evaluate `20 - 6 / 3 * 2` (all int).
2. Evaluate `(4 + 6) % 4`.
3. In `y = a * b % 2 / (c + d)`, which part is done first?

**Answers:** 1. 6 / 3 = 2, 2 × 2 = 4, 20 − 4 = 16. 2. 10 % 4 = 2. 3. The brackets, `c + d`.

### Input with Scanner

To read input from the keyboard, Java uses the **Scanner** class of the package `java.util`:

```java
import java.util.Scanner;              // 1. import the class
public class Input
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);   // 2. create a Scanner on the keyboard
        System.out.print("Enter your age: ");
        int age = sc.nextInt();                // 3. read a whole number
        System.out.println("Next year you will be " + (age + 1));
    }
}
```

| Method | Reads |
|---|---|
| `sc.nextInt()` | an `int` |
| `sc.nextDouble()` / `sc.nextFloat()` | a decimal number |
| `sc.next()` | one word |
| `sc.nextLine()` | a whole line |
| `sc.next().charAt(0)` | one character |

Common mistakes: `new Scanner(System.out)` (must be **`System.in`**), `nextInt()` without `sc.` in front, and `nextlnt` (small L) instead of `nextInt`.

**Why the three steps?** Java keeps most tools in packages, so `Scanner` must first be **imported** from `java.util`. Scanner is a class, so we must **create an object** of it with `new`, and tell it where to read from: `System.in`, the keyboard. Then the object's methods (`nextInt()`, `next()`) **read** the values.

**What the screen shows for the program above** (the user types 15):

```
Enter your age: 15
Next year you will be 16
```

#### Worked examples

**Example 1 (basic).** Write a program to read a person's first name and greet them.

*Solution.*

```java
import java.util.Scanner;
public class Greet
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = sc.next();
        System.out.println("Khublei, " + name + "!");
    }
}
```

**Output** (input Iba): `Khublei, Iba!`

**Example 2 (board level — SSLC 2022, Q12(b)).** Write a program in Java to accept marks in three subjects out of 100 each and print the total and percentage. (5 marks)

*Solution.*

```java
import java.util.Scanner;
public class Percent
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter marks in three subjects: ");
        int m1 = sc.nextInt();
        int m2 = sc.nextInt();
        int m3 = sc.nextInt();
        int total = m1 + m2 + m3;
        double per = total * 100.0 / 300;
        System.out.println("Total = " + total);
        System.out.println("Percentage = " + per);
    }
}
```

**Output** (input 78 85 92):

```
Total = 255
Percentage = 85.0
```

*Key point:* `100.0` makes the division a decimal one; `total * 100 / 300` with ints would cut off any decimal part.

**Example 3 (a twist — the kind of debugging in SSLC 2026, Q47).** Find and correct the errors.

```
Scanner sc = new Scanner(System.out);
int a = sc.nextlnt();
int b = nextInt();
System.out.println("Sum = " + a + b);
```

*Solution.*
1. `System.out` → `System.in` (input comes from the keyboard).
2. `nextlnt` → `nextInt` (capital I, not small L).
3. `nextInt()` → `sc.nextInt()` (the method belongs to the Scanner object).
4. `"Sum = " + a + b` → `"Sum = " + (a + b)` — otherwise 3 and 4 print as "34".
Also check that the program begins with `import java.util.Scanner;`.

#### Doubts cleared

**Q. What is the difference between `next()` and `nextLine()`?**
`next()` reads one word (up to a space); `nextLine()` reads the whole line, spaces and all.

**Q. How do I read one character?**
`char ch = sc.next().charAt(0);` — read a word and take its first character.

**Q. What happens if the user types a word when `nextInt()` expects a number?**
The program stops with an error (an exception) while running.

#### Mistakes to avoid

- Forgetting `import java.util.Scanner;`.
- `new Scanner(System.out)` instead of `System.in`.
- Writing `sc.nextint()` in small letters. Java is case-sensitive: `nextInt`.

#### Check yourself

1. Which package holds Scanner?
2. Write the statement to read a double into `price`.
3. Write the statement that creates a Scanner object called `in`.

**Answers:** 1. `java.util`. 2. `double price = sc.nextDouble();` 3. `Scanner in = new Scanner(System.in);`

### Output

- `System.out.println(x);` prints x and moves to a new line; `System.out.println();` prints an empty line.
- `System.out.print(x);` prints x and stays on the same line.
- **Only one argument** is passed; join several items with `+`: `System.out.println("Sum = " + (a + b));`.
- Strings use **double quotes** (`"a=?"`); single quotes are only for one character (`'a'`).

**Why only one argument?** `println` takes exactly one thing to print. To print a label and a value together, you build one String with `+` and pass that. This is unlike C++, where `cout << a << b` can list many items.

#### Worked examples

**Example 1 (basic).** What does this print?

```java
public class Show
{
    public static void main(String[] args)
    {
        System.out.print("Tura ");
        System.out.println("Jowai");
        System.out.println();
        System.out.println("Nongpoh");
    }
}
```

*Solution.*

```
Tura Jowai

Nongpoh
```

`print` keeps "Tura " on the line; `println("Jowai")` finishes it; `println()` prints an empty line.

**Example 2 (board level).** With `int a = 5, b = 7;` write one statement that prints `a = 5, b = 7`.

*Solution.* `System.out.println("a = " + a + ", b = " + b);`

**Example 3 (a twist).** With `int a = 5, b = 7;` what do `System.out.println(a + b);` and `System.out.println("" + a + b);` print?

*Solution.* `12` and `57`. In the first, both are numbers, so they are added. In the second, the empty String comes first, so a and b are joined as text.

#### Doubts cleared

**Q. Can I write `System.out.println(a, b);`?**
No. println takes one argument; join them with `+`.

**Q. Is there an `endl` in Java?**
No. `println` itself ends the line; `"\n"` inside a String also works.

**Q. Can println print a boolean?**
Yes — it prints true or false.

#### Mistakes to avoid

- Writing `system.out.println` with a small s.
- Using single quotes for a String: `'Hello'`.
- Writing `println` as `printIn`.

#### Check yourself

1. Which method does not move to a new line?
2. What does `System.out.println("5" + 5);` print?
3. Write the statement that prints an empty line.

**Answers:** 1. `print`. 2. 55. 3. `System.out.println();`

### Programming constructs

Java supports **three basic programming constructs**:

![Fig. 12.3 The three programming constructs](figures/cs_ch12_fig03_constructs.png)

1. **Sequence** — statements run one after another, in the order written.
2. **Selection** — a condition decides which statements run: `if`, `if-else`, `else if`, `switch`.
3. **Repetition (iteration)** — statements are repeated while a condition is true: `for`, `while`, `do-while`.

**Why these three are enough.** Every program, however big, is built from just these three patterns: doing steps in order, choosing between steps, and repeating steps. Learn them well and you can read any program in this course.

#### Worked examples

**Example 1 (basic — SSLC 2026, Q20).** Java supports sequential, selection and … programming constructs.

*Solution.* **Repetition (iteration)**.

**Example 2 (board level — SSLC 2025, Q46).** Explain the three basic programming constructs supported by Java. (3 marks)

*Model answer.*
1. **Sequence** — statements are executed one after another, in the order written. Example: read two numbers, add them, print the sum.
2. **Selection** — a condition decides which statements run. Java uses `if`, `if-else`, `else if` and `switch`. Example: print "Pass" or "Fail".
3. **Repetition (iteration)** — statements are repeated while a condition is true. Java uses `for`, `while` and `do-while`. Example: print 1 to 10.

**Why this scores:** each construct named, explained and matched with its Java statements and an example.

**Example 3 (a twist).** Which constructs does this program use, and what does it print?

```java
public class Count
{
    public static void main(String[] args)
    {
        int evens = 0;
        for (int i = 1; i <= 10; i++)
        {
            if (i % 2 == 0)
                evens++;
        }
        System.out.println("Even numbers: " + evens);
    }
}
```

*Solution.* All three: sequence (the statements of main in order), repetition (`for`) and selection (`if`). **Output:** `Even numbers: 5`.

#### Doubts cleared

**Q. Is a method call a construct?**
No. It is a statement used inside the constructs.

**Q. Are these the same as C++'s control structures?**
Yes — sequence, selection and iteration (Chapter 10).

**Q. Where does `switch` belong?**
Under selection.

#### Mistakes to avoid

- Listing "loop, if and switch" as the three constructs. The three are sequence, selection and repetition.
- Putting do-while under selection.

#### Check yourself

1. Name the three programming constructs.
2. Which construct does `while` belong to?
3. Which construct runs statements simply in order?

**Answers:** 1. Sequence, selection, repetition. 2. Repetition. 3. Sequence.

### Selection in Java

```java
if (marks >= 33)
    System.out.println("Pass");
else
    System.out.println("Fail");
```

```java
switch (choice)
{
    case 1:  System.out.println("Add");      break;
    case 2:  System.out.println("Subtract"); break;
    default: System.out.println("Wrong choice");
}
```

The rules for `switch` are as in C++; Java also allows String values in case labels.

**Why it feels familiar.** Java's if, else if and switch were copied from C and C++ on purpose — one of Java's goals was to be **familiar**. The two differences to remember: a Java condition must give a **boolean** (true/false), so `if (n)` with an int is an error; and switch can also match **Strings**.

#### Worked examples

**Example 1 (board level — SSLC 2026, Q54; SSLC 2023, Q12(a)).** Write a program in Java to print whether a number entered by the user is even or odd. (5 marks)

*Solution.*

```java
import java.util.Scanner;
public class EvenOdd
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        if (n % 2 == 0)
            System.out.println(n + " is even");
        else
            System.out.println(n + " is odd");
    }
}
```

**Output** (input 46): `46 is even`. (Input 19: `19 is odd`.)

**Why this scores:** import and Scanner (1), input (1), condition `n % 2 == 0` (2), both messages (1).

**Example 2 (board level — SSLC 2025, Q54).** Write a Java program to accept an alphabet and check whether it is a vowel or a consonant. (5 marks)

*Solution.*

```java
import java.util.Scanner;
public class Vowel
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an alphabet: ");
        char ch = sc.next().charAt(0);
        switch (ch)
        {
            case 'a': case 'e': case 'i': case 'o': case 'u':
            case 'A': case 'E': case 'I': case 'O': case 'U':
                System.out.println(ch + " is a vowel");
                break;
            default:
                System.out.println(ch + " is a consonant");
        }
    }
}
```

**Output** (input E): `E is a vowel`. (Input t: `t is a consonant`.) Grouping the ten cases lets both capital and small vowels share one message.

**Example 3 (a twist — SSLC 2023, Q12(b)).** Write a Java program to print the greatest of three numbers given by the user. What does it print if two numbers are equal and largest?

*Solution.*

```java
import java.util.Scanner;
public class Greatest3
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter three numbers: ");
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        if (a >= b && a >= c)
            System.out.println("Greatest = " + a);
        else if (b >= c)
            System.out.println("Greatest = " + b);
        else
            System.out.println("Greatest = " + c);
    }
}
```

**Output** (input 14 27 9): `Greatest = 27`. (Input 8 8 3: `Greatest = 8`.) Using `>=` keeps ties safe. With the common pattern `if (a > b && a > c) … else if (b > a && b > c) … else …`, the input 8 8 3 fails both tests and wrongly prints 3.

#### Doubts cleared

**Q. Can I write `if (n % 2)` as in C++?**
No. A Java condition must be boolean. Write `if (n % 2 == 0)` or `if (n % 2 != 0)`.

**Q. Does a missing break cause fall-through in Java too?**
Yes, exactly as in C++.

**Q. Can switch use a String in Java?**
Yes, e.g. `case "Mon":`.

#### Mistakes to avoid

- Using `>` in "greatest" programs and getting a wrong answer for equal values.
- Forgetting `break` after a case.
- Comparing a char with double quotes: `ch == "a"`. Use `ch == 'a'`.

#### Check yourself

1. Write the condition for "n is negative".
2. What does default do in a switch?
3. Is `if (x = 5)` allowed in Java for an int x?

**Answers:** 1. `n < 0` 2. It runs when no case matches. 3. No — `x = 5` gives an int, not a boolean, so it is a compile error (one way Java is safer than C++).

### Loops in Java

**Syntax of the for loop:**

```java
for (initialisation; condition; update)
{
    statements;
}
```

- **Initialisation** (`int i = 1`) runs once; the **condition** (`i <= 10`) is tested before each pass; the **update** (`i++`) runs after each pass.

**while** and **for** are **entry-controlled loops**: the condition is tested **before** the body, so the body may not run at all. **do-while** is **exit-controlled**: the body runs **at least once**.

```java
int i = 1;
while (i <= 5)
{
    System.out.print(i + " ");
    i++;
}                                  // 1 2 3 4 5

int j = 10;
do
{
    System.out.print(j + " ");
    j = j + 2;
} while (j <= 16);                 // 10 12 14 16
```

`break` and `continue` work as in C++. Java has **no goto** (the word is reserved but not used).

**Why for and while are "entry-controlled".** The guard stands at the door. The condition is checked **before** the body each time, including the very first time; if it is false at the start, the body never runs. do-while checks at the exit, after the body.

**Declaring the counter in the loop.** In Java you may write `for (int i = 1; i <= 10; i++)`. Then i exists only inside the loop; using it after the loop is an error.

#### Worked examples

**Example 1 (board level — SSLC 2023, Q5(c); SSLC 2024, Q5(c)).** Explain the syntax of the for loop. Which loop statement is called an entry-controlled loop, and why?

*Model answer.*

```java
for (initialisation; condition; update)
{
    statements;
}
```

- **Initialisation** (e.g. `int i = 1`) runs once, at the start.
- **Condition** (e.g. `i <= 10`) is tested before each pass; the loop runs while it is true.
- **Update** (e.g. `i++`) runs after each pass.
The **for** and **while** loops are entry-controlled, because the condition is tested **before** the body is entered; if it is false at the start, the body does not run at all.

**Why this scores:** the syntax with all three parts explained (for 5(c)), and "for and while — condition checked before the body" (for 5(c) of 2024).

**Example 2 (board level — SSLC 2025, Q47).** Write a Java program to print the squares of the first five multiples of 5. (3 marks)

*Solution.*

```java
public class Squares
{
    public static void main(String[] args)
    {
        for (int i = 1; i <= 5; i++)
        {
            int m = 5 * i;
            System.out.println(m + " squared = " + (m * m));
        }
    }
}
```

**Output:**

```
5 squared = 25
10 squared = 100
15 squared = 225
20 squared = 400
25 squared = 625
```

**Example 3 (a twist — SSLC 2024, Q12(b)).** Write a program to print the even numbers from 10 to 98 using a do-while loop. How many numbers does it print?

*Solution.*

```java
public class Evens
{
    public static void main(String[] args)
    {
        int n = 10;
        do
        {
            System.out.print(n + " ");
            n = n + 2;
        } while (n <= 98);
        System.out.println();
    }
}
```

**Output:** `10 12 14 … 96 98` (all on one line). It prints (98 − 10) / 2 + 1 = **45** numbers. The update `n = n + 2` jumps straight from one even number to the next, so no `if` is needed.

#### Doubts cleared

**Q. Which Java loop runs at least once?**
do-while.

**Q. Does Java have goto?**
No. The word is reserved but not used. Use loops with break and continue.

**Q. Do I need the semicolon after `while (condition)` in do-while?**
Yes, as in C++.

#### Mistakes to avoid

- Using i after `for (int i = 1; …)` has ended.
- Forgetting `n = n + 2` (or `n += 2`) in a do-while, giving an endless loop.
- Writing commas instead of semicolons in the for header.

#### Check yourself

1. How many times does `for (int i = 0; i < 5; i++)` run?
2. Which loop is exit-controlled?
3. Write a while loop header that runs while k is not 0.

**Answers:** 1. 5 (i = 0 to 4). 2. do-while. 3. `while (k != 0)`

### Dry runs

![Fig. 12.4 Dry run of the 2024 series program](figures/cs_ch12_fig04_trace.png)

To find the output of a program, trace each variable pass by pass in a table, as in Fig. 12.4.

**Why a table beats guessing.** Each row of the table is one pass of the loop, each column one variable. You change only one cell at a time, so you cannot "jump ahead" and lose a value. The last row gives the output.

> **In the exam, write:** the dry-run table, then the output exactly as the screen shows it — one line per `println`, and items on the same line for `print`.

#### Worked examples

**Example 1 (board level — SSLC 2024, Q12(a)).** Write a program to display the product of the digits of a number (1234 gives 24), and dry-run it.

*Solution.*

```java
import java.util.Scanner;
public class Product
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int p = 1;
        while (n != 0)
        {
            p = p * (n % 10);
            n = n / 10;
        }
        System.out.println("Product of digits = " + p);
    }
}
```

| Pass | n | n % 10 | p | n / 10 |
|---|---|---|---|---|
| 1 | 1234 | 4 | 4 | 123 |
| 2 | 123 | 3 | 12 | 12 |
| 3 | 12 | 2 | 24 | 1 |
| 4 | 1 | 1 | 24 | 0 |

**Output** (input 1234): `Product of digits = 24`. Note that p starts at **1** — starting a product at 0 would make it 0 for ever.

**Example 2 (board level).** Write the output.

```java
public class Odd
{
    public static void main(String[] args)
    {
        int i = 1, sum = 0;
        while (i <= 5)
        {
            sum = sum + i * i;
            System.out.println("i=" + i + " sum=" + sum);
            i = i + 2;
        }
        System.out.println("Final sum=" + sum);
    }
}
```

*Solution.*

| Pass | i | i × i | sum |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| 2 | 3 | 9 | 10 |
| 3 | 5 | 25 | 35 |

Then i = 7, and 7 <= 5 is false. **Output:**

```
i=1 sum=1
i=3 sum=10
i=5 sum=35
Final sum=35
```

**Example 3 (a twist).** Write the output.

```java
public class Stars
{
    public static void main(String[] args)
    {
        for (int i = 3; i >= 1; i--)
        {
            for (int j = 1; j <= i; j++)
                System.out.print("* ");
            System.out.println();
        }
    }
}
```

*Solution.* The outer loop counts **down**: 3, 2, 1. Each row prints i stars, then `println()` ends the row:

```
* * *
* *
*
```

#### Doubts cleared

**Q. Do I show the spaces in the output?**
Yes, where the program prints them (as in "* "). A missing or extra space can cost the mark.

**Q. What if the loop never runs?**
Then the table has no rows, and only the statements after the loop give output.

**Q. Must the table have a column for every variable?**
For every variable that changes, plus a column for what is printed if that helps.

#### Mistakes to avoid

- Starting a product at 0.
- Printing on separate lines when the program uses `print`, not `println`.
- Updating the loop variable before using it in the same pass.

#### Check yourself

1. What is the product of the digits of 507?
2. In Example 2, what would the final sum be if i started at 2?
3. How many stars does Example 3 print in all?

**Answers:** 1. 5 × 0 × 7 = 0. 2. i = 2 and 4: 4 + 16 = 20. 3. 3 + 2 + 1 = 6.

### Summary of the chapter

- Primitive types (8): byte, short, int, long, float, double, char (2 bytes, 0–65,535, Unicode), boolean. Non-primitive (reference): classes, objects, arrays, String, interfaces; value is a reference or null.
- Variables; constants with `final`.
- Operators as in C++; relational and logical give true/false; `+` joins strings, left to right; compound assignment `+= -= *= /= %=`.
- Evaluate: brackets, unary, `* / %` left to right, `+ -` left to right, assignment.
- Input: `import java.util.Scanner;`, `Scanner sc = new Scanner(System.in);`, `sc.nextInt()`. Output: `println`, `print`; one argument joined with `+`; strings in double quotes.
- Constructs: sequence, selection (if, switch), repetition (for, while, do-while). for and while are entry-controlled; do-while is exit-controlled. No goto.

---

## 2. Learning Objectives

After studying this chapter, you should be able to:

1. Classify Java data types as primitive or non-primitive and state their sizes and ranges.
2. Declare variables and constants.
3. Use operators, compound assignment and string joining, and write the steps to evaluate an expression.
4. Read input with Scanner and print output with print and println.
5. Explain the three programming constructs and use if, switch and loops in Java.
6. Write the standard Java programs asked in the board examination.
7. Find the output of a Java program and debug Java programs.

---

## 3. Detailed Section Explanations

### Section 1 — Data types

**Exam focus:** "char range 0 to 65535" (SSLC 2024); "reference types — non-primitive" (SSLC 2025); "value of a reference type — a reference or a null" (SSLC 2026); "define data type; two primitive types" (SSLC 2023).

### Section 2 — Operators and evaluation

**Exam focus:** "compound assignment operators in Java" (SSLC 2023, 5 marks); "steps to evaluate" (SSLC 2022, 2023, 2024).

### Section 3 — Constructs and loops

**Exam focus:** "sequential, selection and repetition" (SSLC 2025, 2026); "syntax of for loop" (SSLC 2023); "entry-controlled loop" (SSLC 2024).

### Section 4 — Programs, outputs and debugging

**Exam focus:** even/odd, vowel/consonant, positive/negative/zero, greatest of three, product of digits, even numbers with do-while, squares of multiples of 5, total and percentage (SSLC 2022–2026); outputs (SSLC 2022, 2023, 2024); debugging (SSLC 2022, 2023, 2024, 2026).

---

## 4. Vocabulary (Key Terms)

| Term | Meaning | Example |
|---|---|---|
| primitive type | one of the 8 built-in types | `int` |
| non-primitive type | reference type | `String`, arrays |
| reference | the address of an object | — |
| null | a reference to nothing | `String s = null;` |
| Unicode | character code covering all scripts | `char` |
| final | keyword for a constant | `final int MAX = 100;` |
| concatenation | joining strings with + | `"a" + "b"` |
| compound assignment | operator + `=` | `+=` |
| Scanner | class for keyboard input | `new Scanner(System.in)` |
| nextInt() | reads an int | `sc.nextInt()` |
| println | prints and moves to a new line | — |
| construct | basic structure of a program | selection |
| entry-controlled loop | condition tested first | `while` |
| exit-controlled loop | condition tested last | `do-while` |
| dry run | tracing a program by hand | trace table |

---

## 5. Important Facts, Formulas and Results

### 5.1 Key facts

| Fact | Detail |
|---|---|
| char range | 0 to 65,535 (2 bytes, Unicode) |
| Reference-type data | non-primitive |
| Value of a reference variable | a reference or a null |
| Java constructs | sequential, selection and repetition |
| Entry-controlled loops | for, while |
| Exit-controlled loop | do-while |
| Keyboard input | `Scanner sc = new Scanner(System.in);` |
| Read an int | `sc.nextInt()` |
| Constant | `final` |
| `5 > 3` prints | true |
| `"Sum=" + 2 + 3` | Sum=23 |
| Strings are written in | double quotes |

### 5.2 Steps to evaluate (template)

| Step | Rule |
|---|---|
| 1 | work out the brackets (inner first) |
| 2 | unary operators (`++`, `--`, `!`) |
| 3 | `*`, `/`, `%` from left to right |
| 4 | `+`, `-` from left to right |
| 5 | relational, then logical operators |
| 6 | assign the result |

---

## 6. Person Profiles

### 6.1 James Gosling

| Point | Detail |
|---|---|
| Who | Creator of Java |
| Known for | Designed Java's syntax to look like C and C++ so programmers could learn it quickly |

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas

- **Same logic, new language.** Programs written in C++ carry over to Java with small changes.
- **Text joins, numbers add.** The `+` operator depends on its operands.
- **Read, process, print.** Most programs follow this three-step pattern.

### 7.2 Real-life connections

- **Online forms** check that numbers are positive or that a field is a vowel or letter, just like these programs.
- **Results software** computes totals and percentages for every student.

---

## 8. Exam-Oriented Questions

*Keep 2-mark answers within 30 words and 3-mark answers within 50 words; programs may be longer.*

### 8.1 Questions from the MBOSE SSLC papers (2022–2026) — solved

| Source | Question |
|---|---|
| MBOSE SSLC 2026, Q20 (1 mark) | Java supports sequential, selection and … programming constructs. |
| MBOSE SSLC 2026, Q24 (1 mark) | The value assigned to non-primitive or reference-type data is either … |
| MBOSE SSLC 2026, Q47 (3 marks) | Debug the Java program to print the sum of any two numbers (given below). |
| MBOSE SSLC 2026, Q54 (5 marks); 2023, Q12(a) | Write a program in Java to print whether a number entered by the user is even or odd. |
| MBOSE SSLC 2025, Q22 (1 mark) | Reference-type data types, including objects and arrays, are … |
| MBOSE SSLC 2025, Q46 (3 marks) | Explain the three basic programming constructs supported by Java. |
| MBOSE SSLC 2025, Q47 (3 marks) | Write a Java program to print the squares of the first five multiples of 5. |
| MBOSE SSLC 2025, Q54 (5 marks) | Write a Java program to accept an alphabet and check whether it is a vowel or a consonant. |
| MBOSE SSLC 2024, Q1(h) (1 mark) | The char data type in Java stores characters in the range … |
| MBOSE SSLC 2024, Q5(c) | Which loop statement is called an entry-controlled loop, and why? |
| MBOSE SSLC 2024, Q5(d) | Write the steps to evaluate `x=y/4+(3-z*3);` |
| MBOSE SSLC 2024, Q12(a) (5 marks) | Write a program to display the product of the digits of a number (1234 gives 24). |
| MBOSE SSLC 2024, Q12(b) (5 marks) | Write a program to print the even numbers from 10 to 98 using a do-while loop. |
| MBOSE SSLC 2024, Q13(a) (5 marks) | Write the output of the Java series program (given below). |
| MBOSE SSLC 2024, Q13(b) (5 marks) | Debug the Java program to find whether a year is a leap year (given below). |
| MBOSE SSLC 2023, Q5(b) | Define data type. Name two primitive data types supported by Java. |
| MBOSE SSLC 2023, Q5(c) | Explain the syntax of the for loop. |
| MBOSE SSLC 2023, Q5(d) | Write the steps to evaluate `a=x+2*y-(x/y);` |
| MBOSE SSLC 2023, Q12(b) (5 marks) | Write a Java program to print the greatest of three numbers given by the user. |
| MBOSE SSLC 2023, Q13(a) (5 marks) | Write the output of the Java program `Operators` (given below). |
| MBOSE SSLC 2023, Q13(b) (5 marks) | Debug the Java program to print the first 10 natural numbers (given below). |
| MBOSE SSLC 2023, Q16(c) (5 marks) | Explain the compound assignment operators in Java. |
| MBOSE SSLC 2022, Q5(d) | Write the steps to evaluate `y=a*b%2/(c+d);` |
| MBOSE SSLC 2022, Q12(a) (5 marks) | Write a program in Java to display whether a given number is positive, negative or zero. |
| MBOSE SSLC 2022, Q12(b) (5 marks) | Write a program in Java to accept marks in three subjects out of 100 each and print the total and percentage. |
| MBOSE SSLC 2022, Q13(a) (5 marks) | Write the output of the Java program `Output` (given below). |
| MBOSE SSLC 2022, Q13(b) (5 marks) | Debug the Java program to swap two integers without a third variable (given below). |

**Solutions**

**SSLC 2026, Q20.** **(C) repetition.**

**SSLC 2026, Q24.** **(C) a reference or a null.**

**SSLC 2026, Q47.** The program as printed:

```java
import java.util.Scanner;
public class AddNum
{
public static void main(String[ ]args)
{
sc = new Scanner(System.in);
System.out.println("Enter the numbers: ");
a = nextInt( );
b = nextInt( );
System.out.println("Sum of the two numbers = ", a + b);
}
}
```

| Wrong | Correct | Reason |
|---|---|---|
| `sc = new Scanner(System.in);` | `Scanner sc = new Scanner(System.in);` | sc must be declared as a Scanner |
| (no declaration of a and b) | `int a, b;` | variables must be declared |
| `a = nextInt( );` | `a = sc.nextInt( );` | nextInt is called on the Scanner object |
| `b = nextInt( );` | `b = sc.nextInt( );` | same reason |
| `println("Sum of the two numbers = ", a + b);` | `println("Sum of the two numbers = " + (a + b));` | println takes one argument; join with + and bracket the sum |

**SSLC 2026, Q54; 2023, Q12(a).**

```java
import java.util.Scanner;
public class EvenOdd
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        if (n % 2 == 0)
            System.out.println(n + " is even");
        else
            System.out.println(n + " is odd");
    }
}
```

**SSLC 2025, Q22.** **(B) Non-primitive.**

**SSLC 2025, Q46.** (i) **Sequence** — statements are executed one after another in the order written. (ii) **Selection** — a condition decides which statements run, using `if`, `if-else` or `switch`. (iii) **Repetition (iteration)** — statements are repeated while a condition is true, using `for`, `while` or `do-while`.

**SSLC 2025, Q47.**

```java
public class Squares
{
    public static void main(String[] args)
    {
        int i, m;
        for (i = 1; i <= 5; i++)
        {
            m = 5 * i;
            System.out.println("Square of " + m + " = " + (m * m));
        }
    }
}
```

Output: 25, 100, 225, 400 and 625 (the squares of 5, 10, 15, 20 and 25).

**SSLC 2025, Q54.**

```java
import java.util.Scanner;
public class VowelCheck
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an alphabet: ");
        char ch = sc.next().charAt(0);
        switch (ch)
        {
            case 'a': case 'e': case 'i': case 'o': case 'u':
            case 'A': case 'E': case 'I': case 'O': case 'U':
                System.out.println(ch + " is a vowel");
                break;
            default:
                System.out.println(ch + " is a consonant");
        }
    }
}
```

**SSLC 2024, Q1(h).** **(iii) 0 to 65535.**

**SSLC 2024, Q5(c).** The **while** loop (and the for loop) is called entry-controlled, because the condition is tested at the entry, before the body runs; if the condition is false at the start, the body does not run at all.

**SSLC 2024, Q5(d).** For `x=y/4+(3-z*3);`: (1) inside the brackets, `z*3`; (2) then `3 - (z*3)`; (3) `y/4`; (4) add the results of steps 3 and 2; (5) assign the sum to x.

**SSLC 2024, Q12(a).**

```java
import java.util.Scanner;
public class ProductDigits
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int prod = 1;
        while (n != 0)
        {
            prod = prod * (n % 10);
            n = n / 10;
        }
        System.out.println("Product of digits = " + prod);
    }
}
```

For 1234: 4 × 3 × 2 × 1 = **24**.

**SSLC 2024, Q12(b).**

```java
public class EvenNumbers
{
    public static void main(String[] args)
    {
        int i = 10;
        do
        {
            System.out.print(i + " ");
            i = i + 2;
        } while (i <= 98);
    }
}
```

**SSLC 2024, Q13(a).** The program as printed:

```java
public class series
{
public static void main (String[]args)
{
int i =1, t =1, sum=0;
while (i<=4)
{
sum +=t;
system.out.println ("Term="+t);
t+=3;
i++;
}
System.out.println("Sum of series="+sum);
}
}
```

(The paper prints `system` with a small s inside the loop; Java needs `System`, so this is taken as a misprint.) Dry run in Fig. 12.4. **Output:**

```
Term=1
Term=4
Term=7
Term=10
Sum of series=22
```

**SSLC 2024, Q13(b).** The program as printed:

```java
import java.util.  ;
public class leapyear
{
public static void main (String);
{
Scanner sc=new Scanner (System);
int year;
System.out.println("Enter the year");
year=nextInt();
if(year%4=0)
{
System.out.print (year+"is leap year");
}
else
{
System.out.println (year + "is not leap year");
}
}
}
```

| Wrong | Correct | Reason |
|---|---|---|
| `import java.util.  ;` | `import java.util.*;` (or `java.util.Scanner;`) | the class or `*` is missing |
| `public static void main (String);` | `public static void main (String[] args)` | args array needed; no semicolon after the heading |
| `new Scanner (System)` | `new Scanner (System.in)` | the keyboard is `System.in` |
| `year=nextInt();` | `year=sc.nextInt();` | nextInt is called on sc |
| `if(year%4=0)` | `if(year%4==0)` | comparison needs `==` |

(Also add a space: `year + " is leap year"`.)

**SSLC 2023, Q5(b).** A data type tells the kind of value a variable can hold and the memory it uses. Two primitive data types: `int` (whole numbers) and `char` (a single character). (Others: byte, short, long, float, double, boolean.)

**SSLC 2023, Q5(c).** `for (initialisation; condition; update) { statements; }` — the initialisation runs once, the condition is tested before each pass, and the update runs after each pass. Example: `for (int i = 1; i <= 10; i++) System.out.println(i);`.

**SSLC 2023, Q5(d).** For `a=x+2*y-(x/y);`: (1) the brackets, `x/y`; (2) `2*y`; (3) `x + (2*y)`; (4) subtract the result of step 1; (5) assign to a.

**SSLC 2023, Q12(b).**

```java
import java.util.Scanner;
public class Greatest
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter three numbers: ");
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        int big;
        if (a >= b && a >= c)
            big = a;
        else if (b >= c)
            big = b;
        else
            big = c;
        System.out.println("Greatest = " + big);
    }
}
```

**SSLC 2023, Q13(a).** The program as printed:

```java
public class Operators
{
  public static void main (String[]args)
  {
    int a=5;
    int b=10;
    int c=15;
    int d=20;
    System.out.println("a+b="+(a+b));
    System.out.println("a*b="+(a*b));
    System.out.println("a++="+(a++));
    System.out.println("--b="+(--b));
    System.out.println("c!=d="+(c!=d));
  }
}
```

`a++` prints the old value 5 (postfix); `--b` prints 9 (prefix); `c != d` is true. **Output:**

```
a+b=15
a*b=50
a++=5
--b=9
c!=d=true
```

**SSLC 2023, Q13(b).** The program as printed:

```java
public class Natural
{
  public static void main (String)
  {
    i;
    System.out.println("The first 10 natural numbers are :\n");
    for (i=1; i<=n; i++)
    {
      System.out.println(n)
    }
    System.out.println(\n);
  }
}
```

| Wrong | Correct | Reason |
|---|---|---|
| `main (String)` | `main (String[] args)` | main needs a String array parameter |
| `i;` | `int i;` | a variable must be declared with its type |
| `i<=n` | `i<=10` | n is undeclared; the limit is 10 |
| `System.out.println(n)` | `System.out.println(i);` | print the counter i; add the semicolon |
| `System.out.println(\n);` | `System.out.println("\n");` | the escape sequence must be inside quotes |

**SSLC 2023, Q16(c).** Compound assignment operators combine an arithmetic operator with `=`, so the variable is updated using its own value. `+=`: `a += 5` means `a = a + 5`. `-=`: `a -= 5` means `a = a - 5`. `*=`: `a *= 5` means `a = a * 5`. `/=`: `a /= 5` means `a = a / 5`. `%=`: `a %= 3` means `a = a % 3`. With a = 10 they give 15, 5, 50, 2 and 1.

**SSLC 2022, Q5(d).** For `y=a*b%2/(c+d);`: (1) the brackets, `c+d`; (2) `a*b`; (3) `(a*b) % 2`; (4) divide that by `(c+d)`; (5) assign to y. (`*`, `%` and `/` have equal precedence and go left to right.)

**SSLC 2022, Q12(a).**

```java
import java.util.Scanner;
public class Sign
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        if (n > 0)
            System.out.println("Positive");
        else if (n < 0)
            System.out.println("Negative");
        else
            System.out.println("Zero");
    }
}
```

**SSLC 2022, Q12(b).**

```java
import java.util.Scanner;
public class Marks
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter marks in three subjects: ");
        int m1 = sc.nextInt(), m2 = sc.nextInt(), m3 = sc.nextInt();
        int total = m1 + m2 + m3;
        double per = total * 100.0 / 300;
        System.out.println("Total = " + total);
        System.out.println("Percentage = " + per);
    }
}
```

**SSLC 2022, Q13(a).** The program as printed:

```java
public class Output
{
  public static void main (String[]args)
  {
    char chr1='A', chr2='z';
    int i;
    System.out.println( );
    for(i=1; i<=5; i++)
    {
      System.out.println(chr1+""+chr2+",");
      chr1++;
      chr2--;
    }
  }
}
```

The first `println( )` prints an empty line. In each pass, `chr1+""+chr2` joins the two characters as text (the empty string stops them being added as numbers); then chr1 moves forward (A, B, C…) and chr2 backward (z, y, x…). **Output:**

```

Az,
By,
Cx,
Dw,
Ev,
```

**SSLC 2022, Q13(b).** The program as printed:

```java
import java.*;
public class Swap
{
Public static void main( )
{
int a, b;
Scanner sc = new Scanner(System.out);
System.out.println('a=?');
a = sc.nextlnt( );
System.out.println('b=?');
b = sc.nextlnt( );
System.out.println("Before swapping : "+"a="+a+"b="+b);
a = a+b;
b = b-a;
a = a-b;
System.out.println("After swapping : "+"a="+b+"b="+a);
}
}
```

| Wrong | Correct | Reason |
|---|---|---|
| `import java.*;` | `import java.util.*;` | Scanner is in java.util |
| `Public static void main( )` | `public static void main(String[] args)` | keywords are small letters; main needs `String[] args` |
| `new Scanner(System.out)` | `new Scanner(System.in)` | input comes from System.in |
| `println('a=?')`, `println('b=?')` | `println("a=?")`, `println("b=?")` | strings use double quotes |
| `sc.nextlnt( )` | `sc.nextInt( )` | the method is nextInt (capital I) |
| `b = b-a;` | `b = a-b;` | gives b the old value of a |
| `"a="+b+"b="+a` | `"a="+a+" b="+b` | a and b already hold the swapped values |

### 8.2 More questions in the board's style — solved

**Q1.** Write the output: `System.out.println("Sum=" + 2 + 3);` and `System.out.println("Sum=" + (2 + 3));`
**Answer:** `Sum=23` and `Sum=5`.

**Q2.** Write a Java statement to read a decimal number into `price` using Scanner `sc`.
**Answer:** `double price = sc.nextDouble();`

**Q3.** Declare a constant `MAX` equal to 100.
**Answer:** `final int MAX = 100;`

**Q4.** Write a program segment to print the numbers 1 to 10 using a while loop.
**Answer:** `int i = 1; while (i <= 10) { System.out.println(i); i++; }`

**Q5.** What does `System.out.println(10 > 20);` print?
**Answer:** `false`.

### 8.3 More practice in the board's style

**Q1.** How many primitive data types does Java have?
**Answer:** Eight.

**Q2.** Which class reads keyboard input?
**Answer:** Scanner.

**Q3.** Which loop runs at least once?
**Answer:** do-while.

**Q4.** What is the size of char in Java?
**Answer:** 2 bytes.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| MCQ | repetition; reference or null; non-primitive; 0 to 65535; nextInt; System.in; string joining | 9, 8.1 |
| 2 marks | data type and two primitive types; for-loop syntax; entry-controlled loop; steps to evaluate | 10, 8.1 |
| 3 marks | three constructs; squares of multiples of 5; debug AddNum | 10, 8.1 |
| 5 marks | even/odd; vowel/consonant; positive/negative/zero; greatest of three; product of digits; even numbers 10–98; total and percentage; outputs; debugging; compound assignment | 8.1, 11 |

---

## 9. MCQs with Explanations

*Some questions include "All of the above" or "None of the above" as an option, and it is sometimes the correct answer, so read every option carefully.*

### Data types and variables (Q1–Q14)

**Q1.** The char data type in Java stores characters in the range
- (a) 0 to 256
- (b) –128 to 127
- (c) 0 to 65535
- (d) 0 to 32767

**Answer:** (c) 0 to 65535
**Explanation:** MBOSE SSLC 2024, Q1(h): 2 bytes, Unicode.

**Q2.** Reference-type data types, including objects and arrays, are called
- (a) Primitive
- (b) Non-primitive
- (c) Boolean
- (d) Double

**Answer:** (b) Non-primitive
**Explanation:** MBOSE SSLC 2025, Q22.

**Q3.** The value assigned to non-primitive or reference-type data is either
- (a) a number or an alphabet
- (b) a number or a constant
- (c) a reference or a null
- (d) a string or an expression

**Answer:** (c) a reference or a null
**Explanation:** MBOSE SSLC 2026, Q24.

**Q4.** How many primitive data types does Java have?
- (a) 4
- (b) 8
- (c) 6
- (d) 10

**Answer:** (b) 8
**Explanation:** byte, short, int, long, float, double, char, boolean.

**Q5.** The size of char in Java is
- (a) 4 bytes
- (b) 1 byte
- (c) 2 bytes
- (d) 8 bytes

**Answer:** (c) 2 bytes
**Explanation:** Java uses Unicode.

**Q6.** The data type that holds only true or false is
- (a) boolean
- (b) char
- (c) int
- (d) String

**Answer:** (a) boolean
**Explanation:** Java does not use 1 and 0 for true and false.

**Q7.** Which of these is a non-primitive data type?
- (a) int
- (b) String
- (c) double
- (d) char

**Answer:** (b) String
**Explanation:** String is a class.

**Q8.** The smallest whole-number type in Java, of 1 byte, is
- (a) long
- (b) short
- (c) int
- (d) byte

**Answer:** (d) byte
**Explanation:** Range −128 to 127.

**Q9.** A constant in Java is declared with the keyword
- (a) void
- (b) const only
- (c) static only
- (d) final

**Answer:** (d) final
**Explanation:** `final double PI = 3.14159;`

**Q10.** The data type best for a decimal value like 3.14159265 with high precision is
- (a) double
- (b) float
- (c) int
- (d) char

**Answer:** (a) double
**Explanation:** About 15 digits.

**Q11.** A `float` literal is written with the letter
- (a) c
- (b) L
- (c) d only
- (d) f

**Answer:** (d) f
**Explanation:** For example `7.5f`.

**Q12.** The keyword `null` means a reference variable
- (a) holds zero
- (b) refers to no object
- (c) holds an empty string
- (d) is a constant

**Answer:** (b) refers to no object
**Explanation:** It is the default value of a reference variable.

**Q13.** Java uses Unicode for characters so that
- (a) characters of all the world's scripts can be stored
- (b) only English letters are stored
- (c) programs run faster on DOS
- (d) numbers take less space

**Answer:** (a) characters of all the world's scripts can be stored
**Explanation:** Including Indian scripts.

**Q14.** Which statement declares an int and gives it a value together?
- (a) `marks = 85;`
- (b) `int marks;`
- (c) `int marks = 85;`
- (d) `int = 85;`

**Answer:** (c) `int marks = 85;`
**Explanation:** Declaration and initialisation together.

### Operators and output (Q15–Q30)

**Q15.** `System.out.println(5 > 3);` prints
- (a) yes
- (b) 1
- (c) 5
- (d) true

**Answer:** (d) true
**Explanation:** Java prints boolean results as true or false.

**Q16.** `System.out.println("Sum=" + 2 + 3);` prints
- (a) Sum=5
- (b) Sum=23
- (c) Sum=2+3
- (d) an error

**Answer:** (b) Sum=23
**Explanation:** Joined left to right as text.

**Q17.** With brackets, `System.out.println("Sum=" + (2 + 3));` prints
- (a) Sum=(2+3)
- (b) Sum=23
- (c) Sum=5
- (d) 5

**Answer:** (c) Sum=5
**Explanation:** The brackets are worked out first.

**Q18.** `System.out.println(2 + 3 + "x");` prints
- (a) 2+3x
- (b) 23x
- (c) x5
- (d) 5x

**Answer:** (d) 5x
**Explanation:** 2 + 3 is added before the string appears.

**Q19.** If a = 10, after `a *= 5;` a is
- (a) 15
- (b) 50
- (c) 5
- (d) 2

**Answer:** (b) 50
**Explanation:** `a = a * 5`.

**Q20.** If a = 10, after `a %= 3;` a is
- (a) 30
- (b) 3
- (c) 1
- (d) 13

**Answer:** (c) 1
**Explanation:** 10 % 3 = 1.

**Q21.** In the 2023 program `Operators`, with a = 5, the line `"a++="+(a++)` prints
- (a) a++=6
- (b) a++=5
- (c) a++=4
- (d) a++=10

**Answer:** (b) a++=5
**Explanation:** Postfix: the old value is used.

**Q22.** In the same program, with b = 10, `"--b="+(--b)` prints
- (a) --b=11
- (b) --b=10
- (c) --b=9
- (d) --b=8

**Answer:** (c) --b=9
**Explanation:** Prefix: decreased first.

**Q23.** With c = 15 and d = 20, `"c!=d="+(c!=d)` prints
- (a) c!=d=false
- (b) c!=d=true
- (c) c!=d=1
- (d) c!=d=5

**Answer:** (b) c!=d=true
**Explanation:** 15 is not equal to 20.

**Q24.** The statement that prints and stays on the same line is
- (a) `System.out.println()`
- (b) `System.out.print()`
- (c) `System.in.print()`
- (d) `sc.print()`

**Answer:** (b) `System.out.print()`
**Explanation:** println() moves to a new line.

**Q25.** In Java, a string is written in
- (a) double quotes
- (b) single quotes
- (c) square brackets
- (d) angle brackets

**Answer:** (a) double quotes
**Explanation:** Single quotes are for one character (SSLC 2022, Q13(b)).

**Q26.** `System.out.println("Sum = ", a + b);` is wrong because println
- (a) needs single quotes
- (b) cannot print numbers
- (c) takes only one argument
- (d) must be written in capitals

**Answer:** (c) takes only one argument
**Explanation:** Use `"Sum = " + (a + b)` (SSLC 2026, Q47).

**Q27.** The value of `7 / 2` in Java (both int) is
- (a) 1
- (b) 3.5
- (c) 4
- (d) 3

**Answer:** (d) 3
**Explanation:** Integer division, as in C++.

**Q28.** The value of `'A' + 1` in Java is
- (a) 65
- (b) B
- (c) A1
- (d) 66

**Answer:** (d) 66
**Explanation:** The char is used as its code, 65.

**Q29.** In `x = y / 4 + (3 - z * 3);`, the first operation done is
- (a) `z * 3`
- (b) `y / 4`
- (c) `3 - z`
- (d) the assignment

**Answer:** (a) `z * 3`
**Explanation:** Inside the brackets, `*` comes before `-` (SSLC 2024, Q5(d)).

**Q30.** In `a = x + 2 * y - (x / y);`, the bracket `(x / y)` is evaluated
- (a) first
- (b) last
- (c) after the assignment
- (d) never

**Answer:** (a) first
**Explanation:** SSLC 2023, Q5(d).

### Input with Scanner (Q31–Q38)

**Q31.** To read keyboard input, the Scanner is created as
- (a) `new Scanner(System)`
- (b) `new Scanner(System.out)`
- (c) `new Scanner(System.in)`
- (d) `new Scanner(keyboard)`

**Answer:** (c) `new Scanner(System.in)`
**Explanation:** SSLC 2022 and 2024 debug questions.

**Q32.** The Scanner class belongs to the package
- (a) `java.net`
- (b) `java.lang`
- (c) `java.io` only
- (d) `java.util`

**Answer:** (d) `java.util`
**Explanation:** `import java.util.Scanner;`

**Q33.** The Scanner method that reads an int is
- (a) `getInt()`
- (b) `nextlnt()`
- (c) `readInt()`
- (d) `nextInt()`

**Answer:** (d) `nextInt()`
**Explanation:** Capital I, not small L.

**Q34.** `a = nextInt();` is wrong because nextInt must be
- (a) written in capitals
- (b) called on the Scanner object, as `sc.nextInt()`
- (c) placed inside quotes
- (d) followed by a colon

**Answer:** (b) called on the Scanner object, as `sc.nextInt()`
**Explanation:** SSLC 2026, Q47.

**Q35.** To read one character with Scanner sc, write
- (a) `sc.nextChar()`
- (b) `sc.next().charAt(0)`
- (c) `sc.char()`
- (d) `sc.nextInt()`

**Answer:** (b) `sc.next().charAt(0)`
**Explanation:** There is no nextChar() method.

**Q36.** To read a whole line of text, use
- (a) `sc.nextInt()`
- (b) `sc.next()`
- (c) `sc.nextLine()`
- (d) `sc.line()`

**Answer:** (c) `sc.nextLine()`
**Explanation:** `next()` reads one word.

**Q37.** To read a decimal number, use
- (a) `sc.nextDecimal()`
- (b) `sc.nextInt()`
- (c) `sc.next().charAt(0)`
- (d) `sc.nextDouble()`

**Answer:** (d) `sc.nextDouble()`
**Explanation:** Or `nextFloat()`.

**Q38.** `import java.*;` cannot be used to get Scanner because
- (a) Scanner is in the sub-package java.util
- (b) import is not a Java keyword
- (c) java has no packages
- (d) the semicolon is wrong

**Answer:** (a) Scanner is in the sub-package java.util
**Explanation:** SSLC 2022, Q13(b).

### Constructs and loops (Q39–Q47)

**Q39.** Java programming language supports sequential, selection and ______ programming constructs.
- (a) report
- (b) structured
- (c) repetition
- (d) dependent

**Answer:** (c) repetition
**Explanation:** MBOSE SSLC 2026, Q20.

**Q40.** The construct in which a condition decides which statements run is
- (a) sequence
- (b) selection
- (c) repetition
- (d) declaration

**Answer:** (b) selection
**Explanation:** if, switch.

**Q41.** The loop called entry-controlled is
- (a) while
- (b) do-while
- (c) switch
- (d) if-else

**Answer:** (a) while
**Explanation:** SSLC 2024, Q5(c). The for loop is also entry-controlled.

**Q42.** In `for (int i = 1; i <= 10; i++)`, the initialisation runs
- (a) once
- (b) ten times
- (c) eleven times
- (d) never

**Answer:** (a) once
**Explanation:** SSLC 2023, Q5(c).

**Q43.** The output of `int j = 10; do { System.out.print(j + " "); j = j + 2; } while (j <= 16);` is
- (a) 10
- (b) 10 12 14
- (c) 12 14 16
- (d) 10 12 14 16

**Answer:** (d) 10 12 14 16
**Explanation:** After 16, j = 18 and the test fails.

**Q44.** The first even number printed by the 2024 do-while program is
- (a) 10
- (b) 2
- (c) 12
- (d) 98

**Answer:** (a) 10
**Explanation:** i starts at 10 (SSLC 2024, Q12(b)).

**Q45.** In the 2024 series program, the value printed by "Sum of series=" is
- (a) 13
- (b) 10
- (c) 22
- (d) 34

**Answer:** (c) 22
**Explanation:** 1 + 4 + 7 + 10 (Fig. 12.4).

**Q46.** In the 2022 program `Output`, the second character pair printed is
- (a) Az,
- (b) By,
- (c) Bz,
- (d) Ay,

**Answer:** (b) By,
**Explanation:** chr1 goes A → B; chr2 goes z → y.

**Q47.** Java has no
- (a) if statement
- (b) while loop
- (c) switch statement
- (d) goto statement in use

**Answer:** (d) goto statement in use
**Explanation:** goto is reserved but unused.

### Programs and debugging (Q48–Q55)

**Q48.** The condition to test whether n is even is
- (a) `n % 2 == 0`
- (b) `n / 2 == 0`
- (c) `n % 2 == 1`
- (d) `n == 2`

**Answer:** (a) `n % 2 == 0`
**Explanation:** SSLC 2026, Q54.

**Q49.** In the product-of-digits program, prod must start at
- (a) 0
- (b) 1
- (c) 10
- (d) n

**Answer:** (b) 1
**Explanation:** Starting at 0 would make the product 0.

**Q50.** The product of the digits of 1234 is
- (a) 1234
- (b) 10
- (c) 24
- (d) 4321

**Answer:** (c) 24
**Explanation:** 1 × 2 × 3 × 4.

**Q51.** The squares of the first five multiples of 5 end with
- (a) 500
- (b) 125
- (c) 25
- (d) 625

**Answer:** (d) 625
**Explanation:** 25² = 625 (SSLC 2025, Q47).

**Q52.** `if(year%4=0)` is wrong because
- (a) comparison needs `==`
- (b) `%` cannot be used
- (c) year must be a String
- (d) if needs a semicolon

**Answer:** (a) comparison needs `==`
**Explanation:** SSLC 2024, Q13(b).

**Q53.** In the swap `a = a + b; b = ?; a = a - b;`, the missing statement is
- (a) `b = a - b;`
- (b) `b = b - a;`
- (c) `b = a + b;`
- (d) `b = 0;`

**Answer:** (a) `b = a - b;`
**Explanation:** SSLC 2022, Q13(b).

**Q54.** The percentage of marks out of 300 is correctly computed by
- (a) `total * 300 / 100`
- (b) `total / 300`
- (c) `total * 100.0 / 300`
- (d) `300 / total`

**Answer:** (c) `total * 100.0 / 300`
**Explanation:** 100.0 avoids integer division.

**Q55.** `Public static void main( )` has errors because
- (a) `public` must be in small letters and main needs `String[] args`
- (b) `static` is not allowed
- (c) `void` must be `int`
- (d) main must be in capitals

**Answer:** (a) `public` must be in small letters and main needs `String[] args`
**Explanation:** SSLC 2022, Q13(b).

---

## 10. Short-Answer Questions (2 and 3 marks)

### Very short answers (2 marks each)

**Q1.** Define data type. Name two primitive data types of Java.
**Answer:** The kind of value a variable holds and its memory size; e.g. `int` and `char`.

**Q2.** Explain the syntax of the for loop.
**Answer:** `for (initialisation; condition; update) { statements; }` — initialise once, test before each pass, update after each pass.

**Q3.** Which loop is called entry-controlled, and why?
**Answer:** while (and for), because the condition is tested before the body runs.

**Q4.** Write the steps to evaluate `x=y/4+(3-z*3);`.
**Answer:** `z*3`; `3 - (z*3)`; `y/4`; add the two results; assign to x.

**Q5.** Write the steps to evaluate `a=x+2*y-(x/y);`.
**Answer:** `x/y`; `2*y`; `x + 2*y`; subtract `x/y`; assign to a.

**Q6.** Write the steps to evaluate `y=a*b%2/(c+d);`.
**Answer:** `c+d`; `a*b`; `% 2`; divide by `(c+d)`; assign to y.

**Q7.** What is a non-primitive data type? Give two examples.
**Answer:** A reference type holding a reference to an object (or null), e.g. String and arrays.

**Q8.** What is the range of char in Java, and why?
**Answer:** 0 to 65,535, because char uses 2 bytes for Unicode characters.

**Q9.** Write the statements to read an integer using Scanner.
**Answer:** `Scanner sc = new Scanner(System.in);` then `int n = sc.nextInt();`.

**Q10.** Differentiate print() and println().
**Answer:** print() stays on the same line; println() moves to a new line after printing.

**Q11.** What is the output of `System.out.println("Sum=" + 2 + 3);`?
**Answer:** `Sum=23` — the numbers are joined as text, left to right.

**Q12.** How do you declare a constant in Java?
**Answer:** With final: `final double PI = 3.14159;`.

**Q13.** Correct: `Scanner sc = new Scanner(System.out);` and `a = sc.nextlnt();`.
**Answer:** `new Scanner(System.in)` and `a = sc.nextInt();`.

**Q14.** What does `System.out.println(10 > 20);` print?
**Answer:** `false`.

**Q15.** What is null?
**Answer:** A value for a reference variable meaning it refers to no object.

**Q16.** Name the three programming constructs.
**Answer:** Sequence, selection and repetition.

### Short answers (3 marks each)

**Q17.** Explain the three basic programming constructs supported by Java.
**Answer:** Sequence — statements in order; selection — if or switch chooses by a condition; repetition — for, while or do-while repeat statements.

**Q18.** Write a Java program to print the squares of the first five multiples of 5.
**Answer:** `for (int i = 1; i <= 5; i++) { int m = 5 * i; System.out.println(m * m); }` inside main — prints 25, 100, 225, 400, 625.

**Q19.** Debug: `sc = new Scanner(System.in);`, `a = nextInt( );`, `System.out.println("Sum = ", a + b);`.
**Answer:** `Scanner sc = new Scanner(System.in);`; declare `int a, b;`; `a = sc.nextInt( );`; `System.out.println("Sum = " + (a + b));`.

**Q20.** Explain three compound assignment operators.
**Answer:** `a += b` is `a = a + b`; `a -= b` is `a = a - b`; `a *= b` is `a = a * b` (also `/=`, `%=`).

**Q21.** Explain primitive and non-primitive data types.
**Answer:** Primitive: the 8 built-in types storing values (int, char…). Non-primitive: reference types (String, arrays, classes) storing a reference or null.

**Q22.** Differentiate while and do-while in Java.
**Answer:** while tests first (entry-controlled, may not run); do-while tests last (exit-controlled, runs at least once) and ends with `;`.

**Q23.** Write the output of: `char c = 'A'; for (int i = 1; i <= 3; i++) { System.out.print(c); c++; }`
**Answer:** `ABC` — c moves to the next letter each pass.

**Q24.** Explain how + works with strings in Java, with examples.
**Answer:** With a String operand, + joins text: `"Sum=" + 2 + 3` gives Sum=23; with brackets, `"Sum=" + (2 + 3)` gives Sum=5.

**Q25.** Write a program segment to print the even numbers from 10 to 98 using do-while.
**Answer:** `int i = 10; do { System.out.print(i + " "); i += 2; } while (i <= 98);`

**Q26.** Write the steps to use Scanner for input.
**Answer:** `import java.util.Scanner;`; create `Scanner sc = new Scanner(System.in);`; read with `sc.nextInt()`, `sc.nextDouble()` or `sc.next()`.

**Q27.** Write a program segment to check whether n is positive, negative or zero.
**Answer:** `if (n > 0) System.out.println("Positive"); else if (n < 0) System.out.println("Negative"); else System.out.println("Zero");`

**Q28.** Correct: `if(year%4=0)`, `main (String)`, `System.out.println(\n);`.
**Answer:** `if(year%4==0)`, `main (String[] args)`, `System.out.println("\n");`.

---

## 11. Long-Answer Questions (5 marks each)

### Long answers (5 marks each)

**Q1.** Write a Java program to check whether a number is even or odd.
**Answer:**

```java
import java.util.Scanner;
public class EvenOdd
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        if (n % 2 == 0)
            System.out.println(n + " is even");
        else
            System.out.println(n + " is odd");
    }
}
```

**Q2.** Write a Java program to check whether an alphabet is a vowel or a consonant.
**Answer:**

```java
import java.util.Scanner;
public class VowelCheck
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        char ch = sc.next().charAt(0);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'
            || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U')
            System.out.println(ch + " is a vowel");
        else
            System.out.println(ch + " is a consonant");
    }
}
```

**Q3.** Write a Java program to find the greatest of three numbers.
**Answer:**

```java
import java.util.Scanner;
public class Greatest
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        int big = a;
        if (b > big) big = b;
        if (c > big) big = c;
        System.out.println("Greatest = " + big);
    }
}
```

**Q4.** Write a Java program to display the product of the digits of a number.
**Answer:**

```java
import java.util.Scanner;
public class ProductDigits
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int prod = 1;
        while (n != 0)
        {
            prod = prod * (n % 10);
            n = n / 10;
        }
        System.out.println("Product of digits = " + prod);
    }
}
```

**Q5.** Write a Java program to accept marks in three subjects and print the total and percentage.
**Answer:**

```java
import java.util.Scanner;
public class Marks
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt(), m2 = sc.nextInt(), m3 = sc.nextInt();
        int total = m1 + m2 + m3;
        double per = total * 100.0 / 300;
        System.out.println("Total = " + total);
        System.out.println("Percentage = " + per);
    }
}
```

**Q6.** Explain the compound assignment operators in Java with examples.
**Answer:** They combine an arithmetic operator with `=`.
`a += 5` means `a = a + 5` (10 becomes 15).
`a -= 5` means `a = a - 5` (10 becomes 5).
`a *= 5` and `a /= 5` give 50 and 2 from 10.
`a %= 3` means `a = a % 3` (10 becomes 1).

**Q7.** Write the output of the 2023 program `Operators` (a = 5, b = 10, c = 15, d = 20) and explain each line.
**Answer:** `a+b=15` — the brackets add the numbers.
`a*b=50` — the product.
`a++=5` — postfix prints the old value.
`--b=9` — prefix decreases first.
`c!=d=true` — 15 is not equal to 20.

**Q8.** Write a Java program to print the first 10 natural numbers.
**Answer:**

```java
public class Natural
{
    public static void main(String[] args)
    {
        int i;
        System.out.println("The first 10 natural numbers are:");
        for (i = 1; i <= 10; i++)
            System.out.println(i);
    }
}
```

---

## 12. Competency / Application Questions

**Q1. (Shop counter)** A shop program must read the price of an item (₹ with paise) and the quantity. Which Scanner methods and data types should it use?
**Model answer:** `double price = sc.nextDouble();` and `int qty = sc.nextInt();`.

**Q2. (Name badge)** A program prints `"Roll: " + 1 + 2` hoping to show "Roll: 3". What does it print, and how is it fixed?
**Model answer:** It prints Roll: 12; write `"Roll: " + (1 + 2)`.

**Q3. (Menu)** A quiz program must show its menu at least once and repeat while the user chooses to continue. Which loop fits best?
**Model answer:** do-while, as it runs at least once.

**Q4. (Leap years)** The 2024 program says 1900 is a leap year. Is that right? How can the condition be improved?
**Model answer:** No; use `(y % 4 == 0 && y % 100 != 0) || y % 400 == 0`.

**Q5. (Spot the error)** A student writes `String s = 'Hello';` and `char c = "A";`. Correct both.
**Model answer:** `String s = "Hello";` and `char c = 'A';`.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) Both A and R are true, and R is the correct explanation of A.
- (b) Both A and R are true, but R is **not** the correct explanation of A.
- (c) A is true, but R is false.
- (d) A is false, but R is true.

**Q1.**
**A:** char in Java takes 2 bytes.
**R:** Java uses Unicode for characters.
**Answer:** (a)
**Explanation:** Range 0 to 65,535.

**Q2.**
**A:** `"Sum=" + 2 + 3` gives Sum=5.
**R:** + joins strings from left to right.
**Answer:** (d)
**Explanation:** It gives Sum=23.

**Q3.**
**A:** A do-while loop runs at least once.
**R:** It is an exit-controlled loop.
**Answer:** (a)
**Explanation:** The condition is tested after the body.

**Q4.**
**A:** A String variable can hold null.
**R:** String is a reference (non-primitive) type.
**Answer:** (a)
**Explanation:** SSLC 2026, Q24.

**Q5.**
**A:** `new Scanner(System.out)` reads from the keyboard.
**R:** System.in is the standard input stream.
**Answer:** (d)
**Explanation:** It must be System.in.

**Q6.**
**A:** `System.out.println(5 > 3);` prints 1.
**R:** Relational expressions give boolean values in Java.
**Answer:** (d)
**Explanation:** It prints true.

**Q7.**
**A:** `a %= 3` with a = 10 gives 1.
**R:** `a %= 3` means `a = a % 3`.
**Answer:** (a)
**Explanation:** 10 % 3 leaves remainder 1.

**Q8.**
**A:** while is an entry-controlled loop.
**R:** Java supports sequence, selection and repetition.
**Answer:** (b)
**Explanation:** Both true; R does not explain A.

**Q9.**
**A:** `'a=?'` is a valid Java string.
**R:** Single quotes hold one character.
**Answer:** (d)
**Explanation:** Strings need double quotes.

**Q10.**
**A:** In the product-of-digits program, prod starts at 1.
**R:** 1 does not change a product.
**Answer:** (a)
**Explanation:** Starting at 0 would always give 0.

---

## 14. Case-Based Questions

*Read each passage and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — Reading marks

> `Scanner sc = new Scanner(System.in); int m1 = sc.nextInt(), m2 = sc.nextInt(), m3 = sc.nextInt(); int total = m1 + m2 + m3; double per = total * 100.0 / 300;` The user enters 80, 70 and 90.

**(i)** Which package must be imported?
**Answer:** `java.util` (Scanner).

**(ii)** What is total?
**Answer:** 240.

**(iii)** What is per?
**Answer:** 80.0.

**(iv)** Why is 100.0 written instead of 100?
**Answer:** To get a decimal result, not integer division.

### Case 2 — Printing

> `int a = 4, b = 6;` A student writes `System.out.println("Total " + a + b);` and then `System.out.println("Total " + (a + b));`.

**(i)** What does the first statement print?
**Answer:** Total 46.

**(ii)** What does the second print?
**Answer:** Total 10.

**(iii)** What does `+` do with a String?
**Answer:** Joins (concatenates) text.

**(iv)** What would `System.out.println(a > b);` print?
**Answer:** false.

### Case 3 — Loop choice

> A program prints 5, 10, 15, 20, 25 using `for (int i = 5; i <= 25; i += 5)`.

**(i)** What is the initialisation?
**Answer:** `int i = 5`.

**(ii)** What is the update?
**Answer:** `i += 5`.

**(iii)** How many numbers are printed?
**Answer:** Five.

**(iv)** Is this loop entry- or exit-controlled?
**Answer:** Entry-controlled.

### Case 4 — Debugging

> `public static void main (String);` / `Scanner sc = new Scanner(System);` / `year = nextInt();` / `if (year % 4 = 0)`

**(i)** Correct the main heading.
**Answer:** `public static void main(String[] args)`.

**(ii)** Correct the Scanner line.
**Answer:** `Scanner sc = new Scanner(System.in);`.

**(iii)** Correct the input line.
**Answer:** `year = sc.nextInt();`.

**(iv)** Correct the condition.
**Answer:** `if (year % 4 == 0)`.

---

## 15. Revision Notes

### Chapter at a glance
- Primitive (8): byte 1, short 2, int 4, long 8, float 4, double 8, char 2 (0–65,535, Unicode), boolean. Non-primitive: classes, objects, arrays, String, interfaces — value is a reference or null.
- `final` makes a constant. Java is case-sensitive.
- Operators as in C++; relational gives true/false; `+` joins strings left to right (`"Sum=" + 2 + 3` = Sum=23); compound `+= -= *= /= %=`.
- Evaluate: brackets → unary → `* / %` → `+ -` → relational → logical → assignment.
- `import java.util.Scanner;` `Scanner sc = new Scanner(System.in);` `sc.nextInt()`, `nextDouble()`, `next()`, `nextLine()`, `next().charAt(0)`.
- `println` (new line), `print` (same line); one argument; strings in double quotes.
- Constructs: sequence, selection, repetition. for/while entry-controlled; do-while exit-controlled; no goto.
- Programs: `% 2 == 0`; `% 10` and `/ 10`; prod starts at 1; percentage `* 100.0 / 300`; swap `a=a+b; b=a-b; a=a-b`.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| `new Scanner(System.out)` | `System.in`. |
| `nextInt()` alone, `nextlnt` | `sc.nextInt()`. |
| `println("x", y)` | `println("x" + y)`. |
| `'a=?'` for a string | `"a=?"`. |
| `if (a = b)` | `if (a == b)`. |
| `main(String)` | `main(String[] args)`. |
| `Public`, `system` | `public`, `System`. |
| `"Sum=" + a + b` to add | `"Sum=" + (a + b)`. |

---

## 16. Chapter Test

**Class X · Computer Science · Object-Oriented Programming II (Java) Chapter 12: Java Programming**
**Time:** 1½ hours · **Maximum marks:** 40

**General instructions:**
1. Section A: multiple-choice questions; attempt all (10 × 1 = 10).
2. Section B: very short answers; answer any three of the four (3 × 2 = 6).
3. Section C: short answers; answer any three of the four (3 × 3 = 9).
4. Section D: long answers; answer any three of the four (3 × 5 = 15).

### Section A — Multiple-choice questions (10 × 1 = 10)

**1.** Java supports sequential, selection and ______ constructs.
- (a) report
- (b) structured
- (c) repetition
- (d) dependent

**2.** The value of a reference-type variable is either
- (a) a number or an alphabet
- (b) a reference or a null
- (c) a number or a constant
- (d) a string or an expression

**3.** Reference types such as objects and arrays are
- (a) primitive
- (b) boolean
- (c) double
- (d) non-primitive

**4.** char in Java stores characters in the range
- (a) 0 to 65535
- (b) 0 to 256
- (c) –128 to 127
- (d) 0 to 32767

**5.** `System.out.println("Sum=" + 2 + 3);` prints
- (a) Sum=5
- (b) Sum=23
- (c) Sum=2+3
- (d) an error

**6.** Keyboard input needs
- (a) `new Scanner(System.out)`
- (b) `new Scanner(System)`
- (c) `new Scanner(System.in)`
- (d) `new Scanner(keyboard)`

**7.** The entry-controlled loop is
- (a) do-while
- (b) while
- (c) switch
- (d) if

**8.** If a = 10, after `a %= 3;` a is
- (a) 3
- (b) 13
- (c) 30
- (d) 1

**9.** `System.out.println(5 > 3);` prints
- (a) 1
- (b) true
- (c) 5
- (d) yes

**10.** The product of the digits of 1234 is
- (a) 10
- (b) 1234
- (c) 24
- (d) 4321

### Section B — Very short answers (answer any three: 3 × 2 = 6)

**11.** Define data type. Name two primitive data types of Java.
**12.** Explain the syntax of the for loop.
**13.** Which loop is called entry-controlled, and why?
**14.** Write the steps to evaluate `x=y/4+(3-z*3);`.

### Section C — Short answers (answer any three: 3 × 3 = 9)

**15.** Explain the three basic programming constructs supported by Java.
**16.** Write a Java program to print the squares of the first five multiples of 5.
**17.** Debug: `sc = new Scanner(System.in);`, `a = nextInt( );`, `System.out.println("Sum = ", a + b);`.
**18.** Explain primitive and non-primitive data types.

### Section D — Long answers (answer any three: 3 × 5 = 15)

**19.** Write a Java program to check whether a number is even or odd.
**20.** Write a Java program to check whether an alphabet is a vowel or a consonant.
**21.** Write a Java program to accept marks in three subjects and print the total and percentage.
**22.** Write the output of the 2023 program `Operators` and explain each line.

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|---|---|
| 1 | c | 12 | b | 23 | b | 34 | b | 45 | c |
| 2 | b | 13 | a | 24 | b | 35 | b | 46 | b |
| 3 | c | 14 | c | 25 | a | 36 | c | 47 | d |
| 4 | b | 15 | d | 26 | c | 37 | d | 48 | a |
| 5 | c | 16 | b | 27 | d | 38 | a | 49 | b |
| 6 | a | 17 | c | 28 | d | 39 | c | 50 | c |
| 7 | b | 18 | d | 29 | a | 40 | b | 51 | d |
| 8 | d | 19 | b | 30 | a | 41 | a | 52 | a |
| 9 | d | 20 | c | 31 | c | 42 | a | 53 | a |
| 10 | a | 21 | b | 32 | d | 43 | d | 54 | c |
| 11 | d | 22 | c | 33 | d | 44 | a | 55 | a |

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | a | d | a | a | d | d | a | b | d | a |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | `java.util` | 240 | 80.0 | decimal result |
| 2 | Total 46 | Total 10 | joins text | false |
| 3 | `int i = 5` | `i += 5` | five | entry-controlled |
| 4 | `main(String[] args)` | `System.in` | `sc.nextInt()` | `==` |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Section A (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | c | b | d | a | b | c | b | d | b | c |

**Section B (2 marks each)**

**11.** Definition (1); two types (1).
**12.** Syntax (1); the three parts explained (1).
**13.** while/for (1); reason (1).
**14.** Correct order of steps (2).

**Section C (3 marks each)**

**15.** Each construct (1 each).
**16.** Loop (1); multiples (1); squares printed (1).
**17.** Any three corrections (1 each).
**18.** Primitive with examples (1½); non-primitive with examples (1½).

**Section D (5 marks each)**

**19.** Import and Scanner (1); input (1); condition (2); output (1).
**20.** Input of a char (1); vowel test (3); output (1).
**21.** Input (1); total (1½); percentage (1½); output (1).
**22.** Each line with reason (1 each).
