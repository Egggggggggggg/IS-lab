import AliceBob
import ParadigmStrings

plaintext=setString("Hello")
key=13

def Ceaser(pt,k):
	return pt<<k

def DeCeaser(pt,k):
	return pt>>k
	
def BruteForceCeaser(pt):
	decs=set()
	for i in range(27):
		decs.add(pt<<i)
	return decs

Alice=Agent("Alice")
Bob=Agent("Bob")
Eve=Agent("Eve")

InsecureChannel=Channel()

ABE_Standard=Model()

ABE_Standard.AddAgent(Alice)
ABE_Standard.AddAgent(Bob)
ABE_Standard.AddAgent(Eve)

ABE_Standard.AddChannel(InsecureChannel)

Alice.PlainText=plaintext
Alice.PrivateKey=key
Alice.encryption=Ceaser
Alice.decryption=DeCeaser
Bob.encryption=Ceaser
Bob.decryption=DeCeaser

