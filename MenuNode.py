import sys
import time


class MenuNode:
    current_node = None
    default_node = None

    def __init__(self, name, content=None, options=None, parent=None):
        self.name = name
        self.content = content
        if self.content is None:
            self.content = {}
        self.options = options
        if options is None:
            self.options = {}
        self.parent = parent
        MenuNode.current_node = self

    def __repr__(self):
        return self.name

    def get_children(self):
        return self.options

    def add_options(self, *new_func_or_node):
        for func_or_node in new_func_or_node:
            self.options[str(len(self.options) + 1)] = func_or_node
            self.content[str(len(self.content) + 1)] = f'|{str(len(self.content) + 1)}| {func_or_node.name}'
            func_or_node.parent = self

    def get_parent(self):
        return self.parent

    def set_parent(self, node):
        self.parent = node

    def get_content(self):
        if self.parent is not None:
            self.options[0] = self.parent
        return self.content

    def printing_menu_view(self):
        for key in self.content.keys():
            print(self.content[key])

    def adding_back_module_to_parent_menu(self):
        # Adding "Back" module to given menu, if there is a path to go back to, by choosing "0".
        if self.parent is not None:
            self.content['0'] = "|0| Back"
            self.options['0'] = self.parent  # Always the first menu-node in self.options is a parent

    def adding_exit_module(self):
        # Adding "Exit" module to every menu, by choosing "Q" or "q".
        self.content['Q'] = '|Q| Exit'
        self.options['Q'] = sys.exit

    def get_users_choice_prompt(self):
        current = MenuNode.current_node
        current.adding_back_module_to_parent_menu()
        current.adding_exit_module()
        current.printing_menu_view()
        while True:
            choice = input("\nEnter characters to choose an option:\n")
            if choice in self.content.keys():
                return choice
            elif choice.lower() == 'q':
                ans = input("\nAre you sure you are leaving?\nEnter Y or N.\n")
                if ans.lower() == "y":
                    self.options["Q"]()
                    # sys.exit()
                else:
                    continue
            else:
                print("Please enter a valid option.")
                continue

    def show_menu_view_and_go_next(self):
        # Content is a dictionary of key:value pairs, paired <int from 0>:<str> e.g. for displaying views to users.
        # Other menu-nodes (views or functions) that we want to display on given <self> menu, we add to self.options.

        # Getting user's choice
        choice = self.get_users_choice_prompt()
        try:
            chosen_option = self.options[choice]
            MenuNode.current_node = self
            if callable(self.options[choice]):
                self.options[choice]()
            chosen_option.show_menu_view_and_go_next()
        except KeyError:
            print("Please choose from available options.")
