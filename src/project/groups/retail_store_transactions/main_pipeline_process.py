################################################################################################

from logging import getLogger
from pandas import DataFrame
from pandera.errors import SchemaErrors
from pydantic import BaseModel
from typing import Any, List, cast

################################################################################################

from project.errors import LazyError
from project.models import PipelineConfigurationSettings as Config
from project.types import StartPipelineAction

from .business.load_configuration import load_configuration, LoadConfigurationError
from .business.authorize_pipeline import authorize_pipeline, AuthorizePipelineError
from .business.initialize_pipeline import initialize_pipeline, InitializePipelineError
from .business.start_main_process import start_main_process
from .business.finalize_pipeline import finalize_pipeline, FinalizePipelineError

from .schemas.internal import schema

from .utils import generate_id, generate_timestamp

################################################################################################

logger = getLogger(__name__)

################################################################################################

class ValidateBatchDataResult(BaseModel):
  accepted_data: DataFrame
  rejected_data: DataFrame
  rejected_index_list: List[Any]

################################################################################################

def validate_batch_data(config: Config, source: Config.External.Source, raw_data: DataFrame):
  try:
    try:
      return schema.validate(raw_data, lazy=True)
    except SchemaErrors as e:
      failure_data = cast(DataFrame, e.failure_cases)
      rejected_index_list = list(failure_data["index"].unique())
      candidate_valid_data = raw_data.drop(index=rejected_index_list)
      accepted_data = schema.validate(candidate_valid_data)
      rejected_data = raw_data.loc[rejected_index_list]
      rejected_data = rejected_data.merge()
      return (accepted_data, rejected_data)
  except Exception as e:
    exception = LazyError("process batch data")
    logger.error(exception.message)
    raise exception

################################################################################################

def run_batch_process(config: Config, source: Config.External.Source):
  batch_id = generate_id()
  batch_start_timestamp = generate_timestamp()
  logger.info(f"batch_process_id = {batch_id}")
  logger.info(f"batch_process_start_timestamp = {batch_start_timestamp}")
  batch_failure: bool = False
  try:
    raw_data = load_external_data(config, source)
    raw_data = raw_data[list(source.table.fields.map.keys())].rename(columns=source.table.fields.map)
    # data = data[[col for col in source.table.fields.map if col in list(data.columns)]].rename(columns=source.table.fields.map)
    valid_data = schema.validate(raw_data, lazy=True)
    # validate_external_schema(config, source, data)
    # data = data.rename(columns=source.table.fields.map)
    # print("Head", data.head(100), sep="\n\n", end="\n\n")
    # for row in data.itertuples(index=True):
    #   print(row)
  except LoadExternalDataError as e:
    batch_failure = True
    raise LazyError("batch process") from e
  except SchemaErrors as e:
    rejected_indicies = e.failure_cases["index"].unique()
    candiate_valid_data = cast(DataFrame, e.data).drop(index=rejected_indicies)
    accepted_data = schema.validate(candiate_valid_data)
    rejected_data = 
    print("COMPLETE DATA", e.data, sep="\n\n", end="\n\n")
    print("REJECTED DATA", e.failure_cases, sep="\n\n", end="\n\n")
  except Exception as e:
    batch_failure = True
    raise LazyError("batch process") from e
  finally:
    batch_final_timestamp = generate_timestamp()
    logger.info(f"batch_process_final_timestamp = {batch_final_timestamp}")

################################################################################################
