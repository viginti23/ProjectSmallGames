### **Project "Small Games"**

**Run**

You need to have Python3 installed (and preferably aliased to 'python').

Open your terminal/command line.\
Change directory to ProjectSmallGames folder.\
Type in: _python startProgram.py_\
Follow the instruction in the terminal/command line window.

**Short description**\

The application shows how much money random games of chances can make.

You can play the games as a guest user, however your scores will not be saved nor will you be able to build up your wallet when winning.

Registering as a user allows to use those functionalities and compare ones results with user's.



At the base there is a simple apps/games management system written in Python based on custom classes, the simplest database possible:
json data in a non-secured file.\
It supports registration, logging in and out, hashed password, administrators, top scores, money refill requests, flexibility 
and re-usability with creating a menu view.

The main structures are classes called "MenuNode" and its subclass "FuncNode".

**MenuNode**\
Used when creating a menu view with some options to choose from. Those options can either be
MenuNode, or a FuncNode.

**FuncNode**\
Used when we want to pass a function (or whole script) as an option in a menu view.


**Admin**\
To register as an admin, type in the password during the registration.
_admin_




Future ideas to implement:
- clean the code,
- user ID number,
- sending e-mails with confirmation of the user registration,
- add some ASCII animations,
- allowing admins to check the total register status,
- add more games (Hanoi?).
