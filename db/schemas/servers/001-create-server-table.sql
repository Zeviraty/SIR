-- servers.001.create-server-table migration
CREATE TABLE server (
    name TEXT PRIMARY KEY UNIQUE,
    ip TEXT
);
