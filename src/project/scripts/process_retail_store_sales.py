################################################################################################

import logging
import pandas

import uuid

from pandas import DataFrame

################################################################################################

from project.core import configure_logging

from project.errors import ReadFileError

from project.models.data_configuration_object import (
  DataConfigurationObject,
  FieldsConfiguration,
  SourceConfiguration
)

from project.types import (
  SourceFormat
)

from project.utils import read_yaml_from_file

################################################################################################

logger = logging.getLogger(__name__)

################################################################################################

class InvalidFieldCountException(Exception): pass
class InvalidFieldNameException(Exception): pass
class InvalidFieldTypeException(Exception): pass
class InvalidTableStructureException(Exception): pass
class InvalidConfigurationException(Exception): pass

################################################################################################

def load_config_from_project() -> DataConfigurationObject:
  """
  ### **Throws**

  `ReadFileError`
  """
  path = "config/sources/retail_store_sales.yaml"
  try: return DataConfigurationObject(**read_yaml_from_file(path))
  except Exception as e:
    logger.error("error reading retail store sales configuration")
    logger.debug("path = %s", path)
    raise ReadFileError(f"error reading retail sales configuration at {path}") from e

################################################################################################

def load_data_from_source(config: DataConfigurationObject, source: SourceConfiguration) -> DataFrame:
  logger.info("Loading Data from Source...")
  match source.format:
    case SourceFormat.CSV: return pandas.read_csv(source.path, dtype={p.input.name: p.input.type for p in config.fields.adjacent})
    case SourceFormat.JSON: return pandas.read_json(source.path)

################################################################################################

def validate_field_structure(fields: FieldsConfiguration, extracted: DataFrame) -> None:
  logger.info("Validating Field Structure...")
  expected_field_count = fields.count
  received_field_count = extracted.shape[1]
  if received_field_count != expected_field_count:
    logger.error("The received field count does not match the expected field count.")
    logger.debug("expected = %d", expected_field_count)
    logger.debug("received = %d", received_field_count)
    raise InvalidFieldCountException(f"invalid field count :: expected {expected_field_count} :: received {received_field_count}")
  for i in range(expected_field_count):
    received_field_name = extracted.columns[i]
    received_field_type = extracted.dtypes.iat[i]
    expected_field_name = fields.adjacent[i].input.name
    expected_field_type = fields.adjacent[i].input.type
    if received_field_name != expected_field_name:
      logger.error("The received field name does not match the expected field name.")
      logger.debug("expected = %d", expected_field_name)
      logger.debug("received = %d", received_field_name)
      raise InvalidFieldNameException(f'invalid field name :: expected "{expected_field_name}" :: received "{received_field_name}"')
    if received_field_type != expected_field_type:
      logger.error("The received field type does not match the expected field type.")
      logger.debug("expected = %d", expected_field_type)
      logger.debug("received = %d", received_field_type)
      raise InvalidFieldTypeException(f'invalid field type :: expected "{expected_field_type}" :: received "{received_field_type}"')
  logger.info("Field Structure is Valid!")

def validate_table_structure(fields: FieldsConfiguration, df: DataFrame):
  logger.info("Validating Table Structure...")
  try:
    validate_field_structure(fields, df)
  except (InvalidFieldCountException, InvalidFieldNameException, InvalidFieldTypeException) as e:
    logger.error("The received table structure does not match the expected table structure.")
    raise InvalidTableStructureException("invalid table structure") from e
  logger.info("Table Structure is Valid!")

################################################################################################

def validate_transaction_id(): pass
def validate_customer_id(): pass
def validate_category(): pass
def validate_item(): pass
def validate_price_per_unit(): pass
def validate_quantity(): pass
def validate_total_spent(): pass
def validate_payment_method(): pass
def validate_location(): pass
def validate_transaction_date(): pass
def validate_discount_applied(): pass

################################################################################################

def process_retail_store_sales():
  logger.info("Processing Retail Store Sales...")
  try:
    config = load_config_from_project()
  except ReadFileError as e:
    raise InvalidConfigurationException("cannot process retail store sales :: invalid configuration") from e # may change later
  output_field_names = list(pair.input.name for pair in config.fields.adjacent)
  accepted_table = DataFrame(columns=output_field_names)
  rejected_table = DataFrame(columns=output_field_names.extend(["rejection_reason"]))
  for source in config.sources:
    try:
      extracted = load_data_from_source(config, source)
      validate_table_structure(config.fields, extracted)
    except InvalidTableStructureException as e:
      continue # can change later
    total_record_count = extracted.shape[0]
    accepted_record_count = 0
    rejected_record_count = 0

################################################################################################

if __name__ == "__main__":
  configure_logging()
  process_retail_store_sales()

################################################################################################
