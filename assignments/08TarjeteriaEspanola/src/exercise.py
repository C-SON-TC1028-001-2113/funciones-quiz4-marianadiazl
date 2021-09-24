def tarjetas(x,y):
    t=(x*12)
    p=(y*35)
    if t<p:
        return(t)
    elif p<t:
        return(p)

def main():
    #escribe tu código abajo de esta línea
    t=int(input('Dame la cantidad de pliegos de papel albanene: '))
    p=int(input('Dame la cantidad de plumones: '))
    r=tarjetas(t,p)
    print('El número máximo de tarjetas que se pueden hacer es: ' + str(r))

    

if __name__=='__main__':
    main()
