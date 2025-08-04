from datetime import datetime

class Usuario:
    """Representa un usuario en el CRM."""
    def __init__(self, user_id, nombre, apellidos, email, telefono=None, direccion=None):
        self.id = user_id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono or "No especificado"
        self.direccion = direccion or "No especificado"
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y")

    def __repr__(self):
        return f"{self.id} - {self.nombre} {self.apellidos} ({self.email})"


class Factura:
    """Representa una factura en el CRM."""
    def __init__(self, num_factura, email_usuario, descripcion, monto, estado):
        self.numero = num_factura
        self.email_usuario = email_usuario
        self.descripcion = descripcion
        self.monto = monto
        self.estado = estado
        self.fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    def __repr__(self):
        return f"{self.numero} - {self.descripcion} - {self.monto}€ ({self.estado})"