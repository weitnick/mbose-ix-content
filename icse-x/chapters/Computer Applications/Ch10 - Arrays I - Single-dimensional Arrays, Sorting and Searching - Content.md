# Arrays I — Single-dimensional Arrays, Sorting and Searching

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 10 |
| Title | Arrays I — Single-dimensional Arrays, Sorting and Searching |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 7. Arrays |
| Exam weightage | **Section B**: an array program in almost every paper — **linear or binary search**, **bubble or selection sort**, or a count/sum over an array (15 marks). **Section A**: MCQs and 2-mark parts on **index, length, memory in bytes** and **outputs**. |
| Syllabus scope | Definition of an array; types; need; declaration, initialisation and accepting data in single-dimensional arrays; accessing elements; searching — linear and binary; sorting — bubble and selection. |
| In short | How to store many values in one array, and how to search and sort them using linear search, binary search, bubble sort and selection sort. |

> **Note on the text:** CISCE prescribes no textbook for ICSE Computer Applications; this chapter follows the ICSE 2027 syllabus in its own words. Its questions are the CISCE papers of 2017–2026 and the 2024 and 2025 specimens, answered from CISCE's marking schemes and examiners' comments where published. **Every program was compiled and run (Java 21).**
>
> **Exam note:** Declare the array with **the data type and size given in the question** (char array for characters, double for decimals, size 20 if 20 values). Indexes run from **0 to length − 1**; `a.length` has **no brackets**. Use **the technique named** — binary search only on sorted data, selection sort when selection is asked. Always **print the result** (sorted array, "found" message) after the loop, not inside it.

---

## 1. Complete Lesson

### Why arrays?

To store the marks of 40 students we would need 40 variables — m1, m2, … m40 — and 40 input statements. An **array** stores all of them under **one name**, and a loop can process them.

An **array** is a collection of **elements of the same data type**, stored in **consecutive memory locations** and referred to by **one name**. Each element is identified by its **index (subscript)**, which starts at **0**.

![Fig. 10.1 A single-dimensional array: one name, numbered cells starting at index 0](figures/ca_ch10_fig01_array_anatomy.png)

Types of arrays in the syllabus: **single-dimensional** (one index, a list — this chapter) and **double-dimensional** (two indexes, a table — Chapter 11).

### Declaring, creating and initialising

```java
int a[] = new int[10];          // declares and creates an array of 10 ints (all 0)
int[] b = new int[5];           // the brackets may follow the type
double x[] = {2.5, 4.5, 5.5, 6.4};      // declared and initialised: size 4
char ch[] = {'A', 'E', 'I', 'O', 'U'};
String s[] = {"Blue", "Red", "Violet"};
```

- `new int[10]` gives every element its **default value**: 0 for numbers, 0.0 for double, false for boolean, null for String.
- An initialiser list `{…}` can be used **only in the declaration**: `a = {1, 2, 3};` on its own line is a compile error.
- The **size is fixed** once the array is created.

### Length, index and the last element

- `a.length` gives the number of elements — it is a **property, written without brackets** (`a.length()` is an error). For a String inside a String array, `s[2].length()` is the String's length — with brackets.
- The first element is `a[0]`; the **last** is `a[a.length - 1]` (ICSE 2025 Q1(xiii)). For 50 elements the last is `x[49]` (ICSE 2025 specimen Q1(xi)); the 5th element is `X[4]` (ICSE 2024 specimen Q1(x)).
- Using an index outside 0 to length − 1 compiles but stops the program with **ArrayIndexOutOfBoundsException** (a run-time error).

### Memory occupied by an array

Memory = **number of elements × size of one element**:

| Type | Bytes per element | Example | Memory |
|---|---|---|---|
| byte | 1 | `byte b[] = new byte[10];` | 10 bytes |
| short / char | 2 | `char c[] = new char[10];` | 20 bytes |
| int / float | 4 | `int a[] = new int[9];` | 36 bytes |
| long / double | 8 | `double x[] = {2.5, 4.5, 5.5, 6.4};` | 32 bytes |

So 10 decimal (double) values take **80 bytes** (ICSE 2026 Improvement Q1(v)), a 10-element char array **20 bytes** (ICSE 2024 specimen Q1(v)) and a 6-element char array **12 bytes**.

### Input and output with loops

```java
Scanner sc = new Scanner(System.in);
int a[] = new int[10];
for (int i = 0; i < a.length; i++)       // input
    a[i] = sc.nextInt();
for (int i = 0; i < a.length; i++)       // output
    System.out.print(a[i] + " ");
```

Use the Scanner method that matches the type: `nextDouble()` for double, `next().charAt(0)` for char, `nextLine()` (or `next()` for one word) for String. The examiners have noted int arrays declared for characters (2023), integers accepted where characters were given (2025) and input taken without a loop (2019).

### Working with every element

| Task | Core statement inside the loop |
|---|---|
| Sum | `sum = sum + a[i];` |
| Largest | `if (a[i] > max) max = a[i];` (start with max = a[0]) |
| Smallest | `if (a[i] < min) min = a[i];` (start with min = a[0]) |
| Count matches | `if (d[i].equals(key)) count++;` |
| One-digit / two-digit | `if (a[i] >= 0 && a[i] <= 9) …` / `else if (a[i] >= 10 && a[i] <= 99) …` |

For 2023 Q8 the examiners noted candidates who treated **every** number that was not one-digit as two-digit, and who used `||` instead of `&&`.

### Searching

**Searching** finds whether a value (the **key**) is present in an array, and where. **Sorting** arranges the elements in order (ICSE 2018 Q1(b)).

**Linear search** compares the key with each element in turn, from index 0:

```java
int pos = -1;
for (int i = 0; i < a.length; i++)
{
    if (a[i] == key)
    {
        pos = i;
        break;            // stop at the first match
    }
}
if (pos >= 0)
    System.out.println(key + " found at index " + pos);
else
    System.out.println(key + " not found");
```

A **flag** (boolean found) or `System.exit(0)` after printing "found" can be used instead of pos. Print "not found" **after** the loop — printing it inside the loop prints it many times.

**Binary search** works only on a **sorted** array. It compares the key with the **middle** element and throws away the half that cannot contain it:

![Fig. 10.3 Binary search compares the key with the middle element and discards half each time](figures/ca_ch10_fig03_binary_search.png)

```java
int low = 0, high = a.length - 1, pos = -1;
while (low <= high)
{
    int mid = (low + high) / 2;
    if (a[mid] == key)
    {
        pos = mid;
        break;
    }
    else if (a[mid] < key)
        low = mid + 1;        // key is in the right half
    else
        high = mid - 1;       // key is in the left half
}
```

Three details decide the marks: **high = length − 1** (not length), the loop condition **low <= high**, and **low = mid + 1 / high = mid − 1**. Characters are compared with `==` and `<` (not equals()); Strings are compared with `compareTo()`.

| Linear search | Binary search |
|---|---|
| Array need not be sorted | Array must be sorted |
| Checks each element from index 0 in order | Checks the middle element and halves the range |
| Slow for large arrays (up to n comparisons) | Fast (about log₂ n comparisons) |
| Simple | Slightly more complex |

### Sorting

**Bubble sort** compares **neighbouring** elements and swaps them if they are in the wrong order. After each pass the largest remaining element "bubbles" to the end:

```java
for (int i = 0; i < a.length - 1; i++)            // n - 1 passes
{
    for (int j = 0; j < a.length - 1 - i; j++)    // compare neighbours
    {
        if (a[j] > a[j + 1])                      // > for ascending
        {
            int temp = a[j];
            a[j] = a[j + 1];
            a[j + 1] = temp;
        }
    }
}
```

**Selection sort** finds the **smallest** element of the unsorted part and swaps it into the first unsorted position — one swap per pass:

```java
for (int i = 0; i < a.length - 1; i++)
{
    int min = i;
    for (int j = i + 1; j < a.length; j++)
    {
        if (a[j] < a[min])
            min = j;
    }
    int temp = a[i];
    a[i] = a[min];
    a[min] = temp;
}
```

![Fig. 10.2 Both sorts need n − 1 passes for n elements; they differ in which elements they swap](figures/ca_ch10_fig02_sorting.png)

| Bubble sort | Selection sort |
|---|---|
| Compares neighbouring elements | Finds the minimum of the unsorted part |
| May swap many times in a pass | Swaps once per pass |
| Largest element moves to the end each pass | Smallest element moves to the front each pass |

For **descending** order, change `>` to `<` in bubble sort, or look for the **maximum** in selection sort. Characters sort by their codes (digits, then capitals, then small letters); Strings sort with `compareTo()`. The 2024 examiners noted candidates who wrote insertion or bubble sort when **selection sort** was asked, inverted the comparison, or did not print the sorted array.

### Swapping two elements

With a third variable: `int t = x[0]; x[0] = x[1]; x[1] = t;`. Without one (ICSE 2026 Q2(ix)), using multiplication and division (for non-zero values):

```java
x[0] = x[0] * x[1];     // 32
x[1] = x[0] / x[1];     // 4
x[0] = x[0] / x[1];     // 8
```

### Parallel arrays and array references

- **Parallel arrays** keep related data at the same index: `name[i]` and `totalmarks[i]` belong to the same student (ICSE 2018 Q9). When sorting, swap the elements of **both** arrays.
- An array variable holds a **reference**: after `int r[] = q;`, both names refer to one array, so `r[1] = 60;` also changes `q[1]`.

### Summary of the chapter

- **Array** — same-type elements, one name, index from 0; size fixed; `a.length` without brackets.
- **Memory** — elements × bytes per element (int 4, double 8, char 2).
- **Linear search** — any array, element by element; **binary search** — sorted array, halve with low, high, mid.
- **Bubble sort** — swap neighbours; **selection sort** — swap the minimum into place; n − 1 passes each.
- **Searching** finds; **sorting** arranges.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Explain the need for arrays and declare, create and initialise single-dimensional arrays of any type.
2. Use index, length and the last element correctly, and calculate the memory an array occupies.
3. Input, output and process all elements (sum, largest, smallest, count).
4. Write linear search and binary search, and compare them.
5. Write bubble sort and selection sort, trace their passes and compare them.
6. Use parallel arrays and understand array references.

---

## 3. Detailed Section Explanations

### Section 1 — One name, many boxes
An array is a row of numbered boxes; the number (index) starts at 0.

### Section 2 — Loops and arrays go together
Every array task — input, output, sum, search, sort — is a loop over the indexes.

### Section 3 — Two ways to search
Linear search works anywhere; binary search needs sorted data but is much faster.

### Section 4 — Two ways to sort
Bubble sort swaps neighbours; selection sort selects the minimum.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Array | A collection of same-type elements under one name. |
| Element | One value stored in an array. |
| Index (subscript) | The position number of an element, starting at 0. |
| length | The number of elements in an array (a.length). |
| Single-dimensional array | An array with one index — a list. |
| Initialiser list | Values in braces that create and fill an array. |
| ArrayIndexOutOfBoundsException | The run-time error for an index outside 0 to length − 1. |
| Searching | Finding whether and where a value occurs. |
| Linear search | Checking elements one by one from the start. |
| Binary search | Repeatedly checking the middle of a sorted range. |
| Sorting | Arranging elements in ascending or descending order. |
| Bubble sort | Sorting by swapping neighbouring elements. |
| Selection sort | Sorting by swapping the minimum into place each pass. |
| Pass | One complete run of the inner loop of a sort. |
| Parallel arrays | Arrays whose elements at the same index belong together. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| Index of the first element | 0 |
| Index of the last element of ar | ar.length - 1 |
| Initialise the last of 50 elements to 100 | x[49] = 100 |
| The 5th element of X | X[4] |
| Number of Strings in String s[] | s.length |
| double x[] = {2.5, 4.5, 5.5, 6.4} | 32 bytes |
| 10 double values | 80 bytes |
| char array of 10 elements | 20 bytes |
| int a[] = {12,10,8,4,6,2,3,5,7}: a[0] + a[5] | 14 |
| ch[0] * 2 for ch[0] = 'A' | 130 |
| color[2].length() for "Violet" | 6 |
| Joining arrays of 4 and 3 elements | size 7; first index 0, last index 6 |
| Binary search needs | a sorted array |

### 5.2 Memory aids

- **"Zero to length minus one."**
- **"Binary needs Bound and sorted: low ≤ high."**
- **"Bubble: Buddies swap. Selection: Smallest steps forward."**

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- Binary search on a million sorted values needs at most 20 comparisons; linear search may need a million.
- Java's library has `Arrays.sort(a)` (in java.util), but ICSE answers must write the sort themselves.
- Other sorting methods include insertion sort, merge sort and quick sort; they are not in the ICSE Class X syllabus.

---

## 6. Person Profiles

### 6.1 John von Neumann (1903–1957)
A Hungarian-American mathematician who, in 1945, wrote one of the first programs for sorting data on a stored-program computer (a merge sort), at a time when sorting was one of the main jobs computers were wanted for.

### 6.2 Donald Knuth (born 1938)
An American computer scientist whose *The Art of Computer Programming*, Volume 3 — *Sorting and Searching* (1973) analysed searching and sorting methods, including binary search, bubble sort and selection sort, in great depth. He received the Turing Award in 1974.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Same type, one name** — arrays make large data manageable.
- **Order speeds search** — sorted data allows binary search.
- **Count the comparisons** — different methods do the same job with very different effort.

### 7.2 Real-life connections
- **Dictionaries and phone contacts** are sorted so that a word or name can be found quickly — the idea behind binary search.
- **Meghalaya:** a school's results list sorted by marks (with names kept alongside) is a parallel-array sort.
- **Shops:** a billing counter searches a product code in its list — linear search for a short unsorted list, binary search for a long sorted one.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section B** (60 marks, any four of six programs) almost always has a single-dimensional array program — linear or binary search, bubble or selection sort, or a count or sum over an array — worth 15 marks. **Section A** asks MCQs and 2-mark parts on index, length, memory and outputs.

### 8.1 Graded exercises — solutions

#### Exercise 10A — Basics

**Q1.** Write a statement to create an array of 25 doubles named price.
**Answer:** `double price[] = new double[25];`

**Q2.** For `int z[] = {4, 7, 9, 66, 72, 0, 16};` give z.length, z[4] and the index of the last element.
**Answer:** 7, 72 and 6.

**Q3.** How many bytes does `long n[] = new long[6];` occupy?
**Answer:** 6 × 8 = 48 bytes.

**Q4.** What are the values of p[2] and d[0] after `int p[] = new int[5]; double d[] = new double[3];`?
**Answer:** 0 and 0.0 — default values.

**Q5.** Why is `a.length()` an error for an array a?
**Answer:** length of an array is a property, written without brackets: a.length.

#### Exercise 10B — Searching and sorting

**Q6.** In binary search on {31, 36, 45, 50, 60, 75, 86, 90} for 75, give mid at each step.
**Answer:** mid = 3 (50 < 75, low = 4), then mid = 5 (75, found).

**Q7.** Give the array after the first pass of bubble sort on {5, 1, 4, 2, 8}.
**Answer:** 1 4 2 5 8.

**Q8.** Give the array after the first two passes of selection sort on {29, 10, 14, 37, 13}.
**Answer:** 10 29 14 37 13, then 10 13 14 37 29.

**Q9.** After `int q[] = {3, 6, 9}; int r[] = q; r[1] = 60;`, what is q[1]? What is the sum of q's elements?
**Answer:** 60 (r and q are one array); the sum is 3 + 60 + 9 = 72.

**Q10.** State one advantage and one condition of binary search over linear search.
**Answer:** It is much faster for large arrays; the array must be sorted.
### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(xvii) (1 mark) | An array with 3 elements is arranged in ascending order as follows: [Picture: 4 1 3, the 4 and 1 swapped → 1 4 3, the 4 and 3 swapped → 1 3 4] Name the technique used: (a) Bubble sort (b) Linear Search (c) Selection sort (d) Binary Search |
| ICSE 2026, Q2(ix) (2 marks) | The following program segment swaps the first element and the second element of the given array without using the third variable; fill in the blanks with appropriate Java statements: `void swap() { int x[] = {4, 8, 19, 24, 15}; (1) ________; (2) ________; x[0] = x[0] / x[1]; System.out.println(x[0] + " " + x[1]); }` |
| ICSE 2026, Q4 (15 marks) | Write a program to accept the designations of 100 employees in a single dimensional array. Accept the designation from the user and print the total number of employees with the designation given by the user as input. Example: Trainee, Manager, Chef, Manager, Director, Manager; Input: Manager; Output: 3 |
| ICSE 2026 Improvement, Q1(ix) (1 mark) | Consider the array: `int x[] = {4, 3, 7, 9, 120, -12, 8};` What is the index of the negative number of the array? (a) 5 (b) 6 (c) 4 (d) x.length |
| ICSE 2026 Improvement, Q1(v) (1 mark) | The number of bytes occupied by the array of 10 elements which are decimal values: (a) 80 bytes (b) 320 bytes (c) 10 bytes (d) 8 bytes |
| ICSE 2026 Improvement, Q1(xvii) (1 mark) | The following character array is sorted in alphabetical order using SELECTION SORT method: W S L A H. After the first iteration the array is changed to A S L W H. What will be the array after the second iteration? (a) W S L A H (b) A H L A S (c) A H L W S (d) W E L A H |
| ICSE 2026 Improvement, Q2(iv) (2 marks) | Differentiate between searching and sorting in single dimensional arrays. |
| ICSE 2025, Q1(iii) (1 mark) | `double x[] = {2.5, 4.5, 5.5, 6.4};` occupies __________ bytes. (a) 16 (b) 4 (c) 8 (d) 32 |
| ICSE 2025, Q1(xiii) (1 mark) | The index (subscript) of the last element of an array ar[] is: (a) ar.length() (b) ar[].length (c) ar.length()-1 (d) ar.length-1 |
| ICSE 2025, Q2(viii) (2 marks) | Consider the following array and answer the questions given below: `int a[] = {12, 10, 8, 4, 6, 2, 3, 5, 7};` (a) What is the output of `System.out.print(a[0] + a[5]);`? (b) What is the index (subscript) of the largest element of the array a[]? |
| ICSE 2025, Q6 (15 marks) | Define a class to initialise the following data in an array. Search for a given character input by the user, using the Binary Search technique. Print "Search Successful" if the character is found otherwise print "Search is not Successful". 'A', 'H', 'N', 'P', 'S', 'U', 'W', 'Y', 'Z', 'b', 'd' |
| ICSE 2025 Improvement, Q2(ix) (2 marks) | Consider the following array and answer the questions given below: `char ch[] = {'A', '%', 'y', '@', '7', 'p'};` (a) How many bytes does the array occupy? (b) What is the output of the statement `Character.isDigit(ch[4])`? |
| ICSE 2025 Improvement, Q8 (15 marks) | Define a class to accept 10 integers in an array, search for the given value using the Linear Search technique and print appropriate messages. |
| ICSE 2025 specimen, Q1(ix) (1 mark) | Consider the array given below: `char ch[] = {'A', 'E', 'I', 'O', 'U'};` Write the output of the following statement: `System.out.println(ch[0] * 2);` (a) 65 (b) 130 (c) 'A' (d) 0 |
| ICSE 2025 specimen, Q1(xi) (1 mark) | A single dimensional array has 50 elements; which of the following is the correct statement to initialize the last element to 100? (a) x[51]=100 (b) x[48]=100 (c) x[49]=100 (d) x[50]=100 |
| ICSE 2025 specimen, Q1(xviii) (1 mark) | The statement used to find the total number of Strings present in the string array String s[] is: (a) s.length (b) s.length() (c) length(s) (d) len(s) |
| ICSE 2025 specimen, Q4 (15 marks) | Define a class to search for a value input by the user from the list of values given below. If it is found display the message "Search successful", otherwise display the message "Search element not found" using Binary search technique. 5.6, 11.5, 20.8, 35.4, 43.1, 52.4, 66.6, 78.9, 80.0, 95.5 |
| ICSE 2024, Q1(xix) (1 mark) | What is the output of the Java code given below? `String color[] = {"Blue", "Red", "Violet"}; System.out.println(color[2].length());` (a) 6 (b) 5 (c) 3 (d) 2 |
| ICSE 2024, Q7 (15 marks) | Define a class pin code and store the given pin codes in a single dimensional array. Sort these pin codes in ascending order using the Selection Sort technique only. Display the sorted array. 110061, 110001, 110029, 110023, 110055, 110006, 110019, 110033 |
| ICSE 2024 specimen, Q1(v) (1 mark) | The number of bytes occupied by a character array of 10 elements: (a) 20 bytes (b) 60 bytes (c) 40 bytes (d) 120 bytes |
| ICSE 2024 specimen, Q1(x) (1 mark) | Java statement to access the 5th element of an array is: (a) X[4] (b) X[5] (c) X[3] (d) X[0] |
| ICSE 2024 specimen, Q2(x) (2 marks) | `int P[] = {12, 14, 16, 18}; int Q[] = {20, 22, 24};` Place all elements of P array and Q array in the array R one after the other. (a) What will be the size of array R[]? (b) Write the index position of the first and last element. |
| ICSE 2024 specimen, Q4 (15 marks) | Define a class to accept values in an integer array of size 10. Sort them in ascending order using the selection sort technique. Display the sorted array. |
| ICSE 2023, Q2(viii) (2 marks) | Consider the given array and answer the questions given below: `int x[] = {4, 7, 9, 66, 72, 0, 16};` (a) What is the length of the array? (b) What is the value in x[4]? |
| ICSE 2023, Q4 (15 marks) | Define a class to accept 10 characters from a user. Using bubble sort technique arrange them in ascending order. Display the sorted array and original array. |
| ICSE 2023, Q7 (15 marks) | Define a class to accept values into an array of double data type of size 20. Accept a double value from user and search in the array using linear search method. If value is found display message "Found" with its position where it is present in the array. Otherwise display message "not found". |
| ICSE 2023, Q8 (15 marks) | Define a class to accept values in integer array of size 10. Find sum of one digit numbers and sum of two digit numbers entered. Display them separately. Example: Input: a[] = {2, 12, 4, 9, 18, 25, 3, 32, 20, 1}; Output: Sum of one digit numbers : 2 + 4 + 9 + 3 + 1 = 19; Sum of two digit numbers : 12 + 18 + 25 + 32 + 20 = 107 |
| ICSE 2020, Q5 (15 marks) | Write a program to search for an integer value input by the user in the sorted list given below using binary search technique. If found display "Search Successful" and print the element, otherwise display "Search Unsuccessful". {31, 36, 45, 50, 60, 75, 86, 90} |
| ICSE 2019, Q2(e) (2 marks) | What is the difference between the linear search and the binary search technique? |
| ICSE 2019, Q3(i) (2 marks) | `String x[] = {"Artificial intelligence", "IOT", "Machine learning", "Big data"};` Give the output of the following statements: (i) `System.out.println(x[3]);` (ii) `System.out.println(x.length);` |
| ICSE 2019, Q6 (15 marks) | Write a program to input 15 integer elements in an array and sort them in ascending order using the bubble sort technique. |
| ICSE 2018, Q1(b) (2 marks) | Differentiate between searching and sorting. |
| ICSE 2018, Q9 (15 marks) | Write a program to accept name and total marks of N number of students in two single subscript arrays name[] and totalmarks[]. Calculate and print: (i) the average of the total marks obtained by N number of students [average = (sum of total marks of all the students)/N]; (ii) deviation of each student's total marks with the average [deviation = total marks of a student − average]. |
| ICSE 2017, Q1(e) (2 marks) | `String x[] = {"SAMSUNG", "NOKIA", "SONY", "MICROMAX", "BLACKBERRY"};` Give the output of the following statements: (i) `System.out.println(x[1]);` (ii) `System.out.println(x[3].length());` |
| ICSE 2017, Q7 (15 marks) | Write a program to input integer elements into an array of size 20 and perform the following operations: (i) display the largest number from the array; (ii) display the smallest number from the array; (iii) display the sum of all the elements of the array. |

**Solutions**

**2026 Q1(xvii).** **(a) Bubble sort** — each step swaps two **neighbouring** elements, and the largest value, 4, is carried step by step to the end, as in a bubble-sort pass. (With only three elements, selection sort happens to make the same two swaps; the picture of 4 moving along by neighbour swaps is the bubble-sort pattern.) *(Worked answer.)*

**2026 Q2(ix).** (1) `x[0] = x[0] * x[1];` (2) `x[1] = x[0] / x[1];` — x[0] becomes 32, then x[1] = 32 / 8 = 4 and x[0] = 32 / 4 = 8. Output: `8 4`. *(Worked answer.)*

**2026 Q4.** The designations are read one per line with nextLine(), so a designation of two words also works:
```java
import java.util.*;
class Designation
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String d[] = new String[100];
        System.out.println("Enter 100 designations:");
        for (int i = 0; i < d.length; i++)
            d[i] = sc.nextLine();
        System.out.print("Enter the designation to count: ");
        String key = sc.nextLine();
        int count = 0;
        for (int i = 0; i < d.length; i++)
        {
            if (d[i].equals(key))
                count++;
        }
        System.out.println("Number of employees: " + count);
    }
}
```
Sample run — the first six of the 100 designations are those of the example; Manager occurs three times in all:
```
Enter 100 designations:
Trainee
Manager
Chef
Manager
Director
Manager
```
(94 more designations, none of them Manager)
```
Enter the designation to count: Manager
Number of employees: 3
```
`equalsIgnoreCase()` may be used instead of `equals()` so that "manager" also matches. *(Worked answer.)*

**2026 Improvement Q1(ix).** **(a) 5** — the indexes are 0 (4), 1 (3), 2 (7), 3 (9), 4 (120), 5 (−12). *(Worked answer.)*

**2026 Improvement Q1(v).** **(a) 80 bytes** — 10 doubles × 8 bytes. *(Worked answer.)*

**2026 Improvement Q1(xvii).** **(c) A H L W S** — the second pass finds the smallest of S L W H, which is H, and swaps it with S at index 1. *(Worked answer.)*

**2026 Improvement Q2(iv).** **Searching** finds whether a given value is present in the array and at which position (linear or binary search). **Sorting** arranges the elements of the array in ascending or descending order (bubble or selection sort). *(Worked answer.)*

**2025 Q1(iii).** **(d) 32** — 4 doubles × 8 bytes.

**2025 Q1(xiii).** **(d) ar.length-1**

**2025 Q2(viii).** (a) **14** — 12 + 2. (b) **0** — the largest element, 12, is a[0].

**2025 Q6.** The marking scheme sets `l = ch.length` and loops `while (f < l)`; run on all eleven characters, that version fails to find H, S, Y and b. The correct bounds are `l = ch.length - 1` and `while (f <= l)`:
```java
import java.util.*;
class CharSearch
{
    public static void main(String args[])
    {
        char ch[] = {'A', 'H', 'N', 'P', 'S', 'U', 'W', 'Y', 'Z', 'b', 'd'};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the character to be searched: ");
        char n = sc.next().charAt(0);
        int f = 0, l = ch.length - 1, m;
        boolean found = false;
        while (f <= l)
        {
            m = (f + l) / 2;
            if (ch[m] == n)
            {
                found = true;
                break;
            }
            else if (ch[m] < n)
                f = m + 1;
            else
                l = m - 1;
        }
        if (found)
            System.out.println("Search Successful");
        else
            System.out.println("Search is not Successful");
    }
}
```
Sample runs:
```
Enter the character to be searched: H
Search Successful
```
```
Enter the character to be searched: B
Search is not Successful
```
'b' and 'B' are different characters. The examiners noted these errors: linear search used instead of binary search, the array accepted instead of initialised, integers used for characters, `length()` written for length, characters compared with equals() instead of ==, mid not calculated, and first and last updated wrongly.

**2025 Improvement Q2(ix).** (a) **12 bytes** — 6 chars × 2 bytes. (b) **true** — ch[4] is '7'. *(Worked answer.)*

**2025 Improvement Q8.**
```java
import java.util.*;
class LinearSearch
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[10];
        System.out.println("Enter 10 integers:");
        for (int i = 0; i < a.length; i++)
            a[i] = sc.nextInt();
        System.out.print("Enter the value to search: ");
        int key = sc.nextInt();
        int pos = -1;
        for (int i = 0; i < a.length; i++)
        {
            if (a[i] == key)
            {
                pos = i;
                break;
            }
        }
        if (pos >= 0)
            System.out.println(key + " found at index " + pos);
        else
            System.out.println(key + " not found");
    }
}
```
Sample runs:
```
Enter 10 integers:
14 7 23 9 41 6 18 30 11 25
Enter the value to search: 18
18 found at index 6
```
```
Enter 10 integers:
14 7 23 9 41 6 18 30 11 25
Enter the value to search: 99
99 not found
```
*(Worked answer.)*

**2025 specimen Q1(ix).** **(b) 130** — 'A' is 65, and 65 × 2 = 130.

**2025 specimen Q1(xi).** **(c) x[49]=100**

**2025 specimen Q1(xviii).** **(a) s.length**

**2025 specimen Q4.** The draft scheme starts with `l = x.length`; it should be `x.length - 1`:
```java
import java.util.*;
class DoubleBinary
{
    public static void main(String args[])
    {
        double x[] = {5.6, 11.5, 20.8, 35.4, 43.1, 52.4, 66.6, 78.9, 80.0, 95.5};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value to search: ");
        double n = sc.nextDouble();
        int f = 0, l = x.length - 1, m;
        boolean found = false;
        while (f <= l)
        {
            m = (f + l) / 2;
            if (x[m] == n)
            {
                found = true;
                break;
            }
            else if (x[m] < n)
                f = m + 1;
            else
                l = m - 1;
        }
        if (found)
            System.out.println("Search successful");
        else
            System.out.println("Search element not found");
    }
}
```
Sample runs:
```
Enter the value to search: 66.6
Search successful
```
```
Enter the value to search: 50
Search element not found
```

**2024 Q1(xix).** **(a) 6** — "Violet" has 6 characters.

**2024 Q7.** A class name cannot contain a space, so the class is named pincode (the scheme uses pincodes):
```java
class pincode
{
    public static void main(String args[])
    {
        int arr[] = {110061, 110001, 110029, 110023, 110055, 110006, 110019, 110033};
        int n = arr.length;
        for (int i = 0; i < n - 1; i++)
        {
            int min = i;
            for (int j = i + 1; j < n; j++)
            {
                if (arr[j] < arr[min])
                    min = j;
            }
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
        System.out.println("Sorted pin codes:");
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
}
```
Output:
```
Sorted pin codes:
110001 110006 110019 110023 110029 110033 110055 110061
```
The examiners noted that many candidates wrote insertion or bubble sort instead of selection sort, did not initialise the array, inverted the comparison, swapped wrongly, or did not display the sorted array with a loop.

**2024 specimen Q1(v).** **(a) 20 bytes** — 10 chars × 2 bytes. *(Worked answer.)*

**2024 specimen Q1(x).** **(a) X[4]** *(Worked answer.)*

**2024 specimen Q2(x).** (a) **7** (4 + 3). (b) First element at index **0**, last at index **6**. *(Worked answer.)*

**2024 specimen Q4.**
```java
import java.util.*;
class SelectionSort
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[10];
        System.out.println("Enter 10 integers:");
        for (int i = 0; i < a.length; i++)
            a[i] = sc.nextInt();
        for (int i = 0; i < a.length - 1; i++)
        {
            int min = i;
            for (int j = i + 1; j < a.length; j++)
            {
                if (a[j] < a[min])
                    min = j;
            }
            int t = a[i];
            a[i] = a[min];
            a[min] = t;
        }
        System.out.print("Sorted: ");
        for (int i = 0; i < a.length; i++)
            System.out.print(a[i] + " ");
        System.out.println();
    }
}
```
Sample run:
```
Enter 10 integers:
42 7 19 3 88 25 61 14 9 50
Sorted: 3 7 9 14 19 25 42 50 61 88
```
*(Worked answer.)*

**2023 Q2(viii).** (a) **7** (b) **72**

**2023 Q4.** A copy of the original array is kept so that both can be displayed:
```java
import java.util.*;
class BubbleChars
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        char a[] = new char[10];
        char orig[] = new char[10];
        System.out.println("Enter 10 characters:");
        for (int i = 0; i < a.length; i++)
        {
            a[i] = sc.next().charAt(0);
            orig[i] = a[i];
        }
        for (int i = 0; i < a.length - 1; i++)
        {
            for (int j = 0; j < a.length - 1 - i; j++)
            {
                if (a[j] > a[j + 1])
                {
                    char t = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = t;
                }
            }
        }
        System.out.print("Original array: ");
        for (int i = 0; i < orig.length; i++)
            System.out.print(orig[i] + " ");
        System.out.println();
        System.out.print("Sorted array  : ");
        for (int i = 0; i < a.length; i++)
            System.out.print(a[i] + " ");
        System.out.println();
    }
}
```
Sample run (characters sort by their codes: digits, then capitals, then small letters):
```
Enter 10 characters:
q d M a Z k 7 B x c
Original array: q d M a Z k 7 B x c
Sorted array  : 7 B M Z a c d k q x
```
The scheme prints the original array before sorting, which also meets the question. The examiners noted that most candidates declared an int array instead of a char array, read the characters wrongly, swapped wrongly, or did not print the sorted array.

**2023 Q7.**
```java
import java.util.*;
class LinearDouble
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        double a[] = new double[20];
        System.out.println("Enter 20 numbers:");
        for (int i = 0; i < a.length; i++)
            a[i] = sc.nextDouble();
        System.out.print("Enter the number to search: ");
        double s = sc.nextDouble();
        boolean flag = false;
        for (int i = 0; i < a.length; i++)
        {
            if (a[i] == s)
            {
                System.out.println("Found at position " + (i + 1));
                flag = true;
                break;
            }
        }
        if (!flag)
            System.out.println("not found");
    }
}
```
Sample run (9.1 is the 14th value):
```
Enter 20 numbers:
2.5 7.1 3.3 9.9 4.4 1.2 8.8 6.6 5.5 0.7 12.5 3.6 7.7 9.1 2.2 4.8 6.3 8.4 1.9 5.0
Enter the number to search: 9.1
Found at position 14
```
The scheme accepts the position as i + 1 or i. The examiners noted these errors: an int array instead of double, size 10 instead of 20, the search value not accepted, no break after setting the flag, the "not found" message missing, and binary search used instead of linear.

**2023 Q8.** The expressions are built as Strings so that the output matches the example:
```java
import java.util.*;
class DigitSums
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[10];
        System.out.println("Enter 10 integers:");
        for (int i = 0; i < a.length; i++)
            a[i] = sc.nextInt();
        int s1 = 0, s2 = 0;
        String e1 = "", e2 = "";
        for (int i = 0; i < a.length; i++)
        {
            if (a[i] >= 0 && a[i] <= 9)
            {
                s1 = s1 + a[i];
                e1 = e1 + (e1.equals("") ? "" : " + ") + a[i];
            }
            else if (a[i] >= 10 && a[i] <= 99)
            {
                s2 = s2 + a[i];
                e2 = e2 + (e2.equals("") ? "" : " + ") + a[i];
            }
        }
        System.out.println("Sum of one digit numbers : " + e1 + " = " + s1);
        System.out.println("Sum of two digit numbers : " + e2 + " = " + s2);
    }
}
```
Sample run:
```
Enter 10 integers:
2 12 4 9 18 25 3 32 20 1
Sum of one digit numbers : 2 + 4 + 9 + 3 + 1 = 19
Sum of two digit numbers : 12 + 18 + 25 + 32 + 20 = 107
```
The scheme prints only the two sums, and it accepts other correct logic. The examiners noted that many candidates treated every number that was not one-digit as two-digit, used || instead of &&, or printed inside the loop.

**2020 Q5.**
```java
import java.util.*;
class IntBinary
{
    public static void main(String args[])
    {
        int a[] = {31, 36, 45, 50, 60, 75, 86, 90};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number to search: ");
        int n = sc.nextInt();
        int low = 0, high = a.length - 1, pos = -1;
        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (a[mid] == n)
            {
                pos = mid;
                break;
            }
            else if (a[mid] < n)
                low = mid + 1;
            else
                high = mid - 1;
        }
        if (pos != -1)
            System.out.println("Search Successful: " + a[pos]);
        else
            System.out.println("Search Unsuccessful");
    }
}
```
Sample runs:
```
Enter the number to search: 75
Search Successful: 75
```
```
Enter the number to search: 40
Search Unsuccessful
```
*(Worked answer.)*

**2019 Q2(e).** From the scheme:
- Linear search: the array need not be sorted; binary search: the array must be sorted in ascending or descending order.
- Linear search checks each item, in sequence from index 0; binary search does not check each item.
- Binary search checks the search value against the middle value and divides the array into two halves.

**2019 Q3(i).** (i) **Big data** (ii) **4**

**2019 Q6.** As in the scheme, with the display loop added — the scheme sorts the array but never prints it:
```java
import java.util.*;
class Bubble15
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[15];
        System.out.println("Enter 15 integers:");
        for (int i = 0; i < a.length; i++)
            a[i] = sc.nextInt();
        for (int i = 0; i < a.length - 1; i++)
        {
            for (int j = 0; j < a.length - 1 - i; j++)
            {
                if (a[j] > a[j + 1])
                {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
            }
        }
        System.out.print("Sorted: ");
        for (int i = 0; i < a.length; i++)
            System.out.print(a[i] + " ");
        System.out.println();
    }
}
```
Sample run:
```
Enter 15 integers:
34 12 89 5 67 23 1 45 90 17 8 56 3 72 29
Sorted: 1 3 5 8 12 17 23 29 34 45 56 67 72 89 90
```
The examiners noted these errors: the array not created properly, input without a loop, wrong loop limits (i <= 15, j <= 15), and a swap that lost a value.

**2018 Q1(b).** **Searching** is finding an element in an array; **sorting** is arranging the elements in an order.

**2018 Q9.** The scheme reads each name with nextLine() straight after nextInt() or nextDouble(); that nextLine() returns the empty rest of the line, so the names are lost. The version below reads the leftover line first:
```java
import java.util.*;
class Deviation
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of students: ");
        int n = sc.nextInt();
        sc.nextLine();
        String name[] = new String[n];
        double totalmarks[] = new double[n];
        double sum = 0;
        for (int i = 0; i < n; i++)
        {
            System.out.print("Name: ");
            name[i] = sc.nextLine();
            System.out.print("Total marks: ");
            totalmarks[i] = sc.nextDouble();
            sc.nextLine();
            sum = sum + totalmarks[i];
        }
        double avg = sum / n;
        System.out.println("Average = " + Math.round(avg * 100) / 100.0);
        System.out.println("Deviation of each student from the average:");
        for (int i = 0; i < n; i++)
            System.out.println(name[i] + " : " + Math.round((totalmarks[i] - avg) * 100) / 100.0);
    }
}
```
Sample run:
```
Enter the number of students: 3
Name: Kong Dari
Total marks: 420
Name: Bah Shai
Total marks: 365
Name: Aiti Lyngdoh
Total marks: 455
Average = 413.33
Deviation of each student from the average:
Kong Dari : 6.67
Bah Shai : -48.33
Aiti Lyngdoh : 41.67
```
The examiners noted these errors: N read after the arrays were created, name[] used without an index, the average calculated inside the input loop, and the deviations not displayed for each student.

**2017 Q1(e).** (i) **NOKIA** (ii) **8** — "MICROMAX" has 8 letters. *(Worked answer.)*

**2017 Q7.** The largest and smallest start from a[0]:
```java
import java.util.*;
class ArrayStats
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[20];
        System.out.println("Enter 20 integers:");
        for (int i = 0; i < a.length; i++)
            a[i] = sc.nextInt();
        int max = a[0], min = a[0], sum = 0;
        for (int i = 0; i < a.length; i++)
        {
            if (a[i] > max)
                max = a[i];
            if (a[i] < min)
                min = a[i];
            sum = sum + a[i];
        }
        System.out.println("Largest  : " + max);
        System.out.println("Smallest : " + min);
        System.out.println("Sum      : " + sum);
    }
}
```
Sample run:
```
Enter 20 integers:
15 -4 23 8 42 16 7 31 0 19 11 5 28 3 36 9 -12 21 14 6
Largest  : 42
Smallest : -12
Sum      : 278
```
*(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Give the output: `int e[] = {2, 4, 6}; System.out.println(e[e.length - 1] + e[0]);`
**Answer:** `8` — 6 + 2.

**Q2.** (2 marks) What happens when `int a[] = {1, 2, 3}; System.out.println(a[3]);` runs?
**Answer:** It compiles, but stops at run time with ArrayIndexOutOfBoundsException — the valid indexes are 0 to 2.

**Q3.** (2 marks) How many comparisons does bubble sort make in all for 5 elements?
**Answer:** 4 + 3 + 2 + 1 = 10.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 15 marks | Binary search on a given sorted int, double or char array | 8.2, Section 11 |
| 15 marks | Bubble or selection sort of input or given values, then display | 8.2 |
| 15 marks | Linear search with position, or count/sum/largest over an array | 8.2, Section 11 |
| MCQ / 2 marks | Bytes occupied; last index; length; output of a[i] expressions | 8.2, 5.1 |

---
## 9. MCQs with Explanations

### Array basics (Q1–Q16)

**Q1.** An array is a collection of
- (a) elements of different data types
- (b) elements of the same data type under one name
- (c) methods of a class
- (d) packages

**Answer:** (b) elements of the same data type under one name
**Explanation:** Elements are reached by index.

**Q2.** The index of the first element of an array is
- (a) −1
- (b) 1
- (c) 0
- (d) the length

**Answer:** (c) 0
**Explanation:** Java counts from 0.

**Q3.** The index (subscript) of the last element of an array ar[] is
- (a) ar.length()
- (b) ar[].length
- (c) ar.length()-1
- (d) ar.length-1

**Answer:** (d) ar.length-1
**Explanation:** Indexes run from 0 to length − 1.

**Q4.** The correct statement to create an int array of 10 elements is
- (a) int a[10];
- (b) int a = new int[10];
- (c) int a[] = new int[10];
- (d) int a[] = int[10];

**Answer:** (c) int a[] = new int[10];
**Explanation:** new allocates the elements.

**Q5.** A single-dimensional array has 50 elements. The statement to set the last element to 100 is
- (a) x[51] = 100
- (b) x[48] = 100
- (c) x[49] = 100
- (d) x[50] = 100

**Answer:** (c) x[49] = 100
**Explanation:** The last index is 49.

**Q6.** The Java statement to access the 5th element of array X is
- (a) X[4]
- (b) X[5]
- (c) X[3]
- (d) X[0]

**Answer:** (a) X[4]
**Explanation:** The 5th element has index 4.

**Q7.** After int p[] = new int[5];, the value of p[2] is
- (a) 0
- (b) garbage
- (c) null
- (d) 2

**Answer:** (a) 0
**Explanation:** Default value for int elements.

**Q8.** After String ss[] = new String[2];, the value of ss[0] is
- (a) ""
- (b) null
- (c) 0
- (d) " "

**Answer:** (b) null
**Explanation:** Object elements default to null.

**Q9.** int a[] = new int[3]; a = {1, 2, 3}; gives
- (a) a = {0, 0, 0}
- (b) a = {1, 2, 3}
- (c) a run-time error
- (d) a compile error

**Answer:** (d) a compile error
**Explanation:** An initialiser list is allowed only in a declaration.

**Q10.** int a[] = {1, 2, 3}; System.out.println(a[3]); gives
- (a) 3
- (b) 0
- (c) ArrayIndexOutOfBoundsException at run time
- (d) a compile error

**Answer:** (c) ArrayIndexOutOfBoundsException at run time
**Explanation:** Valid indexes are 0 to 2.

**Q11.** Which is a valid declaration?
- (a) x[] double = new double[3];
- (b) double x = {2.5, 4.5};
- (c) double[3] x;
- (d) double x[] = {2.5, 4.5, 5.5};

**Answer:** (d) double x[] = {2.5, 4.5, 5.5};
**Explanation:** Declared and initialised together.

**Q12.** The size of an array, once created,
- (a) grows automatically
- (b) is fixed
- (c) shrinks when elements are removed
- (d) doubles on overflow

**Answer:** (b) is fixed
**Explanation:** A new array is needed for a different size.

**Q13.** The elements of an array are stored in
- (a) the keyboard buffer
- (b) random places
- (c) different files
- (d) consecutive memory locations

**Answer:** (d) consecutive memory locations
**Explanation:** One after another.

**Q14.** To read a character into ch[i] with Scanner sc, the statement is
- (a) ch[i] = sc.nextLine();
- (b) ch[i] = sc.nextChar();
- (c) ch[i] = sc.next().charAt(0);
- (d) ch = sc.next();

**Answer:** (c) ch[i] = sc.next().charAt(0);
**Explanation:** Scanner has no nextChar().

**Q15.** An array of the marks of 40 students is better than 40 variables because
- (a) one loop can process all the marks
- (b) arrays use no memory
- (c) arrays need no index
- (d) variables cannot store marks

**Answer:** (a) one loop can process all the marks
**Explanation:** One name, many elements.

**Q16.** After int q[] = {3, 6, 9}; int r[] = q; r[1] = 60;, the value of q[1] is
- (a) 6
- (b) 60
- (c) 0
- (d) an error

**Answer:** (b) 60
**Explanation:** q and r refer to the same array.

### Length and memory (Q17–Q28)

**Q17.** The number of elements of an array a is given by
- (a) length(a)
- (b) a.length()
- (c) a.length
- (d) a.size()

**Answer:** (c) a.length
**Explanation:** A property, without brackets.

**Q18.** The statement to find the total number of Strings in the array String s[] is
- (a) s.length()
- (b) s.length
- (c) length(s)
- (d) len(s)

**Answer:** (b) s.length
**Explanation:** ICSE 2025 specimen Q1(xviii).

**Q19.** int a[] = {1, 2, 3}; System.out.println(a.length()); gives
- (a) 3
- (b) the error: cannot find symbol
- (c) 2
- (d) a run-time error

**Answer:** (b) the error: cannot find symbol
**Explanation:** length has no brackets for arrays.

**Q20.** double x[] = {2.5, 4.5, 5.5, 6.4}; occupies
- (a) 16 bytes
- (b) 4 bytes
- (c) 8 bytes
- (d) 32 bytes

**Answer:** (d) 32 bytes
**Explanation:** 4 × 8.

**Q21.** An array of 10 decimal (double) values occupies
- (a) 8 bytes
- (b) 320 bytes
- (c) 10 bytes
- (d) 80 bytes

**Answer:** (d) 80 bytes
**Explanation:** 10 × 8.

**Q22.** A character array of 10 elements occupies
- (a) 20 bytes
- (b) 60 bytes
- (c) 40 bytes
- (d) 120 bytes

**Answer:** (a) 20 bytes
**Explanation:** 10 × 2.

**Q23.** char ch[] = {'A', '%', 'y', '@', '7', 'p'}; occupies
- (a) 6 bytes
- (b) 12 bytes
- (c) 24 bytes
- (d) 48 bytes

**Answer:** (b) 12 bytes
**Explanation:** 6 × 2.

**Q24.** int a[] = {12, 10, 8, 4, 6, 2, 3, 5, 7}; occupies
- (a) 9 bytes
- (b) 18 bytes
- (c) 36 bytes
- (d) 72 bytes

**Answer:** (c) 36 bytes
**Explanation:** 9 × 4.

**Q25.** long n[] = new long[6]; occupies
- (a) 24 bytes
- (b) 48 bytes
- (c) 6 bytes
- (d) 12 bytes

**Answer:** (b) 48 bytes
**Explanation:** 6 × 8.

**Q26.** For int x[] = {4, 7, 9, 66, 72, 0, 16};, x.length and x[4] are
- (a) 7 and 72
- (b) 6 and 66
- (c) 7 and 66
- (d) 6 and 72

**Answer:** (a) 7 and 72
**Explanation:** Seven elements; index 4 holds 72.

**Q27.** int P[] = {12, 14, 16, 18}; int Q[] = {20, 22, 24}; An array R holding all of them has size
- (a) 4
- (b) 3
- (c) 7
- (d) 12

**Answer:** (c) 7
**Explanation:** 4 + 3.

**Q28.** In R of size 7, the indexes of the first and last elements are
- (a) 0 and 7
- (b) 1 and 7
- (c) 0 and 6
- (d) 1 and 6

**Answer:** (c) 0 and 6
**Explanation:** 0 to length − 1.

### Outputs with arrays (Q29–Q40)

**Q29.** int a[] = {12, 10, 8, 4, 6, 2, 3, 5, 7}; System.out.print(a[0] + a[5]); prints
- (a) 18
- (b) 122
- (c) 14
- (d) 10

**Answer:** (c) 14
**Explanation:** 12 + 2.

**Q30.** In the same array, the index of the largest element is
- (a) 0
- (b) 8
- (c) 1
- (d) 4

**Answer:** (a) 0
**Explanation:** 12 is a[0].

**Q31.** char ch[] = {'A', 'E', 'I', 'O', 'U'}; System.out.println(ch[0] * 2); prints
- (a) 65
- (b) 130
- (c) AA
- (d) 0

**Answer:** (b) 130
**Explanation:** 'A' is 65.

**Q32.** String color[] = {"Blue", "Red", "Violet"}; System.out.println(color[2].length()); prints
- (a) 2
- (b) 5
- (c) 3
- (d) 6

**Answer:** (d) 6
**Explanation:** "Violet" has 6 letters.

**Q33.** String x[] = {"Artificial intelligence", "IOT", "Machine learning", "Big data"}; x[3] and x.length are
- (a) Machine learning and 4
- (b) Big data and 4
- (c) Big data and 3
- (d) IOT and 4

**Answer:** (b) Big data and 4
**Explanation:** Index 3 is the fourth String.

**Q34.** String x[] = {"SAMSUNG", "NOKIA", "SONY", "MICROMAX", "BLACKBERRY"}; x[1] and x[3].length() are
- (a) SONY and 8
- (b) SAMSUNG and 4
- (c) NOKIA and 4
- (d) NOKIA and 8

**Answer:** (d) NOKIA and 8
**Explanation:** "MICROMAX" has 8 letters.

**Q35.** For char ch[] = {'A', '%', 'y', '@', '7', 'p'};, Character.isDigit(ch[4]) gives
- (a) an error
- (b) false
- (c) 7
- (d) true

**Answer:** (d) true
**Explanation:** ch[4] is '7'.

**Q36.** int x[] = {4, 3, 7, 9, 120, -12, 8}; The index of the negative number is
- (a) 6
- (b) 5
- (c) 4
- (d) x.length

**Answer:** (b) 5
**Explanation:** −12 is the sixth element.

**Q37.** int e[] = {2, 4, 6}; System.out.println(e[e.length - 1] + e[0]); prints
- (a) 8
- (b) 62
- (c) 6
- (d) 10

**Answer:** (a) 8
**Explanation:** 6 + 2.

**Q38.** int x[] = {4, 8, 19, 24, 15}; after x[0] = x[0] * x[1]; x[1] = x[0] / x[1]; x[0] = x[0] / x[1]; the values of x[0] and x[1] are
- (a) 32 and 4
- (b) 4 and 8
- (c) 8 and 4
- (d) 32 and 8

**Answer:** (c) 8 and 4
**Explanation:** The two elements are swapped.

**Q39.** int q[] = {3, 60, 9}; the sum of its elements found by a loop is
- (a) 72
- (b) 18
- (c) 69
- (d) 63

**Answer:** (a) 72
**Explanation:** 3 + 60 + 9.

**Q40.** double d[] = new double[3]; boolean bb[] = new boolean[2]; d[0] and bb[1] are
- (a) null and false
- (b) 0 and true
- (c) 0.0 and false
- (d) 0.0 and null

**Answer:** (c) 0.0 and false
**Explanation:** Default values.

### Searching (Q41–Q58)

**Q41.** Finding whether a value is present in an array is
- (a) sorting
- (b) searching
- (c) merging
- (d) boxing

**Answer:** (b) searching
**Explanation:** Sorting arranges values.

**Q42.** Linear search
- (a) checks only the middle element
- (b) needs a sorted array
- (c) checks each element in turn from the start
- (d) swaps elements

**Answer:** (c) checks each element in turn from the start
**Explanation:** Element by element.

**Q43.** Binary search requires the array to be
- (a) unsorted
- (b) of type int only
- (c) of odd length
- (d) sorted

**Answer:** (d) sorted
**Explanation:** It discards half each step.

**Q44.** In binary search, the first value of high is
- (a) 0
- (b) a.length
- (c) a.length - 1
- (d) a.length + 1

**Answer:** (c) a.length - 1
**Explanation:** The last valid index.

**Q45.** The loop condition of binary search is
- (a) high < 0
- (b) low > high
- (c) low == high
- (d) low <= high

**Answer:** (d) low <= high
**Explanation:** Stop when the range is empty.

**Q46.** If a[mid] < key in an ascending array, the next step is
- (a) high = mid + 1
- (b) high = mid - 1
- (c) low = mid - 1
- (d) low = mid + 1

**Answer:** (d) low = mid + 1
**Explanation:** The key is in the right half.

**Q47.** When the middle element is greater than the key in an ascending array, binary search next sets
- (a) low = mid + 1
- (b) high = mid - 1
- (c) mid = mid + 1
- (d) high = low

**Answer:** (b) high = mid - 1
**Explanation:** The key is in the left half.

**Q48.** Searching 75 in {31, 36, 45, 50, 60, 75, 86, 90}, the first mid is
- (a) 3
- (b) 4
- (c) 5
- (d) 7

**Answer:** (a) 3
**Explanation:** (0 + 7) / 2.

**Q49.** In the same search, 75 is found when mid is
- (a) 3
- (b) 4
- (c) 6
- (d) 5

**Answer:** (d) 5
**Explanation:** Second step: (4 + 7) / 2.

**Q50.** Searching 40 in the same array checks the elements
- (a) 50, 36, 45
- (b) 31, 36, 45
- (c) 50, 60, 75
- (d) 45 only

**Answer:** (a) 50, 36, 45
**Explanation:** mid = 3, 1, 2, then low > high.

**Q51.** Characters in a binary search are compared with
- (a) == and <
- (b) equals()
- (c) compareTo()
- (d) length

**Answer:** (a) == and <
**Explanation:** char is a primitive type.

**Q52.** Strings in a binary search are compared with
- (a) ==
- (b) compareTo()
- (c) <
- (d) charAt()

**Answer:** (b) compareTo()
**Explanation:** It returns negative, zero or positive.

**Q53.** In linear search, "not found" should be printed
- (a) never
- (b) inside the loop at each mismatch
- (c) before the loop
- (d) after the loop, if no match was found

**Answer:** (d) after the loop, if no match was found
**Explanation:** Otherwise it prints many times.

**Q54.** A flag variable in linear search
- (a) records whether the value was found
- (b) counts the passes
- (c) stores the array size
- (d) sorts the array

**Answer:** (a) records whether the value was found
**Explanation:** Checked after the loop.

**Q55.** Which statement is TRUE?
- (a) Binary search is faster than linear search for a large sorted array.
- (b) Linear search needs a sorted array.
- (c) Binary search checks every element.
- (d) Linear search starts from the middle.

**Answer:** (a) Binary search is faster than linear search for a large sorted array.
**Explanation:** It halves the range each step.

**Q56.** The 2025 scheme's binary search used l = ch.length and while (f < l). Its effect was that
- (a) every search succeeded
- (b) some characters present in the array were not found
- (c) the program would not compile
- (d) it sorted the array

**Answer:** (b) some characters present in the array were not found
**Explanation:** H, S, Y and b are missed.

**Q57.** In linear search on {14, 7, 23, 9, 41, 6, 18, 30, 11, 25}, the value 18 is at index
- (a) 6
- (b) 7
- (c) 5
- (d) 18

**Answer:** (a) 6
**Explanation:** Counting from 0.

**Q58.** The largest number of comparisons binary search needs for 8 elements is about
- (a) 16
- (b) 8
- (c) 3 or 4
- (d) 1

**Answer:** (c) 3 or 4
**Explanation:** 8 → 4 → 2 → 1.

### Sorting (Q59–Q76)

**Q59.** Arranging elements in ascending or descending order is
- (a) sorting
- (b) searching
- (c) indexing
- (d) parsing

**Answer:** (a) sorting
**Explanation:** ICSE 2018 Q1(b).

**Q60.** Bubble sort compares
- (a) neighbouring elements
- (b) the first and last elements only
- (c) the middle element with the key
- (d) each element with the minimum

**Answer:** (a) neighbouring elements
**Explanation:** a[j] with a[j + 1].

**Q61.** Selection sort, in each pass,
- (a) swaps every neighbouring pair
- (b) finds the smallest unsorted element and swaps it into place
- (c) searches for a key
- (d) reverses the array

**Answer:** (b) finds the smallest unsorted element and swaps it into place
**Explanation:** One swap per pass.

**Q62.** The number of passes both sorts need for n elements is
- (a) n − 1
- (b) n
- (c) n + 1
- (d) 2n

**Answer:** (a) n − 1
**Explanation:** The last element is then in place.

**Q63.** After the first pass of bubble sort, {5, 1, 4, 2, 8} becomes
- (a) 1 4 2 5 8
- (b) 1 2 4 5 8
- (c) 1 5 4 2 8
- (d) 5 1 4 2 8

**Answer:** (a) 1 4 2 5 8
**Explanation:** 5 moves right until it meets 8.

**Q64.** After the first pass of selection sort, {29, 10, 14, 37, 13} becomes
- (a) 10 14 29 37 13
- (b) 10 13 14 37 29
- (c) 29 10 14 13 37
- (d) 10 29 14 37 13

**Answer:** (d) 10 29 14 37 13
**Explanation:** The minimum 10 is swapped with 29.

**Q65.** After the second pass of selection sort on the same array, it becomes
- (a) 13 10 14 37 29
- (b) 10 29 14 37 13
- (c) 10 13 14 29 37
- (d) 10 13 14 37 29

**Answer:** (d) 10 13 14 37 29
**Explanation:** 13 is swapped with 29.

**Q66.** W S L A H is selection-sorted alphabetically. After the first pass it is A S L W H. After the second pass it is
- (a) W S L A H
- (b) A H L A S
- (c) A H L W S
- (d) W E L A H

**Answer:** (c) A H L W S
**Explanation:** H, the smallest of S L W H, moves to index 1.

**Q67.** The inner loop of bubble sort for ascending order swaps when
- (a) a[j] < a[j + 1]
- (b) a[j] > a[j + 1]
- (c) a[j] == a[j + 1]
- (d) j > i

**Answer:** (b) a[j] > a[j + 1]
**Explanation:** The larger value moves right.

**Q68.** To sort in descending order with bubble sort, the condition becomes
- (a) a[j] >= 0
- (b) a[j] > a[j + 1]
- (c) a[j] != a[j + 1]
- (d) a[j] < a[j + 1]

**Answer:** (d) a[j] < a[j + 1]
**Explanation:** The smaller value moves right.

**Q69.** In selection sort, the variable min stores
- (a) the smallest value of the whole program
- (b) the index of the smallest element found so far
- (c) the number of passes
- (d) the array length

**Answer:** (b) the index of the smallest element found so far
**Explanation:** It is swapped with a[i] after the inner loop.

**Q70.** A picture shows 4 1 3 → 1 4 3 → 1 3 4, each step swapping neighbours as the 4 moves to the end. The technique is
- (a) selection sort
- (b) linear search
- (c) bubble sort
- (d) binary search

**Answer:** (c) bubble sort
**Explanation:** The largest value is carried along by neighbour swaps.

**Q71.** Sorting the characters q d M a Z k 7 B x c in ascending order gives
- (a) B M Z a c d k q x 7
- (b) a B c d k M q x Z 7
- (c) 7 B M Z a c d k q x
- (d) 7 a B c d k M q x Z

**Answer:** (c) 7 B M Z a c d k q x
**Explanation:** Digits, then capitals, then small letters.

**Q72.** The total number of comparisons bubble sort makes for 5 elements is
- (a) 10
- (b) 5
- (c) 25
- (d) 4

**Answer:** (a) 10
**Explanation:** 4 + 3 + 2 + 1.

**Q73.** The swap in bubble sort is written as
- (a) a[j + 1] = temp; temp = a[j];
- (b) a[j] = a[j + 1]; a[j + 1] = a[j];
- (c) temp = a[j]; a[j + 1] = temp; a[j] = a[j + 1];
- (d) temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp;

**Answer:** (d) temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp;
**Explanation:** The other orders lose a value.

**Q74.** When sorting the marks[] of parallel arrays name[] and marks[], the program must
- (a) swap only the marks
- (b) swap the elements of both arrays together
- (c) sort the names separately
- (d) delete the names

**Answer:** (b) swap the elements of both arrays together
**Explanation:** Otherwise names no longer match marks.

**Q75.** The 2024 examiners' most common error in the pin-code program was
- (a) printing the sorted array
- (b) using an int array
- (c) insertion sort written instead of selection sort
- (d) using a loop

**Answer:** (c) insertion sort written instead of selection sort
**Explanation:** Use the technique named.

**Q76.** Selection-sorting the pin codes 110061, 110001, 110029, 110023, 110055, 110006, 110019, 110033 puts first
- (a) 110019
- (b) 110061
- (c) 110006
- (d) 110001

**Answer:** (d) 110001
**Explanation:** The smallest pin code.
## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** What is an array? Why is it needed?
**Answer:** A collection of elements of the same data type, stored together and referred to by one name with an index.
It lets one loop process many values instead of many separate variables.

**Q2.** Write statements to (i) create an int array of 20 elements and (ii) create and initialise a char array of the vowels.
**Answer:** (i) `int a[] = new int[20];`
(ii) `char v[] = {'a', 'e', 'i', 'o', 'u'};`

**Q3.** Differentiate between searching and sorting.
**Answer:** Searching finds whether a value is present in an array and at which position.
Sorting arranges the elements in ascending or descending order.

**Q4.** State two differences between linear search and binary search.
**Answer:** Linear search works on any array; binary search needs a sorted array.
Linear search checks elements one by one from index 0; binary search checks the middle element and halves the range.

**Q5.** State two differences between bubble sort and selection sort.
**Answer:** Bubble sort compares and swaps neighbouring elements; selection sort finds the minimum of the unsorted part.
Bubble sort may swap many times in a pass; selection sort swaps once per pass.

**Q6.** What is the difference between a.length and s.length() in a program with `int a[]` and `String s`?
**Answer:** a.length (no brackets) is the number of elements in the array.
s.length() (with brackets) is the number of characters in the String.

**Q7.** How is the memory occupied by an array calculated? Find it for `double m[] = new double[12];`.
**Answer:** Number of elements × bytes per element.
12 × 8 = 96 bytes.

**Q8.** What is ArrayIndexOutOfBoundsException? When does it occur?
**Answer:** A run-time error that stops the program.
It occurs when an index outside 0 to length − 1 is used, e.g. a[3] for an array of 3 elements.

**Q9.** Why must binary search start with high = a.length - 1 and loop while low <= high?
**Answer:** a.length - 1 is the last valid index.
With low < high, or high = a.length, some values present in the array are never found.

**Q10.** What are parallel arrays? Give an example.
**Answer:** Arrays whose elements at the same index belong together.
e.g. name[i] and totalmarks[i] are the name and marks of the same student.

**Q11.** Give the default values of the elements of `new int[3]`, `new double[3]` and `new String[3]`.
**Answer:** 0, 0.0.
null.

**Q12.** How is bubble sort changed to sort in descending order?
**Answer:** Swap when `a[j] < a[j + 1]` instead of `a[j] > a[j + 1]`.
The smaller values then move to the end.

### Output and error questions (2 marks each)

**Q13.** `int a[] = {12, 10, 8, 4, 6, 2, 3, 5, 7};` Give the output of `System.out.print(a[0] + a[5]);` and the index of the largest element.
**Answer:** `14`
0 (a[0] = 12).

**Q14.** `int x[] = {4, 8, 19, 24, 15}; x[0] = x[0] * x[1]; x[1] = x[0] / x[1]; x[0] = x[0] / x[1]; System.out.println(x[0] + " " + x[1]);`
**Answer:** `8 4`
The first two elements are swapped without a third variable.

**Q15.** `char ch[] = {'A', 'E', 'I', 'O', 'U'}; System.out.println(ch[0] * 2);`
**Answer:** `130`
'A' is 65.

**Q16.** `String x[] = {"SAMSUNG", "NOKIA", "SONY", "MICROMAX", "BLACKBERRY"}; System.out.println(x[1]); System.out.println(x[3].length());`
**Answer:** `NOKIA`
`8`

**Q17.** `int q[] = {3, 6, 9}; int r[] = q; r[1] = 60;` Give q[1] and the sum of q's elements.
**Answer:** 60
72 (3 + 60 + 9).

**Q18.** Give the array after each pass of bubble sort on {5, 1, 4, 2, 8} until no change remains.
**Answer:** Pass 1: 1 4 2 5 8.
Pass 2: 1 2 4 5 8 (passes 3 and 4 make no change).

**Q19.** Give the array after each pass of selection sort on {29, 10, 14, 37, 13}.
**Answer:** 10 29 14 37 13; 10 13 14 37 29.
10 13 14 37 29; 10 13 14 29 37.

**Q20.** Find the error: `int a[] = {1, 2, 3}; System.out.println(a.length());`
**Answer:** "cannot find symbol" — length of an array has no brackets.
Write `a.length`.

**Q21.** Find the error: `int a[] = new int[3]; a = {1, 2, 3};`
**Answer:** An initialiser list is allowed only in the declaration (javac: illegal start of expression).
Write `int a[] = {1, 2, 3};` or assign the elements one by one.

**Q22.** What happens when `int a[] = {1, 2, 3}; System.out.println(a[3]);` runs?
**Answer:** It compiles but stops with ArrayIndexOutOfBoundsException: Index 3 out of bounds for length 3.
The last valid index is 2.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; the output or a sample run follows each.*

### Section B programs (15 marks each)

**Q1.** Two arrays are given: P = {12, 14, 16, 18} and Q = {20, 22, 24}. Write a program to place all the elements of P and then of Q in a third array R, and print the size of R, its elements, and its first and last elements with their indexes.
**Answer:**
```java
class MergeArrays
{
    public static void main(String args[])
    {
        int P[] = {12, 14, 16, 18};
        int Q[] = {20, 22, 24};
        int R[] = new int[P.length + Q.length];
        for (int i = 0; i < P.length; i++)
            R[i] = P[i];
        for (int i = 0; i < Q.length; i++)
            R[P.length + i] = Q[i];
        System.out.println("Size of R: " + R.length);
        System.out.print("R: ");
        for (int i = 0; i < R.length; i++)
            System.out.print(R[i] + " ");
        System.out.println();
        System.out.println("First element R[0] = " + R[0] + ", last element R[" + (R.length - 1) + "] = " + R[R.length - 1]);
    }
}
```
Output:
```
Size of R: 7
R: 12 14 16 18 20 22 24
First element R[0] = 12, last element R[6] = 24
```

**Q2.** Write a program to input n integers into an array and reverse the array in place (without a second array), then print it.
**Answer:**
```java
import java.util.*;
class ReverseArray
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("How many numbers? ");
        int n = sc.nextInt();
        int a[] = new int[n];
        System.out.println("Enter " + n + " numbers:");
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        for (int i = 0; i < n / 2; i++)
        {
            int t = a[i];
            a[i] = a[n - 1 - i];
            a[n - 1 - i] = t;
        }
        System.out.print("Reversed: ");
        for (int i = 0; i < n; i++)
            System.out.print(a[i] + " ");
        System.out.println();
    }
}
```
Sample run (only n / 2 swaps are needed):
```
How many numbers? 6
Enter 6 numbers:
3 8 1 9 4 7
Reversed: 7 4 9 1 8 3
```

**Q3.** Write a program to input 10 integers and find the largest and the second largest distinct values in one pass, without sorting.
**Answer:**
```java
import java.util.*;
class SecondLargest
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[10];
        System.out.println("Enter 10 integers:");
        for (int i = 0; i < a.length; i++)
            a[i] = sc.nextInt();
        int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
        for (int i = 0; i < a.length; i++)
        {
            if (a[i] > first)
            {
                second = first;
                first = a[i];
            }
            else if (a[i] > second && a[i] != first)
                second = a[i];
        }
        System.out.println("Largest        : " + first);
        if (second == Integer.MIN_VALUE)
            System.out.println("No second largest value");
        else
            System.out.println("Second largest : " + second);
    }
}
```
Sample run (78 occurs twice; the second largest distinct value is 70):
```
Enter 10 integers:
45 12 78 33 78 9 64 21 50 70
Largest        : 78
Second largest : 70
```

**Q4.** Write a program to input the names and marks of 5 students in two parallel arrays and print a rank list in descending order of marks, using selection sort and swapping both arrays together.
**Answer:**
```java
import java.util.*;
class RankList
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String name[] = new String[5];
        int marks[] = new int[5];
        for (int i = 0; i < 5; i++)
        {
            System.out.print("Name and marks: ");
            name[i] = sc.next();
            marks[i] = sc.nextInt();
        }
        for (int i = 0; i < 4; i++)
        {
            int max = i;
            for (int j = i + 1; j < 5; j++)
            {
                if (marks[j] > marks[max])
                    max = j;
            }
            int tm = marks[i];
            marks[i] = marks[max];
            marks[max] = tm;
            String tn = name[i];
            name[i] = name[max];
            name[max] = tn;
        }
        System.out.println("Rank list:");
        for (int i = 0; i < 5; i++)
            System.out.println((i + 1) + ". " + name[i] + " " + marks[i]);
    }
}
```
Sample run:
```
Name and marks: Aibor 72
Name and marks: Banri 88
Name and marks: Daiaphi 65
Name and marks: Kyrmen 91
Name and marks: Risa 80
Rank list:
1. Kyrmen 91
2. Banri 88
3. Risa 80
4. Aibor 72
5. Daiaphi 65
```

**Q5.** The capitals of the north-eastern states are stored in alphabetical order: Agartala, Aizawl, Dispur, Gangtok, Imphal, Itanagar, Kohima, Shillong. Write a program to search for a capital input by the user using binary search with compareTo().
**Answer:**
```java
import java.util.*;
class CapitalSearch
{
    public static void main(String args[])
    {
        String city[] = {"Agartala", "Aizawl", "Dispur", "Gangtok", "Imphal", "Itanagar", "Kohima", "Shillong"};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a capital to search: ");
        String key = sc.nextLine();
        int low = 0, high = city.length - 1, pos = -1;
        while (low <= high)
        {
            int mid = (low + high) / 2;
            int c = key.compareTo(city[mid]);
            if (c == 0)
            {
                pos = mid;
                break;
            }
            else if (c > 0)
                low = mid + 1;
            else
                high = mid - 1;
        }
        if (pos >= 0)
            System.out.println(key + " found at index " + pos);
        else
            System.out.println(key + " is not in the list");
    }
}
```
Sample runs:
```
Enter a capital to search: Shillong
Shillong found at index 7
```
```
Enter a capital to search: Guwahati
Guwahati is not in the list
```

**Q6.** Write a program to input the marks (out of 10) of 15 students and print how many students scored each mark, from 10 down to 0, skipping marks no one scored. Use a counting array freq[] in which freq[k] counts the mark k.
**Answer:**
```java
import java.util.*;
class MarkFrequency
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int m[] = new int[15];
        int freq[] = new int[11];          // freq[k] counts the mark k (0 to 10)
        System.out.println("Enter 15 marks out of 10:");
        for (int i = 0; i < m.length; i++)
        {
            m[i] = sc.nextInt();
            if (m[i] >= 0 && m[i] <= 10)
                freq[m[i]]++;
        }
        System.out.println("Mark  Students");
        for (int k = 10; k >= 0; k--)
        {
            if (freq[k] > 0)
                System.out.println(k + "     " + freq[k]);
        }
    }
}
```
Sample run:
```
Enter 15 marks out of 10:
7 9 10 6 7 8 9 7 5 10 8 7 9 6 8
Mark  Students
10     2
9     3
8     3
7     4
6     2
5     1
```

---

## 12. Competency / Application Questions

**Q1. (Choose the search)** A shop has 5000 product codes in ascending order. Which search should the billing program use, and why?
**Model answer:** Binary search — the list is sorted and large, so it needs only about 13 comparisons instead of up to 5000.

**Q2. (Choose the type)** A question asks to store the heights of 30 plants in metres, such as 1.25. Declare the array.
**Model answer:** `double h[] = new double[30];`

**Q3. (Fix the search)** A binary search starts with `high = a.length` and loops `while (low < high)`. What can go wrong?
**Model answer:** Some values present in the array are never found; use `high = a.length - 1` and `while (low <= high)`.

**Q4. (Keep the pairs)** A program sorts marks[] but not name[]. What is wrong with the printed rank list?
**Model answer:** The names no longer match their marks; swap name[] along with marks[].

**Q5. (Memory)** How many bytes do the elements of `char grade[] = new char[40];` and `long phone[] = new long[40];` occupy?
**Model answer:** 80 bytes and 320 bytes.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** The last element of an array a is a[a.length - 1].
**R:** Array indexes start at 0.
**Answer:** (c)
**Explanation:** n elements have indexes 0 to n − 1.

**Q2.**
**A:** Binary search can be used on any array.
**R:** Binary search compares the key with the middle element.
**Answer:** (b)
**Explanation:** The array must be sorted.

**Q3.**
**A:** `double x[] = {2.5, 4.5, 5.5, 6.4};` occupies 32 bytes.
**R:** A double occupies 8 bytes.
**Answer:** (c)
**Explanation:** 4 × 8.

**Q4.**
**A:** Selection sort makes one swap in each pass.
**R:** Bubble sort compares neighbouring elements.
**Answer:** (d)
**Explanation:** Both true; R is about the other sort.

**Q5.**
**A:** `a.length()` gives the number of elements of an array.
**R:** length of an array is a property, not a method.
**Answer:** (b)
**Explanation:** Write a.length.

**Q6.**
**A:** Using a[5] in an array of 5 elements causes a run-time error.
**R:** The valid indexes are 0 to 4.
**Answer:** (c)
**Explanation:** ArrayIndexOutOfBoundsException.

**Q7.**
**A:** After `int r[] = q; r[1] = 60;`, q[1] is 60.
**R:** r is a separate copy of q.
**Answer:** (a)
**Explanation:** r and q refer to the same array.

**Q8.**
**A:** Bubble sort needs n − 1 passes for n elements.
**R:** After each pass, the largest remaining element is in its final place.
**Answer:** (c)
**Explanation:** After n − 1 passes all are placed.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The pin-code list

> Eight pin codes, from 110061 to 110033, are stored in an int array and sorted by selection sort.

**(i)** How many passes are needed?
**Answer:** 7.

**(ii)** Which pin code is placed first after pass 1?
**Answer:** 110001.

**(iii)** How many bytes do the eight ints occupy?
**Answer:** 32.

**(iv)** After sorting, which search could find a pin code quickly?
**Answer:** Binary search.

### Case 2 — The binary search

> The sorted array {31, 36, 45, 50, 60, 75, 86, 90} is searched for 75.

**(i)** What are low, high and mid at the start?
**Answer:** 0, 7 and 3.

**(ii)** What is done after comparing with a[3] = 50?
**Answer:** low = mid + 1 = 4.

**(iii)** At which index is 75 found?
**Answer:** 5.

**(iv)** How does a search for 40 end?
**Answer:** low becomes greater than high: "Search Unsuccessful".

### Case 3 — The class results

> name[] and totalmarks[] hold the names and totals of N students; the average and each student's deviation are printed.

**(i)** What are such arrays called?
**Answer:** Parallel arrays.

**(ii)** When should the average be calculated — inside or after the input loop?
**Answer:** After the loop, once the sum is complete.

**(iii)** With totals 420, 365, 455, what is the average?
**Answer:** 413.33.

**(iv)** What is the deviation for 455?
**Answer:** 41.67.

---

## 15. Revision Notes

### Chapter at a glance
- Array: same type, one name, index 0 to length − 1; `a.length` without brackets; size fixed.
- Memory = elements × bytes (char 2, int 4, double 8).
- Defaults with new: 0, 0.0, false, null; `{…}` only in a declaration.
- Linear search: any array, one by one; binary search: sorted, low/high/mid, low <= high.
- Bubble sort: neighbours swapped; selection sort: minimum swapped into place; n − 1 passes.
- Parallel arrays: same index, same record — swap together.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| int array for characters or decimals | Use the type in the question: char, double. |
| `a.length()` | `a.length` |
| `high = a.length`, `while (low < high)` | `high = a.length - 1`, `while (low <= high)` |
| Binary search on unsorted data | Sort first, or use linear search. |
| "not found" printed inside the loop | Print it after the loop using a flag. |
| Bubble sort written for "selection sort only" | Use the technique named. |
| Sorted array not displayed | Print it with a loop. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 10: Arrays I**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** The index of the last element of ar[]:
(a) ar.length() (b) ar[].length (c) ar.length()-1 (d) ar.length-1

**2.** `double x[] = {2.5, 4.5, 5.5, 6.4};` occupies:
(a) 16 bytes (b) 32 bytes (c) 8 bytes (d) 4 bytes

**3.** The last of 50 elements is set to 100 by:
(a) x[49]=100 (b) x[50]=100 (c) x[51]=100 (d) x[48]=100

**4.** Binary search needs the array to be:
(a) of int type (b) unsorted (c) sorted (d) of odd length

**5.** `String color[] = {"Blue", "Red", "Violet"}; color[2].length()` is:
(a) 5 (b) 3 (c) 2 (d) 6

**6.** A character array of 10 elements occupies:
(a) 20 bytes (b) 10 bytes (c) 40 bytes (d) 80 bytes

**7.** The sort that swaps the minimum into place in each pass:
(a) bubble sort (b) selection sort (c) linear sort (d) binary sort

**8.** `char ch[] = {'A', 'E'}; ch[0] * 2` is:
(a) AA (b) 65 (c) 130 (d) an error

**9.** Number of passes to sort 8 elements by bubble sort:
(a) 8 (b) 9 (c) 64 (d) 7

**10.** Statement I: Linear search needs a sorted array. Statement II: Binary search halves the range each step.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

### Part I — Short answers (5 × 2 = 10)

**11.** Differentiate between linear search and binary search. [2]

**12.** `int a[] = {12, 10, 8, 4, 6, 2, 3, 5, 7};` (a) Output of `System.out.print(a[0] + a[5]);` (b) Index of the largest element. [2]

**13.** Give the array after the first two passes of selection sort on {29, 10, 14, 37, 13}. [2]

**14.** `String x[] = {"Artificial intelligence", "IOT", "Machine learning", "Big data"};` Give the output of `x[3]` and `x.length`. [2]

**15.** Fill the blanks to swap x[0] and x[1] without a third variable: `(1) ____; (2) ____; x[0] = x[0] / x[1];` [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Search for a character input by the user in {'A', 'H', 'N', 'P', 'S', 'U', 'W', 'Y', 'Z', 'b', 'd'} using binary search. [10]

**17.** Input 15 integers and sort them in ascending order using bubble sort; display the sorted array. [10]

**18.** Input 10 integers and find the sum of the one-digit numbers and of the two-digit numbers separately. [10]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | d | b | c | a | c |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | 7 | 110001 | 32 | Binary search |
| 2 | 0, 7, 3 | low = 4 | 5 | low > high |
| 3 | Parallel arrays | After the loop | 413.33 | 41.67 |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | d | b | a | c | d | a | b | c | d | d |

**Part I, Q11–15 (2 marks each)**

**11.** Sorted or not (1); one by one vs middle and halving (1).
**12.** 14 (1); 0 (1).
**13.** 10 29 14 37 13 (1); 10 13 14 37 29 (1).
**14.** Big data (1); 4 (1).
**15.** `x[0] = x[0] * x[1];` (1) `x[1] = x[0] / x[1];` (1).

**Part II (10 marks each)**

**16.–18.** Array declared with the right type and size (2), input or initialisation (2), the technique or logic (4), output (2).
