-- Crear tabla de opciones
CREATE TABLE IF NOT EXISTS opciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    clave INTEGER UNIQUE NOT NULL,
    valor TEXT NOT NULL
);

-- Crear tabla de reparaciones
CREATE TABLE IF NOT EXISTS reparaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL,
    fecha TEXT NOT NULL,
    costo REAL,
    estado TEXT
);

-- Crear tabla de tareas
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    prioridad TEXT,
    fecha_hora TEXT,
    estado TEXT
);

-- Crear tabla de inventario
CREATE TABLE IF NOT EXISTS inventario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    cantidad INTEGER,
    ubicacion TEXT,
    fecha_caducidad TEXT
);

-- Crear tabla de objetivos
CREATE TABLE IF NOT EXISTS objetivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    objetivo TEXT NOT NULL,
    descripcion TEXT,
    fecha_limite TEXT,
    progreso INTEGER
);

-- Crear tabla de plan de trabajo
CREATE TABLE IF NOT EXISTS plan_trabajo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    fecha_hora TEXT
);

-- Crear tabla de calendario
CREATE TABLE IF NOT EXISTS calendario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evento TEXT NOT NULL,
    descripcion TEXT,
    fecha_hora TEXT
);
