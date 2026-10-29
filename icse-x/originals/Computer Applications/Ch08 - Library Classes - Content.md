# Library Classes

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 8 |
| Title | Library Classes |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 5. Library classes |
| Exam weightage | **Section A** in every paper: MCQs and 2-mark outputs on **Character methods**, **parseInt / parseDouble / valueOf**, **wrapper classes**, **boxing and unboxing** and **java.lang**. **Section B** programs use Character methods to classify characters. |
| Syllabus scope | Wrapper classes and their methods for numeric and character types; autoboxing and unboxing; class as a composite type; primitive versus composite (class) types; classes as user-defined types. |
| In short | How Java's wrapper classes turn basic values into objects, with autoboxing, unboxing and handy methods for numbers and characters. |

> **Note on the text:** CISCE prescribes no textbook for ICSE Computer Applications; this chapter follows the ICSE 2027 syllabus in its own words. Its questions are the CISCE papers of 2017–2026 and the 2024 and 2025 specimens, answered from CISCE's marking schemes and examiners' comments where published. **Every program and output was checked with Java 21.**
>
> **Exam note:** Write library methods with **exact spelling and case** — `Integer.parseInt`, `Double.parseDouble`, `Character.isLetterOrDigit` — since options such as `Integer.parseint` or `Double.Parsedouble` are wrong. Note the **return type**: `is…()` methods return **boolean**, `to…Case()` return **char**, `parseInt()` returns **int**. Watch for **+ with a String** (it joins) versus + with numbers (it adds).

---

## 1. Complete Lesson

### Library classes and packages

Java comes with thousands of ready-made **library classes**, grouped into **packages**:

| Package | Some classes | Needs import? |
|---|---|---|
| java.lang | String, Math, System, the wrapper classes (Integer, Character …) | No — imported automatically |
| java.util | Scanner, Arrays, Random | Yes: `import java.util.*;` |
| java.io | input and output streams | Yes: `import java.io.*;` |
| java.awt | graphics and windows | Yes |

Because **java.lang** is the default package, classes such as Integer, Character and Math can be used **without an import statement** (ICSE 2025 specimen Q1(xvi)). Character class methods are found in java.lang (ICSE 2025 Q1(i)), and so are all the wrapper classes (ICSE 2018 Q2(a); 2024 specimen Q1(xiii)).

### Class as a composite type

A class groups several variables (possibly of different types) and the methods that work on them, so a class is a **composite data type**. A class written by the programmer is a **user-defined data type**: once `class Student` exists, `Student s;` declares a variable of that type just as `int n;` declares an int.

| Primitive type | Composite (class) type |
|---|---|
| Built into Java (8 types) | Built by combining other types; may be user-defined |
| Holds a single value | Holds several values and methods |
| Fixed size (int: 4 bytes) | Size depends on its members |
| Default value 0, 0.0, false or `'\u0000'` | Default value null |
| e.g. int, char, double | e.g. String, Scanner, Student, arrays |

### Wrapper classes

A **wrapper class** "wraps" a primitive value inside an object. There is one wrapper class for each primitive type, all in java.lang:

![Fig. 8.1 Every primitive type has a wrapper class; boxing and unboxing convert between them](figures/ca_ch08_fig01_wrapper_classes.png)

| Primitive | Wrapper class | Primitive | Wrapper class |
|---|---|---|---|
| byte | Byte | float | Float |
| short | Short | double | Double |
| int | **Integer** | char | **Character** |
| long | Long | boolean | Boolean |

The wrapper class for char is **Character** (not Char — ICSE 2024 specimen Q1(xii)), and for int it is **Integer**.

**Why wrapper classes are needed:**
- They provide **useful static methods** — converting a String to a number (`Integer.parseInt("45")`) or testing a character (`Character.isDigit(ch)`).
- They provide **constants** such as `Integer.MAX_VALUE` (2147483647) and `Integer.MIN_VALUE` (−2147483648).
- Some parts of Java (for example collections of objects) work only with **objects**, not primitive values.

### Numeric wrapper methods: converting between Strings and numbers

Input read as text, or digits inside a String, must be converted before arithmetic. The **parse** methods take a **String** argument (ICSE 2026 Q1(xiii)):

| Method | Converts | Example | Result |
|---|---|---|---|
| `Integer.parseInt(String)` | String → int | `Integer.parseInt("4578")` | 4578 |
| `Long.parseLong(String)` | String → long | `Long.parseLong("9436012345")` | 9436012345 |
| `Float.parseFloat(String)` | String → float | `Float.parseFloat("2.5")` | 2.5 |
| `Double.parseDouble(String)` | String → double | `Double.parseDouble("25")` | 25.0 |
| `Integer.valueOf(String)` | String → Integer object (unboxes to int) | `int b = Integer.valueOf("22");` | 22 |
| `Integer.toString(int)` | int → String | `Integer.toString(254) + 1` | "2541" |
| `String.valueOf(any)` | any value → String | `String.valueOf(3.5) + 2` | "3.52" |

Two points the examiners test:
- **+ joins Strings but adds numbers.** `"12" + "8"` is "128", while `Integer.parseInt("12") + Integer.parseInt("8")` is 20.
- **The parsed type must fit the variable.** `int y = Double.parseDouble(x);` is a **compile-time (syntax) error** — *possible lossy conversion from double to int*; write `double y = …` (ICSE 2025 specimen Q2(viii)).

If the String is not a valid number, parsing fails **at run time** with a **NumberFormatException**: `Integer.parseInt("25.5")` and `Integer.parseInt("abc")` both stop the program. Spelling mistakes such as `Integer.parseint` are compile errors (*cannot find symbol*), and `Integer.parseInt(4578)` without quotes is also a compile error (*int cannot be converted to String*).

### Character class methods

The Character class provides **static** methods — called with the class name, without an object — to test and convert single characters (`isLetter(char)` is a static method; length() and nextLine() are not — ICSE 2025 Improvement Q1(xiv)).

| Method | Returns | True / result for |
|---|---|---|
| `Character.isLetter(ch)` | boolean | 'A'–'Z', 'a'–'z' |
| `Character.isDigit(ch)` | boolean | '0'–'9' |
| `Character.isLetterOrDigit(ch)` | boolean | a letter or a digit |
| `Character.isWhitespace(ch)` | boolean | space, tab `'\t'`, new line `'\n'` |
| `Character.isUpperCase(ch)` | boolean | 'A'–'Z' |
| `Character.isLowerCase(ch)` | boolean | 'a'–'z' |
| `Character.toUpperCase(ch)` | char | the capital form; other characters unchanged |
| `Character.toLowerCase(ch)` | char | the small form; other characters unchanged |

![Fig. 8.2 Classifying a character with the static methods of the Character class](figures/ca_ch08_fig02_character_methods.png)

Points that come up again and again:
- `Character.toUpperCase('a')` is 'A'; `Character.isLetterOrDigit('#')` is false (ICSE 2023 Q2(iv)).
- **Non-letters are returned unchanged:** `Character.toLowerCase('1')` is '1' (ICSE 2024 specimen Q1(xx)); `Character.toUpperCase('#')` is '#'.
- `Character.isLetterOrDigit('\n')` is **false** — a new line is neither (ICSE 2025 Improvement Q1(x)).
- isUpperCase() **checks** and returns boolean; toUpperCase() **converts** and returns char (ICSE 2018 Q1(c)).

### Characters in arithmetic

A char is stored as its code (Unicode, matching ASCII for English letters and digits): 'A' = 65, 'a' = 97, '0' = 48.
- `int res = 'A';` gives 65 (ICSE 2018 Q2(a)).
- **char + int gives int:** `Character.toUpperCase('b') + 2` is 'B' + 2 = 66 + 2 = **68**, printed as a number (ICSE 2026 Q1(vii)). Storing it in a char needs a cast: `char c = (char) (Character.toUpperCase('b') + 2);` gives 'D'.
- **Digit value:** for a digit character ch, `ch - '0'` is its numeric value ('7' − '0' = 7).
- **Position in the alphabet:** `Character.toLowerCase('Q') - 'a'` is 16.

Example (ICSE 2025 specimen Q2(vii)): `char chr = Character.toLowerCase('B');` gives 'b' (98); `(char) (98 - 10)` is 'X'; so `System.out.println((char) n + "\t" + chr);` prints X, a tab, then b.

### Character codes to remember

Many output questions need only a few codes:

| Characters | Codes | Note |
|---|---|---|
| space | 32 | the smallest printable character |
| '0' to '9' | 48 to 57 | digit value = ch − 48 = ch − '0' |
| 'A' to 'Z' | 65 to 90 | capitals come first |
| 'a' to 'z' | 97 to 122 | small letter = capital + 32 |

So the case of a letter can also be changed by arithmetic: `(char) ('g' - 32)` is 'G' and `(char) ('K' + 32)` is 'k' — the gap 'a' − 'A' is 32. The Character methods are safer, because they leave non-letters alone.

Two more traps with + and char:
- `'A' + 'B'` adds the codes: **131**.
- `"" + 'A' + 'B'` starts with a String, so + joins: **AB**.

### The character-by-character pattern

Programs that classify or change characters all follow one loop:

```java
for (int i = 0; i < s.length(); i++)
{
    char ch = s.charAt(i);          // take one character
    if (Character.isUpperCase(ch))  // test it
        upper++;                    // count it, or build a new String
    else if (Character.isDigit(ch))
        digit++;
    // ... other tests
}
```

Test with the **is…()** methods; change with the **to…()** methods; build a new String with `t = t + ch;`.

### Autoboxing, unboxing and boxing

- **Boxing** — converting a primitive value into an object of its wrapper class (ICSE 2024 specimen Q1(iv)): `Integer k = Integer.valueOf(40);`
- **Unboxing** — converting a wrapper object back to its primitive type (ICSE 2023 Q1(xviii)): `int v = k.intValue();`
- **Autoboxing** — Java does the boxing **automatically** when a primitive is assigned to a wrapper variable: `Integer n = 25;` (ICSE 2020 Q2(a)).
- **Auto-unboxing** — Java unboxes automatically when a wrapper object is used where a primitive is needed: `int m = n;` or `n + 5`.

```java
Integer boxed = 25;          // autoboxing
int unboxed = boxed;         // unboxing
System.out.println(boxed + unboxed);     // 50
Double dd = 2.5;             // autoboxing a double
System.out.println(dd * 2);  // 5.0 (unboxed for the multiplication)
```

### Summary of the chapter

- **Library classes** live in packages; **java.lang** (String, Math, wrappers) needs no import, java.util (Scanner) does.
- **Class** = composite, user-defined type; primitive = single built-in value.
- **Wrapper classes**: Byte, Short, Integer, Long, Float, Double, Character, Boolean — in java.lang.
- **Conversions**: parseInt/parseDouble (String → number, String argument), valueOf, toString, String.valueOf; NumberFormatException for bad input.
- **Character methods** (static): isLetter, isDigit, isLetterOrDigit, isWhitespace, isUpperCase, isLowerCase (boolean); toUpperCase, toLowerCase (char).
- **Boxing / unboxing / autoboxing**: primitive ↔ wrapper object, automatically when needed.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Name common library packages and explain why java.lang needs no import.
2. Distinguish primitive and composite (class) types.
3. Name the wrapper class of each primitive type and explain why wrappers are needed.
4. Convert between Strings and numbers with parse and valueOf methods, and predict errors.
5. Use the Character methods to test and convert characters, and state their return types.
6. Define boxing, unboxing and autoboxing with examples.

---

## 3. Detailed Section Explanations

### Section 1 — Ready-made tools
Library classes save effort; know which package each lives in.

### Section 2 — A box for a value
A wrapper class turns a primitive into an object and adds helpful methods and constants.

### Section 3 — Text to number and back
Text must be parsed before arithmetic; + on Strings joins them.

### Section 4 — Test, then convert
is…() methods test a character (boolean); to…() methods convert it (char).

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Library class | A ready-made class supplied with Java. |
| Package | A group of related classes, e.g. java.lang, java.util. |
| java.lang | The default package, imported automatically. |
| Composite data type | A type made from other types, e.g. a class or array. |
| User-defined data type | A class written by the programmer. |
| Wrapper class | A class whose object holds one primitive value. |
| Boxing | Converting a primitive to its wrapper object. |
| Unboxing | Converting a wrapper object to its primitive. |
| Autoboxing | Boxing done automatically by Java. |
| parseInt() | Converts a String of digits to an int. |
| NumberFormatException | The run-time error for text that is not a valid number. |
| Static method | A method called with the class name, e.g. Character.isDigit(ch). |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| Package of Character methods and wrapper classes | java.lang |
| Wrapper class of char | Character |
| Parameter type of parseInt() | String |
| Converts "25" to 25.0 | `Double.parseDouble("25")` |
| Converts "4578" to 4578 | `Integer.parseInt("4578")` |
| Character method that returns char | toUpperCase(char) / toLowerCase(char) |
| Return type of isWhitespace() | boolean |
| Return type of compareToIgnoreCase() | int |
| `Character.toUpperCase('b') + 2` | 68 |
| `Character.isLetterOrDigit('\n')` | false |
| Primitive → object | boxing |
| Object → primitive | unboxing |

### 5.2 Memory aids

- **"is → boolean, to → char, parse → number."**
- **"Only two irregular wrappers: Integer and Character."**
- **"Quotes join, numbers add."**

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- `Integer.toBinaryString(10)` gives "1010"; `Integer.toHexString(255)` gives "ff".
- Adding 1 to Integer.MAX_VALUE wraps round to Integer.MIN_VALUE (−2147483648) — an overflow.
- `Boolean.parseBoolean("TRUE")` is true (case is ignored), but any other text, such as "yes", gives false.

---

## 6. Person Profiles

### 6.1 Joe Becker, Lee Collins and Mark Davis
In 1987–88 Joe Becker of Xerox, with Lee Collins and Mark Davis of Apple, began the Unicode character code, which gives every character of the world's scripts its own number. Java's char holds Unicode values, which is why 'A' is 65 and why Character methods work for letters of many languages.

### 6.2 Joshua Bloch (born 1961)
An American software engineer who designed and built much of the Java platform's library at Sun Microsystems, including its collections framework, and wrote *Effective Java*, a widely read guide to using library classes well.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Don't reinvent the wheel** — use the library.
- **Text is not a number** — parse before you calculate.
- **Classify, then act** — Character methods sort characters into kinds.

### 7.2 Real-life connections
- **Online forms:** a mobile number typed into a form arrives as text and is parsed with Long.parseLong.
- **Passwords:** websites check for an uppercase letter, a digit and a special character with methods like isUpperCase and isDigit.
- **Meghalaya:** a bus-ticket app converts "45.50" typed by a conductor into a double to total the day's fares.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section A** (40 marks) asks MCQs and 2-mark outputs on Character and wrapper methods almost every year. **Section B** programs (Strings and characters) rely on Character methods to classify characters.

### 8.1 Graded exercises — solutions

#### Exercise 8A — Concepts

**Q1.** Name the wrapper classes of int, char and boolean.
**Answer:** Integer, Character and Boolean.

**Q2.** Why can Math and Integer be used without an import statement?
**Answer:** They belong to java.lang, which Java imports automatically.

**Q3.** Give the return types of Character.isDigit() and Character.toLowerCase().
**Answer:** boolean and char.

**Q4.** Define autoboxing with an example.
**Answer:** Java automatically converts a primitive into its wrapper object: `Integer n = 25;`.

#### Exercise 8B — Outputs

**Q5.** Give the output: `System.out.println("12" + "8"); System.out.println(Integer.parseInt("12") + Integer.parseInt("8"));`
**Answer:** `128` then `20`.

**Q6.** Give the output: `System.out.println(Double.parseDouble("7") / 2);`
**Answer:** `3.5`

**Q7.** Give the output: `System.out.println((char) (Character.toUpperCase('m') + 1));`
**Answer:** `N` — 'M' + 1 is 78, cast back to char.

**Q8.** Give the output: `char c = '7'; System.out.println(c - '0' + 1);`
**Answer:** `8` — '7' − '0' is 7.
### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(vii) (1 mark) | The output of the statement `System.out.println(Character.toUpperCase('b') + 2);` is: (a) 66 (b) 100 (c) 68 (d) 98 |
| ICSE 2026, Q1(xiii) (1 mark) | What is the type of parameter to be given for the method parseInt()? (a) double (b) String (c) char (d) int |
| ICSE 2026 Improvement, Q1(ii) (1 mark) | Which of the following Character methods results in char? (a) Character.isUpperCase(char) (b) Character.isLowerCase(char) (c) Character.toUpperCase(char) (d) character.toupperCase(char) |
| ICSE 2026 Improvement, Q1(iii) (1 mark) | [Picture: the String "4578" converted to the number 4578] Select the correct method to perform the above conversion: (a) Integer.ParseInt(4578) (b) Integer.parseInt("4578") (c) Integer.parse(4578) (d) Integer.parseint("4578") |
| ICSE 2025, Q1(i) (1 mark) | Character class methods are found in the package called: (a) java.util (b) java.lang (c) java.awt (d) java.io |
| ICSE 2025, Q1(xvi) (1 mark) | Which of the following converts "25" to 25.0? (a) Double.Parsedouble("25") (b) Double.parse("25") (c) Double.parseDouble("25") (d) Double.parseDouble(25) |
| ICSE 2025 Improvement, Q1(x) (1 mark) | What will be the output of the following Java method? `Character.isLetterOrDigit('\n')` (a) 1 (b) 0 (c) true (d) false |
| ICSE 2025 Improvement, Q1(xiv) (1 mark) | Identify the static method from the list given below: (a) length() (b) nextLine() (c) substring(int) (d) isLetter(char) |
| ICSE 2025 specimen, Q1(xv) (1 mark) | The method to convert a lowercase character to uppercase is: (a) String.toUpperCase() (b) Character.isUppercase(char) (c) Character.toUpperCase(char) (d) toUpperCase() |
| ICSE 2025 specimen, Q1(xvi) (1 mark) | Assertion (A): Integer class can be used in the program without calling a package. Reason (R): It belongs to the default package java.lang. (a) Both A and R are true and R is a correct explanation of A (b) Both A and R are true and R is not a correct explanation of A (c) A is true and R is false (d) A is false and R is true |
| ICSE 2025 specimen, Q2(vii) (2 marks) | Predict the output of the following code snippet: `char ch = 'B'; char chr = Character.toLowerCase(ch); int n = (int) chr - 10; System.out.println((char) n + "\t" + chr);` |
| ICSE 2025 specimen, Q2(viii) (2 marks) | A student is trying to convert the string present in x to a numerical value, so as to find the square root of the converted value. However the code has an error. Name the error (syntax / logical / runtime). Correct the code so that it compiles and runs correctly. `String x = "25"; int y = Double.parseDouble(x); double r = Math.sqrt(y); System.out.println(r);` |
| ICSE 2024, Q1(ix) (1 mark) | What is the method to check whether a character is a letter or digit? (a) isDigit(char) (b) isLetterOrDigit() (c) isLetterOrDigit(char) (d) isLETTERorDIGIT(char) |
| ICSE 2024, Q2(v) (2 marks) | `String s1 = "45.50"; String s2 = "54.50"; double d1 = Double.parseDouble(s1); double d2 = Double.parseDouble(s2); int x = (int)(d1 + d2);` What is the value of x? |
| ICSE 2024, Q2(vii) (2 marks) | Differentiate between boxing and unboxing. |
| ICSE 2024 specimen, Q1(iv) (1 mark) | When a primitive data type is converted to a corresponding object of its class, it is called: (a) Boxing (b) Unboxing (c) explicit type conversion (d) implicit type conversion |
| ICSE 2024 specimen, Q1(xii) (1 mark) | Which of the following is the wrapper class for the data type char? (a) String (b) Char (c) Character (d) Float |
| ICSE 2024 specimen, Q1(xiii) (1 mark) | Name the package that contains wrapper classes: (a) java.lang (b) java.util (c) java.io (d) java.awt |
| ICSE 2024 specimen, Q1(xx) (1 mark) | What will be the output for: `System.out.print(Character.toLowerCase('1'));` (a) 0 (b) 1 (c) A (d) true |
| ICSE 2024 specimen, Q2(viii) (2 marks) | Predict the output of the following code snippet: `String a = "20"; String b = "23"; int p = Integer.parseInt(a); int q = Integer.parseInt(b); System.out.print(a + "*" + b);` |
| ICSE 2023, Q1(x) (1 mark) | Predict the output of the following code snippet: `String P = "20", Q = "22"; int a = Integer.parseInt(P); int b = Integer.valueOf(Q); System.out.println(a + "" + b);` (a) 20 (b) 20 22 (c) 2220 (d) 22 |
| ICSE 2023, Q1(xviii) (1 mark) | When an object of a Wrapper class is converted to its corresponding primitive data type, it is called as ___________. (a) Boxing (b) Explicit type conversion (c) Unboxing (d) Implicit type conversion |
| ICSE 2023, Q2(iv) (2 marks) | Give the output of the following Character class methods: (a) `Character.toUpperCase('a')` (b) `Character.isLetterOrDigit('#')` |
| ICSE 2020, Q2(a) (2 marks) | What is autoboxing in Java? Give an example. |
| ICSE 2020, Q3(f) (2 marks) | What is the data type returned by the following library methods? (i) isWhitespace() (ii) compareToIgnoreCase() |
| ICSE 2019, Q2(b) (2 marks) | Give the output of the following code: `String P = "20", Q = "19"; int a = Integer.parseInt(P); int b = Integer.valueOf(Q); System.out.println(a + "" + b);` |
| ICSE 2019, Q2(d) (2 marks) | State the data type and value of res after the following is executed: `char ch = '9'; res = Character.isDigit(ch);` |
| ICSE 2018, Q1(c) (2 marks) | Write a difference between the functions isUpperCase() and toUpperCase(). |
| ICSE 2018, Q2(a) (2 marks) | (i) `int res = 'A';` What is the value of res? (ii) Name the package that contains wrapper classes. |
| ICSE 2017, Q2(c) (2 marks) | State the data type and value of res after the following is executed: `char ch = 't'; res = Character.toUpperCase(ch);` |
| ICSE 2017, Q3(h) (2 marks) | Give the output of the following code: `String A = "26", B = "100"; String D = A + B + "200"; int x = Integer.parseInt(A); int y = Integer.parseInt(B); int d = x + y; System.out.println("Result 1 = " + D); System.out.println("Result 2 = " + d);` |

**Solutions**

**2026 Q1(vii).** **(c) 68** — toUpperCase('b') gives 'B' (66); a char plus an int is an int, so 66 + 2 = 68 is printed. *(Worked answer.)*

**2026 Q1(xiii).** **(b) String** — parseInt converts a String such as "45" into an int. *(Worked answer.)*

**2026 Improvement Q1(ii).** **(c) Character.toUpperCase(char)** — the is…() methods return boolean, and option (d) is misspelt. *(Worked answer.)*

**2026 Improvement Q1(iii).** **(b) Integer.parseInt("4578")** — exact spelling, and a String argument. *(Worked answer.)*

**2025 Q1(i).** **(b) java.lang**

**2025 Q1(xvi).** **(c) Double.parseDouble("25")**

**2025 Improvement Q1(x).** **(d) false** — `'\n'` (new line) is neither a letter nor a digit. *(Worked answer.)*

**2025 Improvement Q1(xiv).** **(d) isLetter(char)** — Character.isLetter() is static and is called with the class name; length(), nextLine() and substring() are called through objects. *(Worked answer.)*

**2025 specimen Q1(xv).** **(c) Character.toUpperCase(char)**

**2025 specimen Q1(xvi).** **(a) Both A and R are true and R is a correct explanation of A**

**2025 specimen Q2(vii).** chr = 'b' (98); n = 98 − 10 = 88; (char) 88 is 'X'. Output: **X**, then a tab space, then **b**.

**2025 specimen Q2(viii).** **Syntax (compile-time) error** — parseDouble returns a double, which cannot be stored in an int (javac: possible lossy conversion from double to int). Correct statement: `double y = Double.parseDouble(x);` — the program then prints 5.0.

**2024 Q1(ix).** **(c) isLetterOrDigit(char)**

**2024 Q2(v).** **100** — 45.5 + 54.5 = 100.0, and (int) gives 100. The examiners noted that some candidates rounded the numbers first, ignored the cast, or joined the Strings instead of converting them.

**2024 Q2(vii).** **Boxing** is the conversion of a primitive type into an object of its wrapper class, e.g. `Integer k = Integer.valueOf(40);`. **Unboxing** is the conversion of a wrapper-class object back to the corresponding primitive, e.g. `int v = k.intValue();`. The examiners noted that some candidates interchanged the two.

**2024 specimen Q1(iv).** **(a) Boxing** *(Worked answer.)*

**2024 specimen Q1(xii).** **(c) Character** *(Worked answer.)*

**2024 specimen Q1(xiii).** **(a) java.lang** *(Worked answer.)*

**2024 specimen Q1(xx).** **(b) 1** — toLowerCase leaves a non-letter unchanged. *(Worked answer.)*

**2024 specimen Q2(viii).** `20*23` — the + operators join the Strings a and b; p and q are calculated but not printed. *(Worked answer.)*

**2023 Q1(x).** **(b) 20 22** in the scheme. Java actually prints `2022` with no space — "" turns + into joining. The examiners noted that many candidates chose (c) 2220, reversing the order.

**2023 Q1(xviii).** **(c) Unboxing** — the examiners noted that many chose (b) or (d).

**2023 Q2(iv).** (a) **A** (b) **false** — the examiners noted that a few wrote 'a' or true.

**2020 Q2(a).** **Autoboxing** is the automatic conversion of a primitive value into an object of its wrapper class by the Java compiler, e.g. `Integer n = 25;` (or `Character c = 'x';`). *(Worked answer.)*

**2020 Q3(f).** (i) **boolean** (ii) **int** *(Worked answer.)*

**2019 Q2(b).** **2019** — a is 20 and b is 19, and `a + "" + b` joins them.

**2019 Q2(d).** (i) **boolean** (ii) **true**

**2018 Q1(c).** isUpperCase() **checks** whether a character is an uppercase letter and returns a **boolean**; toUpperCase() **converts** a character to uppercase and returns a **char**.

**2018 Q2(a).** (i) **65** (ii) **java.lang**

**2017 Q2(c).** Data type **char**, value **'T'**. *(Worked answer.)*

**2017 Q3(h).** Output: *(Worked answer.)*
```
Result 1 = 26100200
Result 2 = 126
```
D joins the three Strings; d adds the parsed numbers 26 + 100.

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Give the output: `System.out.println(Integer.toString(254) + 1); System.out.println(String.valueOf(3.5) + 2);`
**Answer:** `2541` and `3.52` — both are Strings, so + joins.

**Q2.** (2 marks) What happens when `Integer.parseInt("25.5")` runs? Name the error.
**Answer:** The program stops with a NumberFormatException — a run-time error, since "25.5" is not an integer.

**Q3.** (2 marks) Give the output: `Integer boxed = 25; int unboxed = boxed; System.out.println(boxed + unboxed);`
**Answer:** `50` — boxed is unboxed for the addition.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| MCQ | Output of a Character method; correct parse method; wrapper of char; package java.lang | 8.2, 5.1 |
| 2 marks | Output of parseInt / valueOf with + and "" | 8.2, Section 10 |
| 2 marks | Boxing vs unboxing; autoboxing with an example | 8.2, Section 1 |
| 15 marks | Count or convert the characters of a String with Character methods | Section 11 |

---
## 9. MCQs with Explanations

### Packages and composite types (Q1–Q12)

**Q1.** Character class methods are found in the package
- (a) java.util
- (b) java.lang
- (c) java.awt
- (d) java.io

**Answer:** (b) java.lang
**Explanation:** The default package.

**Q2.** The package that is imported automatically into every Java program is
- (a) java.util
- (b) java.io
- (c) java.lang
- (d) java.awt

**Answer:** (c) java.lang
**Explanation:** No import statement is needed.

**Q3.** The Scanner class belongs to
- (a) java.lang
- (b) java.awt
- (c) java.math
- (d) java.util

**Answer:** (d) java.util
**Explanation:** Hence import java.util.*;

**Q4.** The package that contains the wrapper classes is
- (a) java.lang
- (b) java.util
- (c) java.io
- (d) java.awt

**Answer:** (a) java.lang
**Explanation:** Integer, Character and the rest.

**Q5.** The Integer class can be used without an import statement because
- (a) it belongs to java.lang
- (b) it is a keyword
- (c) it is a primitive type
- (d) it is user-defined

**Answer:** (a) it belongs to java.lang
**Explanation:** java.lang is imported automatically.

**Q6.** A class is called a composite data type because it
- (a) groups variables and methods together
- (b) holds a single value
- (c) is built into the processor
- (d) has a fixed size of 4 bytes

**Answer:** (a) groups variables and methods together
**Explanation:** It is built from other types.

**Q7.** Which is a primitive data type?
- (a) String
- (b) Scanner
- (c) char
- (d) Integer

**Answer:** (c) char
**Explanation:** The others are classes.

**Q8.** The default value of a String instance variable is
- (a) ""
- (b) " "
- (c) 0
- (d) null

**Answer:** (d) null
**Explanation:** Composite types default to null.

**Q9.** A class written by the programmer is a
- (a) keyword
- (b) primitive data type
- (c) package
- (d) user-defined data type

**Answer:** (d) user-defined data type
**Explanation:** It can then declare variables.

**Q10.** Which statement about primitive types is TRUE?
- (a) They hold a single value.
- (b) They have methods.
- (c) Their default value is null.
- (d) They are created with new.

**Answer:** (a) They hold a single value.
**Explanation:** e.g. int n = 5;

**Q11.** Math, String and System are classes of
- (a) java.io
- (b) java.util
- (c) java.lang
- (d) java.net

**Answer:** (c) java.lang
**Explanation:** All used without import.

**Q12.** A package is
- (a) an operator
- (b) a single method
- (c) a primitive type
- (d) a group of related classes

**Answer:** (d) a group of related classes
**Explanation:** e.g. java.util.

### Wrapper classes, boxing and unboxing (Q13–Q28)

**Q13.** The wrapper class for the data type char is
- (a) String
- (b) Char
- (c) Character
- (d) Float

**Answer:** (c) Character
**Explanation:** Not Char.

**Q14.** The wrapper class for int is
- (a) Int
- (b) Number
- (c) Integer
- (d) Long

**Answer:** (c) Integer
**Explanation:** One of the two irregular names.

**Q15.** The wrapper class for boolean is
- (a) Boolean
- (b) Bool
- (c) Bit
- (d) Logic

**Answer:** (a) Boolean
**Explanation:** Capital B.

**Q16.** How many wrapper classes does Java have for its primitive types?
- (a) 4
- (b) 6
- (c) 8
- (d) 10

**Answer:** (c) 8
**Explanation:** One per primitive type.

**Q17.** When a primitive data type is converted to a corresponding object of its class, it is called
- (a) implicit type conversion
- (b) unboxing
- (c) explicit type conversion
- (d) boxing

**Answer:** (d) boxing
**Explanation:** The value is put in a box (object).

**Q18.** When an object of a wrapper class is converted to its primitive type, it is called
- (a) boxing
- (b) explicit type conversion
- (c) unboxing
- (d) implicit type conversion

**Answer:** (c) unboxing
**Explanation:** The value comes out of the box.

**Q19.** Integer n = 25; is an example of
- (a) parsing
- (b) unboxing
- (c) explicit casting
- (d) autoboxing

**Answer:** (d) autoboxing
**Explanation:** Java boxes the int automatically.

**Q20.** int m = n; where n is an Integer object, is an example of
- (a) boxing
- (b) unboxing
- (c) parsing
- (d) widening

**Answer:** (b) unboxing
**Explanation:** The object gives back an int.

**Q21.** Integer boxed = 25; int unboxed = boxed; System.out.println(boxed + unboxed); prints
- (a) 2525
- (b) 25
- (c) 50
- (d) an error message

**Answer:** (c) 50
**Explanation:** Both are numbers for +.

**Q22.** Double dd = 2.5; System.out.println(dd * 2); prints
- (a) 5
- (b) 5.0
- (c) 2.52
- (d) an error message

**Answer:** (b) 5.0
**Explanation:** Unboxed for the multiplication.

**Q23.** Integer k = Integer.valueOf(40); System.out.println(k.intValue() / 3); prints
- (a) 3
- (b) 13.33
- (c) 40
- (d) 13

**Answer:** (d) 13
**Explanation:** int division.

**Q24.** One reason wrapper classes are needed is that they
- (a) remove the need for variables
- (b) make programs run faster
- (c) replace all primitive types
- (d) provide methods to convert Strings to numbers

**Answer:** (d) provide methods to convert Strings to numbers
**Explanation:** e.g. Integer.parseInt.

**Q25.** Integer.MAX_VALUE is
- (a) 2147483647
- (b) 32767
- (c) 65535
- (d) 9999999999

**Answer:** (a) 2147483647
**Explanation:** The largest int.

**Q26.** System.out.println(Integer.MAX_VALUE + 1); prints
- (a) 2147483648
- (b) -2147483648
- (c) an error message
- (d) 0

**Answer:** (b) -2147483648
**Explanation:** int overflow wraps round.

**Q27.** Autoboxing is done by
- (a) the Java compiler automatically
- (b) the programmer with a cast
- (c) the Scanner class
- (d) the import statement

**Answer:** (a) the Java compiler automatically
**Explanation:** No method call is written.

**Q28.** Which statement shows explicit boxing?
- (a) double d = 40;
- (b) int v = 40;
- (c) int v = k.intValue();
- (d) Integer k = Integer.valueOf(40);

**Answer:** (d) Integer k = Integer.valueOf(40);
**Explanation:** valueOf makes an Integer object.

### Converting between Strings and numbers (Q29–Q46)

**Q29.** The type of parameter given to parseInt() is
- (a) double
- (b) char
- (c) String
- (d) int

**Answer:** (c) String
**Explanation:** It converts text to an int.

**Q30.** Which converts "25" to 25.0?
- (a) Double.parse("25")
- (b) Integer.parseInt("25")
- (c) Double.parseDouble("25")
- (d) Double.parseDouble(25)

**Answer:** (c) Double.parseDouble("25")
**Explanation:** String argument, double result.

**Q31.** The correct method to convert "4578" into the int 4578 is
- (a) Integer.parse(4578)
- (b) Integer.parseInt("4578")
- (c) String.parseInt("4578")
- (d) Integer.toString(4578)

**Answer:** (b) Integer.parseInt("4578")
**Explanation:** A String argument is needed.

**Q32.** The return type of Integer.parseInt("12") is
- (a) String
- (b) int
- (c) double
- (d) char

**Answer:** (b) int
**Explanation:** A primitive int.

**Q33.** System.out.println("12" + "8"); prints
- (a) 20
- (b) 128
- (c) 12 8
- (d) an error message

**Answer:** (b) 128
**Explanation:** + joins Strings.

**Q34.** System.out.println(Integer.parseInt("12") + Integer.parseInt("8")); prints
- (a) 12 8
- (b) 128
- (c) 20
- (d) 4

**Answer:** (c) 20
**Explanation:** + adds the parsed numbers.

**Q35.** String s1 = "45.50", s2 = "54.50"; int x = (int)(Double.parseDouble(s1) + Double.parseDouble(s2)); The value of x is
- (a) 99
- (b) 100
- (c) 45505450
- (d) 101

**Answer:** (b) 100
**Explanation:** 45.5 + 54.5 = 100.0.

**Q36.** String P = "20", Q = "19"; int a = Integer.parseInt(P); int b = Integer.valueOf(Q); System.out.println(a + "" + b); prints
- (a) 39
- (b) 2019
- (c) 1920
- (d) 20 19

**Answer:** (b) 2019
**Explanation:** "" makes + join.

**Q37.** String a = "20", b = "23"; with p and q the parsed values, System.out.print(a + "*" + b); prints
- (a) 460
- (b) `20*23`
- (c) 43
- (d) an error message

**Answer:** (b) `20*23`
**Explanation:** a and b are Strings; p and q are unused.

**Q38.** int y = Double.parseDouble("25"); gives
- (a) 25
- (b) a compile-time (syntax) error
- (c) a run-time error
- (d) a logical error

**Answer:** (b) a compile-time (syntax) error
**Explanation:** Possible lossy conversion from double to int.

**Q39.** Integer.parseInt("25.5") gives
- (a) 25
- (b) 26
- (c) a NumberFormatException at run time
- (d) a compile-time error

**Answer:** (c) a NumberFormatException at run time
**Explanation:** "25.5" is not an integer.

**Q40.** Integer.parseInt(4578) (without quotes) gives
- (a) 4578
- (b) a compile error: int cannot be converted to String
- (c) a run-time error
- (d) "4578"

**Answer:** (b) a compile error: int cannot be converted to String
**Explanation:** The argument must be a String.

**Q41.** System.out.println(Integer.toString(254) + 1); prints
- (a) 255
- (b) 2541
- (c) 254
- (d) an error message

**Answer:** (b) 2541
**Explanation:** toString gives a String.

**Q42.** System.out.println(String.valueOf(3.5) + 2); prints
- (a) 5.5
- (b) 7.0
- (c) 3.5
- (d) 3.52

**Answer:** (d) 3.52
**Explanation:** valueOf gives a String.

**Q43.** System.out.println(Double.parseDouble("7") / 2); prints
- (a) 3
- (b) 3.5
- (c) 3.0
- (d) 72

**Answer:** (b) 3.5
**Explanation:** 7.0 / 2.

**Q44.** System.out.println(Integer.valueOf("15") + 5); prints
- (a) 155
- (b) 15
- (c) 20
- (d) an error message

**Answer:** (c) 20
**Explanation:** The Integer is unboxed and added.

**Q45.** The method that converts "9436012345" into a number without overflow is
- (a) Integer.parseInt
- (b) Character.getNumericValue
- (c) Long.parseLong
- (d) String.valueOf

**Answer:** (c) Long.parseLong
**Explanation:** It is larger than the int range.

**Q46.** String A = "26", B = "100"; String D = A + B + "200"; The value of D is
- (a) 326
- (b) 226
- (c) 126200
- (d) 26100200

**Answer:** (d) 26100200
**Explanation:** Three Strings joined.

### Character class methods (Q47–Q66)

**Q47.** The method to check whether a character is a letter or digit is
- (a) isDigit(char)
- (b) isLetterOrDigit()
- (c) isLetterOrDigit(char)
- (d) isLetter(char)

**Answer:** (c) isLetterOrDigit(char)
**Explanation:** It takes the character as argument.

**Q48.** Which Character method returns a char?
- (a) Character.isUpperCase(char)
- (b) Character.isLowerCase(char)
- (c) Character.toUpperCase(char)
- (d) Character.isDigit(char)

**Answer:** (c) Character.toUpperCase(char)
**Explanation:** is…() methods return boolean.

**Q49.** The method to convert a lowercase character to uppercase is
- (a) String.toUpperCase()
- (b) Character.isUpperCase(char)
- (c) Character.toUpperCase(char)
- (d) toUpperCase()

**Answer:** (c) Character.toUpperCase(char)
**Explanation:** Static method of Character.

**Q50.** The output of `Character.isLetterOrDigit('\n')` is
- (a) 1
- (b) 0
- (c) true
- (d) false

**Answer:** (d) false
**Explanation:** A new line is neither.

**Q51.** Identify the static method:
- (a) length()
- (b) nextLine()
- (c) substring(int)
- (d) isLetter(char)

**Answer:** (d) isLetter(char)
**Explanation:** Called as Character.isLetter(ch).

**Q52.** System.out.print(Character.toLowerCase('1')); prints
- (a) 0
- (b) 1
- (c) A
- (d) true

**Answer:** (b) 1
**Explanation:** Non-letters are unchanged.

**Q53.** Character.toUpperCase('a') gives
- (a) 97
- (b) 65
- (c) true
- (d) A

**Answer:** (d) A
**Explanation:** A char result.

**Q54.** Character.isLetterOrDigit('#') gives
- (a) true
- (b) false
- (c) #
- (d) 35

**Answer:** (b) false
**Explanation:** # is a special character.

**Q55.** char ch = '9'; res = Character.isDigit(ch); The data type and value of res are
- (a) boolean, true
- (b) int, 9
- (c) char, '9'
- (d) boolean, false

**Answer:** (a) boolean, true
**Explanation:** '9' is a digit.

**Q56.** char ch = 't'; res = Character.toUpperCase(ch); The data type and value of res are
- (a) char, 'T'
- (b) boolean, true
- (c) int, 84
- (d) String, "T"

**Answer:** (a) char, 'T'
**Explanation:** toUpperCase returns char.

**Q57.** The return type of Character.isWhitespace() is
- (a) boolean
- (b) char
- (c) int
- (d) String

**Answer:** (a) boolean
**Explanation:** It tests a character.

**Q58.** Character.isWhitespace(' ') and Character.isWhitespace('_') give
- (a) true and true
- (b) true and false
- (c) false and true
- (d) false and false

**Answer:** (b) true and false
**Explanation:** The underscore is not whitespace.

**Q59.** Character.isLetter('5'), Character.isUpperCase('a') and Character.isLowerCase('a') give
- (a) true, true, true
- (b) true, false, true
- (c) false, true, false
- (d) false, false, true

**Answer:** (d) false, false, true
**Explanation:** '5' is a digit; 'a' is lowercase.

**Q60.** Character.toUpperCase('#') gives
- (a) #
- (b) an error message
- (c) 35
- (d) a space

**Answer:** (a) #
**Explanation:** Non-letters are unchanged.

**Q61.** isUpperCase() differs from toUpperCase() in that isUpperCase()
- (a) returns int
- (b) converts and returns char
- (c) works only on Strings
- (d) checks and returns boolean

**Answer:** (d) checks and returns boolean
**Explanation:** toUpperCase converts and returns char.

**Q62.** Which characters make Character.isWhitespace() true?
- (a) space, tab and new line
- (b) only the space
- (c) letters and digits
- (d) punctuation marks

**Answer:** (a) space, tab and new line
**Explanation:** All whitespace characters.

**Q63.** The Character methods such as isDigit() are called
- (a) with the class name, as Character.isDigit(ch)
- (b) through a Scanner object
- (c) only inside main
- (d) with new Character()

**Answer:** (a) with the class name, as Character.isDigit(ch)
**Explanation:** They are static.

**Q64.** To count the uppercase letters in a String s, the test inside the loop is
- (a) Character.isUpperCase(s.charAt(i))
- (b) Character.toUpperCase(s.charAt(i))
- (c) s.isUpperCase(i)
- (d) Character.isLetter(s)

**Answer:** (a) Character.isUpperCase(s.charAt(i))
**Explanation:** Test each character.

**Q65.** A character that is not a letter, digit or whitespace is counted as
- (a) a special character
- (b) a vowel
- (c) a consonant
- (d) a number

**Answer:** (a) a special character
**Explanation:** e.g. # @ ! ,

**Q66.** A password checker sets up = true when
- (a) the first character is a space
- (b) the password has eight characters
- (c) Character.isDigit(ch) is true
- (d) Character.isUpperCase(ch) is true for some character

**Answer:** (d) Character.isUpperCase(ch) is true for some character
**Explanation:** One capital letter is enough.

### Characters in arithmetic and output (Q67–Q76)

**Q67.** System.out.println(Character.toUpperCase('b') + 2); prints
- (a) 66
- (b) 100
- (c) 68
- (d) 98

**Answer:** (c) 68
**Explanation:** 'B' is 66; char + int is int.

**Q68.** int res = 'A'; The value of res is
- (a) A
- (b) 65
- (c) 97
- (d) 1

**Answer:** (b) 65
**Explanation:** The code of 'A'.

**Q69.** char ch = 'B'; char chr = Character.toLowerCase(ch); int n = (int) chr - 10; The value of (char) n is
- (a) 88
- (b) b
- (c) X
- (d) R

**Answer:** (c) X
**Explanation:** 98 − 10 = 88, which is 'X'.

**Q70.** System.out.println((char) (Character.toUpperCase('m') + 1)); prints
- (a) M1
- (b) O
- (c) 78
- (d) N

**Answer:** (d) N
**Explanation:** 'M' + 1 = 78, cast to char.

**Q71.** char c = '7'; System.out.println(c - '0' + 1); prints
- (a) 8
- (b) 71
- (c) 56
- (d) 7

**Answer:** (a) 8
**Explanation:** '7' − '0' is 7.

**Q72.** System.out.println(Character.toLowerCase('Q') - 'a'); prints
- (a) 16
- (b) 17
- (c) q
- (d) 113

**Answer:** (a) 16
**Explanation:** 'q' (113) − 'a' (97).

**Q73.** System.out.println((int) Character.toUpperCase('z')); prints
- (a) 90
- (b) 122
- (c) Z
- (d) 26

**Answer:** (a) 90
**Explanation:** 'Z' is 90.

**Q74.** char c = Character.toUpperCase('b') + 2; gives
- (a) 'D'
- (b) 'B'
- (c) 68
- (d) the error: possible lossy conversion from int to char

**Answer:** (d) the error: possible lossy conversion from int to char
**Explanation:** The sum is an int; a cast is needed.

**Q75.** In a Caesar code that shifts letters by 3, 'x' becomes
- (a) a
- (b) {
- (c) b
- (d) u

**Answer:** (a) a
**Explanation:** 'a' + (23 + 3) % 26.

**Q76.** System.out.println(Long.parseLong("9436012345") + 1); prints
- (a) 94360123451
- (b) 9436012346
- (c) an error message
- (d) 9436012345

**Answer:** (b) 9436012346
**Explanation:** The parsed long is added to 1.
## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** What are wrapper classes? Name two.
**Answer:** Classes whose objects hold a single primitive value, one for each primitive type, in java.lang.
e.g. Integer (for int) and Character (for char).

**Q2.** Give two reasons why wrapper classes are needed.
**Answer:** They provide methods such as `Integer.parseInt()` and `Character.isDigit()`, and constants such as `Integer.MAX_VALUE`.
Some parts of Java work only with objects, not primitive values.

**Q3.** Distinguish between boxing and unboxing.
**Answer:** Boxing converts a primitive value into an object of its wrapper class: `Integer k = Integer.valueOf(40);`.
Unboxing converts the wrapper object back to the primitive: `int v = k.intValue();`.

**Q4.** What is autoboxing? Give an example.
**Answer:** The automatic conversion of a primitive into its wrapper object by the Java compiler.
e.g. `Integer n = 25;`

**Q5.** Distinguish between primitive and composite data types.
**Answer:** A primitive type is built in and holds one value of fixed size, e.g. int.
A composite type (a class or array) groups several values and may be user-defined; its default value is null.

**Q6.** Why does the Integer class not need an import statement?
**Answer:** It belongs to java.lang.
java.lang is imported into every program automatically.

**Q7.** State the return types of Character.isLetter(), Character.toLowerCase(), Integer.parseInt() and Double.parseDouble().
**Answer:** boolean, char.
int, double.

**Q8.** Write one difference between isUpperCase() and toUpperCase().
**Answer:** isUpperCase() checks whether a character is a capital letter and returns boolean.
toUpperCase() converts a character to a capital and returns char.

**Q9.** Distinguish between Integer.parseInt() and Integer.valueOf().
**Answer:** parseInt("22") returns a primitive int.
valueOf("22") returns an Integer object, which is unboxed to int when needed.

**Q10.** What is a NumberFormatException, and when does it occur?
**Answer:** A run-time error that stops the program.
It occurs when a parse method gets text that is not a valid number, e.g. `Integer.parseInt("25.5")`.

**Q11.** Name the Character method used to check each of these: a capital letter, a digit, a space.
**Answer:** `Character.isUpperCase(ch)`, `Character.isDigit(ch)`.
`Character.isWhitespace(ch)`.

**Q12.** Write statements to convert (i) "125" to an int n and (ii) the double 3.75 to a String s.
**Answer:** (i) `int n = Integer.parseInt("125");`
(ii) `String s = String.valueOf(3.75);` (or `Double.toString(3.75)`).

### Output and error questions (2 marks each)

**Q13.** Give the output: `System.out.println("12" + "8"); System.out.println(Integer.parseInt("12") + Integer.parseInt("8"));`
**Answer:** `128` then `20`
Strings join; parsed numbers add.

**Q14.** Give the output of `System.out.println(Character.toUpperCase('b') + 2);` and of `System.out.println((char) (Character.toUpperCase('b') + 2));`
**Answer:** `68` and `D`
'B' + 2 is the int 68; the cast turns it into 'D'.

**Q15.** Give the output: `char ch = 'B'; char chr = Character.toLowerCase(ch); int n = (int) chr - 10; System.out.println((char) n + "\t" + chr);`
**Answer:** X, then a tab space, then b.
'b' is 98; 98 − 10 = 88, which is 'X'.

**Q16.** Give the output: `String A = "26", B = "100"; String D = A + B + "200"; int d = Integer.parseInt(A) + Integer.parseInt(B); System.out.println("Result 1 = " + D); System.out.println("Result 2 = " + d);`
**Answer:** `Result 1 = 26100200` then `Result 2 = 126`
D joins Strings; d adds numbers.

**Q17.** Give the output: `String P = "20", Q = "22"; int a = Integer.parseInt(P); int b = Integer.valueOf(Q); System.out.println(a + "" + b);`
**Answer:** `2022`
The empty String makes + join the two numbers.

**Q18.** Give the output: `System.out.println(Character.isWhitespace(' ') + " " + Character.isWhitespace('_'));` and `System.out.println(Character.isLetter('5') + " " + Character.isLowerCase('a'));`
**Answer:** `true false`
`false true`

**Q19.** Give the output: `Integer boxed = 25; int unboxed = boxed; System.out.println(boxed + unboxed); Double dd = 2.5; System.out.println(dd * 2);`
**Answer:** `50` then `5.0`
The objects are unboxed for the arithmetic.

**Q20.** Find the error and correct it: `String x = "25"; int y = Double.parseDouble(x);`
**Answer:** Compile-time error: possible lossy conversion from double to int.
Write `double y = Double.parseDouble(x);`.

**Q21.** Find the error and correct it: `char c = Character.toUpperCase('b') + 2;`
**Answer:** Compile-time error: possible lossy conversion from int to char — the sum is an int.
Write `char c = (char) (Character.toUpperCase('b') + 2);`, which gives 'D'.

**Q22.** What happens when `int n = Integer.parseInt("abc");` runs? How can a program avoid it?
**Answer:** A NumberFormatException stops the program at run time.
Check that every character is a digit with `Character.isDigit()` before parsing.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; sample runs follow each.*

### Section B programs (15 marks each)

**Q1.** Write a program to input a character and print its ASCII code. If it is a letter, state whether it is uppercase or lowercase and print it in the other case; if it is a digit, print twice its value; otherwise print "Special character". Use Character class methods.
**Answer:**
```java
import java.util.*;
class CharReport
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a character: ");
        char ch = sc.next().charAt(0);
        System.out.println("ASCII code : " + (int) ch);
        if (Character.isLetter(ch))
        {
            if (Character.isUpperCase(ch))
                System.out.println("Uppercase letter; lowercase form " + Character.toLowerCase(ch));
            else
                System.out.println("Lowercase letter; uppercase form " + Character.toUpperCase(ch));
        }
        else if (Character.isDigit(ch))
            System.out.println("Digit; its value doubled is " + (ch - '0') * 2);
        else
            System.out.println("Special character");
    }
}
```
Sample runs:
```
Enter a character: g
ASCII code : 103
Lowercase letter; uppercase form G
```
```
Enter a character: 7
ASCII code : 55
Digit; its value doubled is 14
```

**Q2.** Write a program to input a sentence and count its uppercase letters, lowercase letters, digits, spaces and special characters, using Character class methods.
**Answer:**
```java
import java.util.*;
class CountKinds
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine();
        int upper = 0, lower = 0, digit = 0, space = 0, special = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (Character.isUpperCase(ch))
                upper++;
            else if (Character.isLowerCase(ch))
                lower++;
            else if (Character.isDigit(ch))
                digit++;
            else if (Character.isWhitespace(ch))
                space++;
            else
                special++;
        }
        System.out.println("Uppercase letters  : " + upper);
        System.out.println("Lowercase letters  : " + lower);
        System.out.println("Digits             : " + digit);
        System.out.println("Spaces             : " + space);
        System.out.println("Special characters : " + special);
    }
}
```
Sample run:
```
Enter a sentence: Shillong 2026: Peak of ICSE!
Uppercase letters  : 6
Lowercase letters  : 12
Digits             : 4
Spaces             : 4
Special characters : 2
```

**Q3.** Write a program to input a sentence and change every uppercase letter to lowercase and every lowercase letter to uppercase, leaving other characters unchanged.
**Answer:**
```java
import java.util.*;
class ToggleCase
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word or sentence: ");
        String s = sc.nextLine();
        String t = "";
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (Character.isUpperCase(ch))
                t = t + Character.toLowerCase(ch);
            else if (Character.isLowerCase(ch))
                t = t + Character.toUpperCase(ch);
            else
                t = t + ch;
        }
        System.out.println("Toggled: " + t);
    }
}
```
Sample run:
```
Enter a word or sentence: Hello World 2026
Toggled: hELLO wORLD 2026
```

**Q4.** Define a class Caesar with a method char shift(char ch, int k) that moves a letter k places forward in the alphabet, wrapping round from z to a and keeping its case; other characters are returned unchanged. In main, input a message and print it coded with k = 3.
**Answer:**
```java
import java.util.*;
class Caesar
{
    char shift(char ch, int k)
    {
        if (Character.isUpperCase(ch))
            return (char) ('A' + (ch - 'A' + k) % 26);
        else if (Character.isLowerCase(ch))
            return (char) ('a' + (ch - 'a' + k) % 26);
        else
            return ch;
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        Caesar ob = new Caesar();
        System.out.print("Enter the message: ");
        String s = sc.nextLine();
        String code = "";
        for (int i = 0; i < s.length(); i++)
            code = code + ob.shift(s.charAt(i), 3);
        System.out.println("Coded: " + code);
    }
}
```
Sample run (x, y, z wrap round to a, b, c):
```
Enter the message: Attack at Dawn, xyz!
Coded: Dwwdfn dw Gdzq, abc!
```

**Q5.** Write a program to input a password and check whether it is strong: at least 8 characters with at least one uppercase letter, one lowercase letter, one digit and one special character. If it is weak, list what is missing.
**Answer:**
```java
import java.util.*;
class Password
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a password: ");
        String p = sc.nextLine();
        boolean up = false, low = false, dig = false, spec = false;
        for (int i = 0; i < p.length(); i++)
        {
            char ch = p.charAt(i);
            if (Character.isUpperCase(ch))
                up = true;
            else if (Character.isLowerCase(ch))
                low = true;
            else if (Character.isDigit(ch))
                dig = true;
            else if (!Character.isWhitespace(ch))
                spec = true;
        }
        if (p.length() >= 8 && up && low && dig && spec)
            System.out.println("Strong password");
        else
        {
            System.out.println("Weak password. Missing:");
            if (p.length() < 8) System.out.println("- at least 8 characters");
            if (!up) System.out.println("- an uppercase letter");
            if (!low) System.out.println("- a lowercase letter");
            if (!dig) System.out.println("- a digit");
            if (!spec) System.out.println("- a special character");
        }
    }
}
```
Sample runs:
```
Enter a password: Core9X@Shillong
Strong password
```
```
Enter a password: mango12
Weak password. Missing:
- at least 8 characters
- an uppercase letter
- a special character
```

**Q6.** Write a program that reads the quantity and price of two items as Strings, converts them with Integer.parseInt() and Double.parseDouble(), and prints the number of items, the total and the total as a String with Double.toString().
**Answer:**
```java
import java.util.*;
class PriceTotal
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter quantity and price of item 1: ");
        String q1 = sc.next(), p1 = sc.next();
        System.out.print("Enter quantity and price of item 2: ");
        String q2 = sc.next(), p2 = sc.next();
        int qty1 = Integer.parseInt(q1), qty2 = Integer.parseInt(q2);
        double pr1 = Double.parseDouble(p1), pr2 = Double.parseDouble(p2);
        double total = qty1 * pr1 + qty2 * pr2;
        System.out.println("Items  : " + (qty1 + qty2));
        System.out.println("Total  : " + total);
        System.out.println("As text: " + Double.toString(total) + " rupees");
    }
}
```
Sample run (3 × 45.50 + 2 × 120):
```
Enter quantity and price of item 1: 3 45.50
Enter quantity and price of item 2: 2 120
Items  : 5
Total  : 376.5
As text: 376.5 rupees
```

---

## 12. Competency / Application Questions

**Q1. (Text from a form)** A form sends the amount "1,250". Why does `Integer.parseInt("1,250")` fail, and what should the program do?
**Model answer:** The comma is not a digit, so a NumberFormatException occurs; remove the comma (or reject the input) before parsing.

**Q2. (Choose the method)** A mobile number arrives as the text "9436012345". Which method converts it to a number, and why not parseInt?
**Model answer:** `Long.parseLong()` — the value is larger than the int range (2147483647).

**Q3. (Spot the join)** `System.out.println("Total: " + a + b);` with a = 20 and b = 30 prints "Total: 2030". Fix it.
**Model answer:** `System.out.println("Total: " + (a + b));` prints Total: 50.

**Q4. (Classify)** Which Character method is true for a tab character? What do isLetterOrDigit() and isWhitespace() give for '#'?
**Model answer:** isWhitespace() is true for a tab; for '#', both isLetterOrDigit() and isWhitespace() are false.

**Q5. (Check a PIN)** How can a program check that a 4-character PIN contains only digits?
**Model answer:** Check that the length is 4 and that `Character.isDigit()` is true for every character in a loop.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** The Integer class can be used without an import statement.
**R:** It belongs to the default package java.lang.
**Answer:** (c)
**Explanation:** java.lang is imported automatically.

**Q2.**
**A:** `Character.toUpperCase('5')` returns '5'.
**R:** toUpperCase changes only letters.
**Answer:** (c)
**Explanation:** Other characters are returned unchanged.

**Q3.**
**A:** `Integer.parseInt("25.5")` returns 25.
**R:** parseInt converts a String of digits to an int.
**Answer:** (b)
**Explanation:** "25.5" causes a NumberFormatException.

**Q4.**
**A:** `Integer n = 25;` is autoboxing.
**R:** Java converts the primitive into a wrapper object automatically.
**Answer:** (c)
**Explanation:** No method call is written.

**Q5.**
**A:** `Character.isDigit()` returns a char.
**R:** isDigit() tests whether a character is a digit.
**Answer:** (b)
**Explanation:** It returns boolean.

**Q6.**
**A:** `"12" + "8"` gives "128".
**R:** + joins Strings.
**Answer:** (c)
**Explanation:** No addition takes place.

**Q7.**
**A:** The wrapper class of char is Character.
**R:** Wrapper classes belong to java.util.
**Answer:** (a)
**Explanation:** They belong to java.lang.

**Q8.**
**A:** `System.out.println(Character.toUpperCase('b') + 2);` prints 68.
**R:** Java is case sensitive.
**Answer:** (d)
**Explanation:** Both true; the reason is char + int giving int.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The canteen bill

> A canteen app reads the price "45.50" and the quantity "3" as Strings.

**(i)** Which method converts the price?
**Answer:** `Double.parseDouble()`.

**(ii)** Which method converts the quantity?
**Answer:** `Integer.parseInt()`.

**(iii)** What does `"45.50" + "3"` give?
**Answer:** "45.503".

**(iv)** What is the correct total?
**Answer:** 136.5.

### Case 2 — The password rule

> A strong password needs a capital, a small letter, a digit, a special character and 8 or more characters.

**(i)** Which method tests for a capital letter?
**Answer:** `Character.isUpperCase()`.

**(ii)** Which method tests for a digit?
**Answer:** `Character.isDigit()`.

**(iii)** Is "mango12" strong?
**Answer:** No — it is weak.

**(iv)** What is the return type of these testing methods?
**Answer:** boolean.

### Case 3 — The secret code

> Each letter is shifted 3 places forward, keeping its case; other characters stay the same.

**(i)** What does 'A' become?
**Answer:** 'D'.

**(ii)** What does 'z' become?
**Answer:** 'c'.

**(iii)** Which methods tell the case of a letter?
**Answer:** isUpperCase() and isLowerCase().

**(iv)** What does '!' become?
**Answer:** '!' — unchanged.

---

## 15. Revision Notes

### Chapter at a glance
- java.lang (String, Math, wrappers) is imported automatically; java.util (Scanner) needs import.
- Class = composite, user-defined type; primitive = one built-in value.
- Wrappers: Byte, Short, Integer, Long, Float, Double, Character, Boolean.
- parseInt / parseLong / parseDouble take a String; valueOf gives a wrapper object; toString / String.valueOf give a String.
- Character: isLetter, isDigit, isLetterOrDigit, isWhitespace, isUpperCase, isLowerCase → boolean; toUpperCase, toLowerCase → char; non-letters unchanged.
- char + int = int; `ch - '0'` = digit value.
- Boxing (primitive → object), unboxing (object → primitive), autoboxing (automatic).

### Common mistakes

| Mistake | Correct idea |
|---|---|
| `Integer.parseint`, `Double.Parsedouble` | Exact case: parseInt, parseDouble. |
| `Integer.parseInt(4578)` | The argument is a String: "4578". |
| `int y = Double.parseDouble(x);` | Store in a double. |
| Expecting 'D' from `toUpperCase('b') + 2` | It prints the int 68; cast to char for 'D'. |
| Wrapper of char written as Char | Character. |
| `"Total: " + a + b` | Bracket the sum: `(a + b)`. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 8: Library Classes**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** Character class methods are found in:
(a) java.util (b) java.io (c) java.lang (d) java.awt

**2.** The wrapper class for char:
(a) Character (b) Char (c) String (d) Letter

**3.** The type of parameter for parseInt():
(a) int (b) double (c) char (d) String

**4.** `System.out.println(Character.toUpperCase('b') + 2);` prints:
(a) 66 (b) 100 (c) 68 (d) 98

**5.** Converts "25" to 25.0:
(a) Double.parse("25") (b) Double.parseDouble("25") (c) Integer.parseInt("25") (d) Double.parseDouble(25)

**6.** Converting a primitive to an object of its wrapper class:
(a) unboxing (b) parsing (c) boxing (d) casting

**7.** `Character.isLetterOrDigit('#')` gives:
(a) true (b) false (c) # (d) 35

**8.** `Character.toLowerCase('1')` gives:
(a) 0 (b) A (c) true (d) 1

**9.** The return type of isWhitespace():
(a) char (b) int (c) boolean (d) String

**10.** Statement I: Unboxing converts a wrapper object to a primitive. Statement II: Autoboxing needs an explicit method call.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

### Part I — Short answers (5 × 2 = 10)

**11.** Differentiate between boxing and unboxing. [2]

**12.** Give the output: `String A = "26", B = "100"; String D = A + B + "200"; int d = Integer.parseInt(A) + Integer.parseInt(B); System.out.println("Result 1 = " + D); System.out.println("Result 2 = " + d);` [2]

**13.** Give the output: `char chr = Character.toLowerCase('B'); int n = (int) chr - 10; System.out.println((char) n + " " + chr);` [2]

**14.** Write one difference between isUpperCase() and toUpperCase(). [2]

**15.** Name the error and correct it: `String x = "25"; int y = Double.parseDouble(x);` [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Write a program to input a sentence and count the uppercase letters, lowercase letters, digits, spaces and special characters. [10]

**17.** Write a program to input a sentence and toggle the case of every letter. [10]

**18.** Write a program to check whether an input password is strong (8 or more characters, with an uppercase letter, a lowercase letter, a digit and a special character). [10]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | c | b | c | b | c | a | d |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | Double.parseDouble() | Integer.parseInt() | "45.503" | 136.5 |
| 2 | isUpperCase() | isDigit() | No (weak) | boolean |
| 3 | 'D' | 'c' | isUpperCase(), isLowerCase() | '!' |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | c | a | d | c | b | c | b | d | c | c |

**Part I, Q11–15 (2 marks each)**

**11.** Boxing: primitive → wrapper object (1); unboxing: wrapper object → primitive (1).
**12.** `Result 1 = 26100200` (1); `Result 2 = 126` (1).
**13.** `X b` (2).
**14.** isUpperCase checks and returns boolean (1); toUpperCase converts and returns char (1).
**15.** Syntax error, lossy conversion (1); `double y = Double.parseDouble(x);` (1).

**Part II (10 marks each)**

**16.–18.** Input with Scanner (2), loop over the characters with charAt (2), correct Character methods (3), counters or result built correctly (2), output (1).
