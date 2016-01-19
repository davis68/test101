#   Introduction to Linux and Python

<!-- tags:  linux, bash, python, help, docs, piazza, relate, stackoverflow -->

<blockquote>
︎❖ *Objectives*:

1.  Learn to edit text files.

1.  Familiarize yourself with Linux, the command line, and the online Python environment.

1.  Learn how course policies will be applied with respect to labs and assignments.
</blockquote>

Welcome to Computer Science 101!  In this course, we will explore the fundamentals of computation as a tool for engineering.  As an engineer, you naturally will have recourse to mathematics, physics, and computation as core elements of your professional competence.  You will have the opportunity during your undergraduate experience to explore each of these fields and hone your abilities.  This course focuses on the computation component.

Why is this course—and the discipline itself—called computer "science"?  Well, a minimal definition of science could refer simply to the cyclical method of modeling–testing–revision that is practiced by scientists and engineers.  We expect you to carry out these three steps to solve problems using the machine, as well as to determine what you can do using computation.

Or, put another way, engineering is a process that uses *experiments* to derive *models* which inform *theory* which is then used to predict new *experiments*.  Computational thinking resides in the *modeling* portion of this cycle.

![](./img/cse-cycle.png)

For instance, you may wish to use past meteorological evaluations to predict future weather patterns.  You notice that temperature tends to be broadly cyclical, hotter near afternoon and colder near dawn.  This suggests using a periodic function like a sine wave to model the daily temperature cycle.  Thus a (very) simple model would simply take a collection of sine waves, determine how to best model past behavior (known historic temperatures) using this collection, and then express the resulting equation.  (This is the "model" step of the foregoing scientific method.)  Next, you would predict today's temperature pattern, see if the observations match up with the model, and quantify the resulting error (the "test" step).  Finally, you can revise this model by incorporating the new data, considering more kinds of known data, obtaining new types of data that you may think are relevant, and changing the underlying mathematics (away from just sines, perhaps)—the "revise" stage.

![](./img/temps.png)

This entire process is in principle doable by hand—but it would take hours or days to complete even one portion if any significant amount of data is involved.  Far better to use the computer to automate your calculation and make it both less prone to error and easier to revise.

Thus we can talk about computation as a core competency for the engineer or scientist.  But even more than this, we expect you to explore how the computer itself works—not just how to work on it.  If you have a question about what a particular method or expression does, then *try it out and see*!  The wonderful thing about the platform we will use for programming is that it very robustly handles your input, gives you reasonably helpful error messages if necessary, and can report results in a clean, easy-to-understand format.

The first portion of the course will be devoted to explaining the Python programming language and environment.  Python allows you to phrase specific mathematical expressions, like a calculator, but it enables so much more:  concisely expressing complex calculations, automating repetitive tasks to minimize human error and tedium, and representing results in tabular and graphical formats.

Today, you will start to explore Python and learn about the Linux computer system you will work in, as well as take a look at the sorts of exercises you will do in this course.  If you don't understand everything, or anything, in this lab today, then don't worry!  Just type in the code, and after the lectures of this week and next come back and check these pieces to see how they fit into your new understanding.

<blockquote>
In the interest of tuning lab lengths appropriately, we ask you to note the starting and ending time of each lab you turn in so you can report total time spent.  If you finish early, feel free to (appropriately!) help other students, continue to explore any asides on advanced topics, or clean up and leave early.
</blockquote>


##  Introduction to the Lab Environment

<blockquote>
︎❖ *Objectives*:

1.  Learn to edit text files.

1.  Familiarize yourself with Linux, the command line, and the Python environment.
</blockquote>


### Linux

There are two major operating system branches in personal computing today:  the Windows tradition and the Unix tradition.  The Unix tradition is more than forty years old, and represents a venerable and stable family of largely intercompatible systems including Linux and Mac OS X.  Because of the wealth of software development tools and the platform's ubiquity in high-performance computing and scientific computing, CS 101 will be conducted entirely in Linux.

Linux's popularity in scientific computing is derived from two benefits:  its access to the substantial collection of code already developed for the earlier Unix systems (and the subsequent ones as well); and its status as a *free software* platform.  (This second point means that everything—all code, all data, all programs—down to the source code is available for you to read and modify if you are so inclined.)

One of today's objectives is to get you more comfortable working in Linux.  To that end, we will guide you through the graphical interface and the command line interface so you can see what conventions to expect (and what's different from your prior experience with Mac or Windows machines).

<blockquote>
☞*Aside*:  *Asides* like this will provide or direct you to supplemental information that is *not required* for successful completion of this course, but will provide clarification, motivation, and further reading for students.  If you're pressed for time, you can safely skip asides.

You may hear the terms *Unix* and *Linux* being used interchangeably.  Unix proper refers to an operating system developed in 1972 at Bell Labs and its descendants and re-implementations<sup>[[Wikipedia](https://en.wikipedia.org/wiki/Unix)]</sup>.  Unix was widely successfully due to its locally minimalist, globally expansionist philosophy.  What I mean by this is that Unix prefers small simple programs which carry out one task and do it extremely well, but contains a multitude of such programs.

Linux has been developed as an independent project since 1991.  Linux largely reimplements Unix's functionality but with an *open source* policy of providing the source code to all features.  This openness has served it well in the computational science and scientific computing communities, who appreciated the ability to look inside of algorithms and thus verify numerics and algorithms.  (Due to its incorporation of the [GNU Project](https://gnu.org/)'s implementations of Unix tools, Linux is more properly but cumbersomely known as GNU/Linux.)
</blockquote>


#### Command Line (Initial Setup)

From the system task bar, select `Applications` and then `Accessories`.  Among the applications you can launch is listed ![](./img/icon-terminal.png) `Terminal`.  (In the future we will write this as `Applications→Accessories→Terminal`.  Also, this same icon may appear on your system task bar—if so, you can just click it there.)  If you click on this icon, the system will launch a window with an *instance* of the command line.  *Instance* here means an independent process or point of access to the system—you could open multiple instances as new windows by clicking the ![](./img/icon-terminal.png) `Terminal` icon repeatedly.

<blockquote>
☞*Aside*:  You will often hear the terms *shell*, *`bash`*, *terminal*, and *command line* used interchangeably for historic reasons.  The only point of confusion to be aware of is that the term *shell* is overloaded and can also refer to the Python interpreter.
</blockquote>

What you see of the command line is simple:  a short snippet indicating that you are in your home directory (which can always be referred to by the shorthand `~`) followed by the *prompt* `$`.  Anytime you see `$` followed by a cursor, the shell is waiting for you to provide a command for it to execute—a patient genie, but a pedantic one.

Right now, we're primarily interested in being able to:

-   Navigate the file system.
-   Open the Python interpreter.

That's it, and it doesn't take much to do either of those things.

However, there is a *one-time setup* step which your TA will now instruct everyone in.  (Please wait for the TA to cover this point before proceeding.)

    /class/cs101/etc/setup101

If you received a success message, then please continue.  If an error occurs, double-check your input; if it's okay, then please contact your TA for assistance.  You should also see a number of folders appear on your computer desktop called `lab1` through `lab13`—you will use these for your assignments.  You may now close this terminal window.


#### Editing Files

You will often need to edit files containing data or code for CS 101.  A text editor lets you enter and edit simple plain text, without formatting (like **bold** or *italic* text), and lets you save `.txt` files.  Please open the text editor called Gedit by selecting from the main toolbar `Applications→Accessories→Text Editor`.  Gedit will open with an empty text file.

For this lab, numbered questions are listed throughout each section.  You will answer the questions by typing (or copying and pasting) answers into this new empty text file.  At the conclusion of the lab, you will submit this file for grading.

1.  First, write your netid on a single line and save the text file in the `Desktop/lab1` directory as `lab1.txt`.  (This pattern will hold for later labs as well.)  Then type:
    
        1. hello cs 101
    
    as your answer to this first question.

Each question should be answered in the above format on subsequent lines.  For instance, if your netid were `rowlf` and your TA were Kermit the Frog, the first few lines of your lab file should look like:

    rowlf
    1. hello cs 101
    2. kermit_the_frog@illinois.edu
    3. 1
    4. -7
    5. 4

and so forth.  (Line 2 will contain a different email address.)  We recommend *saving frequently* and *keeping Gedit open while you work*.


#### Operations

Our policy in this class is that work should be completed on your own, although reference to outside materials and consultation with peers is acceptable *as long as it is clearly documented* and falls within acceptable parameters.  (More on this policy follows [below](#peer-assistance).)

-   **Lock Screen**.  Thus, while labs and MPs should be completed separately (and some lab work will be completed in pairs), you are not cut off from aid.  However, in order to keep your work secure and protect yourself against accusations of plagiarism, please take advantage of Linux's "Lock Screen" feature, found on the main toolbar at `System→Lock Screen`.  (You need report nothing for this question.)

-   **Take Screenshot**.  It will also be occasionally convenient for you to take a screenshot when answering questions.  To do this, from the main toolbar select `Applications→Accessories→Take Screenshot` (or press the `Print Screen` key).  (You need report nothing for this question.)

-   **Log Out**.  At the completion of your work, you should always log out of the system completely.  When you are ready to do so, from the main toolbar select `System→Log Out`.  (You need report nothing for this question.)

1.  **Teaching Assistants**.  You should have been introduced to the TA leading your lab section already.  Get their email address and report this.


#### The File System

You are probably familiar with Finder on a Mac or Windows Explorer on a Windows machine.  Both of these are simply portals onto the file system, allowing you to locate files according to a logical hierarchy of folders (like "Documents" or "Music").  Linux has a number of similar portals available; here we will examine one that will be occasionally useful to you.

Along the top bar of your computer desktop, a list of menus appears.  This is the system task bar.  One of the menus reads `Places`.  Click this, and a list of directories on the file system appears.  Select (and click) `Home Directory`.

A Navigator window appears.  This Navigator window (intuitively) refers to your home directory.  This is analogous to the `/Users/name` directory on a Mac and the `C:\Users\name` directory on Windows.

Select the `Desktop` directory.  Among a few other files which are possibly present, you should see a list of directories from `lab1` to `lab13`.  These will be the directories you will work in for each lab throughout the semester.

You can select different directories or folders (we'll use these words interchangeably) in the left-hand sidebar, or just explore the directories you see in the window now as well.  When you are finished, you can close the Navigator window.


### Command Line (Revisited)

Open a new terminal window.  Although the command line is extremely powerful and a bit cryptic, we only need a little bit of its potency right now.  We're primarily interested in being able to:

-   Navigate the file system via text commands.
-   Open the Python interpreter.

That's it, and it doesn't take much to do either of those things.


#### Navigate the File System

Just as before when we opened Navigator, we start in the `/home/netid` directory.  If at any time you get lost and need to reset the commands, you can type `cd` by itself, which stands for *c*hange *d*irectory—in this case, back to your home directory.

`cd` generally lets you change directories either *absolutely*—when you know exactly where on the file system you want to go—or *relatively*—when you need to go to a child or sibling directory.

Since we're currently in the home directory, let's move our shell prompt to the desktop.  Type

    cd Desktop

Your prompt's logical location is now the `Desktop`, just as if you had navigated there in Navigator.

Now move into the directory for today's lab, `lab1`:

    cd lab1

That's it—this is the basic process you should use for each lab exercise.  If you need to go back up to the `Desktop` directory, type `cd -` to return to the last directory you were in.  A [reference for the shell](http://mywiki.wooledge.org/BashGuide) is available (actually, many are), but you shouldn't need anything more than `cd` for this class.  Your TA can assist you if any part of this process doesn't work properly.

You're now ready to open Python.

<blockquote>
☞*Aside*:  All major operating systems have their own version of the command line, which provides an alternate access point to the system.  (Windows actually has two:  command.exe and PowerShell.)

One advantage of using a command-line shell is that tasks can be stored as a list of consecutive actions, or *script*; consider trying to store a set of mouse movements to reproduce some actions in your graphical environment.  It would be too difficult to generalize!  With scripts, you can automate repetitive or common tasks, reducing time spent and the likelihood of making mistakes.  We will discuss scripting with Python, but it is equally possible with the shell (although often for different applications).
</blockquote>


### Python Interpreter

At the command line prompt, type

    python

After some preamble, the Python prompt appears, `>>>`.  Just as with the command line, Python also awaits your instructions.

There are two ways to execute programs in Python.  In the first place, you can simply type in code line-by-line and have it immediately evaluated—that is, the result of any expression is returned to you as output.  Alternatively, you can collect a bunch of these statements, logically organized, into a *script* which can be used to automate repetitive tasks (or just make them more reliable than typing them in by hand every time would be).  We are going to work interactively in Python today.


#### Numbers and Expressions

At this point, you can consider Python a straightforward calculator.  We will begin by simply considering numbers.

1.  `1`
1.  `-7`
1.  `4`
1.  `+9`
1.  `4.5`
1.  `3.1415`
1.  `-0.0001`
1.  `1.`
1.  `1e5`  (Exponential notation, equivalent to $1\times 10^{5}$)
1.  `1.564e15`
1.  `1.54643e-4`

Expressions are more complicated statements composed of values (like numbers) and operators (like addition $+$).

Try the following expressions and report the results.

1.  `1 + 1`
1.  `100000 + 1`
1.  `7.5 / 1.25`
1.  `867-5309`
1.  `7 ** -2`
1.  `3 ** 3`
1.  `16 % 7`  (This is the *modulus* operator, or the remainder after division.)
1.  `(2 * -5) + 7`
1.  `16.0 / 3`
1.  `divmod(16,3)`  (What does this expression do?  Try a few numbers and figure it out.  However, only report the result of this expression.)
1.  `8*9+10`
1.  `8*(9+10)`
1.  `abs(10)`
1.  `abs(-7.25)`
1.  `-(-8)`
1.  `1 + 4 * 5`
1.  `(1 + 4) * 5`

Variables are ways of storing the results of past calculations with a reusable label—we'll use them more next week.  Try the following:

    a = 5
    b = 3

What is the result of:

1.  `a*b`
1.  `-a**b`
1.  `a * 4*b`
1.  `a / b + a * b`

Simple (and complicated) mathematical expressions can carry out calculations for you, but how do you see the resulting data?  You require explicit *output*, which really encompasses anything that the program produces for the user—these can be files, graphs, or tables.  Basic text output is typically handled using the `print` statement:

1.  `print 3+4`
1.  `print a*b, a/b`

(The result doesn't look much different from what you saw a moment ago with expressions, but that's because the interpreter always outputs the results of simple expressions if you don't tell it what to do with the result otherwise.)

But you may want to output a message as well.  In this case, just typing the following will fail:

    print hello world

(Go on, try it.  We'll wait.)

What happens here is that the Python interpreter can't distinguish between *text you write as commands* and *text you write as messages*.  We can circumvent this problem by wrapping our messages in quotation marks.  To do this, press the up arrow once on your keyboard; this will show the last command typed, which can save a lot of time.  Use the arrow keys to go back and forth, and add quotation marks to the statement:

1.  `print 'hello world'`

The interpreter understands quoted text as special, like a slip of paper with words written on it).  When you run *this* command, Python responds by carrying out the command to *print* the *message* it was handed.  This quoted message is called a *string*, and we'll explore it further in future lectures and labs.

1.  Close Python by typing `exit`.  What is the result?  Now close Python for real.  We'll use it later today, but you can open it again by typing `python` at the command prompt when necessary.  (Answer this question with the result of typing just `exit`.)

You can tell that Python has closed because the prompt changes from `>>>` to `$`.


##  Getting Help

<blockquote>
︎❖ *Objectives*:

1.  Learn how to use documentation and online resources to answer questions.

1.  Learn how course policies will be applied with respect to labs and assignments.
</blockquote>

Let's suppose that you are working on a project in a few months' time.  During the course of revising your teammate's code, you run across an obscure function that she's written using the keyword `pass`.  As she is not on hand to answer your question, and has gone mysteriously radio silent on text, you are thrown back onto your own resources to interpret this keyword.

Now, in this situation you can always just google `python pass keyword`, of course, but not all sources of information are going to be of equal value to you.  We suggest that the first two places you should generally look for help are [the Python documentation](https://docs.python.org/3/index.html) and [Stack Overflow](https://stackoverflow.com/questions/tagged/python).  Questions that are not trivially resolved through those means can be asked directly to TAs on-duty in your lab or via the Piazza forum (discussed below).


### Piazza

A major component of this course will be the message forum hosted in Piazza.  You will use this as a question-and-answer platform to get feedback

-   Make sure that you've received the email and activated your Piazza account.

-   Enroll in the [Piazza CS 101](piazza.com/illinois/fall2015/cs101) course (if you are not already enrolled automatically).

-   Find the thread "Welcome to CS 101".  Add a short note replying to that thread—"hello everyone" or something like that.


### Python Interpreter Documentation

Functions are commands which take a few values of input and process these values (like `sin(4.5)` for $\sin(4.5)$).  Functions generally have short explanatory paragraphs describing their use within Python.  These descriptions are easy to access and generally easy to understand—simply type in `help(function_name)`, where `function_name` is the function you are interested in.  Try it:

1.  Type `help(abs)` into Python.  A separate page appears, describing how to use the built-in `abs` absolute value function; *i.e.*,
    
    $$ |x| = \left\{ \begin{array}{lr} -x & : x < 0 \\ x & : x \geq 0 \end{array} \right. \text{.}$$

    What is the descriptive text following `Return the`?  (Now press `q` to leave the dialog window and return to the Python interpreter.)  Try `abs(5)` and a few other numbers (negative and positive).

1.  What is the last line of text of the docstring shown by invoking `help(oct)` (without preceding spaces)?

1.  What is the last line of text of the docstring shown by invoking `help(min)` (without preceding spaces)?

1.  A major use of this feature is to learn how to effectively use library functions.  For instance, let's take a look at the hyperbolic tangent $\tanh$ (pronounced "tanch") from the `math` module:
    
        from math import tanh
        help(tanh)
    
    What is the last line of text in this help message (without preceding spaces)?

1.  While the foregoing help messages were all very short, others are quite involved.  Type
    
        help(int)
    
    to see Python's discussion of the integer data type `int`.  Scroll all the way to the bottom using the down arrow key.  What is the text of the last line (*i.e.*, don't include the `|` and preceding spaces, just the `T.__new__` etc.)?

1.  Try to ask Python for `help` with operators:  `help(*)`.  What is the output (four lines)?
    
    This happens because Python isn't sure whether to treat your `*` as an operator (*i.e.*, should it try to multiply `help(` by `)`, which is meaningless?) or as some sort of function.  So `help` isn't good for everything, but it can get you squared away particularly when you know a feature exists and are just trying to remember the right way to use it.


### Python Online Documentation

The [Python documentation](https://docs.python.org/2/index.html) contains descriptions of the standard Python language (keywords like `is` and `print`; syntax like `a=1`) as well as of many useful libraries.  While fairly technical, the documentation often includes code examples which demonstrate the keyword under consideration.

For instance, navigate to [the page on numeric types](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex).  While the text is fairly technical (although we'll discuss this topic in this week's lecture), useful features like a table of operators and their definitions is included.

1.  Somewhere in the page on numeric types is a brief table entry on `math.ceil(x)`.  What is the corresponding text in the Results column?  (Copy it into your answer for this question.)

1.  Immediately below that section is a line about seeing the `math` and `cmath` libraries.  Click through to the `math` library.  A more comprehensive description of `math.ceil(x)` is included there; copy the complete text for that entry (two sentences) as your answer for this question.

1.  Find the entry (on the `math` module page) for `math.pi`.  What is the complete text for that entry?

1.  Now return to the Python interpreter.  Type:
    
        from math import pi
        print pi
    
    The first line tells your Python interpreter about the variable `pi`.  The second—well, what is the result of executing this code snippet?

1.  Search the documentation for `pass statements`.  How many results did you get?

1.  Click on the first result, "4. More Control Flow Tools".  (Note that the text you previously searched for is highlighted.)  Search for the text `pass statements` within this page.  What is the first sentence describing the `pass` statement in the paragraph of text?

1.  Return to the main documentation page.  There is a section on "Installing Python Modules".  (Although we will rarely (if ever) need to do this on these machines, if you have any intent to use Python yourself you will need to know how to add new libraries or modules to your environment.  We will cover this process in a later lab—for now we just want you to know how the documentation works.)
    
    Click into that page and find the text `Basic usage`.  Some text and then a code block are listed below that heading (actually, several are located there), indicated by a `monospaced` typeface and a light green background.  What is the content of the first code block under this heading?

1.  Return to the main documentation page.  Click into the "FAQs" page, and then the "General Python FAQ".  Find the question on "Is Python a good language for beginning programmers?".  Read this section (and don't worry if some of it is too technical to understand now!), and then answer this question with the complete text of the last paragraph before the code block.

Please be careful throughout this course, however, that when you search for Python documentation you are consulting the Python **2** documentation.  In the address bar, the URL should begin with this:

    http://docs.python.org/2/...

<a id="2to3"></a>
<blockquote>
☞*Aside*:  Python gradually changes and evolves.  Mostly, this is in the direction of adding new features or removing difficult and obscure components added a decade or more ago.

You will find many references to Python 2 *v.* Python 3 online.  In this course, we will use Python 2.  For *most* purposes, the version doesn't matter, although there are some subtleties.  You won't need to worry about this at all in this class, and likely never during your undergraduate experience.

If you *do* end up needing to know more, start with [PietersND](#PietersND).  More advanced resources include [Python2014](#Python2014) and [Regebreo2015](#Regebro2015).

-   <a id="PietersND">PietersND</a>:  M. Pieters, [Python 2.7 vs Python 3.4—What should Python beginners choose?](https://www.codementor.io/python/tutorial/python-2-7-vs-python-3-4), n.d.

-   <a id="Python2014">Python2014</a>:  Python team, ["Should I use Python 2 or Python 3 for my development activity?"](https://wiki.python.org/moin/Python2orPython3), 2014.

-   <a id="Regebro2015">Regebro2015</a>:  L. Regebro, [*Porting to Python 3* (2015)](http://python3porting.com/toc.html), 2015.
</blockquote>


### Stack Overflow

Stack Overflow is a community-driven question-and-answer site, in which people ask challenging or obscure questions and others attempt to answer these questions correctly in competition for points.  Of course, you are not guaranteed that any particular answer is accurate, but with thousands of eyes on the site, the likelihood of any error going uncontested is low.

![](http://imgs.xkcd.com/comics/duty_calls.png)

(Although you can create a user account on SO if you wish to contribute, we certainly do not require that for this course.  You may find it useful if you wish to vote for answers which have helped you at SO.)

As SO has been around for several years, most questions that beginning users will ask have already been posed.  Feel free to consult SO for clarification of how elements of Python work, or how to solve a problem "Pythonically" (that is, in the manner best suited to Python syntax and features).  Just make sure that any usage is cited in accordance with the class policy on plagiarism—this includes code snippets!

1.  What is the user name of the original asker of the question "How to use the `pass` statement in Python?" on SO?

1.  Who gave the second-most popular answer?

1.  Find the question "In Python, check if a directory exists and create it if necessary" on SO (the title is verbatim, and asked originally by the user Parand).  Fill in the blank from that question to answer this question:  "Somehow, I missed _________ (thanks, kanja, ...".

1.  Go to the [Python tag page](https://stackoverflow.com/questions/tagged/python).  Next to the heading "Tagged Questions", there are several options for sorting.  Sort by "Votes".  What is the second most popular question to date regarding Python?

1.  Sort by "Newest".  What is the newest question?

1.  What is the newest question with an answer?

1.  Find the question "Is it possible to get a list of keywords in Python?".  The first answer has (of course) a solution in the grey code block.  There are two commands listed there, with output.  Run these two commands in your Python interpreter.  Your list may be slightly different from that given in the answer, as Python gradually changes (see the <a href="#2to3">aside above on Python 2 v. 3</a> if you're interested in knowing more).  Report your list.


<!--
### Other Online Resources

-   [Code.org](code.org/learn) has a number of simple tutorials for coding.  While the general tone is often aimed at a 9–12 audience (or younger), there are valuable tutorials there which can clarify key conceptual topics.

-   The [UIUC subreddit](https://www.reddit.com/r/UIUC) often has question and answer threads discussing courses such as CS 101.  While it would be inappropriate to seek help for an MP or lab, you can use this resource to discuss more about the course and its relationship to majors and the university.
-->


<a id="peer-assistance"></a>

### Peer Assistance

Finally, you can always ask others for help.  What is the appropriate amount of help to request (or offer)?

The line we must walk lies between having you perform all work in total isolation (no help being permitted from outside sources beyond the TAs and professors) and thus tempting you to plagiarize work due to excessive pressure to perform in a certain way; and having you freely copy and use others’ work without regard to its source.  Both of these extremes are highly undesirable.

Our philosophy in this course is based on the fact that (in real life) most of the time you have access to many resources:  websites, peers, mentors, books, and others' source code.  Your competence will be greatly increased by the resources you can use without recourse to external references, but when learning it only makes sense to let you function in a realistic manner.  Thus, for lab exercises and homework, you should work alone unless told otherwise, but you may consult outside sources of information as long as you (1) do not copy that source's work verbatim (*i.e.*, write your own code!); and (2) cite all sources used and the contribution they made to your work.  This policy is designed to protect you against plagiarism without being *carte blanche* to skip doing the work yourself.

So what is plagiarism?  The university defines it thusly:
<blockquote>
Plagiarism is using others' ideas and/or words without clearly acknowledging the source of that information.  Students may plagiarize very deliberately (e.g., copying or purchasing papers from an online source), or they may not realize what they are doing, which is sometimes the case when students fail to give credit for authors' ideas that they have paraphrased or summarized in their own words.<sup>[[Illinois2014](#Illinois2014)]</sup>
</blockquote>

1.  What is the first heading on the academic integrity page (*i.e.*, "Definition of ______")?

We won't enforce formal citation rules:  it's enough for you to say something like:

    Stack Overflow (stackoverflow.com/questions/890128/python-lambda-why) to clarify use of "lambda" keyword
    
    101 classmate Cho Chang explained ravenclaw library
    
    TA Stan Shunpike allowed consultation of his "get_bus_velocity()" function

Semiliterate responses on the order of

    cho chang

are not acceptable as they do not specify the information you obtained.

What about using books or the better class of programming website?  Again, make sure that you don't copy the source's code verbatim and that you cite the work and its contribution.

Pair exercises need not include a note about peer consultation.

-  <a id="Illinois2014">Illinois2014</a>:  [Academic integrity and plagiarism](http://www.library.illinois.edu/learn/research/academicintegrity.html)


##  In Conclusion

A couple of final policies you should be aware of:

-   The labs collectively constitute 25% of your grade in CS 101.  Although they will gradually increase in difficulty, you should be able to complete the lab exercises in the two-hour period allotted to you.  Today’s lab is worth 1% of your overall grade; the subsequent twelve labs each contribute 2% to your overall grade.

-   A corollary policy is that you should always attend your assigned lab section.  Attendance and submission of your work will be graded on that basis, and *failure to attend the proper section in which you are enrolled will lead to a grade of zero* on that lab.

1.  How long did this lab exercise take you to complete (in minutes)?
1.  Which questions, if any, were unclear?
1.  Cite any consultations or references required to complete your work.

Finally, you can close and save the text file containing your homework.  (It is important that you name files properly, as the TAs will be checking only the files you have been assigned to create.)  Make sure that this file is saved with the name `lab1.txt`, and ensure that it has been saved inside of the `lab1` folder on your `Desktop`.  (Feel free to open the Navigator and double-check.)  Then open a new command line window and type the following commands:

    cd
    cd Desktop
    submit101 AYA lab1

where instead of `AYA` you should type your actual section.  (Your TA will know the section if you do not.)  The script will list the files which are being submitted as well as the time stamp; confirm that these are correct.  If these are wrong, please immediately let your TA know.  Additionally, if an error message appears, simply make the adjustments it requests and check your typing.

Don't forget to log out after you submit your text file.  See you next week!

<!-- A.M.D.G. -->