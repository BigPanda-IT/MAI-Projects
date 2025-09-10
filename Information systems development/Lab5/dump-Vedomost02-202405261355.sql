--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

-- Started on 2024-05-26 13:55:19

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE "Vedomost02";
--
-- TOC entry 3353 (class 1262 OID 62453)
-- Name: Vedomost02; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE "Vedomost02" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';


\connect "Vedomost02"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 3354 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 219 (class 1259 OID 62518)
-- Name: bottom_table; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.bottom_table (
    b1 integer,
    b2 character varying
);


--
-- TOC entry 215 (class 1259 OID 62502)
-- Name: left_table; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.left_table (
    l_code integer NOT NULL,
    name_ character varying,
    key1 integer,
    key2 integer
);


--
-- TOC entry 214 (class 1259 OID 62501)
-- Name: left_table_l_code_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.left_table ALTER COLUMN l_code ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.left_table_l_code_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 223 (class 1259 OID 62531)
-- Name: professors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.professors (
    id integer NOT NULL,
    kafedra integer NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    patronymic character varying NOT NULL
);


--
-- TOC entry 222 (class 1259 OID 62530)
-- Name: professors_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.professors ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.professors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 62508)
-- Name: right_table; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.right_table (
    r_code integer NOT NULL,
    city character varying,
    key3 integer
);


--
-- TOC entry 216 (class 1259 OID 62507)
-- Name: right_table_r_code_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.right_table ALTER COLUMN r_code ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.right_table_r_code_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 221 (class 1259 OID 62525)
-- Name: third_year_students; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.third_year_students (
    id integer NOT NULL,
    gruppa integer NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    patronymic character varying NOT NULL,
    zachotka_id integer NOT NULL,
    kafedra integer NOT NULL,
    graduation_year integer NOT NULL
);


--
-- TOC entry 220 (class 1259 OID 62524)
-- Name: third_year_students_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.third_year_students ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.third_year_students_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 218 (class 1259 OID 62513)
-- Name: top_table; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.top_table (
    t1 integer,
    t2 character varying
);


--
-- TOC entry 3343 (class 0 OID 62518)
-- Dependencies: 219
-- Data for Name: bottom_table; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.bottom_table (b1, b2) FROM stdin;
1012	qwe
1013	qer
1014	qrt
1015	qty
10013	qyu
1016	qui
10017	qio
1018	qop
1019	qpp
1012	qwe
1013	qer
1014	qrt
1015	qty
10013	agh
1016	qui
10017	qio
1018	qop
1019	qpp
\.


--
-- TOC entry 3339 (class 0 OID 62502)
-- Dependencies: 215
-- Data for Name: left_table; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.left_table (l_code, name_, key1, key2) FROM stdin;
1	Артем	1717	523414
2	Роман	1717	513141
3	Елена	1918	148964
4	Денис	2017	189657
5	Екатерина	1890	145893
6	Никита	1817	149728
7	Петр	1918	551734
8	Сергей	2031	412313
9	Настя	3131	732943
10	Семен	2314	843923
\.


--
-- TOC entry 3347 (class 0 OID 62531)
-- Dependencies: 223
-- Data for Name: professors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.professors (id, kafedra, first_name, last_name, patronymic) FROM stdin;
1	805	Александр	Громов	Николаевич
2	811	Сергей	Нефедов	Викторович
3	803	Михаил	Дыбнов	Александрович
4	804	Степан	Климкин	Сергеевич
5	809	Елизавета	Лапокина	Михайлович
\.


--
-- TOC entry 3341 (class 0 OID 62508)
-- Dependencies: 217
-- Data for Name: right_table; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.right_table (r_code, city, key3) FROM stdin;
1	Владимир	20
2	Собинка	20
3	Кинешма	19
4	Юрьевец	22
5	Юрьевец	24
6	Орг-труд	26
7	Владимир	34
8	Москва	31
9	Рязань	51
10	Саратов	18
\.


--
-- TOC entry 3345 (class 0 OID 62525)
-- Dependencies: 221
-- Data for Name: third_year_students; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.third_year_students (id, gruppa, first_name, last_name, patronymic, zachotka_id, kafedra, graduation_year) FROM stdin;
1	5	Сергей	Волков	Олегович	10345	805	3
2	2	Роман	Смирнов	Викторович	14513	804	3
3	3	Елена	Запелова	Михайловна	17163	809	3
4	5	Денис	Борисов	Данилович	19001	811	3
5	2	Екатерина	Косарева	Юрьевна	18902	803	3
6	3	Никита	Мартьянов	Сергеевич	18175	805	3
7	5	Петр	Яковлев	Алексеевич	19186	804	3
\.


--
-- TOC entry 3342 (class 0 OID 62513)
-- Dependencies: 218
-- Data for Name: top_table; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.top_table (t1, t2) FROM stdin;
10011	asd
10012	adf
10013	afg
10013	agh
10013	ahj
10014	ajk
10015	akl
10016	alz
10017	azx
10017	azx
10018	azx
10019	axc
\.


--
-- TOC entry 3355 (class 0 OID 0)
-- Dependencies: 214
-- Name: left_table_l_code_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.left_table_l_code_seq', 10, true);


--
-- TOC entry 3356 (class 0 OID 0)
-- Dependencies: 222
-- Name: professors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.professors_id_seq', 5, true);


--
-- TOC entry 3357 (class 0 OID 0)
-- Dependencies: 216
-- Name: right_table_r_code_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.right_table_r_code_seq', 10, true);


--
-- TOC entry 3358 (class 0 OID 0)
-- Dependencies: 220
-- Name: third_year_students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.third_year_students_id_seq', 7, true);


-- Completed on 2024-05-26 13:55:20

--
-- PostgreSQL database dump complete
--

