import boto3 
from botocore.exceptions import ClientError


class MetricsHelper:
    def __init__(self, *args, **kwargs):
        self._client = boto3.resource("cloudwatch")
        self._namespace = "DaftPropertyScraper"
        self._namespace_name = "run_time_metrics"
        self._metric = self._client.Metric(self._namespace, self._namespace_name)

    def put_metric_data(self, name, value, unit):
        """
        Sends a single data value to CloudWatch for a metric. This metric is given
        a timestamp of the current UTC time.

        :param namespace: The namespace of the metric.
        :param name: The name of the metric.
        :param value: The value of the metric.
        :param unit: The unit of the metric.
        """
        try:
            self._metric.put_data(
                Namespace=self._namespace,
                MetricData=[{
                    'MetricName': name,
                    'Value': value,
                    'Unit': unit
                }]
            )
        except ClientError:
            return
