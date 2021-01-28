from metrics_helper import MetricsHelper
from evaluator import Evaluator
import datetime


evaluator = Evaluator(locations=["rathmines-dublin", "rathgar-dublin", "ranelagh-dublin"], price_range=(1000, 1500))
metrics_helper = MetricsHelper()
print("starting at: {}".format(datetime.datetime.now()))
try:
    evaluator.run()
except: 
    metrics_helper.put_metric_data("sucessful run", 0, "Count")
else:
    metrics_helper.put_metric_data("sucessful run", 1, "Count")

# TODO setup config file and reader
# TODO pass User-Agent to request as header (do I need to this?)
