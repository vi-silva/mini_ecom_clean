from src.presentation.main import get_app
from src.adapter.orm import start_mapper

start_mapper()

app = get_app()
