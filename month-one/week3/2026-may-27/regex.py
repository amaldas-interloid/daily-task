   #findall.......................................................
   
   
# import re
# txt  = "lion the king of jungle "
# x = re.findall("[a-e]",txt)
# print(x)


     # ^  start with..................................................................
# import re
# txt ="lion the king of jungle"
# x = re.sub("^lion","amal",txt)
# print(x)


        #$ ends with.............................................................................
        
import re
txt = "satheesh is very hansome boy"
a = re.findall("boy$",txt)
b = re.search("^satheesh",txt)
c= re.sub("satheesh","naveen",txt)
d = re.findall("sa..e",txt)
e= re.findall("sa.*o",txt)
f= re.findall("sa.{2}e",txt)
g= re.findall("satheesh|amal",txt)
if a :
    print("correct")

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


