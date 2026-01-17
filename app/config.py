import time
import os

START_TIME = time.time()
SERVICE_NAME = os.getenv("SERVICE_NAME", "wsbapp-health-api")
VERSION = os.getenv("VERSION", "1.0.0")