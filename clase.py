class Envio:
    def __init__(self, cod_origen, cod_pago, id_pago, id, nom, tasa, mont, idcom, idimp):
        self.codigo_origen = cod_origen
        self.codigo_pago = cod_pago
        self.identificador_pago = id_pago
        self.identificacion = id
        self.nombre = nom
        self.tasa = tasa
        self.monto = mont
        self.alg_comision = idcom
        self.alg_impositivo = idimp

    def __str__(self):
        r = "Moneda de Origen: {:<5}- Moneda de pago: {:<5} - Identificador de pago: {:<5} - Identificacion: {:<5} - Destinatario: {:<5} - Tasa de conversion: {:<5} - Monto nominal: {:<5} "
        return r.format(self.codigo_origen, self.codigo_pago, self.identificador_pago, self.identificacion, self.nombre, self.tasa, self.monto)
