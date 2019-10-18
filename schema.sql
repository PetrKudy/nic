CREATE SCHEMA AUTHORIZATION nic;

CREATE SEQUENCE nic.domain_id_seq;
CREATE TABLE nic.domain(
	id integer not null default nextval('nic.domain_id_seq'::regclass) primary key,
	fgdn character varying(255) not null,
	crdate timestamp without time zone not null default now(),
	erdate timestamp without time zone
	);

CREATE TYPE nic.flag_type as ENUM ('EXPIRED',
			       'OUTZONE',
			       'DELETE_CANDIDATE'
				);

CREATE SEQUENCE nic.domain_flag_id_seq;
CREATE TABLE nic.domain_flag(
	id integer not null default nextval('nic.domain_flag_id_seq'::regclass) primary key,
	domain_id integer not null REFERENCES nic.domain(id),
	flag nic.flag_type not null,
	valid_from timestamp without time zone not null,
	valid_to timestamp without time zone
	);

\COPY nic.domain FROM 'domain_table.csv' DELIMITER ',' CSV HEADER;
\COPY nic.domain_flag FROM 'domain_flag_table.csv' DELIMITER ',' CSV HEADER;

SELECT *
FROM nic.domain 
JOIN nic.domain_flag 
ON nic.domain.id = nic.domain_flag.domain_id
WHERE nic.domain_flag.flag != 'EXPIRED'
AND nic.domain.erdate IS NULL;

SELECT DISTINCT domain.fgdn
FROM nic.domain 
JOIN nic.domain_flag 
ON nic.domain.id = nic.domain_flag.domain_id
WHERE domain.fgdn in (
		SELECT DISTINCT domain.fgdn
		FROM nic.domain 
		JOIN nic.domain_flag 
		ON nic.domain.id = nic.domain_flag.domain_id
		WHERE nic.domain_flag.flag = 'EXPIRED')
AND domain.fgdn in (
		SELECT DISTINCT domain.fgdn
		FROM nic.domain 
		JOIN nic.domain_flag 
		ON nic.domain.id = nic.domain_flag.domain_id
		WHERE nic.domain_flag.flag = 'OUTZONE'
);





