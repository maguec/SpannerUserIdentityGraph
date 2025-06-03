-- Node Tables

CREATE TABLE ShippingAddress (
  id STRING(36) NOT NULL,
  address STRING(MAX),
  sus INT64,
  address_Tokens TOKENLIST AS (TOKENIZE_NGRAMS(address, ngram_size_min=>3, ngram_size_max=>4)) HIDDEN,
) PRIMARY KEY (id);

CREATE SEARCH INDEX StreetIndex ON ShippingAddress(address_Tokens);

CREATE TABLE SalesOrder (
  id STRING(36) NOT NULL,
  sus INT64,
) PRIMARY KEY (id);

CREATE TABLE IP (
  id STRING(36) NOT NULL,
  ip STRING(MAX),
  sus INT64,
) PRIMARY KEY (id);

CREATE TABLE CC(
  id STRING(36) NOT NULL,
  last4 STRING(4),
  zip STRING(5),
  sus INT64,
) PRIMARY KEY (id);

CREATE TABLE Device (
  id STRING(36) NOT NULL,
  sus INT64,
) PRIMARY KEY (id);


CREATE TABLE Email (
  id STRING(36) NOT NULL,
  email STRING(MAX),
  sus INT64,
  email_Tokens TOKENLIST AS (TOKENIZE_NGRAMS(email, ngram_size_min=>3, ngram_size_max=>4)) HIDDEN,
) PRIMARY KEY (id);

CREATE SEARCH INDEX EmailIndex ON Email(email_Tokens);
CREATE INDEX email_idx ON Email (email);

-- Edge Tables

CREATE TABLE SalesOrderHasShippingAddress (
  id STRING(36) NOT NULL,
  to_id STRING(36) NOT NULL,
  ts TIMESTAMP,
  FOREIGN KEY(to_id) REFERENCES ShippingAddress(id)
) PRIMARY KEY (id, to_id, ts),
INTERLEAVE IN PARENT SalesOrder ON DELETE CASCADE;

CREATE TABLE SalesOrderHasEmail (
  id STRING(36) NOT NULL,
  to_id STRING(36) NOT NULL,
  ts TIMESTAMP,
  FOREIGN KEY(to_id) REFERENCES Email(id)
) PRIMARY KEY (id, to_id, ts),
INTERLEAVE IN PARENT SalesOrder ON DELETE CASCADE;

CREATE TABLE HasDevice (
  id STRING(36) NOT NULL,
  to_id STRING(36) NOT NULL,
  ts TIMESTAMP,
  FOREIGN KEY(to_id) REFERENCES Device(id)
) PRIMARY KEY (id, to_id, ts),
INTERLEAVE IN PARENT Email ON DELETE CASCADE;

CREATE TABLE EmailHasCC (
  id STRING(36) NOT NULL,
  to_id STRING(36) NOT NULL,
  ts TIMESTAMP,
  FOREIGN KEY(to_id) REFERENCES CC(id)
) PRIMARY KEY (id, to_id, ts),
INTERLEAVE IN PARENT Email ON DELETE CASCADE;

CREATE TABLE DeviceHasCC (
  id STRING(36) NOT NULL,
  to_id STRING(36) NOT NULL,
  ts TIMESTAMP,
  FOREIGN KEY(to_id) REFERENCES CC(id)
) PRIMARY KEY (id, to_id, ts),
INTERLEAVE IN PARENT Device ON DELETE CASCADE;

CREATE TABLE DeviceHasIP (
  id STRING(36) NOT NULL,
  to_id STRING(36) NOT NULL,
  ts TIMESTAMP,
  FOREIGN KEY(to_id) REFERENCES IP(id)
) PRIMARY KEY (id, to_id, ts),
INTERLEAVE IN PARENT Device ON DELETE CASCADE;

-- Property Graph

CREATE OR REPLACE PROPERTY GRAPH UserIdentity

  NODE TABLES (
    Device,
    IP,
    CC,
    ShippingAddress,
    SalesOrder,
    Email
  )

  EDGE TABLES (
    HasDevice
      SOURCE KEY (id) REFERENCES Email (id)
      DESTINATION KEY (to_id) REFERENCES Device (id)
      LABEL HAS_DEVICE,
    DeviceHasIP
      SOURCE KEY (id) REFERENCES Device (id)
      DESTINATION KEY (to_id) REFERENCES IP (id)
      LABEL HAS_IP,
    DeviceHasCC
      SOURCE KEY (id) REFERENCES Device (id)
      DESTINATION KEY (to_id) REFERENCES CC (id)
      LABEL DEVICE_HAS_CC,
    SalesOrderHasShippingAddress
      SOURCE KEY (id) REFERENCES SalesOrder (id)
      DESTINATION KEY (to_id) REFERENCES ShippingAddress (id)
      LABEL HAS_ADDRESS,
    SalesOrderHasEmail
      SOURCE KEY (id) REFERENCES SalesOrder (id)
      DESTINATION KEY (to_id) REFERENCES Email (id)
      LABEL HAS_EMAIL,
    EmailHasCC
      SOURCE KEY (id) REFERENCES Email (id)
      DESTINATION KEY (to_id) REFERENCES CC (id)
      LABEL EMAIL_HAS_CC
  );
