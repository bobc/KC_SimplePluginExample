import pcbnew

class SimplePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "SimplePluginExample"
        self.category = "Examples"
        self.description = "A simple example of a simple plugin"

    def Run(self):
        # The entry function of the plugin that is executed on user action
        print("Hello World")

SimplePlugin().register() # Instantiate and register to Pcbnew
