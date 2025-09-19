import ParadigmStrings

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
    decryption= lambda CipherText: PlainText
    
    def __init__(self,Name,*args,PlainText="",PrivateKey="",PublicKey="",encryption=lambda CipherText: PlainText, decryption= lambda CipherText: PlainText):
        self.Name=Name
        self.PlainText=PlainText
        self.PrivateKey=PrivateKey
        self.PublicKey=PublicKey
        self.encryption=encryption
        self.decryption=decryption

    def encrypt(self,encryption=0):
        if encryption==0:
            encryption=self.encryption
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

#For now I'm only adding support for a single standard model cause this is harder than I thought it'd be...

class Model:
    Agents=[]
    Channels=[]
    AccessList=set()
    
    def AddAgent(self,Agent):
        self.Agents.append(Agent)
    
    def AddChannel(self,Channel):
        self.Channels.append(Channel)
        
    def AddAccessPair(self,Agent,Channel):
        if Agent not in set(self.Agents):
            raise "Unknown Agent"
        if Channel not in set(self.Channels):
            raise "Unknown Channel"
        self.AccessList.add((Agent,Channel))
        
    def GenerateCompleteAccessList():
        for i in Agents:
            for j in Channels:
            	AccessList.add((i,j))
        
    def VerifyTopMost(Channel)
