class Repositorio:
    """Gestiona datos en memoria usando Singleton."""
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.usuarios = []
            cls._instancia.facturas = []
        return cls._instancia

    # Métodos para usuarios
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario_por_email(self, email):
        return next((u for u in self.usuarios if u.email == email), None)

    def buscar_usuarios_por_nombre(self, nombre):
        return [u for u in self.usuarios if nombre.lower() in u.nombre.lower()]

    # Métodos para facturas
    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def facturas_por_email(self, email):
        return [f for f in self.facturas if f.email_usuario == email]
