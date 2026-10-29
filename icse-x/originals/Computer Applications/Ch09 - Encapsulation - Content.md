# Encapsulation

| Field | Value |
|---|---|
| Board | ICSE (Council for the Indian School Certificate Examinations) |
| Class | X |
| Subject | Computer Applications |
| Chapter | 9 |
| Title | Encapsulation |
| Textbook source | CISCE prescribes no textbook for Computer Applications; written to the ICSE 2027 syllabus, Class X — 6. Encapsulation |
| Exam weightage | **Section A**: MCQs and 2-mark parts on **access specifiers** (which is least accessible, which is not one, real-life examples), **private versus public**, and **static versus instance** members. Every Section B class program uses member, local and argument variables. |
| Syllabus scope | Access specifiers and their scope and visibility: private, protected and public; visibility rules; scope of variables — class variables, instance variables, argument variables, local variables. |
| In short | How access specifiers like private and public protect a class's data, and where different kinds of variables can be used in a program. |

> **Note on the text:** CISCE prescribes no textbook for ICSE Computer Applications; this chapter follows the ICSE 2027 syllabus in its own words. Its questions are the CISCE papers of 2017–2026 and the 2024 and 2025 specimens, answered from CISCE's marking schemes and examiners' comments where published. **Every program and error message was checked with Java 21.**
>
> **Exam note:** Know the order of access, **private (least) → default → protected → public (most)**, and that **"package" is not an access specifier**. **static** makes a class variable, shared by all objects; a **static method cannot use instance variables directly**. A variable is visible only inside the braces where it is declared.

---

## 1. Complete Lesson

### What is encapsulation?

**Encapsulation** is the wrapping up of **data (member variables) and the methods that work on that data into a single unit — the class**. It is one of the four principles of object-oriented programming, with abstraction, inheritance and polymorphism.

Encapsulation usually goes with **data hiding**: the member variables are declared **private**, so that code outside the class cannot read or change them directly. Other classes use the object only through its **public methods**.

![Fig. 9.1 Encapsulation: private data can be reached only through the class's public methods](figures/ca_ch09_fig01_encapsulation.png)

```java
class SavingsAccount
{
    private double balance;                 // hidden data

    double getBalance()                     // public way to read it
    {
        return balance;
    }

    void deposit(double amt)                // public way to change it, with a check
    {
        if (amt > 0)
            balance = balance + amt;
        else
            System.out.println("Deposit must be positive");
    }
}
// In another class:  ac.deposit(1500);   allowed
//                    ac.balance = 0;     error: balance has private access in SavingsAccount
```

**Why encapsulate?**
- **Protection** — data cannot be set to wrong values (a negative balance, marks of 130), because every change passes through a method that checks it.
- **Control** — the class decides what may be read and what may be changed.
- **Flexibility** — the inside of the class can change (for example, storing temperature in Celsius only) without changing the code that uses it.
- **Easier maintenance** — errors in the data can only come from the class's own methods.

### Access specifiers

An **access specifier** (access modifier) is a keyword written before a member to control **who can use it**. Java has three access-specifier keywords — **private**, **protected** and **public** — and a fourth level, **default (package) access**, given when no specifier is written.

| Access | Keyword | Visible in |
|---|---|---|
| Private | private | only its own class |
| Default (package) | none — no keyword is written | all classes in the same package |
| Protected | protected | the same package, and subclasses in other packages |
| Public | public | every class, everywhere |

Points examined:
- **"package" is not an access specifier** (ICSE 2026 Q1(iv)). Default access has no keyword; the word package is used only to declare a package. Writing `package int a;` gives *illegal start of type*.
- **private gives the least accessibility** (ICSE 2024 Q1(iv)); public gives the most.
- A member accessible **only within its own class** is **private** (ICSE 2025 Improvement Q1(ix)).
- **public members can be accessed from any other class; private members only within the class that declares them** (ICSE 2018 Q1(d)).

### Visibility rules

| Can it be used from … | private | default | protected | public |
|---|---|---|---|---|
| the same class | Yes | Yes | Yes | Yes |
| another class in the same package | No | Yes | Yes | Yes |
| a subclass in another package | No | No | Yes | Yes |
| any other class in another package | No | No | No | Yes |

Order of accessibility: **private < default < protected < public**.

**Real-life examples:**
- A **post office** serves everyone — **public** (ICSE 2025 Q1(x)).
- Your own **diary or ATM PIN** — **private**: only you use it.
- A **school notice board** read by students of that school only — **default (package)**: open to the "family" of classes in the same package.
- A **family recipe** shared with the family and passed on to children who move away — **protected**: the package plus subclasses.

The examiners of 2025 noted that a few candidates chose protected for the post office.

### Getters and setters

A class with private data provides **accessor (getter)** methods to read values and **mutator (setter)** methods to change them:

```java
class Marks
{
    private int marks;

    void setMarks(int m)              // setter: changes the value after checking it
    {
        if (m >= 0 && m <= 100)
            marks = m;
        else
            System.out.println("Invalid marks: " + m);
    }

    int getMarks()                    // getter: returns the value
    {
        return marks;
    }
}
// m.setMarks(85); m.setMarks(130); System.out.println(m.getMarks());
// prints "Invalid marks: 130", then 85
```

Getters are **pure** (they change nothing); setters are **impure** (they change the object's state) — see Chapter 6. A class can also have **private methods**, such as `valid(int m)` in StudentRecord, that are helpers for its own use only.

### Scope of variables

The **scope** of a variable is the part of the program in which it can be used. Its **lifetime** is how long it exists while the program runs. The syllabus names four kinds:

![Fig. 9.2 Scope of variables: each kind is visible only inside its own region](figures/ca_ch09_fig02_scope.png)

| Kind | Declared | Copies | Default value | Lifetime |
|---|---|---|---|---|
| **Class variable** | in the class, with **static** | one, shared by all objects | yes (0, 0.0, false, null) | while the program runs |
| **Instance variable** | in the class, without static | one per object | yes (0, 0.0, false, null) | while its object exists |
| **Argument variable** (parameter) | in the method or constructor header | one per call | none — receives the argument | while the method runs |
| **Local variable** | inside a method or a block | one per call | **none — must be assigned before use** | until the end of its block |

```java
class LibraryBook
{
    static int issuedCount = 0;        // class variable
    private String title;              // instance variable
    private boolean issued;            // instance variable

    void returnBook(int daysLate)      // daysLate: argument variable
    {
        int fine = 0;                  // local variable
        if (daysLate > 0)
            fine = daysLate * 2;
        issued = false;
        issuedCount--;
        System.out.println(title + " returned; fine Rs " + fine);
    }
}
```

The keyword that **makes a variable a class variable is static** (ICSE 2019 Q1(c)); the examiners of 2019 noted that many candidates could not name it.

**Rules of scope (all checked with javac):**
- A **local variable must be given a value before use**: `int n; System.out.println(n);` gives *variable n might not have been initialized*.
- A variable declared **inside a block** (between braces, such as a loop body) **cannot be used after the block**: printing `sq` after the loop that declared it gives *cannot find symbol*.
- A local variable **cannot be declared again** in an inner block of the same method: *variable k is already defined in method main(String[])*.
- A parameter or local variable with the **same name as an instance variable hides it**; use `this.x` for the instance variable.

```java
class Scope
{
    static int count = 0;
    int x = 10;

    void show(int x)                       // parameter x hides the instance x
    {
        int y = 5;
        System.out.println(x + " " + this.x + " " + y + " " + count);
    }
}
```

### Static and instance members

| Static (class) members | Instance members |
|---|---|
| Declared with static | Declared without static |
| One copy for the whole class | One copy for each object |
| Used as ClassName.member | Used as object.member |
| A static method can use **only static members directly** | An instance method can use **both static and instance members** |

- A static method using an instance variable gives *non-static variable x cannot be referenced from a static context*; calling an instance method from a static method gives *non-static method show() cannot be referenced from a static context*. This is why main, which is static, must create an object before calling accept() or display().
- An instance method **can** use a static variable — e.g. `void up() { c++; }` with `static int c` compiles and works.

For ICSE 2024 Q1(xviii): the Assertion "a static method can access static and instance variables" is **false**. The scheme takes the Reason, "a static variable can be accessed only by a static method", as true and gives option (c). Strictly, instance methods can also use static variables (as above), so a well-argued (d) has the facts right — but write the scheme's answer, (c), in the examination.

### Encapsulation in Section B programs

ICSE class programs give **instance variables** as "member variables / data members" and **methods** to work on them — encapsulation in practice. Good habits:
- Declare data members at class level (not inside a method).
- Keep each member's work inside the class's methods (accept, calculate, display).
- Use local variables for temporary values (a loop counter, a slab amount) and parameters for values passed in.
- Use static only for data that truly belongs to the whole class (a counter of objects, a fixed rate).

### Summary of the chapter

- **Encapsulation** — data and methods in one unit (class); **data hiding** with private; access through public methods.
- **Access specifiers** — private, protected, public; default when none is written; "package" is not one.
- **Visibility** — private (class) < default (package) < protected (package + subclasses) < public (everywhere).
- **Getters and setters** — controlled reading and changing of private data, with checks.
- **Scope** — class (static, shared), instance (per object), argument (per call), local (per block; must be initialised).
- **Static rule** — static methods use static members directly; instance methods use both.

---

## 2. Learning Objectives

By the end of this chapter you should be able to:
1. Define encapsulation and data hiding and state their benefits.
2. Name the access specifiers, arrange them by accessibility and give real-life examples.
3. Apply the visibility rules for private, default, protected and public members.
4. Write getter and setter methods that protect private data.
5. Identify class, instance, argument and local variables, with their scope and lifetime.
6. Predict javac's errors for scope and static-context mistakes.

---

## 3. Detailed Section Explanations

### Section 1 — A capsule around the data
The class keeps its data and the code that changes it together; private hides the data.

### Section 2 — Four levels of access
private, default, protected, public — from the most closed to the most open.

### Section 3 — Doors with locks
Setters check every new value; getters hand out copies of values without changing them.

### Section 4 — Where a variable lives
A variable is usable only inside the braces where it is declared; static variables belong to the class itself.

---

## 4. Vocabulary (Key Terms)

| Term | Meaning |
|---|---|
| Encapsulation | Wrapping data and methods into a single unit, the class. |
| Data hiding | Keeping data private so that other classes cannot use it directly. |
| Access specifier | A keyword that controls where a member can be used. |
| private | Accessible only within its own class. |
| protected | Accessible in its package and in subclasses. |
| public | Accessible from every class. |
| Default access | Package-level access, when no specifier is written. |
| Getter (accessor) | A method that returns the value of a private variable. |
| Setter (mutator) | A method that changes a private variable, usually after checking. |
| Scope | The part of a program where a variable can be used. |
| Lifetime | How long a variable exists while the program runs. |
| Class variable | A static variable shared by all objects. |
| Instance variable | A non-static member variable; each object has its own copy. |
| Argument variable | A parameter that receives a value when a method is called. |
| Local variable | A variable declared inside a method or block. |

---

## 5. Important Facts, Formulas and Results

### 5.1 Must-know facts

| Fact | Detail |
|---|---|
| NOT an access specifier (private, protected, package, public) | package |
| Least accessibility | private |
| Accessible only within its own class | private |
| Post office example | public |
| Keyword for "no return type" | void |
| Keyword that makes a class variable | static |
| public vs private members | any class vs only the declaring class |
| Static method + instance variable | not allowed directly |
| Instance method + static variable | allowed |
| Local variable default value | none — must be assigned |
| Error for using a private member outside | "x has private access in ClassName" |

### 5.2 Memory aids

- **"Pri-De-Pro-Pub"** — private, default, protected, public, from least to most open.
- **"Static stays with the class; instance goes with the object."**
- **"A variable lives between its braces."**

### 5.3 Beyond the text (general knowledge, not needed for exam answers)

- `final` makes a variable a constant: `static final double MIN_BALANCE = 1000;`.
- Classes themselves can be public or default; a file can have only one public class, named like the file.
- In large programs, packages group classes, and default access keeps helper classes hidden inside a package.

---

## 6. Person Profiles

### 6.1 David Parnas (born 1941)
A Canadian computer scientist whose 1972 paper "On the Criteria To Be Used in Decomposing Systems into Modules" introduced information hiding: each module should hide its design decisions behind an interface. Encapsulation with private data is this idea at work.

### 6.2 Alan Kay (born 1940)
An American computer scientist who led the Smalltalk team at Xerox PARC in the 1970s and is widely credited with coining the term "object-oriented". In his view, objects keep their state to themselves and interact only by messages — method calls.

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas
- **Hide the data, show the service.**
- **Every change is checked** — setters guard the data.
- **The smaller the scope, the safer the variable.**

### 7.2 Real-life connections
- **ATMs:** the balance is private; you reach it only through the machine's menu (methods) after a PIN check.
- **Meghalaya:** a district office's records are private to its staff, its notice board is public, and its circulars are shared within the department — like default access.
- **Apps:** a game hides a player's score inside the program; only the game's own methods can add points.

---

## 8. Exam-Oriented Questions

> **How this chapter is examined (ICSE pattern):** The ICSE Computer Applications paper is of **2 hours, 100 marks**. **Section A** (40 marks) asks MCQs and 2-mark parts on access specifiers, private and public members, static members and the keywords void and static. **Section B** class programs rely on member, local and argument variables throughout.

### 8.1 Graded exercises — solutions

#### Exercise 9A — Concepts

**Q1.** Arrange in increasing order of accessibility: public, private, protected, default.
**Answer:** private, default, protected, public.

**Q2.** Name the kind of each variable: `class T { static int n; int a; void f(int b) { int c = 0; } }`
**Answer:** n — class variable; a — instance variable; b — argument variable; c — local variable.

**Q3.** What is data hiding? How is it done in Java?
**Answer:** Preventing other classes from using an object's data directly; the data members are declared private.

**Q4.** Write a getter and a setter for `private String name;`.
**Answer:** `String getName() { return name; }` and `void setName(String n) { name = n; }`.

**Q5.** Give a real-life example of public and of private access.
**Answer:** Public: a post office, open to all. Private: a personal locker or ATM PIN.

#### Exercise 9B — Tracing and errors

**Q6.** In class Scope, `static int count` and `int x = 10;`. After `a.bump(); a.bump(); b.bump();` (each bump adds 1 to count and to x), what does `a.show(99)` print, where show prints `x + " " + this.x + " " + y + " " + count` with `int y = 5`?
**Answer:** `99 12 5 3` — the parameter is 99; a's own x is 12; count is shared, so 3.

**Q7.** With the same objects, what does `b.show(1)` print?
**Answer:** `1 11 5 3` — b's x was bumped once.

**Q8.** Why does `class E16 { int x = 5; public static void main(String args[]) { System.out.println(x); } }` fail?
**Answer:** main is static and x is an instance variable: "non-static variable x cannot be referenced from a static context". Create an object and print `ob.x`, or make x static.

**Q9.** Will `int total = 0; for (int i = 1; i <= 3; i++) { int sq = i * i; total = total + sq; } System.out.println(total);` compile? What does it print?
**Answer:** Yes — total is declared outside the loop. It prints 14 (1 + 4 + 9).

**Q10.** In Marks, what is printed by `m.setMarks(85); m.setMarks(130); System.out.println(m.getMarks());`?
**Answer:** "Invalid marks: 130", then 85 — the setter refused 130.
### 8.2 Questions from CISCE board and specimen papers — solved

| Source | Question |
|---|---|
| ICSE 2026, Q1(iv) (1 mark) | Which of the following is NOT an access specifier? (a) private (b) protected (c) package (d) public |
| ICSE 2025, Q1(x) (1 mark) | Post office is an example for __________ access specifier. (a) public (b) local (c) protected (d) private |
| ICSE 2025 Improvement, Q1(ix) (1 mark) | Which of the following access specifiers will make a member accessible only within its own class? (a) public (b) private (c) protected (d) default |
| ICSE 2024, Q1(iv) (1 mark) | The access specifier that gives least accessibility is: (a) package (b) public (c) protected (d) private |
| ICSE 2024, Q1(xviii) (1 mark) | Assertion (A): Static method can access static and instance variables. Reason (R): Static variable can be accessed only by static method. (a) Assertion and Reason both are correct. (b) Assertion is true and Reason is false. (c) Assertion is false and Reason is true. (d) Assertion and Reason both are false. |
| ICSE 2019, Q1(c) (2 marks) | Name the keyword which: (i) indicates that a method has no return type. (ii) makes the variable as a class variable. |
| ICSE 2018, Q1(d) (2 marks) | How are private members of a class different from public members? |

**Solutions**

**2026 Q1(iv).** **(c) package** — Java's access-specifier keywords are private, protected and public; package (default) access has no keyword. *(Worked answer.)*

**2025 Q1(x).** **(a) public** — a post office serves everyone. The examiners noted that a few candidates chose (c) protected.

**2025 Improvement Q1(ix).** **(b) private** *(Worked answer.)*

**2024 Q1(iv).** **(d) private**

**2024 Q1(xviii).** **(c) Assertion is false and Reason is true** (the scheme's answer). The Assertion is false: a static method cannot use instance variables directly (javac: non-static variable cannot be referenced from a static context). Note that the Reason is not strictly true either — an instance method can also use a static variable — but the scheme accepts (c). The examiners noted that some candidates were unclear about static members and accessibility.

**2019 Q1(c).** (i) **void** (ii) **static** — the examiners noted that many candidates could not name static, and some wrote "keyword" as the answer.

**2018 Q1(d).** **public** members can be accessed from any other class; **private** members can be accessed only within the class in which they are declared.

### 8.3 More practice in the ICSE style

**Q1.** (2 marks) Name the access specifier for each: (i) a member any class may use; (ii) a member only its own class may use.
**Answer:** (i) public (ii) private.

**Q2.** (2 marks) State the scope of (i) an instance variable and (ii) a local variable declared in a for loop's body.
**Answer:** (i) the whole class — every non-static method of the class; (ii) only that loop body.

**Q3.** (2 marks) Why does `int n; System.out.println(n);` inside main not compile?
**Answer:** Local variables get no default value; javac reports "variable n might not have been initialized".

**Q4.** (2 marks) Give the output: `class E20 { static int c = 0; void up() { c++; } }` with `E20 p = new E20(); p.up(); System.out.println(E20.c);`
**Answer:** `1` — an instance method can change a static variable.

**Q5.** (2 marks) What is the error in `System.out.println(s.code);` where code is declared `private int code = 42;` in class Secret?
**Answer:** "code has private access in Secret" — a private member cannot be used from another class; provide a getter `int getCode()`.

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| MCQ | Least accessible specifier; NOT an access specifier; real-life example of an access level | 8.2, Section 1 |
| 2 marks | private vs public; keywords void and static | 8.2, 5.1 |
| MCQ / A-R | Static method and instance variables | 8.2, Section 1 |
| 2 marks | Identify class, instance, argument and local variables in a program | 8.1, Section 10 |

---
## 9. MCQs with Explanations

### Encapsulation and data hiding (Q1–Q12)

**Q1.** Wrapping up data and the methods that work on it into a single unit is
- (a) encapsulation
- (b) inheritance
- (c) polymorphism
- (d) iteration

**Answer:** (a) encapsulation
**Explanation:** The unit is the class.

**Q2.** The single unit in which Java encapsulates data and methods is
- (a) a package
- (b) a class
- (c) a loop
- (d) a variable

**Answer:** (b) a class
**Explanation:** Members are declared in a class.

**Q3.** Keeping data members private so that other classes cannot use them directly is
- (a) casting
- (b) overloading
- (c) boxing
- (d) data hiding

**Answer:** (d) data hiding
**Explanation:** It goes with encapsulation.

**Q4.** In an encapsulated class, data members are usually declared
- (a) public
- (b) private
- (c) static only
- (d) void

**Answer:** (b) private
**Explanation:** They are reached through methods.

**Q5.** Other classes use a well-encapsulated object through its
- (a) private variables
- (b) public methods
- (c) local variables
- (d) import statements

**Answer:** (b) public methods
**Explanation:** Methods are the doors to the data.

**Q6.** A benefit of encapsulation is that
- (a) data cannot be set to invalid values from outside
- (b) programs need no methods
- (c) every variable becomes static
- (d) objects need no constructors

**Answer:** (a) data cannot be set to invalid values from outside
**Explanation:** Every change passes through a checking method.

**Q7.** Which is NOT one of the four OOP principles?
- (a) encapsulation
- (b) abstraction
- (c) compilation
- (d) polymorphism

**Answer:** (c) compilation
**Explanation:** The fourth is inheritance.

**Q8.** ac.balance = 0; in another class, where balance is private, gives
- (a) balance becomes 0
- (b) a warning only
- (c) a run-time error
- (d) the error: balance has private access in SavingsAccount

**Answer:** (d) the error: balance has private access in SavingsAccount
**Explanation:** Private members are hidden.

**Q9.** Encapsulation makes a class easier to change because
- (a) the class has no constructor
- (b) all data is public
- (c) outside code depends only on its methods
- (d) variables are local

**Answer:** (c) outside code depends only on its methods
**Explanation:** The inside can change freely.

**Q10.** Storing a temperature only in Celsius but offering getFahrenheit() is an example of
- (a) an infinite loop
- (b) method overriding
- (c) boxing
- (d) hiding the internal representation

**Answer:** (d) hiding the internal representation
**Explanation:** Users do not see how it is stored.

**Q11.** A class can have private methods to
- (a) replace constructors
- (b) be called from any class
- (c) help its own methods, hidden from other classes
- (d) create packages

**Answer:** (c) help its own methods, hidden from other classes
**Explanation:** e.g. valid(int m).

**Q12.** In real life, an ATM keeps the balance private and allows changes only through its menu. In Java the menu options correspond to
- (a) packages
- (b) private variables
- (c) local variables
- (d) public methods

**Answer:** (d) public methods
**Explanation:** The balance is the private data.

### Access specifiers and visibility (Q13–Q34)

**Q13.** Which of the following is NOT an access specifier?
- (a) private
- (b) protected
- (c) package
- (d) public

**Answer:** (c) package
**Explanation:** Default access has no keyword.

**Q14.** The access specifier that gives the least accessibility is
- (a) package
- (b) public
- (c) protected
- (d) private

**Answer:** (d) private
**Explanation:** Only its own class.

**Q15.** The access specifier that gives the most accessibility is
- (a) private
- (b) protected
- (c) public
- (d) default

**Answer:** (c) public
**Explanation:** Every class can use it.

**Q16.** A post office is an example of the ______ access specifier.
- (a) protected
- (b) local
- (c) public
- (d) private

**Answer:** (c) public
**Explanation:** It serves everyone.

**Q17.** The access specifier that makes a member accessible only within its own class is
- (a) public
- (b) protected
- (c) private
- (d) default

**Answer:** (c) private
**Explanation:** ICSE 2025 Improvement Q1(ix).

**Q18.** When no access specifier is written, the member has
- (a) public access
- (b) private access
- (c) default (package) access
- (d) no access at all

**Answer:** (c) default (package) access
**Explanation:** Visible in the same package.

**Q19.** The correct order from least to most accessible is
- (a) protected, private, default, public
- (b) public, protected, default, private
- (c) default, private, public, protected
- (d) private, default, protected, public

**Answer:** (d) private, default, protected, public
**Explanation:** Pri-De-Pro-Pub.

**Q20.** A protected member is visible in
- (a) its package and in subclasses in other packages
- (b) its own class only
- (c) every class everywhere
- (d) no class

**Answer:** (a) its package and in subclasses in other packages
**Explanation:** More than default, less than public.

**Q21.** A default member is visible in
- (a) subclasses only
- (b) its own class only
- (c) every class everywhere
- (d) all classes of the same package

**Answer:** (d) all classes of the same package
**Explanation:** Package-level access.

**Q22.** public members can be accessed from
- (a) any other class
- (b) only the same class
- (c) only subclasses
- (d) only static methods

**Answer:** (a) any other class
**Explanation:** As in the 2018 scheme.

**Q23.** private members can be accessed from
- (a) any class
- (b) only the class in which they are declared
- (c) the same package
- (d) subclasses

**Answer:** (b) only the class in which they are declared
**Explanation:** As in the 2018 scheme.

**Q24.** Which access specifier is suitable for a balance that only the account's methods should change?
- (a) public
- (b) private
- (c) protected
- (d) default

**Answer:** (b) private
**Explanation:** Data hiding.

**Q25.** Which access specifier is suitable for a deposit() method used by every class?
- (a) public
- (b) private
- (c) none is possible
- (d) static

**Answer:** (a) public
**Explanation:** It is a service for others.

**Q26.** Writing package int a; as a member declaration gives
- (a) default access
- (b) the error: illegal start of type
- (c) public access
- (d) private access

**Answer:** (b) the error: illegal start of type
**Explanation:** package is not an access specifier.

**Q27.** Access specifiers are also called
- (a) access modifiers
- (b) data types
- (c) literals
- (d) operators

**Answer:** (a) access modifiers
**Explanation:** They modify access.

**Q28.** A private member of class A can be used in class B
- (a) only in loops
- (b) always
- (c) only if B is in the same package
- (d) never directly

**Answer:** (d) never directly
**Explanation:** Only through A's methods.

**Q29.** A school notice board read only by students of that school is most like
- (a) private access
- (b) public access
- (c) default (package) access
- (d) no access

**Answer:** (c) default (package) access
**Explanation:** Open to the "family" only.

**Q30.** A personal ATM PIN is most like
- (a) public access
- (b) private access
- (c) protected access
- (d) default access

**Answer:** (b) private access
**Explanation:** Known only to its owner.

**Q31.** Which statement is TRUE?
- (a) private is less accessible than protected.
- (b) public is less accessible than default.
- (c) protected is the least accessible.
- (d) default is more accessible than public.

**Answer:** (a) private is less accessible than protected.
**Explanation:** private is the most closed.

**Q32.** Statement I: A public member is visible in every class. Statement II: A protected member is visible only in its own class.
- (a) Both statements are true.
- (b) Both statements are false.
- (c) Statement I is true, Statement II is false.
- (d) Statement I is false, Statement II is true.

**Answer:** (c) Statement I is true, Statement II is false.
**Explanation:** That describes private.

**Q33.** The keyword public before main allows
- (a) main to be overloaded only
- (b) main to return a value
- (c) Java to call main from outside the class
- (d) main to be private

**Answer:** (c) Java to call main from outside the class
**Explanation:** The Java system starts the program there.

**Q34.** The error message for using a private member from another class is
- (a) unreachable statement
- (b) cannot find symbol
- (c) missing return statement
- (d) x has private access in ClassName

**Answer:** (d) x has private access in ClassName
**Explanation:** javac names the class.

### Getters and setters (Q35–Q44)

**Q35.** A method that returns the value of a private variable is a
- (a) getter (accessor)
- (b) setter (mutator)
- (c) constructor
- (d) static block

**Answer:** (a) getter (accessor)
**Explanation:** e.g. getBalance().

**Q36.** A method that changes a private variable, usually after a check, is a
- (a) getter
- (b) setter
- (c) destructor
- (d) package

**Answer:** (b) setter
**Explanation:** e.g. setMarks(int m).

**Q37.** A getter is usually a
- (a) pure method
- (b) impure method
- (c) constructor
- (d) static variable

**Answer:** (a) pure method
**Explanation:** It changes nothing.

**Q38.** A setter is usually a
- (a) pure method
- (b) impure method
- (c) wrapper class
- (d) local variable

**Answer:** (b) impure method
**Explanation:** It changes the object's state.

**Q39.** The correct getter for private String name; is
- (a) String getName() { return name; }
- (b) void getName() { return name; }
- (c) getName() { name = n; }
- (d) int getName() { return name; }

**Answer:** (a) String getName() { return name; }
**Explanation:** It returns a String.

**Q40.** The correct setter for private int age; is
- (a) setAge(int a) { }
- (b) int setAge() { return age; }
- (c) void setAge() { return a; }
- (d) void setAge(int a) { age = a; }

**Answer:** (d) void setAge(int a) { age = a; }
**Explanation:** It receives the new value.

**Q41.** setMarks(int m) saves m only if 0 ≤ m ≤ 100. After setMarks(85); setMarks(130); the value returned by getMarks() is
- (a) 130
- (b) 85
- (c) 0
- (d) 215

**Answer:** (b) 85
**Explanation:** 130 was refused.

**Q42.** SavingsAccount refuses a withdrawal that would leave less than 1000. Starting with 5000, after withdraw(4500) and withdraw(3000) the balance is
- (a) 500
- (b) −2500
- (c) 5000
- (d) 2000

**Answer:** (d) 2000
**Explanation:** The first withdrawal is refused.

**Q43.** The main reason to use a setter instead of a public variable is
- (a) to check the new value before saving it
- (b) to make the program longer
- (c) to avoid using objects
- (d) to make the variable static

**Answer:** (a) to check the new value before saving it
**Explanation:** Invalid values are rejected.

**Q44.** Thermometer stores celsius only. After setFahrenheit(212), getCelsius() returns
- (a) 212.0
- (b) 0.0
- (c) 100.0
- (d) 32.0

**Answer:** (c) 100.0
**Explanation:** (212 − 32) × 5 / 9.

### Scope of variables (Q45–Q62)

**Q45.** The part of a program in which a variable can be used is its
- (a) value
- (b) type
- (c) scope
- (d) package

**Answer:** (c) scope
**Explanation:** Between its braces.

**Q46.** A variable declared in a class with the keyword static is a
- (a) constant only
- (b) local variable
- (c) argument variable
- (d) class variable

**Answer:** (d) class variable
**Explanation:** One copy for the class.

**Q47.** The keyword which makes a variable a class variable is
- (a) void
- (b) static
- (c) private
- (d) new

**Answer:** (b) static
**Explanation:** ICSE 2019 Q1(c).

**Q48.** The keyword which indicates that a method has no return type is
- (a) void
- (b) static
- (c) null
- (d) return

**Answer:** (a) void
**Explanation:** ICSE 2019 Q1(c).

**Q49.** A member variable declared without static is
- (a) an argument variable
- (b) a class variable
- (c) a local variable
- (d) an instance variable

**Answer:** (d) an instance variable
**Explanation:** Each object has its own copy.

**Q50.** In void f(int b), the variable b is
- (a) an argument variable
- (b) a class variable
- (c) an instance variable
- (d) a constant

**Answer:** (a) an argument variable
**Explanation:** A parameter.

**Q51.** A variable declared inside a method is
- (a) a local variable
- (b) an instance variable
- (c) a class variable
- (d) a package

**Answer:** (a) a local variable
**Explanation:** It exists only in that method.

**Q52.** How many copies of a class variable exist for 5 objects?
- (a) 6
- (b) 5
- (c) 1
- (d) 0

**Answer:** (c) 1
**Explanation:** It is shared.

**Q53.** How many copies of an instance variable exist for 5 objects?
- (a) 1
- (b) 10
- (c) 5
- (d) 0

**Answer:** (c) 5
**Explanation:** One per object.

**Q54.** int n; System.out.println(n); inside main gives
- (a) 0
- (b) the error: variable n might not have been initialized
- (c) null
- (d) a run-time error

**Answer:** (b) the error: variable n might not have been initialized
**Explanation:** Local variables get no default value.

**Q55.** Using sq after the loop in which it was declared gives
- (a) the last value of sq
- (b) the error: cannot find symbol
- (c) 0
- (d) a warning only

**Answer:** (b) the error: cannot find symbol
**Explanation:** sq lives only in the loop body.

**Q56.** int k = 1; followed by an inner block { int k = 2; } in the same method gives
- (a) k = 2 everywhere
- (b) two separate variables, both allowed
- (c) the error: variable k is already defined
- (d) a run-time error

**Answer:** (c) the error: variable k is already defined
**Explanation:** A local name cannot be reused inside its scope.

**Q57.** int total = 0; for (int i = 1; i <= 3; i++) { int sq = i * i; total = total + sq; } total is then
- (a) 6
- (b) 14
- (c) 9
- (d) an error

**Answer:** (b) 14
**Explanation:** 1 + 4 + 9.

**Q58.** The default value of an instance variable of type int is
- (a) 1
- (b) none
- (c) null
- (d) 0

**Answer:** (d) 0
**Explanation:** Member variables get defaults.

**Q59.** A local variable's lifetime ends
- (a) never
- (b) when the program ends
- (c) when the object is created
- (d) at the end of its block

**Answer:** (d) at the end of its block
**Explanation:** Then it no longer exists.

**Q60.** In void show(int x) inside a class with an instance variable x, the expression this.x refers to
- (a) the instance variable
- (b) the parameter
- (c) a local variable
- (d) a class variable

**Answer:** (a) the instance variable
**Explanation:** The parameter hides it.

**Q61.** In LibraryBook, int fine = 0; inside returnBook() is
- (a) an argument variable
- (b) an instance variable
- (c) a class variable
- (d) a local variable

**Answer:** (d) a local variable
**Explanation:** Declared in the method body.

**Q62.** In LibraryBook, static int issuedCount is
- (a) a class variable
- (b) a local variable
- (c) an argument variable
- (d) a private method

**Answer:** (a) a class variable
**Explanation:** Shared by all books.

### Static and instance members (Q63–Q76)

**Q63.** A static method can use directly
- (a) only static members
- (b) only instance members
- (c) both static and instance members
- (d) no members

**Answer:** (a) only static members
**Explanation:** It has no object of its own.

**Q64.** An instance method can use
- (a) no members
- (b) only instance members
- (c) only static members
- (d) both static and instance members

**Answer:** (d) both static and instance members
**Explanation:** It runs on an object and can see the class too.

**Q65.** Assertion (A): Static method can access static and instance variables. Reason (R): Static variable can be accessed only by static method. The scheme's answer is
- (a) Both A and R are correct.
- (b) A is true and R is false.
- (c) A is false and R is true.
- (d) Both A and R are false.

**Answer:** (c) A is false and R is true.
**Explanation:** ICSE 2024 Q1(xviii), as marked in the scheme.

**Q66.** class E16 { int x = 5; } with System.out.println(x); inside static main gives
- (a) 5
- (b) the error: non-static variable x cannot be referenced from a static context
- (c) 0
- (d) null

**Answer:** (b) the error: non-static variable x cannot be referenced from a static context
**Explanation:** main is static.

**Q67.** Calling the instance method show() directly from a static method gives
- (a) the error: non-static method show() cannot be referenced from a static context
- (b) a normal call
- (c) a run-time error
- (d) missing return statement

**Answer:** (a) the error: non-static method show() cannot be referenced from a static context
**Explanation:** An object is needed.

**Q68.** static int c = 0; void up() { c++; } and in main, E20 p = new E20(); p.up(); prints c as
- (a) 0
- (b) 1
- (c) an error
- (d) 2

**Answer:** (b) 1
**Explanation:** Instance methods can change static variables.

**Q69.** A static variable is accessed from outside the class as
- (a) new variable
- (b) variable() only
- (c) ClassName.variable
- (d) this.variable only

**Answer:** (c) ClassName.variable
**Explanation:** e.g. Visitor.getCount(), Scope.count.

**Q70.** In Visitor, the constructor increases static count. After three objects are created, Visitor.getCount() returns
- (a) 1
- (b) 3
- (c) 0
- (d) 4

**Answer:** (b) 3
**Explanation:** One shared counter.

**Q71.** In Scope, count is static and x = 10 is an instance variable. After a.bump(); a.bump(); b.bump(); the value of Scope.count is
- (a) 2
- (b) 3
- (c) 1
- (d) 12

**Answer:** (b) 3
**Explanation:** Three bumps in all.

**Q72.** With the same calls, a.x and b.x are
- (a) 12 and 11
- (b) 13 and 13
- (c) 10 and 10
- (d) 11 and 12

**Answer:** (a) 12 and 11
**Explanation:** Each object has its own x.

**Q73.** Why must main create an object before calling accept()?
- (a) main has no parameters
- (b) accept() is private
- (c) main is static and accept() is an instance method
- (d) objects run faster

**Answer:** (c) main is static and accept() is an instance method
**Explanation:** Instance methods need an object.

**Q74.** Which variable is the best choice to be static?
- (a) a method's parameter
- (b) each student's name
- (c) a loop counter
- (d) a counter of all objects created

**Answer:** (d) a counter of all objects created
**Explanation:** It belongs to the whole class.

**Q75.** static int twice() { return count * 2; } with count = 3 returns
- (a) 3
- (b) 6
- (c) 9
- (d) an error

**Answer:** (b) 6
**Explanation:** A static method may use a static variable.

**Q76.** Which is TRUE of class variables?
- (a) They have no default value.
- (b) Each object has a separate copy.
- (c) They must be declared inside a method.
- (d) They are shared by all objects of the class.

**Answer:** (d) They are shared by all objects of the class.
**Explanation:** One copy for the class.
## 10. Short-Answer Questions (Section A, 2 marks)

### Concept questions (2 marks each)

**Q1.** What is encapsulation?
**Answer:** The wrapping up of data and the methods that work on that data into a single unit, the class.
The data is usually hidden (private) and used through public methods.

**Q2.** What is data hiding? How does Java achieve it?
**Answer:** Preventing other classes from using an object's data directly.
The data members are declared private and reached only through the class's methods.

**Q3.** Name the access specifiers of Java in increasing order of accessibility.
**Answer:** private, default (no keyword), protected, public.
private is the least accessible and public the most.

**Q4.** How are private members of a class different from public members?
**Answer:** public members can be accessed from any other class.
private members can be accessed only within the class in which they are declared.

**Q5.** Distinguish between protected and default access.
**Answer:** Default (package) access, with no keyword, allows use only within the same package.
protected allows use within the same package and also in subclasses in other packages.

**Q6.** What are getter and setter methods? Give one example of each.
**Answer:** A getter returns the value of a private variable: `int getMarks() { return marks; }`.
A setter changes it after a check: `void setMarks(int m) { if (m >= 0 && m <= 100) marks = m; }`.

**Q7.** Distinguish between a class variable and an instance variable.
**Answer:** A class variable is declared with static; one copy is shared by all objects.
An instance variable is declared without static; each object has its own copy.

**Q8.** Distinguish between a local variable and an argument variable.
**Answer:** A local variable is declared inside a method or block and must be assigned before use.
An argument variable is declared in the method header and receives the value passed in the call.

**Q9.** Name the keyword which (i) indicates that a method has no return type, (ii) makes a variable a class variable.
**Answer:** (i) void
(ii) static

**Q10.** What is meant by the scope and the lifetime of a variable?
**Answer:** Scope is the part of the program in which the variable can be used.
Lifetime is how long it exists while the program runs.

**Q11.** Can a static method use an instance variable directly? Explain.
**Answer:** No — a static method belongs to the class and has no object, so it cannot know whose instance variable to use.
javac reports "non-static variable cannot be referenced from a static context".

**Q12.** Give a real-life example of public access and of private access.
**Answer:** Public: a post office, open to everyone.
Private: a person's ATM PIN, known only to its owner.

### Output and error questions (2 marks each)

**Q13.** Identify the kind of each variable: `class T { static int n; int a; void f(int b) { int c = 0; } }`
**Answer:** n — class variable; a — instance variable.
b — argument variable; c — local variable.

**Q14.** In class Scope (`static int count = 0; int x = 10;`), bump() does `count++; x++;`. After `a.bump(); a.bump(); b.bump();`, give the output of `System.out.println(Scope.count + " " + Scope.twice());` where twice() returns count * 2.
**Answer:** `3 6`
count is shared by a and b.

**Q15.** With the same objects, show(int x) prints `x + " " + this.x + " " + y + " " + count` with local y = 5. Give the output of `a.show(99); b.show(1);`
**Answer:** `99 12 5 3` then `1 11 5 3`
The parameter x hides the instance x; this.x is the object's own.

**Q16.** Give the output: `Marks m = new Marks(); m.setMarks(85); m.setMarks(130); System.out.println(m.getMarks());` where setMarks prints "Invalid marks: " + m for values outside 0–100.
**Answer:** `Invalid marks: 130` then `85`
The setter refused the second value.

**Q17.** Give the output: `class E20 { static int c = 0; void up() { c++; } }` with `E20 p = new E20(); p.up(); E20 q = new E20(); q.up(); System.out.println(E20.c);`
**Answer:** `2`
Both objects increase the one shared c.

**Q18.** Find the error: `class Secret { private int code = 42; }` and in another class `System.out.println(s.code);`
**Answer:** "code has private access in Secret".
Add a getter `int getCode() { return code; }` and print `s.getCode()`.

**Q19.** Find the error: `class E16 { int x = 5; public static void main(String args[]) { System.out.println(x); } }`
**Answer:** "non-static variable x cannot be referenced from a static context".
Create an object: `E16 ob = new E16(); System.out.println(ob.x);`.

**Q20.** Find the error: `for (int i = 1; i <= 3; i++) { int sq = i * i; } System.out.println(sq);`
**Answer:** "cannot find symbol" — sq exists only inside the loop body.
Declare sq before the loop.

**Q21.** Find the error: `int n; System.out.println(n);` inside main.
**Answer:** "variable n might not have been initialized".
Local variables get no default value; write `int n = 0;`.

**Q22.** Find the error: `class E19 { int v; void show() { System.out.println(v); } static void tell() { show(); } }`
**Answer:** "non-static method show() cannot be referenced from a static context".
Make tell() non-static, or call show() through an object.

---

## 11. Long-Answer Questions (Section B programs)

*Each program was compiled and run with Java 21; the output follows each.*

### Section B programs (15 marks each)

**Q1.** Define a class SavingsAccount with private members holder and balance and a minimum balance of ₹1000. A constructor sets the holder and the opening balance; getBalance() returns the balance; deposit(double amt) accepts only positive amounts; withdraw(double amt) refuses any withdrawal that would leave less than ₹1000. Test it in main.
**Answer:**
```java
class SavingsAccount
{
    private String holder;
    private double balance;
    private static final double MIN_BALANCE = 1000;

    SavingsAccount(String h, double opening)
    {
        holder = h;
        balance = opening;
    }

    double getBalance()
    {
        return balance;
    }

    void deposit(double amt)
    {
        if (amt > 0)
            balance = balance + amt;
        else
            System.out.println("Deposit must be positive");
    }

    void withdraw(double amt)
    {
        if (balance - amt >= MIN_BALANCE)
            balance = balance - amt;
        else
            System.out.println("Refused: balance cannot fall below " + MIN_BALANCE);
    }

    public static void main(String args[])
    {
        SavingsAccount ac = new SavingsAccount("Ibadahun Rymbai", 5000);
        ac.deposit(-200);
        ac.withdraw(4500);
        ac.withdraw(3000);
        ac.deposit(1500);
        System.out.println(ac.holder + ": balance " + ac.getBalance());
    }
}
```
Output (5000; −200 refused; 4500 refused; 3000 withdrawn; 1500 deposited):
```
Deposit must be positive
Refused: balance cannot fall below 1000.0
Ibadahun Rymbai: balance 3500.0
```

**Q2.** Define a class StudentRecord with private name and marks in English, Maths and Science. The constructor sets the name; setMarks(int e, int m, int s) saves the marks only if all are from 0 to 100, using a private method valid(int m); getPercentage() and getName() return values. Test with an invalid and a valid set of marks.
**Answer:**
```java
class StudentRecord
{
    private String name;
    private int eng, maths, sci;

    StudentRecord(String n)
    {
        name = n;
    }

    private boolean valid(int m)
    {
        return m >= 0 && m <= 100;
    }

    void setMarks(int e, int m, int s)
    {
        if (valid(e) && valid(m) && valid(s))
        {
            eng = e;
            maths = m;
            sci = s;
        }
        else
            System.out.println("Marks must be from 0 to 100; not saved");
    }

    double getPercentage()
    {
        return (eng + maths + sci) / 3.0;
    }

    String getName()
    {
        return name;
    }

    public static void main(String args[])
    {
        StudentRecord r = new StudentRecord("Mebanshan");
        r.setMarks(78, 104, 66);
        r.setMarks(78, 94, 66);
        System.out.println(r.getName() + ": " + Math.round(r.getPercentage() * 100) / 100.0 + "%");
    }
}
```
Output:
```
Marks must be from 0 to 100; not saved
Mebanshan: 79.33%
```

**Q3.** Define a class Visitor with a private static count and a private instance variable name. The constructor stores the name and increases count; static getCount() returns count; greet() prints a welcome with the visitor number so far. Create three visitors and show that count is shared.
**Answer:**
```java
class Visitor
{
    private static int count = 0;      // class variable: one copy for all objects
    private String name;               // instance variable: one copy per object

    Visitor(String n)
    {
        name = n;
        count++;
    }

    static int getCount()
    {
        return count;
    }

    void greet()
    {
        System.out.println("Welcome, " + name + ". You are visitor number " + count + " so far.");
    }

    public static void main(String args[])
    {
        Visitor v1 = new Visitor("Aiom");
        v1.greet();
        Visitor v2 = new Visitor("Batskhem");
        Visitor v3 = new Visitor("Careen");
        v1.greet();
        System.out.println("Total visitors: " + Visitor.getCount());
    }
}
```
Output:
```
Welcome, Aiom. You are visitor number 1 so far.
Welcome, Aiom. You are visitor number 3 so far.
Total visitors: 3
```

**Q4.** Define a class LibraryBook with a class variable issuedCount, private instance variables title and issued, a constructor, issue(String member) and returnBook(int daysLate), which uses a local variable fine (₹2 per day late). Label each kind of variable in comments and test the class.
**Answer:**
```java
class LibraryBook
{
    static int issuedCount = 0;        // class variable
    private String title;              // instance variables
    private boolean issued;

    LibraryBook(String t)              // t: argument variable
    {
        title = t;
        issued = false;
    }

    void issue(String member)          // member: argument variable
    {
        if (issued)
            System.out.println(title + " is already issued");
        else
        {
            issued = true;
            issuedCount++;
            System.out.println(title + " issued to " + member);
        }
    }

    void returnBook(int daysLate)
    {
        int fine = 0;                  // local variable
        if (daysLate > 0)
            fine = daysLate * 2;
        issued = false;
        issuedCount--;
        System.out.println(title + " returned; fine Rs " + fine);
    }

    public static void main(String args[])
    {
        LibraryBook b1 = new LibraryBook("Wings of Fire");
        LibraryBook b2 = new LibraryBook("The Story of My Experiments with Truth");
        b1.issue("Rangdajied");
        b1.issue("Saphira");
        b2.issue("Saphira");
        System.out.println("Books out: " + LibraryBook.issuedCount);
        b1.returnBook(4);
        System.out.println("Books out: " + LibraryBook.issuedCount);
    }
}
```
Output:
```
Wings of Fire issued to Rangdajied
Wings of Fire is already issued
The Story of My Experiments with Truth issued to Saphira
Books out: 2
Wings of Fire returned; fine Rs 8
Books out: 1
```

**Q5.** Define a class Thermometer that stores a temperature privately in Celsius only, with setCelsius(), setFahrenheit(), getCelsius() and getFahrenheit(). Test with 37 °C and 212 °F.
**Answer:**
```java
class Thermometer
{
    private double celsius;            // stored in one unit only

    void setCelsius(double c)
    {
        celsius = c;
    }

    void setFahrenheit(double f)
    {
        celsius = (f - 32) * 5 / 9;
    }

    double getCelsius()
    {
        return celsius;
    }

    double getFahrenheit()
    {
        return celsius * 9 / 5 + 32;
    }

    public static void main(String args[])
    {
        Thermometer t = new Thermometer();
        t.setCelsius(37);
        System.out.println(t.getCelsius() + " C = " + t.getFahrenheit() + " F");
        t.setFahrenheit(212);
        System.out.println(t.getCelsius() + " C = " + t.getFahrenheit() + " F");
    }
}
```
Output:
```
37.0 C = 98.6 F
100.0 C = 212.0 F
```

**Q6.** Define a class Plot with private length and breadth. setSize(double l, double b) returns false and prints a message for non-positive sides, otherwise saves them and returns true; area(), perimeter() and isSquare() complete the class. Test with −4 × 9, 12 × 12 and 20 × 15.
**Answer:**
```java
class Plot
{
    private double length, breadth;

    boolean setSize(double l, double b)
    {
        if (l <= 0 || b <= 0)
        {
            System.out.println("Sides must be positive");
            return false;
        }
        length = l;
        breadth = b;
        return true;
    }

    double area()
    {
        return length * breadth;
    }

    double perimeter()
    {
        return 2 * (length + breadth);
    }

    boolean isSquare()
    {
        return length == breadth;
    }

    public static void main(String args[])
    {
        Plot p = new Plot();
        p.setSize(-4, 9);
        if (p.setSize(12, 12))
            System.out.println("Area " + p.area() + ", perimeter " + p.perimeter() + ", square: " + p.isSquare());
        p.setSize(20, 15);
        System.out.println("Area " + p.area() + ", perimeter " + p.perimeter() + ", square: " + p.isSquare());
    }
}
```
Output:
```
Sides must be positive
Area 144.0, perimeter 48.0, square: true
Area 300.0, perimeter 70.0, square: false
```

---

## 12. Competency / Application Questions

**Q1. (Choose the access)** A Student class has name, marks and a method calculateGrade(). Which members should be private and which public?
**Model answer:** name and marks private; calculateGrade() and the getters and setters public.

**Q2. (Fix the design)** A Bank class has `public double balance;`, and another class sets it to −5000. How should the class be changed?
**Model answer:** Make balance private and provide deposit() and withdraw() methods that check the amounts.

**Q3. (Static or not?)** In a class Ticket, which should be static: the ticket number of each ticket, or the total number of tickets sold? Why?
**Model answer:** The total sold — it belongs to the whole class; each ticket's own number is an instance variable.

**Q4. (Find the scope)** A student declares `int sum` inside a for loop and prints it after the loop. What goes wrong, and how is it fixed?
**Model answer:** sum is out of scope after the loop ("cannot find symbol"); declare and initialise it before the loop.

**Q5. (Hide the format)** Why is it useful that Thermometer stores only Celsius but offers getFahrenheit()?
**Model answer:** Users need not know how the value is stored, and the class can change its storage without affecting them.

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) A is true, but R is false.
- (b) A is false, but R is true.
- (c) Both A and R are true, and R is the correct explanation of A.
- (d) Both A and R are true, but R is **not** the correct explanation of A.

**Q1.**
**A:** A private member cannot be used directly from another class.
**R:** private gives the least accessibility.
**Answer:** (c)
**Explanation:** It is limited to its own class.

**Q2.**
**A:** package is an access specifier in Java.
**R:** Default access is given when no access specifier is written.
**Answer:** (b)
**Explanation:** Default access has no keyword.

**Q3.**
**A:** A class variable has one copy shared by all objects.
**R:** It is declared with the keyword static.
**Answer:** (c)
**Explanation:** static makes it belong to the class.

**Q4.**
**A:** A local variable gets the default value 0.
**R:** Instance variables get default values.
**Answer:** (b)
**Explanation:** Local variables must be assigned before use.

**Q5.**
**A:** Encapsulation protects data from invalid changes.
**R:** Changes go through methods that can check them.
**Answer:** (c)
**Explanation:** Setters check values.

**Q6.**
**A:** An instance method can use a static variable.
**R:** The main method is static.
**Answer:** (d)
**Explanation:** Both true; unrelated.

**Q7.**
**A:** A variable declared inside a loop body can be used after the loop.
**R:** A variable is visible only inside the block in which it is declared.
**Answer:** (b)
**Explanation:** It goes out of scope.

**Q8.**
**A:** A getter is usually a pure method.
**R:** A getter must be declared static.
**Answer:** (a)
**Explanation:** Getters are usually instance methods.

---

## 14. Case-Based Questions

*Read each situation and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The guarded account

> SavingsAccount keeps holder and balance private and allows changes only through deposit() and withdraw().

**(i)** Which OOP principle is shown?
**Answer:** Encapsulation (with data hiding).

**(ii)** What happens if another class writes `ac.balance = 0;`?
**Answer:** A compile error: balance has private access.

**(iii)** Which access specifier suits deposit()?
**Answer:** public.

**(iv)** Is getBalance() pure or impure?
**Answer:** Pure.

### Case 2 — The visitor counter

> Visitor has `private static int count` and `private String name`; the constructor increases count.

**(i)** Name the kind of variable count is.
**Answer:** Class variable.

**(ii)** Name the kind of variable name is.
**Answer:** Instance variable.

**(iii)** After three objects, what is count?
**Answer:** 3.

**(iv)** Can a static method use name directly?
**Answer:** No.

### Case 3 — The library fine

> In returnBook(int daysLate), the line `int fine = 0;` is followed by `if (daysLate > 0) fine = daysLate * 2;`.

**(i)** What kind of variable is daysLate?
**Answer:** Argument variable.

**(ii)** What kind of variable is fine?
**Answer:** Local variable.

**(iii)** What is the fine for 4 days late?
**Answer:** ₹8.

**(iv)** Can fine be used in issue()?
**Answer:** No — it is local to returnBook().

---

## 15. Revision Notes

### Chapter at a glance
- Encapsulation: data + methods in one class; data hiding with private; access through public methods.
- Access: private (class) < default, no keyword (package) < protected (package + subclasses) < public (all). "package" is not an access specifier.
- Getters (accessors, pure) read; setters (mutators, impure) change after checking.
- Variables: class (static, shared), instance (per object), argument (per call), local (per block, no default).
- Static methods use only static members directly; instance methods use both.
- Keywords: void = no return type; static = class variable or method.

### Common mistakes

| Mistake | Correct idea |
|---|---|
| Listing "package" as an access specifier | The three keywords are private, protected, public. |
| Using a private member from another class | Use the class's getter or setter. |
| Printing an instance variable inside static main | Create an object first. |
| Using a loop's local variable after the loop | Declare it before the loop. |
| Using a local variable before giving it a value | Initialise it: `int n = 0;`. |
| Making every member public | Keep data private; expose methods. |

---

## 16. Chapter Test

**Class X · Computer Applications · Chapter 9: Encapsulation**
**Time:** 1 hour · **Maximum marks:** 40

**General instructions:**
1. Part I (20 marks) is compulsory. Attempt any two questions from Part II (2 × 10 = 20).
2. The intended marks for questions or parts of questions are given in brackets [ ].

### Part I — Multiple-choice questions (10 × 1 = 10)

**1.** NOT an access specifier:
(a) private (b) protected (c) package (d) public

**2.** Least accessibility:
(a) package (b) public (c) protected (d) private

**3.** A post office is an example of ______ access:
(a) public (b) local (c) protected (d) private

**4.** The keyword that makes a variable a class variable:
(a) void (b) new (c) static (d) private

**5.** Accessible only within its own class:
(a) public (b) protected (c) default (d) private

**6.** A variable declared in a method header is:
(a) a local variable (b) an argument variable (c) a class variable (d) an instance variable

**7.** A local variable used before assignment gives:
(a) 0 (b) null (c) the error: might not have been initialized (d) a warning only

**8.** Wrapping data and methods into one unit:
(a) inheritance (b) encapsulation (c) polymorphism (d) abstraction

**9.** A static method can use directly:
(a) only static members (b) only instance members (c) both (d) neither

**10.** Statement I: Each object has its own copy of an instance variable. Statement II: Each object has its own copy of a class variable.
(a) Both true (b) Both false (c) I true, II false (d) I false, II true

### Part I — Short answers (5 × 2 = 10)

**11.** How are private members of a class different from public members? [2]

**12.** Name the keyword which (i) indicates that a method has no return type, (ii) makes a variable a class variable. [2]

**13.** Identify the variables in `class T { static int n; int a; void f(int b) { int c = 0; } }` by kind. [2]

**14.** Find the error: `int n; System.out.println(n);` inside main. [2]

**15.** What is encapsulation? [2]

### Part II — Answer any two questions (2 × 10 = 20)

**16.** Define the class SavingsAccount (private data, minimum balance ₹1000, deposit, withdraw, getBalance). [10]

**17.** Define the class Visitor with a static counter and show that it is shared by three objects. [10]

**18.** Define the class StudentRecord with private marks, a validating setter and getPercentage(). [10]

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
| 1 | Encapsulation | Compile error (private) | public | Pure |
| 2 | Class variable | Instance variable | 3 | No |
| 3 | Argument variable | Local variable | ₹8 | No |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Part I, Q1–10 (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | c | d | a | c | d | b | c | b | a | c |

**Part I, Q11–15 (2 marks each)**

**11.** public: any class (1); private: only the declaring class (1).
**12.** void (1); static (1).
**13.** n class, a instance (1); b argument, c local (1).
**14.** "variable n might not have been initialized" (1); initialise it (1).
**15.** Data and methods in one unit, the class (1); data hidden and used through methods (1).

**Part II (10 marks each)**

**16.–18.** Private data members (2), constructor or setters with checks (3), other methods (3), main testing the class (2).
