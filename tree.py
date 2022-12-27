sayi = 10

def yilbasi_agaci_ciz():
    print("yılbası ağacı ciziliyorrr:") 
    for satir in range(sayi):
        print(" " *(sayi - satir -1)+ '*'*(2*satir+1))
        
yilbasi_agaci_ciz()
