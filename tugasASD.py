#Nama : Taufik Hidayat
#Kelas : Sistem Informasi B '22
#NIM : 2209116097
def partition(l, bwh, atas): #Melakukan quicksorting pada setiap partisi yang telah dibagi
    # print("List : ",l,"\n")
    pivot = l[atas]
    index = bwh
    current = bwh
    while (current < atas) :
        if l[current] <= pivot:
            l[index],l[current]=l[current],l[index] #Swapping antara value[index] dan value[current]
            index += 1
        current += 1
    l[index],l[atas] = l[atas],l[index] #Swapping antara value[pivot] dan value[index]
    # print("Partisi : ",l,"\n")
    return index

def quicksort(l, bwh, atas): #Melakukan pembagian partisi
  if bwh < atas:
    index = partition(l, bwh, atas) #mendapatkan index untuk membagi partisi
    quicksort(l, bwh, index-1) #quicksorting partisi kiri (lebih kecil dari pivot)
    quicksort(l, index+1, atas) #quicksorting partisi kanan (lebih besar dari pivot)
    return l

def pisah_int_list(pisahin): #Untuk memisahkan Integer dan list
    global integ
    global list1

    integ = [] #angka
    list1 = [] #angka dan list pisahin
    # while pisahin :
    while True:
            print("ini pisahin",pisahin)
            print("ini integ",integ)
            print('ini list1',list1)
            if len(pisahin) == 0:
                print("habis")
                break
            elif type(pisahin[0]) == int:
                integ.append(pisahin[0])
                pisahin.pop(0)
            else:
                list1.extend(pisahin[0])
                pisahin.pop(0)
                pisahin.extend(list1)
                list1.clear()
                print("ini list1",list1)
angka = [12, 1, [22,3,[8,14,[10,[13,[17]]]],18], 2, 6, [11,[15,16]], 90,[89]] 
pisah_int_list(angka)
akhir = quicksort(integ,0,len(integ)-1)
print("Setelah disort : ",akhir)
