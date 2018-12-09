import argparse

class parser:

	def __init__(self):
		self.m_parser = argparse.ArgumentParser();
		self.m_parser.add_argument("--shader",
									help = "Path to file containing the shader",
									type = str);
		self._args = self.m_parser.parse_args();

	def get_args(self):
		if(self._args.shader):
			print("Shader path : "+self._args.shader)
		return self._args; 