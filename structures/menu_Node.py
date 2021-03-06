import sys, os
import json_data_funcs


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
                self.content[str(len(self.content) + 1)] = f'|{str(len(self.content) + 1)}| {func_or_menu_node.name}\n'
                func_or_menu_node.parent_up = self
        return

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

    def updating_current_node(self):
        MenuNode.current_node = self

    def adding_back_module_leading_to_previously_visited_menu(self):
        if not self.main_menu:
            if self.parent_up:
                self.content['B'] = '|B| Back'
                self.installed_options['B'] = self.parent_up
        return
        # Back menu is a temporary state, it alters after each change of nodes (going through the menu).

    def printing_menu_view(self):
        # If any user is logged in, we are displaying their username on the top of each menu view.
        users = json_data_funcs.read_data_from_users_database()
        admins = json_data_funcs.read_data_from_admins_database()
        from structures.user_class import User, Admin
        current_usr = None

        if User.logged:
            current_usr = User.logged
            if User.logged.is_admin:
                current_usr = Admin.logged

        all_users = []
        for a in admins['admins']:
            all_users.append(a)
        for u in users['users']:
            all_users.append(u)

        if current_usr:

            if len(all_users) > 0:
                for user in all_users:
                    name = user['username']
                    if current_usr.username == name:
                        current_usr = user
                        break

            if current_usr['is_admin']:
                print(f"\n\n{25 * '-'}")
                print(f"You have {len(admins['admins_inf']['requests_box'])} new requests!")
                print(f"{25 * '-'}")
                print(f"\n\n\nAdmin: {current_usr['username']}\n")
            else:
                if len(current_usr['notifications']) > 0:
                    print(f"You have {len(current_usr['notifications'])} notifications:")
                    for notif in current_usr['notifications']:
                        print(f"\n\n{notif}")
                    current_usr['notifications'] = []
                else:
                    print("\nNo news.\n")
                print(f"\n\n\nUser: {current_usr['username']}\n")
            print(f"{MenuNode.current_node.name}")

            # Current node's name
        else:
            print(f'\n\t{MenuNode.current_node.name}\n{25 * "-"}')

        print(f"{25 * '-'}")
        for key in self.content.keys():
            print(self.content[key])
        print(f"{25 * '-'}")
        json_data_funcs.write_data_to_users_database(users)
        json_data_funcs.write_data_to_admins_database(admins)
        return

    def get_users_choice_prompt(self):
        os.system('clear')
        # self.check_logged_user()
        # self.adding_back_module_leading_to_previously_visited_menu()
        from structures.Refill_Requests import RefRequest
        RefRequest.checking_pending_requests()

        os.system('clear')

        self.install_options()
        self.adding_up_module_leading_to_parent_menu()
        self.adding_exit_module()

        self.updating_current_node()
        self.printing_menu_view()

        while True:
            choice = input("\nEnter characters to choose an option:\n")
            if choice in self.installed_options.keys():
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
                    return self.installed_options['0']()
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
        return chosen_option()

        # except KeyError:
        #     print("Please choose only from available options.")

