# String Handling II — String Programs

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 13 |
| Title | String Handling II — String Programs |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 8. String handling |
| Exam weightage | **Section B**: a String program in every paper since 2017 (15 marks) — counting kinds of characters, changing characters, working word by word, splitting and rejoining, or sorting a String array. |
| Syllabus scope | Programs based on the String methods; extracting and modifying characters of a String; alphabetical order of Strings in an array (bubble and selection sort); searching for a String by linear search. |
| In short | Learn to write Java programs that process text, changing characters, sorting words alphabetically and searching for a word in a list. |

> **Note on the text:** CISCE prescribes no textbook for ICSE Computer Applications; this chapter follows the ICSE 2027 syllabus in its own words. Its questions are the CISCE papers of 2017–2026 and the 2024 and 2025 specimens, answered from CISCE's marking schemes and examiners' comments where published. **Every program was compiled and run (Java 21).**
>
> **Exam note:** Read a sentence with **nextLine()** and a single word with **next()**. Loop with **i < s.length()** and take each character with **charAt(i)**; use **Character methods** when the question says so. Initialise counters **before** the loop and print **after** it. Print the messages **exactly** as the question words them.

---

## 1. Complete Lesson

### The toolkit of a String program

Almost every ICSE String program is built from a few steps:

```java
Scanner sc = new Scanner(System.in);
String s = sc.nextLine();             // a sentence (next() for one word)
s = s.toUpperCase();                  // normalise the case if the question allows
int count = 0;                        // counters before the loop
String t = "";                        // a new String is built from ""
for (int i = 0; i < s.length(); i++)
{
    char ch = s.charAt(i);            // one character at a time
    // test ch, count it, or add something to t
}
System.out.println(...);              // results after the loop
```

**Testing a character:**

| Test | Code |
|---|---|
| Letter / digit | `Character.isLetter(ch)` / `Character.isDigit(ch)` |
| Capital / small | `Character.isUpperCase(ch)` / `Character.isLowerCase(ch)` |
| Special character | `!Character.isLetterOrDigit(ch)` (spaces included, unless tested first) |
| Vowel | `"AEIOU".indexOf(ch) >= 0` after converting to uppercase, or `ch == 'A' \|\| ch == 'E' \|\| …` |
| Consonant | a letter that is not a vowel |
| Space | `ch == ' '` |

### Pattern 1 — counting

Count each kind of character in one pass. ICSE has asked for digits, alphabets and special characters (2023 Q6), uppercase versus lowercase letters (2025 Q5, the "Super String"), vowels versus consonants (2025 Improvement Q6, the "Special String") and vowels after converting to uppercase (2024 specimen Q5).

```java
for (int i = 0; i < s.length(); i++)
{
    char ch = s.charAt(i);
    if (Character.isUpperCase(ch))
        uc++;
    else if (Character.isLowerCase(ch))
        lc++;
}
if (uc == lc)
    System.out.println("String is a Super String");
```

The 2025 examiners noted counters initialised **inside** the loop, `if (uc = lc)` written for `if (uc == lc)`, range tests used where Character methods were required, and missing messages.

### Pattern 2 — changing each character

Build a **new String**, adding a changed character each time (Strings cannot be changed in place):

```java
String t = "";
for (int i = 0; i < s.length(); i++)
{
    char ch = s.charAt(i);
    if (Character.isLetter(ch))
    {
        if ("AEIOU".indexOf(ch) >= 0)
            t = t + (char) (ch + 1);      // vowel: next character
        else
            t = t + (char) (ch - 1);      // consonant: previous character
    }
    else
        t = t + ch;                       // others unchanged
}
```

This is ICSE 2025 specimen Q5: "#IMAGINATION@2024" becomes "#JLBFJMBSJPM@2024". The cast `(char)` is needed because `ch + 1` is an int.

### Pattern 3 — reversing

`r = r + s.charAt(i);` with i running **backwards** from `s.length() - 1` to 0, or `r = s.charAt(i) + r;` with i running forwards, gives the reverse ("Meghalaya" → "ayalahgeM"). ICSE 2026 Improvement Q6 reverses all but the first letter after coding it as @ or #.

### Pattern 4 — word by word

![Fig. 13.1 Extracting the words of a sentence, one character at a time](figures/ca_ch13_fig01_extract_words.png)

**Adding a space at the end** makes the last word end like the others. Collect letters into `word`; at each space, use the word and reset it:

```java
s = s + " ";
String word = "";
for (int i = 0; i < s.length(); i++)
{
    char ch = s.charAt(i);
    if (ch != ' ')
        word = word + ch;
    else
    {
        System.out.println(word);      // or count it, test it, reverse it ...
        word = "";
    }
}
```

Other word tasks need only the character **before** each position:
- **First letter of each word** — position 0, or any position after a space: `i == 0 || s.charAt(i - 1) == ' '` (2018 Q6, capitalising; 2019 Q8, counting words that start with A).
- **Number of words** in a sentence with single spaces — the number of spaces + 1.

The 2018 examiners noted `ch.toUpperCase()` (a char has no methods — use `Character.toUpperCase(ch)`) and `(ch + 1)` where `charAt(i + 1)` was meant.

### Pattern 5 — splitting and rejoining

![Fig. 13.2 Splitting a word at a position and joining the parts in a new order](figures/ca_ch13_fig02_split_rejoin.png)

Find a position with a loop or indexOf, cut with substring, and join in the new order:
- **Symbolic word** (2026 Q8): split at the first consonant — AIRWAYS → RWAYS + AI + TR.
- **Gmail check** (2024 Q8): split at '@' and at the last '.' — the parts must be "gmail" and "com".
- **Pig Latin**: split at the first vowel and add "AY" — TROUBLE → OUBLETRAY.

### Pattern 6 — String arrays: sort and search

The syllabus asks for **alphabetical order** of Strings in an array by **bubble** or **selection** sort, and **linear search** for a String. The array programs of Chapter 10 work unchanged, with two replacements:
- compare with **compareTo()** instead of < or >: `if (n[j].compareTo(n[j + 1]) > 0)` swaps for ascending order;
- test equality with **equals()** (or equalsIgnoreCase()) instead of ==.

Capitals sort before small letters ("aiom".compareTo("Rida") is 15, so aiom comes after Rida); keep the case consistent, or use compareToIgnoreCase(), when names are typed in mixed case.

### Summary of the chapter

- **Toolkit** — nextLine/next, toUpperCase, a loop with charAt, counters before and output after the loop.
- **Counting** — Character methods or vowel tests; compare counts at the end.
- **Changing** — build a new String from ""; cast `(char)` after arithmetic.
- **Reversing** — loop backwards, or add each character in front.
- **Words** — add a space at the end; collect letters; act at each space.
- **Split and rejoin** — indexOf or a loop to find the cut; substring to cut.
- **String arrays** — compareTo for order, equals for search.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Write the standard loop over the characters of a String and test each character.
2. Count letters, digits, special characters, cases, vowels and consonants.
3. Build new Strings by changing, shifting or reversing characters.
4. Process a sentence word by word: extract, count, capitalise and test words.
5. Split a String at a position and rejoin the parts.
6. Sort a String array alphabetically and search it for a String.

---

## 3. Detailed Section Explanations

### Section 1 — One character at a time
Every String program is a loop that looks at charAt(i) for each i.

### Section 2 — Count, change or collect
Inside the loop you either count the character, add a changed version to a new String, or collect it into a word.

### Section 3 — Words end at spaces
A space marks the end of a word; one extra space at the end catches the last word.

### Section 4 — Order by compareTo
String arrays use the same sorts as number arrays, comparing with compareTo().

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Traversal | Visiting each character of a String in turn. |
| Counter | A variable increased each time a condition is met. |
| Accumulator String | A String built up from "" inside a loop. |
| Vowel test | Checking whether a character is A, E, I, O or U. |
| Special character | A character that is neither a letter nor a digit. |
| Word extraction | Collecting the characters of each word between spaces. |
| Title case | The first letter of every word in capitals. |
| Palindrome | A word that reads the same backwards. |
| Acronym | A word formed from the first letters of other words. |
| Alphabetical (lexicographic) order | Dictionary order, decided by compareTo(). |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| "KAPILDEV@83" | 8 alphabets, 2 digits, 1 special character |
| "COmmITmeNt" | 5 uppercase, 5 lowercase: a Super String |
| "MINE" | 2 vowels, 2 consonants: a Special String |
| "robotics" in uppercase | ROBOTICS, 3 vowels |
| "#IMAGINATION@2024" coded | #JLBFJMBSJPM@2024 |
| AIRWAYS / BEAUTY symbolic | RWAYSAITR / BEAUTYTR |
| APPEARANCE6 / PERFORM encoded | @6ECNARAEPP / #MROFRE |
| Words starting with A in the 2019 sentence | 4 |
| Vowel test after toUpperCase() | "AEIOU".indexOf(ch) >= 0 |
| Compare Strings in a sort | compareTo(); equality: equals() |

### 5.2 Memory aids

- **"Take, Test, Tally"** — take charAt(i), test it, tally or build.
- **"Space at the end catches the last word."**
- **"Strings sort with compareTo, search with equals."**

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- Java's `split(" ")` returns the words of a sentence as an array in one call.
- Building a long String with + inside a loop is slow for huge texts; StringBuilder is used then.
- Spell-checkers, search engines and plagiarism checkers are large-scale String programs.

---

## 6. Person Profiles

### 6.1 Ralph Griswold (1934–2006)
An American computer scientist who, with David Farber and Ivan Polonsky at Bell Labs in the 1960s, created SNOBOL, one of the first programming languages designed for processing strings of text, and later the Icon language.

### 6.2 Douglas McIlroy (born 1932)
An American computer scientist at Bell Labs who invented Unix pipes and, with James Hunt, the diff program that compares two texts line by line — text processing that every programmer still uses.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Small steps, big results** — a loop of simple character tests solves most text problems.
- **Build, don't change** — new Strings are assembled piece by piece.
- **Words are found, not given** — spaces mark where words begin and end.

### 7.2 Real-life connections
- **Messaging apps** count characters, capitalise the first letter of a sentence and detect links.
- **Meghalaya:** a school's register prints names in title case ("Kong Wanda Nongrum") and sorts them alphabetically.
- **E-mail sign-ups** check an address's parts — the idea behind ICSE 2024 Q8.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section B** (60 marks, any four of six programs) has had a String program in every paper since 2017, worth 15 marks — counting, changing, word-by-word processing, splitting, or sorting a String array.

### 8.1 Graded exercises — solutions

#### Exercise 13A — Building blocks

**Q1.** Write the test for "ch is a vowel" when s has been converted to uppercase.
**Answer:** `"AEIOU".indexOf(ch) >= 0`

**Q2.** Write a loop that builds r, the reverse of s.
**Answer:** `for (int i = s.length() - 1; i >= 0; i--) r = r + s.charAt(i);`

**Q3.** Why is a space added at the end of a sentence before extracting words?
**Answer:** So that the last word is also followed by a space and is handled like the others.

**Q4.** Why does `char c = ch + 1;` not compile, and what is the fix?
**Answer:** ch + 1 is an int; write `char c = (char) (ch + 1);`.

**Q5.** Write the condition for "the character at i is the first letter of a word".
**Answer:** `i == 0 || s.charAt(i - 1) == ' '`

#### Exercise 13B — Tracing

**Q6.** What does the reversing loop give for "Meghalaya"?
**Answer:** "ayalahgeM".

**Q7.** For "COMPUTER", how many vowels and consonants are there?
**Answer:** 3 vowels (O, U, E) and 5 consonants.

**Q8.** What does toggling the case of every letter give for "aBc1"?
**Answer:** "AbC1" — the digit is unchanged.

**Q9.** How many words has "we are in cyber world" (single spaces)?
**Answer:** 5 — four spaces + 1.

**Q10.** What is `"ABC"` after each character is replaced by `(char) (ch + 1)`?
**Answer:** "BCD".
### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q8 (15 marks) | Write a program to accept a word and print the Symbolic of the accepted word. A Symbolic word is formed by extracting the characters from the first consonant, then adding the characters before the first consonant of the accepted word, and ending with "TR". Example: AIRWAYS — Symbolic word is RWAYSAITR; BEAUTY — Symbolic word is BEAUTYTR. |
| ICSE 2026 Improvement, Q5 (15 marks) | Define a class to accept the names of 10 students in an array, arrange the names in alphabetical order using the BUBBLE SORT method, and print the original array and the sorted array. |
| ICSE 2026 Improvement, Q6 (15 marks) | A secret agency encodes the given message (String) as follows: the first letter of the message is converted to @ if it is a vowel, otherwise it is converted to #; all the other letters are reversed. Print the original String and the encoded string. Example: S = "APPEARANCE6", Encoded String: @6ECNARAEPP; S = "PERFORM", Encoded String: #MROFRE. |
| ICSE 2025, Q5 (15 marks) | Define a class to accept a String and print if it is a Super string or not. A String is Super if the number of uppercase letters is equal to the number of lowercase letters. [Use Character and String methods only] Example: "COmmITmeNt" — Number of Uppercase letters – 5, Number of Lowercase letters – 5, String is a Super String. |
| ICSE 2025 Improvement, Q6 (15 marks) | Define a class to accept a string. Check if it is a Special String or not. A String is Special if the number of vowels equals the number of consonants. Example: MINE — Number of vowels = 2, Number of Consonants = 2. |
| ICSE 2025 specimen, Q5 (15 marks) | Define a class to accept a string and convert the same to uppercase; create and display the new string by replacing each vowel by the immediate next character and every consonant by the previous character. The other characters remain the same. Example: Input: #IMAGINATION@2024, Output: #JLBFJMBSJPM@2024. |
| ICSE 2024, Q8 (15 marks) | Define a class to accept the gmail id and check for its validity. A gmail id is valid only if it has: @, . (dot), gmail, com. Example: icse2024@gmail.com is a valid gmail id. |
| ICSE 2024 specimen, Q5 (15 marks) | Define a class to accept a string and convert it into uppercase. Count and display the number of vowels in it. Input: robotics; Output: ROBOTICS, Number of vowels: 3. |
| ICSE 2023, Q6 (15 marks) | Define a class to accept a String and print the number of digits, alphabets and special characters in the string. Example: S = "KAPILDEV@83"; Output: Number of digits – 2, Number of Alphabets – 8, Number of Special characters – 1. |
| ICSE 2020, Q6 (15 marks) | Write a program to input a sentence and convert it into uppercase and display each word in a separate line. Example: Input: India is my country; Output: INDIA / IS / MY / COUNTRY (one word per line). |
| ICSE 2019, Q8 (15 marks) | Write a program to input a sentence and convert it into uppercase and count and display the total number of words starting with a letter 'A'. Example: Sample Input: ADVANCEMENT AND APPLICATION OF INFORMATION TECHNOLOGY ARE EVER CHANGING. Sample Output: Total number of words starting with letter 'A' = 4. |
| ICSE 2018, Q6 (15 marks) | Write a program in Java to accept a string in lower case and change the first letter of every word to upper case. Display the new string. Sample input: we are in cyber world; Sample output: We Are In Cyber World. |
| ICSE 2017, Q9 (15 marks) | Write a program to input forty words in an array. Arrange these words in descending order of alphabets, using selection sort technique. Print the sorted array. |

**Solutions**

**2026 Q8.** The loop stops at the first letter that is not a vowel; substring then cuts the word there:
```java
import java.util.*;
class Symbolic
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String w = sc.next().toUpperCase();
        int i;
        for (i = 0; i < w.length(); i++)
        {
            char ch = w.charAt(i);
            if (Character.isLetter(ch) && "AEIOU".indexOf(ch) == -1)
                break;                      // first consonant found
        }
        String sym = w.substring(i) + w.substring(0, i) + "TR";
        System.out.println("Symbolic word is " + sym);
    }
}
```
Sample runs:
```
Enter a word: AIRWAYS
Symbolic word is RWAYSAITR
```
```
Enter a word: BEAUTY
Symbolic word is BEAUTYTR
```
For BEAUTY the first consonant is at index 0, so `substring(0, 0)` is empty. *(Worked answer.)*

**2026 Improvement Q5.** Bubble sort with compareTo(); a copy keeps the original order for printing:
```java
import java.util.*;
class NameBubble
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String n[] = new String[10];
        String orig[] = new String[10];
        System.out.println("Enter 10 names:");
        for (int i = 0; i < 10; i++)
        {
            n[i] = sc.nextLine();
            orig[i] = n[i];
        }
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9 - i; j++)
            {
                if (n[j].compareTo(n[j + 1]) > 0)
                {
                    String t = n[j];
                    n[j] = n[j + 1];
                    n[j + 1] = t;
                }
            }
        }
        System.out.println("Original array:");
        for (int i = 0; i < 10; i++)
            System.out.print(orig[i] + "  ");
        System.out.println();
        System.out.println("Sorted array:");
        for (int i = 0; i < 10; i++)
            System.out.print(n[i] + "  ");
        System.out.println();
    }
}
```
Sample run (the ten names typed one per line):
```
Enter 10 names:
Wanda
Ibapynshai
Daphi
Banri
Rida
Kitbor
Aiom
Mebanshan
Saphira
Careen
Original array:
Wanda  Ibapynshai  Daphi  Banri  Rida  Kitbor  Aiom  Mebanshan  Saphira  Careen
Sorted array:
Aiom  Banri  Careen  Daphi  Ibapynshai  Kitbor  Mebanshan  Rida  Saphira  Wanda
```
*(Worked answer.)*

**2026 Improvement Q6.**
```java
import java.util.*;
class SecretCode
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the message: ");
        String s = sc.nextLine();
        char first = Character.toUpperCase(s.charAt(0));
        String code;
        if ("AEIOU".indexOf(first) >= 0)
            code = "@";
        else
            code = "#";
        for (int i = s.length() - 1; i >= 1; i--)
            code = code + s.charAt(i);
        System.out.println("Original String : " + s);
        System.out.println("Encoded String  : " + code);
    }
}
```
Sample runs:
```
Enter the message: APPEARANCE6
Original String : APPEARANCE6
Encoded String  : @6ECNARAEPP
```
```
Enter the message: PERFORM
Original String : PERFORM
Encoded String  : #MROFRE
```
*(Worked answer.)*

**2025 Q5.** As in the marking scheme, with Character methods for the two counts. The scheme reads one word with next(); nextLine() also allows spaces:
```java
import java.util.*;
class SuperString
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String: ");
        String s = sc.nextLine();
        int uc = 0, lc = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (Character.isUpperCase(ch))
                uc++;
            else if (Character.isLowerCase(ch))
                lc++;
        }
        System.out.println("Number of Uppercase letters - " + uc);
        System.out.println("Number of Lowercase letters - " + lc);
        if (uc == lc)
            System.out.println("String is a Super String");
        else
            System.out.println("String is not a Super String");
    }
}
```
Sample run:
```
Enter a String: COmmITmeNt
Number of Uppercase letters - 5
Number of Lowercase letters - 5
String is a Super String
```
The examiners noted these errors: Character methods not used, counters initialised inside the loop, the String initialised instead of accepted, length() missed, `if (uc = lc)` written for `if (uc == lc)`, and messages not printed.

**2025 Improvement Q6.** Consonants are letters that are not vowels, so digits and symbols are not counted:
```java
import java.util.*;
class SpecialString
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String: ");
        String s = sc.nextLine().toUpperCase();
        int v = 0, c = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (Character.isLetter(ch))
            {
                if ("AEIOU".indexOf(ch) >= 0)
                    v++;
                else
                    c++;
            }
        }
        System.out.println("Number of vowels = " + v);
        System.out.println("Number of Consonants = " + c);
        if (v == c)
            System.out.println("Special String");
        else
            System.out.println("Not a Special String");
    }
}
```
Sample runs:
```
Enter a String: MINE
Number of vowels = 2
Number of Consonants = 2
Special String
```
```
Enter a String: SHILLONG
Number of vowels = 2
Number of Consonants = 6
Not a Special String
```
*(Worked answer.)*

**2025 specimen Q5.** As in the draft scheme:
```java
import java.util.*;
class VowelShift
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input : ");
        String s = sc.nextLine().toUpperCase();
        String t = "";
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (Character.isLetter(ch))
            {
                if ("AEIOU".indexOf(ch) >= 0)
                    t = t + (char) (ch + 1);
                else
                    t = t + (char) (ch - 1);
            }
            else
                t = t + ch;
        }
        System.out.println("Output : " + t);
    }
}
```
Sample run:
```
Input : #IMAGINATION@2024
Output : #JLBFJMBSJPM@2024
```

**2024 Q8.** The scheme splits the id at '@' and at the first '.', and checks that the parts are "gmail" and "com". With the first dot, an id such as first.last@gmail.com (a dot before the @) makes `substring(p + 1, q)` fail with StringIndexOutOfBoundsException; the version below uses the **last** dot and also checks that there is exactly one @:
```java
import java.util.*;
class GmailCheck
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the gmail id: ");
        String s = sc.nextLine().trim();
        int p = s.indexOf('@');
        int q = s.lastIndexOf('.');
        if (p <= 0 || p != s.lastIndexOf('@'))
            System.out.println("Invalid - there must be one @ after the user name");
        else if (q < p)
            System.out.println("Invalid - no . after @");
        else if (!s.substring(p + 1, q).equalsIgnoreCase("gmail"))
            System.out.println("Invalid - no gmail");
        else if (!s.substring(q + 1).equalsIgnoreCase("com"))
            System.out.println("Invalid - no com");
        else
            System.out.println("Valid gmail id");
    }
}
```
Sample runs:
```
Enter the gmail id: icse2024@gmail.com
Valid gmail id
```
```
Enter the gmail id: first.last@gmail.com
Valid gmail id
```
```
Enter the gmail id: kong@yahoo.com
Invalid - no gmail
```
```
Enter the gmail id: icse2024gmail.com
Invalid - there must be one @ after the user name
```
The examiners noted that this pattern was asked for the first time and that marks were also given to candidates who checked that the id ends with "@gmail.com" — `s.endsWith("@gmail.com")` is a valid short answer.

**2024 specimen Q5.**
```java
import java.util.*;
class VowelCount
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input: ");
        String s = sc.nextLine().toUpperCase();
        int v = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U')
                v++;
        }
        System.out.println("Output: " + s);
        System.out.println("Number of vowels: " + v);
    }
}
```
Sample run:
```
Input: robotics
Output: ROBOTICS
Number of vowels: 3
```
*(Worked answer.)*

**2023 Q6.** As in the scheme, Character methods sort each character into one of three kinds:
```java
import java.util.*;
class CharTypes
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String: ");
        String s = sc.nextLine();
        int d = 0, a = 0, sp = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (Character.isDigit(ch))
                d++;
            else if (Character.isLetter(ch))
                a++;
            else
                sp++;
        }
        System.out.println("Number of digits - " + d);
        System.out.println("Number of Alphabets - " + a);
        System.out.println("Number of Special characters - " + sp);
    }
}
```
Sample run:
```
Enter a String: KAPILDEV@83
Number of digits - 2
Number of Alphabets - 8
Number of Special characters - 1
```
The examiners noted these errors: characters not extracted, Character methods misused, wrong range checks, and the count printed inside the loop.

**2020 Q6.** A space added at the end lets the last word be printed like the others:
```java
import java.util.*;
class WordsPerLine
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input : ");
        String s = sc.nextLine().trim().toUpperCase() + " ";
        String word = "";
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (ch != ' ')
                word = word + ch;
            else if (word.length() > 0)
            {
                System.out.println(word);
                word = "";
            }
        }
    }
}
```
Sample run:
```
Input : India is my country
INDIA
IS
MY
COUNTRY
```
*(Worked answer.)*

**2019 Q8.** A word starts with 'A' at index 0 or just after a space (the scheme compares each character with the next):
```java
import java.util.*;
class CountA
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine().toUpperCase();
        int c = 0;
        if (s.length() > 0 && s.charAt(0) == 'A')
            c++;
        for (int i = 1; i < s.length(); i++)
        {
            if (s.charAt(i - 1) == ' ' && s.charAt(i) == 'A')
                c++;
        }
        System.out.println("Total number of words starting with letter 'A' = " + c);
    }
}
```
Sample run:
```
Enter a sentence: ADVANCEMENT AND APPLICATION OF INFORMATION TECHNOLOGY ARE EVER CHANGING.
Total number of words starting with letter 'A' = 4
```

**2018 Q6.** The scheme adds a space at the front and capitalises the character after each space; checking `i == 0` or the character before does the same:
```java
import java.util.*;
class TitleCase
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence in lower case: ");
        String s = sc.nextLine();
        String t = "";
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (i == 0 || s.charAt(i - 1) == ' ')
                t = t + Character.toUpperCase(ch);
            else
                t = t + ch;
        }
        System.out.println(t);
    }
}
```
Sample run:
```
Enter a sentence in lower case: we are in cyber world
We Are In Cyber World
```
The examiners noted that most candidates could not answer it, writing `ch.toUpperCase()` (a char has no methods) or `(ch + 1)` instead of the next character.

**2017 Q9.** Selection sort looking for the **largest** String each pass gives descending order:
```java
import java.util.*;
class WordsDesc
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String w[] = new String[40];
        System.out.println("Enter 40 words:");
        for (int i = 0; i < 40; i++)
            w[i] = sc.next();
        for (int i = 0; i < 39; i++)
        {
            int max = i;
            for (int j = i + 1; j < 40; j++)
            {
                if (w[j].compareTo(w[max]) > 0)
                    max = j;
            }
            String t = w[i];
            w[i] = w[max];
            w[max] = t;
        }
        System.out.println("Words in descending order:");
        for (int i = 0; i < 40; i++)
        {
            System.out.print(w[i] + " ");
            if ((i + 1) % 10 == 0)
                System.out.println();
        }
    }
}
```
Sample run (40 words typed in four lines):
```
Enter 40 words:
river hill mango cloud orange forest pine stone rain lake
bridge market school garden temple valley tiger eagle honey bamboo
paddy orchid monsoon village festival music dance story friend window
candle silver golden ladder rocket planet comet harbor island meadow
Words in descending order:
window village valley tiger temple story stone silver school rocket
river rain planet pine paddy orchid orange music monsoon meadow
market mango lake ladder island honey hill harbor golden garden
friend forest festival eagle dance comet cloud candle bridge bamboo
```
*(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) What does the loop `for (int i = 0; i < s.length(); i++) t = s.charAt(i) + t;` build from s = "Meghalaya"?
**Answer:** "ayalahgeM" — each character is added in front.

**Q2.** (2 marks) Give the number of special characters in "KAPILDEV@83" counted by `!Character.isLetterOrDigit(ch)`.
**Answer:** 1 — the @.

**Q3.** (2 marks) Why does "aiom" come after "Rida" when names are sorted with compareTo()?
**Answer:** 'a' (97) is greater than 'R' (82); "aiom".compareTo("Rida") is 15. Use the same case for all names, or compareToIgnoreCase().

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 15 marks | Count kinds of characters and compare counts (Super, Special) | 8.2, Section 11 |
| 15 marks | Change characters by a rule (shift, code, reverse) | 8.2 |
| 15 marks | Word by word: each word on a line, title case, words starting with a letter | 8.2, Section 11 |
| 15 marks | Sort names alphabetically (bubble/selection) or search a name | 8.2, Section 11 |

---
## 9. MCQs with Explanations

### The String-program toolkit (Q1–Q14)

**Q1.** To read a sentence with spaces, use
- (a) sc.nextWord()
- (b) sc.next()
- (c) sc.nextInt()
- (d) sc.nextLine()

**Answer:** (d) sc.nextLine()
**Explanation:** next() reads one word.

**Q2.** The loop that visits every character of s is
- (a) for (int i = 1; i <= s.length(); i++)
- (b) for (int i = 0; i < s.length(); i++)
- (c) for (int i = 0; i <= s.length(); i++)
- (d) for (int i = 0; i < s.length; i++)

**Answer:** (b) for (int i = 0; i < s.length(); i++)
**Explanation:** Indexes 0 to length() − 1.

**Q3.** Inside the loop, the character at position i is
- (a) s.substring(i)
- (b) s[i]
- (c) s.char(i)
- (d) s.charAt(i)

**Answer:** (d) s.charAt(i)
**Explanation:** charAt returns a char.

**Q4.** A new String built inside a loop should start as
- (a) null
- (b) ""
- (c) " "
- (d) 0

**Answer:** (b) ""
**Explanation:** The empty String.

**Q5.** Counters in a String program should be set to 0
- (a) never
- (b) inside the loop
- (c) after the loop
- (d) before the loop

**Answer:** (d) before the loop
**Explanation:** Otherwise they restart for each character.

**Q6.** The results of a counting program are printed
- (a) after the loop
- (b) inside the loop for each character
- (c) before the loop
- (d) only for the last character

**Answer:** (a) after the loop
**Explanation:** Once the counting is complete.

**Q7.** char c = ch + 1; does not compile because
- (a) ch + 1 is an int
- (b) ch is a String
- (c) + cannot be used with char
- (d) c must be final

**Answer:** (a) ch + 1 is an int
**Explanation:** Write (char) (ch + 1).

**Q8.** ch.toUpperCase() for a char ch gives
- (a) the capital letter
- (b) a compile error — a char has no methods
- (c) a String
- (d) the code of ch

**Answer:** (b) a compile error — a char has no methods
**Explanation:** Use Character.toUpperCase(ch).

**Q9.** A vowel test after converting to uppercase is
- (a) ch == "AEIOU"
- (b) "AEIOU".indexOf(ch) == -1
- (c) "AEIOU".indexOf(ch) >= 0
- (d) Character.isVowel(ch)

**Answer:** (c) "AEIOU".indexOf(ch) >= 0
**Explanation:** indexOf finds ch in the vowel list.

**Q10.** A consonant is a character that is
- (a) a space
- (b) any non-vowel
- (c) a digit
- (d) a letter but not a vowel

**Answer:** (d) a letter but not a vowel
**Explanation:** Digits and symbols are not consonants.

**Q11.** A special character is one for which
- (a) Character.isDigit(ch) is true
- (b) Character.isLetter(ch) is true
- (c) !Character.isLetterOrDigit(ch) is true
- (d) ch == 'A'

**Answer:** (c) !Character.isLetterOrDigit(ch) is true
**Explanation:** Neither a letter nor a digit.

**Q12.** In "if (uc = lc)", the error is
- (a) if cannot compare ints
- (b) uc must be a String
- (c) = is assignment; == is needed for comparison
- (d) there is no error

**Answer:** (c) = is assignment; == is needed for comparison
**Explanation:** An examiners' note from 2025.

**Q13.** When a question says "use Character and String methods only", a capital letter is tested with
- (a) ch >= 'A' && ch <= 'Z'
- (b) Character.isUpperCase(ch)
- (c) ch.isUpper()
- (d) s.toUpperCase()

**Answer:** (b) Character.isUpperCase(ch)
**Explanation:** Range tests lose marks then.

**Q14.** Converting s to uppercase before counting vowels
- (a) removes the spaces
- (b) changes the number of vowels
- (c) is not allowed
- (d) means only "AEIOU" needs checking

**Answer:** (d) means only "AEIOU" needs checking
**Explanation:** Small vowels become capitals.

### Counting programs (Q15–Q28)

**Q15.** "KAPILDEV@83" has how many alphabets, digits and special characters?
- (a) 8, 2, 1
- (b) 7, 2, 2
- (c) 8, 3, 0
- (d) 9, 2, 0

**Answer:** (a) 8, 2, 1
**Explanation:** KAPILDEV, 83 and @.

**Q16.** "COmmITmeNt" has how many uppercase and lowercase letters?
- (a) 6 and 4
- (b) 4 and 6
- (c) 5 and 5
- (d) 10 and 0

**Answer:** (c) 5 and 5
**Explanation:** C O I T N and m m m e t.

**Q17.** A String is a Super String (ICSE 2025) when
- (a) it is a palindrome
- (b) all letters are capitals
- (c) vowels equal consonants
- (d) uppercase letters equal lowercase letters in number

**Answer:** (d) uppercase letters equal lowercase letters in number
**Explanation:** "COmmITmeNt" is one.

**Q18.** A String is a Special String (ICSE 2025 Improvement) when
- (a) it has a special character
- (b) vowels equal consonants in number
- (c) uppercase equals lowercase
- (d) it has an even length

**Answer:** (b) vowels equal consonants in number
**Explanation:** MINE: 2 and 2.

**Q19.** "SHILLONG" has how many vowels and consonants?
- (a) 3 and 5
- (b) 2 and 6
- (c) 1 and 7
- (d) 2 and 5

**Answer:** (b) 2 and 6
**Explanation:** I and O are the vowels.

**Q20.** "ROBOTICS" has how many vowels?
- (a) 3
- (b) 2
- (c) 4
- (d) 5

**Answer:** (a) 3
**Explanation:** O, O, I.

**Q21.** "COMPUTER" has how many consonants?
- (a) 4
- (b) 3
- (c) 8
- (d) 5

**Answer:** (d) 5
**Explanation:** 8 letters − 3 vowels.

**Q22.** The number of times 'a' occurs in "banana" is
- (a) 3
- (b) 2
- (c) 1
- (d) 6

**Answer:** (a) 3
**Explanation:** b a n a n a.

**Q23.** In "Education is the most powerful weapon", the number of E's (case ignored) is
- (a) 3
- (b) 4
- (c) 5
- (d) 2

**Answer:** (b) 4
**Explanation:** Education, the, powerful, weapon.

**Q24.** The 2023 examiners noted that some candidates printed the counts
- (a) with Character methods
- (b) after the loop
- (c) inside the loop
- (d) with a Scanner

**Answer:** (c) inside the loop
**Explanation:** The counts were printed many times.

**Q25.** In a counting program, else if is used because
- (a) if cannot be repeated
- (b) each character belongs to only one kind
- (c) Java needs else after every if
- (d) it makes the loop faster than for

**Answer:** (b) each character belongs to only one kind
**Explanation:** Once a kind matches, the rest are skipped.

**Q26.** For a sentence with single spaces between words, the number of words is
- (a) the number of spaces + 1
- (b) the number of spaces
- (c) the length of the sentence
- (d) the number of vowels

**Answer:** (a) the number of spaces + 1
**Explanation:** "we are in cyber world": 4 + 1.

**Q27.** The number of words in "we are in cyber world" is
- (a) 4
- (b) 5
- (c) 21
- (d) 6

**Answer:** (b) 5
**Explanation:** Four spaces.

**Q28.** Words starting with 'A' in "ADVANCEMENT AND APPLICATION OF INFORMATION TECHNOLOGY ARE EVER CHANGING." number
- (a) 3
- (b) 4
- (c) 5
- (d) 2

**Answer:** (b) 4
**Explanation:** ADVANCEMENT, AND, APPLICATION, ARE.

### Changing and reversing (Q29–Q42)

**Q29.** The reverse of "Meghalaya" is
- (a) aMeghalay
- (b) Meghalaya
- (c) ayalahge
- (d) ayalahgeM

**Answer:** (d) ayalahgeM
**Explanation:** The capital M comes last.

**Q30.** The loop for (i = 0; i < s.length(); i++) t = s.charAt(i) + t; builds
- (a) the reverse of s
- (b) a copy of s
- (c) s in uppercase
- (d) an empty String

**Answer:** (a) the reverse of s
**Explanation:** Each character goes in front.

**Q31.** "PERFORM" encoded by the 2026 secret-agency rule is
- (a) #MROFRE
- (b) @MROFRE
- (c) #ERFORM
- (d) MROFREP

**Answer:** (a) #MROFRE
**Explanation:** P is a consonant: #, then ERFORM reversed.

**Q32.** "APPEARANCE6" encoded by the same rule is
- (a) @PPEARANCE6
- (b) #6ECNARAEPP
- (c) @6ECNARAEPP
- (d) 6ECNARAEPPA

**Answer:** (c) @6ECNARAEPP
**Explanation:** A is a vowel: @.

**Q33.** "#IMAGINATION@2024" with each vowel moved forward and each consonant back gives
- (a) #IMAGINATION@2024
- (b) #HNBHHOBUHNO@2024
- (c) #JLBFJMBSJPM@3135
- (d) #JLBFJMBSJPM@2024

**Answer:** (d) #JLBFJMBSJPM@2024
**Explanation:** Other characters stay the same.

**Q34.** Toggling the case of every letter of "aBc1" gives
- (a) 1CbA
- (b) AbC2
- (c) AbC1
- (d) bCa1

**Answer:** (c) AbC1
**Explanation:** The digit is unchanged.

**Q35.** Replacing every character of "ABC" by (char) (ch + 1) gives
- (a) 666768
- (b) ABC
- (c) BCD
- (d) ZAB

**Answer:** (c) BCD
**Explanation:** Each letter moves forward one.

**Q36.** Taking the characters of "HELLO" at i = 0, 2, 4 gives
- (a) LLO
- (b) ELL
- (c) HEL
- (d) HLO

**Answer:** (d) HLO
**Explanation:** Every second character.

**Q37.** "banana".replace('a', '*') is
- (a) `b*n*n*`
- (b) `banana`
- (c) `b*nana`
- (d) `*b*n*n`

**Answer:** (a) `b*n*n*`
**Explanation:** Every a is replaced.

**Q38.** "we are in cyber world" in title case is
- (a) We-Are-In-Cyber-World
- (b) We Are In Cyber
- (c) W A I C W
- (d) We Are In Cyber World

**Answer:** (d) We Are In Cyber World
**Explanation:** First letter of each word.

**Q39.** The character at i is the first letter of a word when
- (a) i == 0 || s.charAt(i - 1) == ' '
- (b) s.charAt(i) == ' '
- (c) i == s.length() - 1
- (d) s.charAt(i + 1) == ' '

**Answer:** (a) i == 0 || s.charAt(i - 1) == ' '
**Explanation:** At the start, or after a space.

**Q40.** A palindrome check for "level" compares
- (a) charAt(i) with charAt(i + 1)
- (b) charAt(i) with charAt(length() − 1 − i)
- (c) the word with its uppercase form
- (d) the first and second halves' lengths

**Answer:** (b) charAt(i) with charAt(length() − 1 − i)
**Explanation:** Matching pairs from both ends.

**Q41.** Comparing a word with its reverse using equalsIgnoreCase(), "Malayalam" is
- (a) an error
- (b) not a palindrome
- (c) a palindrome
- (d) empty

**Answer:** (c) a palindrome
**Explanation:** Case is ignored.

**Q42.** In "PERFORM", g.substring(1) + " " + g.charAt(0) is
- (a) P ERFORM
- (b) PERFORM P
- (c) ERFOR M
- (d) ERFORM P

**Answer:** (d) ERFORM P
**Explanation:** All but the first, then the first.

### Words (Q43–Q58)

**Q43.** A space is added at the end of a sentence before extracting words so that
- (a) the first word is skipped
- (b) the sentence is longer
- (c) the last word is also followed by a space
- (d) uppercase is not needed

**Answer:** (c) the last word is also followed by a space
**Explanation:** Every word then ends at a space.

**Q44.** In word extraction, word = "" is done
- (a) before every character
- (b) after a word has been used at a space
- (c) only once before the loop
- (d) never

**Answer:** (b) after a word has been used at a space
**Explanation:** Ready for the next word.

**Q45.** "India is my country" in uppercase, one word per line, prints first
- (a) COUNTRY
- (b) IND
- (c) INDIA
- (d) INDIA IS

**Answer:** (c) INDIA
**Explanation:** The words in order.

**Q46.** The last word of "India is my country" is
- (a) e.substring(e.indexOf(' '))
- (b) e.substring(e.lastIndexOf(' ') + 1)
- (c) e.charAt(e.length())
- (d) e.substring(0, e.indexOf(' '))

**Answer:** (b) e.substring(e.lastIndexOf(' ') + 1)
**Explanation:** After the last space.

**Q47.** The first word of the same sentence is
- (a) e.substring(e.lastIndexOf(' '))
- (b) e.substring(0, e.indexOf(' '))
- (c) e.charAt(0)
- (d) e.substring(1)

**Answer:** (b) e.substring(0, e.indexOf(' '))
**Explanation:** Up to the first space.

**Q48.** The longest word of "Cherrapunji receives very heavy monsoon rainfall" is
- (a) Cherrapunji
- (b) receives
- (c) rainfall
- (d) monsoon

**Answer:** (a) Cherrapunji
**Explanation:** 11 letters.

**Q49.** Reversing each word of "India is my country" but keeping the order gives
- (a) yrtnuoc ym si aidnI
- (b) country my is India
- (c) aidnI si ym yrtnuoc
- (d) INDIA IS MY COUNTRY

**Answer:** (c) aidnI si ym yrtnuoc
**Explanation:** Each word is reversed in place.

**Q50.** The acronym of "Indian Space Research Organisation" is
- (a) ISRO
- (b) ISR
- (c) INDIA
- (d) SRO

**Answer:** (a) ISRO
**Explanation:** First letters of the words.

**Q51.** The 2019 scheme counts words starting with 'A' by checking
- (a) the length of each word
- (b) only the last word
- (c) every 'A' in the sentence
- (d) a space followed by 'A', and an 'A' at index 0

**Answer:** (d) a space followed by 'A', and an 'A' at index 0
**Explanation:** Every 'A' would overcount.

**Q52.** Counting "the" in "The cat and the dog met the other cat" with indexOf (after toLowerCase) gives
- (a) 5
- (b) 3
- (c) 2
- (d) 4

**Answer:** (d) 4
**Explanation:** "other" also contains "the".

**Q53.** To count whole words equal to "the", a program should
- (a) use indexOf only
- (b) extract each word and compare it with equals()
- (c) count the letters t, h, e
- (d) use lastIndexOf only

**Answer:** (b) extract each word and compare it with equals()
**Explanation:** Then "other" is not counted.

**Q54.** The 2018 examiners noted that many candidates wrote
- (a) ch.toUpperCase() for a char
- (b) Character.toUpperCase(ch)
- (c) a for loop
- (d) nextLine()

**Answer:** (a) ch.toUpperCase() for a char
**Explanation:** A char has no methods.

**Q55.** To print each word of a sentence on a new line, the program prints word
- (a) with println at each space
- (b) after the whole loop only
- (c) for every character
- (d) before the loop

**Answer:** (a) with println at each space
**Explanation:** One line per word.

**Q56.** Pig Latin of "TROUBLE" (move the letters before the first vowel to the end and add AY) is
- (a) AYOUBLETR
- (b) TROUBLEAY
- (c) ROUBLETAY
- (d) OUBLETRAY

**Answer:** (d) OUBLETRAY
**Explanation:** OUBLE + TR + AY.

**Q57.** Pig Latin of "APPLE" is
- (a) APPLEAY
- (b) PPLEAAY
- (c) AYAPPLE
- (d) PLEAPAY

**Answer:** (a) APPLEAY
**Explanation:** The first letter is already a vowel.

**Q58.** In word extraction, a double space between words produces
- (a) a compile error
- (b) an empty word, unless word.length() > 0 is checked
- (c) a skipped character
- (d) no effect at all

**Answer:** (b) an empty word, unless word.length() > 0 is checked
**Explanation:** Check the word before using it.

### Splitting and rejoining (Q59–Q66)

**Q59.** The Symbolic word of AIRWAYS (ICSE 2026) is
- (a) WAYSAIRTR
- (b) AIRWAYSTR
- (c) RWAYSAITR
- (d) RWAYSTR

**Answer:** (c) RWAYSAITR
**Explanation:** RWAYS + AI + TR.

**Q60.** The Symbolic word of BEAUTY is
- (a) BEAUTYTR
- (b) EAUTYBTR
- (c) TYBEAUTR
- (d) BTR

**Answer:** (a) BEAUTYTR
**Explanation:** B is already a consonant.

**Q61.** The general rule for splitting a word w at position i is
- (a) w.charAt(i) + w
- (b) w.substring(0, i) + w.substring(0, i)
- (c) w.substring(i) + w.substring(0, i)
- (d) w.substring(i, 0)

**Answer:** (c) w.substring(i) + w.substring(0, i)
**Explanation:** The two parts swapped.

**Q62.** In checking "icse2024@gmail.com", the part between @ and the last dot is
- (a) gmail
- (b) icse2024
- (c) com
- (d) gmail.com

**Answer:** (a) gmail
**Explanation:** substring(p + 1, q).

**Q63.** The part after the last dot of "icse2024@gmail.com" is
- (a) com
- (b) gmail
- (c) .com
- (d) gmail.com

**Answer:** (a) com
**Explanation:** substring(q + 1).

**Q64.** The 2024 scheme uses indexOf('.') for the dot. For first.last@gmail.com this
- (a) returns "Valid" for every id
- (b) works correctly
- (c) fails with StringIndexOutOfBoundsException
- (d) does not compile

**Answer:** (c) fails with StringIndexOutOfBoundsException
**Explanation:** The first dot is before the @.

**Q65.** The examiners also accepted, for the gmail check,
- (a) s.equals("gmail")
- (b) s.startsWith("gmail")
- (c) s.length() > 10
- (d) s.endsWith("@gmail.com")

**Answer:** (d) s.endsWith("@gmail.com")
**Explanation:** A short, valid test.

**Q66.** "kong@yahoo.com" checked by the gmail program gives
- (a) Valid gmail id
- (b) Invalid - no gmail
- (c) Invalid - no com
- (d) Invalid - no @

**Answer:** (b) Invalid - no gmail
**Explanation:** The middle part is yahoo.

### String arrays (Q67–Q76)

**Q67.** In bubble-sorting names alphabetically, the swap condition is
- (a) n[j].equals(n[j + 1])
- (b) n[j] > n[j + 1]
- (c) n[j].compareTo(n[j + 1]) > 0
- (d) n[j].length() > n[j + 1].length()

**Answer:** (c) n[j].compareTo(n[j + 1]) > 0
**Explanation:** Strings cannot use >.

**Q68.** To arrange 40 words in descending order by selection sort, each pass finds the
- (a) shortest word
- (b) smallest remaining word
- (c) largest remaining word
- (d) first word only

**Answer:** (c) largest remaining word
**Explanation:** It is swapped to the front.

**Q69.** Linear search for a name in a String array compares with
- (a) charAt()
- (b) ==
- (c) compareTo() > 0
- (d) equals() or equalsIgnoreCase()

**Answer:** (d) equals() or equalsIgnoreCase()
**Explanation:** Contents, not references.

**Q70.** "aiom".compareTo("Rida") is
- (a) -15
- (b) 15
- (c) 0
- (d) -17

**Answer:** (b) 15
**Explanation:** 'a' (97) − 'R' (82).

**Q71.** Because of Q70, a sort with compareTo() puts "aiom"
- (a) first in every list
- (b) before "Rida"
- (c) after "Rida"
- (d) nowhere

**Answer:** (c) after "Rida"
**Explanation:** Small letters come after capitals.

**Q72.** To sort names typed in mixed case, a program can use
- (a) compareToIgnoreCase()
- (b) equals()
- (c) length()
- (d) charAt(0) only

**Answer:** (a) compareToIgnoreCase()
**Explanation:** Case is then ignored.

**Q73.** Sorting Wanda, Ibapynshai, Daphi, Banri, Rida, Kitbor, Aiom, Mebanshan, Saphira, Careen alphabetically puts first
- (a) Banri
- (b) Aiom
- (c) Wanda
- (d) Careen

**Answer:** (b) Aiom
**Explanation:** A comes first.

**Q74.** In the same sorted list, the last name is
- (a) Mebanshan
- (b) Saphira
- (c) Rida
- (d) Wanda

**Answer:** (d) Wanda
**Explanation:** W is last.

**Q75.** Searching "meghalaya" in {"Arunachal Pradesh", "Assam", "Manipur", "Meghalaya", …} with equalsIgnoreCase() finds it at index
- (a) -1
- (b) 4
- (c) 3
- (d) 2

**Answer:** (c) 3
**Explanation:** Case is ignored.

**Q76.** The 2026 Improvement Q5 program must print
- (a) the number of names
- (b) only the sorted array
- (c) only the first name
- (d) both the original array and the sorted array

**Answer:** (d) both the original array and the sorted array
**Explanation:** As the question asks.
## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** Write the standard loop that takes each character of a String s.
**Answer:** `for (int i = 0; i < s.length(); i++) { char ch = s.charAt(i); … }`
Indexes run from 0 to length() − 1.

**Q2.** Write a test for "ch is a vowel", for a String already in uppercase.
**Answer:** `"AEIOU".indexOf(ch) >= 0`
or `ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U'`.

**Q3.** How is a special character identified with Character methods?
**Answer:** It is neither a letter nor a digit.
`!Character.isLetterOrDigit(ch)` is true for it.

**Q4.** Why is a new String built from "" instead of changing s?
**Answer:** Strings are immutable; their characters cannot be changed.
A new String is built: `t = t + ch;`.

**Q5.** Why is `(char)` needed in `t = t + (char) (ch + 1);`?
**Answer:** ch + 1 is an int.
Without the cast, the number would be added to t instead of the next character.

**Q6.** Why add a space at the end of a sentence before extracting its words?
**Answer:** Each word is used when a space is reached.
The added space makes the last word end at a space too.

**Q7.** Write the condition for "the character at index i begins a word".
**Answer:** `i == 0 || s.charAt(i - 1) == ' '`
The first character, or one after a space.

**Q8.** Write two ways to build the reverse r of a String s.
**Answer:** `for (int i = s.length() - 1; i >= 0; i--) r = r + s.charAt(i);`
`for (int i = 0; i < s.length(); i++) r = s.charAt(i) + r;`

**Q9.** How is a String array sorted alphabetically by bubble sort?
**Answer:** Compare neighbours with compareTo().
Swap when `n[j].compareTo(n[j + 1]) > 0`.

**Q10.** How is a name searched in a String array?
**Answer:** By linear search, comparing each element with the name.
Use equals() or equalsIgnoreCase(), not ==.

**Q11.** Distinguish between a Super String (ICSE 2025) and a Special String (ICSE 2025 Improvement).
**Answer:** Super: number of uppercase letters = number of lowercase letters.
Special: number of vowels = number of consonants.

**Q12.** What mistakes did the examiners report in the 2025 Super String program?
**Answer:** Counters initialised inside the loop, Character methods not used, `if (uc = lc)` for `if (uc == lc)`.
Also length() missed and the messages not printed.

### Output and error questions (2 marks each)

**Q13.** `String s = "Meghalaya", r = ""; for (int i = s.length() - 1; i >= 0; i--) r = r + s.charAt(i); System.out.println(r);`
**Answer:** `ayalahgeM`

**Q14.** `String w = "COMPUTER"; int v = 0; for (int i = 0; i < w.length(); i++) if ("AEIOU".indexOf(w.charAt(i)) >= 0) v++; System.out.println(v + " " + (w.length() - v));`
**Answer:** `3 5` — three vowels and five other letters.

**Q15.** `String x = "aBc1", y = "";` A loop adds `Character.toLowerCase(ch)` for each capital and `Character.toUpperCase(ch)` otherwise. Give y.
**Answer:** `AbC1` — the digit is unchanged by toUpperCase.

**Q16.** `String q = "HELLO", z = ""; for (int i = 0; i < q.length(); i += 2) z = z + q.charAt(i); System.out.println(z);`
**Answer:** `HLO` — indexes 0, 2 and 4.

**Q17.** `String m = "ABC", n = ""; for (int i = 0; i < m.length(); i++) n = n + (char) (m.charAt(i) + 1); System.out.println(n);`
**Answer:** `BCD`

**Q18.** `String k = "banana"; int c = 0; for (int i = 0; i < k.length(); i++) if (k.charAt(i) == 'a') c++; System.out.println(c + " " + k.replace('a', '*'));`
**Answer:** `3 b*n*n*`

**Q19.** `String e = "India is my country"; System.out.println(e.substring(e.lastIndexOf(' ') + 1) + " " + e.substring(0, e.indexOf(' ')));`
**Answer:** `country India` — the last word, then the first.

**Q20.** `String names[] = {"Rida", "aiom", "Banri"}; System.out.println(names[1].compareTo(names[0]) + " " + names[0].compareTo(names[2]));`
**Answer:** `15 16` — 'a' − 'R' and 'R' − 'B'.

**Q21.** Find the error: `char ch = s.charAt(i); ch = ch.toUpperCase();`
**Answer:** A char has no methods.
Write `ch = Character.toUpperCase(ch);`.

**Q22.** Find the error: in the 2024 gmail check, `q = s.indexOf('.')` is used. What happens for "first.last@gmail.com"?
**Answer:** The first dot is before the @, so `s.substring(p + 1, q)` throws StringIndexOutOfBoundsException.
Use `q = s.lastIndexOf('.')`.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; sample runs follow each.*

### Section B programs (15 marks each)

**Q1.** Write a program to input a sentence and print the number of words and the longest word with its length.
**Answer:**
```java
import java.util.*;
class LongestWord
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine().trim() + " ";
        String word = "", longest = "";
        int count = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (ch != ' ')
                word = word + ch;
            else if (word.length() > 0)
            {
                count++;
                if (word.length() > longest.length())
                    longest = word;
                word = "";
            }
        }
        System.out.println("Number of words : " + count);
        System.out.println("Longest word    : " + longest + " (" + longest.length() + " letters)");
    }
}
```
Sample run:
```
Enter a sentence: Cherrapunji receives very heavy monsoon rainfall
Number of words : 6
Longest word    : Cherrapunji (11 letters)
```

**Q2.** Write a program to input a sentence and reverse each word, keeping the words in their order.
**Answer:**
```java
import java.util.*;
class ReverseWords
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine() + " ";
        String word = "", out = "";
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if (ch != ' ')
                word = ch + word;          // builds the word backwards
            else
            {
                out = out + word + " ";
                word = "";
            }
        }
        System.out.println(out.trim());
    }
}
```
Sample run:
```
Enter a sentence: India is my country
aidnI si ym yrtnuoc
```

**Q3.** Write a program to input a sentence and print the frequency of each vowel (A, E, I, O, U), ignoring case.
**Answer:**
```java
import java.util.*;
class VowelFrequency
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine().toUpperCase();
        String v = "AEIOU";
        for (int k = 0; k < v.length(); k++)
        {
            char vowel = v.charAt(k);
            int count = 0;
            for (int i = 0; i < s.length(); i++)
            {
                if (s.charAt(i) == vowel)
                    count++;
            }
            System.out.println(vowel + " : " + count);
        }
    }
}
```
Sample run:
```
Enter a sentence: Education is the most powerful weapon
A : 2
E : 4
I : 2
O : 4
U : 2
```

**Q4.** The north-eastern states Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim and Tripura are stored in a String array. Write a program to search for a state input by the user by linear search, ignoring case.
**Answer:**
```java
import java.util.*;
class NameSearch
{
    public static void main(String args[])
    {
        String states[] = {"Arunachal Pradesh", "Assam", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Sikkim", "Tripura"};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a state: ");
        String key = sc.nextLine().trim();
        int pos = -1;
        for (int i = 0; i < states.length; i++)
        {
            if (states[i].equalsIgnoreCase(key))
            {
                pos = i;
                break;
            }
        }
        if (pos >= 0)
            System.out.println(states[pos] + " found at index " + pos);
        else
            System.out.println(key + " is not a north-eastern state in the list");
    }
}
```
Sample runs:
```
Enter a state: meghalaya
Meghalaya found at index 3
```
```
Enter a state: Kerala
Kerala is not a north-eastern state in the list
```

**Q5.** Write a program to input the name of an organisation and print its acronym — the first letter of each word in capitals.
**Answer:**
```java
import java.util.*;
class Acronym
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a name: ");
        String s = " " + sc.nextLine().trim();
        String a = "";
        for (int i = 0; i < s.length() - 1; i++)
        {
            if (s.charAt(i) == ' ' && s.charAt(i + 1) != ' ')
                a = a + Character.toUpperCase(s.charAt(i + 1));
        }
        System.out.println("Acronym: " + a);
    }
}
```
Sample run:
```
Enter a name: Indian Space Research Organisation
Acronym: ISRO
```

**Q6.** Write a program to input a word and convert it to Pig Latin: move the letters before the first vowel to the end and add "AY".
**Answer:**
```java
import java.util.*;
class PigLatin
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String w = sc.next().toUpperCase();
        int i;
        for (i = 0; i < w.length(); i++)
        {
            if ("AEIOU".indexOf(w.charAt(i)) >= 0)
                break;                     // first vowel
        }
        String p = w.substring(i) + w.substring(0, i) + "AY";
        System.out.println("Piglatin: " + p);
    }
}
```
Sample runs:
```
Enter a word: trouble
Piglatin: OUBLETRAY
```
```
Enter a word: apple
Piglatin: APPLEAY
```

---

## 12. Competency / Application Questions

**Q1. (Plan the program)** A question asks: "accept a word and print it with every consonant doubled". List the steps.
**Model answer:** Read the word; set t = ""; for each character, add it to t, and add it again if it is a letter that is not a vowel; print t.

**Q2. (Find the bug)** A program counts digits with `if (ch >= 0 && ch <= 9) d++;`. Why is the count wrong?
**Model answer:** It compares codes with the numbers 0 to 9; the digit characters are '0' to '9' (48 to 57). Use `Character.isDigit(ch)` or `ch >= '0' && ch <= '9'`.

**Q3. (Sort the register)** Names are typed as "aiom", "Rida", "banri". Why does compareTo give a strange order, and how is it fixed?
**Model answer:** Capitals come before small letters; convert all names to one case first or use compareToIgnoreCase().

**Q4. (Whole words only)** Why can counting "is" with indexOf in "This is his list" give the wrong number of words, and what is better?
**Model answer:** indexOf also finds "is" inside This, his and list; extract each word and compare it with equals("is").

**Q5. (Check an id)** Write one statement that checks whether a String id is a gmail.com address.
**Model answer:** `if (id.endsWith("@gmail.com"))` — accepted by the 2024 examiners.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** A new String is built from "" in a loop to change characters.
**R:** Strings are immutable.
**Answer:** (c)
**Explanation:** The original cannot be changed.

**Q2.**
**A:** `ch.toUpperCase()` converts a char to uppercase.
**R:** Character.toUpperCase(ch) is a static method.
**Answer:** (b)
**Explanation:** A char has no methods.

**Q3.**
**A:** Counters must be initialised before the loop.
**R:** Initialising inside the loop resets them for every character.
**Answer:** (c)
**Explanation:** An examiners' note from 2025.

**Q4.**
**A:** Strings in an array are compared with > in a sort.
**R:** compareTo() returns an int.
**Answer:** (b)
**Explanation:** Use compareTo() > 0.

**Q5.**
**A:** "aiom" comes after "Rida" when sorted with compareTo().
**R:** Small letters have larger codes than capitals.
**Answer:** (c)
**Explanation:** 'a' 97 > 'R' 82.

**Q6.**
**A:** The Symbolic word of BEAUTY is BEAUTYTR.
**R:** Java is case sensitive.
**Answer:** (d)
**Explanation:** Both true; B is already a consonant.

**Q7.**
**A:** indexOf("the") counts only whole words "the".
**R:** indexOf finds a substring anywhere.
**Answer:** (b)
**Explanation:** It also finds "the" in "other".

**Q8.**
**A:** A space is added at the end of a sentence before extracting words.
**R:** next() reads a whole sentence.
**Answer:** (a)
**Explanation:** next() reads one word; nextLine() reads the sentence.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The secret agency

> The first letter becomes @ (vowel) or # (consonant); the rest is reversed.

**(i)** Encode "PERFORM".
**Answer:** #MROFRE.

**(ii)** Encode "APPEARANCE6".
**Answer:** @6ECNARAEPP.

**(iii)** Which test decides @ or #?
**Answer:** `"AEIOU".indexOf(first) >= 0`.

**(iv)** In which direction does the loop for the rest run?
**Answer:** From the last index down to 1.

### Case 2 — The Super String

> "COmmITmeNt" is tested with Character.isUpperCase and Character.isLowerCase.

**(i)** How many uppercase letters?
**Answer:** 5.

**(ii)** How many lowercase letters?
**Answer:** 5.

**(iii)** Is it a Super String?
**Answer:** Yes.

**(iv)** Where are the counters set to 0?
**Answer:** Before the loop.

### Case 3 — The class register

> Ten names are sorted alphabetically by bubble sort, and the original list is also printed.

**(i)** Which method compares two names?
**Answer:** compareTo().

**(ii)** When are two neighbours swapped?
**Answer:** When `n[j].compareTo(n[j + 1]) > 0`.

**(iii)** Why is a copy of the array kept?
**Answer:** To print the original order after sorting.

**(iv)** How many passes are needed for 10 names?
**Answer:** 9.

---

## 15. Revision Notes

### Chapter at a glance
- Toolkit: nextLine (sentence) / next (word); toUpperCase; loop i < length(); charAt(i); counters before, output after.
- Counting: Character methods; vowel test "AEIOU".indexOf(ch) >= 0; consonant = letter, not vowel.
- Changing: build t from ""; (char) after arithmetic; reverse by looping backwards.
- Words: add a space at the end; collect letters; act at each space; a word begins at i == 0 or after a space.
- Split and rejoin: find the position, then substring(i) + substring(0, i).
- String arrays: compareTo() for sorting, equals() for searching.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| `ch.toUpperCase()` | `Character.toUpperCase(ch)` |
| Counters set inside the loop | Set them before the loop. |
| `if (uc = lc)` | `if (uc == lc)` |
| `t = t + ch + 1` for the next character | `t = t + (char) (ch + 1)` |
| Strings compared with == or > | equals() and compareTo() |
| Last word missed in word extraction | Add a space at the end. |
| next() used for a sentence | nextLine() |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 13: String Handling II**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** "KAPILDEV@83" has special characters:
(a) 0 (b) 2 (c) 1 (d) 3

**2.** The Symbolic word of AIRWAYS:
(a) AIRWAYSTR (b) RWAYSAITR (c) WAYSAIRTR (d) RWAYSTR

**3.** A vowel test after toUpperCase():
(a) "AEIOU".indexOf(ch) >= 0 (b) "AEIOU".indexOf(ch) == -1 (c) ch == "AEIOU" (d) Character.isVowel(ch)

**4.** The reverse of "Meghalaya":
(a) Meghalaya (b) ayalahge (c) aMeghalay (d) ayalahgeM

**5.** Swap condition for alphabetical bubble sort:
(a) n[j] > n[j + 1] (b) n[j].compareTo(n[j + 1]) > 0 (c) n[j].equals(n[j + 1]) (d) n[j].length() > 0

**6.** Words starting with A in the 2019 sentence:
(a) 3 (b) 5 (c) 4 (d) 2

**7.** "PERFORM" encoded (@/# then reverse):
(a) #MROFRE (b) @MROFRE (c) #ERFORM (d) MROFREP

**8.** A character begins a word when:
(a) s.charAt(i) == ' ' (b) i == s.length() - 1 (c) s.charAt(i + 1) == ' ' (d) i == 0 || s.charAt(i - 1) == ' '

**9.** "aiom".compareTo("Rida"):
(a) 15 (b) -15 (c) 0 (d) 17

**10.** Statement I: A char has no methods. Statement II: next() reads a whole sentence.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

### Part I — Short answers (5 × 2 = 10)

**11.** Write the test for a special character using Character methods. [2]

**12.** Give the output: `String m = "ABC", n = ""; for (int i = 0; i < m.length(); i++) n = n + (char) (m.charAt(i) + 1); System.out.println(n);` [2]

**13.** Why is a space added at the end of a sentence before extracting words? [2]

**14.** Find the error: `ch = ch.toUpperCase();` for a char ch. [2]

**15.** Give the output: `String e = "India is my country"; System.out.println(e.substring(e.lastIndexOf(' ') + 1));` [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Accept a String and check whether it is a Super String (equal numbers of uppercase and lowercase letters). [10]

**17.** Accept a sentence in lower case and print it with the first letter of every word in capitals. [10]

**18.** Accept the names of 10 students, sort them alphabetically by bubble sort, and print the original and sorted lists. [10]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | b | c | d | b | a |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | #MROFRE | @6ECNARAEPP | "AEIOU".indexOf(first) >= 0 | Last index down to 1 |
| 2 | 5 | 5 | Yes | Before the loop |
| 3 | compareTo() | compareTo() > 0 | To print the original | 9 |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | c | b | a | d | b | c | a | d | a | c |

**Part I, Q11–15 (2 marks each)**

**11.** `!Character.isLetterOrDigit(ch)` (2).
**12.** `BCD` (2).
**13.** So that the last word also ends at a space (2).
**14.** A char has no methods (1); `ch = Character.toUpperCase(ch);` (1).
**15.** `country` (2).

**Part II (10 marks each)**

**16.–18.** Input (2), loop with charAt or array loop (2), correct methods and logic (4), output messages (2).
