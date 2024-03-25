d = {'jack':'jack@mail.com', 'tom':'tom@mail.com'}
d['jim'] = 'jim@sin.com'
del d['tom']
s = list(d.keys())
s = sorted(s)
print(s)