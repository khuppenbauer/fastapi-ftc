# schemas.py
from pydantic import BaseModel

class FtcInput(BaseModel):
  name_1_first_name: str = None
  name_1_last_name: str = None
  address_1_street_address: str = None
  address_1_city: str = None
  email_1: str = None
  phone_1: str = None
  phone_2: str = None
  number_1: str = None
  radio_1: str = None
  radio_2: str = None
  radio_3: str = None
  radio_4: str = None
  text_1: str = None
  entry_time: str = None
