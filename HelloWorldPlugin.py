from pcraft.PluginsContext import PluginsContext

class PCraftPlugin(PluginsContext):
    name = "HelloWorldPlugin"

    def __init__(self, app, session, plugins_data):
        super().__init__(app, session, plugins_data)

    def run(self, script=None):
        self.update_vars_from_script(script)

        print("Hello, world!")

        if script:
            return script["_next"], self.plugins_data
        else:
            return None, self.plugins_data
