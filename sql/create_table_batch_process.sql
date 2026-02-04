CREATE TABLE IF NOT EXISTS batch_process (
  main_process_id uuid NOT NULL,
  id uuid NOT NULL,
  source_index int NOT NULL,
  source_path text NOT NULL,
  start_timestamp timestamptz NOT NULL,
  final_timestamp timestamptz,
  CONSTRAINT batch_process_pkey PRIMARY KEY (id),
  CONSTRAINT batch_process_main_process_id_fkey
    FOREIGN KEY (main_process_id)
    REFERENCES main_process(id)
    ON UPDATE NO ACTION
    ON DELETE CASCADE
);
