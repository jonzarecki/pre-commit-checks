import os
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

_curr_time = datetime.now().isoformat(" ", "seconds")
