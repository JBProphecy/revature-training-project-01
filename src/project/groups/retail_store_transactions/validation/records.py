################################################################################################

from ..errors import InvalidFieldValueError

################################################################################################

def validate_transaction_id(value: str):
  prefix = "TXN_"
  if not value.startswith(prefix):
    raise InvalidFieldValueError(
      reason=f"expected to start with \"{prefix}\"",
      field_name="transaction_id",
      field_value=value
    )

def validate_customer_id(value: str):
  prefix = "CUST_"
  if not value.startswith(prefix):
    raise InvalidFieldValueError(
      reason=f"expected to start with \"{prefix}\"",
      field_name="customer_id",
      field_value=value
    )

def validate_category(): pass

def validate_item(value:str):
  prefix = "Item_"
  if not value.startswith(prefix):
    raise InvalidFieldValueError(
      reason=f"expected to start with \"{prefix}\"",
      field_name="category",
      field_value=value
    )

def validate_price_per_unit(value: float):
  if value < 0:
    raise InvalidFieldValueError(
      reason="price cannot be negative",
      field_name="price_per_unit",
      field_value=value
    )

def validate_quantity(value: float):
  if value < 0:
    raise InvalidFieldValueError(
      reason="quantity cannot be negative",
      field_name="quantity",
      field_value=value
    )

def validate_total_spent(value: float):
  if value < 0:
    raise InvalidFieldValueError(
      reason="price cannot be negative",
      field_name="total_spent",
      field_value=value
    )

def validate_payment_method(value: str):
  valid_payment_method = {"Digital Wallet", "Credit Card", "Cash"}
  if value not in valid_payment_method:
    raise InvalidFieldValueError(
      reason="unknown payment method",
      field_name="payment_method",
      field_value=value
    )

def validate_location(value: str):
  valid_payment_method = {"Online", "In-store"}
  if value not in valid_payment_method:
    raise InvalidFieldValueError(
      reason="unknown payment location",
      field_name="location",
      field_value=value
    )

def validate_transaction_date(): pass

def validate_discount_applied(): pass

################################################################################################
