import sys
import time
from user import User


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
        if not parent:
            self.parent = MenuNode.current_node

    def __repr__(self):
        return self.name

    def __call__(self):
        return self.run()

    def get_options(self):
        return self.options

    def get_parent(self):
        return self.parent

    def set_parent(self, node):
        self.parent = node

    def get_content(self):
        return self.content

    def add_options(self, *new_func_or_node):
        for func_or_menu_node in new_func_or_node:
            self.options[str(len(self.options) + 1)] = func_or_menu_node
            self.content[str(len(self.content) + 1)] = f'|{str(len(self.content) + 1)}| {func_or_menu_node.name}\n'
            func_or_menu_node.parent = self

    def adding_back_module_leading_to_parent_menu(self):
        # Adding "Back" module to given menu, if there is a path to go back to, by choosing "0".
        if self.parent:
            self.content['0'] = "|0| Back"
            self.options['0'] = self.parent  # Always the first menu-node in self.options is a parent

    def adding_exit_module(self):
        # Adding "Exit" module to every menu. Action by choosing "Q" or "q".
        self.content['Q'] = '|Q| Exit'
        self.options['Q'] = sys.exit

    def printing_menu_view(self):
        # If any user is logged in, we are displaying their username on the top of each menu view.
        if User.user_logged:
            print(f'\n\n\nUser: {User.user_logged}\n')
            print(f"{MenuNode.current_node.name}")
        # Current's node name
        else:
            print(f'\n\t{MenuNode.current_node.name}\n{25 * "-"}')

        print(f"{25 * '-'}")
        for key in self.content.keys():
            print(self.content[key])
        print(f"{25 * '-'}")

    def get_users_choice_prompt(self):
        current = MenuNode.current_node
        current.adding_back_module_leading_to_parent_menu()
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

    def run(self):
        # Content is a dictionary of key:value pairs, paired <int from 0>:<str> e.g. for displaying views to users.
        # Other MenuNodes (views) or FuncNodes (scripts/functions) that we want to display on given <self> menu,
        # we add to self.options.
        MenuNode.current_node = self
        # Getting user's choice
        choice = self.get_users_choice_prompt()
        try:
            chosen_option = self.options[choice]
            self.options[choice].parent = self
            if callable(self.options[choice]):
                self.options[choice]()
            chosen_option.run()  # recursive call to the next menu
        except KeyError:
            print("Please choose only from available options.")
