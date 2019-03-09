import logging

# Create a custom logger
logger = logging.getLogger(__name__)

handler2 = logging.StreamHandler()  # handler for routine view
handler1 = logging.FileHandler('CatFitBot.log')

# Create handlers
format1 = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
format2 = logging.Formatter('%(name)s - %(message)s')
handler1.setFormatter(format1)
handler2.setFormatter(format2)

# Create formatters and add it to handlers
#handler.setLevel(logging.INFO)
logger.addHandler(handler1)
logger.addHandler(handler2)

logger.info('This is an error')
logger.log(level=40, msg='This is an error4')
