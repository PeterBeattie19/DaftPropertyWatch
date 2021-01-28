import boto3
from botocore.exceptions import ClientError


class EmailHandler:
    def __init__(self):
        self.SENDER = "peterbeattie19@gmail.com"
        self.AWS_REGION = "eu-west-1"
        self.DEFAULT_SUBJECT = "New Property Listed On Daft"
        self.CHARSET = "UTF-8"
        self.AWS_SES = "ses"
        self._client = boto3.client(self.AWS_SES, region_name=self.AWS_REGION)

    def send_new_prop_emails(self, properties):
        content = """<html>
        <head></head>
        <body>
          <h1>Daft Listings </h1>
          <ul>
          {}
          </ul>
        </body>
        <style> li {{
        margin-top: 1em;
        margin-bottom: 1em;
        }} 
        </style>
        </html>
        """.format("".join(["<li>{}\n".format(x.url) for x in properties]))
        print(content)
        self._send_email("New Properties Listed On Daft", content)

    def _send_email(self, html_content, content):
        try:
            response = self._client.send_email(
                Destination={
                    'ToAddresses': [
                        self.SENDER,
                        'samadekunle12@gmail.com'
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.CHARSET,
                            'Data': content,
                        },
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': html_content,
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': self.DEFAULT_SUBJECT,
                    },
                },
                Source=self.SENDER,
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
