from models import Usuario, Factura
from repository import Repositorio
from utils import email_valido

class CRMService:
    """Capa de lógica de negocio del CRM."""
    def __init__(self):
        self.repo = Repositorio()

    def registrar_usuario(self, nombre, apellidos, email, telefono=None, direccion=None):
        if not nombre or not apellidos or not email_valido(email):
            return "❌ Datos inválidos."
        if self.repo.buscar_usuario_por_email(email):
            return "❌ Email ya registrado."
        
        nuevo_usuario = Usuario(f"USR{len(self.repo.usuarios)+1:03}", nombre, apellidos, email, telefono, direccion)
        self.repo.agregar_usuario(nuevo_usuario)
        return f"✅ Usuario {nuevo_usuario.id} registrado."

    def crear_factura(self, email, descripcion, monto, estado):
        usuario = self.repo.buscar_usuario_por_email(email)
        if not usuario:
            return "❌ Usuario no encontrado."
        if monto <= 0:
            return "❌ Monto inválido."
        
        num_factura = f"FAC{len(self.repo.facturas)+1:03}"
        nueva_factura = Factura(num_factura, email, descripcion, monto, estado)
        self.repo.agregar_factura(nueva_factura)
        return f"✅ Factura {num_factura} creada."

    def resumen_financiero(self):
        resumen = []
        for u in self.repo.usuarios:
            facturas = self.repo.facturas_por_email(u.email)
            total = sum(f.monto for f in facturas)
            pagadas = sum(f.monto for f in facturas if f.estado == "Pagada")
            pendientes = sum(f.monto for f in facturas if f.estado == "Pendiente")
            resumen.append((u.nombre, total, pagadas, pendientes))
        return resumen
