import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Track
Track_node1716234073611 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://fetl-data/staging/track.csv"], "recurse": True}, transformation_ctx="Track_node1716234073611")

# Script generated for node Album
Album_node1716234071972 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://fetl-data/staging/albums.csv"], "recurse": True}, transformation_ctx="Album_node1716234071972")

# Script generated for node Artist
Artist_node1716234074713 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://fetl-data/staging/artists.csv"], "recurse": True}, transformation_ctx="Artist_node1716234074713")

# Script generated for node Join Album Artist
JoinAlbumArtist_node1716234332754 = Join.apply(frame1=Artist_node1716234074713, frame2=Album_node1716234071972, keys1=["id"], keys2=["artist_id"], transformation_ctx="JoinAlbumArtist_node1716234332754")

# Script generated for node Join with Tracks
JoinwithTracks_node1716234567430 = Join.apply(frame1=Track_node1716234073611, frame2=JoinAlbumArtist_node1716234332754, keys1=["track_id"], keys2=["track_id"], transformation_ctx="JoinwithTracks_node1716234567430")

# Script generated for node Drop Fields
DropFields_node1716234655002 = DropFields.apply(frame=JoinwithTracks_node1716234567430, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1716234655002")

# Script generated for node Destination
Destination_node1716234740625 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1716234655002, connection_type="s3", format="glueparquet", connection_options={"path": "s3://fetl-data/warehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1716234740625")

job.commit()
