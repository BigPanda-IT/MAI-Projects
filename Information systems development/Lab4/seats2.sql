-- DROP TABLE bookings.seats;

CREATE TABLE bookings.seats (
	aircraft_code bpchar(3) NOT NULL,
	seat_no varchar(4) NOT NULL,
	fare_conditions varchar(10) NOT NULL,
	CONSTRAINT seats_fare_conditions_check CHECK (((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text]))),
	CONSTRAINT seats_pkey PRIMARY KEY (aircraft_code, seat_no)
);


-- bookings.seats внешние включи

ALTER TABLE bookings.seats ADD CONSTRAINT seats_aircraft_code_fkey FOREIGN KEY (aircraft_code) REFERENCES bookings.aircrafts_data(aircraft_code) ON DELETE CASCADE;