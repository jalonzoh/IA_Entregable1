# IA_Entregable1
Entregable 1 - Guayerd IA

# Tema General: 
## Optimización de Estrategias de Ventas y Fidelización de Clientes
Este tema abarca cómo mejorar la forma en que vendes y cómo retienes a tus clientes, lo cual es fundamental para cualquier negocio.

# Problema Específico: 
## Identificación de Clientes de Alto Valor y Productos Estrella para Aumentar la Rentabilidad
Muchas empresas tienen datos de ventas, pero no los usan para entender quiénes son sus mejores clientes o qué productos generan más ingresos. Este problema busca transformar esos datos en conocimiento útil.

# Solución: 
Desarrollo de un Sistema de Análisis de Ventas y Segmentación de Clientes y Popularidad de Productos

# Informacion de las Tablas

## Tabla: clientes
### Definición:
Contiene la información maestra de cada cliente que ha interactuado con la empresa (ha comprado, se ha registrado, etc.). Es el "quién" en el contexto de las transacciones.

### Estructura (Atributos/Columnas Comunes):
id_cliente (Clave Primaria, identificador único)
nombre_cliente
apellido_cliente
email
telefono
direccion
ciudad
pais
fecha_registro
tipo_cliente (ej. 'Individual', 'Empresa', 'VIP')
fecha_nacimiento (para segmentación demográfica)

### Tipos de Datos (Ejemplos):
id_cliente: INT, UUID, VARCHAR(50)
nombre_cliente, apellido_cliente: VARCHAR(100)
email: VARCHAR(255)
telefono: VARCHAR(20)
direccion, ciudad, pais: VARCHAR(255), VARCHAR(100), VARCHAR(50)
fecha_registro, fecha_nacimiento: DATE, DATETIME
tipo_cliente: VARCHAR(50)

### Escala (ejemplo de registros):
* Pequeña: Cientos a miles (ej. startup, negocio local).
* Mediana: Decenas de miles a cientos de miles (ej. e-commerce en crecimiento).
* Grande: Millones a decenas de millones (ej. retailer nacional, telecomunicaciones).
* Muy Grande: Cientos de millones (ej. grandes plataformas globales).

## Tabla: productos

### Definición:
Almacena la información maestra de cada producto que la empresa vende u ofrece. Es el "qué" se vende.

### Estructura (Atributos/Columnas Comunes):
id_producto (Clave Primaria, identificador único)
nombre_producto
descripcion
precio_unitario
costo_unitario (si se usa para análisis de rentabilidad)
categoria
marca
stock_actual (si se integra con inventario)
fecha_creacion
activo (BOOLEAN: si el producto está disponible)

### Tipos de Datos (Ejemplos):
id_producto: INT, UUID, VARCHAR(50)
nombre_producto: VARCHAR(255)
descripcion: TEXT
precio_unitario, costo_unitario: DECIMAL(10, 2), FLOAT
categoria, marca: VARCHAR(100)
stock_actual: INT
fecha_creacion: DATE, DATETIME
activo: BOOLEAN

### Escala (ejemplo de registros):
* Pequeña: Decenas a cientos (ej. boutique, pequeña fábrica).
* Mediana: Miles a decenas de miles (ej. e-commerce con catálogo variado).
* Grande: Cientos de miles a millones (ej. supermercado, distribuidor global).

## Tabla: ventas

### Definición:
Registra las transacciones de ventas principales, actuando como un encabezado para cada pedido o compra. Es el "cuándo" y "quién" de la transacción.

### Estructura (Atributos/Columnas Comunes):
id_venta (Clave Primaria, identificador único de la transacción)
id_cliente (Clave Foránea a clientes.id_cliente)
fecha_venta
hora_venta
total_venta
estado_venta (ej. 'Completado', 'Pendiente', 'Cancelado')
metodo_pago
id_sucursal (si aplica)

### Tipos de Datos (Ejemplos):
id_venta: INT, UUID, VARCHAR(50)
id_cliente: INT, UUID, VARCHAR(50) (Debe coincidir con el tipo en clientes.id_cliente)
fecha_venta: DATE, DATETIME
hora_venta: TIME
total_venta: DECIMAL(10, 2), FLOAT
estado_venta, metodo_pago: VARCHAR(50)
id_sucursal: INT, VARCHAR(50)

### Escala (ejemplo de registros):
* Pequeña: Cientos a miles (ej. negocio local).
* Mediana: Decenas de miles a cientos de miles al mes/año.
* Grande: Millones a decenas de millones al mes/año.
* Muy Grande: Cientos de millones a miles de millones (grandes retailers, e-commerce global).

## Tabla: detalle_ventas

### Definición:
Contiene el detalle de cada artículo individual vendido dentro de una transacción de venta específica. Es el "cuántos" de "qué" en cada venta. Es una tabla de hechos transaccionales.

### Estructura (Atributos/Columnas Comunes):
id_detalle (Clave Primaria, identificador único de la línea de detalle)
id_venta (Clave Foránea a ventas.id_venta)
id_producto (Clave Foránea a productos.id_producto)
cantidad (corresponde a tu cantidad_cajas si es por cajas)
precio_unitario_venta (el precio al que se vendió en esa transacción específica, puede variar si hay ofertas)
subtotal_linea (cantidad * precio_unitario_venta)
descuento_linea (si aplica a ese artículo)

### Tipos de Datos (Ejemplos):

id_detalle: INT, UUID, VARCHAR(50)
id_venta: INT, UUID, VARCHAR(50) (Debe coincidir con el tipo en ventas.id_venta)
id_producto: INT, UUID, VARCHAR(50) (Debe coincidir con el tipo en productos.id_producto)
cantidad: INT, SMALLINT
precio_unitario_venta, subtotal_linea, descuento_linea: DECIMAL(10, 2), FLOAT

### Escala (ejemplo de registros):
* Pequeña: Millares (miles) (ej. negocio local).
* Mediana: Cientos de miles a millones (ej. e-commerce con muchos ítems por pedido).
*Grande: Decenas de millones a cientos de millones (grandes retailers).
*Muy Grande: Miles de millones (grandes plataformas con alto volumen transaccional). Esta tabla suele ser la más grande de un sistema de ventas.

