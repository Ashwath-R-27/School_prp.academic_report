
CREATE TABLE sslc_result (
    reg_no integer PRIMARY KEY,
    class varchar(2),
    name varchar(30),
    tamil integer,
    english integer,
    maths integer,
    science integer,
    social integer,
    total integer
);

CREATE TABLE hsc_result_cs (
    reg_no integer PRIMARY KEY,
    class varchar(2),
    name varchar(30),
    lang integer,
    eng integer,
    phy integer,
    chem integer,
    csc integer,
    maths integer,
    total integer,
    cut_off real
);

CREATE TABLE hsc_result_bio (
    reg_no integer PRIMARY KEY,
    class varchar(2),
    name varchar(30),
    lang integer,
    eng integer,
    phy integer,
    chem integer,
    bio integer,
    maths integer,
    total integer,
    cut_off real
);
