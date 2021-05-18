from metrics_helper import MetricsHelper
from evaluator import Evaluator
import datetime
import time


evaluator = Evaluator(locations=["rathmines-dublin", "rathgar-dublin", "ranelagh-dublin", "ballsbridge-dublin", "donnybrook-dublin", "dublin-4-dublin", "dublin-6-dublin"], price_range=(1350, 1600))
metrics_helper = MetricsHelper()

print("starting at: {}".format(datetime.datetime.now()))
start_time = time.time()

try:
    evaluator.run()
except: 
    metrics_helper.put_metric_data("sucessful run", 0, "Count")
else:
    metrics_helper.put_metric_data("sucessful run", 1, "Count")

end_time = time.time()
total_time = end_time - start_time
metrics_helper.put_metric_data("Total Run Time", total_time, "Seconds") 

