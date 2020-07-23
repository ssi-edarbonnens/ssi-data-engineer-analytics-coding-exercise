import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


def data_analytics_project(myargs, sc, glueContext):

    # Your code here
    #
    # Write the data in a format such as Apache Parquet
    return True


if __name__ == '__main__':
    
    ## @params: [JOB_NAME]
    args = getResolvedOptions(sys.argv, ['JOB_NAME'])

    # Initialize Glue context and SparkContext for the Job.
    sc = SparkContext().getOrCreate()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session
    job = Job(glueContext)
    job.init(args['JOB_NAME'], args)

    # Call Analytics Function
    returned_value = data_analytics_project(myargs, sc, glueContext)

    # Finally commit your Job.
    job.commit()
