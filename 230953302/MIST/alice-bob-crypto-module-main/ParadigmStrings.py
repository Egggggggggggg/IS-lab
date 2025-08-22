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
        return "".join(s)

    def __iter__(self):
        return self._s.__iter__()

    def __next__(self):
        return self._s.__next__()

    def __getitem__(self,key):
        return self._s[key]

    def __len__(self):
        return len(self._s)
    
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
        if isinstance(self.s,str) and isinstance(c,chr):
            self._s=self._s[:n]+c+self._s[n+1:]
        elif isinstance(self.s,str) and not isinstance(c,chr):
            raise TypeError("Expected character")
        else:
            self._s[n]=c

    def substitute(self,subs_dict):
        pass
