from .start import register_start_handlers
from .ranks import register_ranks_handlers

def register_handlers(dp):
    register_start_handlers(dp)
    register_ranks_handlers(dp)
