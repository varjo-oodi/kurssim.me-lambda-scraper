# kurssim.me lambda scraper

The Opintoni/Weboodi scraper turned into AWS Lambda function with Serverless.

# How to run locally

You should already have Python 3.6 installed.

If you want to deploy this to your own AWS environment then you should also install `aws-cli` and then create a local profile with full admin rights (hihi) and a S3 bucket.

Also you need Docker if you want to deploy to AWS. Yeah...

## Installation for Mac OS X and Ubuntu

1) Install Node.js version >=8 using nvm
2) Download this repo and enter `npm i`
3) Install serverless globally: `npm i -g serverless`
4) Install virtualenv if you don't have it already: `pip3 install virtualenv` (or just pip if you don't have Python2 locally or `python3.6 -m pip install virtualenv` if you have other than Python 3.6 as default)
4) Generate virtual environment: `virtualenv venv` (you might have to specify Python version if you have other than 3.6 as default)
5) Activate virtual environment: `source venv/bin/activate`
6) Install AWS's Python SDK: `pip install boto3` (it's globally available on AWS Lambda which is why it's not included in the `requirements.txt` bundle)
7) Install other dependencies: `pip install -r requirements.txt`
8) Before invoking the lambda if you want to upload the file to S3 you need to have AWS account locally with permissions to a bucket (in `~/.aws/credentials`)
9) Then you should invoke the Lambda locally: `./invoke.sh` or more elaborate `sls invoke local --function crawl --aws-profile <your-profile> --stage local --bucket <your-bucket>` where you should replace the profile and bucket with your values.
10) If you want to deploy the whole CloudFormation stack to AWS then you should have admin permissions on your local AWS profile and then use: `serverless deploy --aws-profile <your-profile> --stage dev --bucket <your-bucket>`. There's no difference between `prod` and `dev` but their names. NOTE: this one requires Docker to build the image.

## Installation for Windows

As of now I don't think you can install this on either regular Windows or Windows Ubuntu subsystem. That's because `multiprocessing` -module doesn't work with regular Windows and `twisted` -library doesn't work with subsystem.

But you can run the scraper manually by first installing `scrapy` with `pip install scrapy` and then running it with `./crawl.sh`. This should be basically the same what the Serverless would do with the exception of course it will put the results into S3-bucket.

# Additional information

You can trigger the Lambda manually by going to your AWS Console's Lambda page and creating & sending a test event.

# TODO

Disable Scrapy logging. Seriously annoying to read million rows in CloudWatch Logs.

Maybe add to CI pipeline eg. Travis. Or not. Admin rights is tricky business.



