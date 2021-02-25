import sys


class Node:
    def __init__(self, name, content, children=None, parent=None):
        self.content = content
        if children is None:
            self.children = {}
        self.parent = parent
        self.name = name

    def __repr__(self):
        return self.name

    def get_children(self):
        return self.children

    def add_options(self, *new_node):
        for node in new_node:
            self.children[len(self.children) + 1] = node
            node.parent = self

    def get_parent(self):
        return self.parent

    def set_parent(self, node):
        self.parent = node

    def get_content(self):
        if self.parent is not None:
            self.children[0] = self.parent
        return self.content

    def show_menu_view_and_go_next(self):
        content = self.get_content()
        children = self.children
        current_menu = self
        while True:
            try:

                # Add "Back" module to given menu, if there is a path to go back to, by choosing "0".
                if self.parent is not None:
                    content[0] = "|0| Back"
                    children[0] = self.parent

                # Add "Exit" module to every menu, by choosing "Q" or "q".
                content['Q'] = '|Q| Exit'
                for option in content:
                    print(content.get(option))

                user_choice = input("\nEnter characters to choose an option:\n")

                if user_choice.lower() == "q":
                    ans = input("\nAre you sure you are leaving?\nEnter Y or N.\n")
                    if ans.lower() == "y":
                        sys.exit()
                    else:
                        current_menu.show_menu_view_and_go_next()
                else:
                    user_choice = int(user_choice)

                next_node_content = children[user_choice]
                current_menu = next_node_content
                return next_node_content.show_menu_view_and_go_next()
            except ValueError:
                # if view[0]:
                #     print('You must input a valid number according to the menu displayed above')
                #     continue
                print('You must input a valid number according to the menu displayed above')
                continue

            except KeyError:
                # if view[0]:
                #     print('You must input a valid number according to the menu displayed above')
                #     continue
                print('You must input a valid characters according to the key menu displayed above.')
                continue
