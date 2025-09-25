import clase

#esto es para la r2.1
def porcentaje_promedio(envios):
    sum_p = 0
    for envio in envios:
        mot, com = monto_base(envio.monto, envio.alg_comision)
        porc = (com / envio.monto) * 100
        sum_p += porc
    promedio = sum_p / len(envios)
    return round(promedio, 2)

#esto es para el r2.2
def mayor_descuento(envios):
    max_porc = 0
    id_pago_max = ""

    for envio in envios:
        monto_b, comi = monto_base(envio.monto, envio.alg_comision)
        monto_f = monto_final(monto_b, envio.alg_impositivo)
        desc_total = envio.monto - monto_f
        porc_desc = (desc_total / envio.monto) * 100

        if porc_desc > max_porc:
            max_porc = porc_desc
            id_pago_max = envio.identificador_pago
    return id_pago_max

def monto_final(monto_base, alg_imp):
    monto_final = 0
    impuesto = 0

    if alg_imp == 1:
        if monto_base <= 300000:
            impuesto = 0
        elif monto_base > 300000:
            excedente = monto_base - 300000
            impuesto = (25 / 100) * excedente

        monto_final = monto_base - impuesto

    elif alg_imp == 2:
        if monto_base < 50000:
            impuesto = 50
        elif monto_base >= 50000:
            impuesto = 100

        monto_final = monto_base - impuesto

    elif alg_imp == 3:
        impuesto = (3 / 100) * monto_base
        monto_final = monto_base - impuesto

    return monto_final


def monto_base(monto_nominal, alg_comision):
    monto_base = 0
    comision = 0

    if alg_comision == 1:
        comision = (9 / 100) * monto_nominal
        monto_base = monto_nominal - comision

    elif alg_comision == 2:
        if monto_nominal < 50000:
                comision = 0

        elif 50000 <= monto_nominal < 80000:
                comision = (5 / 100) * monto_nominal

        elif monto_nominal >= 80000:
                comision = (7.8 / 100) * monto_nominal

        monto_base = monto_nominal - comision

    elif alg_comision == 3:
        monto_fijo = 100
        if monto_nominal > 25000:
            comision = (6 / 100) * monto_nominal
            comision += monto_fijo
        else:
            comision = monto_fijo
            monto_base = monto_nominal - comision

    elif alg_comision == 4:
        if monto_nominal <= 100000:
            comision = 500
        elif monto_nominal > 100000:
            comision = 1000

        monto_base = monto_nominal - comision

    elif alg_comision == 5:
        if monto_nominal < 500000:
            comision = 0
        elif monto_nominal >= 500000:
            comision = (7 / 100) * monto_nominal

        if comision > 50000:
            comision = 50000

        monto_base = monto_nominal - comision

    return monto_base, comision


def mostrar(v):
    suma_porc = 0
    for envio in v:
        monto_b, comision = monto_base(envio.monto, envio.alg_comision)
        porc_comision = (comision / envio.monto) * 100
        suma_porc += porc_comision
    #r2.1
    promedio_comisiones = suma_porc / len(v)
    print("r2.1:", round(promedio_comisiones, 2))

    #r2.2
    id_pago_max = mayor_descuento(v)
    print("r2.2:", id_pago_max)

def cargar_envios(envios):
    v = []
    envios_leidos_cargados = envios_diferentes = 0
    archivo = open("envios.csv")
    for linea in archivo:
        linea = linea.strip()
        linea_1 = linea.split(",")
        envio = pasaje_desde_csv(linea_1)
        v.append(envio)
        envios_leidos_cargados += 1

    n = len(v)
    for i in range(n):
        if v[i].codigo_pago != v[i].codigo_origen:
            envios_diferentes += 1
    print(envios_leidos_cargados)
    print(envios_diferentes)
    return v

def pasaje_desde_csv(linea):

    partes1 = linea[0].split("|")
    mod_origen = int(partes1[0])
    mod_pago = int(partes1[1])
    id_pago = partes1[2]

    identificacion = linea[1].strip()
    nombre = linea[2].strip()
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

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("Debe cargar primero el vector")
        else:
            print("Programa finalizado. . .")

if __name__ == '__main__':
    principal()
