class operand:

	def __init__(self):
		self._value = -1;
		self._type = INVALID;

	def set(self, _val, _ty):
		self._value = _val;
		self._ty = _ty;

class instruction:

	def __init__(self):
		self._type = None;
		self._subtype = None;
		self._args = [];

	def get_type(self):
		return self._type;

	def get_subtype(self):
		return self._subtype;

	def get_num_args(self):
		return len(self._args);

	def get_args(self, _arg_id = -1):
		if _arg_id == -1:
			return self._args;
		return self._args[_args_id];

class decoder:

	def __init__(self, _decoder_file):
		

class shader_parser:

	def __init__(self, _shader_str):
		shader = _shader_str.splitlines();
		m_instr_list = [];
		for instr_str in shader:
			self.m_instr_list.append(decode_instr(instr_str));




	
