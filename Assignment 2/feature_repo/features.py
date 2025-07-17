
from feast import FeatureView, FileSource, Entity, Field
from feast.types import Float32, Int64
from datetime import timedelta
import os

# Entity
athlete = Entity(name="athlete_id", join_keys=["athlete_id"])

# Data source
if os.path.exists("../athletes_data.parquet"):
    file_source = FileSource(path="../athletes_data.parquet", timestamp_field="timestamp")
else:
    file_source = FileSource(path="../athletes_data.csv", timestamp_field="timestamp")

# Feature View 1: Relative Performance Metrics
relative_performance = FeatureView(
    name="relative_performance",
    entities=[athlete],
    ttl=timedelta(days=365),
    schema=[
        Field(name="snatch_to_bodyweight", dtype=Float32),
        Field(name="candj_to_bodyweight", dtype=Float32),
        Field(name="technical_ratio", dtype=Float32),
        Field(name="snatch_percentile", dtype=Float32),
    ],
    online=True,
    source=file_source,
)

# Feature View 2: Physical Foundation  
physical_foundation = FeatureView(
    name="physical_foundation",
    entities=[athlete],
    ttl=timedelta(days=365),
    schema=[
        Field(name="deadlift", dtype=Float32),
        Field(name="backsq", dtype=Float32), 
        Field(name="height", dtype=Float32),
        Field(name="weight", dtype=Float32),
        Field(name="bmi", dtype=Float32),
    ],
    online=True,
    source=file_source,
)
