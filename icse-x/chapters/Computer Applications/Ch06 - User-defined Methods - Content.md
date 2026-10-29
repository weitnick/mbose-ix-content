# User-defined Methods

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 6 |
| Title | User-defined Methods |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 3. User-defined Methods |
| Exam weightage | **Section B**: a **method-overloading program** (15 marks) in every paper since 2017. **Section A**: MCQs and 2-mark parts on **prototypes**, **parameters**, **call by value or reference**, and **pure, impure and static** methods. |
| Syllabus scope | Need, syntax and forms of methods; static and non-static methods; prototype and signature; actual and formal parameters; call by value and call by reference; pure and impure methods; returning values; method overloading. |
| In short | How to write your own methods in Java, pass values to them, return results and overload methods that share the same name. |

> **Note on the text:** CISCE prescribes no textbook for ICSE Computer Applications; this chapter follows the ICSE 2027 syllabus in its own words. Its questions are the CISCE papers of 2017–2026 and the 2024 and 2025 specimens, answered from CISCE's marking schemes and examiners' comments where published. **Every program was compiled and run (Java 21).**
>
> **Exam note:** Overloading answers are marked **method by method**: the **name given in the question**, the **given return type and parameters**, and the logic. The examiners' reports of 2018–2025 list the same lost marks: **different method names**, **print where the method should return**, **Scanner input inside a method that has parameters**, and patterns **without println() after the inner loop**.

---

## 1. Complete Lesson

### Why we need methods

A **method** is a named block of statements that performs one task and can be **called (invoked)** whenever that task is needed. A program built from small methods is:
- **Modular** — each method does one job (accept, calculate, display), so the program is easier to read.
- **Reusable** — a method written once (say isPrime) can be called many times, even from other programs.
- **Shorter** — no repeated code.
- **Easier to test and correct** — an error is found in one small method.

Java's own methods (Math.sqrt(), charAt(), println()) are **library methods**; the methods you write in your class are **user-defined methods**.

### The syntax of a method

```java
public static int sum(int a, int b)     // method header (prototype)
{
    int s = a + b;                      // method body
    return s;
}
```

![Fig. 6.1 Parts of a method, and how a call passes values in and gets one value back](figures/ca_ch06_fig01_method_anatomy.png)

| Part | In the example | Meaning |
|---|---|---|
| Access specifier | public | Who may call the method: public, private, protected or (none) default |
| Modifier | static | Optional; static makes the method belong to the class |
| Return type | int | The type of the value sent back; **void** if nothing is returned |
| Method name | sum | An identifier, by convention starting with a small letter |
| Parameter list | (int a, int b) | Variables that receive the values sent by the caller; empty brackets if none |
| Method body | { … } | The statements, ending (for a non-void method) with return |

**Method prototype** — the **first line (header)** of the method: access specifier, modifier, return type, name and parameter list, e.g. `public void Accept(int a)`.
**Method signature** — only the **name and the parameter list** (number, types and order of parameters), e.g. `sum(int, int)`. The return type is **not** part of the signature.

### Forms of methods (ways to define a method)

| Form | Example | Called as |
|---|---|---|
| No parameters, no return value | `void line()` prints a line of dashes | `ob.line();` |
| Parameters, no return value | `void table(int n)` prints the table of n | `ob.table(7);` |
| No parameters, returns a value | `int readAge()` reads and returns an age | `int a = ob.readAge();` |
| Parameters and a return value | `boolean isEven(int n)` | `if (ob.isEven(x)) …` |

A method that returns a value is usually called **inside an expression** or an assignment; a void method is called **as a statement on its own**.

### The return statement

- `return value;` sends **one value** back to the caller and **ends the method** at once.
- A method can return **only one value** at a time (ICSE 2023 Q1(ix)).
- The returned value must match the return type (an int can be returned from a double method — it widens — but a double cannot be returned from an int method without a cast).
- A **void** method may use `return;` (with no value) to stop early, but `return n;` in a void method is an error.
- A non-void method must return a value on **every path**; otherwise javac reports *missing return statement*. A statement placed after return is *unreachable*.

| Code | javac's verdict |
|---|---|
| `int f(int n) { if (n > 0) return 1; }` | error: missing return statement |
| `int f(int n) { return n; System.out.println(n); }` | error: unreachable statement |
| `void f(int n) { return n; }` | error: incompatible types: unexpected return value |
| `int f(int n) { return n * 2.5; }` | error: possible lossy conversion from double to int |

### Actual and formal parameters

| Actual parameters (arguments) | Formal parameters |
|---|---|
| The values or variables written **in the call**: `sum(5, 7)` | The variables written **in the method header**: `int a, int b` |
| Belong to the caller | Local to the method; created when the method is called |
| Can be constants, variables or expressions | Must be variables with declared types |

The actual parameters must match the formal parameters in **number, type and order**. An **argument** is the value passed when the method is called (ICSE 2025 specimen Q1(xx)).

### Invoking (calling) a method

- A **non-static** method is called through an **object**: `Overload ob = new Overload(); ob.print();`
- A **static** method is called with the class name, or directly from another static method of the same class: `Temperature2.toFahrenheit(37)` or just `toFahrenheit(37)` inside main.
- Methods of a class can call one another directly: `isPalindrome(n)` can call `reverse(n)`.
- A method returning a value can be used in an expression: `double m = perform(45, 'A');` (ICSE 2026 Improvement Q1(vi)).

### Static and non-static methods

| Static method | Non-static (instance) method |
|---|---|
| Declared with the keyword **static** | Declared without static |
| Belongs to the **class** — "part of a class rather than an instance" (ICSE 2023 Q1(xx)) | Belongs to each **object** |
| Called without creating an object: `ClassName.method()` | Needs an object: `ob.method()` |
| Cannot use instance variables directly | Can use the object's instance variables |
| e.g. `main`, `Math.sqrt()` | e.g. `accept()`, `display()` of a class |

### Ways to invoke: call by value and call by reference

![Fig. 6.2 Call by value copies the value; call by reference lets the method reach the original object](figures/ca_ch06_fig02_value_reference.png)

**Call by value** — the **values** of the actual parameters are **copied** into the formal parameters. Changes made inside the method affect only the copies; the caller's variables do not change. Java passes all **primitive** arguments (int, double, char, boolean …) this way.

```java
void swap(int a, int b)
{
    int t = a;
    a = b;
    b = t;
    System.out.println("Inside: " + a + " " + b);
}
// in main: int a = 5, b = 9; ob.swap(a, b); System.out.println("Outside: " + a + " " + b);
```
Output:
```
Inside: 9 5
Outside: 5 9
```

**Call by reference** — the method receives a **reference** to the original object (or array), so changes made through it **change the original**. In Java this happens when **objects or arrays** are passed: "invoking a method by passing the objects of a class" is call by reference (ICSE 2024 Q1(xvi)).

```java
void shift(Point p)
{
    p.x = p.x + 10;      // changes the caller's object
}
// in main: Point p = new Point(); p.x = 3; ob.shift(p); System.out.println(p.x);   prints 13
```

| Call by value | Call by reference |
|---|---|
| Works with primitive data types | Works with reference (object) types |
| A copy of the value is passed | The reference (address) of the object is passed |
| The original value does not change | The original object can change |
| Pure method | Impure method |

*(Strictly, Java copies the reference too; the method still reaches the same object, which is why the ICSE syllabus calls passing an object "call by reference".)*

### Pure and impure methods

- A **pure method** does **not change** the state of the object or the values of its arguments; it usually works on its parameters and **returns** a result. Calling it again with the same values gives the same result. Example: `int reverse(int n)` returns the reverse of n and changes nothing else — ICSE 2024 Q1(xiv) calls the method that reverses a number a pure method. Pure methods are also called **accessors**.
- An **impure method** **changes** the state of an object (its member variables) or of an object passed to it. Example: `shift(Point p)` above, or a deposit() method that adds to the balance. Impure methods are also called **modifiers (mutators)**.

### Method overloading (polymorphism)

**Method overloading** means defining **two or more methods with the same name in one class**, differing in their **parameter lists** — the number of parameters, their types, or their order. It is a form of **polymorphism** ("many forms"): one name, several behaviours. A calculator with several calculate() methods for different operations uses polymorphism (ICSE 2026 Q1(xi)).

```java
int max(int a, int b)
int max(int a, int b, int c)       // different number
double max(double a, double b)     // different types
char max(char a, char b)
```

**Rules:**
1. The names must be the **same**; the parameter lists must be **different**.
2. A difference in **return type alone is not overloading** — `void test(int a)` and `int test(int a)` give *method test(int) is already defined* (ICSE 2025 Q1(xv)).
3. The access specifier or parameter names alone do not make a new method.

**How Java chooses the method (resolution):**
- An **exact match** of argument types is chosen first: `show(7)` calls show(int); `show(7.0)` calls show(double).
- Otherwise Java **widens** the argument: a char goes to int (`show('A')` prints `int 65`), an int goes to long, float or double (`only(7)` with only `only(double)` prints `only 7.0`).
- If two methods fit equally well the call is **ambiguous**: with `test(int, double)` and `test(double, int)`, the call `test(1, 2)` gives *reference to test is ambiguous* (the two declarations themselves compile).

### Writing an overloading program for Section B

A complete answer has one class, all methods with the **same name**, each with the parameters and return type given, and (good practice) a main method that creates an object and calls every version:

```java
class Overload
{
    void print()                    { ... }           // pattern with nested loops
    double print(double a, double b) { ... return s; } // returns: do not just print
    int print(char ch1, char ch2)    { ... return ...; }

    public static void main(String args[])
    {
        Overload ob = new Overload();
        ob.print();
        System.out.println(ob.print(1.0, 4.0));
        System.out.println(ob.print('a', 'Z'));
    }
}
```

Checklist from the examiners' reports:
- Use **the parameters** the method receives; do not read new values with Scanner inside it.
- **void** → display the result inside the method; **int / double / boolean / char** → **return** it.
- Patterns: **nested loops**, with `System.out.println()` **after the inner loop**.
- Sums: declare the sum variable, initialise it (0 or 0.0) **before** the loop and print it **after** the loop.
- For series like 1/2 + 1/3 + …, use `1.0 / i` (or a cast) so the division is not integer division.

### Modular programming: several methods with different names

Large tasks are split into small methods with different names, each calling the next: `isPalindrome(n)` calls `reverse(n)`, main calls both with `isPrime(n)` to list palindromic primes. Each method is short, testable and reusable.

### Summary of the chapter

- **Method** — a named block for one task; header (prototype) + body; reusable and modular.
- **Prototype** = header line; **signature** = name + parameter list.
- **Four forms** — with or without parameters, with or without a return value; **return** sends one value and ends the method.
- **Actual** parameters in the call, **formal** in the header — matched in number, type and order.
- **Static** methods belong to the class; **non-static** ones are called through an object.
- **Call by value** (primitives, originals unchanged, pure) vs **call by reference** (objects, originals can change, impure).
- **Overloading** — same name, different parameter lists; return type alone is not enough; exact match, then widening.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Explain the need for methods and write methods in all four forms.
2. Name the parts of a method header and distinguish a prototype from a signature.
3. Distinguish actual from formal parameters, static from non-static methods, and pure from impure methods.
4. Explain call by value with a program and call by reference with an example.
5. Use return correctly and predict javac's errors for missing or wrong returns.
6. Write and call overloaded methods, and predict which version a call chooses.

---

## 3. Detailed Section Explanations

### Section 1 — One task, one method
Name each method for its task (accept, calculate, isPrime). If a method needs a value, give it a parameter; if the caller needs a result, return it.

### Section 2 — The header is a contract
The prototype says exactly what goes in (parameter list) and what comes out (return type). The question's prototype must be copied exactly.

### Section 3 — Copies and references
Primitive arguments arrive as copies; objects arrive as references to the same object. That is the whole difference between call by value and call by reference.

### Section 4 — Same name, different lists
Overloaded methods share a name; Java tells them apart only by their parameter lists, never by the return type.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Method | A named block of statements that performs a task. |
| User-defined method | A method written by the programmer. |
| Method header / prototype | The first line: access specifier, modifier, return type, name, parameters. |
| Method signature | The method name with its parameter list. |
| Return type | The type of value a method sends back; void if none. |
| return | The statement that sends a value back and ends the method. |
| Actual parameters | Values or variables passed in the method call (arguments). |
| Formal parameters | Variables in the method header that receive the values. |
| Call by value | Passing copies of values; the originals do not change. |
| Call by reference | Passing a reference to an object; the original can change. |
| Pure method | A method that does not change the state of objects or its arguments. |
| Impure method | A method that changes the state of an object. |
| Static method | A method that belongs to the class and needs no object. |
| Non-static method | A method called through an object. |
| Method overloading | Several methods with the same name and different parameter lists. |
| Polymorphism | One name taking many forms; overloading is one kind. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| Number of values a method can return | 1 |
| Statement that returns control to the caller | return |
| Prototype of check() taking an int and returning a char | `char check(int x)` |
| Prototype of compute() taking two ints and returning true/false | `boolean compute(int a, int b)` |
| Return type for "YES" or "NO" | String |
| `public void Accept(int a)` is a | method prototype |
| `int check(char ch, String s)` | has return type int |
| Invoking a method by passing objects | call by reference |
| Method that does not modify variables | pure method |
| Method that reverses a given number | pure method |
| Method belonging to the class, not an instance | static method |
| Several calculate() methods in a calculator | polymorphism (overloading) |
| `void test(int a)` and `int test(int a)` | compile-time error: not valid overloading |

### 5.2 Memory aids

- **"Prototype = whole Header; Signature = Name + List"** (P-H, S-NL).
- **"Value copies, Reference reaches"** — call by value copies; call by reference reaches the original.
- **"Pure Preserves, Impure Modifies."**
- **"Overload by the List, never by the Return."**

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- System.out.println is itself overloaded: there are versions for int, double, char, boolean, String and more.
- A method can call itself; this is called recursion.
- Java runs every method call on a "call stack": each call gets its own fresh set of local variables and formal parameters.

---

## 6. Person Profiles

### 6.1 David Wheeler (1927–2004)
A British computer scientist at the University of Cambridge who, while programming the EDSAC computer around 1950, devised the closed subroutine — a block of code that could be called from anywhere and return to the caller. Every Java method descends from this idea.

### 6.2 Christopher Strachey (1916–1975)
A British computer scientist who, in 1967 lecture notes, named and separated two kinds of polymorphism — "ad hoc" polymorphism, which includes overloading one name for different types, and "parametric" polymorphism. The words programmers still use for overloading come from his work.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Divide and conquer** — a big problem becomes several small methods.
- **Black box** — a caller needs only the prototype, not the code inside.
- **One name, many forms** — overloading keeps related operations under one easy name.

### 7.2 Real-life connections
- **Calculator apps:** add() for whole numbers and add() for decimals — overloading.
- **Meghalaya:** a school fee system might have calculateFee(int classNo) and calculateFee(int classNo, boolean hostel).
- **Banking:** checkBalance() is pure (changes nothing); deposit() is impure (changes the balance).

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section B** (60 marks, any four of six programs) has had a **method-overloading program** in every paper since 2017, worth 15 marks. **Section A** has MCQs and 2-mark parts on prototypes, return values, parameters, pure and impure methods, static methods and call by value or reference.

### 8.1 Graded exercises — solutions

#### Exercise 6A — Concepts

**Q1.** Write the prototype of a method area that takes a double radius and returns a double.
**Answer:** `double area(double r)`

**Q2.** In `int t = ob.sum(x, 4);` and `int sum(int a, int b)`, name the actual and formal parameters.
**Answer:** Actual: x and 4. Formal: a and b.

**Q3.** Can `int f(int a)` and `double f(int b)` be in the same class? Why?
**Answer:** No — their parameter lists are the same (one int); a different return type or parameter name does not overload.

**Q4.** Is `void deposit(double amt) { balance = balance + amt; }` pure or impure?
**Answer:** Impure — it changes the member variable balance.

#### Exercise 6B — Tracing and writing

**Q5.** Give the output: `int square(int n) { return n * n; }` and `System.out.println(ob.square(ob.square(3)));`
**Answer:** 81 — square(3) is 9, square(9) is 81.

**Q6.** With `void show(int n)`, `void show(long n)` and `void show(double d)`, which is called by `ob.show('A')` and what is printed?
**Answer:** show(int) — the char widens to int; it prints `int 65`.

**Q7.** Write a method `boolean isEven(int n)` and use it in a statement that prints "Even" for x.
**Answer:** `boolean isEven(int n) { return n % 2 == 0; }` and `if (ob.isEven(x)) System.out.println("Even");`

**Q8.** Write the overloaded prototypes for a method volume that finds the volume of a cube (one double) and of a cuboid (three doubles).
**Answer:** `double volume(double s)` and `double volume(double l, double b, double h)`
### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(x) (1 mark) | In the following method prototype to accept a character, an integer and return YES or NO, fill in the blank to complete the method prototype: `public __________ someMethod(char ch, int n)` (a) boolean (b) String (c) int (d) double |
| ICSE 2026, Q1(xi) (1 mark) | In a calculator, which Java feature allows multiple methods named calculate() for the different operations? (a) abstraction (b) inheritance (c) encapsulation (d) polymorphism |
| ICSE 2026, Q7 (15 marks) | Define a class to overload the method format as follows: void format() — to print the following pattern using nested for loops only: 1 2 3 4 5 / 2 3 4 5 / 3 4 5 / 4 5 / 5. int format(String s) — to calculate and return the sum of ASCII codes of each character of the String. Example: CAB; Output: 67 + 65 + 66, 198. void format(int n) — to calculate and display the sum of natural numbers up to n given by the formula n(n + 1)/2. |
| ICSE 2026 Improvement, Q1(vi) (1 mark) | The right statement to invoke the method perform which accepts an integer and a character and returns a double value: (a) `perform(45, 'A')` (b) `double m = perform(45, 'A')` (c) `double m = perform("A", 45)` (d) `perform('A', 45)` |
| ICSE 2026 Improvement, Q2(ix) (2 marks) | Write the prototype of the method CALCULATE which accepts two integers and a String and displays a formatted output. |
| ICSE 2026 Improvement, Q7 (15 marks) | Define a class to overload the method display as follows: void display() — to display the format using NESTED LOOPS only: 1 2 3 / 4 5 6 / 7 8 9. void display(int n, char ch) — to print the square root of n if ch is 'S' or print the cube root of n if ch is 'C'. double display(double r, double h) — to return the volume of a cylinder as follows: volume = area × h, area = πr². |
| ICSE 2025, Q1(xv) (1 mark) | Which of the following pairs of methods will cause a compile-time error due to incorrect method overloading? (a) `void test(int a, int b)` and `void test(double a, double b)` (b) `void test(int a, double b)` and `void test(double a, int b)` (c) `void test(int a, double b)` and `void test(int a)` (d) `void test(int a)` and `int test(int a)` |
| ICSE 2025, Q7 (15 marks) | Define a class to overload the method print() as follows: void print() — to print the given format using nested loops: @#@#@ (four rows). double print(double a, double b) — to display the sum of numbers between a and b with difference of 0.5, e.g. if a = 1.0, b = 4.0 output is: 1.0 + 1.5 + 2.0 + 2.5 + … + 4.0. int print(char ch1, char ch2) — compare the two characters and return the ASCII code of the largest character. |
| ICSE 2025 Improvement, Q1(iii) (1 mark) | Which statement is correct for the method prototype given below: `int check(char ch, String s)` (a) check() does not return any value (b) check() has return type int (c) check method has two actual parameters (d) check() is a constructor |
| ICSE 2025 Improvement, Q1(xii) (1 mark) | The statement given below is termed as: `public void Accept(int a)` (a) Method signature (b) Method block (c) Method prototype (d) Constructor |
| ICSE 2025 Improvement, Q5 (15 marks) | Define a class to overload the method transform as follows: int transform(int n) — to return the sum of the digits of the given number. Example: n = 458, output: 17. void transform(String s) — to convert the given String to upper case and print. Example: if S = "Blue", Output: BLUE. void transform(char ch) — to print the character ch in 3 rows and 3 columns using nested loops. Example: if ch = '@', Output: @@@ / @@@ / @@@. |
| ICSE 2025 specimen, Q1(xii) (1 mark) | Method prototype for the method compute which accepts two integer arguments and returns true/false: (a) `void compute(int a, int b)` (b) `boolean compute(int a, int b)` (c) `Boolean compute(int a,b)` (d) `int compute(int a, int b)` |
| ICSE 2025 specimen, Q1(xiii) (1 mark) | The statement that brings the control back to the calling method is: (a) break (b) System.exit(0) (c) continue (d) return |
| ICSE 2025 specimen, Q1(xix) (1 mark) | Consider the following program segment in which the statements are jumbled; choose the correct order of statements to swap two variables using the third variable. `void swap(int a, int b) { a = b; (1) b = t; (2) int t = 0; (3) t = a; (4) }` (a) (1) (2) (3) (4) (b) (3) (4) (1) (2) (c) (1) (3) (4) (2) (d) (2) (1) (4) (3) |
| ICSE 2025 specimen, Q1(xx) (1 mark) | Assertion (A): An argument is a value that is passed to a method when it is called. Reason (R): Variables which are declared in a method prototype to receive values are called actual parameters. (a) Both A and R are true and R is a correct explanation of A (b) Both A and R are true and R is not a correct explanation of A (c) A is true and R is false (d) A is false and R is true |
| ICSE 2025 specimen, Q8 (15 marks) | Define a class to overload the method display() as follows: void display() — to print the following format using nested loop: 1 2 1 2 1 / 1 2 1 2 1 / 1 2 1 2 1. void display(int n, int m) — to print the quotient of the division of m and n if m is greater than n, otherwise print the sum of twice n and thrice m. double display(double a, double b, double c) — to print the value of z where z = p × q, p = (a + b)/c, q = a + b + c. |
| ICSE 2024, Q1(xiv) (1 mark) | Method which reverses a given number is: (a) Impure method (b) Pure method (c) Constructor (d) Destructor |
| ICSE 2024, Q1(xvi) (1 mark) | Invoking a method by passing the objects of a class is termed as: (a) Call by reference (b) Call by value (c) Call by method (d) Call by constructor |
| ICSE 2024, Q4 (15 marks) | Define a class to overload the method perform as follows: double perform(double r, double h) — to calculate and return the value of the curved surface area of a cone, CSA = πrl, where l = √(r² + h²). void perform(int r, int c) — use NESTED FOR LOOP to generate the following format for r = 4, c = 5: 1 2 3 4 5 (four rows). void perform(int m, int n, char ch) — to print the quotient of the division of m and n if ch is Q, else print the remainder of the division of m and n if ch is R. |
| ICSE 2024 specimen, Q1(xix) (1 mark) | Assertion (A): Call by value is known as pure method. Reason (R): The original value of variable does not change as operation is performed on copied values. (a) Both A and R are true and R is a correct explanation of A (b) Both A and R are true and R is not a correct explanation of A (c) A is false and R is true (d) A is false and R is true |
| ICSE 2024 specimen, Q8 (15 marks) | Define a class to overload the method display as follows: void display() — to print the following format using nested loop: 1 / 1 2 / 1 2 3 / 1 2 3 4 / 1 2 3 4 5. void display(int n) — to print the square root of each digit of the given number. Example: n = 4329, output: 3.0, 1.414213562, 1.732050808, 2.0. |
| ICSE 2023, Q1(ix) (1 mark) | The number of values that a method can return is: (a) 1 (b) 2 (c) 3 (d) 4 |
| ICSE 2023, Q1(viii) (1 mark) | Write a method prototype name check() which takes an integer argument and returns a char: (a) `char check()` (b) `void check(int x)` (c) `check(int x)` (d) `char check(int x)` |
| ICSE 2023, Q1(xvii) (1 mark) | A method which does not modify the value of variables is termed as: (a) Impure method (b) Pure method (c) Primitive method (d) User defined method |
| ICSE 2023, Q1(xx) (1 mark) | Method which is a part of a class rather than an instance of the class is termed as: (a) Static method (b) Non static method (c) Wrapper class (d) String method |
| ICSE 2023, Q5 (15 marks) | Define a class to overload the function print as follows: void print() — to print the following format: 1 1 1 1 / 2 2 2 2 / 3 3 3 3 / 4 4 4 4 / 5 5 5 5. void print(int n) — to check whether the number is a lead number. A lead number is the one whose sum of even digits is equal to the sum of odd digits, e.g. 3669: odd digits sum = 3 + 9 = 12, even digits sum = 6 + 6 = 12, so 3669 is a lead number. |
| ICSE 2020, Q7 (15 marks) | Design a class to overload a method Number() as follows: (i) void Number(int num, int d) — to count and display the frequency of a digit in a number. Example: num = 2565685, d = 5; Frequency of digit 5 = 3. (ii) void Number(int n1) — to find and display the sum of even digits of a number. Example: n1 = 29865; Sum of even digits = 16. Write a main method to create an object and invoke the above methods. |
| ICSE 2019, Q3(e) (2 marks) | State a difference between call by value and call by reference. |
| ICSE 2019, Q7 (15 marks) | Design a class to overload a function series() as follows: (a) void series(int x, int n) — to display the sum of the series x¹ + x² + x³ + … + xⁿ terms. (b) void series(int p) — to display the following series: 0, 7, 26, 63, … p terms. (c) void series() — to display the sum of the series 1/2 + 1/3 + 1/4 + … + 1/10. |
| ICSE 2018, Q2(d) (2 marks) | Write the prototype of a function check which takes an integer as an argument and returns a character. |
| ICSE 2018, Q7 (15 marks) | Design a class to overload a function volume() as follows: (i) double volume(double R) — with radius (R) as an argument, returns the volume of a sphere using the formula V = 4/3 × 22/7 × R³. (ii) double volume(double H, double R) — with height (H) and radius (R) as the arguments, returns the volume of a cylinder using the formula V = 22/7 × R² × H. (iii) double volume(double L, double B, double H) — with length (L), breadth (B) and height (H) as the arguments, returns the volume of a cuboid using the formula V = L × B × H. |
| ICSE 2017, Q2(b) (2 marks) | What are the two ways of invoking functions? |
| ICSE 2017, Q8 (15 marks) | Design a class to overload a function check() as follows: (i) void check(String str, char ch) — to find and print the frequency of a character in a string. Example: str = "success", ch = 's'; Output: number of s present is = 3. (ii) void check(String s1) — to display only vowels from string s1, after converting it to lower case. Example: s1 = "computer"; Output: o u e. |

**Solutions**

**2026 Q1(x).** **(b) String** — "YES" and "NO" are words, so the method returns a String. *(Worked answer.)*

**2026 Q1(xi).** **(d) polymorphism** — several methods with one name (method overloading) is polymorphism. *(Worked answer.)*

**2026 Q7.** All three methods are named format; they differ in their parameter lists. The String version prints the codes and returns the total.
```java
class OverloadFormat
{
    void format()
    {
        for (int i = 1; i <= 5; i++)
        {
            for (int j = i; j <= 5; j++)
                System.out.print(j + " ");
            System.out.println();
        }
    }

    int format(String s)
    {
        int sum = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            sum = sum + (int) ch;
            System.out.print((int) ch);
            if (i < s.length() - 1)
                System.out.print(" + ");
        }
        System.out.println();
        return sum;
    }

    void format(int n)
    {
        int sum = n * (n + 1) / 2;
        System.out.println("Sum of natural numbers up to " + n + " = " + sum);
    }

    public static void main(String args[])
    {
        OverloadFormat ob = new OverloadFormat();
        ob.format();
        int s = ob.format("CAB");
        System.out.println(s);
        ob.format(10);
    }
}
```
Output:
```
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
67 + 65 + 66
198
Sum of natural numbers up to 10 = 55
```
*(Worked answer.)*

**2026 Improvement Q1(vi).** **(b) `double m = perform(45, 'A')`** — the arguments are in the order int, char, and the returned double is stored. *(Worked answer.)*

**2026 Improvement Q2(ix).** `void CALCULATE(int a, int b, String s)` — void, because the method displays the output instead of returning it. *(Worked answer.)*

**2026 Improvement Q7.** A counter k runs from 1 to 9 inside the nested loops; Math.cbrt() gives the cube root.
```java
class OverloadDisplay
{
    void display()
    {
        int k = 1;
        for (int i = 1; i <= 3; i++)
        {
            for (int j = 1; j <= 3; j++)
            {
                System.out.print(k + " ");
                k++;
            }
            System.out.println();
        }
    }

    void display(int n, char ch)
    {
        if (ch == 'S')
            System.out.println("Square root = " + Math.sqrt(n));
        else if (ch == 'C')
            System.out.println("Cube root = " + Math.cbrt(n));
        else
            System.out.println("Invalid choice");
    }

    double display(double r, double h)
    {
        double area = Math.PI * r * r;
        double volume = area * h;
        return volume;
    }

    public static void main(String args[])
    {
        OverloadDisplay ob = new OverloadDisplay();
        ob.display();
        ob.display(64, 'S');
        ob.display(64, 'C');
        double v = ob.display(7.0, 10.0);
        System.out.println("Volume of the cylinder = " + v);
    }
}
```
Output:
```
1 2 3
4 5 6
7 8 9
Square root = 8.0
Cube root = 4.0
Volume of the cylinder = 1539.3804002589986
```
*(Worked answer.)*

**2025 Q1(xv).** **(d) `void test(int a)` and `int test(int a)`** — the parameter lists are the same; a different return type alone is not overloading (javac: method test(int) is already defined). Pair (b) compiles, although a call such as test(1, 2) would be ambiguous.

**2025 Q7.** As in the marking scheme (which has two typing slips, "]" after the if and "rerurn"), with the series also displayed:
```java
class OverloadPrint
{
    void print()
    {
        for (int i = 1; i <= 4; i++)
        {
            for (int j = 1; j <= 5; j++)
            {
                if (j % 2 == 0)
                    System.out.print("#");
                else
                    System.out.print("@");
            }
            System.out.println();
        }
    }

    double print(double a, double b)
    {
        double s = 0.0;
        for (double x = a; x <= b; x = x + 0.5)
        {
            System.out.print(x);
            if (x < b)
                System.out.print(" + ");
            s = s + x;
        }
        System.out.println();
        return s;
    }

    int print(char ch1, char ch2)
    {
        if (ch1 > ch2)
            return (int) ch1;
        else
            return (int) ch2;
    }

    public static void main(String args[])
    {
        OverloadPrint ob = new OverloadPrint();
        ob.print();
        double s = ob.print(1.0, 4.0);
        System.out.println("Sum = " + s);
        System.out.println("ASCII code of the larger character = " + ob.print('a', 'Z'));
    }
}
```
Output:
```
@#@#@
@#@#@
@#@#@
@#@#@
1.0 + 1.5 + 2.0 + 2.5 + 3.0 + 3.5 + 4.0
Sum = 17.5
ASCII code of the larger character = 97
```
The examiners noted these errors: separate programs instead of one overloaded method, println() inside both loops of the pattern, the loops reversed, print used instead of return, and a loop that could not step by 0.5.

**2025 Improvement Q1(iii).** **(b) check() has return type int.** *(Worked answer.)*

**2025 Improvement Q1(xii).** **(c) Method prototype** — the whole header line (the paper prints "pubic", a misprint for public). *(Worked answer.)*

**2025 Improvement Q5.**
```java
class OverloadTransform
{
    int transform(int n)
    {
        int sum = 0;
        while (n > 0)
        {
            sum = sum + n % 10;
            n = n / 10;
        }
        return sum;
    }

    void transform(String s)
    {
        System.out.println(s.toUpperCase());
    }

    void transform(char ch)
    {
        for (int i = 1; i <= 3; i++)
        {
            for (int j = 1; j <= 3; j++)
                System.out.print(ch);
            System.out.println();
        }
    }

    public static void main(String args[])
    {
        OverloadTransform ob = new OverloadTransform();
        System.out.println(ob.transform(458));
        ob.transform("Blue");
        ob.transform('@');
    }
}
```
Output:
```
17
BLUE
@@@
@@@
@@@
```
*(Worked answer.)*

**2025 specimen Q1(xii).** **(b) `boolean compute(int a, int b)`**

**2025 specimen Q1(xiii).** **(d) return**

**2025 specimen Q1(xix).** **(b) (3) (4) (1) (2)** — `int t = 0; t = a; a = b; b = t;`

**2025 specimen Q1(xx).** **(c) A is true and R is false** — the variables in the prototype are formal parameters, not actual parameters.

**2025 specimen Q8.** The draft scheme prints 2 in even columns and 1 in odd columns:
```java
class OverloadDisplay2
{
    void display()
    {
        for (int r = 1; r <= 3; r++)
        {
            for (int c = 1; c <= 5; c++)
            {
                if (c % 2 == 0)
                    System.out.print("2 ");
                else
                    System.out.print("1 ");
            }
            System.out.println();
        }
    }

    void display(int n, int m)
    {
        if (m > n)
            System.out.println("Quotient = " + (m / n));
        else
            System.out.println("Sum = " + (2 * n + 3 * m));
    }

    double display(double a, double b, double c)
    {
        double p = (a + b) / c;
        double q = a + b + c;
        double z = p * q;
        System.out.println("z = " + z);
        return z;
    }

    public static void main(String args[])
    {
        OverloadDisplay2 ob = new OverloadDisplay2();
        ob.display();
        ob.display(4, 25);
        ob.display(9, 5);
        ob.display(2.0, 4.0, 3.0);
    }
}
```
Output (display(4, 25) gives 25/4; display(9, 5) gives 2 × 9 + 3 × 5):
```
1 2 1 2 1
1 2 1 2 1
1 2 1 2 1
Quotient = 6
Sum = 33
z = 18.0
```

**2024 Q1(xiv).** **(b) Pure method**

**2024 Q1(xvi).** **(a) Call by reference**

**2024 Q4.** The scheme's version prints each number on its own line, because its println() is inside the inner loop, and it misses a semicolon. The examiners asked for println() **after** the inner loop, as here:
```java
class OverloadPerform
{
    double perform(double r, double h)
    {
        double l = Math.sqrt(r * r + h * h);
        double csa = 22.0 / 7 * r * l;
        return csa;
    }

    void perform(int r, int c)
    {
        for (int x = 1; x <= r; x++)
        {
            for (int y = 1; y <= c; y++)
                System.out.print(y + " ");
            System.out.println();
        }
    }

    void perform(int m, int n, char ch)
    {
        if (ch == 'Q' || ch == 'q')
            System.out.println("Quotient = " + (m / n));
        else if (ch == 'R' || ch == 'r')
            System.out.println("Remainder = " + (m % n));
        else
            System.out.println("Invalid choice");
    }

    public static void main(String args[])
    {
        OverloadPerform ob = new OverloadPerform();
        System.out.println("CSA = " + ob.perform(3.0, 4.0));
        ob.perform(4, 5);
        ob.perform(17, 5, 'Q');
        ob.perform(17, 5, 'R');
    }
}
```
Output:
```
CSA = 47.142857142857146
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
Quotient = 3
Remainder = 2
```
The examiners also noted these errors: input taken inside the methods instead of using the arguments, print used instead of return for the CSA, and m/n and m%n calculated but not printed.

**2024 specimen Q1(xix).** **(a) Both A and R are true and R is a correct explanation of A** — the ICSE 2019 marking scheme also calls call by value a pure function, because the original values do not change. (The paper prints options (c) and (d) the same.) *(Worked answer.)*

**2024 specimen Q8.** Digits come out from the right, so 4329 gives √9, √2, √3, √4. Java prints the full double, not the nine decimal places of the example.
```java
class OverloadDisplay3
{
    void display()
    {
        for (int i = 1; i <= 5; i++)
        {
            for (int j = 1; j <= i; j++)
                System.out.print(j + " ");
            System.out.println();
        }
    }

    void display(int n)
    {
        while (n > 0)
        {
            int d = n % 10;
            System.out.println(Math.sqrt(d));
            n = n / 10;
        }
    }

    public static void main(String args[])
    {
        OverloadDisplay3 ob = new OverloadDisplay3();
        ob.display();
        ob.display(4329);
    }
}
```
Output:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
3.0
1.4142135623730951
1.7320508075688772
2.0
```
*(Worked answer.)*

**2023 Q1(ix).** **(a) 1**

**2023 Q1(viii).** **(d) `char check(int x)`**

**2023 Q1(xvii).** **(b) Pure method**

**2023 Q1(xx).** **(a) Static method**

**2023 Q5.** The marking scheme makes both methods static and calls them from main without an object; the version below uses an object, which is equally correct.
```java
class OverloadPrint2
{
    void print()
    {
        for (int i = 1; i <= 5; i++)
        {
            for (int j = 1; j <= 4; j++)
                System.out.print(i + " ");
            System.out.println();
        }
    }

    void print(int n)
    {
        int even = 0, odd = 0, num = n;
        while (n > 0)
        {
            int d = n % 10;
            if (d % 2 == 0)
                even = even + d;
            else
                odd = odd + d;
            n = n / 10;
        }
        if (even == odd)
            System.out.println(num + " is a lead number");
        else
            System.out.println(num + " is not a lead number");
    }

    public static void main(String args[])
    {
        OverloadPrint2 ob = new OverloadPrint2();
        ob.print();
        ob.print(3669);
        ob.print(1234);
    }
}
```
Output:
```
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
5 5 5 5
3669 is a lead number
1234 is not a lead number
```
The examiners noted that many candidates did not use overloading or the given method name, printed the pattern without nested loops, or could not extract the digits.

**2020 Q7.**
```java
class OverloadNumber
{
    void Number(int num, int d)
    {
        int count = 0, n = num;
        while (n > 0)
        {
            if (n % 10 == d)
                count++;
            n = n / 10;
        }
        System.out.println("Frequency of digit " + d + " = " + count);
    }

    void Number(int n1)
    {
        int sum = 0;
        while (n1 > 0)
        {
            int dg = n1 % 10;
            if (dg % 2 == 0)
                sum = sum + dg;
            n1 = n1 / 10;
        }
        System.out.println("Sum of even digits = " + sum);
    }

    public static void main(String args[])
    {
        OverloadNumber ob = new OverloadNumber();
        ob.Number(2565685, 5);
        ob.Number(29865);
    }
}
```
Output:
```
Frequency of digit 5 = 3
Sum of even digits = 16
```
*(Worked answer.)*

**2019 Q3(e).** Any one difference, from the scheme:
- Call by value works with primitive data types; call by reference works with reference data types.
- In call by value the original value does not change; in call by reference it can change.
- Call by value works on duplicate values; call by reference works on the original values.
- Call by value is a pure function; call by reference is an impure function.

**2019 Q7.** The logic follows the marking scheme (which makes the methods static). The term of (b) is i³ − 1, and (c) starts at i = 2 with `1.0 / i`:
```java
class OverloadSeries
{
    void series(int x, int n)
    {
        double sum = 0.0;
        for (int i = 1; i <= n; i++)
            sum = sum + Math.pow(x, i);
        System.out.println("Sum = " + sum);
    }

    void series(int p)
    {
        for (int i = 1; i <= p; i++)
            System.out.print((i * i * i - 1) + " ");
        System.out.println();
    }

    void series()
    {
        double sum = 0.0;
        for (int i = 2; i <= 10; i++)
            sum = sum + 1.0 / i;
        System.out.println("Sum = " + sum);
    }

    public static void main(String args[])
    {
        OverloadSeries ob = new OverloadSeries();
        ob.series(2, 5);
        ob.series(5);
        ob.series();
    }
}
```
Output (for series(2, 5), series(5) and series()):
```
Sum = 62.0
0 7 26 63 124
Sum = 1.928968253968254
```
The examiners noted that the sum variable was often not declared or not double, the loop for (c) began at 1, and the output statement was put inside the loop.

**2018 Q2(d).** `char check(int n)`

**2018 Q7.** As in the marking scheme (which writes `Math.pow(R, 3)`; `R * R * R` is the same):
```java
class OverloadVolume
{
    double volume(double R)
    {
        double V = 4.0 / 3 * 22.0 / 7 * R * R * R;
        return V;
    }

    double volume(double H, double R)
    {
        double V = 22.0 / 7 * R * R * H;
        return V;
    }

    double volume(double L, double B, double H)
    {
        double V = L * B * H;
        return V;
    }

    public static void main(String args[])
    {
        OverloadVolume ob = new OverloadVolume();
        System.out.println("Sphere   : " + ob.volume(7.0));
        System.out.println("Cylinder : " + ob.volume(10.0, 7.0));
        System.out.println("Cuboid   : " + ob.volume(5.0, 4.0, 3.0));
    }
}
```
Output (R = 7; H = 10, R = 7; 5 × 4 × 3):
```
Sphere   : 1437.3333333333335
Cylinder : 1540.0
Cuboid   : 60.0
```
The examiners noted these errors: void with a return statement, double with println() but no return, a capital R in "Return", R3 written for R*R*R, and three methods with different names.

**2017 Q2(b).** Call by value and call by reference. *(Worked answer.)*

**2017 Q8.**
```java
class OverloadCheck
{
    void check(String str, char ch)
    {
        int count = 0;
        for (int i = 0; i < str.length(); i++)
        {
            if (str.charAt(i) == ch)
                count++;
        }
        System.out.println("number of " + ch + " present is = " + count);
    }

    void check(String s1)
    {
        s1 = s1.toLowerCase();
        for (int i = 0; i < s1.length(); i++)
        {
            char ch = s1.charAt(i);
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                System.out.print(ch + " ");
        }
        System.out.println();
    }

    public static void main(String args[])
    {
        OverloadCheck ob = new OverloadCheck();
        ob.check("success", 's');
        ob.check("COMPUTER");
    }
}
```
Output:
```
number of s present is = 3
o u e
```
*(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Write the prototype of a method isPerfect that takes an int and returns true or false.
**Answer:** `boolean isPerfect(int n)`

**Q2.** (2 marks) Give the output of `ob.show(7L);` with show(int), show(long) and show(double) defined.
**Answer:** `long 7` — the exact match show(long) is chosen.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 15 marks | Overload a method: a nested-loop pattern + a digit/number method + a formula or String method | 8.2, Section 11 |
| MCQ | Prototype for given parameters and return type; return type for a YES/NO answer | 8.2, 5.1 |
| MCQ / 2 marks | Pure vs impure; call by value vs reference; static method; actual vs formal | 8.2, Section 1 |
| MCQ | Which pair is not valid overloading | 8.2 (2025 Q1(xv)) |

---
## 9. MCQs with Explanations

### Methods and their syntax (Q1–Q14)

**Q1.** A method is
- (a) a named block of statements that performs a task
- (b) a variable that stores many values
- (c) a comment in a program
- (d) a package of classes

**Answer:** (a) a named block of statements that performs a task
**Explanation:** It runs whenever it is called.

**Q2.** Which of these is NOT a benefit of using methods?
- (a) reuse of code
- (b) modular programs
- (c) easier debugging
- (d) a longer program with repeated code

**Answer:** (d) a longer program with repeated code
**Explanation:** Methods remove repetition.

**Q3.** The first line of a method, giving its return type, name and parameters, is the
- (a) method body
- (b) return statement
- (c) method call
- (d) method prototype

**Answer:** (d) method prototype
**Explanation:** Also called the method header.

**Q4.** A method signature consists of
- (a) the return type and the name
- (b) the name and the parameter list
- (c) the access specifier only
- (d) the whole method body

**Answer:** (b) the name and the parameter list
**Explanation:** The return type is not part of it.

**Q5.** In public static int sum(int a, int b), the return type is
- (a) public
- (b) static
- (c) int
- (d) sum

**Answer:** (c) int
**Explanation:** It comes just before the name.

**Q6.** In the same header, the word public is the
- (a) access specifier
- (b) modifier
- (c) return type
- (d) method name

**Answer:** (a) access specifier
**Explanation:** It controls who can call the method.

**Q7.** A method that returns no value has the return type
- (a) null
- (b) void
- (c) empty
- (d) int

**Answer:** (b) void
**Explanation:** void means nothing is returned.

**Q8.** The statement public void Accept(int a) is termed a
- (a) method signature
- (b) method block
- (c) method prototype
- (d) constructor

**Answer:** (c) method prototype
**Explanation:** It is the full header line.

**Q9.** For the prototype int check(char ch, String s), which statement is correct?
- (a) check() returns no value
- (b) check() has two actual parameters
- (c) check() has return type int
- (d) check() is a constructor

**Answer:** (c) check() has return type int
**Explanation:** ch and s are formal parameters.

**Q10.** The prototype of compute, which accepts two integers and returns true or false, is
- (a) void compute(int a, int b)
- (b) boolean compute(int a, int b)
- (c) Boolean compute(int a,b)
- (d) int compute(int a, int b)

**Answer:** (b) boolean compute(int a, int b)
**Explanation:** true/false is boolean; each parameter needs a type.

**Q11.** The prototype of check(), which takes an integer argument and returns a char, is
- (a) char check()
- (b) void check(int x)
- (c) check(int x)
- (d) char check(int x)

**Answer:** (d) char check(int x)
**Explanation:** Return type char, one int parameter.

**Q12.** A method that accepts a character and an integer and returns YES or NO has the return type
- (a) boolean
- (b) int
- (c) String
- (d) double

**Answer:** (c) String
**Explanation:** "YES" and "NO" are strings.

**Q13.** Which of these is a library method?
- (a) a calculate() method written by the programmer
- (b) an accept() method written in the class
- (c) Math.sqrt()
- (d) a display() method written for the program

**Answer:** (c) Math.sqrt()
**Explanation:** It is built into Java; the others are user-defined.

**Q14.** The prototype of CALCULATE, which accepts two integers and a String and displays a formatted output, is
- (a) void CALCULATE(int a, int b, s)
- (b) int CALCULATE(int a, int b, String s)
- (c) CALCULATE(int a, b, String s)
- (d) void CALCULATE(int a, int b, String s)

**Answer:** (d) void CALCULATE(int a, int b, String s)
**Explanation:** It displays, so it returns nothing.

### Return values and forms of methods (Q15–Q26)

**Q15.** The number of values a method can return at a time is
- (a) 1
- (b) 2
- (c) 3
- (d) any number

**Answer:** (a) 1
**Explanation:** return sends back one value.

**Q16.** The statement that brings control back to the calling method is
- (a) break
- (b) System.exit(0)
- (c) continue
- (d) return

**Answer:** (d) return
**Explanation:** break and continue work on loops; exit ends the program.

**Q17.** The method int f(int n) { if (n > 0) return 1; } gives the compile error
- (a) reference is ambiguous
- (b) unreachable statement
- (c) no error
- (d) missing return statement

**Answer:** (d) missing return statement
**Explanation:** Nothing is returned when n ≤ 0.

**Q18.** The method int f(int n) { return n; System.out.println(n); } gives the compile error
- (a) missing return statement
- (b) runtime error only
- (c) unreachable statement
- (d) none; it prints n

**Answer:** (c) unreachable statement
**Explanation:** Nothing after return can run.

**Q19.** The method void f(int n) { return n; }
- (a) compiles and returns n
- (b) prints n
- (c) returns 0
- (d) gives the error: unexpected return value

**Answer:** (d) gives the error: unexpected return value
**Explanation:** A void method cannot return a value.

**Q20.** The method int f(int n) { return n * 2.5; }
- (a) returns a double
- (b) gives the error: possible lossy conversion from double to int
- (c) returns 0
- (d) rounds the value

**Answer:** (b) gives the error: possible lossy conversion from double to int
**Explanation:** A double cannot be returned as int without a cast.

**Q21.** A void method can end early with the statement
- (a) end;
- (b) return 0;
- (c) stop;
- (d) return;

**Answer:** (d) return;
**Explanation:** return with no value.

**Q22.** square(int n) returns n * n. The output of System.out.println(ob.square(ob.square(3))); is
- (a) 9
- (b) 81
- (c) 18
- (d) 27

**Answer:** (b) 81
**Explanation:** square(3) = 9; square(9) = 81.

**Q23.** sign(n) returns 1 for positive, −1 for negative and 0 for zero. The output of System.out.println(ob.sign(-8) + ob.sign(0) + ob.sign(4)); is
- (a) −1
- (b) 1
- (c) 0
- (d) 2

**Answer:** (c) 0
**Explanation:** −1 + 0 + 1.

**Q24.** sumTo(n) returns 1 + 2 + … + n. The value of ob.sumTo(4) + ob.sumTo(3) is
- (a) 10
- (b) 6
- (c) 16
- (d) 13

**Answer:** (c) 16
**Explanation:** 10 + 6.

**Q25.** isEven(n) returns n % 2 == 0. The output of System.out.println(ob.isEven(7) + " " + ob.isEven(10)); is
- (a) true false
- (b) false true
- (c) 1 0
- (d) 0 1

**Answer:** (b) false true
**Explanation:** boolean values print as words.

**Q26.** The output of System.out.println("" + ob.square(2) + ob.square(3)); is
- (a) 13
- (b) 49
- (c) 4 9
- (d) 36

**Answer:** (b) 49
**Explanation:** The empty string makes + join 4 and 9.

### Parameters, static methods and calling (Q27–Q40)

**Q27.** The variables in a method header that receive the values are
- (a) actual parameters
- (b) formal parameters
- (c) global variables
- (d) literals

**Answer:** (b) formal parameters
**Explanation:** They are local to the method.

**Q28.** In ob.sum(x, 4), x and 4 are
- (a) formal parameters
- (b) actual parameters
- (c) return values
- (d) member methods

**Answer:** (b) actual parameters
**Explanation:** They are written in the call.

**Q29.** Actual and formal parameters must match in
- (a) number only
- (b) names only
- (c) number, type and order
- (d) nothing at all

**Answer:** (c) number, type and order
**Explanation:** Names may differ.

**Q30.** An argument is
- (a) a value passed to a method when it is called
- (b) a variable declared in the class
- (c) the return type of a method
- (d) a comment inside a method

**Answer:** (a) a value passed to a method when it is called
**Explanation:** Another name for an actual parameter.

**Q31.** A method which is part of a class rather than an instance of the class is a
- (a) static method
- (b) non-static method
- (c) wrapper class
- (d) String method

**Answer:** (a) static method
**Explanation:** It belongs to the class.

**Q32.** A static method can be called
- (a) only through an object
- (b) with the class name, without creating an object
- (c) only from another class
- (d) never from main

**Answer:** (b) with the class name, without creating an object
**Explanation:** e.g. Math.sqrt(16).

**Q33.** A non-static method is called
- (a) by an import statement
- (b) only by its class name
- (c) without parentheses
- (d) through an object

**Answer:** (d) through an object
**Explanation:** ob.display();

**Q34.** perform accepts an integer and a character and returns a double. The right statement to invoke it is
- (a) perform(45, 'A')
- (b) double m = perform(45, 'A')
- (c) double m = perform("A", 45)
- (d) perform('A', 45)

**Answer:** (b) double m = perform(45, 'A')
**Explanation:** Correct order and the result is stored.

**Q35.** The keyword that makes a method belong to the class is
- (a) void
- (b) static
- (c) new
- (d) return

**Answer:** (b) static
**Explanation:** Static members are shared by the class.

**Q36.** Which method is static in every Java application?
- (a) calculate
- (b) accept
- (c) display
- (d) main

**Answer:** (d) main
**Explanation:** It runs before any object exists.

**Q37.** tick() adds 1 to a static variable count that starts at 0. After ob.tick(); ob.tick(); ob.tick(); the value of count is
- (a) 0
- (b) 1
- (c) 3
- (d) 6

**Answer:** (c) 3
**Explanation:** Each call adds 1.

**Q38.** isPalindrome(n) in the same class can use reverse(n) by
- (a) calling it directly by name
- (b) importing it first
- (c) copying its code
- (d) declaring it private

**Answer:** (a) calling it directly by name
**Explanation:** Methods of a class can call one another.

**Q39.** To swap a and b in void swap(int a, int b) the jumbled statements are (1) a = b; (2) b = t; (3) int t = 0; (4) t = a;. The correct order is
- (a) (1) (2) (3) (4)
- (b) (3) (4) (1) (2)
- (c) (1) (3) (4) (2)
- (d) (2) (1) (4) (3)

**Answer:** (b) (3) (4) (1) (2)
**Explanation:** Declare t, save a, copy b into a, then t into b.

**Q40.** A correct call of void table(int n) is
- (a) ob.table();
- (b) int t = ob.table(7);
- (c) ob.table(7);
- (d) table int(7);

**Answer:** (c) ob.table(7);
**Explanation:** A void method is called as a statement.

### Call by value, call by reference, pure and impure (Q41–Q54)

**Q41.** In call by value, a method receives
- (a) a copy of the value
- (b) the original variable itself
- (c) the address of the class
- (d) nothing

**Answer:** (a) a copy of the value
**Explanation:** The original stays unchanged.

**Q42.** Java passes primitive arguments such as int and double by
- (a) constructor
- (b) reference
- (c) name
- (d) value

**Answer:** (d) value
**Explanation:** The method gets copies.

**Q43.** swap(int a, int b) exchanges its two parameters. In main, a = 5 and b = 9; after ob.swap(a, b); the statement System.out.println(a + " " + b); prints
- (a) 9 5
- (b) 5 9
- (c) 5 5
- (d) 9 9

**Answer:** (b) 5 9
**Explanation:** Only the copies were swapped.

**Q44.** Invoking a method by passing the objects of a class is termed
- (a) call by method
- (b) call by value
- (c) call by reference
- (d) call by constructor

**Answer:** (c) call by reference
**Explanation:** The method reaches the original object.

**Q45.** shift(Point p) adds 10 to p.x. After p.x = 3; ob.shift(p); the value of p.x is
- (a) 3
- (b) 10
- (c) 13
- (d) 30

**Answer:** (c) 13
**Explanation:** The method changed the same object.

**Q46.** A method which does not modify the value of variables is termed a
- (a) impure method
- (b) user defined method
- (c) primitive method
- (d) pure method

**Answer:** (d) pure method
**Explanation:** It changes no state.

**Q47.** A method which reverses a given number and returns the result is a
- (a) impure method
- (b) pure method
- (c) constructor
- (d) destructor

**Answer:** (b) pure method
**Explanation:** It only returns a value.

**Q48.** deposit(double amt) adds amt to the member variable balance. It is
- (a) a pure method
- (b) an impure method
- (c) a constructor
- (d) a library method

**Answer:** (b) an impure method
**Explanation:** It changes the object's state.

**Q49.** Pure methods are also called
- (a) destructors
- (b) mutators
- (c) constructors
- (d) accessors

**Answer:** (d) accessors
**Explanation:** They read data without changing it.

**Q50.** Impure methods are also called
- (a) accessors
- (b) modifiers
- (c) wrappers
- (d) literals

**Answer:** (b) modifiers
**Explanation:** Also mutators; they change state.

**Q51.** Which statement about call by reference is TRUE?
- (a) The original object can change.
- (b) It works only with int values.
- (c) It copies the object's values first.
- (d) It is a pure method.

**Answer:** (a) The original object can change.
**Explanation:** The method reaches the original object.

**Q52.** Statement I: In call by value, changes inside the method do not affect the caller's variables. Statement II: Call by value works with reference data types.
- (a) Both statements are true.
- (b) Both statements are false.
- (c) Statement I is true, Statement II is false.
- (d) Statement I is false, Statement II is true.

**Answer:** (c) Statement I is true, Statement II is false.
**Explanation:** Call by value works with primitive types.

**Q53.** The two ways of invoking methods are
- (a) call by value and call by reference
- (b) call by name and call by number
- (c) static and import
- (d) public and private

**Answer:** (a) call by value and call by reference
**Explanation:** ICSE 2017 Q2(b).

**Q54.** Assertion (A): An argument is a value passed to a method when it is called. Reason (R): Variables declared in a method prototype to receive values are called actual parameters.
- (a) Both A and R are true, and R explains A.
- (b) Both A and R are true, but R does not explain A.
- (c) A is true, but R is false.
- (d) A is false, but R is true.

**Answer:** (c) A is true, but R is false.
**Explanation:** Those variables are formal parameters.

### Method overloading (Q55–Q76)

**Q55.** Defining several methods with the same name but different parameter lists in one class is
- (a) method overloading
- (b) inheritance
- (c) encapsulation
- (d) abstraction

**Answer:** (a) method overloading
**Explanation:** One name, many forms.

**Q56.** Overloaded methods must differ in their
- (a) parameter lists
- (b) return types only
- (c) access specifiers only
- (d) parameter names only

**Answer:** (a) parameter lists
**Explanation:** Number, type or order of parameters.

**Q57.** In a calculator, the Java feature that allows several methods named calculate() for different operations is
- (a) abstraction
- (b) inheritance
- (c) encapsulation
- (d) polymorphism

**Answer:** (d) polymorphism
**Explanation:** Overloading is a kind of polymorphism.

**Q58.** Which pair of methods causes a compile-time error due to incorrect overloading?
- (a) void test(int a, int b) and void test(double a, double b)
- (b) void test(int a, double b) and void test(double a, int b)
- (c) void test(int a, double b) and void test(int a)
- (d) void test(int a) and int test(int a)

**Answer:** (d) void test(int a) and int test(int a)
**Explanation:** Same parameter list; only the return type differs.

**Q59.** Which of these does NOT overload a method?
- (a) a different number of parameters
- (b) different parameter types
- (c) a different order of parameter types
- (d) a different return type only

**Answer:** (d) a different return type only
**Explanation:** The signature must differ.

**Q60.** void test(int a) and int test(int a) in one class give the error
- (a) method test(int) is already defined
- (b) missing return statement
- (c) unreachable statement
- (d) no error

**Answer:** (a) method test(int) is already defined
**Explanation:** javac's message.

**Q61.** A class has show(int), show(long) and show(double). The call ob.show(7) runs
- (a) none; it is an error
- (b) show(long)
- (c) show(double)
- (d) show(int)

**Answer:** (d) show(int)
**Explanation:** Exact match first.

**Q62.** With the same methods, each printing its type and value, ob.show(7.0) prints
- (a) int 7
- (b) long 7
- (c) double 7.0
- (d) an error message

**Answer:** (c) double 7.0
**Explanation:** 7.0 is a double literal.

**Q63.** With the same methods, ob.show('A') prints
- (a) int 65
- (b) A
- (c) double 65.0
- (d) an error message

**Answer:** (a) int 65
**Explanation:** char widens to int first.

**Q64.** A class has only void only(double d), which prints "only " + d. The call ob.only(7) prints
- (a) only 7
- (b) only 7.0
- (c) an error: no such method
- (d) only 7.00

**Answer:** (b) only 7.0
**Explanation:** The int widens to double.

**Q65.** A class has test(int, double) and test(double, int). The call test(1, 2) gives
- (a) a call to the first method
- (b) a call to the second method
- (c) the error: reference to test is ambiguous
- (d) a runtime error

**Answer:** (c) the error: reference to test is ambiguous
**Explanation:** Both fit equally well.

**Q66.** With the same two methods, the call test(1, 2.0) runs
- (a) test(int, double)
- (b) test(double, int)
- (c) neither; it is ambiguous
- (d) neither; it does not compile

**Answer:** (a) test(int, double)
**Explanation:** It matches exactly.

**Q67.** max(int a, int b, int c) is written as return max(max(a, b), c);. The value of max(4, 19, 11) is
- (a) 4
- (b) 11
- (c) 19
- (d) 34

**Answer:** (c) 19
**Explanation:** max(4, 19) = 19; max(19, 11) = 19.

**Q68.** A class has max(int, int), max(double, double) and max(char, char). The call max(5, 6.5) runs
- (a) max(int, int)
- (b) max(double, double)
- (c) max(char, char)
- (d) none; it is an error

**Answer:** (b) max(double, double)
**Explanation:** 5 widens to 5.0; the result is 6.5.

**Q69.** In an overloading question, each method must
- (a) be written in a separate class
- (b) have a different name
- (c) read its values with Scanner
- (d) have the name given in the question

**Answer:** (d) have the name given in the question
**Explanation:** Different names lose the overloading marks.

**Q70.** When the question gives double print(double a, double b), the method must
- (a) be declared void
- (b) only print the result
- (c) return the result
- (d) take no parameters

**Answer:** (c) return the result
**Explanation:** A non-void type needs a return.

**Q71.** For the pattern 1 2 3 4 5 / 2 3 4 5 / 3 4 5 / 4 5 / 5 with outer loop i from 1 to 5, the inner loop is
- (a) for (j = i; j <= 5; j++)
- (b) for (j = 1; j <= i; j++)
- (c) for (j = 5; j >= 1; j--)
- (d) for (j = 1; j <= 5; j++)

**Answer:** (a) for (j = i; j <= 5; j++)
**Explanation:** Each row starts at the row number.

**Q72.** In the pattern @#@#@ printed with columns j = 1 to 5, '#' is printed when
- (a) j % 2 == 0
- (b) j % 2 == 1
- (c) i % 2 == 0
- (d) j == 5

**Answer:** (a) j % 2 == 0
**Explanation:** Even columns hold #.

**Q73.** For the series 1/2 + 1/3 + … + 1/10, the statement that adds a term correctly is
- (a) sum = sum + 1.0 / i;
- (b) sum = sum + 1 / i;
- (c) sum = 1 / i;
- (d) sum = sum * i;

**Answer:** (a) sum = sum + 1.0 / i;
**Explanation:** 1 / i is integer division and gives 0.

**Q74.** The nth term of the series 0, 7, 26, 63, … is
- (a) 2 × n − 1
- (b) n × n − 1
- (c) n × n × n
- (d) n × n × n − 1

**Answer:** (d) n × n × n − 1
**Explanation:** 1 − 1, 8 − 1, 27 − 1, 64 − 1.

**Q75.** A lead number has equal sums of even and odd digits. Which is a lead number?
- (a) 3669
- (b) 1234
- (c) 1111
- (d) 2020

**Answer:** (a) 3669
**Explanation:** 6 + 6 = 3 + 9 = 12.

**Q76.** int transform(int n) returns the sum of the digits. The value of transform(458) is
- (a) 17
- (b) 854
- (c) 458
- (d) 160

**Answer:** (a) 17
**Explanation:** 4 + 5 + 8.
## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** Why do we need methods? Give two reasons.
**Answer:** Methods make a program modular — each method does one task — and reusable, so a task written once can be called many times.
They also remove repeated code and make errors easier to find.

**Q2.** Distinguish between a method prototype and a method signature.
**Answer:** The prototype is the whole header line, e.g. `public int sum(int a, int b)`.
The signature is only the name with the parameter list, e.g. `sum(int, int)`; the return type is not part of it.

**Q3.** Distinguish between actual and formal parameters.
**Answer:** Actual parameters are the values written in the method call, e.g. 5 and 7 in `sum(5, 7)`.
Formal parameters are the variables in the method header that receive them, e.g. a and b in `int sum(int a, int b)`.

**Q4.** State two differences between call by value and call by reference.
**Answer:** Call by value passes copies of primitive values, so the originals do not change.
Call by reference passes a reference to an object, so the method can change the original object.

**Q5.** Distinguish between pure and impure methods, with one example each.
**Answer:** A pure method does not change the state of an object, e.g. `int reverse(int n)` that returns the reverse.
An impure method changes it, e.g. `void deposit(double amt)` that adds to the balance.

**Q6.** Distinguish between static and non-static methods.
**Answer:** A static method belongs to the class and is called without an object, e.g. `Math.sqrt(16)`.
A non-static method belongs to an object and is called through it, e.g. `ob.display()`.

**Q7.** What is method overloading? Give an example.
**Answer:** Two or more methods with the same name but different parameter lists in one class, e.g. `double area(double r)` and `double area(double l, double b)`.

**Q8.** Can two methods be overloaded by their return types alone? Explain.
**Answer:** No. Java tells overloaded methods apart only by their parameter lists.
`void test(int a)` and `int test(int a)` give "method test(int) is already defined".

**Q9.** State two uses of the return statement.
**Answer:** It sends one value back to the caller, and it ends the method at once, returning control to the caller.

**Q10.** Name the four forms of methods, by parameters and return values.
**Answer:** No parameters and no return value; parameters and no return value.
No parameters with a return value; parameters with a return value.

**Q11.** Why is method overloading called polymorphism?
**Answer:** Polymorphism means "many forms"; in overloading one method name has many forms, one for each parameter list.

**Q12.** Write the prototypes of (i) a method find that takes a String and a char and returns an int, and (ii) a method getRate with no parameters that returns a double.
**Answer:** (i) `int find(String s, char ch)` (ii) `double getRate()`

### Output and error questions (2 marks each)

**Q13.** `void swap(int a, int b) { int t = a; a = b; b = t; System.out.println("Inside: " + a + " " + b); }` In main: `int a = 5, b = 9; ob.swap(a, b); System.out.println("Outside: " + a + " " + b);` Give the output.
**Answer:** `Inside: 9 5` then `Outside: 5 9`
Call by value: only the copies were swapped.

**Q14.** `void shift(Point p) { p.x = p.x + 10; }` In main: `Point p = new Point(); p.x = 3; ob.shift(p); System.out.println(p.x);` Give the output.
**Answer:** `13` — the method changed the caller's object (call by reference).

**Q15.** A class has `show(int n)`, `show(long n)` and `show(double d)`, each printing its type and value. Give the output of `ob.show(7); ob.show(7L);`
**Answer:** `int 7` then `long 7` — each call matches its type exactly.

**Q16.** With the methods of Q15, give the output of `ob.show('A');`. If a class has only `void only(double d)`, give the output of `ob.only(7);`.
**Answer:** `int 65` — the char widens to int.
`only 7.0` — the int widens to double.

**Q17.** `int square(int n) { return n * n; }` Give the output of `System.out.println(ob.square(ob.square(3)));` and of `System.out.println("" + ob.square(2) + ob.square(3));`
**Answer:** `81` and `49` — the empty string makes + join 4 and 9.

**Q18.** sign(n) returns 1, −1 or 0, and sumTo(n) returns 1 + 2 + … + n. Give the output of `System.out.println(ob.sign(-8) + ob.sign(0) + ob.sign(4));` and `System.out.println(ob.sumTo(4) + ob.sumTo(3));`
**Answer:** `0` (−1 + 0 + 1) and `16` (10 + 6).

**Q19.** Find the error: `void test(int a) { }` and `int test(int a) { return a; }` in the same class.
**Answer:** "method test(int) is already defined" — they differ only in return type.
Change one parameter list, e.g. `int test(int a, int b)`.

**Q20.** Find the error and correct it: `int f(int n) { if (n > 0) return 1; }`
**Answer:** "missing return statement" — nothing is returned when n ≤ 0.
Add `return 0;` before the closing brace.

**Q21.** Find the error and correct it: `void f(int n) { return n; }`
**Answer:** "incompatible types: unexpected return value" — a void method cannot return a value.
Write `int f(int n) { return n; }`.

**Q22.** A class has `test(int a, double b)` and `test(double a, int b)`. Why does `test(1, 2);` fail, and how can it be corrected?
**Answer:** "reference to test is ambiguous" — both methods fit after widening.
Write `test(1, 2.0);` or `test(1.0, 2);`.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; the output follows each.*

### Section B programs (15 marks each)

**Q1.** Define a class to overload the method area as follows: double area(double r) — returns the area of a circle (πr²); double area(double l, double b) — returns the area of a rectangle; double area(double a, double b, double c) — returns the area of a triangle with sides a, b, c by Heron's formula, √(s(s − a)(s − b)(s − c)), where s = (a + b + c)/2. Write main to call each method.
**Answer:**
```java
class OverloadArea
{
    double area(double r)
    {
        return Math.PI * r * r;
    }

    double area(double l, double b)
    {
        return l * b;
    }

    double area(double a, double b, double c)
    {
        double s = (a + b + c) / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }

    public static void main(String args[])
    {
        OverloadArea ob = new OverloadArea();
        System.out.println("Circle, radius 7    : " + ob.area(7.0));
        System.out.println("Rectangle 12 by 5   : " + ob.area(12.0, 5.0));
        System.out.println("Triangle 3, 4 and 5 : " + ob.area(3.0, 4.0, 5.0));
    }
}
```
Output:
```
Circle, radius 7    : 153.93804002589985
Rectangle 12 by 5   : 60.0
Triangle 3, 4 and 5 : 6.0
```

**Q2.** Define a class PalPrime with the methods int reverse(int n) — returns the reverse of n; boolean isPalindrome(int n) — uses reverse() to check whether n is a palindrome; boolean isPrime(int n) — checks whether n is prime. In main, print all numbers from 10 to 500 that are both palindromes and primes.
**Answer:**
```java
class PalPrime
{
    int reverse(int n)
    {
        int rev = 0;
        while (n > 0)
        {
            rev = rev * 10 + n % 10;
            n = n / 10;
        }
        return rev;
    }

    boolean isPalindrome(int n)
    {
        return n == reverse(n);
    }

    boolean isPrime(int n)
    {
        if (n < 2)
            return false;
        for (int i = 2; i * i <= n; i++)
        {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    public static void main(String args[])
    {
        PalPrime ob = new PalPrime();
        System.out.println("Palindromic primes from 10 to 500:");
        for (int n = 10; n <= 500; n++)
        {
            if (ob.isPalindrome(n) && ob.isPrime(n))
                System.out.print(n + " ");
        }
        System.out.println();
    }
}
```
Output:
```
Palindromic primes from 10 to 500:
11 101 131 151 181 191 313 353 373 383
```

**Q3.** Define a class to overload the method pattern as follows: void pattern(int n) — prints a right triangle of n rows of stars; void pattern(char ch, int n) — prints ch in n rows and n columns; void pattern(String s) — prints the first 1, 2, 3, … characters of s on successive lines. Use nested loops where needed.
**Answer:**
```java
class OverloadPattern
{
    void pattern(int n)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= i; j++)
                System.out.print("* ");
            System.out.println();
        }
    }

    void pattern(char ch, int n)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
                System.out.print(ch + " ");
            System.out.println();
        }
    }

    void pattern(String s)
    {
        for (int i = 1; i <= s.length(); i++)
            System.out.println(s.substring(0, i));
    }

    public static void main(String args[])
    {
        OverloadPattern ob = new OverloadPattern();
        ob.pattern(4);
        ob.pattern('#', 3);
        ob.pattern("BLUE");
    }
}
```
Output:
```
*
* *
* * *
* * * *
# # #
# # #
# # #
B
BL
BLU
BLUE
```

**Q4.** Define a class Niven with the methods int countDigits(int n), int sumOfDigits(int n) and boolean isNiven(int n) — a Niven (Harshad) number is divisible by the sum of its digits. In main, input a number and print its digit count, digit sum and whether it is a Niven number.
**Answer:**
```java
import java.util.*;
class Niven
{
    int countDigits(int n)
    {
        int c = 0;
        while (n > 0)
        {
            c++;
            n = n / 10;
        }
        return c;
    }

    int sumOfDigits(int n)
    {
        int s = 0;
        while (n > 0)
        {
            s = s + n % 10;
            n = n / 10;
        }
        return s;
    }

    boolean isNiven(int n)
    {
        return n % sumOfDigits(n) == 0;
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        Niven ob = new Niven();
        System.out.print("Enter a positive number: ");
        int n = sc.nextInt();
        System.out.println("Number of digits : " + ob.countDigits(n));
        System.out.println("Sum of digits    : " + ob.sumOfDigits(n));
        if (ob.isNiven(n))
            System.out.println(n + " is a Niven number");
        else
            System.out.println(n + " is not a Niven number");
    }
}
```
Sample run (126 ÷ 9 = 14):
```
Enter a positive number: 126
Number of digits : 3
Sum of digits    : 9
126 is a Niven number
```

**Q5.** Define a class to overload the method max: int max(int a, int b); int max(int a, int b, int c), which uses the two-parameter version; double max(double a, double b); char max(char a, char b). In main call max(12, 7), max(4, 19, 11), max(3.5, 2.25), max('k', 'p') and max(5, 6.5).
**Answer:**
```java
class OverloadMax
{
    int max(int a, int b)
    {
        if (a > b)
            return a;
        else
            return b;
    }

    int max(int a, int b, int c)
    {
        return max(max(a, b), c);
    }

    double max(double a, double b)
    {
        if (a > b)
            return a;
        else
            return b;
    }

    char max(char a, char b)
    {
        if (a > b)
            return a;
        else
            return b;
    }

    public static void main(String args[])
    {
        OverloadMax ob = new OverloadMax();
        System.out.println(ob.max(12, 7));
        System.out.println(ob.max(4, 19, 11));
        System.out.println(ob.max(3.5, 2.25));
        System.out.println(ob.max('k', 'p'));
        System.out.println(ob.max(5, 6.5));
    }
}
```
Output (max(5, 6.5) runs the double version, because 5 widens to 5.0):
```
12
19
3.5
p
6.5
```

**Q6.** Define a class Temperature2 with two **static** methods: double toFahrenheit(double c) = 9c/5 + 32 and double toCelsius(double f) = 5(f − 32)/9. In main (without creating an object) print a conversion table for 0 °C to 100 °C in steps of 20, and convert 98.6 °F to Celsius.
**Answer:**
```java
class Temperature2
{
    static double toFahrenheit(double c)
    {
        return 9 * c / 5 + 32;
    }

    static double toCelsius(double f)
    {
        return 5 * (f - 32) / 9;
    }

    public static void main(String args[])
    {
        System.out.println("Celsius -> Fahrenheit");
        for (int c = 0; c <= 100; c = c + 20)
            System.out.println(c + " -> " + toFahrenheit(c));
        System.out.println("98.6 F = " + toCelsius(98.6) + " C");
    }
}
```
Output:
```
Celsius -> Fahrenheit
0 -> 32.0
20 -> 68.0
40 -> 104.0
60 -> 140.0
80 -> 176.0
100 -> 212.0
98.6 F = 37.0 C
```

---

## 12. Competency / Application Questions

**Q1. (Design the overloads)** A shop's bill() should handle (i) price and quantity, (ii) price, quantity and a discount percentage, (iii) a list of three prices. Write the three prototypes.
**Model answer:** `double bill(double price, int qty)`, `double bill(double price, int qty, double disc)`, `double bill(double p1, double p2, double p3)`.

**Q2. (Return or print?)** A question asks for `int sumDigits(int n)`. A candidate prints the sum inside the method and writes no return. What happens, and what is the fix?
**Model answer:** javac reports "missing return statement". The method must end with `return sum;`, and main prints the returned value.

**Q3. (Spot the overloading trap)** Why can `double avg(int a, int b)` and `int avg(int a, int b)` not both be in a class?
**Model answer:** They have the same signature avg(int, int); return type alone does not overload.

**Q4. (Value or reference?)** A method doubles every element of an array passed to it. Does the caller's array change? Why?
**Model answer:** Yes — an array is an object; the method receives a reference to the same array.

**Q5. (Choose static)** Why can a helper such as `static boolean isPrime(int n)` be called from main without creating an object?
**Model answer:** A static method belongs to the class; main, also static, can call it directly.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** A method can return two values with the statement `return a, b;`.
**R:** The return statement sends back one value.
**Answer:** (b)
**Explanation:** Only one value can be returned.

**Q2.**
**A:** `void test(int a)` and `int test(int a)` cannot be in one class.
**R:** The return type is not part of the method signature.
**Answer:** (c)
**Explanation:** Their signatures are the same.

**Q3.**
**A:** In call by value the caller's variables do not change.
**R:** The method works on copies of the values.
**Answer:** (c)
**Explanation:** Changes affect only the copies.

**Q4.**
**A:** The main method is declared static.
**R:** Java is case sensitive.
**Answer:** (d)
**Explanation:** Both true; main is static so it can run without an object.

**Q5.**
**A:** Passing an object lets a method change the object's member variables.
**R:** The method receives a reference to the same object.
**Answer:** (c)
**Explanation:** Call by reference.

**Q6.**
**A:** A method that reverses a number and returns it is impure.
**R:** A pure method does not change the state of an object.
**Answer:** (b)
**Explanation:** It is pure; R is true.

**Q7.**
**A:** With show(int) and show(double), `show('A')` runs show(int).
**R:** A char widens to int before it widens to double.
**Answer:** (c)
**Explanation:** The nearest widening is chosen.

**Q8.**
**A:** Formal parameters are declared in the method header.
**R:** Formal parameters can be constants such as 5.
**Answer:** (a)
**Explanation:** Formal parameters are always variables; constants can be actual parameters.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The fee calculator

> A class has `double fee(int classNo)` and `double fee(int classNo, boolean hostel)`; the office calls `fee(9, true)`.

**(i)** Which Java feature do the two methods show?
**Answer:** Method overloading (polymorphism).

**(ii)** Which method runs for fee(9, true)?
**Answer:** `fee(int classNo, boolean hostel)`.

**(iii)** Can `int fee(int classNo)` be added to the class?
**Answer:** No — it has the same parameter list as the first method.

**(iv)** Name the actual parameters in fee(9, true).
**Answer:** 9 and true.

### Case 2 — The swap that did not swap

> `swap(int a, int b)` swaps its parameters; after `ob.swap(x, y)` with x = 5, y = 9, main still prints 5 and 9.

**(i)** Which way of invoking is used?
**Answer:** Call by value.

**(ii)** Why are x and y unchanged?
**Answer:** The method swapped only copies.

**(iii)** Are x and y actual or formal parameters?
**Answer:** Actual parameters.

**(iv)** Would main see a change made inside the method to a Point object passed instead?
**Answer:** Yes — call by reference.

### Case 3 — Palindromic primes

> A class has `int reverse(int n)`, `boolean isPalindrome(int n)` (which calls reverse) and `boolean isPrime(int n)`.

**(i)** Which method calls another method of the class?
**Answer:** isPalindrome() calls reverse().

**(ii)** What is the return type of isPrime()?
**Answer:** boolean.

**(iii)** Is reverse() pure or impure?
**Answer:** Pure — it only returns a value.

**(iv)** What is the smallest palindromic prime greater than 100?
**Answer:** 101.

---

## 15. Revision Notes

### Chapter at a glance
- Method = named block for one task; header (prototype) + body; modular and reusable.
- Prototype = access specifier, modifier, return type, name, parameter list; signature = name + parameter list.
- Forms: with or without parameters × with or without a return value; return sends one value and ends the method.
- Actual parameters in the call; formal parameters in the header; match in number, type and order.
- Static: belongs to the class, no object needed; non-static: called through an object.
- Call by value: primitives, copies, originals unchanged (pure). Call by reference: objects, originals can change (impure).
- Overloading: same name, different parameter lists; not by return type; exact match, then widening; ambiguity is an error.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| Giving each overloaded method a different name | Use the one name given in the question. |
| Printing in a method whose return type is int or double | Return the value; print it in main. |
| Reading values with Scanner inside a method that has parameters | Use the parameters. |
| println() inside the inner loop of a pattern | Put it after the inner loop. |
| sum = sum + 1 / i | Use 1.0 / i to avoid integer division. |
| Overloading by return type only | Change the parameter list. |
| Calling a void method in an assignment | Call it as a statement. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 6: User-defined Methods**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** The number of values a method can return is:
(a) 1 (b) 2 (c) 3 (d) 4

**2.** The return type of a method that returns YES or NO:
(a) boolean (b) String (c) int (d) double

**3.** A method that is part of a class rather than an instance:
(a) static method (b) non-static method (c) wrapper class (d) String method

**4.** Invoking a method by passing objects of a class:
(a) call by reference (b) call by value (c) call by method (d) call by constructor

**5.** A method which does not modify the value of variables:
(a) impure method (b) pure method (c) primitive method (d) constructor

**6.** The pair that is NOT valid overloading:
(a) void t(int a) and void t(double a) (b) void t(int a) and void t(int a, int b) (c) void t(int a, double b) and void t(double a, int b) (d) void t(int a) and int t(int a)

**7.** The prototype of check() which takes an int and returns a char:
(a) char check() (b) void check(int x) (c) check(int x) (d) char check(int x)

**8.** The statement that brings control back to the calling method:
(a) break (b) continue (c) System.exit(0) (d) return

**9.** With show(int) and show(double), each printing its type and value, ob.show('A') prints:
(a) int 65 (b) A (c) double 65.0 (d) an error

**10.** Statement I: Overloaded methods share one name. Statement II: Overloaded methods may differ in return type only.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

### Part I — Short answers (5 × 2 = 10)

**11.** Differentiate actual and formal parameters. [2]

**12.** Differentiate call by value and call by reference. [2]

**13.** Give the output: `swap(int a, int b)` exchanges its parameters and prints them; main has a = 5, b = 9, calls `ob.swap(a, b)` and prints a and b. [2]

**14.** Write the prototype of a method isGreater that takes two doubles and returns true or false. [2]

**15.** Find the error and correct it: `void f(int n) { return n; }` [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Define a class to overload volume(): sphere volume(double R) = 4/3 × 22/7 × R³; cylinder volume(double H, double R) = 22/7 × R² × H; cuboid volume(double L, double B, double H) = L × B × H. Each method returns the volume. [10]

**17.** Define a class to overload series(): void series(int x, int n) displays the sum x¹ + x² + … + xⁿ; void series(int p) displays 0, 7, 26, 63, … up to p terms; void series() displays the sum 1/2 + 1/3 + … + 1/10. [10]

**18.** Define a class to overload print(): void print() prints 1 1 1 1 / 2 2 2 2 / … / 5 5 5 5 with nested loops; void print(int n) checks whether n is a lead number (sum of even digits equals sum of odd digits). [10]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | b | c | c | d | c | b | c | a |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | Overloading | fee(int, boolean) | No | 9 and true |
| 2 | Call by value | Copies swapped | Actual | Yes |
| 3 | isPalindrome() | boolean | Pure | 101 |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | a | b | a | a | b | d | d | d | a | c |

**Part I, Q11–15 (2 marks each)**

**11.** Actual: values in the call (1); formal: variables in the header that receive them (1).
**12.** Value: copies, originals unchanged (1); reference: object reference, original can change (1).
**13.** `5 9` — the swap affected only the copies (2).
**14.** `boolean isGreater(double a, double b)` (2).
**15.** A void method cannot return a value (1); `int f(int n) { return n; }` (1).

**Part II (10 marks each)**

**16.–18.** Same method name in all versions (2), correct parameter lists and return types (2), logic of each method (2 + 2), main calling each method or correct returns (2).
