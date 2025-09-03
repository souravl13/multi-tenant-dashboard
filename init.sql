CREATE TABLE IF NOT EXISTS tenants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    users INT NOT NULL,
    active INT NOT NULL
);

INSERT INTO tenants (name, users, active) VALUES
('Tenant A', 12, 8),
('Tenant B', 25, 15),
('Tenant C', 40, 32);
