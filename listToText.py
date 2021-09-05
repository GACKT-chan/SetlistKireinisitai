import re

def Add_text(l, eld, item):
    i = int(eld.get(item))
    # print(l[i])
    return l[i]


print("inputFile  ", end = ':')
inName= input()
print("outputFile ", end = ':')
makeName= input()
inp = re.search(r'.*'+'.txt',inName)
if inp == None:
    inName += '.txt'
out = re.search(r'.*'+'.txt',makeName)
if out == None:
    makeName += '.txt'
with open(inName,'r',encoding="utf-16-le") as f:
    s = f.read()
s = s.replace(u'\ufeff','')
slines = s.split('\n')
slines = [l.replace('\n','') for l in slines]
selements = []
for l in slines:
    ll = str(l).split('\t')
    selements.append(ll)
eld = {}
for l in range(len(selements[0])):
    eld.setdefault(selements[0][l], l)
out_lines = ''
for l in selements[:-1]:
    out_lines += Add_text(l, eld, '#') + '/'
    out_lines += Add_text(l, eld, 'トラックタイトル') + '/'
    out_lines += Add_text(l, eld, 'アーティスト') + '/'
    out_lines += Add_text(l, eld, 'コメント') + '\n'
with open(makeName,'w', encoding='UTF-8') as f:
    f.write(out_lines)