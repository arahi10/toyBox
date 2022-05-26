def f(str):
    return int(str.split(' : ')[1])
c = 0
with open('result.txt','r') as file:
    c += sum(map(f,file.readlines()[::2]))

with open('result2.txt','r') as file:
    c += sum(map(f,file.readlines()[::2]))

z = 0
with open('result_zabuton.txt','r') as file:
    z += sum(map(f,file.readlines()[::2]))

with open('result_zabuton2.txt','r') as file:
    z += sum(map(f,file.readlines()[::2]))
print(c,z,sep='\n')