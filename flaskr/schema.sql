-- Drop tables if they exist
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS category_supplier;
DROP TABLE IF EXISTS standard;

-- Create tables
CREATE TABLE category_supplier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE supplier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    cnpj VARCHAR(14) UNIQUE NOT NULL,
    cep VARCHAR(8) NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category_supplier(id)
);

CREATE TABLE standard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag VARCHAR(80) NOT NULL,
    description VARCHAR(255) NOT NULL,
    year VARCHAR(4) NOT NULL,
    status BOOLEAN NOT NULL,
    verificate_date DATE NOT NULL,
    observation TEXT NOT NULL
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE post (
    -- Defina a estrutura da tabela 'post' se necessário
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Outros campos conforme necessário
);