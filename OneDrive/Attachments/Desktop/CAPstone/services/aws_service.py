import boto3
from datetime import datetime, timedelta
def get_bucket_info():
    try:
        s3 = boto3.client("s3")
        response = s3.list_buckets()
        buckets = response.get("Buckets", [])
        
        if not buckets:
            return {
                "total_buckets": 0,
                "old_buckets": [],
                "new_buckets": [],
                "message": "No S3 buckets found"
            }
        
        current_time = datetime.now()
        thirty_days_ago = current_time - timedelta(days=30)
        old_bucket = []
        new_bucket = []
        
        for bucket in buckets:
            bucket_creation_date = bucket["CreationDate"].replace(tzinfo=None)
            if bucket_creation_date > thirty_days_ago:
                new_bucket.append(bucket["Name"])
            else:
                old_bucket.append(bucket["Name"])
        
        return {
            "total_buckets": len(buckets),
            "old_buckets": old_bucket,
            "new_buckets": new_bucket,
        }
    except Exception as e:
        return {
            "error": str(e),
            "message": "Failed to fetch bucket information. Check AWS credentials."
        }