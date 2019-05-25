import csv
from multiprocessing import Pool

def get_counts(filename):
    fp = open(filename)
    render = csv.DictReader(fp)

    results = defaultdict(int)
    for line in render:
        results[line["VendorID"]] += float(line["fare_amount"])
        cnt += 1
        if cnt > 1000:
            break
        return dict(results)

if __name__ == "__main__":
    filename = [
        yellow_tripdata_2017 - 01.csv
    ]

    pool = Pool(1)
    counts = pool.map(get_counts(filename))

    for count in counts:


#####################################33
% pyspark
from pyspark import SQLContext

sqlContext = SQLContext(sparkContext=sc)

df = sqlContext.read.format('parquet').load('hdfs:///user/zeppelin/full-yellow-trip')

% pyspark

from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType


def add_one(value):
    return value + 1


add_one_udf = udf(add_one, FloatType())
df.select(add_one_udf('fare_amount'), 'fare_amount').take(5)

%pyspark

df.select('fare_amount').withColumn('fare_plus_1', df.fare_amount + 1).take(5)

######################
%pyspark
yellow_trip.write.format('parquet').save('hdfs:///user/zeppelin/test')

%pyspark
from pyspark import SQLContext
sqlContext = SQLContext(sparkContext=sc)

yellow_trip = sqlContext.read.parquet("s3://adaptive-public/pyladies/yellow_trip_parquet/yellow_tripdata_2017-01.pq")

% pyspark
import datetime
from pyspark.sql.functions import udf
from pyspark.sql.types import LongType


def to_day_of_week(date_str):
    date_str = date_str.split(' ')[0]
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date().weekday()


dow_udf = udf(to_day_of_week, LongType())

df = sqlContext.read.format('parquet').load('hdfs:///user/zeppelin/parquet')

df2 = df.select(dow_udf('tpep_pickup_datetime').alias('day_of_week'), 'fare_amount')

%pyspark
df2.groupBy('day_of_week').agg({'fare_amount': 'sum'}).collect()

