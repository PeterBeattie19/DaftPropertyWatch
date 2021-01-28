from evaluator import Evaluator
import datetime


evaluator = Evaluator(locations=["rathmines-dublin", "rathgar-dublin", "ranelagh-dublin"], price_range=(1000, 1500))
print("starting at: {}".format(datetime.datetime.now()))
evaluator.run()

# TODO implement email handler
# TODO setup config file and reader
# TODO pass User-Agent to request as header (do I need to this?)
