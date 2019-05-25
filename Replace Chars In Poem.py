#PF-Assgn-53
#This verification is based on string match.
import re

poem='''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

c=poem.count("v")
li=list(poem.split())
st=" ".join(li)
print(c)
print(st)

st=re.sub(r"co",r"Co",poem)
st=re.sub(r"ch",r"Ch",st)

print(st)
print()
st=re.sub(r"ai...",r"ai*\*",poem)
st=re.sub(r"hi...",r"hi*\*",st)
print(st)
print()
