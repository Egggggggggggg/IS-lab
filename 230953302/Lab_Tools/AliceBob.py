import ParadigmStrings as ps

class Channel:
    BroadcastBoard = []
    Noise = lambda *args: args
    valid = lambda *args: True

    def Broadcast(self, message):
        if self.valid(message):
            self.BroadcastBoard.append(message)
            return True
        return False

    def getTop(self):
        return self.BroadcastBoard[-1]


class Agent:
    Name = ""
    PublicKey = ""
    PrivateKey = ""
    PlainText = ""
    CipherText = ""
    encryption = lambda self, CipherText: self.PlainText
    decryption = lambda self, CipherText: self.PlainText

    def __init__(self, Name, *args, PlainText="", PrivateKey="", PublicKey="", encryption=None, decryption=None):
        self.Name = Name
        self.PlainText = PlainText
        self.PrivateKey = PrivateKey
        self.PublicKey = PublicKey
        self.encryption = encryption if encryption is not None else (lambda CipherText: PlainText)
        self.decryption = decryption if decryption is not None else (lambda CipherText: PlainText)

    def encrypt(self, encryption=0):
        if encryption == 0:
            encryption = self.encryption
        self.CipherText = encryption(self.PlainText,self.PublicKey)

    def decrypt(self, decryption=0):
        if decryption == 0:
            decryption = self.decryption
        self.PlainText = decryption(self.CipherText,self.PrivateKey)

    def post(self, *args):
        # Adds the CipherText to the specified channels
        for chan in args:
            if not isinstance(chan, Channel):
                raise TypeError("Expected Channel")
            if not chan.Broadcast(self.CipherText):
                print("Message Broadcast Failed")
            chan.Broadcast(self.CipherText)

    def encpost(self,*args,encryption=0):
        if encryption == 0:
            encryption = self.encryption
        self.encrypt(encryption)
        self.post(*args)
        # small consolidated method lol


# For now I'm only adding support for a single standard model cause this is harder than I thought it'd be...

class Model:
    Agents = []
    Channels = []
    AccessList = set()

    def AddAgent(self, Agent):
        self.Agents.append(Agent)

    def AddChannel(self, Channel):
        self.Channels.append(Channel)

    def AddAccessPair(self, Agent, Channel):
        if Agent not in set(self.Agents):
            raise Exception("Unknown Agent")
        if Channel not in set(self.Channels):
            raise Exception("Unknown Channel")
        self.AccessList.add((Agent, Channel))

    def GenerateCompleteAccessList(self):
        for i in self.Agents:
            for j in self.Channels:
                self.AccessList.add((i, j))

    def test(self):
        Alice = None
        Bob = None
        Eve = None

        for i in self.Agents:
            if i.Name == "Alice":
                Alice = i
            if i.Name == "Bob":
                Bob = i
            if i.Name == "Eve":
                Eve = i

        for j in self.AccessList:
            if j[0].Name == "Alice":
                j[0].encpost(j[1])
                print("Alice Message Posted")

        for k in self.AccessList:
            if k[0].Name == "Bob":
                k[0].CipherText = k[1].getTop()
                k[0].decrypt()
                if Alice.PlainText in k[0].PlainText or (str(Alice.PlainText) in "".join(k[0].PlainText)):
                    print("Bob Received Message")
                else:
                    print("Bob Decryption Failed")
            if k[0].Name == "Eve":
                k[0].CipherText = k[1].getTop()
                k[0].decrypt()
                if Alice.PlainText in k[0].PlainText or (str(Alice.PlainText) in "".join(k[0].PlainText)):
                    print("Eve Cracked Message")
                else:
                    print("Message Secured From Eve")

