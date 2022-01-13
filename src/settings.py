from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
  db_username: Optional[str]
  db_password: Optional[str]
  db_name: Optional[str]
  db_port: Optional[str]

  @property
  def db_url(self):
    return f'postgresql://{self.db_username}:{self.db_password}@db:{self.db_port}/{self.db_name}'
    # return 'sqlite:////Users/Vitor Silva Bueno\Desktop\workspace\mini_ecomerce_clean\database.db'

settings = Settings()