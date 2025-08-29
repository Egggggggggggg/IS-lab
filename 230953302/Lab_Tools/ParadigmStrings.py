import itertools

ASCII= "".join(chr(i) for i in range(128))
ALPHA="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA_LOWER="abcdefghijklmnopqrstuvwxyz"
ALPHA_UPPER="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALNUM="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
NUM="0123456789"
BIN="01"

class Paradigm:
    _charset = set(ASCII)
    _order= [ALPHA_LOWER,ALPHA_UPPER]
    _unorder= set(ASCII)-set(ALPHA)
    
    def __init__(self,_charset,_order):
        flat_Order=[i for j in _order for i in j]
        if len(flat_Order)!=len(set(flat_Order)):
            raise Exception("All elements in Order should be unique")
        self._charset=set(_charset)
        self._order=_order
        self._unorder=self._charset-set(flat_Order)

    def __str__(self):
        return "placeholder"
    
    def validate(self,tocheck):
        for i in tocheck:
                if i not in self._charset:
                    return False
                else:
                    return True
                
    def Charset(self,new_charset):
        flat_Order=[i for j in self._order for i in j]
        if not self.validate(flat_Order):
            raise Exception("Invalid elements in Order")
        self._charset=set(new_charset)
        self._unorder=self._charset-set(flat_Order)

    def Order(self,new_Order):
        flat_Order=[i for j in new_Order for i in j]
        if not self.validate(flat_Order):
            raise Exception("Invalid elements in Order")
        if len(flat_Order)!=len(set(flat_Order)):
            raise Exception("All elements in Order should be unique")
        self._order=new_Order
        self._unorder=self._charset-set(flat_Order)

DEFAULT_PARADIGM=Paradigm(set(ASCII),[ALPHA_UPPER,ALPHA_LOWER])
REVERSE_PARADIGM=Paradigm(set(ASCII),[ALPHA_UPPER[::-1],ALPHA_LOWER[::-1]])
BIN_PARADIGM=Paradigm(set(BIN),[BIN])

class setString:
    _paradigm = DEFAULT_PARADIGM
    _s=""
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            raise TypeError("Too few arguments")
        if len(args) == 1:
            s=args[0]
            _paradigm = DEFAULT_PARADIGM
            if not _paradigm.validate(s):
                raise Exception("Invalid elements in string")
            self._s=s
            self._paradigm=_paradigm
        if len(args) == 2:
            s=args[0]
            _paradigm = args[1]
            if not isinstance(_paradigm,Paradigm):
                raise TypeError("Expected Paradigm")
            if not _paradigm.validate(s):
                raise Exception("Invalid elements in string")
            self._s=s
            self._paradigm=_paradigm
        if len(args) == 3:
            s=args[0]
            _paradigm = Paradigm(args[1],args[2])
            if not _paradigm.validate(s):
                raise Exception("Invalid elements in string")
            self._s=s
            self._paradigm=_paradigm
        if len(args) > 2:
            raise TypeError("Too many arguments")

    def __str__(self):
        return "".join(self._s)

    def __iter__(self):
        return self._s.__iter__()

    def __next__(self):
        return self._s.__next__()

    def __getitem__(self,key):
        return self._s[key]

    def __len__(self):
        return len(self._s)
    
    def __add__(self,val2):
    	if isinstance(val2,setString):
    		return setString(self._s+val2._s,self._paradigm)
    	if isinstance(val2,str):
    		return setString(self._s+val2,self._paradigm)
    
    def __lshift__(self,shift,fill=-1):
    	if fill==-1:
    		fill=self._paradigm._order[0][0]
    	else:
    		if not self._paradigm.validate(fill):
    			raise TypeError("Unexpected Charachters")
    	if shift>=0:
    		out=self.__class__(self._s+fill*shift)
    	if shift<0:
    		out=self.__rshift__(-shift,fill)
    	return out
    
    
    def __rshift__(self,shift,fill=-1):
    	if fill==-1:
    		fill=self._paradigm._order[0][0]
    	else:
    		if not self._paradigm.validate(fill):
    			raise TypeError("Unexpected Charachters")
    	if shift>=0:
    		out=self.__class__(fill*shift+self._s[:-shift])
    	if shift<0:
    		out=self.__lshift__(-shift,fill)
    	return out
    
    def join(self,val2):
    	if isinstance(val2,setString):
    		return setString(self._s+val2._s,self._paradigm)
    	if isinstance(val2,str):
    		return setString(self._s+val2,self._paradigm)
    
    def write(self,new_s):
        _paradigm=self._paradigm
        if not _paradigm.validate(new_s):
                raise Exception("Invalid elements in string")
        self._s=new_s
        
    def Charset(self,new_charset):
        _paradigm=self._paradigm
        _paradigm.Charset(new_charset)
        if not _paradigm.validate(self._s):
                raise Exception("Invalid elements in string")
        self._paradigm.Charset(new_charset)

    def Order(self,new_Order):
        _paradigm=self._paradigm
        _paradigm.Order(new_Order)
        if not _paradigm.validate(s):
                raise Exception("Invalid elements in string")
        self._paradigm.Order(new_Order)

    def cshift(self,shift):
        #-ve for left, +ve for right
        out=[]
        for i in self._s:
            if i in self._paradigm._unorder:
                out.append(i)
                continue
            for seq in self._paradigm._order:
                if i in seq:
                    out.append(seq[(seq.index(i)+shift)%len(seq)])
                    break
        if isinstance(self._s,str):
            self._s="".join(out)
        else:
            self._s=out
        return self._s

    def replace(self,old,new):
        self._paradigm._validate(new)
        if isinstance(self._s,str):
            self._s.replace(old,new)
        else:
            for i in range(len(self._s)):
                if self._s[i] == old:
                    self._s[i] == new
        return self._s

    def set_at_index(self,n,c):
        self._paradigm.validate(c)
        if isinstance(self._s,str) and isinstance(c,str):
            self._s=self._s[:n]+c+self._s[n+1:]
        elif isinstance(self._s,str) and not isinstance(c,str):
            raise TypeError("Expected character")
        else:
            self._s[n]=c

    def where_inorder(self,n,zero_ofset=0):
        flat_Order=[i for j in self._paradigm._order for i in j]
        element=self._s[n]
        if element in self._paradigm._unorder:
            return 0
        if element in flat_Order:
            for seq in self._paradigm._order:
                if element in seq:
                    return seq.index(element)+zero_ofset

    def modify_at_index(self,n,change,zero_ofset=0):
        #change is function or lambda function
        flat_Order=[i for j in self._paradigm._order for i in j]
        element=self._s[n]
        val_n=self.where_inorder(n,zero_ofset)
        new_val=change(val_n)
        if element in flat_Order:
            for seq in self._paradigm._order:
                if element in seq:
                    new_element = seq[new_val%len(seq)]
        else:
            new_element=element
        self.set_at_index(n,new_element)

    def modify_all(self,change,start=0,end=-1,zero_ofset=0):
        if end<0:
            end=len(self._s)+end+1
        for i in range(start,end):
            self.modify_at_index(i,change,zero_ofset)

    def substitute(self,subs_dict):
        pass

def bin_pad(b,l=8,p="0",debug=False):
    if l<len(b):
        if debug:
            print(f"binary {b} of length {len(b)} is bigger than desired size {l}")
        return b
    if debug:
        print(f"Padded {l-len(b)} {p} bits to {len(b)} bits")
    b=p*(l-len(b))+b
    return b

def ascii_to_bin(a,debug=False):
    out=""
    for i in a:
        binchr=str(bin(ord(i)))[2:]
        out+=bin_pad(binchr)
    if debug:
        print(out)
    return out

def to_blocks(s,size):
    bin_pad(s)
    return [s[i:i+size] for i in range(0,len(s),size)]

def bin_to_ascii(b,debug=False):
    blocks=to_blocks(b,8)
    if debug:
        print(blocks)
    out=""
    for i in blocks:
        out+=chr(int(i,2))
    return out

def bitwise_XOR(b1,b2):
    b1=bin_pad(b1,l=len(b2))
    b2=bin_pad(b2,l=len(b1))
    out=""
    for i in range(len(b1)):
        out+=str(int(b1[i])^int(b2[i]))
    return out

def bitwise_AND(b1,b2):
    b1=bin_pad(b1,l=len(b2))
    b2=bin_pad(b2,l=len(b1))
    out=""
    for i in range(len(b1)):
        out+=str(int(b1[i]) and int(b2[i]))
    return out

def bitwise_OR(b1,b2):
    b1=bin_pad(b1,l=len(b2))
    b2=bin_pad(b2,l=len(b1))
    out=""
    for i in range(len(b1)):
        out+=str(int(b1[i]) or int(b2[i]))
    return out

def circular_shift(b,shift=1):
    out=""
    for i in range(len(b)):
        out+=b[((i-shift)%len(b))]
    return out

class BinStr(setString):
	def __init__(self, s):
		_paradigm = BIN_PARADIGM
		if isinstance(s,int):
			s=str(bin(s))[2:]
		if not _paradigm.validate(s):
			s=ascii_to_bin(s)
		self._s=s
		self._paradigm=_paradigm
	
	def __mul__(self,val2):
		if isinstance(val2,BinStr):
			return BinStr(bitwise_AND(self._s,val2._s))
		else:
			if not self._paradigm.validate(s):
				raise TypeError("Unexpected charachters in BinStr")
			return BinStr(bitwise_AND(self._s,val2))
	
	def __add__(self,val2):
		if isinstance(val2,BinStr):
			return BinStr(bitwise_OR(self._s,val2._s))
		else:
			if not self._paradigm.validate(s):
				raise TypeError("Unexpected charachters in BinStr")
			return BinStr(bitwise_OR(self._s,val2))
	
	def __xor__(self,val2):
		if isinstance(val2,BinStr):
			return BinStr(bitwise_XOR(self._s,val2._s))
		else:
			if not self._paradigm.validate(s):
				raise TypeError("Unexpected charachters in BinStr")
			return BinStr(bitwise_XOR(self._s,val2))
	
	def to_blocks(self,size):
		return [BinStr(i) for i in to_blocks(self._s,size)]
	
	def ascii(self):
		return bin_to_ascii(self._s) 
	
	def num(self):
		return int(self._s,2)
