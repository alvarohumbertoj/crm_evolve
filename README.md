# CRM por Consola en Python

Sistema de gestión de relaciones con clientes (**CRM**) desarrollado en Python con patrón **Layered Architecture** y **Singleton** para la gestión de datos en memoria, diseñado para ser escalable a bases de datos reales.

## 🚀 Características

- Registro de usuarios con validaciones.
- Creación y gestión de facturas asociadas.
- Búsqueda de usuarios por email o nombre.
- Listado de todos los usuarios.
- Consulta de facturas por usuario.
- Resumen financiero por usuario.
- Escalable para conectar a bases de datos reales (MySQL, PostgreSQL, SQLite).

---

## 🛠 Estructura del Proyecto

```
crm_consola/
├── models.py # Modelos de datos (Usuario, Factura)
├── repository.py # Acceso a datos en memoria (Singleton)
├── services.py # Lógica de negocio
├── utils.py # Funciones auxiliares (validaciones)
├── main.py # Presentación por consola (menú)
├── sql_schema.sql # Script SQL de creación de tablas
└── README.md # Documentación
```

---

## 📄 Modelo de Datos

### SQL de creación de tablas

```sql
CREATE TABLE usuarios (
    id_usuario VARCHAR(10) PRIMARY KEY,     -- Ej: USR001
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(80) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(150),
    fecha_registro DATE NOT NULL
);

CREATE TABLE facturas (
    numero_factura VARCHAR(10) PRIMARY KEY, -- Ej: FAC001
    fecha_emision DATETIME NOT NULL,
    descripcion TEXT NOT NULL,
    monto DECIMAL(10,2) NOT NULL CHECK (monto > 0),
    estado ENUM('Pendiente', 'Pagada', 'Cancelada') NOT NULL,
    id_usuario VARCHAR(10) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
```

### 📌 Relación:
Un usuario puede tener muchas facturas (1:N).

### 💻 Instalación y Ejecución
Clonar el repositorio

```
git clone https://github.com/TU_USUARIO/crm_consola.git
cd crm_consola
```

Ejecutar el programa
```
python main.py
```

### 📌 Uso del CRM
Al iniciar, verás un menú con las siguientes opciones:

```
=== SISTEMA CRM ===
1. Registrar nuevo usuario
2. Buscar usuario
3. Crear factura para usuario
4. Mostrar todos los usuarios
5. Mostrar facturas de un usuario
6. Resumen financiero por usuario
7. Salir
```

Puedes registrar usuarios, crear facturas, buscar información y ver el resumen financiero fácilmente.

### 🗄 Modelo Entidad-Relación
El modelo de datos se ha diseñado siguiendo el patrón 1:N entre usuarios y facturas.
Diagrama creado en database.build (puedes generarlo importando sql_schema.sql).

![Modelo de datos del CRM](images/modelo_crm.png)


### 📦 Escalabilidad
Actualmente, los datos se almacenan en memoria mediante un Singleton, pero la arquitectura permite sustituir fácilmente el repositorio por una conexión real a base de datos (MySQL, PostgreSQL, SQLite) sin modificar la lógica de negocio ni la interfaz.