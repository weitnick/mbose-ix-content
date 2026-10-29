# Constructors

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 7 |
| Title | Constructors |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 4. Constructors |
| Exam weightage | **Section A**: MCQs and 2-mark parts on **constructor types**, **overloading** and **outputs of two-constructor programs**. **Section B**: class programs with a **default constructor** (2019 Q4, 2020 Q4). |
| Syllabus scope | Definition, characteristics, types and use of constructors; default and parameterised constructors; constructor overloading; difference between a constructor and a method. |
| In short | How constructors set up new objects in Java, the default and parameterised kinds, and how they differ from ordinary methods. |

> **Note on the text:** CISCE prescribes no textbook for ICSE Computer Applications; this chapter follows the ICSE 2027 syllabus in its own words. Its questions are the CISCE papers of 2017–2026 and the 2024 and 2025 specimens, answered from CISCE's marking schemes and examiners' comments where published. **Every program was compiled and run (Java 21).**
>
> **Exam note:** A constructor has **exactly the class name** and **no return type, not even void**. A "default constructor to initialise the data members" sets **String members to "" and numbers to 0 or 0.0**, with the variables **declared at class level**, not inside the constructor (the commonest 2019 error). In output questions, find **which constructor each new calls**, then trace.

---

## 1. Complete Lesson

### What is a constructor?

A **constructor** is a special member method that has **the same name as its class** and **no return type**. It is **called automatically when an object is created** with new, and its job is to **initialise the instance variables** of that object.

```java
class Box
{
    int l, b;

    Box(int x, int y)       // constructor: class name, no return type
    {
        l = x;
        b = y;
    }
}
// Box r = new Box(6, 3);   creates the object AND runs the constructor
```

![Fig. 7.1 What happens when an object is created: the constructor runs once, automatically](figures/ca_ch07_fig01_object_creation.png)

When `new Box(6, 3)` runs: memory is set aside for the object, every instance variable gets its **default value**, the **constructor body** runs (l = 6, b = 3), and the **reference** of the new object is returned and stored in r.

### Why constructors are needed

- An object gets **sensible starting values at the moment it is created** — there is no chance of forgetting to call an initialising method.
- Values can be supplied **while creating the object**: `new Account("Rida", 30451267L, 5000)`.
- Code is shorter: one statement both creates and initialises the object.

### Characteristics of a constructor

1. It has **the same name as the class** — exactly, because Java is case sensitive (for class Yellow the constructor is Yellow, not yellow — ICSE 2024 Q1(xv)).
2. It has **no return type, not even void**.
3. It is **called automatically** when an object is created; it **cannot be called like an ordinary method** (`ob.Box()` is not allowed).
4. It runs **once for each object**.
5. It is usually declared **public** (or with no access specifier) so that objects can be created from other classes.
6. It **can be overloaded** — a class may have several constructors with different parameter lists.
7. If a class has **no constructor at all**, Java supplies a **default constructor** with no parameters.

### Default values of instance variables

Before the constructor body runs, every instance variable already holds its default value. A constructor that does not set a variable leaves it at this value.

| Type | Default value |
|---|---|
| byte, short, int, long | 0 |
| float, double | 0.0 |
| char | the null character `'\u0000'` |
| boolean | false |
| String and other objects | null |

Local variables (declared inside a method) get **no** default value — they must be given a value before use.

### Types of constructors

**1. Default constructor.** If a class has no constructor, the **compiler supplies one with no parameters**; it leaves every instance variable at its default value (0, 0.0, false, null). A constructor "which has the same name as the class and initialises the instance variables with their default values" is the default constructor (ICSE 2026 Improvement Q1(vii)).

**2. Non-parameterised constructor.** A constructor **written by the programmer with no parameters**. It gives fixed starting values. In ICSE questions it is also called a "default constructor" — e.g. `ShowRoom()` "default constructor to initialise data members" (2019 Q4):

```java
ShowRoom()
{
    name = "";
    mobno = 0;
    cost = 0.0;
    dis = 0.0;
    amount = 0.0;
}
```

**3. Parameterised constructor.** A constructor **with parameters**; the values passed in new become the object's starting values:

```java
perform(int x, String y)
{
    m = x;
    name = y;
}
// perform ob1 = new perform(95, "Xavier");
```

| Default (non-parameterised) constructor | Parameterised constructor |
|---|---|
| Takes no parameters | Takes one or more parameters |
| Gives every object the same starting values | Each object can start with different values |
| `Box()` called by `new Box()` | `Box(int x, int y)` called by `new Box(6, 3)` |

**Important:** once you write **any** constructor, Java no longer supplies the default one. If a class has only `E8(int x)`, then `new E8()` gives the error *constructor E8 in class E8 cannot be applied to given types*.

### Constructor overloading

A class can have **more than one constructor**, all with the class name but with **different parameter lists** (number, type or order of parameters). This is **constructor overloading**, a form of **polymorphism** (ICSE 2024 specimen Q1(xiv); 2024 Q2(ix)). The constructors must differ in their **parameters** (ICSE 2026 Q1(xx)).

![Fig. 7.2 Constructor overloading: one class name, several parameter lists](figures/ca_ch07_fig02_constructor_overloading.png)

```java
class Box
{
    int l, b;
    String tag;

    Box()                  { l = 1; b = 1; tag = "unit"; }
    Box(int s)             { l = s; b = s; tag = "square"; }
    Box(int l, int b)      { this.l = l; this.b = b; tag = "rectangle"; }

    int area() { return l * b; }
}
```

`new Box()` runs the first constructor (area 1), `new Box(4)` the second (area 16) and `new Box(6, 3)` the third (area 18). Java chooses the constructor exactly as it chooses an overloaded method — by the arguments. Two constructors with the **same** parameter list give *constructor E10(int) is already defined*.

### The keyword this

Inside a constructor or method, **this** refers to the **current object** — the one being created or used. It is needed when a parameter has the **same name** as an instance variable:

```java
Box(int l, int b)
{
    this.l = l;      // instance variable l = parameter l
    this.b = b;
}
```

Without this, `l = l;` would assign the parameter to itself and leave the instance variable unchanged. For example, `Shadow(int x) { x = x; }` leaves the member x at **0**.

### Constructor versus method

| Constructor | Method |
|---|---|
| Same name as the class | Any valid name |
| No return type, not even void | Must have a return type (void if nothing is returned) |
| Called automatically when an object is created | Called explicitly through an object or class name |
| Runs once per object | Can be called any number of times |
| Initialises the object | Performs any task |
| If none is written, Java supplies a default one | Never supplied automatically |

**A trap:** `void Trap() { v = 99; }` inside class Trap is **not** a constructor — the word void makes it an ordinary method that happens to share the class name. It does not run on `new Trap()`; it runs only when called as `tr.Trap()`. And `int E9() { a = 4; }` is likewise a method, which fails with *missing return statement*.

### Constructors in "define a class" programs

Section B programs often ask for a constructor along with accept, calculate and display methods:

```java
import java.util.*;
class CabService
{
    String car_type;        // instance variables: declared here, at class level
    double km, bill;

    CabService()            // default constructor
    {
        car_type = "";
        km = 0.0;
        bill = 0.0;
    }
    void accept()    { ... }   // Scanner input
    void calculate() { ... }   // slab logic
    void display()   { ... }

    public static void main(String args[])
    {
        CabService ob = new CabService();   // the constructor runs here
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```

What the examiners of 2019 noted for ShowRoom (Q4):
- Variables declared **inside the constructor** become local and are lost — declare them at class level.
- "Default constructor" means initialising with **default values**, not with sample values.
- Use the **variable and method names given in the question**, and the **Scanner class** for input when asked.

### Constructors that do work

A constructor may do more than copy values. In the Fraction class, `Fraction(6, 8)` reduces the fraction while creating it, so every Fraction object is always in lowest terms (3/4). A constructor can also call other methods of the class (here gcd()) and update a **static** counter — `TokenDesk(String n)` gives each new object the next token number, so the counter shows how many objects have been created.

### Summary of the chapter

- **Constructor** — same name as the class, no return type, called automatically by new, initialises the object.
- **Characteristics** — runs once per object; cannot be called like a method; can be overloaded; supplied by Java only if none is written.
- **Types** — default (compiler-supplied), non-parameterised (user-written, fixed values), parameterised (values passed in new).
- **Default values** — 0, 0.0, `'\u0000'`, false, null.
- **Overloading** — several constructors with different parameter lists; polymorphism.
- **this** — the current object; resolves a clash between parameter and member names.
- **Constructor vs method** — name, return type, how and how often each is called.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Define a constructor and state its characteristics.
2. Distinguish default, non-parameterised and parameterised constructors.
3. State the default values of instance variables of each type.
4. Write overloaded constructors and predict which one new calls.
5. Use this to separate instance variables from parameters.
6. Distinguish a constructor from a method, and write class programs with constructors.

---

## 3. Detailed Section Explanations

### Section 1 — Birth of an object
new does four things: allocate memory, set defaults, run the constructor, return the reference. The constructor is the only code that runs at birth.

### Section 2 — Same name, no return type
These two rules identify a constructor. Add void and it becomes an ordinary method.

### Section 3 — One class, several ways to start
Overloaded constructors let objects start differently; the arguments in new choose the constructor.

### Section 4 — this resolves the clash
When a parameter hides an instance variable, `this.name = name;` sets the object's own variable.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Constructor | A member method with the class name and no return type that initialises an object. |
| Default constructor | The no-parameter constructor Java supplies when a class has none. |
| Non-parameterised constructor | A user-written constructor with no parameters. |
| Parameterised constructor | A constructor that receives values as parameters. |
| Constructor overloading | Several constructors in one class with different parameter lists. |
| Initialisation | Giving variables their starting values. |
| Default value | The value an instance variable has before it is set (0, 0.0, false, null). |
| this | A reference to the current object. |
| Instance variable | A variable declared in a class, outside methods; each object has its own copy. |
| Local variable | A variable declared inside a method or constructor; it exists only there. |
| Instance | An object of a class. |
| new | The operator that creates an object and calls its constructor. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| Constructor's name | the class name, exactly (class Yellow → Yellow) |
| Constructor's return type | none, not even void |
| Constructors in overloading differ in | parameters |
| Constructor overloading follows | polymorphism |
| Initialises instance variables with default values | default constructor |
| An instance of a class is called | an object |
| Method with the same name as the class | constructor |
| Two characteristics (2018 scheme) | same name as the class; executed when an object is created |
| `new report()` then `new report(4, 5)` with a×b printed | 150 and 20 |
| `new temp()` (a = 10) and `new temp(30)` | 10 and 30 |
| Constructor types in calculate() and calculate(int, double) | default (non-parameterised) and parameterised |

### 5.2 Memory aids

- **"Same Name, No Type, Auto Call"** — the three marks of a constructor.
- **"Write one, lose the free one"** — once any constructor is written, Java's default constructor is gone.
- **"this = me"** — the object talking about itself.

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- A constructor can call another constructor of the same class with `this(...)` as its first statement (constructor chaining).
- A **copy constructor** takes an object of the same class and copies its values: `Box(Box other) { l = other.l; b = other.b; }`.
- Java has no destructors; unused objects are removed by the garbage collector.

---

## 6. Person Profiles

### 6.1 Bjarne Stroustrup (born 1950)
A Danish computer scientist who created C++ at Bell Labs, starting in 1979 as "C with Classes". C++ introduced constructors as special functions carrying the class's name, the rule Java later adopted.

### 6.2 James Gosling (born 1955)
A Canadian computer scientist who led the team at Sun Microsystems that created Java, released in 1995. Java kept C++'s constructors but added the automatic default constructor and garbage collection in place of destructors.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Born ready** — an object should be usable the moment it is created.
- **Many ways to begin** — overloaded constructors offer several starting points.
- **Self-reference** — this lets an object refer to its own data.

### 7.2 Real-life connections
- **Bank accounts:** opening an account (the constructor) needs a name, number and opening deposit.
- **Meghalaya:** a token machine at a district office gives each new visitor the next number — exactly what a constructor with a static counter does.
- **Mobile phones:** a new phone starts with factory settings (default constructor) or with settings restored from a backup (parameterised constructor).

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section A** (40 marks) asks MCQs and 2-mark parts on constructors — names, types, overloading and output of short programs. **Section B** (60 marks, any four of six programs) has asked "define a class" programs with a **default constructor** (2019 Q4, 2020 Q4), worth 15 marks.

### 8.1 Graded exercises — solutions

#### Exercise 7A — Concepts

**Q1.** Identify the constructor: `class Pen { int ink; Pen() { ink = 100; } void write() { ink--; } }`
**Answer:** `Pen()` — it has the class name and no return type; write() is a method.

**Q2.** Write a parameterised constructor for `class Car { String model; int year; }`.
**Answer:** `Car(String m, int y) { model = m; year = y; }`

**Q3.** A class has only `Lamp(int watts)`. Will `Lamp l = new Lamp();` compile? Why?
**Answer:** No — once a constructor is written, Java does not supply the default one.

**Q4.** What values do the members of `class Plain { int n; double d; boolean f; String s; }` have after `new Plain()`?
**Answer:** 0, 0.0, false and null.

#### Exercise 7B — Tracing

**Q5.** Give the output: `Box p = new Box(); Box q = new Box(4); System.out.println(p.area() + q.area());` with the Box class of Section 1.
**Answer:** 17 (1 + 16).

**Q6.** Give the output: `Shadow sh = new Shadow(7); System.out.println(sh.x);` where `Shadow(int x) { x = x; }`.
**Answer:** 0 — the parameter is assigned to itself; the member keeps its default value.

**Q7.** In class Trap, `int v = 5;` and `void Trap() { v = 99; }`. Give the output of `Trap tr = new Trap(); System.out.println(tr.v); tr.Trap(); System.out.println(tr.v);`
**Answer:** 5 then 99 — Trap() is a method because of void; it runs only when called.

**Q8.** TokenDesk gives tokens from 101. After three objects are created, what is TokenDesk.next?
**Answer:** 104.
### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(xx) (1 mark) | In constructor overloading all constructors should have the same name as of the class but with a different set of _____________. (a) Access specifiers (b) Classes (c) Return type (d) Parameters |
| ICSE 2026 Improvement, Q1(vii) (1 mark) | A method which has the same name of the class and initialises the instance variables with their default values is: (a) Parameterised Constructor (b) Overloaded method (c) Default constructor (d) Non-parameterised constructor |
| ICSE 2025, Q2(v) (2 marks) | Consider and give the output of the following program: `class report { int a, b; report() { a = 10; b = 15; } report(int x, int y) { a = x; b = y; } void print() { System.out.println(a * b); } static void main() { report r = new report(); r.print(); report p = new report(4, 5); p.print(); } }` |
| ICSE 2025 Improvement, Q2(x) (2 marks) | `class perform { int m; String name; perform(int x, String y) { m = x; name = y; } void print() { System.out.print(name + " " + m); } public static void main() { perform ob1 = new perform(95, "Xavier"); ob1.print(); } }` (a) Give the output of the code given above. (b) Name the type of the constructor used. |
| ICSE 2025 specimen, Q2(ix) (2 marks) | Consider the following program segment and answer the question below: `class calculate { int a; double b; calculate() { a = 0; b = 0.0; } calculate(int x, double y) { a = x; b = y; } void sum() { System.out.println(a * b); } }` Name the type of constructors used in the above program segment. |
| ICSE 2024, Q1(xv) (1 mark) | If the name of the class is "Yellow", what can be the possible name for its constructors? (a) yellow (b) YELLOW (c) Yell (d) Yellow |
| ICSE 2024, Q2(ix) (2 marks) | Consider the given program and answer the questions given below: `class temp { int a; temp() { a = 10; } temp(int z) { a = z; } void print() { System.out.println(a); } void main() { temp t = new temp(); temp x = new temp(30); t.print(); x.print(); } }` (a) What concept of OOPs is depicted in the above program with two constructors? (b) What is the output of the method main()? |
| ICSE 2024 specimen, Q1(xiv) (1 mark) | Constructor overloading follows which principle of Object Oriented programming? (a) Inheritance (b) Polymorphism (c) Abstraction (d) Encapsulation |
| ICSE 2023, Q2(ix) (2 marks) | Name the following: (a) What is an instance of the class called? (b) The method which has same name as that of the class name. |
| ICSE 2020, Q2(c) (2 marks) | What is constructor overloading? |
| ICSE 2020, Q4 (15 marks) | A private Cab service company provides service within the city at the following rates — AC car: up to 5 km ₹150, beyond 5 km ₹10 per km; non-AC car: up to 5 km ₹120, beyond 5 km ₹8 per km. Design a class CabService with the following description: Member variables / data members: String car_type — to store the type of car (AC or NON AC); double km — to store the kilometres travelled; double bill — to calculate and store the bill amount. Member methods: CabService() — default constructor to initialise data members: String data members to "" and double data members to 0.0; void accept() — to accept car_type and km (using Scanner class only); void calculate() — to calculate the bill as per the rules given above; void display() — to display the bill in the format CAR TYPE: , KILOMETER TRAVELLED: , TOTAL BILL: . Create an object of the class in the main method and invoke the member methods. |
| ICSE 2019, Q4 (15 marks) | Design a class name ShowRoom with the following description: Instance variables / data members: String name — to store the name of the customer; long mobno — to store the mobile number of the customer; double cost — to store the cost of the items purchased; double dis — to store the discount amount; double amount — to store the amount to be paid after discount. Member methods: ShowRoom() — default constructor to initialise data members; void input() — to input customer name, mobile number, cost; void calculate() — to calculate discount on the cost of purchased items, based on the following criteria: cost less than or equal to ₹10000, 5%; more than ₹10000 and up to ₹20000, 10%; more than ₹20000 and up to ₹35000, 15%; more than ₹35000, 20%; void display() — to display customer name, mobile number, amount to be paid after discount. Write a main method to create an object of the class and call the above member methods. |
| ICSE 2018, Q3(d) (2 marks) | Write two characteristics of a constructor. |
| ICSE 2017, Q3(e) (2 marks) | Differentiate between constructor and function. |

**Solutions**

**2026 Q1(xx).** **(d) Parameters** — overloaded constructors share the class name and differ in their parameter lists. *(Worked answer.)*

**2026 Improvement Q1(vii).** **(c) Default constructor** — it leaves every instance variable at its default value (0, 0.0, false, null). *(Worked answer.)*

**2025 Q2(v).** `new report()` runs the non-parameterised constructor (a = 10, b = 15); `new report(4, 5)` runs the parameterised one (a = 4, b = 5). Output:
```
150
20
```
(Checked with a standard `public static void main(String args[])`; BlueJ also runs the `static void main()` written in the paper.)

**2025 Improvement Q2(x).** (a) The output is `Xavier 95`. (b) A **parameterised constructor** — it receives 95 and "Xavier" as parameters. *(Worked answer.)*

**2025 specimen Q2(ix).** `calculate()` is a **default (non-parameterised) constructor** and `calculate(int x, double y)` is a **parameterised constructor**; together they show constructor overloading.

**2024 Q1(xv).** **(d) Yellow** — a constructor's name must match the class name exactly. The examiners noted that some candidates wrote "yellow", with a capital Y that could not be told from a small one — write the capital clearly.

**2024 Q2(ix).** (a) **Constructor overloading** (polymorphism) — the scheme accepts polymorphism, overloading, overloading constructors or multiple constructors. (b) The output is
```
10
30
```
`t` is made by temp() and `x` by temp(30).

**2024 specimen Q1(xiv).** **(b) Polymorphism** *(Worked answer.)*

**2023 Q2(ix).** (a) **Object**. (b) **Constructor**. The examiners noted that most candidates wrote "method" for (a) and "static method" for (b).

**2020 Q2(c).** Constructor overloading means defining **more than one constructor in a class**, all with the class name but with **different parameter lists** (number, type or order of parameters). The constructor that runs is chosen by the arguments given with new — e.g. `Box()` and `Box(int l, int b)`. *(Worked answer.)*

**2020 Q4.** Beyond 5 km, the first 5 km cost the flat rate and every further km is charged at the per-km rate:
```java
import java.util.*;
class CabService
{
    String car_type;    // AC or NON AC
    double km;          // kilometres travelled
    double bill;        // bill amount

    CabService()
    {
        car_type = "";
        km = 0.0;
        bill = 0.0;
    }

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter car type (AC or NON AC): ");
        car_type = sc.nextLine();
        System.out.print("Enter kilometres travelled: ");
        km = sc.nextDouble();
    }

    void calculate()
    {
        if (car_type.equalsIgnoreCase("AC"))
        {
            if (km <= 5)
                bill = 150;
            else
                bill = 150 + (km - 5) * 10;
        }
        else
        {
            if (km <= 5)
                bill = 120;
            else
                bill = 120 + (km - 5) * 8;
        }
    }

    void display()
    {
        System.out.println("CAR TYPE: " + car_type);
        System.out.println("KILOMETER TRAVELLED: " + km);
        System.out.println("TOTAL BILL: " + bill);
    }

    public static void main(String args[])
    {
        CabService ob = new CabService();
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```
Sample runs (AC for 12 km: 150 + 7 × 10; NON AC for 3 km: flat ₹120):
```
Enter car type (AC or NON AC): AC
Enter kilometres travelled: 12
CAR TYPE: AC
KILOMETER TRAVELLED: 12.0
TOTAL BILL: 220.0
```
```
Enter car type (AC or NON AC): NON AC
Enter kilometres travelled: 3
CAR TYPE: NON AC
KILOMETER TRAVELLED: 3.0
TOTAL BILL: 120.0
```
car_type is read with nextLine() because "NON AC" contains a space. *(Worked answer.)*

**2019 Q4.** As in the marking scheme, except that the scheme reads the name with next(), which stops at the first space; nextLine() reads a full name:
```java
import java.util.*;
class ShowRoom
{
    String name;        // customer's name
    long mobno;         // mobile number
    double cost;        // cost of items purchased
    double dis;         // discount amount
    double amount;      // amount to be paid

    ShowRoom()
    {
        name = "";
        mobno = 0;
        cost = 0.0;
        dis = 0.0;
        amount = 0.0;
    }

    void input()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter customer name: ");
        name = sc.nextLine();
        System.out.print("Enter mobile number: ");
        mobno = sc.nextLong();
        System.out.print("Enter cost: ");
        cost = sc.nextDouble();
    }

    void calculate()
    {
        if (cost <= 10000)
            dis = cost * 5 / 100;
        else if (cost <= 20000)
            dis = cost * 10 / 100;
        else if (cost <= 35000)
            dis = cost * 15 / 100;
        else
            dis = cost * 20 / 100;
        amount = cost - dis;
    }

    void display()
    {
        System.out.println("Name             : " + name);
        System.out.println("Mobile number    : " + mobno);
        System.out.println("Amount to be paid: " + amount);
    }

    public static void main(String args[])
    {
        ShowRoom ob = new ShowRoom();
        ob.input();
        ob.calculate();
        ob.display();
    }
}
```
Sample run (₹25000 is in the 15% slab: discount 3750):
```
Enter customer name: Larisa Syiem
Enter mobile number: 9436012345
Enter cost: 25000
Name             : Larisa Syiem
Mobile number    : 9436012345
Amount to be paid: 21250.0
```
The examiners noted these errors: variables declared and initialised inside the constructor instead of at class level, the default constructor given sample values instead of default values, different method or variable names, and data read in main and passed as arguments instead of read in input().

**2018 Q3(d).** Any two, from the scheme: (i) A constructor has the same name as its class. (ii) A constructor is executed automatically when an object is created. Also: it has no return type, not even void; it can be overloaded.

**2017 Q3(e).** Any one or two differences:
- A constructor has the same name as the class; a function (method) can have any name.
- A constructor has no return type; a function has a return type (void if it returns nothing).
- A constructor is called automatically when an object is created; a function is called explicitly.
- A constructor runs once per object; a function can be called any number of times.

*(Worked answer.)*

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Write a non-parameterised constructor for `class Hotel { String name; int days; double bill; }` that gives default values.
**Answer:** `Hotel() { name = ""; days = 0; bill = 0.0; }`

**Q2.** (2 marks) Give the output: `class P { int v; P() { v = 2; } P(int x) { v = x * x; } }` with `P a = new P(); P b = new P(5); System.out.println(a.v + b.v);`
**Answer:** `27` (2 + 25).

**Q3.** (2 marks) Why does `class Q { int a; int Q() { a = 4; } }` fail to compile, and what is Q() here?
**Answer:** Q() has a return type (int), so it is a method, not a constructor; it fails with "missing return statement" because it returns nothing.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| 2 marks | Output of a class with a default and a parameterised constructor | 8.2, Section 10 |
| MCQ / 2 marks | Characteristics; name of a constructor; types; overloading = polymorphism | 8.2, 5.1 |
| 2 marks | Constructor vs method; what is constructor overloading | 8.2, Section 1 |
| 15 marks | Class with a default constructor + accept, calculate, display, main | 8.2, Section 11 |

---
## 9. MCQs with Explanations

### What a constructor is (Q1–Q14)

**Q1.** A constructor is a member method that
- (a) initialises an object when it is created
- (b) deletes an object
- (c) prints the class name
- (d) imports a package

**Answer:** (a) initialises an object when it is created
**Explanation:** It sets the starting values.

**Q2.** The name of a constructor is
- (a) the same as the class name
- (b) any valid identifier
- (c) always main
- (d) always init

**Answer:** (a) the same as the class name
**Explanation:** Exactly the class name.

**Q3.** The return type of a constructor is
- (a) void
- (b) int
- (c) none, not even void
- (d) the class name

**Answer:** (c) none, not even void
**Explanation:** Adding a return type makes it a method.

**Q4.** For a class named Yellow, the correct constructor header is
- (a) Yellow()
- (b) void Yellow()
- (c) Yellow int()
- (d) new Yellow()

**Answer:** (a) Yellow()
**Explanation:** Exact class name (case sensitive), no return type.

**Q5.** A constructor is called
- (a) automatically when an object is created
- (b) only by the import statement
- (c) when the program ends
- (d) only from another constructor's return statement

**Answer:** (a) automatically when an object is created
**Explanation:** new runs it.

**Q6.** For each object created, the constructor runs
- (a) once
- (b) twice
- (c) as many times as methods are called
- (d) never

**Answer:** (a) once
**Explanation:** Once, at creation.

**Q7.** An instance of a class is called
- (a) a method
- (b) an object
- (c) a constructor
- (d) a package

**Answer:** (b) an object
**Explanation:** ICSE 2023 Q2(ix)(a).

**Q8.** The method which has the same name as that of the class is
- (a) a static method
- (b) a library method
- (c) a constructor
- (d) the main method

**Answer:** (c) a constructor
**Explanation:** Many candidates wrote "static method" in 2023.

**Q9.** Which statement about constructors is FALSE?
- (a) They have the class name.
- (b) They can be overloaded.
- (c) They must return a value.
- (d) They are called by new.

**Answer:** (c) They must return a value.
**Explanation:** They have no return type.

**Q10.** The main use of a constructor is to
- (a) declare packages
- (b) take input from the keyboard only
- (c) end the program
- (d) initialise instance variables

**Answer:** (d) initialise instance variables
**Explanation:** Starting values for the object.

**Q11.** In Box r = new Box(6, 3);, the constructor called is
- (a) Box()
- (b) main()
- (c) area()
- (d) Box(int x, int y)

**Answer:** (d) Box(int x, int y)
**Explanation:** Two int arguments.

**Q12.** A constructor is usually declared
- (a) void
- (b) private, so that objects can be made anywhere
- (c) static
- (d) public

**Answer:** (d) public
**Explanation:** So objects can be created from other classes.

**Q13.** A constructor cannot be called
- (a) by new
- (b) once per object
- (c) when an object is made
- (d) like an ordinary method, as ob.Box()

**Answer:** (d) like an ordinary method, as ob.Box()
**Explanation:** It runs only through new.

**Q14.** Two characteristics of a constructor are
- (a) any name; must return int
- (b) returns void; called by import
- (c) static; called once per program
- (d) same name as the class; executed when an object is created

**Answer:** (d) same name as the class; executed when an object is created
**Explanation:** As in the 2018 marking scheme.

### Types of constructors and default values (Q15–Q30)

**Q15.** A method which has the same name as the class and initialises the instance variables with their default values is
- (a) a parameterised constructor
- (b) an overloaded method
- (c) a default constructor
- (d) a non-parameterised constructor

**Answer:** (c) a default constructor
**Explanation:** ICSE 2026 Improvement Q1(vii).

**Q16.** Java supplies a default constructor
- (a) only when the class has no constructor
- (b) always, in every class
- (c) only for static classes
- (d) never

**Answer:** (a) only when the class has no constructor
**Explanation:** Writing any constructor removes it.

**Q17.** A constructor that receives values as parameters is
- (a) a default constructor
- (b) a static method
- (c) a parameterised constructor
- (d) a library method

**Answer:** (c) a parameterised constructor
**Explanation:** Values come from new.

**Q18.** In perform(int x, String y) { m = x; name = y; }, the constructor is
- (a) non-parameterised
- (b) not a constructor
- (c) a copy of main
- (d) parameterised

**Answer:** (d) parameterised
**Explanation:** It takes x and y.

**Q19.** In class calculate, calculate() and calculate(int x, double y) are
- (a) both parameterised constructors
- (b) a constructor and a destructor
- (c) two methods
- (d) a default (non-parameterised) and a parameterised constructor

**Answer:** (d) a default (non-parameterised) and a parameterised constructor
**Explanation:** ICSE 2025 specimen Q2(ix).

**Q20.** The default value of an int instance variable is
- (a) 0
- (b) 1
- (c) null
- (d) garbage

**Answer:** (a) 0
**Explanation:** Numeric members start at 0.

**Q21.** The default value of a double instance variable is
- (a) 0
- (b) null
- (c) 0.0
- (d) 1.0

**Answer:** (c) 0.0
**Explanation:** Printed as 0.0.

**Q22.** The default value of a boolean instance variable is
- (a) true
- (b) false
- (c) 0
- (d) null

**Answer:** (b) false
**Explanation:** boolean starts false.

**Q23.** The default value of a String instance variable is
- (a) an empty string
- (b) a space
- (c) null
- (d) 0

**Answer:** (c) null
**Explanation:** Objects default to null.

**Q24.** The default value of a char instance variable is
- (a) ' '
- (b) 'a'
- (c) '0'
- (d) `'\u0000'`

**Answer:** (d) `'\u0000'`
**Explanation:** The null character.

**Q25.** For class D7 with String s, double d and boolean f and no constructor, System.out.println("Name: " + d.s + " " + d.d + " " + d.f); for a new object prints
- (a) Name: null 0.0 false
- (b) Name:  0 true
- (c) an error
- (d) Name: 0 0 0

**Answer:** (a) Name: null 0.0 false
**Explanation:** The default constructor leaves default values.

**Q26.** A class has only E8(int x). The statement E8 ob = new E8(); gives
- (a) an object with a = 0
- (b) the error: constructor E8 in class E8 cannot be applied to given types
- (c) a runtime error only
- (d) an object with a = 1

**Answer:** (b) the error: constructor E8 in class E8 cannot be applied to given types
**Explanation:** No no-argument constructor exists.

**Q27.** When asked for a "default constructor to initialise data members", String and double members should be set to
- (a) "" and 0.0
- (b) "none" and 1.0
- (c) any sample values
- (d) null and -1

**Answer:** (a) "" and 0.0
**Explanation:** Default values, as in 2020 Q4.

**Q28.** A local variable declared inside a constructor
- (a) can be used in every method of the class
- (b) becomes an instance variable
- (c) exists only inside that constructor
- (d) gets the default value 0

**Answer:** (c) exists only inside that constructor
**Explanation:** Declare members at class level.

**Q29.** A non-parameterised constructor is
- (a) a method with void
- (b) always supplied by Java
- (c) a constructor with one parameter
- (d) written by the programmer with no parameters

**Answer:** (d) written by the programmer with no parameters
**Explanation:** e.g. ShowRoom().

**Q30.** `class E7 { int a = 3; E7() { a = a + 4; } }` — the value of new E7().a is
- (a) 3
- (b) 4
- (c) 7
- (d) 0

**Answer:** (c) 7
**Explanation:** The initial value 3 is set before the constructor body runs.

### Constructor overloading and this (Q31–Q48)

**Q31.** Having more than one constructor in a class with different parameter lists is
- (a) constructor overloading
- (b) inheritance
- (c) encapsulation
- (d) abstraction

**Answer:** (a) constructor overloading
**Explanation:** Same name, different lists.

**Q32.** Constructor overloading follows the OOP principle of
- (a) inheritance
- (b) abstraction
- (c) polymorphism
- (d) encapsulation

**Answer:** (c) polymorphism
**Explanation:** One name, many forms.

**Q33.** In constructor overloading all constructors have the class name but a different set of
- (a) access specifiers
- (b) classes
- (c) return types
- (d) parameters

**Answer:** (d) parameters
**Explanation:** ICSE 2026 Q1(xx).

**Q34.** Overloaded constructors may differ in the
- (a) access specifier only
- (b) return type only
- (c) class name
- (d) number, type or order of parameters

**Answer:** (d) number, type or order of parameters
**Explanation:** Exactly as for methods.

**Q35.** Two constructors E10(int x) and E10(int y) in one class give
- (a) constructor overloading
- (b) the error: constructor E10(int) is already defined
- (c) a runtime error
- (d) no error

**Answer:** (b) the error: constructor E10(int) is already defined
**Explanation:** Parameter names do not count.

**Q36.** Box has Box(), Box(int s) and Box(int l, int b). The call new Box(4) runs
- (a) Box()
- (b) no constructor
- (c) Box(int l, int b)
- (d) Box(int s)

**Answer:** (d) Box(int s)
**Explanation:** One int argument.

**Q37.** With the same Box class, new Box() then area() gives 1, new Box(4) gives 16. new Box(6, 3).area() gives
- (a) 9
- (b) 18
- (c) 36
- (d) 1

**Answer:** (b) 18
**Explanation:** 6 × 3.

**Q38.** H7 has H7(), H7(int v) and H7(double d). The call new H7('A') runs
- (a) H7()
- (b) H7(int v)
- (c) H7(double d)
- (d) none; it is an error

**Answer:** (b) H7(int v)
**Explanation:** char widens to int first; v becomes 65.

**Q39.** The keyword this refers to
- (a) the current object
- (b) the class's package
- (c) the main method
- (d) the previous object

**Answer:** (a) the current object
**Explanation:** The object being created or used.

**Q40.** this is needed in Box(int l, int b) because
- (a) this returns a value
- (b) constructors must use this
- (c) this creates the object
- (d) the parameters have the same names as the instance variables

**Answer:** (d) the parameters have the same names as the instance variables
**Explanation:** this.l is the member, l the parameter.

**Q41.** `class B7 { int n; B7(int n) { this.n = n * 2; } }` — new B7(4).n is
- (a) 4
- (b) 8
- (c) 0
- (d) 16

**Answer:** (b) 8
**Explanation:** this.n is the member.

**Q42.** `class C7 { int n; C7(int n) { n = n * 2; } }` — new C7(4).n is
- (a) 4
- (b) 8
- (c) 0
- (d) 16

**Answer:** (c) 0
**Explanation:** Only the parameter changes; the member keeps 0.

**Q43.** Shadow(int x) { x = x; } is called with new Shadow(7). The member x is
- (a) 7
- (b) 0
- (c) 14
- (d) an error

**Answer:** (b) 0
**Explanation:** The parameter is assigned to itself.

**Q44.** In class temp with temp() { a = 10; } and temp(int z) { a = z; }, the concept shown is
- (a) inheritance
- (b) constructor overloading
- (c) encapsulation
- (d) data hiding

**Answer:** (b) constructor overloading
**Explanation:** ICSE 2024 Q2(ix)(a).

**Q45.** Which pair can be overloaded constructors of class Lamp?
- (a) void Lamp() and Lamp()
- (b) Lamp(int a) and Lamp(int b)
- (c) Lamp() and Lamp(int w)
- (d) Lamp() and lamp()

**Answer:** (c) Lamp() and Lamp(int w)
**Explanation:** Different parameter lists.

**Q46.** A class has three constructors. Each new statement calls
- (a) all three
- (b) the first one always
- (c) none of them
- (d) exactly one of them

**Answer:** (d) exactly one of them
**Explanation:** Chosen by the arguments.

**Q47.** `A7() { x = 5; }` and `A7(int k) { x = k + 1; }` — the value of new A7().x + new A7(5).x is
- (a) 10
- (b) 11
- (c) 12
- (d) 6

**Answer:** (b) 11
**Explanation:** 5 + 6.

**Q48.** Constructor overloading lets
- (a) objects be created with different starting values
- (b) a class have two names
- (c) a constructor return a value
- (d) methods run without objects

**Answer:** (a) objects be created with different starting values
**Explanation:** Several ways to begin.

### Constructor versus method; errors (Q49–Q62)

**Q49.** Which is TRUE of a constructor but NOT of a method?
- (a) It can use instance variables.
- (b) It can take parameters.
- (c) It is written inside a class.
- (d) It has no return type.

**Answer:** (d) It has no return type.
**Explanation:** Methods need a return type.

**Q50.** A method, unlike a constructor,
- (a) can be called any number of times
- (b) runs once per object automatically
- (c) must have the class name
- (d) has no return type

**Answer:** (a) can be called any number of times
**Explanation:** Methods are called explicitly.

**Q51.** In class Trap, void Trap() { v = 99; } is
- (a) a constructor
- (b) an ordinary method
- (c) a compile error
- (d) a static block

**Answer:** (b) an ordinary method
**Explanation:** void makes it a method.

**Q52.** With int v = 5; and void Trap() { v = 99; }, after Trap tr = new Trap(); the value of tr.v is
- (a) 0
- (b) 99
- (c) 5
- (d) 104

**Answer:** (c) 5
**Explanation:** Trap() did not run on new.

**Q53.** `int E9() { a = 4; }` in class E9 gives
- (a) a constructor that sets a to 4
- (b) the error: unreachable statement
- (c) no error
- (d) the error: missing return statement

**Answer:** (d) the error: missing return statement
**Explanation:** With int it is a method that returns nothing.

**Q54.** Which is a correct constructor of class Pen?
- (a) Pen() { ink = 100; }
- (b) void Pen() { ink = 100; }
- (c) int Pen() { return 100; }
- (d) Pen { ink = 100; }

**Answer:** (a) Pen() { ink = 100; }
**Explanation:** Exact name, no return type.

**Q55.** A function, unlike a constructor, is
- (a) called explicitly
- (b) named after the class
- (c) called by new
- (d) without a return type

**Answer:** (a) called explicitly
**Explanation:** ICSE 2017 Q3(e).

**Q56.** Which of these is supplied by Java automatically when none is written?
- (a) a default constructor
- (b) an accept() method
- (c) a display() method
- (d) a main method

**Answer:** (a) a default constructor
**Explanation:** Methods are never supplied.

**Q57.** The statement Box b = new Box(2, 3); performs
- (a) object creation and initialisation
- (b) only declaration
- (c) only a method call
- (d) only memory release

**Answer:** (a) object creation and initialisation
**Explanation:** new creates; the constructor initialises.

**Q58.** Which is NOT a step of creating an object with new?
- (a) memory is allocated
- (b) default values are set
- (c) the constructor runs
- (d) the class is compiled again

**Answer:** (d) the class is compiled again
**Explanation:** Compiling happens before running.

**Q59.** A constructor can
- (a) have a name different from the class
- (b) be declared with void
- (c) call other methods of the class
- (d) return an int

**Answer:** (c) call other methods of the class
**Explanation:** e.g. Fraction calls gcd().

**Q60.** The 2019 examiners' most common error in ShowRoom was
- (a) declaring the instance variables inside the constructor
- (b) using the class name
- (c) writing a main method
- (d) using Scanner

**Answer:** (a) declaring the instance variables inside the constructor
**Explanation:** They became local variables.

**Q61.** A copy of an object's reference, Box b2 = b1;,
- (a) calls Box(int, int)
- (b) calls the default constructor
- (c) does not call any constructor
- (d) creates a new object

**Answer:** (c) does not call any constructor
**Explanation:** No new, no constructor.

**Q62.** Which keyword creates an object and calls its constructor?
- (a) this
- (b) new
- (c) void
- (d) static

**Answer:** (b) new
**Explanation:** new Box().

### Tracing programs with constructors (Q63–Q76)

**Q63.** In class report, report() sets a = 10, b = 15 and print() prints a × b. The output of new report() then print() is
- (a) 25
- (b) 150
- (c) 20
- (d) 0

**Answer:** (b) 150
**Explanation:** 10 × 15.

**Q64.** With the same class, report p = new report(4, 5); p.print(); prints
- (a) 9
- (b) 20
- (c) 150
- (d) 45

**Answer:** (b) 20
**Explanation:** 4 × 5.

**Q65.** In class temp, t = new temp() and x = new temp(30); t.print(); x.print(); prints
- (a) 10 and 10
- (b) 30 and 10
- (c) 10 and 30
- (d) 0 and 30

**Answer:** (c) 10 and 30
**Explanation:** Each object has its own a.

**Q66.** perform ob1 = new perform(95, "Xavier"); ob1.print(); with print() printing name + " " + m gives
- (a) Xavier95
- (b) 95 Xavier
- (c) Xavier 95
- (d) null 0

**Answer:** (c) Xavier 95
**Explanation:** name, a space, then m.

**Q67.** F7() { made++; } with static int made = 0. After F7 p = new F7(); F7 q = p; F7 r = new F7(); the value of F7.made is
- (a) 1
- (b) 2
- (c) 3
- (d) 0

**Answer:** (b) 2
**Explanation:** q = p creates no object.

**Q68.** G7(2, 3) sets l and b. After G7 g1 = new G7(2, 3); G7 g2 = g1; g2.l = 5; the value of g1.area() is
- (a) 6
- (b) 25
- (c) 10
- (d) 15

**Answer:** (d) 15
**Explanation:** g1 and g2 refer to one object.

**Q69.** TokenDesk starts next at 101 and each constructor call takes next and adds 1. After three objects, TokenDesk.next is
- (a) 101
- (b) 103
- (c) 104
- (d) 3

**Answer:** (c) 104
**Explanation:** 101, 102, 103 were issued.

**Q70.** Fraction(int n, int d) reduces by the gcd. new Fraction(6, 8) displays
- (a) 6/8
- (b) 3/4
- (c) 2/4
- (d) 4/3

**Answer:** (b) 3/4
**Explanation:** gcd(6, 8) = 2.

**Q71.** H7(double d) { v = (int) d * 10; } — new H7(2.9).v is
- (a) 29
- (b) 20
- (c) 30
- (d) 2

**Answer:** (b) 20
**Explanation:** (int) 2.9 is 2, then × 10.

**Q72.** In CabService, an AC car for 12 km (₹150 up to 5 km, then ₹10 per km) is billed
- (a) ₹120
- (b) ₹220
- (c) ₹270
- (d) ₹150

**Answer:** (b) ₹220
**Explanation:** 150 + 7 × 10.

**Q73.** In ShowRoom, a cost of ₹25000 (15% slab) gives an amount to be paid of
- (a) ₹21250
- (b) ₹22500
- (c) ₹20000
- (d) ₹3750

**Answer:** (a) ₹21250
**Explanation:** 25000 − 3750.

**Q74.** In CabService, a NON AC car for 3 km is billed
- (a) ₹24
- (b) ₹150
- (c) ₹120
- (d) ₹96

**Answer:** (c) ₹120
**Explanation:** Flat rate up to 5 km.

**Q75.** Why is car_type read with nextLine() in CabService?
- (a) car_type is a char
- (b) next() cannot read letters
- (c) nextLine() is faster
- (d) "NON AC" contains a space

**Answer:** (d) "NON AC" contains a space
**Explanation:** next() would read only "NON".

**Q76.** P() { v = 2; } and P(int x) { v = x * x; }. The value of new P().v + new P(5).v is
- (a) 7
- (b) 27
- (c) 12
- (d) 25

**Answer:** (b) 27
**Explanation:** 2 + 25.
## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** Define a constructor. State two of its characteristics.
**Answer:** A constructor is a member method with the class name that initialises an object when it is created.
It has no return type, not even void, and it is called automatically by new.

**Q2.** Why are constructors needed?
**Answer:** They give an object sensible starting values at the moment it is created.
They also let values be supplied while creating the object, e.g. `new Account("Rida", 30451267L, 5000)`.

**Q3.** Distinguish between a default and a parameterised constructor.
**Answer:** A default (non-parameterised) constructor takes no parameters and gives every object the same starting values.
A parameterised constructor takes parameters, so each object can start with different values.

**Q4.** What is constructor overloading? Give an example.
**Answer:** Defining more than one constructor in a class, all with the class name but with different parameter lists.
e.g. `Box()` and `Box(int l, int b)`.

**Q5.** State two differences between a constructor and a method.
**Answer:** A constructor has the class name and no return type; a method has any name and a return type.
A constructor runs automatically once per object; a method is called explicitly, any number of times.

**Q6.** When does Java supply a default constructor?
**Answer:** Only when the class has no constructor at all.
It takes no parameters and leaves every instance variable at its default value.

**Q7.** What is the use of the keyword this in a constructor?
**Answer:** this refers to the current object.
It separates an instance variable from a parameter of the same name: `this.l = l;`.

**Q8.** State the default values of int, double, boolean and String instance variables.
**Answer:** int 0, double 0.0.
boolean false, String null.

**Q9.** What happens if void is written before a constructor's name?
**Answer:** It becomes an ordinary method with the class's name.
It no longer runs on new; it runs only when called explicitly.

**Q10.** Why should data members not be declared inside the constructor?
**Answer:** Variables declared inside the constructor are local to it and vanish after it ends.
Other methods cannot use them; declare them at class level.

**Q11.** Name the types of constructors, with an example of each.
**Answer:** Default/non-parameterised: `ShowRoom()`.
Parameterised: `perform(int x, String y)`.

**Q12.** Write a parameterised constructor for `class Student { String name; int roll; }`.
**Answer:** `Student(String n, int r) { name = n; roll = r; }`

### Output and error questions (2 marks each)

**Q13.** `class report { int a, b; report() { a = 10; b = 15; } report(int x, int y) { a = x; b = y; } void print() { System.out.println(a * b); } }` Give the output of `new report().print(); new report(4, 5).print();`
**Answer:** `150` then `20`
The first object uses report(), the second report(4, 5).

**Q14.** `class temp { int a; temp() { a = 10; } temp(int z) { a = z; } void print() { System.out.println(a); } }` Give the output of `temp t = new temp(); temp x = new temp(30); t.print(); x.print();`
**Answer:** `10` then `30`
Each object has its own a.

**Q15.** Give the values of `new B7(4).n` where `B7(int n) { this.n = n * 2; }` and of `new C7(4).n` where `C7(int n) { n = n * 2; }`.
**Answer:** 8 and 0.
In C7 only the parameter changes; the member keeps its default 0.

**Q16.** `class E7 { int a = 3; E7() { a = a + 4; } }` Give the value of `new E7().a`.
**Answer:** 7
The initial value 3 is set first, then the constructor adds 4.

**Q17.** `class F7 { static int made = 0; F7() { made++; } }` Give the value of F7.made after `F7 p = new F7(); F7 q = p; F7 r = new F7();`.
**Answer:** 2
`q = p` copies a reference; it creates no object.

**Q18.** `G7(int l, int b) { this.l = l; this.b = b; }` and `area()` returns l * b. Give the output of `G7 g1 = new G7(2, 3); G7 g2 = g1; g2.l = 5; System.out.println(g1.area());`
**Answer:** `15`
g1 and g2 refer to the same object.

**Q19.** H7 has `H7() { v = 1; }`, `H7(int v) { this.v = v; }` and `H7(double d) { v = (int) d * 10; }`. Give the values of `new H7().v`, `new H7(7).v`, `new H7(2.9).v` and `new H7('A').v`.
**Answer:** 1, 7, 20 and 65.
'A' widens to the int 65; (int) 2.9 is 2.

**Q20.** Find the error: class E8 has only `E8(int x) { a = x; }`, and main has `E8 ob = new E8();`.
**Answer:** "constructor E8 in class E8 cannot be applied to given types" — no constructor without parameters exists.
Write `new E8(5)` or add `E8() { a = 0; }`.

**Q21.** Find the error: `class E10 { int a; E10(int x) { a = x; } E10(int y) { a = y * 2; } }`
**Answer:** "constructor E10(int) is already defined" — both have the parameter list (int).
Change one list, e.g. `E10(int y, int z)`.

**Q22.** `class Trap { int v = 5; void Trap() { v = 99; } }` Give the output of `Trap tr = new Trap(); System.out.println(tr.v); tr.Trap(); System.out.println(tr.v);`
**Answer:** `5` then `99`
void makes Trap() a method; it runs only when called.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; a sample run or the output follows each.*

### Section B programs (15 marks each)

**Q1.** Define a class CinemaTicket with name (String), type (char: G Gold, S Silver, B Bronze), seats (int) and amount (double). Methods: CinemaTicket() — default constructor; accept() — input the details; calculate() — Gold ₹250, Silver ₹180, Bronze ₹120 per seat, with a 10% discount for more than 5 seats; display(). Write main.
**Answer:**
```java
import java.util.*;
class CinemaTicket
{
    String name;        // customer's name
    char type;          // G = Gold, S = Silver, B = Bronze
    int seats;          // number of seats
    double amount;      // amount to be paid

    CinemaTicket()
    {
        name = "";
        type = ' ';
        seats = 0;
        amount = 0.0;
    }

    void accept()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter class (G/S/B): ");
        type = sc.next().charAt(0);
        System.out.print("Enter number of seats: ");
        seats = sc.nextInt();
    }

    void calculate()
    {
        int rate;
        switch (type)
        {
            case 'G': rate = 250; break;
            case 'S': rate = 180; break;
            default:  rate = 120;
        }
        amount = seats * rate;
        if (seats > 5)
            amount = amount - amount * 10 / 100;
    }

    void display()
    {
        System.out.println("Name   : " + name);
        System.out.println("Seats  : " + seats + " (" + type + ")");
        System.out.println("Amount : " + amount);
    }

    public static void main(String args[])
    {
        CinemaTicket ob = new CinemaTicket();
        ob.accept();
        ob.calculate();
        ob.display();
    }
}
```
Sample run (6 Gold seats: 1500 − 150):
```
Enter name: Wanphrang Lyngdoh
Enter class (G/S/B): G
Enter number of seats: 6
Name   : Wanphrang Lyngdoh
Seats  : 6 (G)
Amount : 1350.0
```

**Q2.** Define a class Triangle2 with sides a, b, c and three overloaded constructors: Triangle2(double s) for an equilateral triangle, Triangle2(double s, double base) for an isosceles triangle, Triangle2(double x, double y, double z) for a scalene triangle. Methods perimeter(), area() (Heron's formula) and display(). Create one object of each kind in main.
**Answer:**
```java
class Triangle2
{
    double a, b, c;     // the three sides
    String kind;

    Triangle2(double s)
    {
        a = s;
        b = s;
        c = s;
        kind = "Equilateral";
    }

    Triangle2(double s, double base)
    {
        a = s;
        b = s;
        c = base;
        kind = "Isosceles";
    }

    Triangle2(double x, double y, double z)
    {
        a = x;
        b = y;
        c = z;
        kind = "Scalene";
    }

    double perimeter()
    {
        return a + b + c;
    }

    double area()
    {
        double s = perimeter() / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }

    void display()
    {
        System.out.println(kind + ": perimeter " + perimeter() + ", area " + Math.round(area() * 100) / 100.0);
    }

    public static void main(String args[])
    {
        Triangle2 t1 = new Triangle2(6);
        Triangle2 t2 = new Triangle2(5, 6);
        Triangle2 t3 = new Triangle2(3, 4, 5);
        t1.display();
        t2.display();
        t3.display();
    }
}
```
Output:
```
Equilateral: perimeter 18.0, area 15.59
Isosceles: perimeter 16.0, area 12.0
Scalene: perimeter 12.0, area 6.0
```

**Q3.** Define a class Account with holder (String), accNo (long) and balance (double). A parameterised constructor sets all three. deposit(double amt) adds to the balance; withdraw(double amt) subtracts only if the balance is enough, otherwise prints a message; display(). In main open an account with ₹5000, deposit ₹2500, try to withdraw ₹9000, then withdraw ₹3000.
**Answer:**
```java
class Account
{
    String holder;
    long accNo;
    double balance;

    Account(String h, long n, double opening)
    {
        holder = h;
        accNo = n;
        balance = opening;
    }

    void deposit(double amt)
    {
        balance = balance + amt;
        System.out.println("Deposited " + amt + ", balance " + balance);
    }

    void withdraw(double amt)
    {
        if (amt <= balance)
        {
            balance = balance - amt;
            System.out.println("Withdrawn " + amt + ", balance " + balance);
        }
        else
            System.out.println("Insufficient balance for " + amt);
    }

    void display()
    {
        System.out.println(holder + " (A/c " + accNo + "): balance " + balance);
    }

    public static void main(String args[])
    {
        Account ac = new Account("Rida Kharshiing", 30451267L, 5000);
        ac.deposit(2500);
        ac.withdraw(9000);
        ac.withdraw(3000);
        ac.display();
    }
}
```
Output:
```
Deposited 2500.0, balance 7500.0
Insufficient balance for 9000.0
Withdrawn 3000.0, balance 4500.0
Rida Kharshiing (A/c 30451267): balance 4500.0
```

**Q4.** Define a class Fraction with num and den. Fraction() makes 0/1; Fraction(int n, int d) stores the fraction in lowest terms, using a method gcd(). add(Fraction f) returns a new Fraction equal to the sum. Display 6/8, 1/6, the zero fraction and 6/8 + 1/6.
**Answer:**
```java
class Fraction
{
    int num, den;

    Fraction()
    {
        num = 0;
        den = 1;
    }

    Fraction(int n, int d)
    {
        int g = gcd(Math.abs(n), Math.abs(d));
        num = n / g;
        den = d / g;
    }

    int gcd(int x, int y)
    {
        while (y != 0)
        {
            int r = x % y;
            x = y;
            y = r;
        }
        return x;
    }

    Fraction add(Fraction f)
    {
        return new Fraction(num * f.den + f.num * den, den * f.den);
    }

    void display()
    {
        System.out.println(num + "/" + den);
    }

    public static void main(String args[])
    {
        Fraction a = new Fraction(6, 8);
        Fraction b = new Fraction(1, 6);
        Fraction zero = new Fraction();
        a.display();
        b.display();
        zero.display();
        Fraction s = a.add(b);
        s.display();
    }
}
```
Output (3/4 + 1/6 = 9/12 + 2/12 = 11/12):
```
3/4
1/6
0/1
11/12
```

**Q5.** Define a class Scholar with name and three marks. Scholar() sets the name to "Not entered" and the marks to 0; Scholar(String n, int a, int b, int c) sets them. average() returns the average; grade() returns A (80 and above), B (60–79), C (40–59) or D (below 40); display(). Create two students with the parameterised constructor and one with the default.
**Answer:**
```java
class Scholar
{
    String name;
    int m1, m2, m3;

    Scholar()
    {
        name = "Not entered";
        m1 = 0;
        m2 = 0;
        m3 = 0;
    }

    Scholar(String n, int a, int b, int c)
    {
        name = n;
        m1 = a;
        m2 = b;
        m3 = c;
    }

    double average()
    {
        return (m1 + m2 + m3) / 3.0;
    }

    char grade()
    {
        double avg = average();
        if (avg >= 80)
            return 'A';
        else if (avg >= 60)
            return 'B';
        else if (avg >= 40)
            return 'C';
        else
            return 'D';
    }

    void display()
    {
        System.out.println(name + ": average " + Math.round(average() * 10) / 10.0 + ", grade " + grade());
    }

    public static void main(String args[])
    {
        Scholar s1 = new Scholar("Iaishah", 86, 78, 91);
        Scholar s2 = new Scholar("Kitbor", 55, 62, 48);
        Scholar s3 = new Scholar();
        s1.display();
        s2.display();
        s3.display();
    }
}
```
Output:
```
Iaishah: average 85.0, grade A
Kitbor: average 55.0, grade C
Not entered: average 0.0, grade D
```

**Q6.** Define a class TokenDesk in which a static variable next starts at 101. The constructor TokenDesk(String n) stores the visitor's name and gives the object the next token number, then increases next. show() prints the token and name. Create three objects and print the next token to be issued.
**Answer:**
```java
class TokenDesk
{
    static int next = 101;      // next token number, shared by all objects
    int token;
    String name;

    TokenDesk(String n)
    {
        name = n;
        token = next;
        next++;
    }

    void show()
    {
        System.out.println("Token " + token + " : " + name);
    }

    public static void main(String args[])
    {
        TokenDesk q1 = new TokenDesk("Banteilang");
        TokenDesk q2 = new TokenDesk("Phidawan");
        TokenDesk q3 = new TokenDesk("Shanbor");
        q1.show();
        q2.show();
        q3.show();
        System.out.println("Next token to be issued: " + TokenDesk.next);
    }
}
```
Output:
```
Token 101 : Banteilang
Token 102 : Phidawan
Token 103 : Shanbor
Next token to be issued: 104
```

---

## 12. Competency / Application Questions

**Q1. (Choose the constructors)** A Rectangle class should be created either as a unit square, as a square of side s, or with length and breadth. Write the three constructor headers.
**Model answer:** `Rectangle()`, `Rectangle(double s)`, `Rectangle(double l, double b)`.

**Q2. (Spot the error)** A student writes `void Hotel() { name = ""; days = 0; }` as the default constructor. What goes wrong?
**Model answer:** With void it is an ordinary method, so it never runs on new; remove void.

**Q3. (Default values)** A class has no constructor and members int qty, double price, String item. What does display() print for a new object?
**Model answer:** qty 0, price 0.0, item null.

**Q4. (Lost the free one)** After adding `Book(String t)` to class Book, the line `Book b = new Book();` stops compiling. Why, and give two fixes.
**Model answer:** Writing a constructor removes Java's default one. Pass a title, or add `Book() { title = ""; }`.

**Q5. (Counting objects)** How can a class report how many objects have been created?
**Model answer:** Keep a static counter and increase it in every constructor.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** A constructor can be declared with the return type void.
**R:** A constructor has no return type.
**Answer:** (b)
**Explanation:** With void it becomes a method.

**Q2.**
**A:** If a class has only a parameterised constructor, `new X()` does not compile.
**R:** Java supplies a default constructor only when no constructor is written.
**Answer:** (c)
**Explanation:** The free constructor is gone.

**Q3.**
**A:** Constructor overloading is an example of polymorphism.
**R:** Overloaded constructors share one name.
**Answer:** (c)
**Explanation:** One name, many forms.

**Q4.**
**A:** A constructor runs once for each object.
**R:** Constructors can be overloaded.
**Answer:** (d)
**Explanation:** Both true; unrelated.

**Q5.**
**A:** In `Box(int l, int b) { this.l = l; }`, this.l is the instance variable.
**R:** this refers to the current object.
**Answer:** (c)
**Explanation:** this.l belongs to the object.

**Q6.**
**A:** A String instance variable is "" by default.
**R:** Instance variables of object types default to null.
**Answer:** (b)
**Explanation:** The default is null.

**Q7.**
**A:** A constructor can call other methods of its class.
**R:** A constructor must return the object it creates.
**Answer:** (a)
**Explanation:** Constructors return nothing; new gives the reference.

**Q8.**
**A:** `Box b2 = b1;` calls no constructor.
**R:** No new object is created.
**Answer:** (c)
**Explanation:** Only a reference is copied.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The cab company

> CabService has a default constructor; AC cars cost ₹150 up to 5 km and ₹10 per km beyond.

**(i)** What values does the constructor give car_type, km and bill?
**Answer:** "", 0.0 and 0.0.

**(ii)** What is the bill for an AC car for 8 km?
**Answer:** ₹180 (150 + 3 × 10).

**(iii)** Why is car_type read with nextLine()?
**Answer:** "NON AC" contains a space.

**(iv)** When does the constructor run?
**Answer:** At `new CabService()`.

### Case 2 — Two constructors

> `temp() { a = 10; }` and `temp(int z) { a = z; }`; main creates `new temp()` and `new temp(30)`.

**(i)** Which concept is shown?
**Answer:** Constructor overloading.

**(ii)** What do the two print() calls show?
**Answer:** 10 and 30.

**(iii)** Which constructor does new temp(30) call?
**Answer:** temp(int z).

**(iv)** What type of constructor is temp()?
**Answer:** Non-parameterised (default).

### Case 3 — Fractions in lowest terms

> `Fraction(int n, int d)` divides n and d by their gcd; `Fraction()` makes 0/1.

**(i)** What does new Fraction(10, 4) display?
**Answer:** 5/2.

**(ii)** What does new Fraction() display?
**Answer:** 0/1.

**(iii)** Which method does the constructor call?
**Answer:** gcd().

**(iv)** Why reduce inside the constructor?
**Answer:** Every object is then always in lowest terms.

---

## 15. Revision Notes

### Chapter at a glance
- Constructor: class name, no return type, runs automatically once per object, initialises instance variables.
- Default constructor: supplied by Java only if none is written; default values 0, 0.0, false, null.
- Non-parameterised (user-written) and parameterised constructors; overloading = several parameter lists (polymorphism).
- this = the current object; `this.x = x;` when names clash.
- Constructor vs method: name, return type, automatic vs explicit, once vs many times.
- In class programs: declare members at class level; default constructor sets "" and 0/0.0.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| Writing void before the constructor | Constructors have no return type. |
| Class Yellow, constructor yellow() | The name must match exactly. |
| Declaring members inside the constructor | Declare them at class level. |
| `x = x;` with a same-named parameter | Write `this.x = x;`. |
| `new X()` when only X(int) exists | Add X() or pass an argument. |
| Giving sample values in a "default constructor" | Use "" and 0 / 0.0. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 7: Constructors**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** If the class is named "Yellow", its constructor can be named:
(a) yellow (b) YELLOW (c) Yell (d) Yellow

**2.** The return type of a constructor is:
(a) void (b) int (c) none (d) the class name

**3.** Constructor overloading follows:
(a) inheritance (b) polymorphism (c) abstraction (d) encapsulation

**4.** The default value of a boolean instance variable:
(a) false (b) true (c) 0 (d) null

**5.** The method which has the same name as the class:
(a) static method (b) main (c) constructor (d) library method

**6.** The keyword that creates an object and calls its constructor:
(a) new (b) this (c) void (d) static

**7.** Java supplies a default constructor:
(a) always (b) never (c) only for static classes (d) only when no constructor is written

**8.** An instance of a class is called:
(a) a method (b) an object (c) a package (d) a constructor

**9.** For `C7(int n) { n = n * 2; }`, the value of new C7(4).n:
(a) 4 (b) 8 (c) 0 (d) 16

**10.** Statement I: A constructor runs once per object. Statement II: A constructor can be called like a method, ob.C().
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

### Part I — Short answers (5 × 2 = 10)

**11.** State two differences between a constructor and a method. [2]

**12.** Give the output: report() sets a = 10, b = 15; report(int x, int y) sets a = x, b = y; print() prints a × b; main runs `new report().print(); new report(4, 5).print();` [2]

**13.** Name the types of constructors in `calculate()` and `calculate(int x, double y)`. [2]

**14.** Write a default constructor for `class Hotel { String name; int days; double bill; }`. [2]

**15.** What is constructor overloading? [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Define the class CabService of ICSE 2020 Q4 (default constructor, accept, calculate, display, main). [10]

**17.** Define the class ShowRoom of ICSE 2019 Q4 (default constructor, input, calculate with discount slabs, display, main). [10]

**18.** Define a class Triangle2 with three overloaded constructors (equilateral, isosceles, scalene), and methods perimeter() and area(). [10]

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Ans | b | c | c | d | c | b | a | c |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | "", 0.0, 0.0 | ₹180 | Space in "NON AC" | At new CabService() |
| 2 | Constructor overloading | 10 and 30 | temp(int z) | Non-parameterised |
| 3 | 5/2 | 0/1 | gcd() | Always lowest terms |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | d | c | b | a | c | a | d | b | c | c |

**Part I, Q11–15 (2 marks each)**

**11.** Name and return type (1); automatic once vs explicit any number of times (1).
**12.** `150` (1) and `20` (1).
**13.** Default / non-parameterised (1) and parameterised (1).
**14.** `Hotel() { name = ""; days = 0; bill = 0.0; }` (2).
**15.** More than one constructor (1) with different parameter lists (1).

**Part II (10 marks each)**

**16.–18.** Class and member variables (2), constructor(s) (2), input or setting values (2), logic (2), display and main (2).
