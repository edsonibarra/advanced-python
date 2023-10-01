import logging
import sys


logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("output.log")

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)


def division():
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
    if divisor == 0.0:
      logger.log(logging.ERROR, "Attempting to divide by 0!")
  except ValueError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return None
  if divisor == 0:
    return None
  else:
    return dividend/divisor
result = division()
if result is None:
  logger.warning("The result value is None!")