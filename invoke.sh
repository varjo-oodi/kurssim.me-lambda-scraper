#!/bin/bash

export AWS_PROFILE=koodivelho && sls invoke local --function crawl --stage local --uploadBucket testaus-bucket
