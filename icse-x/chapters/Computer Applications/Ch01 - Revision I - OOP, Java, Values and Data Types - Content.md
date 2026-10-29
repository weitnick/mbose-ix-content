# Revision I — Object-Oriented Programming, Java, Values and Data Types

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 1 |
| Title | Revision I — Object-Oriented Programming, Java, Values and Data Types |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 1. Revision of Class IX syllabus: (i) Introduction to Object Oriented Programming concepts, (ii) Elementary concept of objects and classes, (iii) Values and data types |
| Exam weightage | Section A (40 marks) always has several 1-mark MCQs and 2-mark parts from this chapter: **OOP principles** (often from a picture), **JVM and byte code**, **features of Java**, **tokens and keywords**, **escape sequences**, **sizes of data types**, **type casting**, **ASCII values** and **packages**. |
| Syllabus scope | Principles of OOP (abstraction, encapsulation, inheritance, polymorphism) and procedure- vs object-oriented programming; Java applets and applications; compilation process — source code, byte code, object code, JVM; features of Java. Objects and classes in outline. Character set, ASCII and Unicode, escape sequences, tokens (keywords, identifiers, literals, punctuators, operators), constants and variables, primitive and non-primitive data types with sizes, implicit and explicit type conversion. Packages and the import statement. |
| In short | A quick revision of object-oriented ideas, how Java programs are compiled and run, and the basic data types Java uses. |

> **Note on the text:** CISCE does not prescribe a textbook for ICSE Computer Applications. This chapter is written to the ICSE 2027 syllabus in its own words; its exam questions are the CISCE board papers of 2017–2026 and the specimen papers of 2024 and 2025, answered from CISCE's marking schemes wherever one has been published. **Every output in this chapter was checked by compiling and running the code (Java 21).**
>
> **Exam note:** Learn the **exact sizes**: byte 1, short 2, int 4, long 8, float 4, double 8, **char 2** (Unicode) bytes. A **char** in an arithmetic expression becomes its **code number** (`'A'` → 65, `'a'` → 97, `'0'` → 48), so `'Z' + 32` prints **122**, not z. Java is **case sensitive**: `static`, `case`, `if` are keywords but `Switch`, `If`, `BOOLEAN` are not. **Byte code** is what `javac` produces; the **JVM** runs it — that is why Java is **platform independent**. Name tokens precisely: `public` keyword, `'a'` character literal, `==` operator, `{ }` separator (punctuator).

---

## 1. Complete Lesson

### Procedure-oriented and object-oriented programming

| Procedure-oriented programming (POP) | Object-oriented programming (OOP) |
|---|---|
| The program is a list of **procedures (functions)** that act on data | The program is built from **objects** that combine **data and the methods** that act on it |
| Emphasis on **what to do** (steps) | Emphasis on **data** and its behaviour |
| Data moves freely between functions — **less secure** | Data is **hidden** inside objects — **more secure** |
| Top-down approach; e.g. C, BASIC | Bottom-up approach; e.g. **Java**, C++, Python |
| Hard to reuse and extend | **Reuse** through classes and inheritance |

### The four principles of OOP

| Principle | Meaning | Real-life example |
|---|---|---|
| **Abstraction** | Representing the **essential features** and **hiding unnecessary or background details** | Driving a car with the steering, brake and accelerator without knowing how the engine works |
| **Encapsulation** | **Wrapping up data and methods** into a single unit (a class) and **controlling access** to the data | A medicine capsule; a bank account whose balance changes only through deposit and withdraw |
| **Inheritance** | A mechanism by which **one class acquires the properties** (data and methods) **of another class** | A child inheriting features from a parent; a `Car` class acquiring the features of a `Vehicle` class |
| **Polymorphism** | The ability of one name to take **many forms** — the same message behaves differently in different situations (e.g. **method overloading**) | One person acts as a student at school and as a player on the field; a calculator's `calculate()` working for add, subtract, multiply |

**Example 1.** *(ICSE 2019, Q1(a))* Name any two basic principles of Object-oriented Programming.
**Solution:** Any two: **Encapsulation, Data Abstraction, Polymorphism, Inheritance.**

**Example 2.** *(ICSE 2018, Q1(a))* Define abstraction.
**Solution:** Abstraction is the act of **representing essential features** and **hiding unnecessary or background details**.

### Introduction to Java

Java was developed by **James Gosling** and his team at **Sun Microsystems** (first called *Oak*, 1991) and released in **1995**; it is now owned by **Oracle**.

**Types of Java programs**
- **Java application** — a stand-alone program that runs on a computer through the JVM and has a `main()` method (all programs in this course).
- **Java applet** — a small program embedded in a web page and run by a browser (no longer used in modern browsers, but part of the syllabus).

**The compilation process**

![Fig. 1.1 Compilation process](figures/ca_ch01_fig01_compilation.png)

| Term | Meaning |
|---|---|
| **Source code** | The program written by the programmer in Java (a **.java** file) |
| **Compiler (javac)** | Translates the whole source code into byte code, reporting syntax errors |
| **Byte code** | The **intermediate, machine-independent code** produced by the Java compiler (a **.class** file) |
| **Java Virtual Machine (JVM)** | The **software (interpreter)** that **executes byte code** on a particular computer, converting it into that machine's code |
| **Object (machine) code** | The **machine-language** instructions the processor actually runs |

**Features of Java**

| Feature | Meaning |
|---|---|
| **Simple** | Easy syntax (like C++ but without pointers) |
| **Object oriented** | Everything is built around classes and objects |
| **Platform independent** | Byte code runs on **any operating system** that has a JVM — "write once, run anywhere" |
| **Robust** | Strong type checking, exception handling and automatic memory management (garbage collection) |
| **Secure** | Runs inside the JVM, with no pointers; protects the system from harmful code |
| **Multithreaded** | Can do several tasks at the same time |
| **Portable** | The same byte code moves between machines without change |

**Example 3.** *(ICSE 2020, Q1(a))* Define Java byte code.
**Solution:** Byte code is the **intermediate, machine-independent code** produced when the **Java compiler** compiles the source code (a .class file); it is executed by the **Java Virtual Machine**.

### Objects and classes — a first look

- An **object** is an entity with a **state** (its attributes or data) and **behaviour** (its methods). A pen has a colour and a brand (state) and can write (behaviour).
- A **class** is a **blueprint (template)** from which objects are created. It can be seen as an **object factory** that produces similar objects, and as a **user-defined data type**.
- Objects communicate by **message passing** — one object calls a method of another.

These ideas are developed fully in **Chapter 5**.

### Character set, ASCII and Unicode

The **character set** of Java is the set of characters it recognises: **letters** (A–Z, a–z), **digits** (0–9), **special characters** (+ − * / % = < > ( ) { } [ ] ; , . etc.) and **white space** (space, tab, new line).

| Code | Bits | Range | Use |
|---|---|---|---|
| **ASCII** (American Standard Code for Information Interchange) | 7 bits | 0 – 127 (128 characters) | English letters, digits, symbols |
| **Unicode** | **16 bits** in a Java `char` | 0 – 65,535 | Characters of almost all languages; **Java uses Unicode**, so a `char` takes **2 bytes** |

**Codes to remember:** `'A'` = **65** … `'Z'` = **90**; `'a'` = **97** … `'z'` = **122**; `'0'` = **48** … `'9'` = **57**; space = **32**. A small letter's code is **32 more** than the capital's.

```java
char ch = 'F';
int m = ch;              // m = 70, the code of 'F'
m = m + 5;
System.out.println(m + " " + ch);   // 75 F
System.out.println('Z' + 32);       // 122  (char + int gives int)
System.out.println((char)('Z' + 32)); // z  (cast back to char)
```

### Escape sequences

An **escape sequence** is a backslash followed by a character; it represents a **non-printable or special character** inside a character or string literal. Each is **one character** (2 bytes as a `char`).

| Escape sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Horizontal tab |
| `\\` | Backslash |
| `\"` | Double quote |
| `\'` | Single quote |

```java
System.out.println("Incredible" + "\n" + "world");
// Incredible
// world
System.out.println("A picture is worth \t \"A thousand words.\" ");
// A picture is worth      "A thousand words."
```

**Example 4.** *(ICSE 2024, Q1(vi))* Which of the following is an escape sequence character in Java? (a) /n (b) \t (c) /t (d) //n
**Solution:** **(b) `\t`** — escape sequences begin with a **backslash**, not a forward slash.

### Tokens

A **token** is the **smallest individual unit** of a program. Java has five kinds:

| Token | Meaning | Examples |
|---|---|---|
| **Keywords** | **Reserved words** with a special meaning; all in **lower case**; cannot be used as names | `public`, `class`, `static`, `void`, `int`, `if`, `case`, `return`, `import`, `final`, `new` |
| **Identifiers** | **Names** given by the programmer to variables, methods, classes | `total`, `area_1`, `Student`, `_count` |
| **Literals (constants)** | **Fixed values** written directly | `25` (integer), `35.2` (real), `'a'` (character), `"AM"` (string), `true` (boolean), `null` |
| **Punctuators (separators)** | Symbols that separate parts of a program | `;` `,` `.` `( )` `{ }` `[ ]` |
| **Operators** | Symbols that perform operations | `+` `-` `*` `/` `%` `==` `&&` `++` `?:` |

**Rules for identifiers:** may contain letters, digits, `_` and the dollar sign; **cannot begin with a digit**; **no spaces**; **cannot be a keyword**; Java is **case sensitive** (`Total` and `total` differ).

**Example 5.** *(ICSE 2019, Q1(e))* Identify and name the following tokens: (i) public (ii) 'a' (iii) == (iv) { }
**Solution:** (i) **Keyword** (ii) **Character literal (constant)** (iii) **Operator** (iv) **Separator / punctuator**.

### Constants and variables

- A **variable** is a **named memory location** whose value can change during execution: `int age = 15;`
- A **constant** (final variable) is a variable whose value **cannot be changed** once assigned; it is declared with the keyword **`final`**: `final double PI = 3.14;`
- **Declaration** reserves memory (`int x;`); **initialisation** gives a first value (`int x = 10;`).

### Data types

![Fig. 1.2 Data types](figures/ca_ch01_fig02_data_types.png)

| Primitive type | Size | Kind | Default value | Example |
|---|---|---|---|---|
| `byte` | 1 byte (8 bits) | integer | 0 | `byte b = 100;` |
| `short` | 2 bytes (16 bits) | integer | 0 | `short s = 3000;` |
| `int` | 4 bytes (32 bits) | integer | 0 | `int n = 25;` |
| `long` | 8 bytes (64 bits) | integer | 0L | `long l = 9876543210L;` |
| `float` | 4 bytes (32 bits) | real (decimal) | 0.0f | `float f = 4.3f;` |
| `double` | 8 bytes (64 bits) | real (decimal) | 0.0d | `double d = 35.2;` |
| `char` | 2 bytes (16 bits) | single Unicode character | `'\u0000'` | `char c = 'a';` |
| `boolean` | (true or false only) | logical | false | `boolean ok = true;` |

**Non-primitive (reference / composite) types** — `String`, **arrays**, **classes** and interfaces. They are built from primitive types, store a **reference** to an object, and have the default value **`null`**.

**Default values** apply to **data members** (instance and class variables) that are not initialised: numbers 0, `char` the null character, `boolean` **false**, references (e.g. a `String`) **null**. Local variables get no default and must be initialised before use.

**Example 6.** *(ICSE 2019, Q1(d))* Write the memory capacity (storage size) of short and float data type in bytes.
**Solution:** **short – 2 bytes**; **float – 4 bytes**.

### Type conversion

**1. Implicit (automatic, widening) conversion** — done by Java when a **smaller type** is assigned to or combined with a **larger type**; no data is lost.

`byte → short → int → long → float → double` and `char → int`

- In an expression, `byte`, `short` and `char` are first promoted to **int**; the result takes the **largest type** in the expression (**type promotion**).
- `int m = 'F';` stores 70; `double d = 7;` stores 7.0.

**2. Explicit conversion (type casting, narrowing)** — done by the programmer, writing the type in brackets; data may be lost.

```java
int x = (int) 32.8;        // 32 — the decimal part is dropped
char ch = (char) 98;       // 'b'
double avg = (double) 7 / 2;   // 3.5 (7 is cast before dividing)
int amount = (int) valueINR;   // double to int
```

**Example 7.** *(ICSE 2023, Q1(xiii))* `int x = (int) 32.8;` is an example of ________ typecasting. (a) implicit (b) automatic (c) explicit (d) coercion
**Solution:** **(c) explicit** — the programmer writes `(int)`; x becomes 32.

### Packages and the import statement

- A **package** is a **group of related classes** (and sub-packages and interfaces), like a folder of ready-made code: `java.lang`, `java.util`, `java.io`.
- **`java.lang`** is the **default package** — imported automatically; it contains `String`, `Math`, `System` and the **wrapper classes** (`Integer`, `Character` …).
- The **`import`** keyword makes the classes of another package available: `import java.util.*;` (for `Scanner`) or `import java.util.Scanner;`.

**Example 8.** *(ICSE 2019, Q3(j))* What is meant by a package? Give an example.
**Solution:** A package in Java is a mechanism to **encapsulate a group of classes, sub-packages and interfaces**. Example: **java.lang**, java.util, java.io.

### Summary of the chapter

- **OOP vs POP** — objects (data + methods) vs procedures; OOP is more secure and reusable.
- **Principles** — abstraction (essential features, hide details), encapsulation (wrap data and methods), inheritance (acquire properties of another class), polymorphism (one name, many forms).
- **Java** — Gosling, Sun Microsystems, 1995; applications and applets; **source code (.java) → javac → byte code (.class) → JVM → machine code**; features: simple, object oriented, **platform independent**, robust, secure, multithreaded, portable.
- **Character set**; **ASCII** (7-bit) and **Unicode** (16-bit; Java char = 2 bytes); 'A' 65, 'a' 97, '0' 48.
- **Escape sequences** `\n \t \\ \" \'`.
- **Tokens** — keywords, identifiers, literals, punctuators, operators; Java is case sensitive.
- **Data types** — 8 primitive (sizes!) and non-primitive (String, array, class); default values (0, false, null).
- **Type conversion** — implicit (widening, promotion) and explicit (casting).
- **Packages** — java.lang (default), java.util (Scanner); `import`.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Distinguish procedure-oriented from object-oriented programming.
2. Define and illustrate abstraction, encapsulation, inheritance and polymorphism.
3. Explain source code, byte code, object code, the compiler and the JVM, and list the features of Java.
4. Use ASCII/Unicode values and escape sequences to predict output.
5. Classify tokens and write valid identifiers.
6. State the size, kind and default value of every primitive data type and distinguish primitive from non-primitive types.
7. Apply implicit and explicit type conversion.
8. Explain packages and the import statement.

---

## 3. Detailed Section Explanations

### Section 1 — Objects first
Java programs model the world as **objects with state and behaviour**. The four OOP principles explain how such objects are designed, protected, reused and made flexible.

### Section 2 — Compile once, run anywhere
`javac` turns your program into **byte code**; each computer's **JVM** runs it. Remember the chain — it answers questions on byte code, JVM and platform independence.

### Section 3 — A character is a number
Every `char` has a **Unicode value**. In arithmetic it becomes an `int`; cast back with `(char)` to see a letter again.

### Section 4 — Sizes matter
Questions on **bytes occupied** need the sizes table: multiply the element size by the number of elements for arrays (Chapter 10).

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Object | An entity with state (data) and behaviour (methods). |
| Class | A blueprint or template from which objects are created. |
| Abstraction | Showing essential features and hiding background details. |
| Encapsulation | Wrapping data and methods into a single unit. |
| Inheritance | One class acquiring the properties of another. |
| Polymorphism | One name taking many forms. |
| Source code | The program written in Java (.java file). |
| Byte code | Machine-independent code produced by the Java compiler (.class file). |
| JVM | The Java Virtual Machine that executes byte code. |
| Object code | Machine-language code run by the processor. |
| Platform independence | Running the same byte code on any operating system. |
| Java application | A stand-alone Java program with a main() method. |
| Java applet | A small Java program run inside a web page. |
| ASCII | 7-bit character code (0–127). |
| Unicode | 16-bit character code used by Java. |
| Escape sequence | A backslash and character representing a special character. |
| Token | The smallest unit of a program. |
| Keyword | A reserved word with a fixed meaning. |
| Identifier | A name given to a variable, method or class. |
| Literal | A constant value written in a program. |
| Variable | A named memory location whose value can change. |
| Constant | A final variable whose value cannot change. |
| Primitive data type | One of the 8 built-in types. |
| Non-primitive data type | A reference type such as String, array or class. |
| Implicit conversion | Automatic widening conversion by Java. |
| Explicit conversion | Type casting written by the programmer. |
| Package | A group of related classes. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| Full form of JVM | Java Virtual Machine |
| Code produced by the compiler | Java byte code (.class) |
| Extension of a source file | .java |
| Byte code runs on all operating systems | Platform independent |
| Sizes | byte 1, short 2, int 4, long 8, float 4, double 8, char 2 bytes |
| A char occupies | 16 bits (2 bytes) — Unicode |
| 'A', 'a', '0', space | 65, 97, 48, 32 |
| Default values of data members | int 0, double 0.0, boolean false, String null |
| Keyword for a constant | final |
| Keyword to use a package | import |
| Default package | java.lang |
| Package of Scanner | java.util |
| Valid keywords (examples) | static, case, if, for, return, final, import |
| Not keywords | Switch, If, BOOLEAN, every, all (Java is case sensitive) |
| `(int) 32.8` | 32 — explicit typecasting |
| Father–child picture | Inheritance |

### 5.2 Memory aids

- **"A PIE"** — **A**bstraction, **P**olymorphism, **I**nheritance, **E**ncapsulation.
- **"1-2-4-8, 4-8, 2"** — byte-short-int-long, float-double, char.
- **"Small = capital + 32"** — 'a' (97) = 'A' (65) + 32.
- **"KILPO"** — Keywords, Identifiers, Literals, Punctuators, Operators.

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- The JVM today uses a **just-in-time (JIT) compiler**, turning frequently run byte code into machine code for speed.
- Android apps are written largely in Java and Kotlin and run on a virtual machine similar in spirit to the JVM.
- Unicode now has more than 150,000 characters; Java represents rare ones with a pair of `char` values.

---

## 6. Person Profiles

### 6.1 James Gosling (born 1955)
A Canadian computer scientist who led the team at Sun Microsystems that created Java (first called Oak) in the early 1990s. He is often called the "father of Java".

### 6.2 Alan Kay (born 1940)
An American computer scientist who coined the term "object-oriented programming" and led the development of Smalltalk at Xerox PARC in the 1970s — the language that shaped the ideas of objects and message passing used in Java.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Model the world as objects** — data and behaviour belong together.
- **Separate writing from running** — byte code and the JVM make programs portable.
- **Everything in memory is a number** — characters, too.

### 7.2 Real-life connections
- **Meghalaya:** a bus booking app for the Shillong–Guwahati route can be modelled with objects such as Bus, Seat and Passenger — each with its own data and actions.
- **Your phone:** apps installed from the same store run on phones from different makers — the same idea as platform independence.
- **Languages:** Unicode lets an app display Khasi, Garo, Hindi and English text on one screen.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section A** (40 marks, compulsory) = **Question 1**: twenty MCQs (1 mark each) and **Question 2**: ten short parts (2 marks each). **Section B** (60 marks) = any **four** of six programs (15 marks each). In **2017–2020** Section A had Questions 1–3 with 2-mark parts and Section B Questions 4–9. This chapter supplies many Section A questions; programs in Section B use its data types and casts.

### 8.1 Graded exercises — solutions

#### Exercise 1A — OOP and Java

**Q1.** Distinguish between encapsulation and abstraction.
**Answer:** Encapsulation wraps data and methods into one unit (a class) and controls access; abstraction shows only essential features and hides details.

**Q2.** Why is Java called platform independent?
**Answer:** Its compiler produces byte code, which runs on any operating system that has a JVM.

**Q3.** Name the file extensions of Java source code and byte code.
**Answer:** .java and .class.

**Q4.** Which OOP principle does method overloading illustrate?
**Answer:** Polymorphism.

#### Exercise 1B — Values and data types

**Q5.** Give the output: `System.out.println((char)('a' + 1) + " " + ('a' + 1));`
**Answer:** `b 98`

**Q6.** Which of these are valid identifiers: 2ndPrize, total_marks, class, _rate?
**Answer:** total_marks and _rate (2ndPrize begins with a digit; class is a keyword).

**Q7.** What is the value of `7 / 2 + " " + (double) 7 / 2`?
**Answer:** `3 3.5` — integer division gives 3; casting 7 to double gives 3.5.

**Q8.** How many bytes do (a) a long and a char together (b) three int variables occupy?
**Answer:** (a) 8 + 2 = 10 bytes. (b) 3 × 4 = 12 bytes.

### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(i) (1 mark) | The full form of JVM is: (a) Java Visible Machine (b) Java Virtual Mode (c) Java Virtual Machine (d) Java Visible Mode |
| ICSE 2026, Q1(ii) (1 mark) | Which of the following occupies 2 bytes of storage? (a) 25 (b) AM (c) 35.2 (d) `\\` |
| ICSE 2026 Improvement, Q1(xi) (1 mark) | Which of the following represents the escape sequence for a new line? (a) `\n` (b) `/n` (c) `//n` (d) `\\n` |
| ICSE 2026 Improvement, Q1(xii) (1 mark) | Raj was asked to accept the name of the employee, gender and the basic salary. Help him to choose the correct datatypes in order. (a) String, char, double (b) char, int, boolean (c) double, char, String (d) int, char, double |
| ICSE 2026 Improvement, Q1(xvi) (1 mark) | Which of the following is the correct output for the java statement: `System.out.println("Dear Child\n\"May God Bless You\"");` (a) Dear Child "May God Bless You" (b) Dear Child"May God Bless You" (c) Dear childMayGod Bless You (d) Dear Child `\"May God Bless You\"` |
| ICSE 2026 Improvement, Q1(xix) (1 mark) | Which of the following is NOT a keyword? (a) if (b) for (c) return (d) Switch |
| ICSE 2025, Q1(ii) (1 mark) | `System.out.println('Z'+32);` will display: (a) z (b) Z (c) 122 (d) 154 |
| ICSE 2025, Q1(xviii) (1 mark) | `System.out.println("I said,\"It\'s wise to obey elders.\"");` The output of the above statement is: (a) I said,'It is wise to obey elders.' (b) I said, "It's wise to obey elders." (c) I said,It's wise to elders. (d) "'It's wise to obey elders.'" |
| ICSE 2025 Improvement, Q1(vi) (1 mark) | Typecasting is often necessary when dealing with financial data. Identify the correct syntax to typecast a double to an int using the variables: int amount; double valueINR (a) `int amount = valueINR;` (b) `int amount = Integer.parseInt(valueINR);` (c) `int amount = (int) valueINR;` (d) `int amount = int (valueINR);` |
| ICSE 2025 Improvement, Q1(xi) (1 mark) | Which of the following is not a type of token in Java? 1. Method 2. Identifier 3. Literal 4. Keyword (a) only 1 (b) 1 and 3 (c) only 2 (d) only 4 |
| ICSE 2025 specimen, Q1(ii) (1 mark) | "Java compiled code (byte code) can run on all operating systems" — Name the feature. (a) Robust and Secure (b) Object Oriented (c) Platform Independent (d) Multithreaded |
| ICSE 2025 specimen, Q1(iii) (1 mark) | The size of `'\n'` is: (a) 2 bytes (b) 4 bytes (c) 8 bytes (d) 16 bytes |
| ICSE 2025 specimen, Q1(v) (1 mark) | Which of the following is a valid java keyword? (a) If (b) BOOLEAN (c) static (d) Switch |
| ICSE 2025 specimen, Q1(xiv) (1 mark) | The default value of a boolean variable is: (a) False (b) 0 (c) false (d) True |
| ICSE 2024, Q1(ii) (1 mark) | `int x = 98; char ch = (char)x;` what is the value in ch? (a) b (b) A (c) B (d) 97 |
| ICSE 2024, Q1(vi) (1 mark) | Which of the following is an escape sequence character in Java? (a) `/n` (b) `\t` (c) `/t` (d) `//n` |
| ICSE 2024, Q1(x) (1 mark) | The extension of a Java source code file is: (a) exe (b) obj (c) jvm (d) java |
| ICSE 2024 specimen, Q1(i) (1 mark) | [Picture: a lion labelled "Father" and a cub labelled "Child"] Name the feature of java depicted in the above picture. (a) Encapsulation (b) Inheritance (c) Abstraction (d) Polymorphism |
| ICSE 2024 specimen, Q1(vii) (1 mark) | Among the following which is a keyword: (a) every (b) all (c) case (d) each |
| ICSE 2024 specimen, Q1(xv) (1 mark) | Which of the following is a valid Integer constant: 1. 4 2. 4.0 3. 4.3f 4. "four" (a) Only 1. (b) 1. and 3. (c) 2. and 4. (d) 1. and 2. |
| ICSE 2024 specimen, Q1(xvii) (1 mark) | Assertion (A): In java statements written in lower case letter or upper case letter are treated as the same. Reason (R): Java is a case sensitive language. (a) Both (A) and (R) are true and (R) is a correct explanation of (A) (b) Both (A) and (R) are true and (R) is not a correct explanation of (A) (c) (A) is true and (R) is false (d) (A) is false and (R) is true |
| ICSE 2024 specimen, Q2(ix) (2 marks) | When there is no explicit initialization, what are the default values set for variables in the following cases? (a) Integer variable (b) String variable |
| ICSE 2023, Q1(i) (1 mark) | A mechanism where one class acquires the properties of another class: (a) Polymorphism (b) Inheritance (c) Encapsulation (d) Abstraction |
| ICSE 2023, Q1(iv) (1 mark) | The keyword used to call package in the program: (a) extends (b) export (c) import (d) package |
| ICSE 2023, Q1(xiii) (1 mark) | `int x = (int) 32.8;` is an example of __________ typecasting. (a) implicit (b) automatic (c) explicit (d) coercion |
| ICSE 2023, Q1(xiv) (1 mark) | The code obtained after compilation is known as: (a) source code (b) object code (c) machine code (d) java byte code |
| ICSE 2023, Q1(xix) (1 mark) | The number of bits occupied by the value 'a' are: (a) 1 bit (b) 2 bits (c) 4 bits (d) 16 bits |
| ICSE 2023, Q2(x) (2 marks) | Write the value of n after execution: `char ch ='d'; int n = ch + 5;` |
| ICSE 2020, Q1(a) (2 marks) | Define Java byte code. |
| ICSE 2020, Q1(c) (2 marks) | Name the following: (i) The keyword which converts variable into constant. (ii) The method which terminates the entire program from any stage. |
| ICSE 2020, Q1(d) (2 marks) | Which of the following are primitive data types? (i) double (ii) String (iii) char (iv) Integer |
| ICSE 2020, Q2(d) (2 marks) | What is the use of import statement in Java? |
| ICSE 2020, Q3(d) (2 marks) | Write the output of the following statement: `System.out.println("A picture is worth \t \"A thousand words.\" ");` |
| ICSE 2019, Q1(a) (2 marks) | Name any two basic principles of Object-oriented Programming. |
| ICSE 2019, Q1(d) (2 marks) | Write the memory capacity (storage size) of short and float data type in bytes. |
| ICSE 2019, Q1(e) (2 marks) | Identify and name the following tokens: (i) public (ii) 'a' (iii) == (iv) { } |
| ICSE 2019, Q3(j) (2 marks) | What is meant by a package? Give an example. |
| ICSE 2018, Q1(a) (2 marks) | Define abstraction. |
| ICSE 2018, Q3(e) (2 marks) | Write the output for the following: `System.out.println("Incredible"+"\n"+"world");` |
| ICSE 2017, Q1(a) (2 marks) | What is inheritance? |
| ICSE 2017, Q1(c) (2 marks) | State the number of bytes occupied by char and int data types. |
| ICSE 2017, Q2(a) (2 marks) | Name the following: (i) A keyword used to call a package in the program. (ii) Any one reference data type. |
| ICSE 2017, Q2(e) (2 marks) | Write the output: `char ch = 'F'; int m = ch; m=m+5; System.out.println(m + " " + ch);` |

**Solutions**

**2026 Q1(i).** **(c) Java Virtual Machine.** *(Worked answer.)*

**2026 Q1(ii).** **(d) `\\`** — an escape sequence is one **char** (Unicode), which occupies **2 bytes**; 25 is an int (4 bytes), 35.2 a double (8 bytes) and AM a string of two characters. *(Worked answer.)*

**2026 Improvement Q1(xi).** **(a) `\n`.** *(Worked answer.)*

**2026 Improvement Q1(xii).** **(a) String, char, double** — a name is text (String), gender a single letter such as 'M' or 'F' (char), salary a decimal amount (double). *(Worked answer.)*

**2026 Improvement Q1(xvi).** **(a)** — `\n` moves to a new line and `\"` prints a double quote, so the output is:
```
Dear Child
"May God Bless You"
```
*(Worked answer.)*

**2026 Improvement Q1(xix).** **(d) Switch** — keywords are in lower case; `switch` is a keyword but `Switch` is not. *(Worked answer.)*

**2025 Q1(ii).** **(c) 122** — `'Z'` (90) + 32 is an int addition.

**2025 Q1(xviii).** **(b) I said, "It's wise to obey elders."** — `\"` prints `"` and `\'` prints `'`.

**2025 Improvement Q1(vi).** **(c) `int amount = (int) valueINR;`** — explicit typecasting. *(Worked answer.)*

**2025 Improvement Q1(xi).** **(a) only 1** — a method is not a token; identifiers, literals and keywords are. *(Worked answer.)*

**2025 specimen Q1(ii).** **(c) Platform Independent.**

**2025 specimen Q1(iii).** **(a) 2 bytes.**

**2025 specimen Q1(v).** **(c) static.**

**2025 specimen Q1(xiv).** **(c) false.**

**2024 Q1(ii).** **(a) b** — 98 is the Unicode value of 'b'.

**2024 Q1(vi).** **(b) `\t`.**

**2024 Q1(x).** **(d) java.**

**2024 specimen Q1(i).** **(b) Inheritance** — the child acquires the features of the father. *(Worked answer.)*

**2024 specimen Q1(vii).** **(c) case.** *(Worked answer.)*

**2024 specimen Q1(xv).** **(a) Only 1.** — 4 is an integer literal; 4.0 and 4.3f are real, "four" is a string. *(Worked answer.)*

**2024 specimen Q1(xvii).** **(d) (A) is false and (R) is true** — because Java is case sensitive, `int` and `INT` are different. *(Worked answer.)*

**2024 specimen Q2(ix).** (a) Integer variable — **0**. (b) String variable — **null**. *(Worked answer.)*

**2023 Q1(i).** **(b) Inheritance.**

**2023 Q1(iv).** **(c) import.**

**2023 Q1(xiii).** **(c) explicit.**

**2023 Q1(xiv).** **(d) java byte code.** *(Worked answer.)*

**2023 Q1(xix).** **(d) 16 bits** — a char takes 2 bytes. *(Worked answer.)*

**2023 Q2(x).** **n = 105** — `'d'` is 100; 100 + 5 = 105. *(Worked answer.)*

**2020 Q1(a).** Java **byte code** is the **intermediate, machine-independent code** produced by the **Java compiler** from the source code (a .class file); it is executed by the **Java Virtual Machine**. *(Worked answer.)*

**2020 Q1(c).** (i) **final**. (ii) **System.exit(0)**. *(Worked answer.)*

**2020 Q1(d).** **(i) double** and **(iii) char** — String and Integer are classes (non-primitive). *(Worked answer.)*

**2020 Q2(d).** The **import** statement makes the **classes of a package available** to a program, e.g. `import java.util.*;` lets the program use **Scanner**. *(Worked answer.)*

**2020 Q3(d).** `\t` gives a tab and `\"` prints a double quote:
```
A picture is worth        "A thousand words."
```
(The gap after "worth " is a tab.)
*(Worked answer.)*

**2019 Q1(a).** **Encapsulation, Data Abstraction, Polymorphism, Inheritance** (any two).

**2019 Q1(d).** **short – 2 bytes; float – 4 bytes.**

**2019 Q1(e).** (i) **Keyword** (ii) **Character literal / constant** (iii) **Operator** (iv) **Separator / punctuator**.

**2019 Q3(j).** A package in Java is a mechanism to **encapsulate a group of classes, sub-packages and interfaces**. Example: **java.lang**, java.util, java.io.

**2018 Q1(a).** **Abstraction** — the act of **representing essential features** and **hiding unnecessary or background details**.

**2018 Q3(e).**
```
Incredible
world
```

**2017 Q1(a).** **Inheritance** is the mechanism by which **one class acquires the properties (data members and methods) of another class**; e.g. a class Car inherits the features of a class Vehicle. *(Worked answer.)*

**2017 Q1(c).** **char — 2 bytes; int — 4 bytes.** *(Worked answer.)*

**2017 Q2(a).** (i) **import**. (ii) Any one: **String**, an **array**, a **class**. *(Worked answer.)*

**2017 Q2(e).** `ch` is 'F' (70); m = 70 + 5 = 75:
```
75 F
```
*(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Give the output: `System.out.println('A' + 'B' + " " + "A" + 'B');`
**Answer:** `131 AB` — 'A' + 'B' = 65 + 66 = 131 (int addition before any string); then "A" + 'B' joins as text.

**Q2.** (2 marks) Give the output: `System.out.println(1 + 2 + "3" + 4 + 5);`
**Answer:** `3345` — 1 + 2 = 3 first; once a string appears, the rest are joined.

**Q3.** (2 marks) What is stored in `f` after `float f = 10 / 4;`?
**Answer:** `2.0` — 10 / 4 is integer division (2), then widened to float.

**Q4.** (2 marks) Name the OOP principle: (a) a remote control hides the circuit (b) a smartphone class reuses features of a phone class.
**Answer:** (a) Abstraction. (b) Inheritance.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| MCQ | OOP principle from a picture; JVM; byte code; platform independence; keyword vs non-keyword; escape sequence; size of char/'\n'; default boolean | 8.2, Section 1 |
| 2 marks | Output of char arithmetic ('Z' + 32, 'd' + 5, (char) 98); output with `\n`, `\t`, `\"` | 8.2, 8.3 |
| 2 marks | Tokens; data type sizes; primitive vs non-primitive; package and import; final; define byte code / abstraction / inheritance | 8.2, Section 1 |

---

## 9. MCQs with Explanations

### OOP principles (Q1–Q12)

**Q1.** Wrapping up data and methods into a single unit is called
- (a) abstraction
- (b) encapsulation
- (c) inheritance
- (d) polymorphism

**Answer:** (b) encapsulation
**Explanation:** A class binds data and methods together.

**Q2.** Representing essential features and hiding background details is
- (a) abstraction
- (b) inheritance
- (c) polymorphism
- (d) compilation

**Answer:** (a) abstraction
**Explanation:** 2018 marking scheme.

**Q3.** A mechanism where one class acquires the properties of another class is
- (a) polymorphism
- (b) encapsulation
- (c) abstraction
- (d) inheritance

**Answer:** (d) inheritance
**Explanation:** 2023 marking scheme.

**Q4.** The ability of one method name to work in different ways is
- (a) encapsulation
- (b) inheritance
- (c) abstraction
- (d) polymorphism

**Answer:** (d) polymorphism
**Explanation:** "Many forms" — e.g. method overloading.

**Q5.** A picture of a father and his child illustrates
- (a) inheritance
- (b) encapsulation
- (c) abstraction
- (d) polymorphism

**Answer:** (a) inheritance
**Explanation:** 2024 specimen picture.

**Q6.** Driving a car without knowing how its engine works illustrates
- (a) inheritance
- (b) abstraction
- (c) polymorphism
- (d) type casting

**Answer:** (b) abstraction
**Explanation:** Only essential controls are shown.

**Q7.** A medicine capsule holding several ingredients inside one cover illustrates
- (a) polymorphism
- (b) inheritance
- (c) encapsulation
- (d) abstraction

**Answer:** (c) encapsulation
**Explanation:** Many items wrapped in one unit.

**Q8.** Which of these is NOT a principle of OOP?
- (a) Inheritance
- (b) Polymorphism
- (c) Encapsulation
- (d) Compilation

**Answer:** (d) Compilation
**Explanation:** The four are abstraction, encapsulation, inheritance, polymorphism.

**Q9.** In procedure-oriented programming, the emphasis is on
- (a) procedures (functions)
- (b) objects
- (c) classes
- (d) data hiding

**Answer:** (a) procedures (functions)
**Explanation:** OOP emphasises data and objects.

**Q10.** Which of these is an object-oriented language?
- (a) BASIC
- (b) Java
- (c) C
- (d) Assembly language

**Answer:** (b) Java
**Explanation:** Java is built around classes and objects.

**Q11.** A class can best be described as
- (a) a single value
- (b) a keyword
- (c) an operator
- (d) a blueprint from which objects are created

**Answer:** (d) a blueprint from which objects are created
**Explanation:** Also an object factory and a user-defined type.

**Q12.** An object has
- (a) only data
- (b) only methods
- (c) neither data nor methods
- (d) state (data) and behaviour (methods)

**Answer:** (d) state (data) and behaviour (methods)
**Explanation:** Attributes plus methods.

### Java, byte code and JVM (Q13–Q24)

**Q13.** The full form of JVM is
- (a) Java Visible Machine
- (b) Java Virtual Machine
- (c) Java Virtual Mode
- (d) Java Variable Method

**Answer:** (b) Java Virtual Machine
**Explanation:** 2026 board MCQ.

**Q14.** The code obtained after compiling a Java program is
- (a) java byte code
- (b) source code
- (c) machine code
- (d) assembly code

**Answer:** (a) java byte code
**Explanation:** Stored in a .class file.

**Q15.** The extension of a Java source code file is
- (a) .class
- (b) .exe
- (c) .java
- (d) .obj

**Answer:** (c) .java
**Explanation:** 2024 board MCQ.

**Q16.** Byte code is stored in a file with the extension
- (a) .java
- (b) .txt
- (c) .jvm
- (d) .class

**Answer:** (d) .class
**Explanation:** Produced by javac.

**Q17.** The program that executes byte code on a computer is the
- (a) JVM
- (b) javac compiler
- (c) editor
- (d) operating system alone

**Answer:** (a) JVM
**Explanation:** The Java Virtual Machine interprets byte code.

**Q18.** "Java byte code can run on all operating systems" describes the feature
- (a) robust
- (b) platform independent
- (c) multithreaded
- (d) object oriented

**Answer:** (b) platform independent
**Explanation:** 2025 specimen MS.

**Q19.** The Java compiler is named
- (a) java
- (b) jvm
- (c) jdb
- (d) javac

**Answer:** (d) javac
**Explanation:** java runs; javac compiles.

**Q20.** A small Java program that runs inside a web page is
- (a) an application
- (b) a package
- (c) a token
- (d) an applet

**Answer:** (d) an applet
**Explanation:** Applications are stand-alone.

**Q21.** Java was developed at
- (a) Sun Microsystems
- (b) Microsoft
- (c) IBM
- (d) Apple

**Answer:** (a) Sun Microsystems
**Explanation:** By James Gosling's team; now owned by Oracle.

**Q22.** Java's ability to do several tasks at the same time is called
- (a) portability
- (b) multithreading
- (c) abstraction
- (d) robustness

**Answer:** (b) multithreading
**Explanation:** A feature of Java.

**Q23.** Machine-language instructions actually run by the processor are called
- (a) byte code
- (b) source code
- (c) object code
- (d) pseudocode

**Answer:** (c) object code
**Explanation:** The final machine code.

**Q24.** Statement I: javac converts source code into byte code. Statement II: The JVM executes byte code.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (a) Both statements are true
**Explanation:** Compile, then run on the JVM.

### Characters, ASCII and escape sequences (Q25–Q36)

**Q25.** The output of `System.out.println('Z'+32);` is
- (a) small z
- (b) capital Z
- (c) 122
- (d) 154

**Answer:** (c) 122
**Explanation:** 'Z' is 90; 90 + 32 = 122.

**Q26.** After `int x = 98; char ch = (char)x;` the value of ch is
- (a) b
- (b) capital B
- (c) 97
- (d) capital A

**Answer:** (a) b
**Explanation:** 98 is the code of small b.

**Q27.** The Unicode value of 'A' is
- (a) 97
- (b) 65
- (c) 48
- (d) 32

**Answer:** (b) 65
**Explanation:** 'a' is 97.

**Q28.** The number of bits occupied by the value 'a' is
- (a) 1
- (b) 8
- (c) 16
- (d) 32

**Answer:** (c) 16
**Explanation:** A char takes 2 bytes.

**Q29.** The size of `'\n'` is
- (a) 2 bytes
- (b) 4 bytes
- (c) 8 bytes
- (d) 1 bit

**Answer:** (a) 2 bytes
**Explanation:** An escape sequence is one char.

**Q30.** Which of these is an escape sequence?
- (a) `/n`
- (b) `//t`
- (c) `\t`
- (d) `/t`

**Answer:** (c) `\t`
**Explanation:** Escape sequences begin with a backslash.

**Q31.** The escape sequence for a new line is
- (a) `\t`
- (b) `\n`
- (c) `\\`
- (d) `\"`

**Answer:** (b) `\n`
**Explanation:** n for new line.

**Q32.** `char ch = 'd'; int n = ch + 5;` stores in n
- (a) 105
- (b) i
- (c) d5
- (d) 100

**Answer:** (a) 105
**Explanation:** 100 + 5.

**Q33.** ASCII uses
- (a) 16 bits
- (b) 32 bits
- (c) 7 bits
- (d) 64 bits

**Answer:** (c) 7 bits
**Explanation:** 0 to 127.

**Q34.** Java uses Unicode because
- (a) it is shorter than ASCII
- (b) it can represent characters of almost all languages
- (c) it uses only digits
- (d) it needs no memory

**Answer:** (b) it can represent characters of almost all languages
**Explanation:** 16-bit codes.

**Q35.** `System.out.println("Incredible"+"\n"+"world");` prints
- (a) `Incredible\nworld`
- (b) Incredible world
- (c) Incredible and world on separate lines
- (d) world Incredible

**Answer:** (c) Incredible and world on separate lines
**Explanation:** \n starts a new line.

**Q36.** The code of the digit character '0' is
- (a) 0
- (b) 65
- (c) 97
- (d) 48

**Answer:** (d) 48
**Explanation:** '9' is 57.

### Tokens, keywords and identifiers (Q37–Q50)

**Q37.** The smallest individual unit of a program is a
- (a) token
- (b) class
- (c) package
- (d) method

**Answer:** (a) token
**Explanation:** Keywords, identifiers, literals, punctuators, operators.

**Q38.** Which of these is a valid Java keyword?
- (a) If
- (b) BOOLEAN
- (c) static
- (d) Switch

**Answer:** (c) static
**Explanation:** 2025 specimen MS — keywords are lower case.

**Q39.** Which of these is NOT a keyword?
- (a) for
- (b) return
- (c) if
- (d) Switch

**Answer:** (d) Switch
**Explanation:** Capital S makes it an identifier.

**Q40.** Which of these is a keyword?
- (a) every
- (b) case
- (c) all
- (d) each

**Answer:** (b) case
**Explanation:** Used in switch.

**Q41.** The token 'a' is a
- (a) keyword
- (b) identifier
- (c) character literal
- (d) operator

**Answer:** (c) character literal
**Explanation:** 2019 MS.

**Q42.** The token { } is a
- (a) separator (punctuator)
- (b) operator
- (c) keyword
- (d) literal

**Answer:** (a) separator (punctuator)
**Explanation:** 2019 MS.

**Q43.** Which identifier is valid?
- (a) 2ndPrize
- (b) total marks
- (c) class
- (d) total_marks

**Answer:** (d) total_marks
**Explanation:** No leading digit, no space, not a keyword.

**Q44.** Which is NOT a type of token?
- (a) keyword
- (b) method
- (c) literal
- (d) identifier

**Answer:** (b) method
**Explanation:** 2025 Improvement.

**Q45.** A valid integer constant is
- (a) 4.0
- (b) 4.3f
- (c) "four"
- (d) 4

**Answer:** (d) 4
**Explanation:** The others are real or string literals.

**Q46.** The keyword that makes a variable a constant is
- (a) final
- (b) static
- (c) const
- (d) void

**Answer:** (a) final
**Explanation:** final double PI = 3.14;

**Q47.** Java treats Total and total as
- (a) the same identifier
- (b) keywords
- (c) different identifiers
- (d) errors

**Answer:** (c) different identifiers
**Explanation:** Java is case sensitive.

**Q48.** A named memory location whose value can change is a
- (a) constant
- (b) variable
- (c) keyword
- (d) literal

**Answer:** (b) variable
**Explanation:** Constants cannot change.

**Q49.** The keyword used to call a package into a program is
- (a) extends
- (b) export
- (c) package
- (d) import

**Answer:** (d) import
**Explanation:** 2023 MS.

**Q50.** The default package of Java is
- (a) java.util
- (b) java.io
- (c) java.lang
- (d) java.awt

**Answer:** (c) java.lang
**Explanation:** Imported automatically.

### Data types (Q51–Q66)

**Q51.** The size of a short in bytes is
- (a) 1
- (b) 2
- (c) 4
- (d) 8

**Answer:** (b) 2
**Explanation:** 2019 MS.

**Q52.** The size of a float in bytes is
- (a) 4
- (b) 2
- (c) 8
- (d) 16

**Answer:** (a) 4
**Explanation:** double is 8.

**Q53.** The size of a long in bytes is
- (a) 2
- (b) 4
- (c) 16
- (d) 8

**Answer:** (d) 8
**Explanation:** 64 bits.

**Q54.** Which occupies 2 bytes of storage?
- (a) 25
- (b) 35.2
- (c) `'\\'`
- (d) "AM"

**Answer:** (c) `'\\'`
**Explanation:** A single char.

**Q55.** The default value of a boolean data member is
- (a) True
- (b) 0
- (c) false
- (d) null

**Answer:** (c) false
**Explanation:** 2025 specimen MS.

**Q56.** The default value of a String data member is
- (a) null
- (b) 0
- (c) an empty space
- (d) false

**Answer:** (a) null
**Explanation:** A reference type.

**Q57.** Which of these is a primitive data type?
- (a) String
- (b) char
- (c) array
- (d) Integer

**Answer:** (b) char
**Explanation:** String, arrays and Integer are reference types.

**Q58.** Which of these is a non-primitive data type?
- (a) int
- (b) double
- (c) boolean
- (d) array

**Answer:** (d) array
**Explanation:** Also String and classes.

**Q59.** The correct data types for a name, gender and basic salary are
- (a) String, char, double
- (b) char, int, boolean
- (c) double, char, String
- (d) int, char, double

**Answer:** (a) String, char, double
**Explanation:** 2026 Improvement MCQ.

**Q60.** How many primitive data types does Java have?
- (a) 4
- (b) 6
- (c) 8
- (d) 10

**Answer:** (c) 8
**Explanation:** byte, short, int, long, float, double, char, boolean.

**Q61.** A boolean variable can hold
- (a) any number
- (b) only true or false
- (c) only characters
- (d) only null

**Answer:** (b) only true or false
**Explanation:** Logical type.

**Q62.** Three int variables together occupy
- (a) 3 bytes
- (b) 6 bytes
- (c) 8 bytes
- (d) 12 bytes

**Answer:** (d) 12 bytes
**Explanation:** 3 × 4.

**Q63.** A real literal such as 35.2 is by default of type
- (a) float
- (b) double
- (c) int
- (d) long

**Answer:** (b) double
**Explanation:** Write 35.2f for a float.

**Q64.** Integer types arranged from smallest to largest are
- (a) byte, short, int, long
- (b) short, byte, long, int
- (c) int, long, byte, short
- (d) long, int, short, byte

**Answer:** (a) byte, short, int, long
**Explanation:** 1, 2, 4, 8 bytes.

**Q65.** Non-primitive data types store
- (a) only characters
- (b) only true or false
- (c) a reference (address) to an object
- (d) nothing

**Answer:** (c) a reference (address) to an object
**Explanation:** Hence the default null.

**Q66.** Statement I: char is 2 bytes in Java. Statement II: Java uses 7-bit ASCII for char.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (c) Statement I is true, Statement II is false
**Explanation:** Java uses 16-bit Unicode.

### Type conversion (Q67–Q76)

**Q67.** `int x = (int) 32.8;` is an example of
- (a) implicit typecasting
- (b) explicit typecasting
- (c) automatic conversion
- (d) coercion

**Answer:** (b) explicit typecasting
**Explanation:** 2023 MS.

**Q68.** After `int x = (int) 32.8;` x holds
- (a) 32.8
- (b) 33
- (c) 32
- (d) 0

**Answer:** (c) 32
**Explanation:** The decimal part is dropped.

**Q69.** The correct way to typecast a double valueINR to an int amount is
- (a) int amount = valueINR;
- (b) int amount = Integer.parseInt(valueINR);
- (c) int amount = int(valueINR);
- (d) int amount = (int) valueINR;

**Answer:** (d) int amount = (int) valueINR;
**Explanation:** 2025 Improvement.

**Q70.** Converting a smaller type to a larger type automatically is
- (a) implicit (widening) conversion
- (b) explicit conversion
- (c) narrowing
- (d) unboxing

**Answer:** (a) implicit (widening) conversion
**Explanation:** No data lost.

**Q71.** The value of `7 / 2` in Java is
- (a) 3.5
- (b) 3
- (c) 4
- (d) 3.0

**Answer:** (b) 3
**Explanation:** Integer division drops the fraction.

**Q72.** The value of `(double) 7 / 2` is
- (a) 3
- (b) 3.0
- (c) 4.0
- (d) 3.5

**Answer:** (d) 3.5
**Explanation:** 7 becomes 7.0 before dividing.

**Q73.** After `float f = 10 / 4;` f holds
- (a) 2.5
- (b) 2.0
- (c) 3.0
- (d) an error

**Answer:** (b) 2.0
**Explanation:** 10 / 4 = 2 first, then widened.

**Q74.** In the expression 'a' + 1, the result type is
- (a) int
- (b) char
- (c) String
- (d) boolean

**Answer:** (a) int
**Explanation:** char is promoted to int (98).

**Q75.** The output of `System.out.println(1 + 2 + "3" + 4 + 5);` is
- (a) 15
- (b) 12345
- (c) 339
- (d) 3345

**Answer:** (d) 3345
**Explanation:** 1 + 2 = 3, then strings join.

**Q76.** In an expression with an int and a double, the result is
- (a) int
- (b) long
- (c) double
- (d) char

**Answer:** (c) double
**Explanation:** The larger type wins (type promotion).

---

## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** Distinguish between procedure-oriented and object-oriented programming.
**Answer:** POP builds a program from procedures and lets data move freely between them.
OOP builds it from objects that combine data and methods, keeping data secure.

**Q2.** Define encapsulation and give a real-life example.
**Answer:** Encapsulation is wrapping data and the methods that act on it into a single unit (a class).
Example: a capsule; a bank account changed only through deposit and withdraw.

**Q3.** Define polymorphism. Name the Java feature that shows it.
**Answer:** Polymorphism is the ability of one name to take many forms.
Method overloading (e.g. several calculate() methods) shows it.

**Q4.** What is the role of the JVM?
**Answer:** The Java Virtual Machine executes byte code.
It converts byte code into the machine code of that computer, making Java platform independent.

**Q5.** Distinguish between source code and byte code.
**Answer:** Source code is the program written by the programmer (.java).
Byte code is the machine-independent code produced by javac from it (.class).

**Q6.** Distinguish between a Java application and a Java applet.
**Answer:** An application is a stand-alone program with a main() method.
An applet is a small program that runs inside a web page.

**Q7.** State two rules for naming identifiers.
**Answer:** An identifier cannot begin with a digit or contain spaces.
It cannot be a keyword; Java treats capital and small letters as different.

**Q8.** What is an escape sequence? Give two examples.
**Answer:** A backslash followed by a character that stands for a special character.
`\n` (new line), `\t` (tab), `\"` (double quote).

**Q9.** Distinguish between a variable and a constant.
**Answer:** A variable is a named memory location whose value can change.
A constant is declared with final and its value cannot change.

**Q10.** Distinguish between primitive and non-primitive data types.
**Answer:** Primitive types are the 8 built-in types with fixed sizes (int, char …).
Non-primitive types (String, arrays, classes) are built from them and store references.

**Q11.** Distinguish between implicit and explicit type conversion.
**Answer:** Implicit conversion is done automatically from a smaller to a larger type (int to double).
Explicit conversion (casting) is written by the programmer, e.g. (int) 32.8.

**Q12.** What is a package? Name the default package.
**Answer:** A group of related classes, sub-packages and interfaces.
java.lang is imported by default.

### Output and error questions (2 marks each)

**Q13.** Give the output: `char c = 'B'; c++; System.out.println(c + " " + (c + 1));`
**Answer:** `C 68`
c becomes 'C'; c + 1 is the int 68.

**Q14.** Give the output: `int a = 'a' - 'A'; System.out.println(a);` and `System.out.println((char)('a' + 25));`
**Answer:** `32` and `z`
97 − 65 = 32; 97 + 25 = 122, the code of z.

**Q15.** Give the output: `double d = 5 / 2; System.out.println(d);`
**Answer:** `2.0`
5 / 2 is integer division (2), then widened to 2.0.

**Q16.** Give the output: `System.out.println((int) 'A' + (char) 66);`
**Answer:** `131`
65 + 66 — a char in an arithmetic expression is treated as its code.

**Q17.** Give the output of `System.out.println("Sum = " + 2 + 3);` and `System.out.println("Sum = " + (2 + 3));`
**Answer:** `Sum = 23` and `Sum = 5`
Once a string comes first, + joins text; brackets add first.

**Q18.** Give the output: `System.out.println("Line1\tA\nLine2");`
**Answer:** Line1, a tab, A on the first line; Line2 on the next line.
`\t` is a tab and `\n` a new line.

**Q19.** Identify the error: `final int MAX = 10; MAX = 20;`
**Answer:** Syntax (compile-time) error — a final variable cannot be given a new value.
Remove `MAX = 20;` or drop final.

**Q20.** Identify and correct the error: `float f = 3.5;`
**Answer:** 3.5 is a double literal; storing it in a float loses precision (compile error).
Write `float f = 3.5f;`

**Q21.** Give the output: `System.out.println('7' + 1);` and `System.out.println((char)('7' + 1));`
**Answer:** `56` and `8`
'7' has code 55; casting 56 back gives the character '8'.

**Q22.** How many bytes do (a) a double and an int (b) two chars and a long occupy?
**Answer:** (a) 8 + 4 = 12 bytes.
(b) 2 + 2 + 8 = 12 bytes.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; a sample run follows each.*

### Section B programs (15 marks each)

**Q1.** Write a program to accept a letter and print its Unicode value, the next and previous characters, and the same letter in the other case (capital ↔ small), using type casting.
**Answer:**
```java
import java.util.*;
class CharInfo
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a letter: ");
        char ch = sc.next().charAt(0);
        int code = ch;                      // implicit conversion char -> int
        char next = (char)(ch + 1);         // explicit cast int -> char
        char prev = (char)(ch - 1);
        char other;
        if (ch >= 'A' && ch <= 'Z')
            other = (char)(ch + 32);        // capital -> small
        else
            other = (char)(ch - 32);        // small -> capital
        System.out.println("Character        : " + ch);
        System.out.println("Unicode value    : " + code);
        System.out.println("Next character   : " + next);
        System.out.println("Previous         : " + prev);
        System.out.println("Other case       : " + other);
    }
}
```
Sample run:
```
Enter a letter: g
Character        : g
Unicode value    : 103
Next character   : h
Previous         : f
Other case       : G
```

**Q2.** Write a program to accept a temperature in Celsius and print it in Fahrenheit (F = 9C/5 + 32) and Kelvin (K = C + 273.15), and the Fahrenheit value as a whole number using a cast.
**Answer:**
```java
import java.util.*;
class Temperature
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter temperature in Celsius: ");
        double c = sc.nextDouble();
        double f = 9 * c / 5 + 32;          // c is double, so no integer division
        double k = c + 273.15;
        System.out.println("Fahrenheit = " + f);
        System.out.println("Kelvin     = " + k);
        int whole = (int) f;                // explicit cast drops decimals
        System.out.println("Fahrenheit (whole degrees) = " + whole);
    }
}
```
Sample run:
```
Enter temperature in Celsius: 37
Fahrenheit = 98.6
Kelvin     = 310.15
Fahrenheit (whole degrees) = 98
```

**Q3.** Write a program to accept two integers and swap them (i) using a third variable (ii) without using a third variable, printing the values each time.
**Answer:**
```java
import java.util.*;
class Swap
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two integers: ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println("Before: a = " + a + ", b = " + b);
        int t = a;          // (1) using a third variable
        a = b;
        b = t;
        System.out.println("After swap with t: a = " + a + ", b = " + b);
        a = a + b;          // (2) without a third variable
        b = a - b;
        a = a - b;
        System.out.println("After swapping back without t: a = " + a + ", b = " + b);
    }
}
```
Sample run:
```
Enter two integers: 15 40
Before: a = 15, b = 40
After swap with t: a = 40, b = 15
After swapping back without t: a = 15, b = 40
```

**Q4.** Write a program to accept a time in seconds and print it in hours, minutes and seconds, and also as a decimal number of hours.
**Answer:**
```java
import java.util.*;
class TimeSplit
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter time in seconds: ");
        long total = sc.nextLong();
        long h = total / 3600;              // integer division
        long m = (total % 3600) / 60;       // remainder, then minutes
        long s = total % 60;
        System.out.println(total + " seconds = " + h + " h " + m + " min " + s + " s");
        double hours = total / 3600.0;      // real division
        System.out.println("In hours (decimal) = " + hours);
    }
}
```
Sample run:
```
Enter time in seconds: 7384
7384 seconds = 2 h 3 min 4 s
In hours (decimal) = 2.051111111111111
```

**Q5.** Write a program to accept the principal, rate and time and print the simple interest (SI = PRT/100), the compound amount A = P(1 + R/100)^T and the compound interest, rounded to two decimal places.
**Answer:**
```java
import java.util.*;
class Interest
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter principal, rate (%) and time (years): ");
        double p = sc.nextDouble();
        double r = sc.nextDouble();
        int t = sc.nextInt();
        double si = p * r * t / 100;
        double amount = p * Math.pow(1 + r / 100, t);
        double ci = amount - p;
        System.out.println("Simple interest   = " + si);
        System.out.println("Compound amount   = " + Math.round(amount * 100) / 100.0);
        System.out.println("Compound interest = " + Math.round(ci * 100) / 100.0);
    }
}
```
Sample run:
```
Enter principal, rate (%) and time (years): 10000 10 2
Simple interest   = 2000.0
Compound amount   = 12100.0
Compound interest = 2100.0
```

**Q6.** Write a program to accept the length and breadth of a rectangle and print its area, perimeter and diagonal (in cm and in inches, using a constant 1 inch = 2.54 cm).
**Answer:**
```java
import java.util.*;
class Rectangle
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length and breadth (cm): ");
        double l = sc.nextDouble();
        double b = sc.nextDouble();
        double area = l * b;
        double perimeter = 2 * (l + b);
        double diagonal = Math.sqrt(l * l + b * b);
        final double CM_PER_INCH = 2.54;    // a constant
        System.out.println("Area      = " + area + " sq cm");
        System.out.println("Perimeter = " + perimeter + " cm");
        System.out.println("Diagonal  = " + diagonal + " cm");
        System.out.println("Diagonal  = " + diagonal / CM_PER_INCH + " inches");
    }
}
```
Sample run:
```
Enter length and breadth (cm): 8 6
Area      = 48.0 sq cm
Perimeter = 28.0 cm
Diagonal  = 10.0 cm
Diagonal  = 3.937007874015748 inches
```

---

## 12. Competency / Application Questions

**Q1. (Choosing types)** A school app stores a student's roll number (up to 60), name, house initial (R, G, B or Y), percentage and whether fees are paid. Choose the most suitable data type for each.
**Model answer:** roll number — byte (or int); name — String; house initial — char; percentage — double; fees paid — boolean.

**Q2. (The wrong answer)** A program computes the average of 7 and 8 as `int s = 7 + 8; double avg = s / 2;` and prints 7.0. Explain and fix it.
**Model answer:** s / 2 is integer division (7) before widening. Write `double avg = s / 2.0;` or `(double) s / 2` to get 7.5.

**Q3. (Spot the principle)** Name the OOP principle: (a) a ticket machine shows only "Select" and "Pay" buttons (b) a SavingsAccount class reuses the features of an Account class (c) a print() method prints a number or a word.
**Model answer:** (a) Abstraction (b) Inheritance (c) Polymorphism.

**Q4. (Caesar shift)** How would you shift the letter 'c' three places forward in Java, and what is printed?
**Model answer:** `char s = (char)('c' + 3);` prints f — 'c' (99) + 3 = 102, cast back to a char.

**Q5. (Same code, many machines)** A Class X student writes a game in Java on Windows; a friend runs the .class file on Linux. Why does it work?
**Model answer:** The compiler produced byte code, not Windows machine code; the friend's JVM converts the byte code for Linux (platform independence).

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** Java is platform independent.
**R:** Java byte code runs on any computer that has a JVM.
**Answer:** (c)
**Explanation:** Write once, run anywhere.

**Q2.**
**A:** `Switch` is a keyword in Java.
**R:** Java is case sensitive.
**Answer:** (b)
**Explanation:** Only lower-case `switch` is a keyword; R is true.

**Q3.**
**A:** A char occupies 2 bytes in Java.
**R:** Java uses 16-bit Unicode for characters.
**Answer:** (c)
**Explanation:** 16 bits = 2 bytes.

**Q4.**
**A:** `int x = (int) 32.8;` stores 33 in x.
**R:** Explicit casting drops the decimal part.
**Answer:** (b)
**Explanation:** It stores 32; R is true.

**Q5.**
**A:** The default value of a String data member is null.
**R:** String is a non-primitive data type.
**Answer:** (c)
**Explanation:** Reference types default to null.

**Q6.**
**A:** `'Z' + 32` prints 122.
**R:** java.lang is the default package.
**Answer:** (d)
**Explanation:** Both true; unrelated.

**Q7.**
**A:** Inheritance allows code reuse.
**R:** A class can acquire the properties of another class.
**Answer:** (c)
**Explanation:** Reuse through inheritance.

**Q8.**
**A:** `float f = 3.5;` compiles without error.
**R:** 3.5 is a double literal.
**Answer:** (b)
**Explanation:** It is a compile error; write 3.5f.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The first program

> Riya types a program in BlueJ and saves it as Welcome.java. She compiles it, and a file Welcome.class appears. Her teacher copies Welcome.class to a Linux laptop and runs it.

**(i)** What kind of code is in Welcome.java?
**Answer:** Source code.

**(ii)** What is in Welcome.class?
**Answer:** Byte code.

**(iii)** Which program runs Welcome.class on the laptop?
**Answer:** The JVM (Java Virtual Machine).

**(iv)** Which feature of Java does this show?
**Answer:** Platform independence.

### Case 2 — Characters as numbers

> `char ch = 'K'; int n = ch; char nx = (char)(n + 1); char sm = (char)(ch + 32);`

**(i)** What is n?
**Answer:** 75.

**(ii)** What is nx?
**Answer:** L.

**(iii)** What is sm?
**Answer:** k.

**(iv)** Which kind of conversion is `int n = ch;`?
**Answer:** Implicit (widening) conversion.

### Case 3 — The design meeting

> A team designs a Library app. Book objects keep their price private and change it only through a method; a ReferenceBook class reuses Book; one method search() works with a title or with an author's name.

**(i)** Keeping the price private and changing it only through a method shows which principle?
**Answer:** Encapsulation.

**(ii)** ReferenceBook reusing Book shows?
**Answer:** Inheritance.

**(iii)** search() working with different arguments shows?
**Answer:** Polymorphism.

**(iv)** What is Book in Java terms?
**Answer:** A class (a blueprint for book objects).

---

## 15. Revision Notes

### Chapter at a glance
- POP vs OOP; principles: abstraction, encapsulation, inheritance, polymorphism (with examples).
- Java (Gosling, Sun, 1995); applications and applets; source code (.java) → javac → byte code (.class) → JVM → machine code; features: simple, OO, platform independent, robust, secure, multithreaded, portable.
- Objects (state + behaviour) and classes (blueprint, object factory, user-defined type).
- Character set; ASCII (7-bit) and Unicode (16-bit); 'A' 65, 'a' 97, '0' 48, space 32.
- Escape sequences: `\n`, `\t`, `\\`, `\"`, `\'`.
- Tokens: keywords, identifiers, literals, punctuators, operators; Java is case sensitive.
- Variables and constants (final).
- Primitive types and sizes: byte 1, short 2, int 4, long 8, float 4, double 8, char 2, boolean; non-primitive: String, array, class; defaults 0, false, null.
- Implicit (widening, promotion) and explicit (casting) conversion; integer division.
- Packages: java.lang (default), java.util (Scanner); import.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| `'Z' + 32` prints z | It prints 122; cast with (char) to get z. |
| Writing escape sequences with a forward slash | Use a backslash: `\n`, `\t`. |
| Calling `Switch`, `If` keywords | Keywords are lower case. |
| char is 1 byte | char is 2 bytes (Unicode). |
| `(int) 32.8` gives 33 | Casting truncates: 32. |
| `5 / 2` is 2.5 | Integer division gives 2. |
| String is a primitive type | String is a class (non-primitive). |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 1: Revision I**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** Code produced by javac:
(a) source code (b) byte code (c) machine code (d) pseudocode

**2.** A father and child picture shows:
(a) inheritance (b) abstraction (c) encapsulation (d) polymorphism

**3.** `System.out.println('Z' + 32);` prints:
(a) small z (b) capital Z (c) 122 (d) 154

**4.** Size of a char:
(a) 1 byte (b) 2 bytes (c) 4 bytes (d) 8 bytes

**5.** A valid keyword:
(a) Switch (b) If (c) static (d) BOOLEAN

**6.** Default value of a boolean data member:
(a) True (b) false (c) 0 (d) null

**7.** `int x = (int) 32.8;` gives x =
(a) 32.8 (b) 33 (c) 32 (d) 0

**8.** Keyword to use a package:
(a) import (b) extends (c) package (d) export

**9.** Statement I: Byte code is machine independent. Statement II: The JVM is a compiler that produces source code.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

**10.** Which is non-primitive?
(a) int (b) char (c) double (d) String

### Part I — Short answers (5 × 2 = 10)

**11.** Define abstraction and inheritance. [2]

**12.** Name the tokens: public, 'a', ==, { }. [2]

**13.** Give the output: `char ch = 'F'; int m = ch; m = m + 5; System.out.println(m + " " + ch);` [2]

**14.** Distinguish implicit and explicit type conversion. [2]

**15.** State the sizes of short, float, long and double. [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** (i) Explain the Java compilation process. [4]
(ii) Write a program to accept a letter and print its Unicode value and the next letter. [6]

**17.** (i) List four features of Java. [4]
(ii) Write a program to swap two numbers without a third variable. [6]

**18.** (i) Give the output: `System.out.println(1 + 2 + "3" + 4 + 5);` and `double d = 5 / 2;` [4]
(ii) Write a program to convert a time in seconds into hours, minutes and seconds. [6]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | b | c | d | c | b |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | Source code | Byte code | JVM | Platform independence |
| 2 | 75 | L | k | Implicit |
| 3 | Encapsulation | Inheritance | Polymorphism | A class |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | b | a | c | b | c | b | c | a | c | d |

**Part I, Q11–15 (2 marks each)**

**11.** Essential features shown, details hidden (1); a class acquiring another's properties (1).
**12.** Keyword, character literal, operator, separator (½ each).
**13.** `75 F` (2).
**14.** Automatic widening (1); programmer's cast (1).
**15.** 2, 4, 8, 8 bytes (½ each).

**Part II (10 marks each)**

**16.** (i) Source → javac → byte code → JVM → machine code (4). (ii) Scanner input (1), int cast (2), (char)(ch + 1) (2), output (1).

**17.** (i) Any four (4). (ii) Input (1), a = a + b; b = a − b; a = a − b (4), output (1).

**18.** (i) `3345` (2); `2.0` (2). (ii) Input (1), h = t / 3600, m = t % 3600 / 60, s = t % 60 (4), output (1).
