CREATE TABLE IF NOT EXISTS pipeline (
  name text NOT NULL,
  status pipeline_status DEFAULT 'idle'::pipeline_status,
  CONSTRAINT pipeline_pkey PRIMARY KEY (name)
);
