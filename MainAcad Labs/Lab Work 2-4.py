alphnum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

alphnumlist = list(alphnum)

print(alphnumlist[0])
print(alphnumlist[-1])
print(alphnumlist[2:-2])

alphnumlist = alphnumlist[10:]

print(alphnumlist[2::2])
print(alphnumlist[-10:])

alphnumlist = alphnumlist[::-1]

"".join(alphnumlist)
