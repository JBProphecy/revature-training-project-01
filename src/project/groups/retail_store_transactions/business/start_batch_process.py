################################################################################################

from dataclasses import dataclass
from datetime import datetime
from logging import getLogger
from uuid import UUID

################################################################################################

from project.models import PipelineConfigurationSettings as Config

from project.sql import (
  insert_batch_process, InsertBatchProcessError,
  update_batch_process, UpdateBatchProcessError
)

from .load_external_data import load_external_data, LoadExternalDataError

from ..utils import generate_id, generate_timestamp

################################################################################################

logger = getLogger(__name__)

################################################################################################

def start_batch_process(config: Config, source_index: int, main_process_id: UUID) -> None:
  logger.info("starting batch process")
  batch_process_start_timestamp = generate_timestamp()
  logger.info("batch process started at %s", batch_process_start_timestamp)
  batch_process_id = generate_id()
  logger.debug("batch_process_id = %s", batch_process_id)
  source = config.external.sources[source_index]
  try: insert_batch_process(main_process_id, batch_process_id, source_index, source.path, batch_process_start_timestamp)
  except InsertBatchProcessError:
    batch_process_final_timestamp = generate_timestamp()
    logger.warning("batch process aborted at %s", batch_process_final_timestamp)
    return
  try: raw_data = load_external_data(config, source)
  except LoadExternalDataError:
    batch_process_final_timestamp = generate_timestamp()
    logger.warning("batch process aborted at %s", batch_process_final_timestamp)
    return
  try: raw_data = raw_data[list(source.table.fields.map.keys())].rename(columns=source.table.fields.map)
  except Exception:
    batch_process_final_timestamp = generate_timestamp()
    logger.warning("batch process aborted at %s", batch_process_final_timestamp)
    return
  print(raw_data.head())
  batch_process_final_timestamp = generate_timestamp()
  try: update_batch_process(batch_process_id, batch_process_final_timestamp)
  except UpdateBatchProcessError:
    logger.warning("batch process aborted at %s", batch_process_final_timestamp)
    return
  logger.info("batch process completed at %s", batch_process_final_timestamp)

################################################################################################

__all__ = ["start_batch_process"]

################################################################################################
