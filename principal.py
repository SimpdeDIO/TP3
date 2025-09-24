def principal():
    v = []
    op = -1
    while op != 0:
        print("1. Cargar Envíos")
        print("2. Mostrar Resultados")
        print("0. Salir")
        op = int(input("Ingresa una opcionde del menu: "))

        if op == 1:
            pass
        elif op == 2:
            if v:
                pass
            else:
                print("Debe cargar primero el vector")
        else:
            print("Programa finalizado. . .")

if __name__ == '__main__':
    principal()