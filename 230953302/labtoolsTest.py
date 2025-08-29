from Lab_Tools import ParadigmStrings as ps

s=ps.setString("I am learning information security")
additive=ps.setString("I am learning information security")
mult=ps.setString("I am learning information security")
affine=ps.setString("I am learning information security")

additive.modify_all(lambda x:x+20)
mult.modify_all(lambda x:x*15)
affine.modify_all(lambda x:x*15+20)

print(s)
print(additive)
print(mult)
print(affine)
