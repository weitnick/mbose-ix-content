# Class as the Basis of all Computation

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 5 |
| Title | Class as the Basis of all Computation |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 2. Class as the Basis of all Computation |
| Exam weightage | **Question 3 of Section B** (15 marks) is almost always a **"define a class with the following specifications"** program — member variables, accept/calculate/display methods and a main method that creates an object — usually with **slab-wise billing** (courier, cloud storage, hotel, electricity, railway ticket). Section A adds MCQs on **class versus object**, **creating objects with new** and **primitive versus composite types**. |
| Syllabus scope | Objects encapsulate state and behaviour; member variables (attributes) define state; member methods (operations, messages) define behaviour. Classes as abstractions for sets of objects; class as an object factory; primitive and composite data types — declarations and differences; objects as instances of a class; real-life examples. |
| In short | How a class works as a blueprint for objects, bundling their data and behaviour, and how primitive and composite data types differ. |

> **Note on the text:** CISCE does not prescribe a textbook for ICSE Computer Applications. This chapter is written to the ICSE 2027 syllabus in its own words; its exam questions are the CISCE board papers of 2017–2026 and the specimen papers of 2024 and 2025, answered from CISCE's marking schemes wherever one has been published. **Every program in this chapter was compiled and run (Java 21).**
>
> **Exam note:** In a "define a class" question, marks are given step by step: **class name and variable declarations** with the data types asked, **input with Scanner** in accept(), the **calculation** (often a slab ladder), the **output** in display(), and **main creating an object and calling each method** through it (`ob.accept(); ob.calculate(); ob.display();`). Name variables and methods **exactly as the question does**. For slab billing, charge each slab at its own rate — "first 100 units at ₹2, next 200 at ₹3" means `100*2 + (units-100)*3`, not `units*3`. Read a String with spaces using **nextLine()** before reading numbers.

---

## 1. Complete Lesson

### Objects: state and behaviour

An **object** is a real-world or conceptual entity that has:
- **State** — its **attributes** (characteristics), stored in **member variables**.
- **Behaviour** — what it **does**, given by **member methods** (operations).

| Object | State (member variables) | Behaviour (member methods) |
|---|---|---|
| Student | name, age, marks | accept(), allocation(), print() |
| Bank account | account number, balance | deposit(), withdraw(), showBalance() |
| Mobile phone | brand, battery level | call(), charge(), sendMessage() |
| Cat | name | meow(), eat(), play() |

An object **encapsulates** (wraps together) its state and behaviour. Objects interact by **message passing**: one object asks another to do something by **calling its method**, e.g. `ob.calculate();`.

### Classes

A **class** is a **blueprint (template)** that describes the **common member variables and methods** of a set of similar objects.

- **Class as an abstraction:** it states only the essential features shared by all its objects — every Student has a name and marks.
- **Class as an object factory:** it is used to **produce** any number of similar objects with `new`.
- **Class as a user-defined (composite) data type:** once `class Student` is written, `Student` can be used as a type, just as `int` is.

![Fig. 5.1 Class and objects](figures/ca_ch05_fig01_class_objects.png)

**Example 1.** *(ICSE 2024, Q1(i))* [Picture: a polygon and several shapes — triangle, square, pentagon …] Choose the correct statement: (a) Polygon is the object and the pictures are classes (b) Both polygon and the pictures are classes (c) Polygon is the class and the pictures are objects (d) Both polygon and the pictures are objects
**Solution:** **(c) Polygon is the class and the pictures are objects.**

### Objects as instances of a class

An **object is an instance of a class** — one particular member of the set the class describes, created from the blueprint.

```java
Student s1 = new Student();     // s1 is an object (instance) of class Student
Student s2 = new Student();     // another object of the same class
```
- `Student` — the class (the type).
- `s1`, `s2` — **reference variables** naming the objects.
- `new` — allocates memory for a new object; `Student()` initialises it (a constructor — Chapter 7).
- Each object gets **its own copy** of the member variables; the methods are shared.

Members are reached with the **dot operator**: `s1.name`, `s1.accept()`.

```java
class Box
{
    int l, b;
    int area() { return l * b; }
}
...
Box b1 = new Box();   b1.l = 4;  b1.b = 3;
Box b2 = new Box();   b2.l = 6;  b2.b = 2;
System.out.println(b1.area() + " " + b2.area());   // 12 12
Box b3 = b1;          // b3 refers to the SAME object as b1
b3.l = 10;
System.out.println(b1.l + " " + b1.area());        // 10 30
```

**Example 2.** *(ICSE 2025, Q1(ix))* Which is true for `Game cricket = new Game();`? (a) Game is an object of cricket class (b) New keyword creates object Game (c) Game is a class and cricket is an object (d) Game and cricket are objects
**Solution:** **(c) Game is a class and cricket is an object.**

**Example 3.** *(ICSE 2025, Q2(iii))* Write the Java statement for creating an object named 'sifra' of the class 'Robot', which takes three double parameters.
**Solution:** `Robot sifra = new Robot(2.5, 3.0, 4.5);` (any three values, or variables `a, b, c`).

### Class versus object

| Class | Object |
|---|---|
| A **blueprint / template** | An **instance** created from the blueprint |
| A **logical** entity — no memory for data until objects are made | A **physical** entity — occupies memory |
| Declared **once** with the keyword class | **Many** can be created with new |
| e.g. `Fruit` | e.g. `mango`, `apple` |

### Primitive and composite data types

| Primitive data types | Composite (non-primitive, reference) data types |
|---|---|
| **Built into** Java: byte, short, int, long, float, double, char, boolean | **Built from** primitive types: **classes**, **arrays**, String, interfaces |
| Hold a **single value** | Hold **several values** (an object's fields) — the variable stores a **reference** |
| **Fixed size** (int 4 bytes) | Size depends on the members |
| Declared directly: `int age;` | Declared and then created: `Student s; s = new Student();` |
| Default value 0, false … | Default value **null** |

**Declarations of both kinds:**
```java
int marks = 85;                  // primitive
double price;                    // primitive
Student s = new Student();       // composite (class type)
int arr[] = new int[5];          // composite (array)
```

### The structure of a "define a class" program

```java
import java.util.*;
class ClassName
{
    // 1. member variables (state)
    datatype var1, var2;

    // 2. member methods (behaviour)
    void accept()      { /* read values with Scanner */ }
    void calculate()   { /* compute using the variables */ }
    void display()     { /* print the results */ }

    // 3. main method: create an object and call the methods
    public static void main(String args[])
    {
        ClassName ob = new ClassName();
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```
In BlueJ the main method is often written simply as `void main()`; the standard form `public static void main(String args[])` works everywhere.

### Slab-wise calculations

Many questions charge **different rates for successive slabs**. Add the **full earlier slabs** to the **part of the current slab**:

```java
// first 15 GB at 15, next 15 GB at 13, above 30 GB at 11
if (space <= 15)
    bill = space * 15;
else if (space <= 30)
    bill = 15 * 15 + (space - 15) * 13;
else
    bill = 15 * 15 + 15 * 13 + (space - 30) * 11;
```
For 42 GB: 225 + 195 + 132 = **552**.

**A Scanner trap:** after `next()` or `nextInt()`, the rest of the line (the Enter key) is still waiting; a following `nextLine()` returns an **empty string**. Read text that may contain spaces (a name, an address) with `nextLine()` **first**, or call an extra `nextLine()` to clear the line.

### Summary of the chapter

- **Object** — state (member variables) + behaviour (member methods); objects interact by message passing (method calls).
- **Class** — blueprint; an abstraction for a set of objects; an object factory; a user-defined (composite) data type.
- **Object = instance of a class** — created with `new`; each object has its own copy of the variables; members via the dot operator; `b3 = b1` makes two names for one object.
- **Class vs object** — template vs instance; logical vs physical; one vs many.
- **Primitive vs composite** — built-in single values vs user-defined collections (class, array, String) holding references.
- **Program structure** — variables, accept/calculate/display, main creating an object; slab billing with cumulative slabs.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Describe objects in terms of state and behaviour, with real-life examples.
2. Explain a class as an abstraction, an object factory and a user-defined data type.
3. Create objects with new and access members with the dot operator.
4. Distinguish a class from an object and primitive from composite data types.
5. Write a complete "define a class" program with accept, calculate, display and main.
6. Program slab-wise calculations correctly.

---

## 3. Detailed Section Explanations

### Section 1 — Model the thing
Start every class question by listing the **data** (what the object knows) and the **actions** (what it does) — exactly as the question's specification lists them.

### Section 2 — One blueprint, many objects
`new` builds a fresh object each time. Two objects of the same class can hold completely different values.

### Section 3 — References, not copies
A class-type variable holds a **reference**. `b3 = b1` does not copy the object; both names now refer to the same object.

### Section 4 — Slabs add up
Charge slab by slab; never multiply the whole quantity by the highest rate.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Object | An entity with state and behaviour. |
| State | The values of an object's attributes. |
| Behaviour | What an object does, given by its methods. |
| Member variable | A variable declared in a class (attribute, data member). |
| Member method | A method declared in a class (operation). |
| Class | A blueprint that describes a set of similar objects. |
| Instance | An object created from a class. |
| Object factory | A class seen as a producer of objects. |
| Message passing | Objects interacting by calling each other's methods. |
| new | The operator that creates an object in memory. |
| Reference variable | A variable that refers to an object. |
| Dot operator | Accesses a member of an object or class. |
| Primitive data type | A built-in type holding a single value. |
| Composite data type | A type built from others, e.g. a class or array. |
| User-defined data type | A type created by the programmer — a class. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| `Game cricket = new Game();` | Game is the class, cricket the object |
| Object named mango of class fruit | `fruit mango = new fruit();` |
| Object BridalGown of class Apparel with 34 | `Apparel BridalGown = new Apparel(34);` |
| User-defined data types (array, double, class, boolean) | array and class |
| A class encapsulates | data members and member methods |
| Polygon and shapes picture | Polygon = class, shapes = objects |
| Package of Character and Boolean classes | java.lang |
| To use Scanner | `import java.util.*;` and `Scanner ob = new Scanner(System.in);` |
| An object is called an instance because | it is created from (is one case of) a class |
| Default value of a class-type member | null |

### 5.2 Memory aids

- **"Class = Cookie cutter, Object = Cookie"** — one cutter, many cookies.
- **"SB: State and Behaviour"** — variables and methods.
- **"Slab by slab"** — full slabs first, then the remainder.

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- Every Java class silently extends a built-in class called Object.
- Java frees the memory of objects that no reference points to — garbage collection.
- Large apps contain thousands of classes organised into packages.

---

## 6. Person Profiles

### 6.1 Ole-Johan Dahl (1931–2002) and Kristen Nygaard (1926–2002)
Norwegian computer scientists who created Simula in the 1960s, the first language with classes and objects — the ideas Java's classes are built on. They received the Turing Award in 2001.

### 6.2 Barbara Liskov (born 1939)
An American computer scientist whose work on data abstraction (designing types by what they do, not how they store data) shaped modern class design; she received the Turing Award in 2008.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Software mirrors the world** — classes model customers, tickets, accounts.
- **Specification first** — the question's list of variables and methods is the design.
- **Objects are independent** — each holds its own data.

### 7.2 Real-life connections
- **Meghalaya:** a MeECL electricity bill or a Shillong–Guwahati bus ticket is calculated by exactly this kind of class with slab-wise charges.
- **E-commerce:** each item in a shopping cart is an object with a name, price and quantity.
- **Fitness apps:** a StepTracker object turns steps into calories and kilometres.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section B** (60 marks, any four of six programs) almost always opens with a **"define a class with the following specifications"** program (Question 3 since 2023; Question 4 in 2017–2020), worth 15 marks. **Section A** has MCQs and 2-mark parts on classes, objects and data types.

### 8.1 Graded exercises — solutions

#### Exercise 5A — Concepts

**Q1.** Identify the class, the objects and one method: `Phone p1 = new Phone(); Phone p2 = new Phone(); p1.call();`
**Answer:** Class Phone; objects p1 and p2; method call().

**Q2.** List two member variables and two member methods for a class Book.
**Answer:** Variables: title, price. Methods: accept(), display().

**Q3.** Why is a class called a user-defined data type?
**Answer:** The programmer creates it, and it can then be used as a type to declare variables (objects), like int.

**Q4.** After `Box b3 = b1; b3.l = 10;` what is b1.l?
**Answer:** 10 — b1 and b3 refer to the same object.

#### Exercise 5B — Slab calculations

**Q5.** Units are billed at ₹2 for the first 100 and ₹3 for the next 200. Find the bill for 250 units.
**Answer:** 100 × 2 + 150 × 3 = 200 + 450 = ₹650.

**Q6.** A courier charges ₹800/kg for the first 5 kg, ₹700/kg for the next 5 kg and ₹500/kg above 10 kg. Find the charge for 12 kg.
**Answer:** 4000 + 3500 + 1000 = ₹8500 (₹10000 if international, adding ₹1500).

**Q7.** Hotel charges: first 3 days ₹1000/day, next 4 days ₹900/day, beyond 7 days ₹800/day, plus 18% GST. Find the bill for 9 days.
**Answer:** 3000 + 3600 + 1600 = 8200; GST 1476; total ₹9676.

**Q8.** Write the statements in main to create an object ob of class ElectricBill and call accept(), calculate() and print().
**Answer:** `ElectricBill ob = new ElectricBill(); ob.accept(); ob.calculate(); ob.print();`

### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(viii) (1 mark) | Consider the following statements: `Computer desktop = new Computer(); Computer Mainframe = new Computer();` Name the objects of the class given above: (a) Desktop, Mainframe (b) desktop, Mainframe (c) Computer, Mainframe (d) Computer, desktop |
| ICSE 2026, Q3 (15 marks) | Define a class named StepTracker with the following specifications: Member Variables: String name — stores the user's name; int sw — stores the total number of steps walked by the user; double cb — stores the estimated calories burned by the user; double km — stores the estimated distance walked in kilometers. Member Methods: void accept() — to input the name and the steps walked using Scanner class methods only. void calculate() — calculates calories burned and distance in km based on steps walked: Calories burned = steps walked × 0.04 (1 step burns 0.04 calories); Distance (km) = steps walked / 1300 (1300 steps is approx. 1 km). void display() — display the calories burned, distance in km and the user's name. Write a main method to create an object of the class and invoke the methods. |
| ICSE 2026 Improvement, Q1(xv) (1 mark) | The statement to create an object "BridalGown" of the class "Apparel" with an integer argument as 34 is: (a) `Apparel BridalGown = new Apparel(34);` (b) `BridalGown Apparel = new Apparel(34);` (c) `Apparel BridalGown = new Apparel();` (d) `Apparel BridalGown = new BridalGown(34);` |
| ICSE 2026 Improvement, Q3 (15 marks) | Performance criteria of an employee is calculated based on the inputs as accuracy (a), reliability (r) and adaptability (ad), recorded as 1 to 10, 10 being the excellent score. Define a class with the following specifications: Class name: performance. Member variables: String n — name of the employee; int a, r, ad; double basic, bonus. Member methods: void input() — to accept the name, accuracy, reliability, adaptability and basic from the user using the methods of Scanner class. void calculate() — to calculate the average of the three inputs, average = (accuracy + reliability + adaptability) / 3, and allot the bonus: if average is above 7, the bonus is 7.5% of basic salary, otherwise 5% of the basic salary. void print() — to print the name of the employee and bonus. void main() — to create an object of the class and invoke the methods. |
| ICSE 2025, Q1(vi) (1 mark) | Which of the following is user defined data type? 1. array 2. double 3. class 4. boolean (a) only 1 (b) 1 and 3 (c) only 2 (d) only 4 |
| ICSE 2025, Q1(ix) (1 mark) | Which of the following is true for the given object creation statement? `Game cricket = new Game();` (a) Game is an object of cricket class (b) New keyword creates object Game (c) Game is a class and cricket is an object (d) Game and cricket are objects |
| ICSE 2025, Q2(iii) (2 marks) | Write the Java statement for creating an object named 'sifra' of the class 'Robot', which takes three double parameters. |
| ICSE 2025, Q3 (15 marks) | Define a class named CloudStorage with the following specifications: Member Variables: int acno — stores the user's account number; int space — stores the amount of storage space in GB purchased by the user; double bill — stores the total price to be paid by the user. Member Methods: void accept() — prompts the user to input their account number and storage space using Scanner class methods only. void calculate() — calculates the bill based on the storage space purchased: first 15 GB — Rs 15 per GB; next 15 GB — Rs 13 per GB; above 30 GB — Rs 11 per GB. void display() — displays the account number, storage space and bill to be paid. Write a main method to create an object of the class and invoke the methods of the class with respect to the object. |
| ICSE 2025 Improvement, Q2(v) (2 marks) | In the example given below of class Cat, identify the variable and the methods: [Class diagram: Cat — Name — meow(), eat(), play()] |
| ICSE 2025 Improvement, Q3 (15 marks) | Define a class with following specifications. Class name: Hotel. Member variables: String name — stores name of customer; long mobno — stores mobile number; int days — stores number of days customer stayed in hotel; int bill — stores customer bill. Member methods: void input() — input values using Scanner class methods only. void charge() — calculate bill as per the following criteria: first 3 days — Rs 1000 per day; next 4 days — Rs 900 per day; more than 7 days — Rs 800 per day; bill = bill + gst (18% of bill). void print() — display customer name, mobile number and bill. Invoke all the above methods in main method with the help of an object. |
| ICSE 2025 specimen, Q3 (15 marks) | Define a class with the following specifications: Class name: Bank. Member variables: double p — stores the principal amount; double n — stores the time period in years; double r — stores the rate of interest; double a — stores the amount. Member methods: void accept() — input values for p and n using Scanner class methods only. void calculate() — calculate the amount based on the following conditions: time up to ½ year — rate 9%; more than ½ to 1 year — 10%; more than 1 to 3 years — 11%; more than 3 years — 12%; a = p(1 + r/100)ⁿ. void display() — display the details in the given format: Principal, Time, Rate, Amount. Write the main method to create an object and call the above methods. |
| ICSE 2024, Q1(i) (1 mark) | [Picture: a polygon with several shapes — triangle, quadrilateral, pentagon, hexagon] Consider the above picture and choose the correct statement from the following: (a) Polygon is the object and the pictures are classes (b) Both polygon and the pictures are classes (c) Polygon is the class and the pictures are objects (d) Both polygon and the pictures are objects |
| ICSE 2024, Q1(xvii) (1 mark) | The correct statement to create an object named mango of class fruit: (a) `Fruit Mango = new fruit();` (b) `fruit mango = new fruit();` (c) `Mango fruit = new Mango();` (d) `fruit mango = new mango();` |
| ICSE 2024, Q2(x) (2 marks) | Primitive data types are built in data types which are a part of the wrapper classes. These wrapper classes are encapsulated in the java.lang package. Non primitive datatypes like Scanner class are a part of the utility package for which an object needs to be created. (a) To which package the Character and Boolean classes belong? (b) Write the statement to access the Scanner class in the program. |
| ICSE 2024, Q3 (15 marks) | DTDC, a courier company, charges for the courier based on the weight of the parcel. Define a class with the following specifications: class name: courier. Member variables: name — name of the customer; weight — weight of the parcel in kilograms; address — address of the recipient; bill — amount to be paid; type — 'D' domestic, 'I' international. Member methods: void accept() — to accept the details using the methods of the Scanner class only. void calculate() — to calculate the bill: first 5 kg — Rs 800 per kg; next 5 kg — Rs 700 per kg; above 10 kg — Rs 500 per kg. An additional amount of Rs 1500 is charged if the type of the courier is I (International). void print() — to print the details. void main() — to create an object of the class and invoke the methods. |
| ICSE 2024 specimen, Q1(xviii) (1 mark) | Read the following text, and choose the correct answer: A class encapsulate Data Members that contains the information necessary to represent the class and Member methods that perform operations on the data member. What does a class encapsulate? (a) Information and operation (b) Data members and Member methods (c) Data members and information (d) Member methods and operation |
| ICSE 2024 specimen, Q3 (15 marks) | Define a class with the following specifications: Class name: Eshop. Member variables: String name — name of the item purchased; double price — price of the item purchased. Member methods: void accept() — accept the name and the price of the item using the methods of Scanner class. void calculate() — to calculate the net amount to be paid by a customer, based on the following criteria: price 1000 – 25000: discount 5.0%; 25001 – 57000: 7.5%; 57001 – 100000: 10.0%; more than 100000: 15.0%. void display() — to display the name of the item and the net amount to be paid. Write the main method to create an object and call the above methods. |
| ICSE 2023, Q3 (15 marks) | Design a class with the following specifications: Class name: Student. Member variables: name — name of student; age — age of student; mks — marks obtained; stream — stream allocated (declare the variables using appropriate data types). Member methods: void accept() — accept name, age and marks using methods of Scanner class. void allocation() — allocate the stream: mks ≥ 300 — Science and Computer; ≥ 200 and < 300 — Commerce and Computer; ≥ 75 and < 200 — Arts and Animation; < 75 — Try Again. void print() — display student name, age, mks and stream allocated. Call all the above methods in main method using an object. |
| ICSE 2020, Q1(b) (2 marks) | Write a difference between class and an object. |
| ICSE 2018, Q1(e) (2 marks) | Classify the following as primitive or non-primitive datatypes: (i) char (ii) arrays (iii) int (iv) classes |
| ICSE 2018, Q4 (15 marks) | Design a class RailwayTicket with following description: Instance variables / data members: String name — to store the name of the customer; String coach — to store the type of coach customer wants to travel; long mobno — to store customer's mobile number; int amt — to store basic amount of ticket; int totalamt — to store the amount to be paid after updating the original amount. Member methods: void accept() — to take input for name, coach, mobile number and amount. void update() — to update the amount as per the coach selected (extra amount: First_AC 700, Second_AC 500, Third_AC 250, sleeper none). void display() — to display all details of a customer such as name, coach, total amount and mobile number. Write a main method to create an object of the class and call the above member methods. |
| ICSE 2017, Q3(c) (2 marks) | Why is an object called an instance of a class? |
| ICSE 2017, Q4 (15 marks) | Define a class ElectricBill with the following specifications: class: ElectricBill. Instance variables / data members: String n — to store the name of the customer; int units — to store the number of units consumed; double bill — to store the amount to be paid. Member methods: void accept() — to accept the name of the customer and number of units consumed. void calculate() — to calculate the bill as per the tariff: first 100 units — Rs 2.00 per unit; next 200 units — Rs 3.00 per unit; above 300 units — Rs 5.00 per unit; a surcharge of 2.5% is charged if the number of units consumed is above 300. void print() — to print the details: Name of the customer, Number of units consumed, Bill amount. Write a main method to create an object of the class and call the above member methods. |

**Solutions**

**2026 Q1(viii).** **(b) desktop, Mainframe** — the names after the class name are the objects; Java is case sensitive. *(Worked answer.)*

**2026 Q3.**
```java
import java.util.*;
class StepTracker
{
    String name;        // user's name
    int sw;             // steps walked
    double cb;          // calories burned
    double km;          // distance in km

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter steps walked: ");
        sw = sc.nextInt();
    }

    void calculate()
    {
        cb = sw * 0.04;
        km = sw / 1300.0;
    }

    void display()
    {
        System.out.println("Name            : " + name);
        System.out.println("Calories burned : " + cb);
        System.out.println("Distance (km)   : " + km);
    }

    public static void main(String args[])
    {
        StepTracker ob = new StepTracker();
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```
Sample run:
```
Enter name: Banri Kharkongor
Enter steps walked: 9100
Name            : Banri Kharkongor
Calories burned : 364.0
Distance (km)   : 7.0
```
*(Worked answer.)*

**2026 Improvement Q1(xv).** **(a) `Apparel BridalGown = new Apparel(34);`** *(Worked answer.)*

**2026 Improvement Q3.**
```java
import java.util.*;
class performance
{
    String n;
    int a, r, ad;
    double basic, bonus;

    void input()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        n = sc.nextLine();
        System.out.print("Enter accuracy, reliability and adaptability (1-10): ");
        a = sc.nextInt();
        r = sc.nextInt();
        ad = sc.nextInt();
        System.out.print("Enter basic salary: ");
        basic = sc.nextDouble();
    }

    void calculate()
    {
        double average = (a + r + ad) / 3.0;
        if (average > 7)
            bonus = basic * 7.5 / 100;
        else
            bonus = basic * 5 / 100;
    }

    void print()
    {
        System.out.println("Name  : " + n);
        System.out.println("Bonus : " + bonus);
    }

    public static void main(String args[])
    {
        performance ob = new performance();
        ob.input();
        ob.calculate();
        ob.print();
    }
}
```
Sample run (average 8 is above 7, so 7.5% of 40000):
```
Enter name: Ibapynshai
Enter accuracy, reliability and adaptability (1-10): 8 7 9
Enter basic salary: 40000
Name  : Ibapynshai
Bonus : 3000.0
```
*(Worked answer.)*

**2025 Q1(vi).** **(b) 1 and 3** — arrays and classes are built by the programmer; double and boolean are primitive.

**2025 Q1(ix).** **(c) Game is a class and cricket is an object.**

**2025 Q2(iii).** `Robot sifra = new Robot(a, b, c);` with three double values or variables, e.g. `Robot sifra = new Robot(2.5, 3.0, 4.5);`

**2025 Q3.** As in the scheme, the bill is built slab by slab:
```java
import java.util.*;
class CloudStorage
{
    int acno, space;
    double bill;

    void accept()
    {
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter account number: ");
        acno = ob.nextInt();
        System.out.print("Enter storage space (GB): ");
        space = ob.nextInt();
    }

    void calculate()
    {
        if (space <= 15)
            bill = space * 15;
        else if (space <= 30)
            bill = 15 * 15 + (space - 15) * 13;
        else
            bill = 15 * 15 + 15 * 13 + (space - 30) * 11;
    }

    void display()
    {
        System.out.println("Account number  = " + acno);
        System.out.println("Storage space   = " + space);
        System.out.println("Bill to be paid = " + bill);
    }

    public static void main(String args[])
    {
        CloudStorage c = new CloudStorage();
        c.accept();
        c.calculate();
        c.display();
    }
}
```
Sample run (42 GB: 225 + 195 + 132):
```
Enter account number: 1021
Enter storage space (GB): 42
Account number  = 1021
Storage space   = 42
Bill to be paid = 552.0
```

**2025 Improvement Q2(v).** **Variable:** Name. **Methods:** meow(), eat(), play(). *(Worked answer.)*

**2025 Improvement Q3.**
```java
import java.util.*;
class Hotel
{
    String name;
    long mobno;
    int days;
    int bill;

    void input()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter customer name: ");
        name = sc.nextLine();
        System.out.print("Enter mobile number: ");
        mobno = sc.nextLong();
        System.out.print("Enter number of days: ");
        days = sc.nextInt();
    }

    void charge()
    {
        if (days <= 3)
            bill = days * 1000;
        else if (days <= 7)
            bill = 3 * 1000 + (days - 3) * 900;
        else
            bill = 3 * 1000 + 4 * 900 + (days - 7) * 800;
        bill = bill + bill * 18 / 100;      // add 18% GST
    }

    void print()
    {
        System.out.println("Name   : " + name);
        System.out.println("Mobile : " + mobno);
        System.out.println("Bill   : " + bill);
    }

    public static void main(String args[])
    {
        Hotel ob = new Hotel();
        ob.input();
        ob.charge();
        ob.print();
    }
}
```
Sample run (9 days: 3000 + 3600 + 1600 = 8200; GST 1476):
```
Enter customer name: Rina Marak
Enter mobile number: 9876543210
Enter number of days: 9
Name   : Rina Marak
Mobile : 9876543210
Bill   : 9676
```
*(Worked answer.)*

**2025 specimen Q3.** The draft scheme's ladder has slips (it tests n > 0.5 && n >= 1, r > 1 and omits the 12% case); the corrected program:
```java
import java.util.*;
class Bank
{
    double p, n, r, a;      // principal, years, rate, amount

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter principal: ");
        p = sc.nextDouble();
        System.out.print("Enter time in years: ");
        n = sc.nextDouble();
    }

    void calculate()
    {
        if (n <= 0.5)
            r = 9;
        else if (n <= 1)
            r = 10;
        else if (n <= 3)
            r = 11;
        else
            r = 12;
        a = p * Math.pow(1 + r / 100, n);
    }

    void display()
    {
        System.out.println("Principal\tTime\tRate\tAmount");
        System.out.println(p + "\t\t" + n + "\t" + r + "\t" + Math.round(a * 100) / 100.0);
    }

    public static void main(String args[])
    {
        Bank ob = new Bank();
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```
Sample run (2 years at 11%):
```
Enter principal: 10000
Enter time in years: 2
Principal    Time    Rate    Amount
10000.0      2.0     11.0    12321.0
```

**2024 Q1(i).** **(c) Polygon is the class and the pictures are objects.**

**2024 Q1(xvii).** **(b) `fruit mango = new fruit();`**

**2024 Q2(x).** (a) **java.lang**. (b) `import java.util.*;` and then `Scanner ob = new Scanner(System.in);`

**2024 Q3.** Following the scheme, with one correction: reading the name with next() and then the address with nextLine() would leave the address empty, so both are read with nextLine():
```java
import java.util.*;
class courier
{
    String name, address;
    double weight, bill;
    char type;

    void accept()
    {
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = ob.nextLine();
        System.out.print("Enter address: ");
        address = ob.nextLine();
        System.out.print("Enter weight (kg): ");
        weight = ob.nextDouble();
        System.out.print("Enter type (D/I): ");
        type = ob.next().charAt(0);
    }

    void calculate()
    {
        if (weight <= 5)
            bill = weight * 800;
        else if (weight <= 10)
            bill = 5 * 800 + (weight - 5) * 700;
        else
            bill = 5 * 800 + 5 * 700 + (weight - 10) * 500;
        if (type == 'I' || type == 'i')
            bill = bill + 1500;
    }

    void print()
    {
        System.out.println("Name    : " + name);
        System.out.println("Address : " + address);
        System.out.println("Weight  : " + weight + " kg");
        System.out.println("Type    : " + type);
        System.out.println("Bill    : Rs " + bill);
    }

    public static void main(String args[])
    {
        courier c = new courier();
        c.accept();
        c.calculate();
        c.print();
    }
}
```
Sample run (12 kg international: 4000 + 3500 + 1000 + 1500):
```
Enter name: Daniel Syiem
Enter address: Laitumkhrah, Shillong
Enter weight (kg): 12
Enter type (D/I): I
Name    : Daniel Syiem
Address : Laitumkhrah, Shillong
Weight  : 12.0 kg
Type    : I
Bill    : Rs 10000.0
```

**2024 specimen Q1(xviii).** **(b) Data members and Member methods.** *(Worked answer.)*

**2024 specimen Q3.**
```java
import java.util.*;
class Eshop
{
    String name;
    double price;
    double net;

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter item name: ");
        name = sc.nextLine();
        System.out.print("Enter price: ");
        price = sc.nextDouble();
    }

    void calculate()
    {
        double rate;
        if (price >= 1000 && price <= 25000)
            rate = 5.0;
        else if (price >= 25001 && price <= 57000)
            rate = 7.5;
        else if (price >= 57001 && price <= 100000)
            rate = 10.0;
        else if (price > 100000)
            rate = 15.0;
        else
            rate = 0;                   // below 1000: no discount
        net = price - price * rate / 100;
    }

    void display()
    {
        System.out.println("Item       : " + name);
        System.out.println("Net amount : " + net);
    }

    public static void main(String args[])
    {
        Eshop ob = new Eshop();
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```
Sample run (62000 is in the 10% slab):
```
Enter item name: Laptop
Enter price: 62000
Item       : Laptop
Net amount : 55800.0
```
*(Worked answer.)*

**2023 Q3.**
```java
import java.util.*;
class Student
{
    String name;
    int age;
    int mks;
    String stream;

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter age: ");
        age = sc.nextInt();
        System.out.print("Enter marks: ");
        mks = sc.nextInt();
    }

    void allocation()
    {
        if (mks >= 300)
            stream = "Science and Computer";
        else if (mks >= 200)
            stream = "Commerce and Computer";
        else if (mks >= 75)
            stream = "Arts and Animation";
        else
            stream = "Try Again";
    }

    void print()
    {
        System.out.println("Name   : " + name);
        System.out.println("Age    : " + age);
        System.out.println("Marks  : " + mks);
        System.out.println("Stream : " + stream);
    }

    public static void main(String args[])
    {
        Student ob = new Student();
        ob.accept();
        ob.allocation();
        ob.print();
    }
}
```
Sample run:
```
Enter name: Tashi Lepcha
Enter age: 15
Enter marks: 245
Name   : Tashi Lepcha
Age    : 15
Marks  : 245
Stream : Commerce and Computer
```

**2020 Q1(b).** A **class** is a **blueprint (template)** that defines the variables and methods of similar objects; an **object** is an **instance** of the class that actually exists in memory with its own values. *(Worked answer.)*

**2018 Q1(e).** (i) char — **primitive** (ii) arrays — **non-primitive** (iii) int — **primitive** (iv) classes — **non-primitive**.

**2018 Q4.**
```java
import java.util.*;
class RailwayTicket
{
    String name, coach;
    long mobno;
    int amt, totalamt;

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter coach (First_AC/Second_AC/Third_AC/sleeper): ");
        coach = sc.next();
        System.out.print("Enter mobile number: ");
        mobno = sc.nextLong();
        System.out.print("Enter basic amount: ");
        amt = sc.nextInt();
    }

    void update()
    {
        if (coach.equalsIgnoreCase("First_AC"))
            totalamt = amt + 700;
        else if (coach.equalsIgnoreCase("Second_AC"))
            totalamt = amt + 500;
        else if (coach.equalsIgnoreCase("Third_AC"))
            totalamt = amt + 250;
        else
            totalamt = amt;                 // sleeper: no extra amount
    }

    void display()
    {
        System.out.println("Name         : " + name);
        System.out.println("Coach        : " + coach);
        System.out.println("Total amount : " + totalamt);
        System.out.println("Mobile no.   : " + mobno);
    }

    public static void main(String args[])
    {
        RailwayTicket ob = new RailwayTicket();
        ob.accept();
        ob.update();
        ob.display();
    }
}
```
Sample run:
```
Enter name: Merina Sangma
Enter coach (First_AC/Second_AC/Third_AC/sleeper): Second_AC
Enter mobile number: 9436012345
Enter basic amount: 1800
Name         : Merina Sangma
Coach        : Second_AC
Total amount : 2300
Mobile no.   : 9436012345
```

**2017 Q3(c).** An object is called an **instance of a class** because it is **created from the class** (the blueprint) — it is **one particular case** of the class, with its own values for the members the class defines. *(Worked answer.)*

**2017 Q4.**
```java
import java.util.*;
class ElectricBill
{
    String n;
    int units;
    double bill;

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter customer name: ");
        n = sc.nextLine();
        System.out.print("Enter units consumed: ");
        units = sc.nextInt();
    }

    void calculate()
    {
        if (units <= 100)
            bill = units * 2.00;
        else if (units <= 300)
            bill = 100 * 2.00 + (units - 100) * 3.00;
        else
        {
            bill = 100 * 2.00 + 200 * 3.00 + (units - 300) * 5.00;
            bill = bill + bill * 2.5 / 100;     // surcharge above 300 units
        }
    }

    void print()
    {
        System.out.println("Name of the customer: " + n);
        System.out.println("Number of units consumed: " + units);
        System.out.println("Bill amount: " + bill);
    }

    public static void main(String args[])
    {
        ElectricBill ob = new ElectricBill();
        ob.accept();
        ob.calculate();
        ob.print();
    }
}
```
Sample run (350 units: 200 + 600 + 250 = 1050, plus 2.5% surcharge):
```
Enter customer name: Kyrshan Lyngdoh
Enter units consumed: 350
Name of the customer: Kyrshan Lyngdoh
Number of units consumed: 350
Bill amount: 1076.25
```
*(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Write the statement to create an object named sedan of class Car that takes a String and an int.
**Answer:** `Car sedan = new Car("Honda", 2026);`

**Q2.** (2 marks) Name the state and behaviour of a class Fan.
**Answer:** State — speed, colour, isOn; behaviour — switchOn(), switchOff(), changeSpeed().

**Q3.** (2 marks) For the cloud-storage slabs (15, 13, 11 per GB), find the bill for 20 GB.
**Answer:** 15 × 15 + 5 × 13 = 225 + 65 = 290.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 15 marks | "Define a class" with accept, slab calculation, display and main | 8.2, Section 11 |
| MCQ | Class vs object from a picture or statement; correct object-creation statement | 8.2, Section 1 |
| 2 marks | Primitive vs non-primitive; why an object is an instance; Scanner access statement | 8.2, 5.1 |

---

## 9. MCQs with Explanations

### Objects, state and behaviour (Q1–Q14)

**Q1.** An object is characterised by its
- (a) state and behaviour
- (b) package and import
- (c) keywords only
- (d) comments

**Answer:** (a) state and behaviour
**Explanation:** Attributes and methods.

**Q2.** The state of an object is stored in its
- (a) methods
- (b) member variables
- (c) comments
- (d) packages

**Answer:** (b) member variables
**Explanation:** Also called attributes or data members.

**Q3.** The behaviour of an object is given by its
- (a) data members
- (b) literals
- (c) packages
- (d) member methods

**Answer:** (d) member methods
**Explanation:** Operations the object can perform.

**Q4.** For a class Cat with Name, meow(), eat() and play(), the variable is
- (a) meow()
- (b) eat()
- (c) play()
- (d) Name

**Answer:** (d) Name
**Explanation:** The rest are methods (2025 Improvement).

**Q5.** Objects interact with each other by
- (a) message passing (calling methods)
- (b) sharing all variables
- (c) importing packages
- (d) comments

**Answer:** (a) message passing (calling methods)
**Explanation:** e.g. ob.calculate();

**Q6.** A class encapsulates
- (a) information and operation
- (b) data members and member methods
- (c) data members and information
- (d) member methods and operation

**Answer:** (b) data members and member methods
**Explanation:** 2024 specimen.

**Q7.** For a BankAccount object, which is a behaviour?
- (a) balance
- (b) account number
- (c) withdraw()
- (d) name

**Answer:** (c) withdraw()
**Explanation:** The others are state.

**Q8.** For a MobilePhone object, which is part of its state?
- (a) call()
- (b) sendMessage()
- (c) charge()
- (d) battery level

**Answer:** (d) battery level
**Explanation:** An attribute.

**Q9.** Wrapping state and behaviour together in an object is
- (a) inheritance
- (b) polymorphism
- (c) compilation
- (d) encapsulation

**Answer:** (d) encapsulation
**Explanation:** The class is the unit.

**Q10.** Variables declared inside a class (outside methods) are called
- (a) local variables
- (b) member variables
- (c) literals
- (d) parameters

**Answer:** (b) member variables
**Explanation:** Instance variables / data members.

**Q11.** Methods declared inside a class are called
- (a) member methods
- (b) packages
- (c) constants
- (d) tokens

**Answer:** (a) member methods
**Explanation:** They define behaviour.

**Q12.** Each object of a class has
- (a) no variables
- (b) a shared copy of every instance variable
- (c) only methods
- (d) its own copy of the instance variables

**Answer:** (d) its own copy of the instance variables
**Explanation:** Methods are shared.

**Q13.** Which is a real-life example of an object?
- (a) the idea "fruit"
- (b) a package
- (c) the word "class"
- (d) a particular mango on your table

**Answer:** (d) a particular mango on your table
**Explanation:** "Fruit" is the class.

**Q14.** Statement I: Objects have state. Statement II: Objects have behaviour.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (a) Both statements are true
**Explanation:** State + behaviour.

### Classes (Q15–Q28)

**Q15.** A class is best described as a
- (a) blueprint for objects
- (b) variable
- (c) keyword
- (d) loop

**Answer:** (a) blueprint for objects
**Explanation:** A template.

**Q16.** A class is called an object factory because it
- (a) stores files
- (b) can produce many similar objects
- (c) runs programs
- (d) compiles code

**Answer:** (b) can produce many similar objects
**Explanation:** With new.

**Q17.** A class is called a user-defined data type because
- (a) Java defines it
- (b) it holds one value
- (c) it has no methods
- (d) the programmer creates it and uses it as a type

**Answer:** (d) the programmer creates it and uses it as a type
**Explanation:** e.g. Student s;

**Q18.** Which are user-defined data types?
- (a) array and class
- (b) only array
- (c) only double
- (d) only boolean

**Answer:** (a) array and class
**Explanation:** 2025 MS.

**Q19.** In a picture of a polygon and various shapes, the polygon is
- (a) the class
- (b) an object
- (c) a method
- (d) a variable

**Answer:** (a) the class
**Explanation:** The shapes are its objects (2024 MS).

**Q20.** A class as an abstraction means it
- (a) hides its name
- (b) holds only one object
- (c) describes the common essential features of a set of objects
- (d) has no variables

**Answer:** (c) describes the common essential features of a set of objects
**Explanation:** Every student has a name and marks.

**Q21.** The keyword used to declare a class is
- (a) new
- (b) object
- (c) import
- (d) class

**Answer:** (d) class
**Explanation:** `class Student { … }`

**Q22.** A class occupies memory for its instance data
- (a) as soon as it is written
- (b) never
- (c) only when objects are created
- (d) only in comments

**Answer:** (c) only when objects are created
**Explanation:** A class is a logical entity.

**Q23.** How many objects can be created from one class?
- (a) only one
- (b) exactly two
- (c) none
- (d) any number

**Answer:** (d) any number
**Explanation:** Each with new.

**Q24.** Which statement about class and object is true?
- (a) A class is a physical entity
- (b) An object is a logical entity
- (c) A class is a template; an object is an instance
- (d) They are the same

**Answer:** (c) A class is a template; an object is an instance
**Explanation:** Logical vs physical.

**Q25.** "Fruit" is to "mango" as
- (a) object is to class
- (b) class is to object
- (c) method is to variable
- (d) package is to class

**Answer:** (b) class is to object
**Explanation:** Mango is one fruit.

**Q26.** Which is NOT usually part of a "define a class" program?
- (a) member variables
- (b) an accept method
- (c) a main method creating an object
- (d) a package of wrapper classes

**Answer:** (d) a package of wrapper classes
**Explanation:** The others are the standard parts.

**Q27.** In BlueJ, the main method is often written as
- (a) void main()
- (b) main void()
- (c) static main
- (d) main()void

**Answer:** (a) void main()
**Explanation:** The standard form is public static void main(String args[]).

**Q28.** Statement I: A class is a composite data type. Statement II: int is a composite data type.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (c) Statement I is true, Statement II is false
**Explanation:** int is primitive.

### Creating and using objects (Q29–Q44)

**Q29.** In `Game cricket = new Game();`
- (a) Game is an object of cricket class
- (b) new creates the object Game
- (c) Game and cricket are objects
- (d) Game is a class and cricket is an object

**Answer:** (d) Game is a class and cricket is an object
**Explanation:** 2025 MS.

**Q30.** The correct statement to create an object mango of class fruit is
- (a) fruit mango = fruit();
- (b) fruit mango = new fruit();
- (c) Mango fruit = new Mango();
- (d) fruit mango = new mango();

**Answer:** (b) fruit mango = new fruit();
**Explanation:** 2024 MS.

**Q31.** In `Computer desktop = new Computer(); Computer Mainframe = new Computer();` the objects are
- (a) Computer only
- (b) desktop, Mainframe
- (c) Computer, Mainframe
- (d) new, Computer

**Answer:** (b) desktop, Mainframe
**Explanation:** The names after the class name are the objects (2026).

**Q32.** The object BridalGown of class Apparel with argument 34 is created by
- (a) Apparel BridalGown = new Apparel(34);
- (b) BridalGown Apparel = new Apparel(34);
- (c) Apparel BridalGown = new Apparel();
- (d) Apparel BridalGown = new BridalGown(34);

**Answer:** (a) Apparel BridalGown = new Apparel(34);
**Explanation:** 2026 Improvement.

**Q33.** The operator that allocates memory for a new object is
- (a) dot
- (b) new
- (c) ==
- (d) +

**Answer:** (b) new
**Explanation:** Dynamic memory allocation.

**Q34.** Members of an object are accessed with the
- (a) dot operator
- (b) comma
- (c) colon
- (d) new operator

**Answer:** (a) dot operator
**Explanation:** ob.accept().

**Q35.** In `Student s1 = new Student();`, s1 is a
- (a) class
- (b) keyword
- (c) reference variable naming an object
- (d) primitive variable

**Answer:** (c) reference variable naming an object
**Explanation:** It refers to the object.

**Q36.** After `Box b3 = b1; b3.l = 10;`, the value of b1.l is
- (a) the old value
- (b) 0
- (c) 10
- (d) an error

**Answer:** (c) 10
**Explanation:** b1 and b3 refer to the same object.

**Q37.** For two separate objects b1 and b2 of class Box, `b1 == b2` is
- (a) true
- (b) false
- (c) an error
- (d) null

**Answer:** (b) false
**Explanation:** == compares references.

**Q38.** An uninitialised int member of a new object holds
- (a) null
- (b) 1
- (c) 0
- (d) garbage

**Answer:** (c) 0
**Explanation:** Default value of int members.

**Q39.** To call the method calculate() of object ob, write
- (a) calculate.ob();
- (b) ob.calculate();
- (c) ob->calculate();
- (d) ob:calculate();

**Answer:** (b) ob.calculate();
**Explanation:** Dot operator.

**Q40.** The statement to create an object sifra of class Robot with three double values is
- (a) Robot sifra = new Robot(2.5, 3.0, 4.5);
- (b) sifra Robot = new sifra();
- (c) Robot = new sifra(2.5);
- (d) new Robot sifra;

**Answer:** (a) Robot sifra = new Robot(2.5, 3.0, 4.5);
**Explanation:** 2025 MS.

**Q41.** Why is an object called an instance of a class?
- (a) It is a keyword
- (b) It is created from the class as one particular case of it
- (c) It is a package
- (d) It has no data

**Answer:** (b) It is created from the class as one particular case of it
**Explanation:** 2017 Q3(c).

**Q42.** Which declares a reference to a Student object without creating it?
- (a) Student s;
- (b) Student s = new Student();
- (c) new Student();
- (d) s.Student();

**Answer:** (a) Student s;
**Explanation:** s is null until an object is assigned.

**Q43.** The statement to access the Scanner class in a program is
- (a) import java.lang.*;
- (b) import java.util.*;
- (c) package java.util;
- (d) include Scanner;

**Answer:** (b) import java.util.*;
**Explanation:** 2024 MS.

**Q44.** The Character and Boolean classes belong to
- (a) java.util
- (b) java.io
- (c) java.awt
- (d) java.lang

**Answer:** (d) java.lang
**Explanation:** 2024 MS.

### Primitive and composite types (Q45–Q54)

**Q45.** Which is a primitive data type?
- (a) array
- (b) class
- (c) String
- (d) char

**Answer:** (d) char
**Explanation:** 2018 MS.

**Q46.** Which is a non-primitive data type?
- (a) int
- (b) double
- (c) char
- (d) arrays

**Answer:** (d) arrays
**Explanation:** Composite.

**Q47.** A composite data type variable stores
- (a) a single value of fixed size
- (b) a reference to an object
- (c) only true or false
- (d) a character

**Answer:** (b) a reference to an object
**Explanation:** The object holds the values.

**Q48.** The default value of a class-type member is
- (a) 0
- (b) false
- (c) null
- (d) an empty space

**Answer:** (c) null
**Explanation:** No object yet.

**Q49.** Primitive data types are
- (a) built into Java
- (b) created by the programmer
- (c) always arrays
- (d) classes

**Answer:** (a) built into Java
**Explanation:** 8 types.

**Q50.** Which declaration creates a composite-type object?
- (a) int x = 5;
- (b) double d;
- (c) Student s = new Student();
- (d) char c = 'a';

**Answer:** (c) Student s = new Student();
**Explanation:** A class type.

**Q51.** A difference between primitive and composite types is that composite types
- (a) have a fixed size of 4 bytes
- (b) cannot hold values
- (c) are built from primitive types and can hold several values
- (d) are keywords

**Answer:** (c) are built from primitive types and can hold several values
**Explanation:** e.g. a Student has name, age, marks.

**Q52.** String is
- (a) a primitive type
- (b) a class (non-primitive)
- (c) a keyword
- (d) an operator

**Answer:** (b) a class (non-primitive)
**Explanation:** In java.lang.

**Q53.** Which pair is correctly classified?
- (a) int — composite; class — primitive
- (b) char — composite; array — primitive
- (c) double — composite; String — primitive
- (d) int — primitive; class — composite

**Answer:** (d) int — primitive; class — composite
**Explanation:** 2018 Q1(e).

**Q54.** Statement I: A primitive variable stores its value directly. Statement II: A class-type variable stores the object itself.
- (a) Both statements are true
- (b) Both statements are false
- (c) Statement I is true, Statement II is false
- (d) Statement I is false, Statement II is true

**Answer:** (c) Statement I is true, Statement II is false
**Explanation:** It stores a reference.

### Class programs and slab calculations (Q55–Q76)

**Q55.** In a StepTracker class, calories = steps × 0.04. For 9100 steps the calories are
- (a) 91.0
- (b) 364.0
- (c) 3640.0
- (d) 36.4

**Answer:** (b) 364.0
**Explanation:** 9100 × 0.04.

**Q56.** With distance = steps / 1300.0, 9100 steps give
- (a) 7.0 km
- (b) 70.0 km
- (c) 0.7 km
- (d) 13 km

**Answer:** (a) 7.0 km
**Explanation:** 9100 ÷ 1300.

**Q57.** Cloud storage at 15/GB for the first 15 GB, 13/GB for the next 15 and 11/GB above 30 costs, for 42 GB,
- (a) 462
- (b) 630
- (c) 552
- (d) 546

**Answer:** (c) 552
**Explanation:** 225 + 195 + 132.

**Q58.** For the same rates, 20 GB costs
- (a) 290
- (b) 300
- (c) 260
- (d) 220

**Answer:** (a) 290
**Explanation:** 225 + 65.

**Q59.** Electricity at ₹2 for the first 100 units and ₹3 for the next 200 costs, for 250 units,
- (a) ₹500
- (b) ₹750
- (c) ₹650
- (d) ₹600

**Answer:** (c) ₹650
**Explanation:** 200 + 450.

**Q60.** For 350 units (₹5/unit above 300, plus 2.5% surcharge), the bill is
- (a) ₹1050
- (b) ₹1076.25
- (c) ₹1100
- (d) ₹1750

**Answer:** (b) ₹1076.25
**Explanation:** 1050 + 26.25.

**Q61.** A courier charges ₹800/kg (first 5 kg), ₹700/kg (next 5 kg), ₹500/kg above 10 kg. A 12 kg domestic parcel costs
- (a) ₹6000
- (b) ₹9600
- (c) ₹7500
- (d) ₹8500

**Answer:** (d) ₹8500
**Explanation:** 4000 + 3500 + 1000.

**Q62.** The same 12 kg parcel sent internationally (₹1500 extra) costs
- (a) ₹10000
- (b) ₹8500
- (c) ₹9500
- (d) ₹11500

**Answer:** (a) ₹10000
**Explanation:** 8500 + 1500.

**Q63.** A hotel charges ₹1000/day for 3 days, ₹900/day for the next 4 and ₹800/day beyond 7, plus 18% GST. 9 days cost
- (a) ₹8200
- (b) ₹9676
- (c) ₹9000
- (d) ₹8856

**Answer:** (b) ₹9676
**Explanation:** 8200 + 1476.

**Q64.** In the Eshop question, an item of ₹62000 gets a discount of
- (a) 5%
- (b) 7.5%
- (c) 10%
- (d) 15%

**Answer:** (c) 10%
**Explanation:** 57001–100000 slab.

**Q65.** The net amount for the ₹62000 item is
- (a) ₹55800
- (b) ₹57350
- (c) ₹52700
- (d) ₹58900

**Answer:** (a) ₹55800
**Explanation:** 62000 − 6200.

**Q66.** In the Student class, 245 marks allocate the stream
- (a) Science and Computer
- (b) Commerce and Computer
- (c) Arts and Animation
- (d) Try Again

**Answer:** (b) Commerce and Computer
**Explanation:** ≥ 200 and < 300.

**Q67.** In the RailwayTicket class, a Second_AC ticket with basic ₹1800 totals
- (a) ₹1800
- (b) ₹2500
- (c) ₹2050
- (d) ₹2300

**Answer:** (d) ₹2300
**Explanation:** 1800 + 500.

**Q68.** In the performance class, accuracy 8, reliability 7 and adaptability 9 give an average of
- (a) 7
- (b) 7.5
- (c) 24
- (d) 8

**Answer:** (d) 8
**Explanation:** 24 ÷ 3.

**Q69.** With that average and basic ₹40000, the bonus is
- (a) ₹2000
- (b) ₹3000
- (c) ₹4000
- (d) ₹2500

**Answer:** (b) ₹3000
**Explanation:** Above 7, so 7.5%.

**Q70.** Comparing strings like "First_AC" regardless of capital or small letters uses
- (a) ==
- (b) equals()
- (c) equalsIgnoreCase()
- (d) compareTo()

**Answer:** (c) equalsIgnoreCase()
**Explanation:** As in the 2018 scheme.

**Q71.** After `name = sc.next();`, a call `address = sc.nextLine();` usually gives
- (a) the full address
- (b) an error
- (c) an empty string
- (d) the name again

**Answer:** (c) an empty string
**Explanation:** It reads the rest of the name's line.

**Q72.** A data type suitable for a mobile number such as 9436012345 is
- (a) int
- (b) short
- (c) long
- (d) byte

**Answer:** (c) long
**Explanation:** It exceeds the int range.

**Q73.** The method that reads a single character for a courier type ('D' or 'I') is
- (a) next().charAt(0)
- (b) nextInt()
- (c) nextLine().length()
- (d) nextDouble()

**Answer:** (a) next().charAt(0)
**Explanation:** First character of the word.

**Q74.** In main, the correct order of statements is usually
- (a) create the object, then call accept, calculate and display
- (b) call methods, then create the object
- (c) only declare variables
- (d) call display before accept

**Answer:** (a) create the object, then call accept, calculate and display
**Explanation:** Methods are called through the object.

**Q75.** In slab billing, "first 100 units at ₹2, next at ₹3" for 150 units is computed as
- (a) 150 × 3
- (b) 150 × 2
- (c) 100 × 2 + 50 × 3
- (d) 100 × 3 + 50 × 2

**Answer:** (c) 100 × 2 + 50 × 3
**Explanation:** Each slab at its own rate.

**Q76.** Which data type is best for the bill in rupees and paise?
- (a) boolean
- (b) char
- (c) int
- (d) double

**Answer:** (d) double
**Explanation:** It can hold decimals.

---

## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** Distinguish between a class and an object.
**Answer:** A class is a blueprint (template) describing the variables and methods of similar objects.
An object is an instance of the class that exists in memory with its own values.

**Q2.** What are the state and behaviour of an object? Give an example.
**Answer:** State is the set of values of its attributes (member variables); behaviour is what it does (member methods).
A Student has name and marks (state) and accept(), print() (behaviour).

**Q3.** Why is a class called an object factory?
**Answer:** Because any number of similar objects can be produced from it.
Each object is created with new.

**Q4.** Why is a class called a user-defined data type?
**Answer:** It is created by the programmer, not built into Java.
Once defined, it can be used as a type to declare objects, like `Student s;`.

**Q5.** What is message passing?
**Answer:** The way objects communicate — one object calls a method of another.
e.g. `ob.calculate();` sends the message "calculate" to ob.

**Q6.** Distinguish between primitive and composite data types.
**Answer:** Primitive types are built in, hold one value and have fixed sizes (int, char).
Composite types (class, array, String) are built from primitives and hold references to objects.

**Q7.** What does the new operator do in `Student s = new Student();`?
**Answer:** It allocates memory for a new Student object.
The reference to that object is stored in s.

**Q8.** Why is an object called an instance of a class?
**Answer:** It is created from the class blueprint.
It is one particular case of the class, with its own values.

**Q9.** Name the parts of a typical "define a class" program.
**Answer:** Member variables and member methods (accept, calculate, display).
A main method that creates an object and calls the methods.

**Q10.** Write two member variables and two member methods of a class Hotel.
**Answer:** Variables: name, days (also mobno, bill).
Methods: input(), charge() (also print()).

**Q11.** Explain slab-wise billing with an example.
**Answer:** Each slab is charged at its own rate and the amounts are added.
For 250 units at ₹2 (first 100) and ₹3 (next 200): 100 × 2 + 150 × 3 = ₹650.

**Q12.** Why should text with spaces be read with nextLine() before numbers?
**Answer:** next() reads only one word; nextLine() reads the whole line.
After nextInt() or next(), a following nextLine() returns the empty rest of the line.

### Output and error questions (2 marks each)

**Q13.** Give the output: `Box b1 = new Box(); b1.l = 4; b1.b = 3; Box b2 = new Box(); b2.l = 6; b2.b = 2; System.out.println(b1.area() + " " + b2.area());` where area() returns l * b.
**Answer:** `12 12`
4 × 3 and 6 × 2.

**Q14.** Continuing Q13: `Box b3 = b1; b3.l = 10; System.out.println(b1.l + " " + b1.area());`
**Answer:** `10 30`
b3 and b1 refer to the same object.

**Q15.** Give the output: `Box b4 = new Box(); System.out.println(b4.l + " " + b4.area());`
**Answer:** `0 0`
int members default to 0.

**Q16.** Give the output of `System.out.println(b1 == b3);` and `System.out.println(b1 == b2);` for Q13–Q14.
**Answer:** `true` and `false`
== compares references, not contents.

**Q17.** Find the error: `fruit mango = fruit();`
**Answer:** The new operator is missing (compile error).
Write `fruit mango = new fruit();`

**Q18.** Find the error: `Student s; s.accept();`
**Answer:** s does not refer to any object (it is null), so the call fails at run time.
Create the object first: `Student s = new Student(); s.accept();`

**Q19.** The courier bill is computed as `bill = weight * 800;` for every weight. What type of error is this, and what is the correct bill for 12 kg?
**Answer:** A logical error — slabs are ignored.
4000 + 3500 + 1000 = ₹8500.

**Q20.** Give the bill for 20 GB at 15/GB (first 15 GB) and 13/GB (next 15 GB).
**Answer:** 290
15 × 15 + 5 × 13 = 225 + 65.

**Q21.** What is printed? `name = sc.next(); address = sc.nextLine(); System.out.println("[" + address + "]");` when the user types `Daniel` and presses Enter.
**Answer:** `[]`
nextLine() returns the empty rest of the line after "Daniel".

**Q22.** Give the hotel bill (with 18% GST) for 5 days at ₹1000/day for the first 3 days and ₹900/day for the next 4.
**Answer:** ₹5664
3000 + 1800 = 4800; GST 864; 4800 + 864 = 5664.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; a sample run follows each.*

### Section B programs (15 marks each)

**Q1.** Define a class LibraryFine with member variables name, title (String), late (int, days returned late) and fine (int). Methods: accept() to read the data; calculate() to compute the fine — first 5 days ₹2 per day, next 5 days ₹3 per day, beyond 10 days ₹5 per day; display() to print the details. Write main to create an object and call the methods.
**Answer:**
```java
import java.util.*;
class LibraryFine
{
    String name;        // borrower's name
    String title;       // book title
    int late;           // days returned late
    int fine;

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter borrower's name: ");
        name = sc.nextLine();
        System.out.print("Enter book title: ");
        title = sc.nextLine();
        System.out.print("Enter number of days late: ");
        late = sc.nextInt();
    }

    void calculate()
    {
        if (late <= 5)
            fine = late * 2;
        else if (late <= 10)
            fine = 5 * 2 + (late - 5) * 3;
        else
            fine = 5 * 2 + 5 * 3 + (late - 10) * 5;
    }

    void display()
    {
        System.out.println("Name  : " + name);
        System.out.println("Book  : " + title);
        System.out.println("Late  : " + late + " days");
        System.out.println("Fine  : Rs " + fine);
    }

    public static void main(String args[])
    {
        LibraryFine ob = new LibraryFine();
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```
Sample run (13 days: 10 + 15 + 15):
```
Enter borrower's name: Wanda Nongrum
Enter book title: The Glass Palace
Enter number of days late: 13
Name  : Wanda Nongrum
Book  : The Glass Palace
Late  : 13 days
Fine  : Rs 40
```

**Q2.** Define a class Employee with name and basic salary. Method compute() calculates DA = 30% of basic, HRA = 15% of basic, PF = 12% of basic, gross = basic + DA + HRA and net = gross − PF. Write accept(), compute(), display() and main.
**Answer:**
```java
import java.util.*;
class Employee
{
    String name;
    double basic, da, hra, pf, gross, net;

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter basic salary: ");
        basic = sc.nextDouble();
    }

    void compute()
    {
        da = basic * 30 / 100;          // dearness allowance
        hra = basic * 15 / 100;         // house rent allowance
        pf = basic * 12 / 100;          // provident fund (deduction)
        gross = basic + da + hra;
        net = gross - pf;
    }

    void display()
    {
        System.out.println("Name   : " + name);
        System.out.println("Basic  : " + basic);
        System.out.println("DA     : " + da);
        System.out.println("HRA    : " + hra);
        System.out.println("PF     : " + pf);
        System.out.println("Gross  : " + gross);
        System.out.println("Net    : " + net);
    }

    public static void main(String args[])
    {
        Employee e = new Employee();
        e.accept();
        e.compute();
        e.display();
    }
}
```
Sample run:
```
Enter name: Pynshai Dkhar
Enter basic salary: 25000
Name   : Pynshai Dkhar
Basic  : 25000.0
DA     : 7500.0
HRA    : 3750.0
PF     : 3000.0
Gross  : 36250.0
Net    : 33250.0
```

**Q3.** Define a class Rect with length and breadth, methods accept(), area(), perimeter() and display(). In main, create two objects, display both and print which rectangle has the larger area.
**Answer:**
```java
import java.util.*;
class Rect
{
    double length, breadth;

    void accept(Scanner sc)
    {
        System.out.print("Enter length and breadth: ");
        length = sc.nextDouble();
        breadth = sc.nextDouble();
    }

    double area()
    {
        return length * breadth;
    }

    double perimeter()
    {
        return 2 * (length + breadth);
    }

    void display()
    {
        System.out.println("Length " + length + ", breadth " + breadth
                           + ": area " + area() + ", perimeter " + perimeter());
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        Rect r1 = new Rect();           // two objects of the same class
        Rect r2 = new Rect();
        r1.accept(sc);
        r2.accept(sc);
        r1.display();
        r2.display();
        if (r1.area() > r2.area())
            System.out.println("The first rectangle is larger");
        else if (r2.area() > r1.area())
            System.out.println("The second rectangle is larger");
        else
            System.out.println("Both have the same area");
    }
}
```
Sample run:
```
Enter length and breadth: 6 4
Enter length and breadth: 5 5
Length 6.0, breadth 4.0: area 24.0, perimeter 20.0
Length 5.0, breadth 5.0: area 25.0, perimeter 20.0
The second rectangle is larger
```

**Q4.** Define a class Parking with vehicle number (String), type (char: C car, B bike), hours (int) and charge (int). For a car charge ₹40 for the first hour and ₹20 for each additional hour; for a bike ₹20 and ₹10. Write accept(), calculate(), display() and main.
**Answer:**
```java
import java.util.*;
class Parking
{
    String vno;         // vehicle number
    char kind;          // 'C' car, 'B' bike
    int hours;
    int charge;

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter vehicle number: ");
        vno = sc.nextLine();
        System.out.print("Enter type (C = car, B = bike): ");
        kind = sc.next().charAt(0);
        System.out.print("Enter hours parked: ");
        hours = sc.nextInt();
    }

    void calculate()
    {
        int first, extra;
        if (kind == 'C' || kind == 'c')
        {
            first = 40;
            extra = 20;
        }
        else
        {
            first = 20;
            extra = 10;
        }
        if (hours <= 1)
            charge = first;
        else
            charge = first + (hours - 1) * extra;
    }

    void display()
    {
        System.out.println("Vehicle : " + vno);
        System.out.println("Hours   : " + hours);
        System.out.println("Charge  : Rs " + charge);
    }

    public static void main(String args[])
    {
        Parking p = new Parking();
        p.accept();
        p.calculate();
        p.display();
    }
}
```
Sample run (car, 4 hours: 40 + 3 × 20):
```
Enter vehicle number: ML05 AB 1234
Enter type (C = car, B = bike): C
Enter hours parked: 4
Vehicle : ML05 AB 1234
Hours   : 4
Charge  : Rs 100
```

**Q5.** Define a class BMI with name, weight (kg), height (m), bmi and category. calculate() finds bmi = weight ÷ height² and the category: below 18.5 Underweight, below 25 Normal, below 30 Overweight, otherwise Obese. Write accept(), calculate(), display() (bmi to one decimal place) and main.
**Answer:**
```java
import java.util.*;
class BMI
{
    String name;
    double weight, height, bmi;     // kg, metres
    String category;

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter weight (kg) and height (m): ");
        weight = sc.nextDouble();
        height = sc.nextDouble();
    }

    void calculate()
    {
        bmi = weight / (height * height);
        if (bmi < 18.5)
            category = "Underweight";
        else if (bmi < 25)
            category = "Normal";
        else if (bmi < 30)
            category = "Overweight";
        else
            category = "Obese";
    }

    void display()
    {
        System.out.println("Name     : " + name);
        System.out.println("BMI      : " + Math.round(bmi * 10) / 10.0);
        System.out.println("Category : " + category);
    }

    public static void main(String args[])
    {
        BMI ob = new BMI();
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```
Sample run:
```
Enter name: Daphi Kharbuli
Enter weight (kg) and height (m): 58 1.62
Name     : Daphi Kharbuli
BMI      : 22.1
Category : Normal
```

**Q6.** Define a class Taxi with passenger name, distance km (int), night (char, 'Y' for a night ride) and fare (double). The fare is ₹100 flat for the first 5 km, ₹15 per km for the next 10 km and ₹12 per km beyond 15 km; a night ride costs 25% extra. Write accept(), calculate(), display() and main.
**Answer:**
```java
import java.util.*;
class Taxi
{
    String name;        // passenger's name
    int km;             // distance travelled
    char night;         // 'Y' for a night ride
    double fare;        // fare to be paid

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter passenger's name: ");
        name = sc.nextLine();
        System.out.print("Enter distance in km: ");
        km = sc.nextInt();
        System.out.print("Night ride (Y/N): ");
        night = sc.next().charAt(0);
    }

    void calculate()
    {
        if (km <= 5)
            fare = 100;
        else if (km <= 15)
            fare = 100 + (km - 5) * 15;
        else
            fare = 100 + 10 * 15 + (km - 15) * 12;
        if (night == 'Y' || night == 'y')
            fare = fare + fare * 25 / 100;
    }

    void display()
    {
        System.out.println("Passenger : " + name);
        System.out.println("Distance  : " + km + " km");
        System.out.println("Fare      : Rs " + fare);
    }

    public static void main(String args[])
    {
        Taxi t = new Taxi();
        t.accept();
        t.calculate();
        t.display();
    }
}
```
Sample run (22 km at night: 100 + 10 × 15 + 7 × 12 = 334; 334 + 25% = 417.5):
```
Enter passenger's name: Iaishah Marbaniang
Enter distance in km: 22
Night ride (Y/N): Y
Passenger : Iaishah Marbaniang
Distance  : 22 km
Fare      : Rs 417.5
```

---

## 12. Competency / Application Questions

**Q1. (Design a class)** A school canteen wants a class Order. List suitable member variables and methods.
**Model answer:** Variables: item name (String), quantity (int), price (double), amount (double). Methods: accept(), calculate() (amount = quantity × price, with a discount for large orders), display().

**Q2. (Spot the slab error)** A bill for 42 GB of cloud storage was computed as 42 × 11 = 462. What went wrong, and what is the correct bill?
**Model answer:** All 42 GB were charged at the cheapest slab rate. Correct: 15 × 15 + 15 × 13 + 12 × 11 = 552.

**Q3. (Two objects)** Write the statements to create two objects t1 and t2 of class StepTracker and call accept() for both.
**Model answer:** `StepTracker t1 = new StepTracker(); StepTracker t2 = new StepTracker(); t1.accept(); t2.accept();`

**Q4. (Choosing types)** For a RailwayTicket class, choose types for name, coach, mobile number and amount.
**Model answer:** String, String, long, int (or double).

**Q5. (Reference trap)** `Box a = new Box(); Box b = a; b.l = 7;` — does a.l change? Why?
**Model answer:** Yes — a and b refer to the same object; no new object was created.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** An object is called an instance of a class.
**R:** An object is created from the class blueprint.
**Answer:** (c)
**Explanation:** It is one case of the class.

**Q2.**
**A:** A class occupies memory for instance variables as soon as it is defined.
**R:** Each object has its own copy of instance variables.
**Answer:** (b)
**Explanation:** Memory is given when objects are created; R is true.

**Q3.**
**A:** A class is a user-defined data type.
**R:** Objects of a class can be declared like variables of a type.
**Answer:** (c)
**Explanation:** e.g. Student s;

**Q4.**
**A:** `b3 = b1;` creates a new copy of the object b1.
**R:** Class-type variables store references.
**Answer:** (b)
**Explanation:** Both names refer to the same object; R is true.

**Q5.**
**A:** int is a primitive data type.
**R:** Scanner belongs to java.util.
**Answer:** (d)
**Explanation:** Both true; unrelated.

**Q6.**
**A:** In slab billing for 250 units, the bill is 100 × 2 + 150 × 3.
**R:** Each slab is charged at its own rate.
**Answer:** (c)
**Explanation:** Slab by slab.

**Q7.**
**A:** A mobile number like 9436012345 can be stored in an int.
**R:** long has a larger range than int.
**Answer:** (b)
**Explanation:** It exceeds the int range; use long.

**Q8.**
**A:** Methods of an object are called with the dot operator.
**R:** The dot operator accesses members of an object.
**Answer:** (c)
**Explanation:** ob.accept().

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The cloud plan

> `CloudStorage c = new CloudStorage();` The user enters account number 1021 and 42 GB. Rates: first 15 GB ₹15/GB, next 15 GB ₹13/GB, above 30 GB ₹11/GB.

**(i)** Name the class and the object.
**Answer:** Class CloudStorage; object c.

**(ii)** Which operator created the object?
**Answer:** new.

**(iii)** What is the bill?
**Answer:** ₹552.

**(iv)** Write the statement that calls calculate().
**Answer:** `c.calculate();`

### Case 2 — The fitness band

> A StepTracker object records 13000 steps. Calories = steps × 0.04; distance = steps ÷ 1300.

**(i)** Calories burned?
**Answer:** 520.0.

**(ii)** Distance?
**Answer:** 10.0 km.

**(iii)** Data type of steps (sw)?
**Answer:** int.

**(iv)** Which method prints the results?
**Answer:** display().

### Case 3 — Classes and objects

> `Apparel BridalGown = new Apparel(34); Apparel Saree = new Apparel(40);`

**(i)** How many objects are created?
**Answer:** Two.

**(ii)** Name the class.
**Answer:** Apparel.

**(iii)** Do the two objects share their instance variables?
**Answer:** No — each has its own copy.

**(iv)** Is Apparel primitive or composite?
**Answer:** Composite (user-defined).

---

## 15. Revision Notes

### Chapter at a glance
- Object = state (member variables) + behaviour (member methods); message passing by method calls.
- Class = blueprint; abstraction for a set of objects; object factory; user-defined (composite) type.
- Object = instance of a class; `ClassName ob = new ClassName();`; members by the dot operator; own copy of variables; `b3 = b1` aliases.
- Class vs object: template vs instance; logical vs physical; one vs many.
- Primitive (8 built-in, single value, fixed size) vs composite (class, array, String; references; default null).
- Program: variables, accept (Scanner), calculate (slabs), display, main creating an object and calling methods.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| Multiplying the whole quantity by one slab rate | Charge each slab at its own rate and add. |
| Forgetting new | `fruit mango = new fruit();` |
| Calling methods without an object | `ob.calculate();` |
| next() then nextLine() for an address | Read with nextLine() first. |
| Storing a mobile number in int | Use long. |
| Renaming the question's variables | Use the names given in the question. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 5: Class as the Basis of all Computation**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** In `Game cricket = new Game();`:
(a) Game is the object (b) cricket is the class (c) Game is the class, cricket the object (d) both are objects

**2.** A class encapsulates:
(a) information and operation (b) data members and member methods (c) packages (d) comments

**3.** User-defined types among array, double, class, boolean:
(a) only array (b) array and class (c) only double (d) only boolean

**4.** Object mango of class fruit:
(a) fruit mango = fruit(); (b) fruit mango = new fruit(); (c) Mango fruit = new Mango(); (d) fruit mango = new mango();

**5.** Allocates memory for an object:
(a) dot (b) new (c) == (d) import

**6.** Default value of a class-type member:
(a) 0 (b) false (c) null (d) 1

**7.** Polygon and shapes picture — polygon is the:
(a) class (b) object (c) method (d) variable

**8.** Package of Character and Boolean:
(a) java.util (b) java.lang (c) java.io (d) java.awt

**9.** Statement I: An object is a logical entity. Statement II: A class is a template.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

**10.** Bill for 250 units at ₹2 (first 100) and ₹3 (next 200):
(a) ₹500 (b) ₹650 (c) ₹750 (d) ₹600

### Part I — Short answers (5 × 2 = 10)

**11.** Differentiate class and object. [2]

**12.** Classify: char, arrays, int, classes. [2]

**13.** Why is an object called an instance of a class? [2]

**14.** Write the statement to create object sifra of class Robot with three double values. [2]

**15.** Identify the variable and methods in class Cat: Name, meow(), eat(), play(). [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Define a class CloudStorage (acno, space, bill; accept, calculate with slabs 15/13/11 per GB, display, main). [10]

**17.** Define a class Hotel (name, mobno, days, bill; input, charge with slabs 1000/900/800 per day plus 18% GST, print, main). [10]

**18.** Define a class Student (name, age, mks, stream; accept, allocation per the 2023 criteria, print, main). [10]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | c | b | c | b | d | c | b | c |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | CloudStorage; c | new | ₹552 | c.calculate(); |
| 2 | 520.0 | 10.0 km | int | display() |
| 3 | Two | Apparel | No | Composite |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | c | b | b | b | b | c | a | b | d | b |

**Part I, Q11–15 (2 marks each)**

**11.** Blueprint (1); instance in memory (1).
**12.** Primitive, non-primitive, primitive, non-primitive (½ each).
**13.** Created from the class (1); one case with its own values (1).
**14.** `Robot sifra = new Robot(2.5, 3.0, 4.5);` (2).
**15.** Name (1); meow(), eat(), play() (1).

**Part II (10 marks each)**

**16.–18.** Class and variables (2), accept with Scanner (2), calculation (3), display (2), main with object and calls (1).
