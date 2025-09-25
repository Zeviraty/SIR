-- domains.001.create-domain-table migration
CREATE TABLE domain (
    domain TEXT PRIMARY KEY UNIQUE,
    owner TEXT,
    ip TEXT
);
