#1
x = input("Nhap bat ki :")
print(len(x))
#2
x2 = input("Hãy nhập cái gì đó: ")
y2 = {}
for i2 in x2:
    y2[i2] = y2.get(i2, 0) + 1
print(y2)
#3
x3 = input("Nhập gì đó đi ạ: ")
if len(x3) < 2:
    print("Nothing there")
else:
   print(x3[0:2], end="")
   print(x3[-2:])
#4
x4 = input("Nhập một chuỗi bất kì: ")
y4 = x4[0] + x4[1:].replace(x4[0], '$')
print(y4)
#5
x5 = str(input("Nhập chuỗi x bất kì: "))
y5 = str(input("Nhập chuỗi y bất kì: "))
z5 = x5[:2]+ y5[2:]
j5 = y5[:2]+ x5[2:]
yeu_cau_bai_5 = str(z5) +" " + str(j5)
print(yeu_cau_bai_5)
#6
x6 = input("Nhập kí tự bất kì: ")
if len(x6) < 3:
    print(x6)
elif x6[-3:] == "ing":
    print(x6+"ly")
else:
    print(x6+"ing")
#7
str7 = "The lyrics is not that poor!"
u7 = str7.find("not")
i7 = str7.find("poor")
if str7 != u7    and str7 != i7 and u7 < i7:
    k = str7[:u7]+"good"+str7[i7+4:]
    print(k)
else:
    print(str7)

#8
list_8 = str(input("Nhập danh sách: "))
long_words = max(list_8.split(), key=len)
print("Long words: ", long_words)
print("Length of long words: ",len(long_words))
#9
string9 = input("Enter a string: ")
n = int(input("Enter an index to remove: "))


if n < 0:
    n = len(string9) + n

if 0 <= n < len(string9):
    result = string9[:n] + string9[n+1:]
    print("Result:", result)
else:
    print("Index out of range")
#10
string10 = str(input("Enter the string: "))
result10 = string10[-1] + string10[1:-1] + string10[0]
print(result10)
#11
string11 = input("Enter the string: ")
print(string11[::2])
#12
string13 = input("Enter the string: ")
print("Upper : " , string13.upper())
print("Lower: " , string13.lower())
#13
string17 = input("Enter the string: ")
if len(string17) >=2 :
    print("Results: ",4*string17[-2:])
else:
    print(string17)
#14
string20 = input("Enter the string: ")
if len(string20) %4 == 0:
    results20 = string20[::-1]
    print(results20)
else:
    print(string20)
#15
str23 = "Hello\nworld"
print(str23.replace("\n", ""))
#16
str22 = input("Enter the string: ")
print(sorted(str22.split()))
#17
str24 = input("Enter the string: ")
check = input("Enter the the word if you want to check: ")
if str24[:len(check)] == check:
    print("YES")
else:
    print("NO")
#18
num31 = float(input("Enter the number: "))
print("Number is {:.2f}".format(num31))
#19
num32 = float(input("Enter the number: "))
print("Number is {:.0f}".format(num32))
#20
num34 = input("Enter a number: ")
n34 = int(input("Enter the width if you want : "))
i34 = n34*"*"+num34
print(i34)
#21
num33 = input("Enter the number: ")
n33 = int(input("Enter the width if you want : "))
i33 = n33*"0"+num33
print(i33)
#22
num35 = int(input("Enter the number: "))
print(f"The number is: {num35:,}")
#23
num37 = int(input("Enter the number: "))
print(f"{num37:>10}")
print(f"{num37:<10}")
print(f"{num37:^10}")
#24
num36 = float(input('Enter a number: '))
txt36 = f"The number is: {num36:%}"
print(txt36)
#25
string41 = input("Enter the string: ")
charactes = input("Enter the characters: ")
results = string41.strip(charactes)
print(results)
#26
import math

h43 = float(input("Nhập chiều rộng: "))
d43 = float(input("Nhập chiều dài: "))
R43 = float(input("Nhập bán kính hình trụ: "))
Area_of_rectangle_43 = h43*d43
Volume_of_cylinder_43 = math.pi*(R43**2)*h43

print(f"Area of rectangle:  {Area_of_rectangle_43}  cm\u00B2")
print(f"Volume of cylinder:  {Volume_of_cylinder_43} cm\u00B3" )
#27
string44 = input("Enter the string: ")
for i44 in range(len(string44)):
    print(f"Current character {string44[i44]} position at {i44}")
#28
string46 = input("Enter the string: ")
print(string46.split())
#29
string47 = str(input("Enter the string: "))
print(string47[0].lower() + string47[1:])
#30
string48 = str(input("Enter the string: "))
k = string48.replace(".", "@").replace(",", ".").replace("@", ",")
print(k)
#31
string57 = "     Hello World     "
print(string57.replace(" ",""))
#32
string58 = "     Hello World     "
print(string58.lstrip())
#33
x59 = input("Nhap bat ki :")
#34
x60 = str(input("Nhap bat ki :"))
results_60 = x60[0].upper() + x60[1:-1] + x60[-1:].upper()
print(results_60)
#35
x71 = "I   had   had   a   nice   day!"
count_white_space = x71.count(" ")
u71 = count_white_space*" "  + x71.replace(" ", "")
print(u71)
#36
x72 = "I   had   had   a   nice   day!"
y72 = input("Enter the except word: ")
if y72 in x72:
    u72 = x72.count(y72)
    print(u72*y72)
else:
    print("Nothing in there!!")

#37
x77 = input("String: ")
n = len(x77)
substring = int((n*(n+1))/2)
print(substring)
#38
x79 = input("String: ")
u79 = x79.split()
print(f"Max: {max(u79,key=len)}")
print(f"Min: {min(u79,key=len)}")
#39
x82 = input("String: ")
u82 = x82.swapcase()
print(u82)
#40
x86 ="Delete all occurrences of a specified character in a given string"
delete = input("Delete word in string: ")
if delete in x86:
    u = x86.replace(delete, "")
    print(u)
#41
x87 = "Hello my good boy!"
y87 = "Hello my good girl!"
z87 = x87.split()
j87 = y87.split()
for i in z87:
    if i in j87:
        print(i)
#42
the_string_81 = input("Enter the string: ")
the_substring = input("Enter the substring: ")
if the_substring in the_string_81:
    print(f"Found at index: {the_string_81.index(the_substring)}")
else:
    print("Not found")
#43
email = input("Enter your email: ")
print(f"Original: {email}")
print(f"Results : {email.split("@")[0]}")
#44
a = "VLLL Cooon caaa biettt bayyy"
b = a.split()

final_result = ""

for x in b:
    ket_qua = ""
    for i in range(len(x)):
        if i == 0 or x[i] != x[i-1]:
            ket_qua += x[i]
    final_result += " " +ket_qua

print("Original : ", a)
print("Ket Qua : ", final_result)
#45
a110 = input("Enter string: ")
results_110 = ""
for s110 in a110:
    if s110.isupper() and   results_110:
        results_110 += " "+s110
    else:
        results_110 += s110

print("original string: ", a110)
print("results: ", results_110)
#46
a108 = input("Enter the string: ")
b108 = "ueoaiUEOAI"
results_108 = ""
for c108 in a108:
    if c108 in b108:
        results_108 += c108
    else:
        results_108 += "-" + c108 + "-"
print(f"Original string: {a108}")
print(f"result: {results_108}")
#47
a49 = input("Enter the string: ")
b49 = "ueoaiUEOAI"
result = ""
for c49 in a49:
    if c49 in b49:
        result += c49
print(f"The results: {result}")
print(f"Count: {len(result)}")
#48
a19 = input("Enter string: ")
b19 = input("Enter the character if u want to get the string before it: ")
print(f"The results is '{a19.split(b19)[0]}'")
#49
a18 = input("Enter string: ")
if len(a18) > 3:
    print(a18[:3])
else:
    print(a18)
#50
a21 = input("Enter string: ")
b21 = a21[:4]
count = sum(1 for i21 in b21 if i21.isupper())
if count >=2 :
    print(a21.upper())
else:
    print(a21)

