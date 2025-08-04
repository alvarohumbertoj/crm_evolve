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