calificacion = input('por favor ingrese una calificación: ')
try:
    calificacion = float(calificacion)
    if 0.0<= calificacion < 0.6:
        print('insuficiente')
    elif 0.6 <= calificacion < 0.7:
        print('Suficiente')
    elif 0.7 <= calificacion < 0.8:
        print('bien')    
    elif 0.8 <= calificacion < 0.9:
        print('notable')  
    elif 0.9<=calificacion<=1.0:
        print ('sobresaliente')       
    else:
        print('fuera de rango')
except:
    print(input('calificacion: '))         
             
