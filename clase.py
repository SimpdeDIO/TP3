class Envio:
    def __init__(self, cod, id, nom, tasa, mont, idcom, idimp):
        self.codigo = cod
        self.identificacion = id
        self.nombre = nom
        self.tasa = tasa
        self.monto = mont
        self.alg_comision = idcom
        self.alg_impositivo = idimp

    def __str__(self):
        r = "Orden de pago: {:<5} - Identificacion: {:<5} - Destinatario: {:<5} - Tasa de conversion: {:<5} - Monto nominal: {:<5} "
        return r.format(self.codigo, self.identificacion, self.nombre, self.tasa, self.monto)