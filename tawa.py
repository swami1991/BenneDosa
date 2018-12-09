import parser;
import gpu;

class tawa:

	def __init__(self):
		self.m_arg_parser = arg_parser.arg_parser();
		self.m_gpu = gpu.gpu(self);

	def start(self):
		self.m_arg_parser.get_args();


def main():
	m_tawa = tawa();
	m_tawa.start();
	print("****END****")

if __name__ == "__main__":
	main();