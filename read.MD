### **Project "Small Games"**

**Run**

You need to have Python3 installed (and preferably aliased to 'python').

Open your terminal/command line.\
Change directory to ProjectSmallGames folder.\
Type in: _python startProgram.py_\
Follow the instruction in the terminal/command line window.

**Short description**\
It is a simple apps/games management system written in Python based on custom classes, the simplest database possible:
json data in a non-secured file.\
It supports registration, logging in and out, hashed password, administrators, top scores, money refill requests, flexibility 
and re-usability with creating a menu view.

The main structures are classes called "MenuNode" and its subclass "FuncNode".

**MenuNode**\
Used when creating a menu view with some options to choose from. Those options can either be
MenuNode, or a FuncNode.

**FuncNode**\
Used when we want to pass a function (or whole script) as an option in a menu view.







Future ideas to implement:
- sending e-mails with confirmation of the user registration,
- allowing admins to check the total register status,
- adding best scores to Turtle Race,
- add more games (Hanoi?).
