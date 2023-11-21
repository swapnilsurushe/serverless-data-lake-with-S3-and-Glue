import boto3

def create_glue_crawler():
    glue_client = boto3.client('glue')

    crawler_name = 'my-crawler'
    crawler_spec = {
        'Name': crawler_name,
        'Targets': {
            'S3Targets': [{
                'Path': 's3://my-s3-bucket/'
            }]
        },
        'Schedule': {
            'Frequency': 'Once',
            'ScheduleExpression': 'cron(0 0 * * ? *)'
        },
        'Classifiers': [{
            'Name': 'csv'
        }]
    }

    glue_client.create_crawler(**crawler_spec)

    print(f"Glue crawler '{crawler_name}' created successfully.")
