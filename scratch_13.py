import sqlite3
CREATE
TABLE
EMPLOYEES(
    EMP_ID
CHAR(9)
NOT
NULL,
F_NAME
VARCHAR(15)
NOT
NULL,
L_NAME
VARCHAR(15)
NOT
NULL,
SSN
CHAR(9),
B_DATE
DATE,
SEX
CHAR,
ADDRESS
VARCHAR(30),
JOB_ID
CHAR(9),
SALARY
DECIMAL(10, 2),
MANAGER_ID
CHAR(9),
DEP_ID
CHAR(9)
NOT
NULL,
PRIMARY
KEY(EMP_ID));

CREATE
TABLE
JOB_HISTORY(
    EMPL_ID
CHAR(9)
NOT
NULL,
START_DATE
DATE,
JOBS_ID
CHAR(9)
NOT
NULL,
DEPT_ID
CHAR(9),
PRIMARY
KEY(EMPL_ID, JOBS_ID));

CREATE
TABLE
JOBS(
    JOB_IDENT
CHAR(9)
NOT
NULL,
JOB_TITLE
VARCHAR(15),
MIN_SALARY
DECIMAL(10, 2),
MAX_SALARY
DECIMAL(10, 2),
PRIMARY
KEY(JOB_IDENT));

CREATE
TABLE
DEPARTMENTS(
    DEPT_ID_DEP
CHAR(9)
NOT
NULL,
DEP_NAME
VARCHAR(15),
MANAGER_ID
CHAR(9),
LOC_ID
CHAR(9),
PRIMARY
KEY(DEPT_ID_DEP));

CREATE
TABLE
LOCATIONS(
    LOCT_ID
CHAR(9)
NOT
NULL,
DEP_ID_LOC
CHAR(9)
NOT
NULL,
PRIMARY
KEY(LOCT_ID, DEP_ID_LOC));
insert
into
JOBS
(JOB_IDENT, JOB_TITLE, MIN_SALARY, MAX_SALARY)
values
('abc', 'student', 5000.00, 1000000),
('ac', 'student', 1000.00, 8000000),
('abcd', 'student', 15000.00, 16000000),
('abcde', 'student', 25000.00, 19000000)
;
select *
from JOBS
