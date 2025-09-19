import AliceBob as ab
import ParadigmStrings as ps
import string

plaintext=ps.setString("Hello")
key=13
vkey="lol"

def Ceaser(pt,k):
	return ps.setString(pt).cshift(k)

def DeCeaser(pt,k):
	return ps.setString(pt).cshift(k)
	
def BruteForceCeaser(pt,k):
	decs=set()
	for i in range(27):
		decs.add("".join(ps.setString(pt).cshift(i)))
	return decs

Alice=ab.Agent("Alice")
Bob=ab.Agent("Bob")
Eve=ab.Agent("Eve")

InsecureChannel=ab.Channel()

ABE_Standard=ab.Model()

ABE_Standard.AddAgent(Alice)
ABE_Standard.AddAgent(Bob)
ABE_Standard.AddAgent(Eve)

ABE_Standard.AddChannel(InsecureChannel)

Alice.PlainText=plaintext
Alice.PrivateKey=-key
Alice.PublicKey=key
Alice.encryption=Ceaser
Alice.decryption=DeCeaser
Bob.PrivateKey=-key
Bob.PublicKey=key
Bob.encryption=Ceaser
Bob.decryption=DeCeaser

Eve.decryption=BruteForceCeaser

ABE_Standard.GenerateCompleteAccessList()
ABE_Standard.test()
