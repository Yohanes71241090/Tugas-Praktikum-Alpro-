import re

#SOAL 1
def bil_tbk(bilangan):
    x =[]

    for i in sorted(bilangan, reverse=True):
        if len(x) < 3:
            x.append(i)
     
    print(x)
        

bil_tbk([1,6,5,2,3,4])
bil_tbk([1,2,3,4,5,6])
bil_tbk([10, 20, 15, 30, 5, 25])
bil_tbk([-5, -1, -10, -3, -2])
bil_tbk([-10, -20, -15, -11, -30])

#SOAL 2
# def input_done():
#     hasilnya = []
#     while True:
#         x = input("Masukkan Anggka (ketik 'done' untuk berhenti): ").strip().lower()

#         if x == "done":
#             break
        
#         angka = float(x)
#         hasilnya.append(angka)
    
#     rata_rata = sum(hasilnya) / len(hasilnya)
#     print(f"Rata-ratanya adalah: {rata_rata:.2f}")

# input_done()

#SOAL 3
# def kata_unik(file1):
#     with open(file1, 'r') as file:
#         line = file.read().lower()
    
#     kata = line.split()
#     bersih = []
#     for i in kata:
#         if i.isalpha():
#             bersih.append(i)
    
#     unik = sorted(list(set(bersih)))
#     print(unik)
    
# kata_unik("artikel/file1.txt")