CREATE TABLE tiendas (
  id SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  barrio TEXT NOT NULL
);

CREATE TABLE productos (
  id SERIAL PRIMARY KEY,
  tienda_id INT REFERENCES tiendas(id),
  nombre TEXT NOT NULL,
  precio NUMERIC(10,2) NOT NULL
);

CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  tienda_id INT REFERENCES tiendas(id),
  cliente TEXT NOT NULL,
  creado_en TIMESTAMP DEFAULT now()
);

INSERT INTO tiendas (nombre, barrio) VALUES
  ('Tienda Doña Rosa', 'Chapinero'),
  ('Minimercado El Vecino', 'Teusaquillo');

INSERT INTO productos (tienda_id, nombre, precio) VALUES
  (1, 'Pan', 500),
  (1, 'Leche', 3200),
  (2, 'Arroz', 4500);
