import sys, os
import shutil
from structures.user_class import User


class MenuNode:

    default_node = None

    current_node = None
    previous_node = None

    def __init__(self, name, content=None, main_menu=False, parent_up=None, options=None):
        self.name = name

        self.content = content
        if not self.content:
            self.content = {}

        self.options = options
        if not options:
            self.options = []

        self.installed_options = {}

        self.main_menu = main_menu
        # if MenuNode.current_node:
        #
        self.parent_up = parent_up
        # if self.parents_up is None:
        #     self.parents_up = []

    def __repr__(self):
        return self.name

    def __call__(self):
        return self.run()

    # @classmethod
    # def check_logged_user(cls):
    #     from structures.user_class import User
    #     return User.logged

    def install_options(self):
        for func_or_menu_node in self.options:
            if func_or_menu_node not in self.installed_options.values():
                self.installed_options[str(len(self.installed_options) + 1)] = func_or_menu_node
                self.content[str(len(self.content) + 1)] = f'|{str(len(self.content) + 1)}| {func_or_menu_node}\n'
                func_or_menu_node.parent_up = self  # todo for games it is easy to lost track and give them more than 1 parent!

    def adding_up_module_leading_to_parent_menu(self):
        # Adding "Up" module to given menu, if there is a path to go back to, by choosing "0".
        # if self.parent_up:
        if not self.main_menu:
            self.content['0'] = "\n|0| Up\n"
            # if len(self.parents_up) == 1:
            self.installed_options['0'] = self.parent_up
                # print(self.parents_up[-1].name)
            # else:
            #     for i in range(len(self.parents_up)):
            #         if MenuNode.previous_node == self.parents_up[i]:
            #             self.options['0'] = self.parents_up[i]
            #             print(self.parents_up[i].name)

    def adding_exit_module(self):
        # Adding "Exit" module to every menu. Action by choosing "Q" or "q".
        self.content['Q'] = '|Q| Exit'
        self.installed_options['Q'] = sys.exit

    def adding_back_module_leading_to_previously_visited_menu(self):
        if not self.main_menu:
            if MenuNode.previous_node:
                self.content['B'] = '|B| Back'
                self.installed_options['B'] = MenuNode.previous_node
        # Back menu is a temporary state, it alters after each change of nodes (going through the menu).

    def saving_previous_node_and_updating_current_node(self):
        MenuNode.previous_node = MenuNode.current_node
        MenuNode.current_node = self

    def printing_menu_view(self):
        # If any user is logged in, we are displaying their username on the top of each menu view.
        usr = User.logged
        if usr:
            if usr.is_admin:
                c = 0
                if c < 1:
                    print(f"\n\n{25 * '-'}")
                    print(f"You have {len(usr.notifications)} new requests!")
                    print(f"{25 * '-'}")
                    c += 1
                print(f'\n\n\nAdmin: {usr.username}\n')
            else:
                print(f'\n\n\nUser: {usr.username}\n')
            print(f"{MenuNode.current_node.name}")
            # Current's node name
        else:
            print(f'\n\t{MenuNode.current_node.name}\n{25 * "-"}')

        print(f"{25 * '-'}")
        for key in self.content.keys():
            print(self.content[key])
        print(f"{25 * '-'}")

    def get_users_choice_prompt(self):
        os.system('clear')
        # self.check_logged_user()
        # self.adding_back_module_leading_to_previously_visited_menu()
        from structures.Refill_Requests import RefRequest
        RefRequest.pending_requests_check()
        RefRequest.executing_pending_requests()

        os.system('clear')

        self.install_options()
        self.adding_up_module_leading_to_parent_menu()
        self.adding_exit_module()

        self.saving_previous_node_and_updating_current_node()
        self.printing_menu_view()

        while True:
            choice = input("\nEnter characters to choose an option:\n")
            if choice in self.content.keys():
                return choice

            elif choice.lower() == 'q':
                ans = input("\nAre you sure you are leaving?\nEnter Y or N.\n")
                if ans.lower() == "y":
                    self.installed_options["Q"]()
                    # sys.exit()
                else:
                    continue

            # elif choice.lower() == 'b':
            #     if not self.main_menu:
            #         self.options["B"]()
            #     else:
            #         print("Please enter a valid option.")
            #         continue

            elif choice.lower() == '0':
                if not self.main_menu:
                    self.installed_options['0']()
                else:
                    print("Please enter a valid option.")
                    continue
            else:
                print("Please enter a valid option.")
                continue

    def run(self):
        # Content is a dictionary of key:value pairs, paired <int from 0>:<str> e.g. for displaying views to users.
        # Other MenuNodes (views) or FuncNodes (scripts/functions) that we want to display on given <self> menu,
        # we add to self.options.

        # Getting user's choice
        choice = self.get_users_choice_prompt()
        # try:
        chosen_option = self.installed_options[choice]
        chosen_option()
            # return
        # except KeyError:
        #     print("Please choose only from available options.")
