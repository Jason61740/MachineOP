
# After completing web setup and lakectl config, test these:

# List repositories (should work if configured)
lakectl repo list

# Create your athletes repository
lakectl repo create lakefs://athletes-ml local://lakefs/data

# Upload your V1 file
lakectl fs upload -s lakefs_data/athletes_v1.csv lakefs://athletes-ml/main/athletes_v1.csv

# Commit V1
lakectl commit lakefs://athletes-ml/main -m "Dataset V1: Original data"

# Verify it worked
lakectl fs ls lakefs://athletes-ml/main/
