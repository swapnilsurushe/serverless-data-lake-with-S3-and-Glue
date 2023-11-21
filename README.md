# serverless-data-lake-with-S3-and-Glue
# Project Description:
This project demonstrates how to build a serverless data lake using Amazon S3 and AWS Glue. The project includes code for creating an S3 bucket, an AWS Glue crawler, and an AWS Glue job. The crawler will periodically scan the S3 bucket for new data files, and the job will run a data quality script to check the quality of the data.


# Project Structure:

serverless-data-lake-with-S3-and-Glue/
├── create_s3_bucket.py
├── create_glue_crawler.py
├── create_glue_job.py
├── data_quality_script.py
├── README.md
└── requirements.txt

# Serverless Data Lake with S3 and Glue

This project demonstrates how to build a serverless data lake using Amazon S3 and AWS Glue.

## Prerequisites

* An AWS account with IAM user access
* Basic understanding of AWS services, including S3 and Glue

## Usage

1. Create an AWS S3 bucket using the `create_s3_bucket.py` script.

2. Create an AWS Glue crawler using the `create_glue_crawler.py` script.

3. Create an AWS Glue job using the `create_glue_job.py` script.

4. Implement data quality checks in the `data_quality_script.py` script.

## License

This project is licensed under the MIT License.
