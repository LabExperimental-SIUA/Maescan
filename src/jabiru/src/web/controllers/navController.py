class NavController:

	def __init__(self, env):
		self.env = env

	def home(self):
		return self.env.get_template('webCorrector.jade').render()

