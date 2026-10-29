# Arrays II — Double-dimensional Arrays

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 11 |
| Title | Arrays II — Double-dimensional Arrays |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 7. Arrays |
| Exam weightage | **Section B**: a double-dimensional array program in every paper since 2024 — row sums or products, diagonal sums, even/odd sums, zero counts, the NORM (15 marks). **Section A**: MCQs and 2-mark parts on **order, index of an element, memory in bytes** and **outputs**. |
| Syllabus scope | Double-dimensional arrays: declaration, initialisation, accepting data and accessing elements; programs on rows, columns and diagonals. |
| In short | How to work with two-dimensional arrays in Java, storing data in rows and columns and processing rows, columns and diagonals. |

> **Note on the text:** CISCE prescribes no textbook for ICSE Computer Applications; this chapter follows the ICSE 2027 syllabus in its own words. Its questions are the CISCE papers of 2017–2026 and the 2024 and 2025 specimens, answered from CISCE's marking schemes and examiners' comments where published. **Every program was compiled and run (Java 21).**
>
> **Exam note:** Write every element as **a[row][column]**, both indexes from 0. Read and process the array with **nested loops** — outer loop for rows, inner for columns. For the diagonals of an n × n array: **left r == c, right r + c == n − 1**. Initialise sums to 0 (products to 1) **before** the loop that uses them, and print the result with the message the question asks for.

---

## 1. Complete Lesson

### What is a double-dimensional array?

A **double-dimensional (2D) array** stores data in **rows and columns**, like a table or a matrix. Each element needs **two indexes**: the **row** and the **column**, both starting at 0.

![Fig. 11.1 A double-dimensional array: element x[row][column], both indexes starting at 0](figures/ca_ch11_fig01_rows_columns.png)

Real tables are 2D arrays: the marks of 40 students in 5 subjects, the sales of 5 salesmen for 5 products, a cinema's seats in rows and columns. A grid of flowers in 4 rows and 5 columns is a "two-dimensional array with 4 rows and 5 columns" (ICSE 2025 specimen Q1(i)).

### Declaring, creating and initialising

```java
int a[][] = new int[3][4];          // 3 rows, 4 columns, all 0
double t[][] = new double[5][5];
int x[][] = {{1, 3}, {5, 7}, {9, 11}};   // 3 rows of 2: the first six odd numbers
char g[][] = {{'A', 'C', 'E'}, {'M', 'A', 'P'}, {'A', 'C', 'T'}};
```

- The **order** of an array is written **rows × columns**: `{{4,3,2},{7,8,2},{8,3,10},{1,2,9}}` has order **4 × 3** (ICSE 2024 Q2(vi)).
- Each inner pair of braces is one **row**.
- Elements created with new get **default values** (0, 0.0, false, null).

### Accessing elements, length and order

- `x[r][c]` is the element in row r, column c. In `{{2,4,5,6},{5,7,8,1},{34,1,10,9}}` the 34 is at `x[2][0]`, and `x[2][3] + x[1][2]` is 9 + 8 = 17 (ICSE 2025 specimen Q2(x)).
- `x.length` is the **number of rows**; `x[0].length` is the **number of columns**.
- The last element of an n × m array is `x[n-1][m-1]`: in a 3 × 3 array, `x[2][2] = 100;` sets the last element (ICSE 2025 Improvement Q1(xvii)).
- An index outside the rows or columns stops the program with **ArrayIndexOutOfBoundsException** (`a[3][0]` in a 3 × 3 array).

**Reading a picture as an array.** For P[2][3] holding Mouse, Keyboard, Printer in row 0 and Scanner, Barcode Scanner, Microphone in row 1, Barcode Scanner is **P[1][1]** (ICSE 2025 Q1(v)). For S[2][3] holding Floppy Disk, Pen Drive, DVD in row 0 and Hard Disk, Storage Tape, Memory card in row 1, the Hard Disk is **S[1][0]** (ICSE 2025 Improvement Q1(xviii)).

### Memory occupied

Memory = **rows × columns × bytes per element**:
- 5 salesmen × 5 products of int: 25 × 4 = **100 bytes** (ICSE 2026 Q1(xviii)).
- A char array of 4 rows and 3 columns: 12 × 2 = **24 bytes** (ICSE 2024 Q1(xi)).
- A 3 × 3 char array: 9 × 2 = **18 bytes**.

### Input and output with nested loops

```java
Scanner sc = new Scanner(System.in);
int a[][] = new int[4][4];
for (int r = 0; r < 4; r++)              // each row
    for (int c = 0; c < 4; c++)          // each column in that row
        a[r][c] = sc.nextInt();

for (int r = 0; r < 4; r++)              // print as a matrix
{
    for (int c = 0; c < 4; c++)
        System.out.print(a[r][c] + " ");
    System.out.println();                // new line after each row
}
```

The values may be typed four to a line or one per line — nextInt() reads them in order, row by row.

### Processing the whole array

| Task | Statement inside the nested loops | Note |
|---|---|---|
| Sum of all | `sum = sum + a[r][c];` | sum = 0 before the loops |
| Even / odd sums | `if (a[r][c] % 2 == 0) even += a[r][c]; else odd += a[r][c];` | Super / special arrays |
| Count zeros | `if (a[r][c] == 0) zero++; else nonzero++;` | Sparse matrix: zero > nonzero |
| Sum of squares (NORM) | `sum = sum + a[r][c] * a[r][c];` | NORM = Math.sqrt(sum) |
| Largest with position | `if (a[r][c] > max) { max = a[r][c]; mr = r; mc = c; }` | start with max = a[0][0] |

### Rows and columns

**Row-wise work** — the outer loop is the row; the total is reset for **each** row:

```java
for (int r = 0; r < 4; r++)
{
    int s = 0;                       // reset for every row
    for (int c = 0; c < 4; c++)
        s = s + a[r][c];
    System.out.println("sum of row " + (r + 1) + " = " + s);
}
```

For a **row product**, start with `p = 1` (ICSE 2025 Improvement Q4). For **column-wise** work, swap the loops: the outer loop runs over the columns and the inner over the rows.

### Diagonals and the boundary

![Fig. 11.2 Conditions on the row r and column c pick out the diagonals and the boundary](figures/ca_ch11_fig02_diagonals.png)

For a **square** n × n array:
- **Left (main) diagonal**: elements with `r == c` — a[0][0], a[1][1], …
- **Right diagonal**: elements with `r + c == n - 1` — a[0][n−1], a[1][n−2], …
- **Boundary**: elements with `r == 0 || r == n - 1 || c == 0 || c == n - 1`.

A **single loop** is enough for the diagonals:

```java
for (int r = 0; r < 4; r++)
{
    ld = ld + x[r][r];          // left diagonal
    rd = rd + x[r][3 - r];      // right diagonal
}
```

The 2024 scheme instead checks `r == c` and `r + c == 3` inside the nested loops; both are correct. The examiners noted candidates who did not compare the two diagonal totals or did not print both messages.

### More matrix operations

- **Transpose**: `t[c][r] = a[r][c];` turns rows into columns.
- **Addition**: `C[r][c] = A[r][c] + B[r][c];` for arrays of the same order.
- **Symmetric**: a square array with `a[r][c] == a[c][r]` for every r and c.

### Summary of the chapter

- **2D array** — rows × columns; element `a[r][c]`; both indexes from 0.
- **Order** = rows × columns; `a.length` rows, `a[0].length` columns.
- **Memory** = rows × columns × bytes per element.
- **Nested loops** — outer rows, inner columns; println after each row to print a matrix.
- **Row work**: reset the sum (0) or product (1) for each row.
- **Diagonals** of n × n: left r == c, right r + c == n − 1; **boundary**: first or last row or column.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Declare, create and initialise double-dimensional arrays and state their order.
2. Access any element by row and column, and find the index of a given element.
3. Calculate the memory occupied by a 2D array.
4. Input and print a 2D array with nested loops.
5. Compute totals, row and column results, even/odd sums, counts and the NORM.
6. Work with the diagonals, the boundary, the transpose and symmetric arrays.

---

## 3. Detailed Section Explanations

### Section 1 — A table in memory
A 2D array is a table: each row is itself a single-dimensional array.

### Section 2 — Two loops for two indexes
The outer loop chooses the row; the inner loop walks along that row.

### Section 3 — Where to reset
Totals for the whole array start before both loops; totals per row start inside the outer loop.

### Section 4 — Patterns in positions
Conditions on r and c select diagonals and boundaries without extra arrays.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Double-dimensional array | An array with rows and columns, needing two indexes. |
| Matrix | A rectangular table of numbers; a 2D array. |
| Row | A horizontal line of elements; first index. |
| Column | A vertical line of elements; second index. |
| Order | Rows × columns, e.g. 4 × 3. |
| Square array | An array with equal numbers of rows and columns. |
| Left (main) diagonal | Elements with row index equal to column index. |
| Right diagonal | Elements with r + c equal to n − 1. |
| Boundary elements | Elements in the first or last row or column. |
| Transpose | The array formed by turning rows into columns. |
| Symmetric array | A square array equal to its transpose. |
| Sparse matrix | (ICSE 2026) A matrix with more zero than non-zero elements. |
| NORM | (ICSE 2025) The square root of the sum of squares of all elements. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| 5 × 5 int array | 100 bytes |
| char array, 4 rows × 3 columns | 24 bytes |
| 3 × 3 char array | 18 bytes |
| Last element of a 3 × 3 array set to 100 | x[2][2] = 100; |
| Order of {{4,3,2},{7,8,2},{8,3,10},{1,2,9}} | 4 × 3 |
| x[0][0] + x[2][2] for that array | 14 |
| First six odd numbers in a 3 × 2 array | int x[][] = {{1, 3}, {5, 7}, {9, 11}}; |
| x[0][1] + x[2][1] for it | 3 + 11 = 14 |
| x[0][2] * x[2][0] for {{2,3,4},{7,9,10},{-11,4,6}} | −44 |
| Max and min of {{4,5},{7,2},{19,4},{7,4}} | 19 at [2][0]; 2 at [1][1] |
| Barcode Scanner in P[2][3] | P[1][1] |
| Hard Disk in S[2][3] | S[1][0] |

### 5.2 Memory aids

- **"RC Cola: Row first, Column second."**
- **"Left diagonal: r equals c; right diagonal: r plus c is n minus one."**
- **"Reset inside, total outside"** — per-row totals reset inside the outer loop.

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- In Java a 2D array is an array of rows, so rows may even have different lengths ("jagged" arrays).
- Images on a screen are 2D arrays of pixel colours; spreadsheets are 2D arrays of cells.
- Multiplying matrices (rows of one with columns of another) is the basis of computer graphics and machine learning.

---

## 6. Person Profiles

### 6.1 James Joseph Sylvester (1814–1897)
An English mathematician who introduced the word "matrix" in 1850 for a rectangular arrangement of numbers — the structure a double-dimensional array stores.

### 6.2 Arthur Cayley (1821–1895)
An English mathematician whose 1858 "A Memoir on the Theory of Matrices" set out matrix addition, multiplication and the transpose, operations programmers now write with nested loops over 2D arrays.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Tables are everywhere** — 2D arrays store them naturally.
- **Position carries meaning** — row = one thing (a student), column = another (a subject).
- **Conditions on indexes** select diagonals, borders and halves.

### 7.2 Real-life connections
- **School results:** marks[student][subject]; row totals give each student's total, column averages each subject's average.
- **Meghalaya:** a shop's daily sales of 5 items over 7 days form a 7 × 5 array; row sums give daily totals.
- **Games:** a tic-tac-toe or chess board is a square 2D array; checking a diagonal win uses r == c and r + c == n − 1.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section B** (60 marks, any four of six programs) has had a double-dimensional array program in every paper since 2024, worth 15 marks. **Section A** asks MCQs and 2-mark parts on order, indexes, memory and outputs.

### 8.1 Graded exercises — solutions

#### Exercise 11A — Basics

**Q1.** Write a statement to create a double array marks with 40 rows and 5 columns.
**Answer:** `double marks[][] = new double[40][5];`

**Q2.** For `int z[][] = {{2, 3, 4}, {5, 1, 2}, {7, 9, 3}};` give the order and z[2][0].
**Answer:** 3 × 3 and 7.

**Q3.** How many bytes does `long n[][] = new long[3][4];` occupy?
**Answer:** 12 × 8 = 96 bytes.

**Q4.** In `int m[][] = new int[2][3];`, give m[1][2], m.length and m[0].length.
**Answer:** 0, 2 and 3.

**Q5.** In `char g[][] = {{'A', 'C', 'E'}, {'M', 'A', 'P'}, {'A', 'C', 'T'}};`, give the index of 'P'.
**Answer:** g[1][2].

#### Exercise 11B — Tracing

**Q6.** For `int t[][] = {{1, 2, 3}, {4, 5, 6}};`, what is the total of all elements?
**Answer:** 21.

**Q7.** For the same t, what does `for (int c = 0; c < 3; c++) System.out.print(t[1][c] + t[0][c] + " ");` print?
**Answer:** `5 7 9` — the column sums.

**Q8.** Give the left and right diagonal sums of {{3, 4, 2, 5}, {2, 5, 2, 3}, {5, 3, 2, 7}, {1, 3, 7, 1}}.
**Answer:** Left 3 + 5 + 2 + 1 = 11; right 5 + 2 + 3 + 1 = 11.

**Q9.** Give the transpose of {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}.
**Answer:** {{1, 4, 7}, {2, 5, 8}, {3, 6, 9}}.

**Q10.** Is {{1, 7, 3}, {7, 4, 5}, {3, 5, 6}} symmetric? Why?
**Answer:** Yes — a[r][c] equals a[c][r] for every r and c (7 and 7, 3 and 3, 5 and 5).
### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(xviii) (1 mark) | The sales made by 5 salesmen selling 5 products is stored in a two-dimensional array of integer data type. How many bytes does the array occupy? (a) 25 (b) 200 (c) 50 (d) 100 |
| ICSE 2026, Q2(viii) (2 marks) | `int X[][] = {{4, 5}, {7, 2}, {19, 4}, {7, 4}};` Write the index of the maximum element and the index of the minimum element of the array. |
| ICSE 2026, Q5 (15 marks) | Write a program to accept a two-dimensional integer array of order 4 × 5 as input from the user. Check if it is a Sparse Matrix or not. A matrix is considered to be sparse if the total number of zero elements is greater than the total number of non-zero elements. Print appropriate messages. Example: rows 4 3 0 1 0 / 1 0 0 2 0 / 1 0 1 0 0 / 0 3 2 0 0 — Number of zero elements = 11, Number of non zero elements = 9, Matrix is a Sparse Matrix. |
| ICSE 2026 Improvement, Q1(xx) (1 mark) | Consider the array: `int x[][] = {{2, 3, 4}, {7, 9, 10}, {-11, 4, 6}};` What is the result of the statement `System.out.println(x[0][2] * x[2][0]);`? (a) 24 (b) -44 (c) 16 (d) -22 |
| ICSE 2026 Improvement, Q2(v) (2 marks) | Consider the following two dimensional array and answer the questions given below: `char x[][] = {{'A', 'C', 'E'}, {'M', 'A', 'P'}, {'A', 'C', 'T'}};` (a) How many bytes are occupied by the array? (b) What is the index of 'P'? |
| ICSE 2026 Improvement, Q8 (15 marks) | Define a class to accept values into a 4 × 4 array and check if it is a Super array or not; an array is Super if the sum of even elements is greater than the sum of odd elements of the array. Example: rows 12 7 8 13 / 1 3 6 5 / 15 2 9 10 / 4 11 14 16 — Sum of even elements = 12 + 8 + 6 + 2 + 10 + 4 + 14 + 16 = 72; Sum of odd elements = 7 + 13 + 1 + 3 + 5 + 15 + 9 + 11 = 64; Array is a super array. |
| ICSE 2025, Q1(v) (1 mark) | [Picture: row 0 — Mouse, Keyboard, Printer; row 1 — Scanner, Barcode Scanner, Microphone] Consider the two dimensional array P[2][3] of peripherals (input / output devices) given above; state the index of the device Barcode Scanner. (a) P[1][1] (b) P[0][1] (c) P[1][2] (d) P[0][0] |
| ICSE 2025, Q2(ix) (2 marks) | (a) Write the Java statement to initialise the first 6 odd numbers in a 3 × 2 array. (b) What is the result of x[0][1] + x[2][1] of the above array? |
| ICSE 2025, Q4 (15 marks) | Define a class to accept values into a 4 × 4 integer array. Calculate and print the NORM of the array. NORM is the square root of sum of squares of all elements. Example: rows 1 2 1 3 / 5 2 1 6 / 3 6 1 2 / 3 4 6 3 — Sum of squares of elements = 1 + 4 + 1 + 9 + 25 + 4 + 1 + 36 + 9 + 36 + 1 + 4 + 9 + 16 + 36 + 9 = 201; NORM = square root of 201 = 14.177446878757825 |
| ICSE 2025 Improvement, Q1(xvii) (1 mark) | Which one of the following Java statements assigns 100 to the last element of a 3 × 3 array? (a) x[2][2]=100; (b) x[3][3]=100; (c) x[2][3]=100; (d) x[3][2]=100; |
| ICSE 2025 Improvement, Q1(xviii) (1 mark) | [Picture: row 0 — Floppy Disk, Pen Drive, DVD; row 1 — Hard Disk, Storage Tape, Memory card] Consider the two dimensional array S[2][3] of storage devices given above; state the index of the Hard disk. (a) S[1][0] (b) S[0][1] (c) S[1][2] (d) S[0][0] |
| ICSE 2025 Improvement, Q2(vii) (2 marks) | Consider the given array and answer the questions given below: `int z[][] = {{2, 3, 4}, {5, 1, 2}, {7, 9, 3}};` (a) What is the order of the array z[][]? (b) What is the value in z[2][0]? |
| ICSE 2025 Improvement, Q4 (15 marks) | Define a class to accept values into a 3 × 3 integer array and print the product of each row's elements. Example: rows 3 1 2 / 4 2 1 / 5 1 2 — Output: Row 0 – 6, Row 1 – 8, Row 2 – 10 |
| ICSE 2025 specimen, Q1(i) (1 mark) | [Picture: a grid of flowers in 4 rows and 5 columns] Name the above structure: (a) One dimensional array (b) Two Dimensional array with 4 rows and 5 columns (c) Three dimensional array (d) Two Dimensional array with 5 rows and 4 columns |
| ICSE 2025 specimen, Q2(x) (2 marks) | Consider the following program segment and answer the questions given below: `int x[][] = {{2, 4, 5, 6}, {5, 7, 8, 1}, {34, 1, 10, 9}};` (a) What is the position of 34? (b) What is the result of x[2][3] + x[1][2]? |
| ICSE 2025 specimen, Q6 (15 marks) | Define a class to accept values into a 4 × 4 array and find and display the sum of each row. Example: A[][] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {1, 3, 5, 7}, {2, 5, 3, 1}}; Output: sum of row 1 = 10 (1 + 2 + 3 + 4); sum of row 2 = 26 (5 + 6 + 7 + 8); sum of row 3 = 16 (1 + 3 + 5 + 7); sum of row 4 = 11 (2 + 5 + 3 + 1) |
| ICSE 2024, Q1(xi) (1 mark) | The number of bytes occupied by a character array of four rows and three columns is: (a) 12 (b) 24 (c) 96 (d) 48 |
| ICSE 2024, Q2(vi) (2 marks) | Consider the following two-dimensional array and answer the questions given below: `int x[][] = {{4, 3, 2}, {7, 8, 2}, {8, 3, 10}, {1, 2, 9}};` (a) What is the order of the array? (b) What is the value of x[0][0] + x[2][2]? |
| ICSE 2024, Q6 (15 marks) | Define a class to accept values into an integer array of order 4 × 4 and check whether it is a DIAGONAL array or not. An array is DIAGONAL if the sum of the left diagonal elements equals the sum of the right diagonal elements. Print the appropriate message. Example: rows 3 4 2 5 / 2 5 2 3 / 5 3 2 7 / 1 3 7 1 — Sum of the left diagonal elements = 3 + 5 + 2 + 1 = 11; Sum of the right diagonal elements = 5 + 2 + 3 + 1 = 11 |
| ICSE 2024 specimen, Q6 (15 marks) | Define a class to accept values into a 3 × 3 array and check if it is a special array. An array is a special array if the sum of the even elements = sum of the odd elements. Example: A[][] = {{4, 5, 6}, {5, 3, 2}, {4, 2, 5}}; Sum of even elements = 4 + 6 + 2 + 4 + 2 = 18; Sum of odd elements = 5 + 5 + 3 + 5 = 18 |
| ICSE 2020, Q9 (15 marks) | Write a program to input and store integer elements in a double dimensional array of size 3 × 3 and find the sum of elements in the left diagonal. Example: rows 1 3 5 / 4 6 8 / 9 2 4 — Output: Sum of the left diagonal elements = (1 + 6 + 4) = 11 |

**Solutions**

**2026 Q1(xviii).** **(d) 100** — 5 × 5 = 25 ints × 4 bytes. *(Worked answer.)*

**2026 Q2(viii).** Maximum 19 at **X[2][0]**; minimum 2 at **X[1][1]**. *(Worked answer.)*

**2026 Q5.** Each element is counted as zero or non-zero while it is read:
```java
import java.util.*;
class Sparse
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[][] = new int[4][5];
        int zero = 0, nonzero = 0;
        System.out.println("Enter 20 elements (4 rows of 5):");
        for (int r = 0; r < 4; r++)
        {
            for (int c = 0; c < 5; c++)
            {
                a[r][c] = sc.nextInt();
                if (a[r][c] == 0)
                    zero++;
                else
                    nonzero++;
            }
        }
        System.out.println("Number of zero elements = " + zero);
        System.out.println("Number of non zero elements = " + nonzero);
        if (zero > nonzero)
            System.out.println("Matrix is a Sparse Matrix");
        else
            System.out.println("Matrix is not a Sparse Matrix");
    }
}
```
Sample run (the example matrix):
```
Enter 20 elements (4 rows of 5):
4 3 0 1 0
1 0 0 2 0
1 0 1 0 0
0 3 2 0 0
Number of zero elements = 11
Number of non zero elements = 9
Matrix is a Sparse Matrix
```
*(Worked answer.)*

**2026 Improvement Q1(xx).** **(b) -44** — x[0][2] is 4 and x[2][0] is −11. *(Worked answer.)*

**2026 Improvement Q2(v).** (a) **18 bytes** — 9 chars × 2 bytes. (b) **x[1][2]** *(Worked answer.)*

**2026 Improvement Q8.**
```java
import java.util.*;
class SuperArray
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[][] = new int[4][4];
        int even = 0, odd = 0;
        System.out.println("Enter 16 elements:");
        for (int r = 0; r < 4; r++)
        {
            for (int c = 0; c < 4; c++)
            {
                a[r][c] = sc.nextInt();
                if (a[r][c] % 2 == 0)
                    even = even + a[r][c];
                else
                    odd = odd + a[r][c];
            }
        }
        System.out.println("Sum of even elements = " + even);
        System.out.println("Sum of odd elements = " + odd);
        if (even > odd)
            System.out.println("Array is a super array.");
        else
            System.out.println("Array is not a super array.");
    }
}
```
Sample run:
```
Enter 16 elements:
12 7 8 13
1 3 6 5
15 2 9 10
4 11 14 16
Sum of even elements = 72
Sum of odd elements = 64
Array is a super array.
```
*(Worked answer.)*

**2025 Q1(v).** **(a) P[1][1]**

**2025 Q2(ix).** (a) `int x[][] = {{1, 3}, {5, 7}, {9, 11}};` (b) **3 + 11 = 14**

**2025 Q4.** As in the marking scheme, the square of each element is added while it is read:
```java
import java.util.*;
class Norm
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int x[][] = new int[4][4];
        int sum = 0;
        System.out.println("Enter 16 elements:");
        for (int r = 0; r < 4; r++)
        {
            for (int c = 0; c < 4; c++)
            {
                x[r][c] = sc.nextInt();
                sum = sum + x[r][c] * x[r][c];
            }
        }
        System.out.println("Sum of squares of elements = " + sum);
        System.out.println("NORM = " + Math.sqrt(sum));
    }
}
```
Sample run (the example):
```
Enter 16 elements:
1 2 1 3
5 2 1 6
3 6 1 2
3 4 6 3
Sum of squares of elements = 201
NORM = 14.177446878757825
```
The examiners noted these errors: the 2D array declared or filled wrongly, sum not initialised to 0, and the elements added instead of their squares.

**2025 Improvement Q1(xvii).** **(a) x[2][2]=100;** *(Worked answer.)*

**2025 Improvement Q1(xviii).** **(a) S[1][0]** *(Worked answer.)*

**2025 Improvement Q2(vii).** (a) **3 × 3** (b) **7** *(Worked answer.)*

**2025 Improvement Q4.** The product starts at 1 for each row:
```java
import java.util.*;
class RowProduct
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[][] = new int[3][3];
        System.out.println("Enter 9 elements:");
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                a[r][c] = sc.nextInt();
        for (int r = 0; r < 3; r++)
        {
            int p = 1;
            for (int c = 0; c < 3; c++)
                p = p * a[r][c];
            System.out.println("Row " + r + " - " + p);
        }
    }
}
```
Sample run:
```
Enter 9 elements:
3 1 2
4 2 1
5 1 2
Row 0 - 6
Row 1 - 8
Row 2 - 10
```
*(Worked answer.)*

**2025 specimen Q1(i).** **(b) Two Dimensional array with 4 rows and 5 columns**

**2025 specimen Q2(x).** (a) **x[2][0]** (b) **17** (9 + 8)

**2025 specimen Q6.** As in the draft scheme, the sum is reset for each row:
```java
import java.util.*;
class RowSum
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int x[][] = new int[4][4];
        System.out.println("Enter 16 elements:");
        for (int r = 0; r < 4; r++)
            for (int c = 0; c < 4; c++)
                x[r][c] = sc.nextInt();
        for (int r = 0; r < 4; r++)
        {
            int s = 0;
            for (int c = 0; c < 4; c++)
                s = s + x[r][c];
            System.out.println("sum of row " + (r + 1) + " = " + s);
        }
    }
}
```
Sample run:
```
Enter 16 elements:
1 2 3 4
5 6 7 8
1 3 5 7
2 5 3 1
sum of row 1 = 10
sum of row 2 = 26
sum of row 3 = 16
sum of row 4 = 11
```

**2024 Q1(xi).** **(b) 24**

**2024 Q2(vi).** (a) **4 × 3** (b) **4 + 10 = 14**

**2024 Q6.** A single loop adds both diagonals; the scheme's nested loops with `r == c` and `r + c == 3` are equally correct:
```java
import java.util.*;
class DiagonalArray
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int x[][] = new int[4][4];
        int ld = 0, rd = 0;
        System.out.println("Enter 16 elements:");
        for (int r = 0; r < 4; r++)
            for (int c = 0; c < 4; c++)
                x[r][c] = sc.nextInt();
        for (int r = 0; r < 4; r++)
        {
            ld = ld + x[r][r];
            rd = rd + x[r][3 - r];
        }
        System.out.println("Sum of the left diagonal elements = " + ld);
        System.out.println("Sum of the right diagonal elements = " + rd);
        if (ld == rd)
            System.out.println("DIAGONAL array");
        else
            System.out.println("Not a DIAGONAL array");
    }
}
```
Sample run:
```
Enter 16 elements:
3 4 2 5
2 5 2 3
5 3 2 7
1 3 7 1
Sum of the left diagonal elements = 11
Sum of the right diagonal elements = 11
DIAGONAL array
```
The examiners noted candidates who did not read the question attentively and did not check whether the two diagonal totals were equal.

**2024 specimen Q6.**
```java
import java.util.*;
class SpecialArray
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[][] = new int[3][3];
        int even = 0, odd = 0;
        System.out.println("Enter 9 elements:");
        for (int r = 0; r < 3; r++)
        {
            for (int c = 0; c < 3; c++)
            {
                a[r][c] = sc.nextInt();
                if (a[r][c] % 2 == 0)
                    even = even + a[r][c];
                else
                    odd = odd + a[r][c];
            }
        }
        System.out.println("Sum of even elements = " + even);
        System.out.println("Sum of odd elements = " + odd);
        if (even == odd)
            System.out.println("Special array");
        else
            System.out.println("Not a special array");
    }
}
```
Sample run:
```
Enter 9 elements:
4 5 6
5 3 2
4 2 5
Sum of even elements = 18
Sum of odd elements = 18
Special array
```
*(Worked answer.)*

**2020 Q9.**
```java
import java.util.*;
class LeftDiagonal
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[][] = new int[3][3];
        System.out.println("Enter 9 elements:");
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                a[r][c] = sc.nextInt();
        int sum = 0;
        for (int i = 0; i < 3; i++)
            sum = sum + a[i][i];
        System.out.println("Sum of the left diagonal elements = " + sum);
    }
}
```
Sample run:
```
Enter 9 elements:
1 3 5
4 6 8
9 2 4
Sum of the left diagonal elements = 11
```
*(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) For `int t[][] = {{1, 2, 3}, {4, 5, 6}};`, give t.length, t[0].length and the total of all elements.
**Answer:** 2, 3 and 21.

**Q2.** (2 marks) What happens when `int a[][] = new int[3][3]; a[3][0] = 5;` runs?
**Answer:** It compiles but stops with ArrayIndexOutOfBoundsException: Index 3 out of bounds for length 3.

**Q3.** (2 marks) Write the condition for the right diagonal of a 5 × 5 array.
**Answer:** `r + c == 4`.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 15 marks | Accept an m × n array; even/odd sums, zero counts, NORM or diagonal check with a message | 8.2, Section 11 |
| 15 marks | Row sums or products; left or right diagonal sum | 8.2 |
| MCQ | Bytes of a 2D array; index of an element in a picture; last element | 8.2, 5.1 |
| 2 marks | Order of an initialised array; value of an expression of elements | 8.2, Section 10 |

---
## 9. MCQs with Explanations

### Double-dimensional array basics (Q1–Q16)

**Q1.** A double-dimensional array stores data in
- (a) separate variables
- (b) a single row only
- (c) a single column only
- (d) rows and columns

**Answer:** (d) rows and columns
**Explanation:** Like a table or matrix.

**Q2.** An element of a 2D array a is written
- (a) a[column][row]
- (b) a[row][column]
- (c) a(row, column)
- (d) a[row, column]

**Answer:** (b) a[row][column]
**Explanation:** Row first, column second.

**Q3.** The first element of a 2D array a is
- (a) a[0][1]
- (b) a[1][1]
- (c) a[0][0]
- (d) a[1][0]

**Answer:** (c) a[0][0]
**Explanation:** Both indexes start at 0.

**Q4.** A grid of flowers in 4 rows and 5 columns is best described as
- (a) a one-dimensional array
- (b) a two-dimensional array with 4 rows and 5 columns
- (c) a three-dimensional array
- (d) a two-dimensional array with 5 rows and 4 columns

**Answer:** (b) a two-dimensional array with 4 rows and 5 columns
**Explanation:** ICSE 2025 specimen Q1(i).

**Q5.** The statement that creates an int array with 3 rows and 4 columns is
- (a) int a[][] = new int[12];
- (b) int a[][] = new int[4][3];
- (c) int a[3][4];
- (d) int a[][] = new int[3][4];

**Answer:** (d) int a[][] = new int[3][4];
**Explanation:** Rows first.

**Q6.** The Java statement that initialises the first six odd numbers in a 3 × 2 array is
- (a) int x[][] = {{1, 3}, {5, 7}, {9, 11}};
- (b) int x[][] = {{1, 3, 5}, {7, 9, 11}};
- (c) int x[] = {1, 3, 5, 7, 9, 11};
- (d) int x[][] = {1, 3, 5, 7, 9, 11};

**Answer:** (a) int x[][] = {{1, 3}, {5, 7}, {9, 11}};
**Explanation:** 3 rows of 2.

**Q7.** In an initialiser, each inner pair of braces is one
- (a) row
- (b) column
- (c) diagonal
- (d) element

**Answer:** (a) row
**Explanation:** {{row 0}, {row 1}, …}

**Q8.** After int m[][] = new int[2][3];, the value of m[1][2] is
- (a) 2
- (b) 0
- (c) 3
- (d) null

**Answer:** (b) 0
**Explanation:** Default value.

**Q9.** A 2D array is processed most naturally with
- (a) a switch statement
- (b) a single if statement
- (c) nested loops
- (d) recursion only

**Answer:** (c) nested loops
**Explanation:** One loop per index.

**Q10.** In the usual nested loops, the outer loop runs over the
- (a) bytes
- (b) columns
- (c) diagonals
- (d) rows

**Answer:** (d) rows
**Explanation:** The inner loop runs over the columns.

**Q11.** To print a 2D array as a matrix, System.out.println() is placed
- (a) before both loops
- (b) inside the inner loop
- (c) after the inner loop
- (d) nowhere

**Answer:** (c) after the inner loop
**Explanation:** One line per row.

**Q12.** int a[][] = new int[3][3]; a[3][0] = 5; gives
- (a) a compile error
- (b) ArrayIndexOutOfBoundsException at run time
- (c) a[3][0] = 5
- (d) nothing

**Answer:** (b) ArrayIndexOutOfBoundsException at run time
**Explanation:** Rows are 0 to 2.

**Q13.** A table of marks of 40 students in 5 subjects is best stored as
- (a) int marks[] = new int[5];
- (b) int marks[][] = new int[40][5];
- (c) int marks = 40 * 5;
- (d) int marks[][] = new int[5];

**Answer:** (b) int marks[][] = new int[40][5];
**Explanation:** A row for each student.

**Q14.** A square array has
- (a) only one row
- (b) equal numbers of rows and columns
- (c) more rows than columns
- (d) no diagonal

**Answer:** (b) equal numbers of rows and columns
**Explanation:** e.g. 4 × 4.

**Q15.** char x[][] = {{'A', 'C', 'E'}, {'M', 'A', 'P'}, {'A', 'C', 'T'}}; The index of 'P' is
- (a) x[1][2]
- (b) x[2][1]
- (c) x[0][2]
- (d) x[2][2]

**Answer:** (a) x[1][2]
**Explanation:** Row 1, column 2.

**Q16.** In the same array, the element x[2][2] is
- (a) E
- (b) P
- (c) T
- (d) C

**Answer:** (c) T
**Explanation:** Last row, last column.

### Order, length and memory (Q17–Q30)

**Q17.** The order of int x[][] = {{4, 3, 2}, {7, 8, 2}, {8, 3, 10}, {1, 2, 9}}; is
- (a) 4 × 4
- (b) 3 × 4
- (c) 12
- (d) 4 × 3

**Answer:** (d) 4 × 3
**Explanation:** 4 rows of 3.

**Q18.** For a 2D array x, x.length gives the number of
- (a) elements
- (b) columns
- (c) rows
- (d) bytes

**Answer:** (c) rows
**Explanation:** x[0].length gives the columns.

**Q19.** For int x[][] = new int[5][7];, x[0].length is
- (a) 35
- (b) 5
- (c) 7
- (d) 0

**Answer:** (c) 7
**Explanation:** Columns in row 0.

**Q20.** The order of int z[][] = {{2, 3, 4}, {5, 1, 2}, {7, 9, 3}}; is
- (a) 3 × 3
- (b) 9
- (c) 3 × 2
- (d) 2 × 3

**Answer:** (a) 3 × 3
**Explanation:** 3 rows of 3.

**Q21.** Sales of 5 salesmen for 5 products stored as int occupy
- (a) 25 bytes
- (b) 200 bytes
- (c) 50 bytes
- (d) 100 bytes

**Answer:** (d) 100 bytes
**Explanation:** 25 × 4.

**Q22.** A character array of four rows and three columns occupies
- (a) 12 bytes
- (b) 24 bytes
- (c) 96 bytes
- (d) 48 bytes

**Answer:** (b) 24 bytes
**Explanation:** 12 × 2.

**Q23.** A 3 × 3 char array occupies
- (a) 9 bytes
- (b) 18 bytes
- (c) 36 bytes
- (d) 72 bytes

**Answer:** (b) 18 bytes
**Explanation:** 9 × 2.

**Q24.** long n[][] = new long[3][4]; occupies
- (a) 12 bytes
- (b) 48 bytes
- (c) 96 bytes
- (d) 24 bytes

**Answer:** (c) 96 bytes
**Explanation:** 12 × 8.

**Q25.** double d[][] = new double[2][5]; occupies
- (a) 40 bytes
- (b) 80 bytes
- (c) 10 bytes
- (d) 20 bytes

**Answer:** (b) 80 bytes
**Explanation:** 10 × 8.

**Q26.** The number of elements in a 4 × 5 array is
- (a) 20
- (b) 9
- (c) 45
- (d) 16

**Answer:** (a) 20
**Explanation:** Rows × columns.

**Q27.** The statement that assigns 100 to the last element of a 3 × 3 array is
- (a) x[3][3]=100;
- (b) x[2][2]=100;
- (c) x[2][3]=100;
- (d) x[3][2]=100;

**Answer:** (b) x[2][2]=100;
**Explanation:** Last row 2, last column 2.

**Q28.** The last element of an n × m array is
- (a) a[n][m]
- (b) a[n-1][m-1]
- (c) a[m-1][n-1]
- (d) a[n][m-1]

**Answer:** (b) a[n-1][m-1]
**Explanation:** Both indexes end one below the size.

**Q29.** int t[][] = {{1, 2, 3}, {4, 5, 6}}; t.length and t[0].length are
- (a) 2 and 6
- (b) 3 and 2
- (c) 6 and 3
- (d) 2 and 3

**Answer:** (d) 2 and 3
**Explanation:** 2 rows of 3.

**Q30.** The number of bytes in an int array of order 4 × 3 is
- (a) 48
- (b) 12
- (c) 24
- (d) 96

**Answer:** (a) 48
**Explanation:** 12 × 4.

### Element access and outputs (Q31–Q46)

**Q31.** For int x[][] = {{2, 3, 4}, {7, 9, 10}, {-11, 4, 6}};, System.out.println(x[0][2] * x[2][0]); prints
- (a) 24
- (b) −44
- (c) 16
- (d) −22

**Answer:** (b) −44
**Explanation:** 4 × −11.

**Q32.** For int x[][] = {{4, 3, 2}, {7, 8, 2}, {8, 3, 10}, {1, 2, 9}};, x[0][0] + x[2][2] is
- (a) 12
- (b) 13
- (c) 14
- (d) 6

**Answer:** (c) 14
**Explanation:** 4 + 10.

**Q33.** For int x[][] = {{1, 3}, {5, 7}, {9, 11}};, x[0][1] + x[2][1] is
- (a) 20
- (b) 10
- (c) 12
- (d) 14

**Answer:** (d) 14
**Explanation:** 3 + 11.

**Q34.** For int x[][] = {{2, 4, 5, 6}, {5, 7, 8, 1}, {34, 1, 10, 9}};, the position of 34 is
- (a) x[3][1]
- (b) x[0][2]
- (c) x[2][0]
- (d) x[2][1]

**Answer:** (c) x[2][0]
**Explanation:** Row 2, column 0.

**Q35.** In the same array, x[2][3] + x[1][2] is
- (a) 17
- (b) 19
- (c) 15
- (d) 18

**Answer:** (a) 17
**Explanation:** 9 + 8.

**Q36.** int z[][] = {{2, 3, 4}, {5, 1, 2}, {7, 9, 3}}; The value of z[2][0] is
- (a) 3
- (b) 4
- (c) 2
- (d) 7

**Answer:** (d) 7
**Explanation:** Row 2 starts with 7.

**Q37.** For int X[][] = {{4, 5}, {7, 2}, {19, 4}, {7, 4}};, the maximum element is at
- (a) X[2][0]
- (b) X[0][2]
- (c) X[3][1]
- (d) X[1][1]

**Answer:** (a) X[2][0]
**Explanation:** 19 is in row 2, column 0.

**Q38.** In the same array, the minimum element is at
- (a) X[2][1]
- (b) X[0][0]
- (c) X[3][1]
- (d) X[1][1]

**Answer:** (d) X[1][1]
**Explanation:** 2 is in row 1, column 1.

**Q39.** P[2][3] holds Mouse, Keyboard, Printer in row 0 and Scanner, Barcode Scanner, Microphone in row 1. Barcode Scanner is
- (a) P[1][1]
- (b) P[0][1]
- (c) P[1][2]
- (d) P[0][0]

**Answer:** (a) P[1][1]
**Explanation:** Row 1, column 1.

**Q40.** S[2][3] holds Floppy Disk, Pen Drive, DVD in row 0 and Hard Disk, Storage Tape, Memory card in row 1. Hard Disk is
- (a) S[0][1]
- (b) S[1][0]
- (c) S[1][2]
- (d) S[0][0]

**Answer:** (b) S[1][0]
**Explanation:** Row 1, column 0.

**Q41.** For int t[][] = {{1, 2, 3}, {4, 5, 6}};, the total of all elements is
- (a) 6
- (b) 15
- (c) 21
- (d) 12

**Answer:** (c) 21
**Explanation:** 1 + 2 + … + 6.

**Q42.** For the same t, the loop for (int c = 0; c < 3; c++) System.out.print(t[1][c] + t[0][c] + " "); prints
- (a) 1 2 3
- (b) 6 15
- (c) 14 25 36
- (d) 5 7 9

**Answer:** (d) 5 7 9
**Explanation:** Column sums.

**Q43.** char g[][] = {{'A', 'C', 'E'}, {'M', 'A', 'P'}, {'A', 'C', 'T'}}; System.out.println(g[1][2] + " " + g[2][0] + g[0][2]); prints
- (a) PAE
- (b) P 134
- (c) P AE
- (d) M AE

**Answer:** (c) P AE
**Explanation:** After a String, + joins the chars.

**Q44.** In the 3 × 3 array {{3, 1, 2}, {4, 2, 1}, {5, 1, 2}}, the product of row 1 is
- (a) 6
- (b) 8
- (c) 10
- (d) 7

**Answer:** (b) 8
**Explanation:** 4 × 2 × 1.

**Q45.** In {{1, 2, 3, 4}, {5, 6, 7, 8}, {1, 3, 5, 7}, {2, 5, 3, 1}}, the sum of the second row is
- (a) 16
- (b) 10
- (c) 26
- (d) 11

**Answer:** (c) 26
**Explanation:** 5 + 6 + 7 + 8.

**Q46.** In {{12, 45, 7}, {33, 9, 61}, {28, 50, 16}}, the largest element and its position are
- (a) 45 at a[0][1]
- (b) 50 at a[2][1]
- (c) 61 at a[2][1]
- (d) 61 at a[1][2]

**Answer:** (d) 61 at a[1][2]
**Explanation:** Row 1, column 2.

### Processing with nested loops (Q47–Q62)

**Q47.** A sum of all elements must be set to 0
- (a) inside the inner loop
- (b) before both loops
- (c) after the loops
- (d) never

**Answer:** (b) before both loops
**Explanation:** Otherwise it restarts.

**Q48.** For the sum of each row, s = 0 is written
- (a) inside the outer loop, before the inner loop
- (b) before the outer loop only
- (c) inside the inner loop
- (d) after both loops

**Answer:** (a) inside the outer loop, before the inner loop
**Explanation:** Reset for each row.

**Q49.** For the product of each row, p starts at
- (a) the row number
- (b) 0
- (c) −1
- (d) 1

**Answer:** (d) 1
**Explanation:** 0 would make every product 0.

**Q50.** The NORM of an array is
- (a) the square root of the sum of squares of all elements
- (b) the sum of all elements
- (c) the largest element
- (d) the number of rows

**Answer:** (a) the square root of the sum of squares of all elements
**Explanation:** As defined in ICSE 2025 Q4.

**Q51.** The statement that adds the square of an element to sum is
- (a) sum = sum + x[r][c] * x[r][c];
- (b) sum = sum + x[r][c];
- (c) sum = x[r][c] * x[r][c];
- (d) sum = sum * x[r][c];

**Answer:** (a) sum = sum + x[r][c] * x[r][c];
**Explanation:** Add each square.

**Q52.** For rows 1 2 1 3 / 5 2 1 6 / 3 6 1 2 / 3 4 6 3, the sum of squares is
- (a) 196
- (b) 49
- (c) 14
- (d) 201

**Answer:** (d) 201
**Explanation:** NORM = √201 ≈ 14.18.

**Q53.** A matrix is sparse (ICSE 2026) when
- (a) it has no diagonal
- (b) all elements are zero
- (c) zero elements outnumber non-zero elements
- (d) it is square

**Answer:** (c) zero elements outnumber non-zero elements
**Explanation:** 11 zeros vs 9 non-zeros in the example.

**Q54.** The test for an even element is
- (a) a[r][c] % 2 == 0
- (b) a[r][c] / 2 == 0
- (c) a[r][c] == 2
- (d) r % 2 == 0

**Answer:** (a) a[r][c] % 2 == 0
**Explanation:** The remainder is 0.

**Q55.** An array is a super array (ICSE 2026 Improvement) when
- (a) the sum of even elements is greater than the sum of odd elements
- (b) the sums of even and odd elements are equal
- (c) all elements are even
- (d) the diagonals are equal

**Answer:** (a) the sum of even elements is greater than the sum of odd elements
**Explanation:** 72 > 64 in the example.

**Q56.** An array is a special array (ICSE 2024 specimen) when
- (a) the array is square
- (b) all elements are odd
- (c) the left diagonal is 0
- (d) the sums of even and odd elements are equal

**Answer:** (d) the sums of even and odd elements are equal
**Explanation:** 18 = 18 in the example.

**Q57.** For {{4, 5, 6}, {5, 3, 2}, {4, 2, 5}}, the sum of the even elements is
- (a) 18
- (b) 20
- (c) 12
- (d) 36

**Answer:** (a) 18
**Explanation:** 4 + 6 + 2 + 4 + 2.

**Q58.** In a column-wise loop, the outer loop runs over the
- (a) rows
- (b) columns
- (c) diagonals
- (d) elements

**Answer:** (b) columns
**Explanation:** The inner loop then runs over the rows.

**Q59.** Matrix addition C = A + B is written as
- (a) C[r] = A[r] + B[r];
- (b) C[r][c] = A[c][r] + B[r][c];
- (c) C = A + B;
- (d) C[r][c] = A[r][c] + B[r][c];

**Answer:** (d) C[r][c] = A[r][c] + B[r][c];
**Explanation:** Element by element.

**Q60.** Two matrices can be added only if they have
- (a) the same order
- (b) the same first element
- (c) an even number of rows
- (d) different orders

**Answer:** (a) the same order
**Explanation:** Every element needs a partner.

**Q61.** Student totals in marks[student][subject] are found by
- (a) adding the diagonal
- (b) adding down each column
- (c) adding along each row
- (d) multiplying the rows

**Answer:** (c) adding along each row
**Explanation:** A row is one student.

**Q62.** Subject averages in the same array are found by
- (a) adding down each column and dividing by the number of students
- (b) adding along each row
- (c) taking the diagonal
- (d) taking the largest element

**Answer:** (a) adding down each column and dividing by the number of students
**Explanation:** A column is one subject.

### Diagonals, boundary and transpose (Q63–Q76)

**Q63.** In a square array, the left (main) diagonal elements satisfy
- (a) r == c
- (b) r + c == n - 1
- (c) r == 0
- (d) c == n - 1

**Answer:** (a) r == c
**Explanation:** a[0][0], a[1][1], …

**Q64.** In a 4 × 4 array, the right diagonal elements satisfy
- (a) r + c == 4
- (b) r == c
- (c) r + c == 3
- (d) r - c == 3

**Answer:** (c) r + c == 3
**Explanation:** n − 1 = 3.

**Q65.** In a 5 × 5 array, the right diagonal elements satisfy
- (a) r - c == 4
- (b) r + c == 5
- (c) r == c
- (d) r + c == 4

**Answer:** (d) r + c == 4
**Explanation:** n − 1 = 4.

**Q66.** The left diagonal sum of {{1, 3, 5}, {4, 6, 8}, {9, 2, 4}} is
- (a) 20
- (b) 11
- (c) 15
- (d) 9

**Answer:** (b) 11
**Explanation:** 1 + 6 + 4.

**Q67.** The right diagonal sum of the same array is
- (a) 15
- (b) 11
- (c) 20
- (d) 17

**Answer:** (c) 20
**Explanation:** 5 + 6 + 9.

**Q68.** For {{3, 4, 2, 5}, {2, 5, 2, 3}, {5, 3, 2, 7}, {1, 3, 7, 1}}, the left and right diagonal sums are
- (a) 10 and 11
- (b) 11 and 13
- (c) 11 and 11
- (d) 12 and 12

**Answer:** (c) 11 and 11
**Explanation:** So it is a DIAGONAL array.

**Q69.** In a single loop over r for a 4 × 4 array, the right-diagonal element is
- (a) x[r][4 - r]
- (b) x[r][r]
- (c) x[3][r]
- (d) x[r][3 - r]

**Answer:** (d) x[r][3 - r]
**Explanation:** Column 3 − r.

**Q70.** An element lies on the boundary of an n × n array if
- (a) r == c
- (b) r == 0 || r == n - 1 || c == 0 || c == n - 1
- (c) r + c == n - 1
- (d) r > 0 && c > 0

**Answer:** (b) r == 0 || r == n - 1 || c == 0 || c == n - 1
**Explanation:** First or last row or column.

**Q71.** The sum of the boundary elements of {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}} is
- (a) 34
- (b) 136
- (c) 102
- (d) 68

**Answer:** (c) 102
**Explanation:** 136 minus the inner 6 + 7 + 10 + 11.

**Q72.** The transpose of a matrix is formed by
- (a) turning rows into columns
- (b) reversing each row
- (c) adding the diagonals
- (d) sorting each column

**Answer:** (a) turning rows into columns
**Explanation:** t[c][r] = a[r][c].

**Q73.** The transpose of {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}} has first row
- (a) 1 2 3
- (b) 1 4 7
- (c) 7 8 9
- (d) 3 6 9

**Answer:** (b) 1 4 7
**Explanation:** The first column becomes the first row.

**Q74.** A square array is symmetric if
- (a) it has an even number of rows
- (b) all its elements are equal
- (c) its diagonals have equal sums
- (d) a[r][c] == a[c][r] for every r and c

**Answer:** (d) a[r][c] == a[c][r] for every r and c
**Explanation:** It equals its transpose.

**Q75.** Which array is symmetric?
- (a) {{1, 2}, {3, 4}}
- (b) {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
- (c) {{1, 7, 3}, {7, 4, 5}, {3, 5, 6}}
- (d) {{0, 1}, {2, 0}}

**Answer:** (c) {{1, 7, 3}, {7, 4, 5}, {3, 5, 6}}
**Explanation:** 7 = 7, 3 = 3, 5 = 5.

**Q76.** The 2024 examiners noted that some candidates writing the DIAGONAL program
- (a) printed a message
- (b) used a 2D array
- (c) used nested loops
- (d) did not compare the two diagonal totals

**Answer:** (d) did not compare the two diagonal totals
**Explanation:** The check decides the message.
## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** What is a double-dimensional array? Give a real-life example.
**Answer:** An array that stores elements in rows and columns; each element needs a row index and a column index.
e.g. the marks of 40 students in 5 subjects: marks[40][5].

**Q2.** Write statements to (i) create a 4 × 5 double array and (ii) initialise a 2 × 3 int array with 1 to 6.
**Answer:** (i) `double a[][] = new double[4][5];`
(ii) `int b[][] = {{1, 2, 3}, {4, 5, 6}};`

**Q3.** How are the number of rows and the number of columns of a 2D array x found?
**Answer:** x.length gives the number of rows.
x[0].length gives the number of columns.

**Q4.** How is the memory occupied by a 2D array calculated? Find it for `char c[][] = new char[6][4];`.
**Answer:** Rows × columns × bytes per element.
6 × 4 × 2 = 48 bytes.

**Q5.** Write the conditions for the left and right diagonals of an n × n array.
**Answer:** Left: r == c.
Right: r + c == n − 1.

**Q6.** Where should the variable for the sum of each row be set to 0, and why?
**Answer:** Inside the outer loop, before the inner loop.
Then each row starts from 0 instead of adding to the previous rows.

**Q7.** What is the transpose of a matrix? Write the statement that forms it.
**Answer:** The matrix formed by turning rows into columns.
`t[c][r] = a[r][c];`

**Q8.** When is a square matrix symmetric?
**Answer:** When a[r][c] equals a[c][r] for every r and c.
That is, it equals its own transpose.

**Q9.** Write the statement that assigns 100 to the last element of a 4 × 6 array x.
**Answer:** `x[3][5] = 100;`
The last row is 3 and the last column is 5.

**Q10.** Define the NORM of an array as used in ICSE 2025, and write the Java statement that prints it from sum.
**Answer:** The square root of the sum of the squares of all elements.
`System.out.println("NORM = " + Math.sqrt(sum));`

**Q11.** What are boundary elements? Write the condition for a 4 × 4 array.
**Answer:** Elements in the first or last row or the first or last column.
`r == 0 || r == 3 || c == 0 || c == 3`

**Q12.** Why should a row product start with p = 1?
**Answer:** 1 does not change a product.
Starting with 0 would make every product 0.

### Output and error questions (2 marks each)

**Q13.** `int x[][] = {{2, 3, 4}, {7, 9, 10}, {-11, 4, 6}}; System.out.println(x[0][2] * x[2][0]);`
**Answer:** `-44`
4 × −11.

**Q14.** `int x[][] = {{4, 3, 2}, {7, 8, 2}, {8, 3, 10}, {1, 2, 9}};` Give the order and x[0][0] + x[2][2].
**Answer:** 4 × 3.
14 (4 + 10).

**Q15.** `int x[][] = {{2, 4, 5, 6}, {5, 7, 8, 1}, {34, 1, 10, 9}};` Give the position of 34 and x[2][3] + x[1][2].
**Answer:** x[2][0].
17 (9 + 8).

**Q16.** `int X[][] = {{4, 5}, {7, 2}, {19, 4}, {7, 4}};` Give the indexes of the maximum and minimum elements.
**Answer:** Maximum 19 at X[2][0].
Minimum 2 at X[1][1].

**Q17.** `int t[][] = {{1, 2, 3}, {4, 5, 6}}; for (int c = 0; c < 3; c++) System.out.print(t[1][c] + t[0][c] + " ");`
**Answer:** `5 7 9`
The sums of the columns.

**Q18.** `char g[][] = {{'A', 'C', 'E'}, {'M', 'A', 'P'}, {'A', 'C', 'T'}}; System.out.println(g[1][2] + " " + g[2][0] + g[0][2]);`
**Answer:** `P AE`
After the String " ", + joins the characters.

**Q19.** `int m[][] = new int[2][3]; System.out.println(m[1][2] + " " + m.length + " " + m[0].length);`
**Answer:** `0 2 3`
Default value, rows, columns.

**Q20.** Give the left and right diagonal sums of {{1, 3, 5}, {4, 6, 8}, {9, 2, 4}}.
**Answer:** Left 1 + 6 + 4 = 11.
Right 5 + 6 + 9 = 20.

**Q21.** What happens when `int a[][] = new int[3][3]; a[3][0] = 5;` runs?
**Answer:** It compiles but stops with ArrayIndexOutOfBoundsException.
The rows are 0 to 2.

**Q22.** A student writes `for (int r = 0; r < 3; r++) { for (int c = 0; c < 3; c++) { s = 0; s = s + a[r][c]; } System.out.println(s); }` to print row sums. What is wrong?
**Answer:** s is reset inside the inner loop, so each printed "sum" is only the last element of the row.
Move `s = 0;` before the inner loop.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; the output or a sample run follows each.*

### Section B programs (15 marks each)

**Q1.** Write a program to input a 3 × 3 integer array and print its transpose.
**Answer:**
```java
import java.util.*;
class Transpose
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[][] = new int[3][3];
        int t[][] = new int[3][3];
        System.out.println("Enter 9 elements:");
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                a[r][c] = sc.nextInt();
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                t[c][r] = a[r][c];
        System.out.println("Transpose:");
        for (int r = 0; r < 3; r++)
        {
            for (int c = 0; c < 3; c++)
                System.out.print(t[r][c] + " ");
            System.out.println();
        }
    }
}
```
Sample run:
```
Enter 9 elements:
1 2 3
4 5 6
7 8 9
Transpose:
1 4 7
2 5 8
3 6 9
```

**Q2.** Two 3 × 3 matrices are A = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}} and B = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}}. Write a program to find and print C = A + B.
**Answer:**
```java
class MatrixAdd
{
    public static void main(String args[])
    {
        int A[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int B[][] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
        int C[][] = new int[3][3];
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                C[r][c] = A[r][c] + B[r][c];
        System.out.println("A + B =");
        for (int r = 0; r < 3; r++)
        {
            for (int c = 0; c < 3; c++)
                System.out.print(C[r][c] + " ");
            System.out.println();
        }
    }
}
```
Output:
```
A + B =
10 10 10
10 10 10
10 10 10
```

**Q3.** The marks of 4 students in English, Maths and Science are stored in a 4 × 3 array, with the names in a parallel array. Write a program to print each student's total and each subject's average.
**Answer:**
```java
class MarksTable
{
    public static void main(String args[])
    {
        String name[] = {"Ador", "Bisu", "Careen", "Dashi"};
        int m[][] = {{78, 85, 69}, {92, 74, 88}, {55, 61, 70}, {83, 90, 77}};
        String subj[] = {"English", "Maths", "Science"};
        System.out.println("Student totals:");
        for (int r = 0; r < 4; r++)
        {
            int total = 0;
            for (int c = 0; c < 3; c++)
                total = total + m[r][c];
            System.out.println(name[r] + " : " + total);
        }
        System.out.println("Subject averages:");
        for (int c = 0; c < 3; c++)
        {
            int sum = 0;
            for (int r = 0; r < 4; r++)
                sum = sum + m[r][c];
            System.out.println(subj[c] + " : " + (sum / 4.0));
        }
    }
}
```
Output:
```
Student totals:
Ador : 232
Bisu : 254
Careen : 186
Dashi : 250
Subject averages:
English : 77.0
Maths : 77.5
Science : 76.0
```

**Q4.** Write a program to input a 3 × 3 integer array and check whether it is symmetric.
**Answer:**
```java
import java.util.*;
class Symmetric
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[][] = new int[3][3];
        System.out.println("Enter 9 elements:");
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                a[r][c] = sc.nextInt();
        boolean sym = true;
        for (int r = 0; r < 3; r++)
        {
            for (int c = 0; c < 3; c++)
            {
                if (a[r][c] != a[c][r])
                    sym = false;
            }
        }
        if (sym)
            System.out.println("Symmetric matrix");
        else
            System.out.println("Not a symmetric matrix");
    }
}
```
Sample runs:
```
Enter 9 elements:
1 7 3
7 4 5
3 5 6
Symmetric matrix
```
```
Enter 9 elements:
1 2 3
4 5 6
7 8 9
Not a symmetric matrix
```

**Q5.** Write a program to input a 4 × 4 integer array, print its boundary elements in their positions (leaving the inner positions blank) and print their sum.
**Answer:**
```java
import java.util.*;
class Boundary
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[][] = new int[4][4];
        System.out.println("Enter 16 elements:");
        for (int r = 0; r < 4; r++)
            for (int c = 0; c < 4; c++)
                a[r][c] = sc.nextInt();
        int sum = 0;
        System.out.println("Boundary elements:");
        for (int r = 0; r < 4; r++)
        {
            for (int c = 0; c < 4; c++)
            {
                if (r == 0 || r == 3 || c == 0 || c == 3)
                {
                    System.out.print(a[r][c] + " ");
                    sum = sum + a[r][c];
                }
                else
                    System.out.print("  ");
            }
            System.out.println();
        }
        System.out.println("Sum of boundary elements = " + sum);
    }
}
```
Sample run:
```
Enter 16 elements:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Boundary elements:
1 2 3 4
5     8
9     12
13 14 15 16
Sum of boundary elements = 102
```

**Q6.** The array {{12, 45, 7}, {33, 9, 61}, {28, 50, 16}} is given. Write a program to search for a number input by the user and print its row and column, or "not found"; then print the largest element with its position.
**Answer:**
```java
import java.util.*;
class FindInMatrix
{
    public static void main(String args[])
    {
        int a[][] = {{12, 45, 7}, {33, 9, 61}, {28, 50, 16}};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number to search: ");
        int key = sc.nextInt();
        boolean found = false;
        for (int r = 0; r < 3 && !found; r++)
        {
            for (int c = 0; c < 3; c++)
            {
                if (a[r][c] == key)
                {
                    System.out.println(key + " found at row " + r + ", column " + c);
                    found = true;
                    break;
                }
            }
        }
        if (!found)
            System.out.println(key + " not found");
        int max = a[0][0], mr = 0, mc = 0;
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                if (a[r][c] > max)
                {
                    max = a[r][c];
                    mr = r;
                    mc = c;
                }
        System.out.println("Largest element " + max + " at a[" + mr + "][" + mc + "]");
    }
}
```
Sample runs:
```
Enter the number to search: 61
61 found at row 1, column 2
Largest element 61 at a[1][2]
```
```
Enter the number to search: 40
40 not found
Largest element 61 at a[1][2]
```

---

## 12. Competency / Application Questions

**Q1. (Design the array)** A school records the attendance (present days) of 30 students for 12 months. Declare the array and say what a row and a column stand for.
**Model answer:** `int att[][] = new int[30][12];` — a row is a student; a column is a month.

**Q2. (Rows or columns?)** For the same array, which loop gives each student's yearly total and which gives each month's class total?
**Model answer:** Adding along each row (outer loop over students) gives student totals; adding down each column (outer loop over months) gives month totals.

**Q3. (Find the diagonal)** In a 6 × 6 seating plan, which seats are on the right diagonal?
**Model answer:** Seats with r + c == 5: [0][5], [1][4], [2][3], [3][2], [4][1], [5][0].

**Q4. (Check the memory)** A 100 × 100 grid of double values is planned. How much memory do its elements need?
**Model answer:** 10000 × 8 = 80000 bytes (about 78 KB).

**Q5. (Spot the slip)** A NORM program adds `x[r][c]` instead of `x[r][c] * x[r][c]`. For the example array, what does it print instead of √201?
**Model answer:** √(sum of elements) = √49 = 7.0 — the examiners noted that many candidates forgot to square the elements.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** For x of order 4 × 3, x.length is 4.
**R:** For a 2D array, length gives the number of rows.
**Answer:** (c)
**Explanation:** x[0].length gives the columns.

**Q2.**
**A:** The last element of a 3 × 3 array is x[3][3].
**R:** Indexes in each dimension start at 0.
**Answer:** (b)
**Explanation:** It is x[2][2].

**Q3.**
**A:** A 3 × 3 char array occupies 18 bytes.
**R:** A char occupies 2 bytes.
**Answer:** (c)
**Explanation:** 9 × 2.

**Q4.**
**A:** In a 4 × 4 array, x[1][2] lies on the right diagonal.
**R:** Right diagonal elements satisfy r + c == 3.
**Answer:** (c)
**Explanation:** 1 + 2 = 3.

**Q5.**
**A:** The product of a row should start at 0.
**R:** 0 is the identity for addition.
**Answer:** (b)
**Explanation:** A product starts at 1.

**Q6.**
**A:** A symmetric array must be square.
**R:** Nested loops are used to read a 2D array.
**Answer:** (d)
**Explanation:** Both true; unrelated.

**Q7.**
**A:** Matrices of orders 2 × 3 and 3 × 2 can be added element by element.
**R:** Addition needs matrices of the same order.
**Answer:** (b)
**Explanation:** The orders differ.

**Q8.**
**A:** The left diagonal of a square array can be summed with a single loop.
**R:** A single loop cannot visit a 2D array.
**Answer:** (a)
**Explanation:** `sum += x[r][r];` needs only one loop.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The sales table

> The sales of 5 salesmen for 5 products are stored in an int array sales[5][5].

**(i)** How many bytes does the array occupy?
**Answer:** 100.

**(ii)** Which element holds salesman 3's sales of product 1 (counting from 0)?
**Answer:** sales[3][1].

**(iii)** What does adding along row 2 give?
**Answer:** The total sales of salesman 2.

**(iv)** What does adding down column 4 give?
**Answer:** The total sales of product 4.

### Case 2 — The sparse check

> A 4 × 5 array has the rows 4 3 0 1 0 / 1 0 0 2 0 / 1 0 1 0 0 / 0 3 2 0 0.

**(i)** How many zeros are there?
**Answer:** 11.

**(ii)** How many non-zero elements?
**Answer:** 9.

**(iii)** Is it a sparse matrix?
**Answer:** Yes.

**(iv)** Where must the counters be set to 0?
**Answer:** Before the nested loops.

### Case 3 — The diagonal test

> The 4 × 4 array {{3, 4, 2, 5}, {2, 5, 2, 3}, {5, 3, 2, 7}, {1, 3, 7, 1}} is tested.

**(i)** What is the left diagonal sum?
**Answer:** 11.

**(ii)** What is the right diagonal sum?
**Answer:** 11.

**(iii)** Is it a DIAGONAL array?
**Answer:** Yes.

**(iv)** Write the right-diagonal element for row r in a single loop.
**Answer:** x[r][3 - r].

---

## 15. Revision Notes

### Chapter at a glance
- 2D array: a[row][column], both from 0; order = rows × columns.
- a.length = rows; a[0].length = columns; memory = rows × columns × bytes.
- Nested loops: outer rows, inner columns; println after each row to print a matrix.
- Whole-array total before the loops; per-row total inside the outer loop; products start at 1.
- Diagonals (n × n): left r == c, right r + c == n − 1; boundary: first or last row or column.
- Transpose: t[c][r] = a[r][c]; symmetric: a[r][c] == a[c][r].

### Common mistakes

| Mistake | Correct idea |
|---|---|
| a[column][row] | a[row][column] |
| Last element of 3 × 3 written x[3][3] | x[2][2] |
| Row sum reset inside the inner loop | Reset before the inner loop. |
| Product starting at 0 | Start at 1. |
| Adding elements for the NORM | Add their squares, then take the square root. |
| Forgetting to compare and print the result | Print the message for both cases. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 11: Arrays II**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** A 5 × 5 int array occupies:
(a) 25 bytes (b) 200 bytes (c) 50 bytes (d) 100 bytes

**2.** The last element of a 3 × 3 array is:
(a) x[3][3] (b) x[2][2] (c) x[2][3] (d) x[3][2]

**3.** A char array of 4 rows and 3 columns occupies:
(a) 24 bytes (b) 12 bytes (c) 96 bytes (d) 48 bytes

**4.** For `int x[][] = {{2, 3, 4}, {7, 9, 10}, {-11, 4, 6}};`, `x[0][2] * x[2][0]` is:
(a) 24 (b) 16 (c) -44 (d) -22

**5.** The order of `{{4, 3, 2}, {7, 8, 2}, {8, 3, 10}, {1, 2, 9}}` is:
(a) 3 × 4 (b) 12 (c) 4 × 4 (d) 4 × 3

**6.** Right-diagonal condition in a 4 × 4 array:
(a) r + c == 3 (b) r == c (c) r + c == 4 (d) r == 3

**7.** Barcode Scanner in P[2][3] (Mouse, Keyboard, Printer / Scanner, Barcode Scanner, Microphone):
(a) P[0][1] (b) P[1][1] (c) P[1][2] (d) P[0][0]

**8.** x.length for a 2D array gives the number of:
(a) columns (b) elements (c) rows (d) bytes

**9.** The first six odd numbers in a 3 × 2 array:
(a) int x[][] = {{1, 3, 5}, {7, 9, 11}}; (b) int x[][] = {{1, 3}, {5, 7}, {9, 11}}; (c) int x[] = {1, 3, 5, 7, 9, 11}; (d) int x[][] = {1, 3, 5, 7, 9, 11};

**10.** Statement I: A row product starts at 1. Statement II: A row sum is reset inside the inner loop.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

### Part I — Short answers (5 × 2 = 10)

**11.** `int x[][] = {{2, 4, 5, 6}, {5, 7, 8, 1}, {34, 1, 10, 9}};` (a) Position of 34. (b) x[2][3] + x[1][2]. [2]

**12.** Write the conditions for the left and right diagonals of an n × n array. [2]

**13.** `int X[][] = {{4, 5}, {7, 2}, {19, 4}, {7, 4}};` Give the indexes of the maximum and minimum elements. [2]

**14.** How many bytes does a 3 × 3 char array occupy, and what is the index of 'P' in {{'A','C','E'},{'M','A','P'},{'A','C','T'}}? [2]

**15.** What is the NORM of an array? [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Accept a 4 × 4 array and check whether it is a DIAGONAL array (equal left and right diagonal sums). [10]

**17.** Accept a 4 × 5 array and check whether it is a sparse matrix. [10]

**18.** Accept a 3 × 3 array and print the product of each row. [10]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | c | b | d | b | a |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | 100 | sales[3][1] | Salesman 2's total | Product 4's total |
| 2 | 11 | 9 | Yes | Before the loops |
| 3 | 11 | 11 | Yes | x[r][3 - r] |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | d | b | a | c | d | a | b | c | b | c |

**Part I, Q11–15 (2 marks each)**

**11.** x[2][0] (1); 17 (1).
**12.** r == c (1); r + c == n − 1 (1).
**13.** X[2][0] (1); X[1][1] (1).
**14.** 18 bytes (1); x[1][2] (1).
**15.** Square root (1) of the sum of squares of all elements (1).

**Part II (10 marks each)**

**16.–18.** 2D array declared with the right order (2), input with nested loops (2), logic (4), message or output (2).
