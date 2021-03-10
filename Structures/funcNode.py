from menuNode import MenuNode


# FuncNode don't change MenuNode.current_node value, MenuNodes do.
# The scripts that FuncNodes hold however, can change the mentioned value if they simply have such code.
# FuncNodes are callable and they return their function call.

class FuncNode(MenuNode):
    def __init__(self, name, func, parent_up_menu):
        super().__init__(name, parent_up_menu)
        self.func = func

    def __call__(self):
        return self.func()


