print("Perngulangan 1")
for i in range(5):
         print(i)



print("Perngulangan 2")
for i in range(1,6):
    print(i)


print("Perngulangan dengan step 3")
for i in range(3,20,3):
    print(i)
    


print("Latihan Perngulangan 1")
for i in (1,2,3,4,5):
    print("Inipengulangan ke -",i)

    
print ("Latihan Perngulangan 2")
# pengulangan sebanyak 8 kali
for i in ["Rawon", "Nasi Kuning", "Soto Madura", "Kupat Tahu", "Kerak Telor", "Rendang Batoko", "Pempek Selam", "Ayam Betutu"] :
 print (i, " adalah masakan khas nusantara …")

print ("Latihan Perngulangan 3")
# pengulangan sebanyak 5 kali for i in "abcde":\
for i in "abcde":
      print (i, " adalah alfabet")

print ("Latihan Pernghulangan 4")
print("PROGRAM PYTHON MENGHITUNG NILAI RATA-RATA")
banyakdata = 5
i = 0
print()
jum = 0
while i < 5 :
 nilai = int(input("Masukkan data ke-%d: " % (i+1)))
 i = i + 1
 jum = jum + nilai
 rata = jum / banyakdata
print("\nRata-rata = %0.2f" % rata)


print("Menampilkan Deret Bilangan Fibonacci")
n = int(input("Masukkan jumlah angka Fibonacci: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


print("Menentukan Bilangan Prima")
number = int(input("Masukkan angka: "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "adalah bilangan prima.")
else:
    print(number, "bukan bilangan prima.")    
