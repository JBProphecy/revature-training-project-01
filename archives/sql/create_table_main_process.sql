CREATE TABLE IF NOT EXISTS main_process (
  pipeline_name text NOT NULL,
  id uuid NOT NULL,
  start_timestamp timestamptz NOT NULL,
  final_timestamp timestamptz,
  CONSTRAINT main_process_pkey PRIMARY KEY (id),
  CONSTRAINT main_process_pipeline_name
    FOREIGN KEY (pipeline_name)
    REFERENCES pipeline(name)
    ON UPDATE NO ACTION
    ON DELETE CASCADE
);
