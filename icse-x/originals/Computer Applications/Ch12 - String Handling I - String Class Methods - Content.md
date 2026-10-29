# String Handling I — String Class Methods

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 12 |
| Title | String Handling I — String Class Methods |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 8. String handling |
| Exam weightage | **Section A** in every paper: MCQs and 2-mark outputs on **substring, indexOf, lastIndexOf, compareTo, replace, concat, equals** and **return types** — often 4 to 6 marks a paper. Section B String programs (Chapter 13) use these methods. |
| Syllabus scope | The String class and its methods: trim, toLowerCase, toUpperCase, length, charAt, indexOf, lastIndexOf, concat, equals, equalsIgnoreCase, compareTo, compareToIgnoreCase, replace, substring (two forms), startsWith, endsWith, valueOf; String arrays. |
| In short | How to use Java's String methods to measure, compare, search, change and pull out parts of text. |

> **Note on the text:** CISCE prescribes no textbook for ICSE Computer Applications; this chapter follows the ICSE 2027 syllabus in its own words. Its questions are the CISCE papers of 2017–2026 and the 2024 and 2025 specimens, answered from CISCE's marking schemes and examiners' comments where published. **Every output in this chapter was checked with Java 21.**
>
> **Exam note:** Count indexes **from 0**. `substring(b, e)` takes characters **b to e − 1**. `compareTo()` returns the **difference of the first unequal characters' codes** (or of the lengths). Learn the **return type** of every method — boolean for equals/startsWith/endsWith, int for length/indexOf/compareTo, char for charAt, String for the rest. A String is **never changed** by its methods; they return new Strings.

---

## 1. Complete Lesson

### The String class

A **String** is a sequence of characters, such as "Shillong" or "ICSE 2027". In Java a String is an **object of the class String**, which belongs to java.lang, so it needs no import.

```java
String s = "Meghalaya";               // a String literal
String t = new String("Meghalaya");   // created with new
String name = sc.nextLine();          // read with Scanner (whole line)
String word = sc.next();              // one word
```

**Strings are immutable.** A String's characters cannot be changed. Methods such as toUpperCase(), replace() and substring() **return a new String** and leave the original as it was (so ICSE 2026 Q1(xix)'s Assertion, "substring() modifies the original String", is false):

```java
String m = "Java";
m.toUpperCase();              // result thrown away
System.out.println(m);        // Java
m = m.toUpperCase();          // keep the new String
System.out.println(m);        // JAVA
```

### Index of characters

Each character has an **index** from 0 to `length() - 1`, as in an array.

![Fig. 12.1 Characters of "COMPOSITION" with their indexes, from 0 to length() − 1](figures/ca_ch12_fig01_string_indexes.png)

An index outside this range stops the program with **StringIndexOutOfBoundsException** — `"HELLO".charAt(5)` and `"HELLO".substring(2, 9)` both do.

### The String methods in the syllabus

| Method | Returns | What it does | Example | Result |
|---|---|---|---|---|
| `length()` | int | number of characters | `"Remarkable".length()` | 10 |
| `charAt(int n)` | char | character at index n | `"Aditi".charAt(1)` | 'd' |
| `indexOf(char ch)` | int | first index of ch, or −1 | `"CONCENTRATION".indexOf('T')` | 6 |
| `lastIndexOf(char ch)` | int | last index of ch, or −1 | `"MONOPOLY".lastIndexOf('O')` | 5 |
| `substring(int b)` | String | from index b to the end | `"Remarkable".substring(6)` | "able" |
| `substring(int b, int e)` | String | from index b to e − 1 | `"COMPOSITION".substring(3, 6)` | "POS" |
| `toUpperCase()` | String | all letters in capitals | `"island".toUpperCase()` | "ISLAND" |
| `toLowerCase()` | String | all letters small | `"Hello".toLowerCase()` | "hello" |
| `trim()` | String | removes spaces at both ends | `"  hi there  ".trim()` | "hi there" |
| `concat(String str)` | String | joins str at the end | `"phoenix".concat("land")` | "phoenixland" |
| `replace(char o, char n)` | String | every o replaced by n | `"DEDICATE".replace('D', 'L')` | "LELICATE" |
| `equals(String str)` | boolean | same characters, same case | `"CAT".equals("cat")` | false |
| `equalsIgnoreCase(String str)` | boolean | same characters, any case | `"CAT".equalsIgnoreCase("cat")` | true |
| `compareTo(String str)` | int | dictionary comparison | `"ANGER".compareTo("ANGEL")` | 6 |
| `compareToIgnoreCase(String str)` | int | comparison ignoring case | `"apple".compareToIgnoreCase("APPLE")` | 0 |
| `startsWith(String str)` | boolean | begins with str? | `"Meghalaya".startsWith("Meg")` | true |
| `endsWith(String str)` | boolean | ends with str? | `"GLAMOROUS".endsWith("IOUS")` | false |
| `String.valueOf(any)` | String | converts any value to a String | `String.valueOf(25) + 5` | "255" |

Points from the papers:
- Methods returning a **boolean**: equals(), equalsIgnoreCase(), startsWith(), endsWith() (ICSE 2025 Improvement Q1(i); 2019 Q3(b); 2018 Q2(e)).
- A method that returns only a **non-negative int** is length(); indexOf() can give −1 and compareTo() can be negative (ICSE 2025 Q2(vi); 2026 Q1(xvi)). A method that returns a **char** is charAt() (2025 Q2(vi)).
- **String methods with no parameter that return a String**: toUpperCase(), toLowerCase(), trim() (ICSE 2026 Q2(x)).
- substring() is **overloaded** — it has a one-parameter and a two-parameter version (ICSE 2026 Improvement Q1(iv)).
- To join two strings: **concat(String)** (ICSE 2023 Q1(xi)).

### substring in detail

- `substring(b)` — from index b to the end: `"GRACIOUS".substring(4)` is "IOUS"; `"Rajeev".substring(2)` is "jeev".
- `substring(b, e)` — from b up to **but not including** e; it has **e − b** characters: `"ACKNOWLEDGEMENT".substring(3, 6)` is "NOW" (ICSE 2026 Q1(xiv)); `"JavaProgramming".substring(4, 11)` is "Program".
- `substring(0)` is the whole String.

### indexOf and lastIndexOf

- `indexOf(ch)` gives the **first** position, `lastIndexOf(ch)` the **last**; both give **−1** when the character is absent.
- `"COMMENCEMENT".lastIndexOf('M')` is 8; `"MEDITERRIAN".indexOf('R')` is 6; `"ARTIFICIAL ".indexOf('I')` is 3; `"Today is Test".indexOf('T')` is 0 (capital T at the start).
- Java also has `indexOf(String)` and `indexOf(ch, from)` (start searching at index from): `"banana".indexOf('a', 2)` is 3. These are useful for counting a word in a sentence (Section 11).

### compareTo — dictionary order

![Fig. 12.2 compareTo() returns a difference of character codes, or of lengths](figures/ca_ch12_fig02_compareto.png)

`s1.compareTo(s2)` compares the Strings **character by character**:
1. At the **first position where they differ**, it returns **(code of s1's character) − (code of s2's character)**: `"ANGER".compareTo("ANGEL")` = 82 − 76 = **6**; `"talent".compareTo("genius")` = 116 − 103 = **13**; `"DEDICATE".compareTo("DEVOTE")` = 68 − 86 = **−18**; `"devote".compareTo("DEVOTE")` = 100 − 68 = **32**.
2. If one String is the **beginning of the other**, it returns the **difference of the lengths**: `"KING".compareTo("KINGDOM")` = 4 − 7 = **−3**.
3. If the Strings are equal, it returns **0** (ICSE 2024 specimen Q1(xvi)).

A **negative** result means s1 comes **before** s2 in dictionary order; positive means after. Capitals come before small letters ('A' is 65, 'a' is 97), so `"Apple".compareTo("apple")` is −32. The 2024 examiners noted candidates who got the sign wrong or wrote all the codes instead of the one difference.

**compareTo returns an int, not a boolean**: `boolean x = a.compareTo(b);` gives *incompatible types: int cannot be converted to boolean* (ICSE 2024 Q2(viii)). Use `int x = a.compareTo(b);` or `boolean x = a.equals(b);`.

### equals versus ==

To compare the **contents** of two Strings, use **equals()** (or equalsIgnoreCase()). `==` compares references and may give false for Strings with the same characters, so String programs should always use equals(). Characters (char), however, are compared with `==`: `x.charAt(0) == y.charAt(0)` (ICSE 2025 specimen Q2(vi)).

### Joining with + and concat

- `+` joins a String with anything: `"Earth" + s1.substring(4)` gives "Earth is Beautiful" (ICSE 2020 Q3(c)).
- Watch the order: `"abc" + 1 + 2` is "abc12", but `(1 + 2) + "abc"` is "3abc".
- A char + a char is an int, but a String + a char joins: `a[1].charAt(1) + "*" + a[2].charAt(2)` is "d*a" (ICSE 2026 Q1(xv)).

### String arrays

A String array holds several Strings: `String arr[] = {"DELHI", "CHENNAI", "MUMBAI", "LUCKNOW", "JAIPUR"};`.
- `arr.length` (no brackets) is the number of Strings; `arr[3].length()` (with brackets) is the length of one String — LUCKNOW has 7 (ICSE 2020 Q2(b) asks this difference).
- `arr[0].length() > arr[3].length()` is false (5 > 7); `arr[4].substring(0, 3)` is "JAI" (ICSE 2018 Q3(h)).
- Sorting and searching String arrays use compareTo() and equals() (Chapter 13).

### Tracing String outputs step by step

Output questions are solved by writing the indexes under the characters and working one method at a time.

**Trace 1 — substring and concat.** `String x = " talent", y = "matrix"; x.substring(3).concat(y.substring(3))`
1. x: ' '0 t1 a2 l3 e4 n5 t6, so x.substring(3) is "lent".
2. y: m0 a1 t2 r3 i4 x5, so y.substring(3) is "rix".
3. "lent".concat("rix") is **"lentrix"**.

**Trace 2 — compareTo.** `"COMPASSIONATE".compareTo("COMPANION")`
1. C O M P A match (indexes 0 to 4).
2. Index 5: 'S' (83) and 'N' (78) differ.
3. Result 83 − 78 = **5** — positive, so COMPASSIONATE comes after COMPANION.

**Trace 3 — a loop with substring.** `String s = "JAVA"; for (int i = 0; i < s.length(); i += 2) System.out.println(s.substring(i));`
1. i = 0: prints "JAVA". i becomes 2.
2. i = 2: prints "VA". i becomes 4.
3. 4 < 4 is false: the loop stops after **two** iterations.

**Trace 4 — charAt and +.** `a[1].charAt(1) + "*" + a[2].charAt(2)` with a[1] = "Aditi", a[2] = "Anant"
1. "Aditi".charAt(1) is 'd'; "Anant".charAt(2) is 'a'.
2. 'd' + "*" is the String "d*" — a char plus a String joins.
3. "d*" + 'a' is **"d*a"**. (Without the String in the middle, 'd' + 'a' would be the int 197.)

### Summary of the chapter

- **String** — an immutable object of class String; methods return new Strings.
- **Index** — 0 to length() − 1; outside it, StringIndexOutOfBoundsException.
- **Return types** — int: length, indexOf, lastIndexOf, compareTo(IgnoreCase); char: charAt; boolean: equals(IgnoreCase), startsWith, endsWith; String: the rest.
- **substring(b, e)** — b to e − 1; **indexOf/lastIndexOf** — first/last position or −1.
- **compareTo** — first difference of codes, else difference of lengths; 0 when equal.
- **equals** for String contents; **==** for chars.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Explain what a String is and why Strings are immutable.
2. State the purpose and return type of each String method in the syllabus.
3. Find characters and positions with charAt, indexOf and lastIndexOf.
4. Extract parts with substring and change Strings with replace, concat, trim and case methods.
5. Compare Strings with equals, equalsIgnoreCase and compareTo, and compute compareTo values.
6. Work with String arrays, distinguishing length from length().

---

## 3. Detailed Section Explanations

### Section 1 — Characters in numbered boxes
A String is like a char array with indexes from 0, but it cannot be changed in place.

### Section 2 — Ask, don't change
Every method answers a question (length, position, comparison) or makes a new String.

### Section 3 — The end index is not included
substring(b, e) stops just before e; it returns e − b characters.

### Section 4 — Comparing is subtracting
compareTo subtracts the first unequal codes, or the lengths if one String begins the other.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| String | A sequence of characters; an object of class String. |
| Immutable | Unable to be changed after creation. |
| Index | The position of a character, from 0. |
| Substring | A part of a String. |
| Concatenation | Joining Strings, with + or concat(). |
| Lexicographic (dictionary) order | The order given by comparing character codes. |
| compareTo() | Returns a negative, zero or positive int for dictionary order. |
| equals() | Tests whether two Strings have the same characters. |
| trim() | Removes leading and trailing spaces. |
| StringIndexOutOfBoundsException | The run-time error for an index outside the String. |
| String array | An array whose elements are Strings. |
| Overloaded method | A method with several parameter lists, e.g. substring. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| "ACKNOWLEDGEMENT".substring(3, 6) | "NOW" |
| "COMPOSITION".substring(3, 6) | "POS" |
| "Remarkable".substring(6) | "able" |
| "CONCENTRATION".indexOf('T') | 6 |
| "MONOPOLY".lastIndexOf('O') | 5 |
| "COMMENCEMENT".lastIndexOf('M') | 8 |
| "ANGER".compareTo("ANGEL") | 6 |
| "talent".compareTo("genius") | 13 |
| "KING".compareTo("KINGDOM") | −3 |
| "DEDICATE".compareTo("DEVOTE") | −18 |
| "ACHIEVEMENT".replace('E', 'A') | "ACHIAVAMANT" |
| Return type of startsWith(), endsWith(), equals() | boolean |
| Method that returns a negative value | compareTo() |
| Method that returns a char | charAt() |

### 5.2 Memory aids

- **"Start in, end out"** — substring includes the start index, excludes the end.
- **"First difference wins; no difference, lengths decide."**
- **"Strings are stone"** — methods never change them; reassign to keep a result.

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- `split(" ")` breaks a sentence into an array of words, and `contains("is")` tests for a substring; neither is in the ICSE syllabus.
- StringBuilder is a changeable (mutable) String class, useful for building long Strings quickly.
- Java Strings use Unicode, so they can hold Khasi, Garo, Hindi or Assamese text as easily as English.

---

## 6. Person Profiles

### 6.1 Herman Hollerith (1860–1929)
An American inventor whose punched-card tabulating machines, first used for the 1890 United States census, stored names and data as patterns of holes — the first large-scale machine processing of text and numbers. His company later became part of IBM.

### 6.2 Ken Thompson (born 1943)
An American computer scientist who, with Rob Pike, designed the UTF-8 encoding in 1992, the way most of the world's text — in every script — is now stored as bytes, including the Strings that Java programs read and write.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Text is data** — names, messages and codes are processed like numbers.
- **Dictionary order is code order** — compareTo turns alphabetical order into arithmetic.
- **Immutability is safety** — a String shared by many parts of a program can never be changed by one of them.

### 7.2 Real-life connections
- **Search boxes** use indexOf-like searching to find a word in a page.
- **Meghalaya:** a school's software prints "K. W. Nongrum" from "Kong Wanda Nongrum" using indexOf, charAt and substring.
- **Login forms** use equals() for passwords (case matters) and equalsIgnoreCase() for user names or e-mail addresses.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section A** (40 marks) has String-method MCQs and 2-mark outputs in every paper — substring, indexOf, compareTo, replace, concat and return types. **Section B** String programs (Chapter 13) build on these methods.

### 8.1 Graded exercises — solutions

#### Exercise 12A — Methods and return types

**Q1.** Give the return type of length(), charAt(), equals() and trim().
**Answer:** int, char, boolean and String.

**Q2.** Give the output of `"Shillong".indexOf('z')` and `"Shillong".indexOf("ll")`.
**Answer:** −1 and 3.

**Q3.** Give the output of `"Meghalaya".startsWith("meg")` and `"Meghalaya".endsWith("aya")`.
**Answer:** false (case differs) and true.

**Q4.** What does `"  hi there  ".trim()` return, and what is its length?
**Answer:** "hi there", length 8.

**Q5.** Why does `String m = "Java"; m.toUpperCase(); System.out.println(m);` print Java?
**Answer:** Strings are immutable; the uppercase String was not stored. Write `m = m.toUpperCase();`.

#### Exercise 12B — Outputs

**Q6.** Give the output of `"apple".compareTo("apples")` and `"Apple".compareTo("apple")`.
**Answer:** −1 (lengths 5 − 6) and −32 ('A' 65 − 'a' 97).

**Q7.** Give the output of `"APPLE".compareTo("BANANA")` and `"zebra".compareTo("apple")`.
**Answer:** −1 and 25.

**Q8.** Give the output of `"Hello World".substring(6).length()`.
**Answer:** 5 — "World".

**Q9.** Give the output of `"Mississippi".lastIndexOf('s')`.
**Answer:** 6.

**Q10.** Give the output of `"abc" + 1 + 2` and `(1 + 2) + "abc"`.
**Answer:** "abc12" and "3abc".
### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(xiv) (1 mark) | To extract the word NOW from the word "ACKNOWLEDGEMENT", the Java statement `"ACKNOWLEDGEMENT".substring(3, _____)` is used. Choose the correct number to fill in the blank. (a) 6 (b) 7 (c) 5 (d) 8 |
| ICSE 2026, Q1(xix) (1 mark) | Assertion (A): The substring() method modifies the original String. Reason (R): The substring() method can extract part of a String starting from a specific index. (a) A is true and R is false. (b) A is false and R is true. (c) Both A and R are true and R is the correct explanation of A. (d) Both A and R are true, but R is not the correct explanation of A. |
| ICSE 2026, Q1(xv) (1 mark) | `String a[] = {"Atasi", "Aditi", "Anant", "Amit", "Ahana"}; System.out.println(a[1].charAt(1) + "*" + a[2].charAt(2));` The output of the above statement is: (a) da (b) d * a (c) ti (d) t * i |
| ICSE 2026, Q1(xvi) (1 mark) | Which of the following String methods returns a negative value? (a) length() (b) equals() (c) compareTo() (d) charAt() |
| ICSE 2026, Q2(v) (2 marks) | Give the output of the following program segment: `String S = "GRACIOUS".substring(4); System.out.println(S); System.out.println("GLAMOROUS".endsWith(S));` |
| ICSE 2026, Q2(x) (2 marks) | Name the following: (a) the return data type of the method equals(); (b) the String method which has no parameter and returns a String. |
| ICSE 2026 Improvement, Q1(iv) (1 mark) | Which of the following String methods can be overloaded? (a) compareTo (b) equalsIgnoreCase (c) length (d) substring |
| ICSE 2026 Improvement, Q1(x) (1 mark) | The output of the statement `"MEDITERRIAN".indexOf('R')` is: (a) true (b) 7 (c) -1 (d) 6 |
| ICSE 2026 Improvement, Q2(viii) (2 marks) | What is the output of the following statements: (a) `"COMPASSIONATE".compareTo("COMPANION");` (b) `Math.ceil(14.2) + Math.floor(17.9);` |
| ICSE 2025, Q1(xix) (1 mark) | What is the output of the statement given below? `"ANGER".compareTo("ANGEL")` (a) 3 (b) –6 (c) 6 (d) 0 |
| ICSE 2025, Q2(ii) (2 marks) | Write the output of the following String method: `String x = " talent"; String y = "matrix"; System.out.print(x.substring(3).concat(y.substring(3)));` |
| ICSE 2025, Q2(vi) (2 marks) | (a) Name one String method which results in a positive integer only. (b) Name one String method which results in a character. |
| ICSE 2025, Q2(x) (2 marks) | Give the output of the following program segment and specify how many times the loop is executed. `String s = "JAVA"; for (i = 0; i < s.length(); i += 2) System.out.println(s.substring(i));` |
| ICSE 2025 Improvement, Q1(i) (1 mark) | Which of the following String methods results in boolean data type? (a) trim() (b) equals() (c) replace() (d) concat() |
| ICSE 2025 Improvement, Q1(v) (1 mark) | What is the output of the following statement: `"MONOPOLY".lastIndexOf('O');` (a) 1 (b) 3 (c) 2 (d) 5 |
| ICSE 2025 Improvement, Q1(viii) (1 mark) | What will be the output of the following statement? `String s = "JavaProgramming"; System.out.println(s.substring(4, 11).toUpperCase());` (a) Programm (b) PROGRAMM (c) PROGRAM (d) program |
| ICSE 2025 Improvement, Q1(xv) (1 mark) | `String a[] = {"Rohini", "Rajarshi", "Rajeev", "Rehan", "Rebecca"}; System.out.println(a[2].substring(2));` Which one of the following will be the output of the above statements? (a) jeev (b) Ra (c) Raj (d) je |
| ICSE 2025 Improvement, Q2(viii) (2 marks) | Give the output of the following: (a) `"ROSE".compareTo("ROJA")` (b) `"DEDICATE".replace('D', 'L')` |
| ICSE 2025 specimen, Q1(vii) (1 mark) | Which of the following returns a String? (a) length() (b) charAt(int) (c) replace(char, char) (d) indexOf(String) |
| ICSE 2025 specimen, Q2(vi) (2 marks) | Write the output of the following String methods: `String x = "Galaxy ", y = "Games ";` (a) `System.out.println(x.charAt(0) == y.charAt(0));` (b) `System.out.println(x.compareTo(y));` |
| ICSE 2024, Q1(iii) (1 mark) | The output of the statement `"CONCENTRATION".indexOf('T')` is: (a) 9 (b) 7 (c) 6 (d) (-1) |
| ICSE 2024, Q1(v) (1 mark) | The output of the statement `"talent".compareTo("genius")` is: (a) 11 (b) –11 (c) 0 (d) 13 |
| ICSE 2024, Q2(viii) (2 marks) | The following code to compare two strings is compiled, and the syntax error "incompatible types – int cannot be converted to boolean" was displayed. Identify the statement which has the error and write the correct statement. Give the output of the program segment. `void calculate() { String a = "KING", b = "KINGDOM"; boolean x = a.compareTo(b); System.out.println(x); }` |
| ICSE 2024 specimen, Q1(xi) (1 mark) | The output of `"Remarkable".substring(6)` is: (a) mark (b) emark (c) marka (d) able |
| ICSE 2024 specimen, Q1(xvi) (1 mark) | The method compareTo() returns __________ when two strings are equal and in lowercase: (a) true (b) 0 (c) 1 (d) false |
| ICSE 2024 specimen, Q2(vi) (2 marks) | Write the output of the following String methods: (a) `"ARTIFICIAL ".indexOf('I')` (b) `"DOG and PUPPY".trim().length()` |
| ICSE 2023, Q1(xi) (1 mark) | The String class method to join two strings is: (a) concat(String) (b) <string>.joint(string) (c) concat(char) (d) Concat() |
| ICSE 2023, Q1(xii) (1 mark) | The output of the function `"COMPOSITION".substring(3, 6)`: (a) POSI (b) POS (c) MPO (d) MPOS |
| ICSE 2023, Q2(vii) (2 marks) | Give the output of the following String class methods: (a) `"COMMENCEMENT".lastIndexOf('M')` (b) `"devote".compareTo("DEVOTE")` |
| ICSE 2020, Q2(b) (2 marks) | State the difference between length and length() in Java. |
| ICSE 2020, Q3(c) (2 marks) | Write the output for the following: `String s1 = "Life is Beautiful"; System.out.println("Earth" + s1.substring(4)); System.out.println(s1.endsWith("L"));` |
| ICSE 2019, Q3(b) (2 marks) | Write the return data type of the following functions: (i) startsWith() (ii) random() |
| ICSE 2019, Q3(g) (2 marks) | Write the output for the following: `String s1 = "phoenix"; String s2 = "island"; System.out.println(s1.substring(0).concat(s2.substring(2))); System.out.println(s2.toUpperCase());` |
| ICSE 2018, Q2(e) (2 marks) | Write the return data type of the following functions: (i) endsWith() (ii) log() |
| ICSE 2018, Q3(g) (2 marks) | Give the output of the following string functions: (i) `"ACHIEVEMENT".replace('E', 'A')` (ii) `"DEDICATE".compareTo("DEVOTE")` |
| ICSE 2018, Q3(h) (2 marks) | Consider the following String array and give the output: `String arr[] = {"DELHI", "CHENNAI", "MUMBAI", "LUCKNOW", "JAIPUR"}; System.out.println(arr[0].length() > arr[3].length()); System.out.print(arr[4].substring(0, 3));` |
| ICSE 2017, Q3(f) (2 marks) | Write the output for the following: `String s = "Today is Test"; System.out.println(s.indexOf('T')); System.out.println(s.substring(0, 7) + " " + "Holiday");` |

**Solutions**

**2026 Q1(xiv).** **(a) 6** — N, O, W are at indexes 3, 4, 5, and the end index is not included. *(Worked answer.)*

**2026 Q1(xix).** **(b) A is false and R is true** — Strings are immutable; substring() returns a new String. *(Worked answer.)*

**2026 Q1(xv).** **(b) d * a** — Java prints `d*a`: "Aditi".charAt(1) is 'd', "Anant".charAt(2) is 'a', and the String "*" makes + join them. *(Worked answer.)*

**2026 Q1(xvi).** **(c) compareTo()** *(Worked answer.)*

**2026 Q2(v).** Output: *(Worked answer.)*
```
IOUS
false
```
"GLAMOROUS" ends with "ROUS", not "IOUS".

**2026 Q2(x).** (a) **boolean** (b) **toUpperCase()** (or toLowerCase() or trim()). *(Worked answer.)*

**2026 Improvement Q1(iv).** **(d) substring** — it already has two forms, substring(int) and substring(int, int). *(Worked answer.)*

**2026 Improvement Q1(x).** **(d) 6** *(Worked answer.)*

**2026 Improvement Q2(viii).** (a) **5** — "COMPAS…" and "COMPAN…" first differ at index 5: 'S' (83) − 'N' (78). (b) **32.0** — 15.0 + 17.0. *(Worked answer.)*

**2025 Q1(xix).** **(c) 6** — 'R' (82) − 'L' (76).

**2025 Q2(ii).** **lentrix** — " talent".substring(3) is "lent" (index 0 is the space) and "matrix".substring(3) is "rix". The scheme also accepts "entrix", read without the leading space; the examiners noted a missing bracket in the printed statement, so marks were given for attempting it.

**2025 Q2(vi).** (a) **length()** (b) **charAt(int)** — the examiners noted that many wrote compareTo(), indexOf() or lastIndexOf(), which can give negative values.

**2025 Q2(x).** Output — the loop runs **two times** (i = 0 and i = 2):
```
JAVA
VA
```
The examiners gave marks to all candidates for this part, because a bracket was missing in the printed segment.

**2025 Improvement Q1(i).** **(b) equals()** *(Worked answer.)*

**2025 Improvement Q1(v).** **(d) 5** *(Worked answer.)*

**2025 Improvement Q1(viii).** **(c) PROGRAM** — indexes 4 to 10 give "Program". *(Worked answer.)*

**2025 Improvement Q1(xv).** **(a) jeev** *(Worked answer.)*

**2025 Improvement Q2(viii).** (a) **9** — 'S' (83) − 'J' (74). (b) **LELICATE** *(Worked answer.)*

**2025 specimen Q1(vii).** **(c) replace(char, char)**

**2025 specimen Q2(vi).** (a) **true** — both begin with 'G'. (b) **-1** — 'l' (108) − 'm' (109).

**2024 Q1(iii).** **(c) 6**

**2024 Q1(v).** **(d) 13** — 't' (116) − 'g' (103). The examiners noted candidates who got the sign wrong or wrote all the ASCII codes.

**2024 Q2(viii).** The error is in `boolean x = a.compareTo(b);` — compareTo returns an int. Correct: `int x = a.compareTo(b);`, which prints **-3** (lengths 4 − 7). The scheme also accepts `boolean x = a.equals(b);` (or equalsIgnoreCase), which prints **false**.

**2024 specimen Q1(xi).** **(d) able** *(Worked answer.)*

**2024 specimen Q1(xvi).** **(b) 0** *(Worked answer.)*

**2024 specimen Q2(vi).** (a) **3** (b) **13** *(Worked answer.)*

**2023 Q1(xi).** **(a) concat(String)**

**2023 Q1(xii).** **(b) POS**

**2023 Q2(vii).** (a) **8** (b) **32** — 'd' (100) − 'D' (68). *(Worked answer.)*

**2020 Q2(b).** **length** is a property of an **array** that gives the number of elements (`a.length`, no brackets); **length()** is a **String method** that gives the number of characters (`s.length()`). *(Worked answer.)*

**2020 Q3(c).** Output: *(Worked answer.)*
```
Earth is Beautiful
false
```
s1 ends with "l", not capital "L".

**2019 Q3(b).** (i) **boolean** (ii) **double**

**2019 Q3(g).** Output:
```
phoenixland
ISLAND
```

**2018 Q2(e).** (i) **boolean** (ii) **double**

**2018 Q3(g).** (i) **ACHIAVAMANT** (ii) **-18** — 'D' (68) − 'V' (86).

**2018 Q3(h).** Output — DELHI has 5 letters and LUCKNOW 7:
```
false
JAI
```

**2017 Q3(f).** Output: *(Worked answer.)*
```
0
Today i Holiday
```
substring(0, 7) is "Today i" — the end index 7 is not included.

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Give the output of `"abc".compareTo("abc")` and `"apple".compareToIgnoreCase("APPLE")`.
**Answer:** `0` and `0`.

**Q2.** (2 marks) What happens when `"HELLO".charAt(5)` runs?
**Answer:** It stops with StringIndexOutOfBoundsException — the indexes are 0 to 4.

**Q3.** (2 marks) Give the output of `"Mississippi".replace('s', 'z')`.
**Answer:** `Mizzizzippi`.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| MCQ / 2 marks | Output of substring, indexOf, lastIndexOf, replace, concat | 8.2, 5.1 |
| MCQ / 2 marks | compareTo of two given Strings | 8.2, Section 1 |
| MCQ / 2 marks | Return type of a String method; method that returns char or boolean | 8.2, Section 1 |
| 2 marks | length vs length(); error in a String statement | 8.2, Section 10 |

---
## 9. MCQs with Explanations

### Strings and immutability (Q1–Q10)

**Q1.** In Java, a String is
- (a) a keyword
- (b) a primitive data type
- (c) an array of int
- (d) an object of the class String

**Answer:** (d) an object of the class String
**Explanation:** String belongs to java.lang.

**Q2.** Strings in Java are immutable. This means
- (a) a String has no length
- (b) a String cannot be printed
- (c) a String cannot be compared
- (d) a String's characters cannot be changed after it is created

**Answer:** (d) a String's characters cannot be changed after it is created
**Explanation:** Methods return new Strings.

**Q3.** Assertion (A): The substring() method modifies the original String. Reason (R): substring() can extract part of a String from a given index.
- (a) A is true and R is false.
- (b) A is false and R is true.
- (c) Both A and R are true, and R explains A.
- (d) Both A and R are true, but R does not explain A.

**Answer:** (b) A is false and R is true.
**Explanation:** The original is unchanged.

**Q4.** String m = "Java"; m.toUpperCase(); System.out.println(m); prints
- (a) Java
- (b) J
- (c) an error message
- (d) avaJ

**Answer:** (a) Java
**Explanation:** The new String was not stored.

**Q5.** To keep the uppercase version of m, write
- (a) toUpperCase(m);
- (b) m.toUpperCase();
- (c) m = m.toUpperCase();
- (d) m.UpperCase();

**Answer:** (c) m = m.toUpperCase();
**Explanation:** Assign the returned String.

**Q6.** The first character of a String s is
- (a) s.charAt(0)
- (b) s.charAt(1)
- (c) s[0]
- (d) s.first()

**Answer:** (a) s.charAt(0)
**Explanation:** Indexes start at 0.

**Q7.** The last character of a String s is
- (a) s.charAt(s.length() - 1)
- (b) s.charAt(s.length())
- (c) s.charAt(-1)
- (d) s.last()

**Answer:** (a) s.charAt(s.length() - 1)
**Explanation:** The last index is length() − 1.

**Q8.** "HELLO".charAt(5) gives
- (a) O
- (b) a space
- (c) StringIndexOutOfBoundsException at run time
- (d) a compile error

**Answer:** (c) StringIndexOutOfBoundsException at run time
**Explanation:** Indexes are 0 to 4.

**Q9.** To read a full name with spaces into a String, use
- (a) sc.nextInt()
- (b) sc.next()
- (c) sc.nextLine()
- (d) sc.nextChar()

**Answer:** (c) sc.nextLine()
**Explanation:** next() stops at a space.

**Q10.** The String class belongs to
- (a) java.text
- (b) java.util
- (c) java.io
- (d) java.lang

**Answer:** (d) java.lang
**Explanation:** No import is needed.

### Return types (Q11–Q22)

**Q11.** The return type of length() is
- (a) boolean
- (b) String
- (c) char
- (d) int

**Answer:** (d) int
**Explanation:** A count of characters.

**Q12.** The return type of charAt(int) is
- (a) int
- (b) String
- (c) char
- (d) boolean

**Answer:** (c) char
**Explanation:** One character.

**Q13.** The return type of equals() is
- (a) char
- (b) int
- (c) String
- (d) boolean

**Answer:** (d) boolean
**Explanation:** true or false.

**Q14.** Which String method results in the boolean data type?
- (a) trim()
- (b) equals()
- (c) replace()
- (d) concat()

**Answer:** (b) equals()
**Explanation:** The others return Strings.

**Q15.** Which of the following returns a String?
- (a) length()
- (b) charAt(int)
- (c) replace(char, char)
- (d) indexOf(String)

**Answer:** (c) replace(char, char)
**Explanation:** It returns the new String.

**Q16.** Which String method can return a negative value?
- (a) length()
- (b) equals()
- (c) compareTo()
- (d) charAt()

**Answer:** (c) compareTo()
**Explanation:** When the first String comes first.

**Q17.** The return types of startsWith() and Math.random() are
- (a) boolean and double
- (b) int and double
- (c) boolean and int
- (d) String and double

**Answer:** (a) boolean and double
**Explanation:** ICSE 2019 Q3(b).

**Q18.** The return types of endsWith() and Math.log() are
- (a) int and double
- (b) String and int
- (c) boolean and double
- (d) boolean and int

**Answer:** (c) boolean and double
**Explanation:** ICSE 2018 Q2(e).

**Q19.** A String method with no parameter that returns a String is
- (a) charAt()
- (b) length()
- (c) toUpperCase()
- (d) equals()

**Answer:** (c) toUpperCase()
**Explanation:** toLowerCase() and trim() also qualify.

**Q20.** Which String method is overloaded?
- (a) compareTo
- (b) equalsIgnoreCase
- (c) length
- (d) substring

**Answer:** (d) substring
**Explanation:** substring(int) and substring(int, int).

**Q21.** The return type of indexOf(char) is
- (a) char
- (b) int
- (c) boolean
- (d) String

**Answer:** (b) int
**Explanation:** A position, or −1.

**Q22.** The return type of compareToIgnoreCase() is
- (a) int
- (b) boolean
- (c) String
- (d) char

**Answer:** (a) int
**Explanation:** Like compareTo.

### length, charAt, indexOf and lastIndexOf (Q23–Q38)

**Q23.** "Remarkable".length() is
- (a) 9
- (b) 10
- (c) 11
- (d) 8

**Answer:** (b) 10
**Explanation:** Ten characters.

**Q24.** "DOG and PUPPY".trim().length() is
- (a) 9
- (b) 11
- (c) 12
- (d) 13

**Answer:** (d) 13
**Explanation:** Spaces inside count.

**Q25.** "CONCENTRATION".indexOf('T') is
- (a) 9
- (b) 7
- (c) 6
- (d) -1

**Answer:** (c) 6
**Explanation:** C0 O1 N2 C3 E4 N5 T6.

**Q26.** "MEDITERRIAN".indexOf('R') is
- (a) true
- (b) 7
- (c) -1
- (d) 6

**Answer:** (d) 6
**Explanation:** The first R.

**Q27.** "MONOPOLY".lastIndexOf('O') is
- (a) 1
- (b) 3
- (c) 2
- (d) 5

**Answer:** (d) 5
**Explanation:** The last O.

**Q28.** "COMMENCEMENT".lastIndexOf('M') is
- (a) 11
- (b) 2
- (c) 3
- (d) 8

**Answer:** (d) 8
**Explanation:** The M before ENT.

**Q29.** "ARTIFICIAL ".indexOf('I') is
- (a) 7
- (b) 5
- (c) 3
- (d) 4

**Answer:** (c) 3
**Explanation:** A0 R1 T2 I3.

**Q30.** "Today is Test".indexOf('T') is
- (a) 0
- (b) 9
- (c) 12
- (d) -1

**Answer:** (a) 0
**Explanation:** The first character is T.

**Q31.** "Shillong".indexOf('z') is
- (a) -1
- (b) 0
- (c) 8
- (d) an error

**Answer:** (a) -1
**Explanation:** Not found.

**Q32.** "Shillong".indexOf("ll") is
- (a) -1
- (b) 2
- (c) 4
- (d) 3

**Answer:** (d) 3
**Explanation:** The first l of "ll".

**Q33.** "banana".indexOf('a', 2) is
- (a) 1
- (b) 3
- (c) 5
- (d) 2

**Answer:** (b) 3
**Explanation:** The search starts at index 2.

**Q34.** "Mississippi".lastIndexOf('s') is
- (a) 3
- (b) 2
- (c) 5
- (d) 6

**Answer:** (d) 6
**Explanation:** M i s s i s s: the fourth s.

**Q35.** "Aditi".charAt(1) is
- (a) d
- (b) A
- (c) i
- (d) t

**Answer:** (a) d
**Explanation:** Index 1.

**Q36.** With a[1] = "Aditi" and a[2] = "Anant", a[1].charAt(1) + "*" + a[2].charAt(2) is
- (a) da
- (b) `d*a`
- (c) ti
- (d) `t*i`

**Answer:** (b) `d*a`
**Explanation:** 'd', then "*", then 'a'.

**Q37.** "Hello".charAt(4) is
- (a) o
- (b) l
- (c) H
- (d) an error

**Answer:** (a) o
**Explanation:** The last character.

**Q38.** A method that returns only a non-negative integer is
- (a) indexOf()
- (b) compareTo()
- (c) length()
- (d) lastIndexOf()

**Answer:** (c) length()
**Explanation:** The others can give negative values.

### substring, case, trim, concat and replace (Q39–Q54)

**Q39.** To extract "NOW" from "ACKNOWLEDGEMENT", the statement is "ACKNOWLEDGEMENT".substring(3, ___):
- (a) 6
- (b) 7
- (c) 5
- (d) 8

**Answer:** (a) 6
**Explanation:** Indexes 3, 4, 5.

**Q40.** "COMPOSITION".substring(3, 6) is
- (a) POSI
- (b) POS
- (c) MPO
- (d) MPOS

**Answer:** (b) POS
**Explanation:** Indexes 3 to 5.

**Q41.** "Remarkable".substring(6) is
- (a) mark
- (b) emark
- (c) marka
- (d) able

**Answer:** (d) able
**Explanation:** From index 6 to the end.

**Q42.** "GRACIOUS".substring(4) is
- (a) GRAC
- (b) CIOUS
- (c) OUS
- (d) IOUS

**Answer:** (d) IOUS
**Explanation:** G0 R1 A2 C3 I4.

**Q43.** String s = "JavaProgramming"; s.substring(4, 11).toUpperCase() gives
- (a) PROGRAMM
- (b) PROGRAM
- (c) ROGRAM
- (d) JAVAPRO

**Answer:** (b) PROGRAM
**Explanation:** Indexes 4 to 10.

**Q44.** For String a[] = {"Rohini", "Rajarshi", "Rajeev", "Rehan", "Rebecca"};, a[2].substring(2) is
- (a) Raj
- (b) Ra
- (c) jeev
- (d) je

**Answer:** (c) jeev
**Explanation:** "Rajeev" from index 2.

**Q45.** String x = " talent", y = "matrix"; x.substring(3).concat(y.substring(3)) is
- (a) talentmatrix
- (b) alentrix
- (c) lentrix
- (d) lentmat

**Answer:** (c) lentrix
**Explanation:** Index 0 of x is a space.

**Q46.** "phoenix".substring(0).concat("island".substring(2)) is
- (a) phoenixisland
- (b) phoenixland
- (c) hoenixland
- (d) phoenixsland

**Answer:** (b) phoenixland
**Explanation:** substring(0) is the whole String.

**Q47.** The String method to join two Strings is
- (a) concat(char)
- (b) join(char)
- (c) concat(String)
- (d) add()

**Answer:** (c) concat(String)
**Explanation:** ICSE 2023 Q1(xi).

**Q48.** "ACHIEVEMENT".replace('E', 'A') is
- (a) ACHIAVAMANT
- (b) ACHIEVEMENT
- (c) ACHIAVEMENT
- (d) AAHIEVEMENT

**Answer:** (a) ACHIAVAMANT
**Explanation:** Every E is replaced.

**Q49.** "DEDICATE".replace('D', 'L') is
- (a) LELICALE
- (b) LEDICATE
- (c) DEDICATE
- (d) LELICATE

**Answer:** (d) LELICATE
**Explanation:** Both D's become L.

**Q50.** "  hi there  ".trim() is
- (a) "hi there"
- (b) "hithere"
- (c) "  hi there"
- (d) "hi"

**Answer:** (a) "hi there"
**Explanation:** Only outer spaces go.

**Q51.** "island".toUpperCase() gives
- (a) ISLAND
- (b) ISLA
- (c) LAND
- (d) 6

**Answer:** (a) ISLAND
**Explanation:** All letters in capitals.

**Q52.** "Hello World".substring(6).length() is
- (a) 11
- (b) 6
- (c) 5
- (d) 4

**Answer:** (c) 5
**Explanation:** "World".

**Q53.** "Mississippi".replace('s', 'z') is
- (a) Mizsissippi
- (b) Mizzizzippi
- (c) Mississippz
- (d) Mzzzzzzzzzz

**Answer:** (b) Mizzizzippi
**Explanation:** Every s is replaced.

**Q54.** String S = "GRACIOUS".substring(4); "GLAMOROUS".endsWith(S) is
- (a) false
- (b) true
- (c) IOUS
- (d) ROUS

**Answer:** (a) false
**Explanation:** GLAMOROUS ends with ROUS.

### equals, compareTo, startsWith and endsWith (Q55–Q70)

**Q55.** "ANGER".compareTo("ANGEL") is
- (a) 3
- (b) -6
- (c) 6
- (d) 0

**Answer:** (c) 6
**Explanation:** 'R' (82) − 'L' (76).

**Q56.** "talent".compareTo("genius") is
- (a) 11
- (b) -11
- (c) 0
- (d) 13

**Answer:** (d) 13
**Explanation:** 't' (116) − 'g' (103).

**Q57.** "KING".compareTo("KINGDOM") is
- (a) -3
- (b) 3
- (c) 0
- (d) -68

**Answer:** (a) -3
**Explanation:** Lengths 4 − 7.

**Q58.** "DEDICATE".compareTo("DEVOTE") is
- (a) 2
- (b) 18
- (c) -18
- (d) -2

**Answer:** (c) -18
**Explanation:** 'D' (68) − 'V' (86).

**Q59.** "devote".compareTo("DEVOTE") is
- (a) 1
- (b) -32
- (c) 0
- (d) 32

**Answer:** (d) 32
**Explanation:** 'd' (100) − 'D' (68).

**Q60.** "ROSE".compareTo("ROJA") is
- (a) 9
- (b) -9
- (c) 1
- (d) 18

**Answer:** (a) 9
**Explanation:** 'S' (83) − 'J' (74).

**Q61.** "COMPASSIONATE".compareTo("COMPANION") is
- (a) 4
- (b) 5
- (c) -5
- (d) 13

**Answer:** (b) 5
**Explanation:** 'S' (83) − 'N' (78).

**Q62.** String x = "Galaxy ", y = "Games "; x.compareTo(y) is
- (a) -1
- (b) 1
- (c) 0
- (d) -11

**Answer:** (a) -1
**Explanation:** 'l' (108) − 'm' (109).

**Q63.** compareTo() returns ___ when two Strings are equal:
- (a) true
- (b) 0
- (c) 1
- (d) false

**Answer:** (b) 0
**Explanation:** No difference.

**Q64.** "apple".compareTo("apples") is
- (a) 1
- (b) -1
- (c) 0
- (d) -115

**Answer:** (b) -1
**Explanation:** Lengths 5 − 6.

**Q65.** boolean x = a.compareTo(b); gives the compile error
- (a) missing return statement
- (b) incompatible types: int cannot be converted to boolean
- (c) cannot find symbol
- (d) unreachable statement

**Answer:** (b) incompatible types: int cannot be converted to boolean
**Explanation:** compareTo returns int.

**Q66.** "CAT".equals("cat") and "CAT".equalsIgnoreCase("cat") are
- (a) true and false
- (b) true and true
- (c) false and true
- (d) false and false

**Answer:** (c) false and true
**Explanation:** equals is case sensitive.

**Q67.** "Meghalaya".startsWith("meg") is
- (a) true
- (b) false
- (c) 0
- (d) an error

**Answer:** (b) false
**Explanation:** Case matters.

**Q68.** String s1 = "Life is Beautiful"; s1.endsWith("L") is
- (a) true
- (b) false
- (c) l
- (d) 16

**Answer:** (b) false
**Explanation:** It ends with small l.

**Q69.** To compare the contents of two Strings, use
- (a) ==
- (b) equals()
- (c) =
- (d) compareTo() == true

**Answer:** (b) equals()
**Explanation:** == compares references.

**Q70.** String x = "Galaxy ", y = "Games "; x.charAt(0) == y.charAt(0) is
- (a) G
- (b) false
- (c) true
- (d) an error

**Answer:** (c) true
**Explanation:** chars are compared with ==.

### String arrays and joining (Q71–Q76)

**Q71.** The difference between length and length() is that
- (a) length: array size; length(): String size
- (b) both give an array's size
- (c) length() is for arrays only
- (d) there is no difference

**Answer:** (a) length: array size; length(): String size
**Explanation:** ICSE 2020 Q2(b).

**Q72.** With arr[0] = "DELHI" and arr[3] = "LUCKNOW", arr[0].length() > arr[3].length() is
- (a) false
- (b) true
- (c) 5
- (d) an error

**Answer:** (a) false
**Explanation:** 5 > 7 is false.

**Q73.** With arr[4] = "JAIPUR", arr[4].substring(0, 3) is
- (a) JAIP
- (b) JAI
- (c) PUR
- (d) LUC

**Answer:** (b) JAI
**Explanation:** Indexes 0 to 2.

**Q74.** String s = "Today is Test"; s.substring(0, 7) + " " + "Holiday" is
- (a) Today is Holiday
- (b) Today i Holiday
- (c) Today Holiday
- (d) Today is THoliday

**Answer:** (b) Today i Holiday
**Explanation:** Index 7 is not included.

**Q75.** "abc" + 1 + 2 is
- (a) an error
- (b) abc3
- (c) 3abc
- (d) abc12

**Answer:** (d) abc12
**Explanation:** After a String, + joins.

**Q76.** For s = "JAVA", the loop for (i = 0; i < s.length(); i += 2) printing s.substring(i) runs
- (a) 2 times: JA, VA
- (b) 4 times
- (c) 1 time: JAVA
- (d) 2 times: JAVA, VA

**Answer:** (d) 2 times: JAVA, VA
**Explanation:** i = 0 and i = 2.
## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** What is meant by "Strings are immutable"? Give an example.
**Answer:** A String's characters cannot be changed; its methods return new Strings.
After `String m = "Java"; m.toUpperCase();`, m is still "Java".

**Q2.** Distinguish between equals() and equalsIgnoreCase().
**Answer:** equals() is true only if the characters and their case match: "CAT".equals("cat") is false.
equalsIgnoreCase() ignores case: "CAT".equalsIgnoreCase("cat") is true.

**Q3.** Distinguish between indexOf() and lastIndexOf().
**Answer:** indexOf(ch) gives the first position of ch; lastIndexOf(ch) gives the last.
Both give −1 if ch is not present: "MONOPOLY".indexOf('O') is 1, lastIndexOf('O') is 5.

**Q4.** Distinguish between substring(int) and substring(int, int).
**Answer:** substring(b) returns the characters from index b to the end.
substring(b, e) returns the characters from b to e − 1.

**Q5.** How does compareTo() work?
**Answer:** It compares character by character and returns the difference of the codes at the first unequal position.
If one String is the start of the other it returns the difference of the lengths; equal Strings give 0.

**Q6.** State the difference between length and length().
**Answer:** length is a property of an array giving the number of elements: a.length.
length() is a String method giving the number of characters: s.length().

**Q7.** Name two String methods that return boolean and two that return int.
**Answer:** boolean: equals(), startsWith() (also equalsIgnoreCase(), endsWith()).
int: length(), indexOf() (also lastIndexOf(), compareTo()).

**Q8.** What does trim() do? Give an example.
**Answer:** It removes the spaces at the beginning and end of a String.
`"  hi there  ".trim()` is "hi there".

**Q9.** Why should Strings be compared with equals() and not ==?
**Answer:** equals() compares the characters; == compares references.
Two Strings with the same characters may be different objects, so == can give false.

**Q10.** Distinguish between replace() and concat().
**Answer:** replace(o, n) returns a String with every character o replaced by n.
concat(str) returns a String with str joined at the end.

**Q11.** What is StringIndexOutOfBoundsException? Give an example.
**Answer:** The run-time error for an index outside 0 to length() − 1.
`"HELLO".charAt(5)` or `"HELLO".substring(2, 9)`.

**Q12.** Name the String methods that (i) give the number of characters, (ii) give the character at a position, (iii) check the end of a String.
**Answer:** (i) length() (ii) charAt(int) (iii) endsWith(String)

### Output and error questions (2 marks each)

**Q13.** `String S = "GRACIOUS".substring(4); System.out.println(S); System.out.println("GLAMOROUS".endsWith(S));`
**Answer:** `IOUS` then `false` — GLAMOROUS ends with ROUS.

**Q14.** `System.out.println("COMPASSIONATE".compareTo("COMPANION")); System.out.println(Math.ceil(14.2) + Math.floor(17.9));`
**Answer:** `5` then `32.0`
'S' − 'N' = 5; 15.0 + 17.0.

**Q15.** `String x = " talent", y = "matrix"; System.out.print(x.substring(3).concat(y.substring(3)));`
**Answer:** `lentrix` — index 0 of x is a space.

**Q16.** `String s = "JAVA"; for (int i = 0; i < s.length(); i += 2) System.out.println(s.substring(i));` Give the output and the number of iterations.
**Answer:** `JAVA` then `VA` — two iterations.

**Q17.** `String arr[] = {"DELHI", "CHENNAI", "MUMBAI", "LUCKNOW", "JAIPUR"}; System.out.println(arr[0].length() > arr[3].length()); System.out.print(arr[4].substring(0, 3));`
**Answer:** `false` then `JAI` — 5 > 7 is false.

**Q18.** `String s = "Today is Test"; System.out.println(s.indexOf('T')); System.out.println(s.substring(0, 7) + " " + "Holiday");`
**Answer:** `0` then `Today i Holiday` — index 7 is not included.

**Q19.** Give the output of `"ACHIEVEMENT".replace('E', 'A')` and `"DEDICATE".compareTo("DEVOTE")`.
**Answer:** `ACHIAVAMANT` and `-18`.

**Q20.** Find the error and correct it: `String a = "KING", b = "KINGDOM"; boolean x = a.compareTo(b); System.out.println(x);`
**Answer:** compareTo returns an int: write `int x = a.compareTo(b);`, which prints -3.
Or `boolean x = a.equals(b);`, which prints false.

**Q21.** What happens when `String s = "HELLO"; System.out.println(s.substring(2, 9));` runs?
**Answer:** StringIndexOutOfBoundsException: Range [2, 9) out of bounds for length 5.
The end index may be at most 5.

**Q22.** `String m = "Java"; m.toUpperCase(); System.out.println(m); m = m.toUpperCase(); System.out.println(m);`
**Answer:** `Java` then `JAVA` — only the reassigned result is kept.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; sample runs follow each.*

### Section B programs (15 marks each)

**Q1.** Write a program to input a sentence and print its length as typed and after trim(), the sentence in uppercase and lowercase, its first and last characters, the index of the first space, and its first and last words, using String methods only.
**Answer:**
```java
import java.util.*;
class StringTour
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine();
        String t = s.trim();
        System.out.println("Length (as typed)  : " + s.length());
        System.out.println("Length (trimmed)   : " + t.length());
        System.out.println("Uppercase          : " + t.toUpperCase());
        System.out.println("Lowercase          : " + t.toLowerCase());
        System.out.println("First and last     : " + t.charAt(0) + " " + t.charAt(t.length() - 1));
        System.out.println("First space at     : " + t.indexOf(' '));
        System.out.println("First word         : " + t.substring(0, t.indexOf(' ')));
        System.out.println("Last word          : " + t.substring(t.lastIndexOf(' ') + 1));
    }
}
```
Sample run (the sentence is typed with two spaces at each end):
```
Enter a sentence:   Shillong is the Scotland of the East
Length (as typed)  : 40
Length (trimmed)   : 36
Uppercase          : SHILLONG IS THE SCOTLAND OF THE EAST
Lowercase          : shillong is the scotland of the east
First and last     : S t
First space at     : 8
First word         : Shillong
Last word          : East
```

**Q2.** Write a program to input two names and print the results of equals(), equalsIgnoreCase() and compareTo(), and which name comes first in dictionary order.
**Answer:**
```java
import java.util.*;
class CompareNames
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("First name : ");
        String a = sc.nextLine();
        System.out.print("Second name: ");
        String b = sc.nextLine();
        System.out.println("equals           : " + a.equals(b));
        System.out.println("equalsIgnoreCase : " + a.equalsIgnoreCase(b));
        int c = a.compareTo(b);
        System.out.println("compareTo        : " + c);
        if (c < 0)
            System.out.println(a + " comes first in dictionary order");
        else if (c > 0)
            System.out.println(b + " comes first in dictionary order");
        else
            System.out.println("The names are the same");
    }
}
```
Sample runs:
```
First name : Banteilang
Second name: banteilang
equals           : false
equalsIgnoreCase : true
compareTo        : -32
Banteilang comes first in dictionary order
```
```
First name : Kyntiew
Second name: Kyrmen
equals           : false
equalsIgnoreCase : false
compareTo        : -4
Kyntiew comes first in dictionary order
```

**Q3.** Write a program to input a sentence and a word, and count how many times the word occurs in the sentence using indexOf(String, int).
**Answer:**
```java
import java.util.*;
class CountWord
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine().toLowerCase();
        System.out.print("Enter a word: ");
        String w = sc.nextLine().toLowerCase();
        int count = 0;
        int pos = s.indexOf(w);
        while (pos != -1)
        {
            count++;
            pos = s.indexOf(w, pos + 1);
        }
        System.out.println("\"" + w + "\" occurs " + count + " time(s)");
    }
}
```
Sample run — "the" is also found inside "other", so indexOf counts 4:
```
Enter a sentence: The cat and the dog met the other cat
Enter a word: the
"the" occurs 4 time(s)
```
To count whole words only, the words must be separated first (Chapter 13).

**Q4.** Write a program to input a full name of two or three words and print it with initials, e.g. "Kong Wanda Nongrum" → "K. W. Nongrum".
**Answer:**
```java
import java.util.*;
class Initials
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a full name: ");
        String n = sc.nextLine().trim();
        int first = n.indexOf(' ');
        int last = n.lastIndexOf(' ');
        if (first == -1)
        {
            System.out.println(n);
            return;
        }
        String out = n.charAt(0) + ". ";
        if (last != first)
            out = out + n.charAt(first + 1) + ". ";
        out = out + n.substring(last + 1);
        System.out.println(out);
    }
}
```
Sample runs:
```
Enter a full name: Kong Wanda Nongrum
K. W. Nongrum
```
```
Enter a full name: Rida Kharshiing
R. Kharshiing
```

**Q5.** Write a program to input a word, print its reverse and check whether it is a palindrome (ignoring case).
**Answer:**
```java
import java.util.*;
class Palindrome
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String w = sc.next();
        String rev = "";
        for (int i = w.length() - 1; i >= 0; i--)
            rev = rev + w.charAt(i);
        System.out.println("Reverse: " + rev);
        if (rev.equalsIgnoreCase(w))
            System.out.println(w + " is a palindrome");
        else
            System.out.println(w + " is not a palindrome");
    }
}
```
Sample runs:
```
Enter a word: Malayalam
Reverse: malayalaM
Malayalam is a palindrome
```
```
Enter a word: Shillong
Reverse: gnollihS
Shillong is not a palindrome
```

**Q6.** Write a program to input a file name and print its name and extension (the part after the last dot), then say whether it is a Java source file (endsWith(".java")), a document (docx or pdf) or another kind of file.
**Answer:**
```java
import java.util.*;
class FileName
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a file name: ");
        String f = sc.nextLine();
        int dot = f.lastIndexOf('.');
        if (dot == -1)
        {
            System.out.println("No extension");
            return;
        }
        String name = f.substring(0, dot);
        String ext = f.substring(dot + 1);
        System.out.println("Name      : " + name);
        System.out.println("Extension : " + ext);
        if (f.endsWith(".java"))
            System.out.println("A Java source file");
        else if (ext.equalsIgnoreCase("docx") || ext.equalsIgnoreCase("pdf"))
            System.out.println("A document");
        else
            System.out.println("Another kind of file");
    }
}
```
Sample runs:
```
Enter a file name: BinarySearch.java
Name      : BinarySearch
Extension : java
A Java source file
```
```
Enter a file name: Report.2026.pdf
Name      : Report.2026
Extension : pdf
A document
```

---

## 12. Competency / Application Questions

**Q1. (Pick the method)** A form must check that a PIN code typed as text has exactly 6 characters and begins with "79". Which methods are used?
**Model answer:** `length() == 6` and `startsWith("79")`.

**Q2. (Case-insensitive login)** Why should a website compare user names with equalsIgnoreCase() but passwords with equals()?
**Model answer:** User names are usually not case sensitive, but passwords are — "Abc" and "abc" must be different passwords.

**Q3. (Extract)** From the e-mail "kong@school.edu.in", which statement gives the user name "kong"?
**Model answer:** `e.substring(0, e.indexOf('@'))`.

**Q4. (Sort two names)** How can a program decide which of two names comes first in a register?
**Model answer:** `if (a.compareTo(b) < 0)` a comes first; otherwise b (or they are equal if 0).

**Q5. (Spot the slip)** `String s = "exam"; s.replace('e', 'E'); System.out.println(s);` prints "exam". Why, and how is it fixed?
**Model answer:** replace() returns a new String that was not stored; write `s = s.replace('e', 'E');`.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** `"COMPOSITION".substring(3, 6)` is "POS".
**R:** The character at the end index is not included.
**Answer:** (c)
**Explanation:** Indexes 3, 4, 5.

**Q2.**
**A:** `"ANGER".compareTo("ANGEL")` is −6.
**R:** compareTo subtracts the codes of the first unequal characters.
**Answer:** (b)
**Explanation:** 82 − 76 = +6.

**Q3.**
**A:** `"CAT".equals("cat")` is false.
**R:** equals() is case sensitive.
**Answer:** (c)
**Explanation:** Use equalsIgnoreCase() to ignore case.

**Q4.**
**A:** `boolean x = "A".compareTo("B");` gives a compile error.
**R:** compareTo returns an int.
**Answer:** (c)
**Explanation:** An int cannot be stored in a boolean.

**Q5.**
**A:** `"KING".compareTo("KINGDOM")` is −3.
**R:** String is a class in java.lang.
**Answer:** (d)
**Explanation:** Both true; the value comes from the lengths.

**Q6.**
**A:** toUpperCase() changes the original String.
**R:** Strings are immutable.
**Answer:** (b)
**Explanation:** It returns a new String.

**Q7.**
**A:** `"Shillong".indexOf('z')` is −1.
**R:** indexOf returns −1 when the character is absent.
**Answer:** (c)
**Explanation:** z does not occur.

**Q8.**
**A:** charAt() returns a char.
**R:** length() can return a negative value.
**Answer:** (a)
**Explanation:** length() is never negative.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The word puzzle

> A puzzle app hides words inside "ACKNOWLEDGEMENT".

**(i)** Which call gives "NOW"?
**Answer:** `substring(3, 6)`.

**(ii)** What is the length of "ACKNOWLEDGEMENT"?
**Answer:** 15.

**(iii)** What is `indexOf('E')`?
**Answer:** 7.

**(iv)** What is `lastIndexOf('E')`?
**Answer:** 12.

### Case 2 — The dictionary order

> A register lists names in dictionary order using compareTo().

**(i)** What is `"ANGER".compareTo("ANGEL")`?
**Answer:** 6.

**(ii)** Which comes first, ANGEL or ANGER?
**Answer:** ANGEL.

**(iii)** What is `"KING".compareTo("KINGDOM")`?
**Answer:** -3.

**(iv)** What does compareTo return for equal Strings?
**Answer:** 0.

### Case 3 — The file name

> A program splits "Report.2026.pdf" at its last dot.

**(i)** What does `lastIndexOf('.')` give?
**Answer:** 11.

**(ii)** What is the extension?
**Answer:** pdf.

**(iii)** Which method checks for ".java"?
**Answer:** endsWith().

**(iv)** What is the return type of that method?
**Answer:** boolean.

---

## 15. Revision Notes

### Chapter at a glance
- String: immutable object of class String (java.lang); index 0 to length() − 1.
- int: length, indexOf, lastIndexOf, compareTo, compareToIgnoreCase. char: charAt. boolean: equals, equalsIgnoreCase, startsWith, endsWith. String: trim, toUpperCase, toLowerCase, concat, replace, substring, valueOf.
- substring(b) to the end; substring(b, e) to e − 1.
- compareTo: first unequal codes subtracted; else lengths subtracted; 0 if equal.
- equals for String contents; == for chars.
- length (arrays) vs length() (Strings).

### Common mistakes

| Mistake | Correct idea |
|---|---|
| Counting indexes from 1 | They start at 0. |
| Including the end index in substring(b, e) | It stops at e − 1. |
| `boolean x = a.compareTo(b);` | `int x = a.compareTo(b);` |
| `s.toUpperCase();` expecting s to change | `s = s.toUpperCase();` |
| Comparing Strings with == | Use equals(). |
| `a.length()` for arrays, `s.length` for Strings | Arrays: a.length; Strings: s.length(). |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 12: String Handling I**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** `"ACKNOWLEDGEMENT".substring(3, ___)` gives "NOW":
(a) 7 (b) 6 (c) 5 (d) 8

**2.** `"ANGER".compareTo("ANGEL")` is:
(a) 3 (b) -6 (c) 6 (d) 0

**3.** The String method that returns a negative value:
(a) length() (b) equals() (c) charAt() (d) compareTo()

**4.** `"CONCENTRATION".indexOf('T')` is:
(a) 6 (b) 7 (c) 9 (d) -1

**5.** Returns boolean:
(a) trim() (b) replace() (c) equals() (d) concat()

**6.** `"Remarkable".substring(6)`:
(a) mark (b) able (c) emark (d) marka

**7.** `"MONOPOLY".lastIndexOf('O')`:
(a) 1 (b) 3 (c) 5 (d) 2

**8.** `"talent".compareTo("genius")`:
(a) 13 (b) -11 (c) 11 (d) 0

**9.** The String method to join two Strings:
(a) join(char) (b) concat(char) (c) add() (d) concat(String)

**10.** Statement I: Strings are immutable. Statement II: compareTo returns boolean.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

### Part I — Short answers (5 × 2 = 10)

**11.** State the difference between length and length(). [2]

**12.** Give the output: `String S = "GRACIOUS".substring(4); System.out.println(S); System.out.println("GLAMOROUS".endsWith(S));` [2]

**13.** Give the output: (a) `"COMMENCEMENT".lastIndexOf('M')` (b) `"devote".compareTo("DEVOTE")` [2]

**14.** Find the error and correct it: `boolean x = a.compareTo(b);` [2]

**15.** Give the output: `"ACHIEVEMENT".replace('E', 'A')` and `"DEDICATE".compareTo("DEVOTE")`. [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Input a word; print its reverse and whether it is a palindrome. [10]

**17.** Input a full name of two or three words and print it with initials. [10]

**18.** Input two names and print equals(), equalsIgnoreCase(), compareTo() and which comes first. [10]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | c | d | b | c | a |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | substring(3, 6) | 15 | 7 | 12 |
| 2 | 6 | ANGEL | -3 | 0 |
| 3 | 11 | pdf | endsWith() | boolean |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | b | c | d | a | c | b | c | a | d | c |

**Part I, Q11–15 (2 marks each)**

**11.** length: array size (1); length(): characters of a String (1).
**12.** IOUS (1); false (1).
**13.** 8 (1); 32 (1).
**14.** compareTo returns int (1); `int x = a.compareTo(b);` (1).
**15.** ACHIAVAMANT (1); -18 (1).

**Part II (10 marks each)**

**16.–18.** Input with Scanner (2), correct String methods (4), logic (2), output (2).
