import boto3
client = boto3.client('ecr')
response = client.create_repository(
    repositoryName='dtm-python-images',
    imageTagMutability='MUTABLE',

    encryptionConfiguration={
        'encryptionType': 'AES256',
    }
)