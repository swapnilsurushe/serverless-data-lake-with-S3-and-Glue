import boto3

def create_glue_job():
    glue_client = boto3.client('glue')

    job_name = 'my-data-quality-job'
    job_spec = {
        'Name': job_name,
        'Role': 'arn:aws:iam::123456789012:role/my-glue-role',
        'GlueJobPlan': {
            'Actions': [{
                'JobId': 'my-crawler',
                'CrawlerTrigger': {
                    'Name': 'my-crawler-trigger'
                }
            }, {
                'JobId': 'my-data-quality-script'
            }]
        }
    }

    glue_client.create_job(**job_spec)

    print(f"Glue job '{job_name}' created successfully.")
