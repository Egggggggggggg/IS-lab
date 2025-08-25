from Lab_Tools import lab_tools as lt
from Lab_Tools import ParadigmStrings as ps

class BinStr(ps.setString):
	def __init__(self, s):
		_paradigm = ps.BIN_PARADIGM
		if isinstance(s,int):
			s=str(bin(s))[2:]
		if not _paradigm.validate(s):
			s=lt.ascii_to_bin(s)
		self._s=s
		self._paradigm=_paradigm
	
	def __mul__(self,val2):
		if isinstance(val2,BinStr):
			return BinStr(lt.bitwise_AND(self._s,val2._s))
		else:
			if not self._paradigm.validate(s):
				raise TypeError("Unexpected charachters in BinStr")
			return BinStr(lt.bitwise_AND(self._s,val2))
	
	def __add__(self,val2):
		if isinstance(val2,BinStr):
			return BinStr(lt.bitwise_OR(self._s,val2._s))
		else:
			if not self._paradigm.validate(s):
				raise TypeError("Unexpected charachters in BinStr")
			return BinStr(lt.bitwise_OR(self._s,val2))
	
	def __xor__(self,val2):
		if isinstance(val2,BinStr):
			return BinStr(lt.bitwise_XOR(self._s,val2._s))
		else:
			if not self._paradigm.validate(s):
				raise TypeError("Unexpected charachters in BinStr")
			return BinStr(lt.bitwise_XOR(self._s,val2))
	
	def to_blocks(self,size):
		return [BinStr(i) for i in lt.to_blocks(self._s,size)]
	
	def ascii(self):
		return lt.bin_to_ascii(self._s) 
	
	def num(self):
		return int(self._s,2)
