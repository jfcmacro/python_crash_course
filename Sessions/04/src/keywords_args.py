def keywords_args(**args):
    def t(d,n,v):
        return d[n] if n in d else v 
    return t(args,'one',1) + t(args,'two',2) * t(args,'three',3)

#

args = { }

print(keywords_args(**args))

args = { 'one' : 20 }

print(keywords_args(**args))

args = { 'one' : 20 , 'two' : 30 }

print(keywords_args(**args))

args = { 'one' : 20, 'two' : 30, 'three' : 40 }

print(keywords_args(**args))

print(keywords_args(one=40))
