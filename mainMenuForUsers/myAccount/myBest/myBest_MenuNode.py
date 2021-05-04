from structures.menu_Node import MenuNode
from mainMenuForUsers.myAccount.myBest.myBest_script import my_bestTurtleRace, my_bestCoinFlip

content = {}

options = [my_bestTurtleRace, my_bestCoinFlip]

myBest_MenuNode = MenuNode("My Best", content=content, options=options)


