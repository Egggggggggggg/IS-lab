import ParadigmStrings

Plaintext=""
Key=""
Message=""

class Channel:
    BroadcastBoard=[]
    Noise = lambda message: message
    valid = lambda message: True
    
    def Broadcast(self,message):
        if valid(message):
            self.BroadcastBoard.append(Noise(message))
        return valid
    
class Agent:
    Name=""
    PublicKey=""
    PrivateKey=""
    PlainText=""
    CipherText=""
    encryption= lambda CipherText: PlainText

    def __init__(self,Name,args*,PlainText="",PrivateKey="",PublicKey="",encryption=self.encryption):
        self.Name=Name
        self.PlainText=PlainText
        self.PrivateKey=PrivateKey
        self.PublicKey=PublicKey
        self.encryption=encryption

    def encrypt(self,encryption=self.encryption):
        self.CipherText=encryption(PlainText)

    def post(self,*args):
        #Adds the Ciphertext to the specified channels
        for chan in args:
            if not isinstance(chan,Channel):
                raise TypeError("Expected Channel")
            if not chan.Broadcast(self.CipherText):
                print(f"Message Broadcast Failed")

    def encpost(self,encryption,*args):
        self.Encrypt(encryption)
        self.Broadcast(args)
        #small consolidated method lol
        
