
#string
str='aku cinta indonesia'
print(str)
str=str[:10]+'tanah air ku'+str[9:]
print(str)
str=''
print(str)
str1='aku cinta tanah air ku indonesia'
str1=str1[:9]+''+str1[22:]
print(str1)
kelas='praktikum pemrograman berorientasi objek'
up=kelas.upper()
lo=kelas.lower()
print(kelas)
print(up)
print(lo)
s='     Python    '
s.strip()
s.lstrip()
s.rstrip()
len(kelas)
jumlah=len(kelas)
print('panjang string adalah:',jumlah)
s1='python'
s2='programming'
print(s1+s2)
print(kelas)
print(kelas.index('a'))
kelas2=kelas.replace('praktikum','praktik')
print(kelas2)
a='satu'
b='dua'
c='tiga'
print('saya mempunyai %s mangga'%(c))
print(kelas2)
kelas2.split()
input('hari ini adalah: ')
data1=input('angka 1: ')
data2=input('angka 2: ')
hasil=int(data1)*int(data2)
print(data1,'*',data2,' = ',hasil)

#list
list=[0,1,2,3,4,5,6,7,8,9]
print(list)
print(list[0])
print(list[5])
print(list[:3])
print(len(list))
print(list[10-3:])
print(list[2:9])
print(list[-10])
list.append(10)
print(list)
list.insert(1,11)
print(list)
list2=['halo']
list.extend(list2)
print(list)
list.extend('hai')
print(list)
del list[1]
print(list)
list.remove(10)
print(list)
print(list.pop())
print(list)
print(list.pop(2))
print(list)

a=[50,10,20,30,40]
b=sorted(a)
print(b)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(min(a))
print(max(a))

#dictionary
d={1:100, 2:200, 3:300, 4:400, 5:500}
print(d)
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[1]
print(d)

b=d.copy()
print(b)
d.clear()
print(d)
len(d)

#tuple
t=(100,200,300,400)
print(t)
print(t[0])
print(t[3])
print(t.index(200))

t2=(10,20,10,30,10,40,20)
print(t.count(10))
print(t2.count(20))
print(t2.count(10))
print(t2.count(30))
print(t.count(30))

#set (himpunan)
data = {1,2,3,4,5,6,7,8,9}
print (data)

data.add(10)
print(data)

data.update([11,12,13])
print(data)

data.remove(3)
print(data) 

data.discard(14)
print(data)

data.pop()
print(data)

data.clear()
print(data)

#operasi gabungan
data1 = {1,2,3,4}
data2 = {5,6,7,8}
# menggunakan tanda palang |
print(data1|data2) 
# menggunakan fungsi union
data3 = data1.union(data2)
print (data3)

#operasi irisan
data1 = {1,2,3,4}
data2 = {1,2,4,5}
# menggunakan tanda palang |
print(data1 & data2)
# menggunakan fungsi intersection
data3 = data1.intersection(data2)
print (data3)

#operasi selisih
data1 = {1,2,3,4}
data2 = {1,2,7,8}
# menggunakan tanda min -
print(data1 - data2)
# menggunakan fungsi difference
data3 = data1.difference(data2)
print (data3)

#operasi komplemen
data1 = {1,2,3,4}
data2 = {1,2,7,8}
# menggunakan tanda min -
print(data1 ^ data2)
# menggunakan fungsi difference
data3 = data1.symmetric_difference(data2)
print (data3)