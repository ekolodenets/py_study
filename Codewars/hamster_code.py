'''
 1  | a e h m r s t
 2  | b f i n     u
 3  | c g j o     v
 4  | d   k p     w
 5  |     l q     x
 6  |             y
 7  |             z

a => a1
b => a2
c => a3
d => a4
e => e1
f => e2
'''

def hamster_me(code, message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    clean = [] if 'a' in code else ['a']
    [clean.append(i) for i in code if i not in clean]
    sclean = sorted(clean)

    l = []
    for i in range(len(sclean)):
        if i+1 <= len(sclean):
            l.append(alphabet.index(sclean[i]))
    nl = []
    for i in range(len(l)):
        try:
            nl.append(alphabet[l[i]:l[i+1]])
        except:
            nl.append(alphabet[l[i]:])

    if 'a' not in code:
        temp = nl.pop(0)
        nl[-1] = nl[-1] + temp


    dic = {}
    for i in nl:
        for j in i:
            if j in message:
                dic[j] = f'{i[0]}{i.index(j)+1}'

    return ''.join([dic[i] for i in message])


assert hamster_me("hamster", "hamster") == "h1a1m1s1t1e1r1"
assert hamster_me("hamster", "helpme") == "h1e1h5m4m1e1"
assert hamster_me("hmster", "hamster") == "h1t8m1s1t1e1r1"
assert hamster_me("hhhhammmstteree", "hamster") == "h1a1m1s1t1e1r1"
assert hamster_me("hamster", "abcdefghijklmnopqrstuvwxyz") == "a1a2a3a4e1e2e3h1h2h3h4h5m1m2m3m4m5r1s1t1t2t3t4t5t6t7"
assert hamster_me("f", "abcdefghijklmnopqrstuvwxyz") == "f22f23f24f25f26f1f2f3f4f5f6f7f8f9f10f11f12f13f14f15f16f17f18f19f20f21"