from tkinter import *
from time import time
import time

menu_inicia =Tk()
menu_inicia.geometry("550x300+200+200")
menu_inicia.title("Trabalho AV1")
menu_inicia.resizable(True,False)
menu_inicia.iconbitmap("img/icon.ico")

chckBox = IntVar()

#Função#
def verificar_usuario():
    l1['text']= text_usuario.get()
    
def menu():
    print(chckBox.get())

def bubble_sorted(array):
    start = time.time()
    time.sleep(0.0000000000001)    
    for current in range(len(array)-1,0,-1):
        for i in range(current):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    timef= time.time()
    start_fin = timef-start

    print(array, "Demorou-->",start_fin)

def shortBubble_sorted(array):
    start = time.time()
    time.sleep(0.0000000000001)   
    exchanges = True
    current = len(array)-1
    while current >0 and exchanges:
        exchanges = False
        for i in range(current):
            if array[i]> array[i+1]:
                exchanges = True
                temp = array[i]
                array[i] = array[i+1]
                array[i+1]= temp
        current = current -1
    timef= time.time()
    start_fin = timef-start

    print(array, "Demorou-->",start_fin)
        
def inserted_sorted(array):
    start = time.time()
    time.sleep(0.0000000000001) 
    for i in range(1, len(array)):
        current_value = array[i]
        current_position = i
        while current_position > 0 and array[current_position - 1] > current_value:
                array[current_position] = array[current_position - 1]
                current_position = current_position - 1
                array[current_position] = current_value
    timef= time.time()
    start_fin = timef-start

    print(array, "Demorou-->",start_fin)

def select_position(array):
    start = time.time()
    time.sleep(0.0000000000001) 
    current = len(array)
    for i in range(current):
        min = i #min = minimo
        for j in range(i +1, current):
            if array[min] > array[j]:
                min = j
        (array[i],array[min]) = (array[min], array[i])
    timef= time.time()
    start_fin = timef-start

    print(array, "Demorou-->",start_fin)

def str_int(array):
   a=array.split()
   list=[]
   for i in range(len(a)):
      b = a[i]
      array.append(int(b))
   print(array)

def shell_sort_help(array, n):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = array[i]
            j = i
            while j >= intervalo and array[j - intervalo] > temp:
                array[j] = array[j - intervalo]
                j -= intervalo

            array[j] = temp
        intervalo //= 2
def shell_sort(array):
    timei = time.time()
    time.sleep(0.0000000000001)
    n1=len(array)
    shell_sort_help(array,n1)
    timef = time.time()
    timeend = timef - timei

    print(array,"Demorou-->",timeend)


def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quick_sort_help(array, low, high):

  if low < high:

    pi = partition(array, low, high)

    quick_sort_help(array, low, pi - 1)
    quick_sort_help(array, pi + 1, high)


def quick_sort(array):
  start = time.time()
  time.sleep(0.0000000000001)
  quick_sort_help(array, 0, len(array) - 1)
  start_fin = time.time()
  timeend = start_fin - start

  print(array,"Demorou-->",timeend)

def mergeSort(array):
    start = time.time()
    time.sleep(0.0000000000001)
    if len(array) > 1:

        
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    start_fin = time.time()
    timeend = start - start_fin
    print(array,"Demorou-->",timeend)


####fim



#---------------------dimensão----------------#
largura = 1000
altura = 750
#-----------------resolução-----------#
largura_screen = menu_inicia.winfo_screenwidth()
altura_screen = menu_inicia.winfo_screenheight()

#-------------------posição-------------------#
posx = largura_screen/2-largura/2
posy = altura_screen/2 - altura/2

#---------------------geometry-------------------#
menu_inicia.geometry("%dx%d+%d+%d" % (largura, altura, posx,posy))

#---------------------Widgets-------------------------------#
frame_login=Frame(menu_inicia)

label_usuario=Label(frame_login, text="Username:")
text_usuario=Entry(frame_login)
l1 = Label(frame_login)
label_qtd=Label(frame_login, text="Quantidade:")
text_qtd=Entry(frame_login)
l2 = Label(frame_login)
btn_acesso=Button(frame_login, text="Executar", command=verificar_usuario)

label_usuario.grid(row=0, column=0)
text_usuario.grid(row=0, column=1)
label_qtd.grid(row=1, column=0)
text_qtd.grid(row=1, column=1)
l2.grid(row=1, column=5)
check.grid(row=3, column=5)
check1.grid(row=3, column=6)
check2.grid(row=3, column=7)
check3.grid(row=3, column=8)
btn_acesso.grid(row=3,column=3)
l1.grid()
frame_login.grid()


check = Checkbutton(
    menu_inicia,
    variable=chckBox,
    text="bubble sorted",
    command= menu
)
check1 = Checkbutton(
    menu_inicia,
    variable=chckBox,
    text="short Bubble sorted",
    command= menu
)
check2 = Checkbutton(
    menu_inicia,
    variable=chckBox,
    text="inserted sorted",
    command= menu
)
check3 = Checkbutton(
    menu_inicia,
    variable=chckBox,
    text="select position",
    command= menu
)

menu_inicia.mainloop()


