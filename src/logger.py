import logging
import os
from datetime import datetime

# Create a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create 'logs' directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), "src", "logs")
os.makedirs(logs_path, exist_ok=True)

# Define full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Clear any existing handlers to avoid duplicate or missing logs
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Export the configured logger (optional, but neat)
logger = logging.getLogger(__name__)

print(f"Logger initialized — logs will be written to: {LOG_FILE_PATH}")
