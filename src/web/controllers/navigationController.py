

class NavigationController:

    def __init__(self, p_env):
        self.env = p_env

    def home(self):
        return self.env.get_template('index.jade').render()

    def about(self):
        return self.env.get_template('aboutUs.jade').render()

    def contact(self):
        return self.env.get_template('contactUs.jade').render()

    def scan(self):
        return self.env.get_template('capture.jade').render()

    def output_preview(self):
        return self.env.get_template('outputPreview.jade').render()

