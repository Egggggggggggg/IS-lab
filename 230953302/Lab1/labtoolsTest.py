from Lab_Tools import ParadigmStrings as ps

s=ps.setString("I am learning information security")
additive=ps.setString("I am learning information security").modify_all(lambda x:x+20)
mult=ps.setString("I am learning information security").modify_all(lambda x:x*15)
affine=ps.setString("I am learning information security").modify_all(lambda x:x*15+20)

print(s)
print(additive)
print(mult)
print(affline)
