import sys
import time
from structures.user_class import User


class MenuNode:

    default_node = None

    current_node = None
    previous_node = None

    def __init__(self, name, content=None, options=None, main_menu=False):
        self.name = name

        self.content = content
        if not self.content:
            self.content = {}

        self.options = options
        if not options:
            self.options = {}

        self.main_menu = main_menu
        # if MenuNode.current_node:
        #
        # self.parent_up = parent_up
        # if self.parent_up is None:
        self.parent_up = None

    def __repr__(self):
        return self.name

    def __call__(self):
        return self.run()

    def get_options(self):
        return self.options

    def get_content(self):
        return self.content

    def add_options(self, *new_func_or_node):
        for func_or_menu_node in new_func_or_node:
            self.options[str(len(self.options) + 1)] = func_or_menu_node
            self.content[str(len(self.content) + 1)] = f'|{str(len(self.content) + 1)}| {func_or_menu_node.name}\n'
            func_or_menu_node.parent_up = self

    def adding_up_module_leading_to_parent_menu(self):
        # Adding "Up" module to given menu, if there is a path to go back to, by choosing "0".
        if self.parent_up:
            self.content['0'] = "|0| Up"
        # The very first menu-node in self.options is always a parent_up.
            self.options['0'] = self.parent_up
        # Back (previous) menu is more structural, general state of the system just as current_node and
        # default_node are, and might be needed in global scope use. Also every node's mandatory argument
        # for instantiation is parent_node argument, except for MainMenu and MainMenuForUsers
        # (there is no menu over them). In that case we pass None for parent's node for MainMenu and MainMenuForUsers.

    def adding_exit_module(self):
        # Adding "Exit" module to every menu. Action by choosing "Q" or "q".
        self.content['Q'] = '|Q| Exit'
        self.options['Q'] = sys.exit

    def adding_back_module_leading_to_previously_visited_menu(self):
        if not self.main_menu:
            if MenuNode.previous_node:
                self.content['B'] = '|B| Back'
                self.options['B'] = MenuNode.previous_node
        # Back menu is a temporary state, it alters after each change of nodes (going through the menu).

    def saving_previous_node_and_updating_current_node(self):
        MenuNode.previous_node = MenuNode.current_node
        MenuNode.current_node = self

    def printing_menu_view(self):
        # If any user is logged in, we are displaying their username on the top of each menu view.
        usr = User.user_logged
        if usr:
            if usr.is_admin:
                print(f'\n\n\nAdmin: {User.user_logged.username}\n')
            else:
                print(f'\n\n\nUser: {User.user_logged.username}\n')
            print(f"{MenuNode.current_node.name}")
        # Current's node name
        else:
            print(f'\n\t{MenuNode.current_node.name}\n{25 * "-"}')

        print(f"{25 * '-'}")
        for key in self.content.keys():
            print(self.content[key])
        print(f"{25 * '-'}")

    def get_users_choice_prompt(self):

        # current = MenuNode.current_node

        self.adding_up_module_leading_to_parent_menu()
        self.adding_back_module_leading_to_previously_visited_menu()
        self.saving_previous_node_and_updating_current_node()
        self.adding_exit_module()
        self.printing_menu_view()

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

            elif choice.lower() == 'b':
                self.options["B"]()

            elif choice.lower() == '0':
                self.options['0']()

            else:
                print("Please enter a valid option.")
                continue

    def run(self):
        # Content is a dictionary of key:value pairs, paired <int from 0>:<str> e.g. for displaying views to users.
        # Other MenuNodes (views) or FuncNodes (scripts/functions) that we want to display on given <self> menu,
        # we add to self.options.

        # Getting user's choice
        choice = self.get_users_choice_prompt()
        try:
            chosen_option = self.options[choice]
            chosen_option()
        except KeyError:
            print("Please choose only from available options.")
