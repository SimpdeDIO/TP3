import clase

def cargar_envios(envios):
    v = []
    archivo = open("envios.csv")
    for linea in archivo:
        linea_1 = linea.split(",")
        envio = pasaje_desde_csv(linea_1)
        v.append(envio)
    return v




def pasaje_desde_csv(linea):
    # 01|05|AB4F35
    partes1 = linea[0].split("|")
    print(partes1)
    mod_origen = int(partes1[0])
    mod_pago = int(partes1[1])
    id_pago = partes1[2]
    identificacion = linea[1]
    nombre = linea[2]
    tasa = float(linea[3])
    monto = int(linea[4])
    alg_comision = int(linea[5])
    alg_impositivo = int(linea[6])
    envio = clase.Envio(mod_origen, mod_pago, id_pago, identificacion, nombre, tasa, monto, alg_comision, alg_impositivo)
    return envio


def principal():
    v = []
    op = -1
    while op != 0:
        print("1. Cargar Envíos")
        print("2. Mostrar Resultados")
        print("0. Salir")
        op = int(input("Ingresa una opcionde del menu: "))

        if op == 1:
            v = cargar_envios("envios.csv")
            print(v)
        elif op == 2:
            if v:
                pass
            else:
                print("Debe cargar primero el vector")
        else:
            print("Programa finalizado. . .")

if __name__ == '__main__':
    principal()
