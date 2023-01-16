class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print('Coordenada del punto')
        print('(', self.x, ',', self.y, ')')
    
    def imprimir_cuadrante(self):
        if self.x > 0 and self.y > 0:
            print('El punto se encuentra en el primer cuadrante')
        elif self.x < 0 and self.y > 0:
            print('El punto se encuentra en el segundo cuadrante') 
        elif self.x < 0 and self.y < 0:
            print('El punto se encuentra en el tercer cuadrante')
        else:
            print('El punto está en el cuarto cuadrante')


x = int(input('ingrese la coordenada en x: '))
y = int(input('ingrese la coordenada en y: '))

punto1 = Punto(x,y)
punto1.imprimir()
punto1.imprimir_cuadrante()


        