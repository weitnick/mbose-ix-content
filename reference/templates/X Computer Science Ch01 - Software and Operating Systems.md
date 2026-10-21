# Software and Operating Systems

| Field | Value |
|---|---|
| Board | MBOSE (Meghalaya Board of School Education) |
| Class | X |
| Subject | Computer Science |
| Chapter | Computer Fundamentals · Chapter 1 |
| Title | Software and Operating Systems |
| Textbook source | *Click Start 10 – Computer Science for Schools* (Cambridge University Press). The book was not available; see the note below. |
| Exam weightage | **Computer Fundamentals** (Chapters 1–4) carries about **20 of 80 marks**. SSLC 2025 and 2026 each set three or four MCQs from this chapter. |
| Syllabus scope | Program and software; system and application software; language translators; utility software; operating system — definition, functions and types; CUI and GUI; UNIX and Linux |

> **Note on the text:** The prescribed Click Start 10 textbook was not available, and no CM IMPACT guidebook for Computer Science was found. This chapter is written from the MBOSE SSLC Computer Science papers of **2022 to 2026**, which show the topics and wording the board uses. Section 8.1 solves every question from those papers on this chapter.
>
> **Syllabus note:** The SSLC papers group this chapter under **Computer Fundamentals**, with Chapters 2–4.

---

## 1. Complete Lesson

### Hardware, programs and software

A computer has two parts that work together:
- **Hardware** — the physical parts you can touch: keyboard, monitor, CPU, printer.
- **Software** — the programs that tell the hardware what to do.

A **program** is a set of instructions written to carry out a particular task. **Software** is a collection of programs, together with the data and documentation (instructions for use) they need. For example, a calculator program is one program; an office suite such as Microsoft Office, with its word processor, spreadsheet and presentation programs and help files, is software.

### Types of software

Software is of two main types: **system software** and **application software**.

![Fig. 1.1 Types of software](figures/cs_ch01_fig01_software.png)

**1. System software** controls and manages the computer itself and provides a platform for other programs. It includes:
- the **operating system**;
- **language translators** (assembler, compiler, interpreter);
- **utility programs**;
- **device drivers**, which let the operating system work with hardware such as printers.

**2. Application software**, also called **end-user programs**, is used by people to do their own tasks.

- **General-purpose application software** can be used by many people for many jobs:
  - **word processors** — MS Word, Writer;
  - **spreadsheets** — MS Excel, Calc;
  - **presentation software** — PowerPoint, Impress;
  - **database software** — Oracle, MS Access, SQL Server, MySQL (MS Excel is a spreadsheet, not database software);
  - **desktop publishing (DTP)** — Adobe PageMaker, MS Publisher;
  - **multimedia software** — Adobe Flash, VLC Media Player;
  - **graphics software** — Adobe Photoshop, Paint.
- **Specific-purpose (customised) application software** is made for one particular job:
  - **payroll software** — calculates salaries and designs payslips as per a company's requirements;
  - **billing and accounting software** — prepares bills and keeps accounts (e.g. Tally);
  - **attendance system software** — records attendance; fingerprint and face-recognition devices have enhanced these systems;
  - **HR (human resource) management software** — keeps employee records, leave and recruitment;
  - **reservation system software** — books railway, airline or hotel tickets (e.g. IRCTC).

### Language translators

Computers understand only **machine language** (0s and 1s). Programs written in other languages must be translated by **language translators**:
- An **assembler** translates assembly language into machine language.
- A **compiler** translates the **whole program at once** into machine code, then lists all the errors together; the translated program runs fast. Example: the C++ compiler.
- An **interpreter** translates and executes the program **one line at a time**, stopping at the first error; it is slower. Example: BASIC, Python interpreters.

### Utility software

**Utility software** helps to **maintain, protect and optimise** the computer. Common utilities:
- **Antivirus** — detects and removes viruses (Chapter 13).
- **Backup utility** — makes copies of data so that it can be restored if the original is lost or damaged.
- **Disk defragmenter** — rearranges the scattered (fragmented) parts of files into continuous space, so the disk works faster. To **defragment** is to bring the pieces of each file together.
- **File compression utility** — reduces file size (WinZip, WinRAR, 7-Zip).
- **Disk checker** (CHKDSK, ScanDisk) — finds and repairs disk errors.
- **Disk cleanup** — removes unwanted temporary files.

### The operating system

An **operating system (OS)** is the system software that **manages all the hardware and software of a computer** and acts as an **interface between the user and the computer**. Without an operating system, a computer cannot be used. Examples: **MS-DOS, Microsoft Windows, UNIX, Linux, macOS, Android**.

![Fig. 1.2 Functions of an operating system](figures/cs_ch01_fig02_os_functions.png)

**Functions of an operating system:**
1. **Process management** — decides which program runs and for how long, and schedules tasks.
2. **Memory management** — **allocates memory** to applications at their request and **frees it** when it is no longer in use.
3. **File management** — creates, saves, copies, deletes and organises files and folders.
4. **Device (input/output) management** — controls devices such as the keyboard, printer and disk through device drivers.
5. **Resource management** — shares the processor, memory and devices among programs and users.
6. **Security** — protects data with passwords and user permissions.
7. **User interface** — lets the user give commands, by typing or by clicking.

### CUI and GUI operating systems

- A **CUI (Character User Interface)** operating system works by **typing commands** at a prompt. **MS-DOS** is purely CUI-based.
- A **GUI (Graphical User Interface)** operating system works with **icons, windows, menus and a mouse**. **Windows** and **macOS** are GUI-based; Linux offers both.

### Types of operating systems (by function)

![Fig. 1.3 Types of operating systems](figures/cs_ch01_fig03_os_types.png)

1. **Batch processing OS** — similar jobs are collected into batches and run one after another without user interaction. Jobs wait in a queue on disk until they can be run; this process of waiting for execution is called **spooling** (Simultaneous Peripheral Operations On-Line). Print queues also use spooling.
2. **Multi-user OS** — many users can use one computer at the same time from different terminals. **UNIX** is a **multi-user, multitasking** operating system.
3. **Multitasking / time-sharing OS** — runs several programs at once by giving each a small slice of processor time.
4. **Real-time OS** — **dedicated systems** in which tasks are **processed immediately**, within a fixed time; used in air-traffic control, missile guidance, medical machines and car brakes.
5. **Network OS** — runs on a server and manages **files, printers, users and security on a network**. Examples: Windows Server, Novell NetWare.
6. **Single-user, single-task OS** — one user runs one program at a time (MS-DOS).
7. **Mobile OS** — for smartphones and tablets (Android, iOS).

### UNIX and Linux

- **UNIX** is a powerful **multi-user, multitasking** operating system developed in **1969 at AT&T's Bell Laboratories** by Ken Thompson and Dennis Ritchie. It is widely used on servers.
- **Linux** is a free, **open-source, UNIX-like** operating system whose kernel was written by **Linus Torvalds in 1991**. Popular versions (distributions) include **Ubuntu**, Fedora and Debian. Linux can be used through commands typed in the **terminal** (Chapter 2) or through a GUI.

### Summary of the chapter

- Hardware is physical; software is programs with data and documentation. A program is a set of instructions for one task.
- System software (OS, translators, utilities, drivers) runs the computer; application software (end-user programs) does users' tasks — general purpose (word processing, spreadsheet, presentation, database, DTP, multimedia) or specific purpose (payroll, billing and accounting, attendance, HR, reservation).
- Translators: assembler; compiler (whole program at once); interpreter (line by line).
- Utilities: antivirus, backup, defragmenter, compression, disk checker, cleanup.
- OS: manages hardware and software, interface between user and computer. Functions: process, memory (allocates and frees), file, device, resource management, security, user interface.
- CUI (MS-DOS) vs GUI (Windows). Types: batch (spooling), multi-user (UNIX), multitasking, real-time (dedicated, immediate), network, single-user, mobile.
- UNIX (1969, Bell Labs); Linux (1991, Linus Torvalds; open source; Ubuntu).

---

## 2. Learning Objectives

After studying this chapter, you should be able to:

1. Distinguish between hardware, program and software.
2. Classify software as system or application software, with examples.
3. Explain the work of compilers, interpreters and assemblers.
4. Name common utility programs and their uses.
5. Define an operating system and list its functions.
6. Distinguish CUI and GUI operating systems.
7. Describe the types of operating systems, including batch, multi-user, real-time and network.
8. Describe UNIX and Linux.

---

## 3. Detailed Section Explanations

### Section 1 — Software and its types

System software runs the machine; application software serves the user. Specific-purpose software solves one business task.

**Exam focus:** "end-user programs" (SSLC 2026, Q1); payroll and attendance software (SSLC 2025–26); "Define software. What are its two types?" (SSLC 2023).

### Section 2 — Translators and utilities

Compilers and interpreters translate programs; utilities keep the computer healthy.

**Exam focus:** "interpreter vs compiler" (SSLC 2023); "functions of utilities", "defragment", "back-up utility" (SSLC 2022–24).

### Section 3 — The operating system

Its functions, its user interfaces and its types.

**Exam focus:** "memory management" and "real-time OS" (SSLC 2025); "four types of OS" (SSLC 2022); "network OS" (SSLC 2024); "Unix and Linux" (SSLC 2026).

---

## 4. Vocabulary (Key Terms)

| Term | Meaning | Example |
|---|---|---|
| hardware | physical parts of a computer | keyboard |
| program | set of instructions for a task | a calculator program |
| software | programs with their data and documentation | MS Office |
| system software | software that runs and manages the computer | Windows |
| application software | end-user programs for users' tasks | MS Word |
| language translator | converts a program into machine language | compiler |
| compiler | translates the whole program at once | C++ compiler |
| interpreter | translates and runs one line at a time | Python interpreter |
| utility software | programs that maintain and protect the computer | antivirus |
| defragment | bring scattered parts of files together | Disk Defragmenter |
| operating system | system software managing hardware and software; user interface | Linux |
| CUI | character user interface (typed commands) | MS-DOS |
| GUI | graphical user interface (icons, mouse) | Windows |
| spooling | jobs waiting in a queue for execution | print queue |
| real-time OS | dedicated OS that processes tasks immediately | air-traffic control |
| network OS | OS managing a network's resources | Windows Server |
| open source | software whose code is freely available | Linux |

---

## 5. Important Facts, Formulas and Results

### 5.1 Key facts

| Fact | Detail |
|---|---|
| End-user programs | application software |
| Designs payslips | payroll software |
| Fingerprint and face recognition enhanced | attendance system software |
| Not database software | MS Excel (a spreadsheet) |
| Adobe Flash | multimedia software |
| Allocates and frees memory | memory management |
| Dedicated systems, tasks processed immediately | real-time OS |
| Waiting of tasks for execution in batch processing | spooling |
| Purely CUI-based OS | MS-DOS |
| Multi-user, multitasking OS | UNIX |
| Linux kernel | Linus Torvalds, 1991; open source |

### 5.2 Compiler and interpreter

| Compiler | Interpreter |
|---|---|
| translates the whole program at once | translates one line at a time |
| lists all errors after compiling | stops at the first error |
| program runs faster | program runs slower |
| e.g. C, C++ | e.g. BASIC, Python |

### 5.3 CUI and GUI

| CUI | GUI |
|---|---|
| commands are typed | icons, menus, windows and mouse |
| harder for beginners | easy to learn |
| uses little memory | needs more memory |
| MS-DOS | Windows, macOS |

### 5.4 Beyond the text (general knowledge, not needed for exam answers)

- **Android**, based on the Linux kernel, is the most widely used operating system in the world, on phones.
- **BOSS Linux** (Bharat Operating System Solutions) is India's own Linux distribution, developed by C-DAC.

---

## 6. Person Profiles

### 6.1 Linus Torvalds (born 1969)

| Point | Detail |
|---|---|
| Who | Finnish-American software engineer |
| Known for | Wrote the Linux kernel in 1991 as a student, and made it free and open source |

### 6.2 Dennis Ritchie (1941–2011) and Ken Thompson (born 1943)

| Point | Detail |
|---|---|
| Who | American computer scientists at Bell Laboratories |
| Known for | Created UNIX (1969); Ritchie also created the C language, from which C++ grew |

---

## 7. Key Ideas and Real-Life Connections

### 7.1 Big ideas

- **Software brings hardware to life.** Without programs, a computer does nothing.
- **The OS is the manager.** It shares memory, processor and devices among programs.
- **Different jobs need different systems.** A missile needs a real-time OS; a school lab needs a network OS.

### 7.2 Real-life connections

- **IRCTC** rail booking is reservation software; your school's fee receipts may come from billing software.
- **Biometric attendance** machines in government offices in Meghalaya use attendance system software.
- **ATMs and traffic signals** run on real-time or embedded operating systems.

---

## 8. Exam-Oriented Questions

*Keep 2-mark answers within 30 words, 3-mark answers within 50 words and 5-mark answers within 80 words.*

### 8.1 Questions from the MBOSE SSLC papers (2022–2026) — solved

| Source | Question |
|---|---|
| MBOSE SSLC 2026, Q1 (1 mark) | Which one of the following is also known as end-user programs? |
| MBOSE SSLC 2026, Q2 (1 mark) | Which of the following designs the payslips as per a company requirement? |
| MBOSE SSLC 2026, Q31 (2 marks) | Define Unix and Linux. |
| MBOSE SSLC 2025, Q1 (1 mark) | It allocates memory to various applications at their request and frees the memory when not in use. |
| MBOSE SSLC 2025, Q2 (1 mark) | These are dedicated systems with immediately processed tasks. |
| MBOSE SSLC 2025, Q3 (1 mark) | Fingerprint and face recognition devices enhanced this system. |
| MBOSE SSLC 2025, Q6 (1 mark) | The process of waiting for task execution in batch processing. |
| MBOSE SSLC 2024, Q1(a) | Which is a multiuser, multitasking operating system? |
| MBOSE SSLC 2024, Q2(a) | What is a network operating system? |
| MBOSE SSLC 2024, Q2(b) | What is the use of a back-up utility? |
| MBOSE SSLC 2024, Q6(a) | Explain any four general-purpose application software. |
| MBOSE SSLC 2024, Q15(a) | State any two functions of an operating system. |
| MBOSE SSLC 2023, Q1(a) | Which of the following is not a database software? (Oracle / MS Access / MS Excel / SQL Server) |
| MBOSE SSLC 2023, Q2(a) | Define operating system. Give two examples. |
| MBOSE SSLC 2023, Q2(b) | Differentiate between interpreter and compiler. |
| MBOSE SSLC 2023, Q2(c) | What are the functions of utilities? |
| MBOSE SSLC 2023, Q6(a) | Define software. What are the two types of software? Explain in brief. |
| MBOSE SSLC 2023, Q15(b); 2022, Q16(a) | Differentiate between CUI and GUI (based operating systems, with one example each). |
| MBOSE SSLC 2022, Q1(a) | Which of the following is purely a CUI-based operating system? |
| MBOSE SSLC 2022, Q1(b) | Adobe Flash is an example of … |
| MBOSE SSLC 2022, Q2(a) | Differentiate between program and software. |
| MBOSE SSLC 2022, Q2(b) | What are language translators? |
| MBOSE SSLC 2022, Q2(e) | Define the term "defragment". Which utility is used to defrag files? |
| MBOSE SSLC 2022, Q6(a) | Explain any four different types of operating systems based on their functions. |

**Solutions**

**SSLC 2026, Q1.** **(B) Application software.**

**SSLC 2026, Q2.** **(B) Payroll software.**

**SSLC 2026, Q31.** **UNIX** is a multi-user, multitasking operating system developed at Bell Laboratories in 1969. **Linux** is a free, open-source, UNIX-like operating system created by Linus Torvalds in 1991 (e.g. Ubuntu).

**SSLC 2025, Q1.** **(C) Memory Management.**

**SSLC 2025, Q2.** **(D) Real Time Operating Systems.**

**SSLC 2025, Q3.** **(B) Attendance System Software.**

**SSLC 2025, Q6.** **(B) Spooling.**

**SSLC 2024, Q1(a).** **(ii) UNIX.**

**SSLC 2024, Q2(a).** A network operating system runs on a server and manages the files, printers, users and security of a network, letting computers share resources. Examples: Windows Server, Novell NetWare.

**SSLC 2024, Q2(b).** A backup utility makes copies of files and data on another drive or location, so that they can be restored if the originals are lost, deleted or damaged.

**SSLC 2024, Q6(a).** (i) **Word processor** (MS Word): to type, edit, format and print documents. (ii) **Spreadsheet** (MS Excel): to calculate and analyse data in rows and columns, with formulas and charts. (iii) **Presentation software** (PowerPoint): to make slide shows with text, pictures and animation. (iv) **Database software** (MS Access, Oracle): to store, organise and search large amounts of data. (Also DTP, multimedia.)

**SSLC 2024, Q15(a).** Memory management — allocating and freeing memory; file management — creating, saving and organising files (also process and device management, security).

**SSLC 2023, Q1(a).** **(iii) MS Excel** — it is a spreadsheet.

**SSLC 2023, Q2(a).** An operating system is system software that manages the computer's hardware and software and acts as an interface between the user and the computer. Examples: Windows, Linux.

**SSLC 2023, Q2(b).** A compiler translates the whole program into machine code at once and lists all errors together; the program then runs fast. An interpreter translates and executes one line at a time and stops at the first error.

**SSLC 2023, Q2(c).** Utilities maintain, protect and optimise the computer: scanning for viruses, backing up data, defragmenting disks, compressing files and checking and repairing disks.

**SSLC 2023, Q6(a).** Software is a collection of programs, with data and documentation, that tells the hardware what to do. **System software** manages the computer and provides a platform for other programs — the operating system, translators, utilities and drivers. **Application software** (end-user programs) does the user's tasks — word processors, spreadsheets, payroll and billing software.

**SSLC 2023, Q15(b); 2022, Q16(a).** A CUI OS is used by typing commands at a prompt; it is harder to learn but uses little memory — e.g. MS-DOS. A GUI OS is used through icons, windows, menus and a mouse; it is easy to learn but needs more memory — e.g. Windows.

**SSLC 2022, Q1(a).** **(ii) MS-DOS.**

**SSLC 2022, Q1(b).** **(iv) multimedia software.**

**SSLC 2022, Q2(a).** A program is a set of instructions for one task. Software is a collection of programs with their data and documentation, e.g. MS Office.

**SSLC 2022, Q2(b).** Programs that convert a program written in a programming language into machine language: assemblers, compilers and interpreters.

**SSLC 2022, Q2(e).** To defragment is to rearrange the scattered pieces of files on a disk into continuous space so that the disk works faster. The **Disk Defragmenter** utility is used.

**SSLC 2022, Q6(a).** (i) **Batch processing** — jobs are grouped and run one after another without user interaction, using spooling. (ii) **Multi-user** — many users share one computer at the same time (UNIX). (iii) **Multitasking / time-sharing** — several programs run at once by sharing processor time (Windows). (iv) **Real-time** — dedicated systems that process tasks immediately (air-traffic control). (Also network OS.)

### 8.2 More questions in the board's style — solved

**Q1.** Name two examples of system software.
**Answer:** Operating system (Windows) and a compiler (also utilities, device drivers).

**Q2.** Give two examples of specific-purpose application software.
**Answer:** Payroll software and reservation system software.

**Q3.** What is a device driver?
**Answer:** System software that lets the operating system communicate with a hardware device such as a printer.

**Q4.** Name two file compression utilities.
**Answer:** WinZip and WinRAR (also 7-Zip).

**Q5.** Which OS type is used in air-traffic control?
**Answer:** A real-time operating system.

**Q6.** Who wrote the Linux kernel, and when?
**Answer:** Linus Torvalds, in 1991.

### 8.3 More practice in the board's style

**Q1.** Fill in the blank: Application software is also known as ______ programs.
**Answer:** end-user.

**Q2.** Which translator converts assembly language into machine language?
**Answer:** An assembler.

**Q3.** What does the operating system do in memory management?
**Answer:** Allocates memory to applications on request and frees it when not in use.

**Q4.** What is spooling?
**Answer:** Placing jobs in a queue to wait for execution, as in batch processing and printing.

**Q5.** Name an open-source operating system.
**Answer:** Linux (e.g. Ubuntu).

### 8.4 High-probability exam questions

| Type | Question | Where answered |
|---|---|---|
| MCQ | end-user programs; payroll; attendance; memory management; real-time; spooling; UNIX multi-user; MS-DOS CUI; MS Excel not database; Adobe Flash multimedia | 9, 8.1 |
| 2 marks | OS with examples; program vs software; translators; network OS; backup utility; defragment; Unix and Linux | 10, 8.1 |
| 3 marks | compiler vs interpreter; CUI vs GUI; functions of utilities; functions of OS | 10, 8.1 |
| 5 marks | types of software; types of OS; general-purpose application software | 11, 8.1 |

---

## 9. MCQs with Explanations

*Some questions include "All of the above" or "None of the above" as an option, and it is sometimes the correct answer, so read every option carefully.*

### Software and its types (Q1–Q18)

**Q1.** Which one of the following is also known as end-user programs?
- (a) System software
- (b) Application software
- (c) Operating system
- (d) File compression utility

**Answer:** (b) Application software
**Explanation:** MBOSE SSLC 2026, Q1.

**Q2.** A set of instructions written to carry out a particular task is a
- (a) hardware device
- (b) program
- (c) port
- (d) cable

**Answer:** (b) program
**Explanation:** Software is a collection of programs with data and documentation.

**Q3.** The physical parts of a computer that we can touch are called
- (a) software
- (b) hardware
- (c) firmware updates
- (d) programs

**Answer:** (b) hardware
**Explanation:** Software cannot be touched.

**Q4.** Which of the following is system software?
- (a) MS Word
- (b) Operating system
- (c) Payroll software
- (d) A video game

**Answer:** (b) Operating system
**Explanation:** The others are application software.

**Q5.** Which of the following designs the payslips as per a company's requirement?
- (a) Billing and accounting software
- (b) Payroll software
- (c) Attendance system software
- (d) HR management software

**Answer:** (b) Payroll software
**Explanation:** MBOSE SSLC 2026, Q2.

**Q6.** Fingerprint and face-recognition devices have enhanced
- (a) reservation system software
- (b) attendance system software
- (c) HR management software
- (d) billing and accounting software

**Answer:** (b) attendance system software
**Explanation:** MBOSE SSLC 2025, Q3.

**Q7.** Which of the following is not a database software?
- (a) Oracle
- (b) MS Access
- (c) MS Excel
- (d) SQL Server

**Answer:** (c) MS Excel
**Explanation:** MBOSE SSLC 2023, Q1(a). MS Excel is a spreadsheet.

**Q8.** Adobe Flash is an example of
- (a) presentation software
- (b) DTP
- (c) compression utility
- (d) multimedia software

**Answer:** (d) multimedia software
**Explanation:** MBOSE SSLC 2022, Q1(b).

**Q9.** Software used to book railway or airline tickets is
- (a) a compiler
- (b) payroll software
- (c) DTP software
- (d) reservation system software

**Answer:** (d) reservation system software
**Explanation:** IRCTC is an example.

**Q10.** MS PowerPoint is an example of
- (a) presentation software
- (b) database software
- (c) an operating system
- (d) a utility

**Answer:** (a) presentation software
**Explanation:** It is general-purpose application software.

**Q11.** Software used to design newspapers, magazines and brochures is
- (a) an interpreter
- (b) payroll software
- (c) desktop publishing (DTP) software
- (d) a network OS

**Answer:** (c) desktop publishing (DTP) software
**Explanation:** E.g. Adobe PageMaker, MS Publisher.

**Q12.** A device driver is
- (a) an application for games
- (b) a person who drives a computer van
- (c) system software that lets the OS work with a hardware device
- (d) a type of virus

**Answer:** (c) system software that lets the OS work with a hardware device
**Explanation:** E.g. a printer driver.

**Q13.** Tally, used for preparing bills and keeping accounts, is
- (a) billing and accounting software
- (b) an operating system
- (c) a compiler
- (d) a web browser

**Answer:** (a) billing and accounting software
**Explanation:** Specific-purpose application software.

**Q14.** Software that keeps employee records, leave and recruitment details is
- (a) a defragmenter
- (b) multimedia software
- (c) an assembler
- (d) HR management software

**Answer:** (d) HR management software
**Explanation:** Specific-purpose application software.

**Q15.** MS Word is a
- (a) operating system
- (b) spreadsheet
- (c) database
- (d) word processor

**Answer:** (d) word processor
**Explanation:** General-purpose application software for documents.

**Q16.** Software is
- (a) a collection of programs with their data and documentation
- (b) only the keyboard and mouse
- (c) a single instruction
- (d) the electricity supply

**Answer:** (a) a collection of programs with their data and documentation
**Explanation:** SSLC 2022, Q2(a).

**Q17.** Which software is general purpose?
- (a) Hospital billing
- (b) Payroll
- (c) Railway reservation
- (d) Spreadsheet

**Answer:** (d) Spreadsheet
**Explanation:** Anyone can use it for many jobs.

**Q18.** Application software is used mainly to
- (a) translate programs
- (b) manage the hardware
- (c) do the user's own tasks
- (d) control memory

**Answer:** (c) do the user's own tasks
**Explanation:** Managing hardware and memory is the work of system software.

### Translators and utilities (Q19–Q30)

**Q19.** A program that translates the whole program into machine code at once is a/an
- (a) compiler
- (b) interpreter
- (c) assembler
- (d) editor

**Answer:** (a) compiler
**Explanation:** SSLC 2023, Q2(b).

**Q20.** A translator that executes a program one line at a time is a/an
- (a) interpreter
- (b) compiler
- (c) assembler
- (d) loader

**Answer:** (a) interpreter
**Explanation:** It stops at the first error.

**Q21.** Assembly language is converted into machine language by an
- (a) antivirus
- (b) interpreter
- (c) assembler
- (d) operating system

**Answer:** (c) assembler
**Explanation:** Compilers and interpreters handle high-level languages.

**Q22.** Compilers, interpreters and assemblers are together called
- (a) language translators
- (b) utilities
- (c) application software
- (d) device drivers

**Answer:** (a) language translators
**Explanation:** SSLC 2022, Q2(b).

**Q23.** The only language a computer understands directly is
- (a) Java
- (b) C++
- (c) machine language
- (d) English

**Answer:** (c) machine language
**Explanation:** It is made of 0s and 1s.

**Q24.** Rearranging the scattered parts of files on a disk into continuous space is called
- (a) formatting
- (b) compressing
- (c) defragmenting
- (d) spooling

**Answer:** (c) defragmenting
**Explanation:** SSLC 2022, Q2(e).

**Q25.** The utility used to defrag files is
- (a) Notepad
- (b) WinZip
- (c) Disk Defragmenter
- (d) Paint

**Answer:** (c) Disk Defragmenter
**Explanation:** SSLC 2022, Q2(e).

**Q26.** WinZip and WinRAR are
- (a) compilers
- (b) antivirus programs
- (c) operating systems
- (d) file compression utilities

**Answer:** (d) file compression utilities
**Explanation:** They reduce file size.

**Q27.** A back-up utility is used to
- (a) make copies of data so that it can be restored if lost
- (b) delete all files
- (c) speed up the internet
- (d) translate programs

**Answer:** (a) make copies of data so that it can be restored if lost
**Explanation:** SSLC 2024, Q2(b).

**Q28.** Utility software is used to
- (a) maintain, protect and optimise the computer
- (b) write letters
- (c) play films only
- (d) book tickets

**Answer:** (a) maintain, protect and optimise the computer
**Explanation:** SSLC 2023, Q2(c).

**Q29.** Which utility finds and repairs disk errors?
- (a) Disk Defragmenter
- (b) Disk checker (CHKDSK)
- (c) WinZip
- (d) Media Player

**Answer:** (b) Disk checker (CHKDSK)
**Explanation:** See also Chapter 2.

**Q30.** An antivirus program is a kind of
- (a) language translator
- (b) application software for payroll
- (c) utility software
- (d) hardware

**Answer:** (c) utility software
**Explanation:** See Chapter 13.

### The operating system (Q31–Q44)

**Q31.** System software that manages the hardware and software and acts as an interface between the user and the computer is the
- (a) operating system
- (b) word processor
- (c) compiler
- (d) printer driver

**Answer:** (a) operating system
**Explanation:** SSLC 2023, Q2(a).

**Q32.** It allocates memory to various applications at their request and frees the memory when not in use.
- (a) Process management
- (b) Resource management
- (c) Memory management
- (d) Utility management

**Answer:** (c) Memory management
**Explanation:** MBOSE SSLC 2025, Q1.

**Q33.** Deciding which program runs and for how long is
- (a) file management
- (b) process management
- (c) device management
- (d) security

**Answer:** (b) process management
**Explanation:** It schedules tasks on the processor.

**Q34.** Creating, saving, copying and deleting files is part of
- (a) file management
- (b) memory management
- (c) process management
- (d) spooling

**Answer:** (a) file management
**Explanation:** An OS function (SSLC 2024, Q15(a)).

**Q35.** Protecting data with passwords and user permissions is the OS function of
- (a) defragmentation
- (b) memory management
- (c) spooling
- (d) security

**Answer:** (d) security
**Explanation:** It protects data from unauthorised users.

**Q36.** Which of the following is purely a CUI-based operating system?
- (a) MS-Windows
- (b) MS-DOS
- (c) Linux
- (d) Mac OS

**Answer:** (b) MS-DOS
**Explanation:** MBOSE SSLC 2022, Q1(a).

**Q37.** GUI stands for
- (a) Graphic Utility Instrument
- (b) General User Input
- (c) Graphical User Interface
- (d) Global User Internet

**Answer:** (c) Graphical User Interface
**Explanation:** It uses icons, windows and a mouse.

**Q38.** In a CUI operating system, the user
- (a) touches the screen only
- (b) clicks icons with a mouse
- (c) speaks to the computer
- (d) types commands at a prompt

**Answer:** (d) types commands at a prompt
**Explanation:** CUI = Character User Interface.

**Q39.** These are dedicated systems with immediately processed tasks.
- (a) Multitasking operating systems
- (b) Batch processing operating systems
- (c) Time-sharing operating systems
- (d) Real-time operating systems

**Answer:** (d) Real-time operating systems
**Explanation:** MBOSE SSLC 2025, Q2.

**Q40.** The process of waiting for task execution in batch processing is
- (a) printing
- (b) spooling
- (c) scanning
- (d) remote terminals

**Answer:** (b) spooling
**Explanation:** MBOSE SSLC 2025, Q6.

**Q41.** Which is a multi-user, multitasking operating system?
- (a) MS Windows
- (b) UNIX
- (c) Linux
- (d) Mac OS

**Answer:** (b) UNIX
**Explanation:** MBOSE SSLC 2024, Q1(a) (Linux is UNIX-like, but UNIX is the expected answer).

**Q42.** An operating system that manages files, printers and users on a network is a
- (a) network operating system
- (b) real-time OS
- (c) single-user OS
- (d) batch OS

**Answer:** (a) network operating system
**Explanation:** SSLC 2024, Q2(a).

**Q43.** Running several programs at once by giving each a slice of processor time is
- (a) batch processing
- (b) multitasking (time-sharing)
- (c) defragmentation
- (d) compiling

**Answer:** (b) multitasking (time-sharing)
**Explanation:** Windows and Linux are multitasking systems.

**Q44.** Android and iOS are
- (a) databases
- (b) compilers
- (c) mobile operating systems
- (d) utilities

**Answer:** (c) mobile operating systems
**Explanation:** Android is based on the Linux kernel.

### UNIX and Linux (Q45–Q55)

**Q45.** UNIX was developed at
- (a) Microsoft
- (b) AT&T Bell Laboratories
- (c) Apple
- (d) Google

**Answer:** (b) AT&T Bell Laboratories
**Explanation:** In 1969, by Ken Thompson and Dennis Ritchie.

**Q46.** The Linux kernel was written by
- (a) James Gosling
- (b) Bill Gates
- (c) Steve Jobs
- (d) Linus Torvalds

**Answer:** (d) Linus Torvalds
**Explanation:** In 1991. (James Gosling created Java — Chapter 11.)

**Q47.** Linux is
- (a) a virus
- (b) a word processor
- (c) a free, open-source, UNIX-like operating system
- (d) a web browser

**Answer:** (c) a free, open-source, UNIX-like operating system
**Explanation:** SSLC 2026, Q31.

**Q48.** Ubuntu is a
- (a) Linux distribution
- (b) spreadsheet
- (c) virus
- (d) programming language

**Answer:** (a) Linux distribution
**Explanation:** Other distributions include Fedora and Debian.

**Q49.** Open-source software is software whose
- (a) only use is gaming
- (b) code is secret
- (c) price is very high
- (d) source code is freely available to use and change

**Answer:** (d) source code is freely available to use and change
**Explanation:** Linux is open source.

**Q50.** In Linux, commands are typed in the
- (a) printer
- (b) recycle bin
- (c) taskbar
- (d) terminal

**Answer:** (d) terminal
**Explanation:** See Chapter 2.

**Q51.** Which of these is NOT an operating system?
- (a) Linux
- (b) MS Excel
- (c) Windows
- (d) MS-DOS

**Answer:** (b) MS Excel
**Explanation:** It is a spreadsheet.

**Q52.** Which of the following offers both a CUI (terminal) and a GUI?
- (a) Linux
- (b) MS-DOS
- (c) a calculator program
- (d) MS Paint

**Answer:** (a) Linux
**Explanation:** MS-DOS is CUI only.

**Q53.** The creator of UNIX who also created the C language was
- (a) Tim Berners-Lee
- (b) Linus Torvalds
- (c) Dennis Ritchie
- (d) Charles Babbage

**Answer:** (c) Dennis Ritchie
**Explanation:** C++ grew out of C (Chapter 8).

**Q54.** Air-traffic control and missile guidance need a
- (a) DTP package
- (b) batch OS
- (c) word processor
- (d) real-time OS

**Answer:** (d) real-time OS
**Explanation:** Tasks must be processed immediately.

**Q55.** India's own Linux distribution, developed by C-DAC, is
- (a) BOSS Linux
- (b) Windows
- (c) macOS
- (d) Android

**Answer:** (a) BOSS Linux
**Explanation:** General knowledge, beyond the textbook.

---

## 10. Short-Answer Questions (2 and 3 marks)

### Very short answers (2 marks each)

**Q1.** Define operating system. Give two examples.
**Answer:** System software that manages hardware and software and is the interface between user and computer, e.g. Windows, Linux.

**Q2.** Differentiate between program and software.
**Answer:** A program is a set of instructions for one task; software is a collection of programs with data and documentation.

**Q3.** What are language translators?
**Answer:** Programs that convert a program into machine language: assemblers, compilers and interpreters.

**Q4.** What is a network operating system?
**Answer:** An OS on a server that manages a network's files, printers, users and security, e.g. Windows Server.

**Q5.** What is the use of a back-up utility?
**Answer:** It copies data to another location so it can be restored if the original is lost or damaged.

**Q6.** Define "defragment". Which utility is used?
**Answer:** Bringing scattered parts of files together into continuous space; Disk Defragmenter.

**Q7.** Define Unix and Linux.
**Answer:** UNIX: multi-user, multitasking OS from Bell Labs (1969). Linux: free, open-source UNIX-like OS by Linus Torvalds (1991).

**Q8.** State any two functions of an operating system.
**Answer:** Memory management (allocating and freeing memory); file management (organising files).

**Q9.** What is application software? Give two examples.
**Answer:** End-user programs for users' own tasks, e.g. MS Word and payroll software.

**Q10.** What is spooling?
**Answer:** Placing jobs in a queue on disk to wait for execution, as in batch processing or printing.

**Q11.** What is a real-time operating system?
**Answer:** A dedicated OS that processes tasks immediately, e.g. in air-traffic control.

**Q12.** What is system software?
**Answer:** Software that manages the computer and gives a platform for other programs, e.g. OS, utilities.

**Q13.** What is a device driver?
**Answer:** System software that lets the operating system communicate with a device such as a printer.

**Q14.** Name two specific-purpose application software.
**Answer:** Payroll software and attendance system software (also billing, HR, reservation).

**Q15.** What is a multi-user operating system? Give an example.
**Answer:** An OS that lets many users use one computer at the same time; UNIX.

**Q16.** What is utility software? Give two examples.
**Answer:** Software that maintains and protects the computer, e.g. antivirus and Disk Defragmenter.

### Short answers (3 marks each)

**Q17.** Differentiate between interpreter and compiler.
**Answer:** A compiler translates the whole program at once, lists all errors together, and the program runs fast. An interpreter translates and runs one line at a time, stops at each error, and is slower.

**Q18.** Differentiate between CUI and GUI with one example each.
**Answer:** CUI: commands are typed at a prompt; harder to learn; little memory — MS-DOS. GUI: icons, menus, windows and mouse; easy to learn; more memory — Windows.

**Q19.** What are the functions of utilities?
**Answer:** They maintain, protect and optimise the computer: scanning for viruses, backing up data, defragmenting disks, compressing files, and checking and repairing disks.

**Q20.** Explain any three functions of an operating system.
**Answer:** Process management schedules programs; memory management allocates and frees memory; file management creates, saves and organises files (also device management, security).

**Q21.** Distinguish between general-purpose and specific-purpose application software.
**Answer:** General-purpose software serves many users for many jobs (word processor, spreadsheet). Specific-purpose software is made for one particular job (payroll, reservation).

**Q22.** Write a short note on Linux.
**Answer:** Linux is a free, open-source, UNIX-like OS whose kernel Linus Torvalds wrote in 1991. Distributions include Ubuntu and Fedora, and it can be used through the terminal or a GUI.

**Q23.** What is batch processing? What is spooling?
**Answer:** Batch processing runs similar jobs together one after another without user interaction. Spooling is the queuing of jobs on disk to wait for execution.

**Q24.** Name three types of system software with one example each.
**Answer:** Operating system — Windows; language translator — C++ compiler; utility — antivirus (also device drivers).

**Q25.** What is payroll software? Name two other specific-purpose programs.
**Answer:** Payroll software calculates salaries and designs payslips as per a company's requirements. Others: billing and accounting software, and attendance system software.

**Q26.** Explain real-time and network operating systems.
**Answer:** A real-time OS is dedicated and processes tasks immediately (air-traffic control). A network OS runs on a server and manages a network's files, printers and users (Windows Server).

**Q27.** Why is an operating system essential?
**Answer:** It manages the hardware and all other programs, shares memory and devices, provides security, and gives the user an interface. Without it the computer cannot be used.

**Q28.** What do database, DTP and multimedia software do? Give one example of each.
**Answer:** Database software stores and searches data (MS Access); DTP designs publications (PageMaker); multimedia software plays or creates sound, video and animation (Adobe Flash).

---

## 11. Long-Answer Questions (5 marks each)

### Long answers (5 marks each)

**Q1.** Define software. What are the two types of software? Explain in brief.
**Answer:** Software is a collection of programs, with data and documentation, that tells the hardware what to do.
System software manages the computer and provides a platform for other programs.
Examples are the operating system, translators, utilities and drivers.
Application software (end-user programs) does the user's own tasks.
It may be general purpose (word processor, spreadsheet) or specific purpose (payroll, billing).

**Q2.** Explain any four different types of operating systems based on their functions.
**Answer:** (i) Batch processing: jobs are grouped and run without user interaction, using spooling.
(ii) Multi-user: many users share one computer at once (UNIX).
(iii) Multitasking or time-sharing: several programs run by sharing processor time (Windows).
(iv) Real-time: dedicated systems processing tasks immediately (air-traffic control).
(v) Network OS manages a network's files, printers and users.

**Q3.** Explain any four general-purpose application software.
**Answer:** (i) Word processor (MS Word): type, edit, format and print documents.
(ii) Spreadsheet (MS Excel): calculations and charts in rows and columns.
(iii) Presentation software (PowerPoint): slide shows with text, pictures and animation.
(iv) Database software (MS Access, Oracle): store, organise and search data.
Others include DTP (PageMaker) and multimedia software (Adobe Flash).

**Q4.** What is an operating system? Explain its functions.
**Answer:** An OS is system software managing hardware and software and acting as the user–computer interface.
Process management schedules programs; memory management allocates and frees memory.
File management organises files and folders.
Device management controls input/output through drivers.
Security protects data with passwords, and the user interface may be CUI or GUI.

**Q5.** What are utility programs? Describe any four.
**Answer:** Utility programs maintain, protect and optimise the computer.
(i) Antivirus: detects and removes viruses.
(ii) Backup utility: copies data so that it can be restored.
(iii) Disk Defragmenter: brings file fragments together to speed up the disk.
(iv) File compression (WinZip): reduces file size; a disk checker (CHKDSK) repairs errors.

**Q6.** What are language translators? Explain the three types.
**Answer:** Translators convert programs into machine language, the only language a computer understands.
An assembler converts assembly language into machine language.
A compiler translates the whole program at once and lists all errors; the program runs fast.
An interpreter translates and runs line by line, stopping at each error.
C++ uses a compiler; BASIC and Python use interpreters.

**Q7.** Describe any five specific-purpose application software.
**Answer:** (i) Payroll: calculates salaries; designs payslips.
(ii) Billing and accounting: prepares bills and keeps accounts (Tally).
(iii) Attendance system: records attendance, enhanced by fingerprint and face recognition.
(iv) HR management: employee records, leave, recruitment.
(v) Reservation system: books rail, air or hotel tickets (IRCTC).

**Q8.** Compare CUI and GUI operating systems, and describe UNIX and Linux.
**Answer:** CUI: commands typed at a prompt; little memory; MS-DOS.
GUI: icons, menus, windows and mouse; easy to use; Windows, macOS.
UNIX is a multi-user, multitasking OS from Bell Labs (1969).
Linux is a free, open-source UNIX-like OS by Linus Torvalds (1991).
Linux offers both a terminal (CUI) and a GUI, as in Ubuntu.

---

## 12. Competency / Application Questions

**Q1. (School office)** A school wants software to record teachers' attendance by fingerprint and to calculate their monthly salaries. Which two specific-purpose software are needed?
**Model answer:** Attendance system software (with a fingerprint device) and payroll software.

**Q2. (Slow computer)** A computer has become slow after years of saving and deleting files. Which utility should be run, and why?
**Model answer:** Disk Defragmenter, which brings the scattered parts of files together so that the disk reads them faster.

**Q3. (Choosing a translator)** A student wants to find all the errors in her C++ program at once. Which translator does C++ use, and why does this help?
**Model answer:** A compiler, which translates the whole program at once and lists all the errors together.

**Q4. (Hospital machine)** A heart-monitoring machine must respond instantly to changes. Which type of OS should it use?
**Model answer:** A real-time operating system, which processes tasks immediately.

**Q5. (Spot the error)** A student writes: "MS Excel is a database and MS-DOS is a GUI operating system." Correct it.
**Model answer:** MS Excel is a spreadsheet (Oracle and MS Access are databases); MS-DOS is a CUI operating system (Windows is GUI).

---

## 13. Assertion–Reason Questions

**Directions:** Read the Assertion (A) and the Reason (R). Choose the correct option:
- (a) Both A and R are true, and R is the correct explanation of A.
- (b) Both A and R are true, but R is **not** the correct explanation of A.
- (c) A is true, but R is false.
- (d) A is false, but R is true.

**Q1.**
**A:** A computer cannot work without an operating system.
**R:** The operating system manages the hardware and other programs.
**Answer:** (a)
**Explanation:** It is the manager and the interface.

**Q2.**
**A:** A compiler is slower than an interpreter at running a program.
**R:** A compiler translates the whole program at once.
**Answer:** (d)
**Explanation:** A compiled program runs faster; R is true.

**Q3.**
**A:** MS-DOS is a CUI operating system.
**R:** In MS-DOS, commands are typed at a prompt.
**Answer:** (a)
**Explanation:** Typing commands is what a character user interface means.

**Q4.**
**A:** Payroll software is general-purpose application software.
**R:** Payroll software designs payslips as per a company's requirement.
**Answer:** (d)
**Explanation:** It is specific-purpose software.

**Q5.**
**A:** Real-time operating systems are used in air-traffic control.
**R:** Real-time systems process tasks immediately.
**Answer:** (a)
**Explanation:** Air-traffic control cannot wait.

**Q6.**
**A:** Defragmenting a disk can make a computer faster.
**R:** It brings the scattered parts of files into continuous space.
**Answer:** (a)
**Explanation:** The disk head moves less to read a file.

**Q7.**
**A:** Linux is open-source software.
**R:** Linux was written by Linus Torvalds in 1991.
**Answer:** (b)
**Explanation:** Both true; who wrote it does not explain why it is open source.

**Q8.**
**A:** UNIX is a single-user operating system.
**R:** UNIX was developed at Bell Laboratories.
**Answer:** (d)
**Explanation:** UNIX is multi-user and multitasking.

**Q9.**
**A:** MS Excel is not database software.
**R:** MS Excel is a spreadsheet program.
**Answer:** (a)
**Explanation:** SSLC 2023, Q1(a).

**Q10.**
**A:** Spooling is used in batch processing.
**R:** In spooling, jobs wait in a queue for execution.
**Answer:** (a)
**Explanation:** SSLC 2025, Q6.

---

## 14. Case-Based Questions

*Read each passage and answer the four questions, 1 mark each (4 × 1 = 4).*

### Case 1 — The school office

> The office of a school in Tura uses one program to type letters, another to calculate marks in rows and columns, a fingerprint machine to record teachers' attendance, and another program that prints salary slips every month.

**(i)** What type of software is used to type letters?
**Answer:** A word processor (general-purpose application software).

**(ii)** Which software calculates marks in rows and columns?
**Answer:** A spreadsheet (MS Excel).

**(iii)** Name the software linked to the fingerprint machine.
**Answer:** Attendance system software.

**(iv)** Which software prints salary slips?
**Answer:** Payroll software.

### Case 2 — Behind the screen

> When Rina opens three programs together, her computer shares its processor among them, gives each the memory it needs, frees that memory when a program closes, and asks for her password at start-up.

**(i)** Which software performs all these jobs?
**Answer:** The operating system.

**(ii)** What is giving and freeing memory called?
**Answer:** Memory management.

**(iii)** What is sharing the processor among programs called?
**Answer:** Process management (multitasking).

**(iv)** Which function is asking for a password?
**Answer:** Security.

### Case 3 — Two translators

> Arjun's teacher showed two ways of translating a program. In one, the whole program was translated before running and all errors were listed together. In the other, each line was translated and run in turn, stopping at the first error.

**(i)** Name the first translator.
**Answer:** A compiler.

**(ii)** Name the second translator.
**Answer:** An interpreter.

**(iii)** Which program runs faster?
**Answer:** The compiled program.

**(iv)** What is the common name for both?
**Answer:** Language translators.

### Case 4 — Operating systems

> A bank's server lets hundreds of tellers work at the same time; a jet's flight computer must react instantly; and an old office PC runs only one program at a time through typed commands.

**(i)** What type of OS does the bank server need?
**Answer:** A multi-user (network) operating system.

**(ii)** What type of OS does the flight computer need?
**Answer:** A real-time operating system.

**(iii)** Name an OS like the old office PC's.
**Answer:** MS-DOS.

**(iv)** What type of interface does that PC use?
**Answer:** A CUI (character user interface).

---

## 15. Revision Notes

### Chapter at a glance
- Hardware (physical) vs software (programs + data + documentation); program = instructions for a task.
- System software: OS, translators, utilities, drivers. Application software = end-user programs: general (word processor, spreadsheet, presentation, database — Oracle, Access, SQL Server; not Excel — DTP, multimedia — Adobe Flash) and specific (payroll — payslips; billing and accounting; attendance — fingerprint and face; HR; reservation).
- Translators: assembler; compiler (whole, fast); interpreter (line by line).
- Utilities: antivirus, backup, Disk Defragmenter (defragment), compression (WinZip), CHKDSK, cleanup.
- OS: manages hardware and software; interface. Functions: process, memory (allocate and free), file, device, resource, security, UI.
- CUI (MS-DOS) vs GUI (Windows). Types: batch (spooling), multi-user (UNIX), multitasking, real-time (dedicated, immediate), network, single-user, mobile.
- UNIX (1969, Bell Labs, Thompson and Ritchie); Linux (1991, Torvalds, open source, Ubuntu).

### Common mistakes

| Mistake | Correct idea |
|---|---|
| MS Excel is database software | It is a **spreadsheet**. |
| MS-DOS is GUI-based | It is **CUI**-based. |
| A compiler translates line by line | That is an **interpreter**. |
| Payroll is general-purpose software | It is **specific-purpose**. |
| Spooling means printing | It means jobs **waiting in a queue**. |
| Linux was made by Microsoft | Linus Torvalds; open source. |

---

## 16. Chapter Test

**Class X · Computer Science · Computer Fundamentals Chapter 1: Software and Operating Systems**
**Time:** 1½ hours · **Maximum marks:** 40

**General instructions:**
1. Section A: multiple-choice questions; attempt all (10 × 1 = 10).
2. Section B: very short answers; answer any three of the four (3 × 2 = 6), in not more than 30 words each.
3. Section C: short answers; answer any three of the four (3 × 3 = 9), in not more than 50 words each.
4. Section D: long answers; answer any three of the four (3 × 5 = 15), in not more than 80 words each.

### Section A — Multiple-choice questions (10 × 1 = 10)

**1.** End-user programs are also known as
- (a) system software
- (b) application software
- (c) operating systems
- (d) utilities

**2.** Which designs payslips as per a company's requirement?
- (a) Payroll software
- (b) Billing software
- (c) HR software
- (d) Attendance software

**3.** Which is purely a CUI-based OS?
- (a) Windows
- (b) Mac OS
- (c) MS-DOS
- (d) Linux

**4.** Allocating and freeing memory is
- (a) process management
- (b) file management
- (c) device management
- (d) memory management

**5.** Dedicated systems that process tasks immediately are
- (a) real-time OS
- (b) batch OS
- (c) time-sharing OS
- (d) single-user OS

**6.** Which is not database software?
- (a) Oracle
- (b) MS Excel
- (c) MS Access
- (d) SQL Server

**7.** A multi-user, multitasking OS is
- (a) MS-DOS
- (b) UNIX
- (c) MS Word
- (d) Paint

**8.** The waiting of jobs for execution in batch processing is called
- (a) scanning
- (b) printing
- (c) spooling
- (d) compiling

**9.** A translator that converts the whole program at once is a/an
- (a) interpreter
- (b) assembler
- (c) editor
- (d) compiler

**10.** Adobe Flash is
- (a) multimedia software
- (b) DTP
- (c) a compression utility
- (d) presentation software

### Section B — Very short answers (answer any three: 3 × 2 = 6)

**11.** Define operating system. Give two examples.
**12.** Differentiate between program and software.
**13.** Define "defragment". Which utility is used?
**14.** Define Unix and Linux.

### Section C — Short answers (answer any three: 3 × 3 = 9)

**15.** Differentiate between interpreter and compiler.
**16.** Differentiate between CUI and GUI with one example each.
**17.** What are the functions of utilities?
**18.** Explain real-time and network operating systems.

### Section D — Long answers (answer any three: 3 × 5 = 15)

**19.** Define software. Explain its two types.
**20.** Explain any four types of operating systems based on their functions.
**21.** Explain any four general-purpose application software.
**22.** What is an operating system? Explain its functions.

---

## 17. Complete Answer Key

### 17.1 MCQ quick key (Section 9)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|---|---|
| 1 | b | 12 | c | 23 | c | 34 | a | 45 | b |
| 2 | b | 13 | a | 24 | c | 35 | d | 46 | d |
| 3 | b | 14 | d | 25 | c | 36 | b | 47 | c |
| 4 | b | 15 | d | 26 | d | 37 | c | 48 | a |
| 5 | b | 16 | a | 27 | a | 38 | d | 49 | d |
| 6 | b | 17 | d | 28 | a | 39 | d | 50 | d |
| 7 | c | 18 | c | 29 | b | 40 | b | 51 | b |
| 8 | d | 19 | a | 30 | c | 41 | b | 52 | a |
| 9 | d | 20 | a | 31 | a | 42 | a | 53 | c |
| 10 | a | 21 | c | 32 | c | 43 | b | 54 | d |
| 11 | c | 22 | a | 33 | b | 44 | c | 55 | a |

### 17.2 Assertion–Reason quick key (Section 13)

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | a | d | a | d | a | a | b | d | a | a |

### 17.3 Case-based quick key (Section 14)

| Case | (i) | (ii) | (iii) | (iv) |
|---|---|---|---|---|
| 1 | word processor | spreadsheet | attendance system | payroll |
| 2 | operating system | memory management | process management | security |
| 3 | compiler | interpreter | compiled program | language translators |
| 4 | multi-user / network | real-time | MS-DOS | CUI |

*Full answers are given under each question in Section 14.*

### 17.4 Chapter Test — answers and marking guide

**Section A (1 mark each)**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ans | b | a | c | d | a | b | b | c | d | a |

**Section B (2 marks each)**

**11.** Definition (1); two examples (½ each).
**12.** Program (1); software (1).
**13.** Meaning (1); Disk Defragmenter (1).
**14.** UNIX (1); Linux (1).

**Section C (3 marks each)**

**15.** Three points of difference (1 each).
**16.** CUI with example (1½); GUI with example (1½).
**17.** Any three functions (1 each).
**18.** Real-time (1½); network (1½).

**Section D (5 marks each)**

**19.** Definition (1); system software (2); application software (2).
**20.** Four types explained (1¼ each).
**21.** Four applications explained (1¼ each).
**22.** Definition (1); four functions (1 each).
