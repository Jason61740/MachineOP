# Create lakeFS repository
lakectl repo create lakefs://athletes-ml s3://your-bucket/data/

# Upload V1 to main branch
lakectl fs upload -s lakefs_data/athletes_v1.csv lakefs://athletes-ml/main/athletes_v1.csv

# Commit V1
lakectl commit lakefs://athletes-ml/main -m 'Dataset V1: Original raw data'