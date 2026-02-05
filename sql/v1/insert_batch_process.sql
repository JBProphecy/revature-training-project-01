INSERT INTO batch_process (
  main_process_id,
  id,
  source_index,
  source_path,
  start_timestamp
)
VALUES (
  :main_process_id,
  :id,
  :source_index,
  :source_path,
  :start_timestamp
);
