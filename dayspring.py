from time import sleep
from dotenv import load_dotenv
from src.display.display import Display
from src.layout.types.fulltime import FullTime
import src.log as logging

load_dotenv()

logger = logging.setup_logger('root')
logger.debug('Logging setup')

fulltime = FullTime()

while True:
    fulltime.get_content()
    sleep(0.5)
