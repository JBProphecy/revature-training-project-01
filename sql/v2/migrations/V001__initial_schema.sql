CREATE TABLE wildfire_global (
  id integer GENERATED ALWAYS AS IDENTITY,
  country text NOT NULL,
  year integer NOT NULL,
  month text NOT NULL,
  region text NOT NULL,
  cause text NOT NULL,
  recorded_fires_count integer NOT NULL,
  burned_area_hectares integer NULL,
  humidity_percent integer NOT NULL,
  wind_speed_kmh integer NOT NULL,
  CONSTRAINT wildfire_global_id PRIMARY KEY (id)
);

CREATE TABLE tornado_usa (
  id integer GENERATED ALWAYS AS IDENTITY,
  year integer NOT NULL,
  month integer NOT NULL,
  day integer NOT NULL,
  date date NOT NULL,
  state integer NOT NULL,
  magnitude integer NOT NULL,
  injury_count integer NOT NULL,
  fatality_count integer NOT NULL,
  latitude double precision NOT NULL,
  longitude double precision NOT NULL,
  CONSTRAINT tornado_usa_pkey PRIMARY KEY (id)
);

--Hello

CREATE TABLE tornado_usabob (
  id integer GENERATED ALWAYS AS IDENTITY,
  year integer NOT NULL,
  month integer NOT NULL,
  day integer NOT NULL,
  date date NOT NULL,
  state integer NOT NULL,
  magnitude integer NOT NULL,
  injury_count integer NOT NULL,
  fatality_count integer NOT NULL,
  latitude double precision NOT NULL,
  longitude double precision NOT NULL,
  CONSTRAINT tornado_usa_pkey PRIMARY KEY (id)
);