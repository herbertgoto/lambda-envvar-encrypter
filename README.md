# Cloudformation solution to encrypt an environment variable before using it in Lambda

This cloudformation creates a KMS CMK, a Lambda, and a Custom Resource that encrypts a variable that can be used as environment var in other Lambdas. 

Using this solution a secret will never be visible in the stack or as an environment varible of a Lambda function. 

# How to install
1. Create a python virtualenv and move files in app folder to it. Install dependencies and zip it(Python runtime used is 3.7.4)
2. Upload that zip file to an AWS S3 bucket.
3. Run the CloudFormation template "lambda-envvar-encrypter.yaml".
    1. You will need to fill in the parameter for S3 bucket name.
    2. You will need to fill in the parameter for S3 key that you stored the zip as.
    3. You will need to fill in the parameter with the secret to be encrypted.
4. Once CloudFormation finishes, you can go to the output session of the stack and check the encrypted secret.

You can use this template within yours to create encrypted environment variables. 

If you alread have the KMS CMK, you can comment the KMS Resource. Use the ARN of the already created KMS CMK in the policy and its ID in the custom resource. 