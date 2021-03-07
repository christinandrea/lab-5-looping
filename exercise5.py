#Christina Andrea Putri - Universitas Kristen Duta Wacana

#Selamat datang di FAST FOOD SERBA 20k! Di restoran ini hanya bisa memesan 1 makanan per 1 pemesanan, dengan harga makanan Rp20.000 untuk semua jenis.
# Untuk tambahan topping, penambahan topping lebih dari 3 akan dikenakan biaya @ Rp5.000/topping.
# Tambahan topping maks. 6. 
# Menu makanan : Seblak, spaghetti, fettucini, steak, nasi goreng, lasagna, pizza, nasi ayam, bibimbap, sushi 
#Topping : keju, daging, sayuran, kimchi, sambal, white sauce, bbq sauce, etc.

#Jika ingin membeli lasagna dengan tambahan topping sebanyak 3, berapa total yang harus dibayar? 

#Input => Menu, jumlah pemesanan, apakah ingin topping?, jumlah topping dan jenis topping
#Proses => total biaya makanan, total tambahan topping
#Output => total biaya keseluruhan 

inp_menu = input("Menu : ")
qty = int(input("How many food(s) do you want to buy ? \n =>"))
yn = input("Do you want any additional toppings? (Yes/No) \n => ")

fp = 20000
tp = 5000

def topping(x):
    top = tp*x
    return top 

def total(y):
    food = qty * fp
    return food 


total = total(inp_menu)
if yn=="Yes":
    summa_top = int(input("How many toppings do you want? \n => "))

    for i in range(summa_top<=6):
        inp_top = input("Topping %d : "%(i+1))

    if summa_top>=3 and summa_top<=6 :
        print("You have to pay IDR ", total+topping(summa_top))
    elif summa_top > 6 : 
        print("You can only add 6 additional toppings. Plese re-input your order.")
    else : 
            print("You have to pay IDR",total,"\n FREE TOPPING FOR ANY ADDITIONAL TOPPINGS LESS THAN 3.")
else : 
    print("You have to pay IDR ",total)

        

