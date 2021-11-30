import boto3

s3 = boto3.resource("s3")

def get_buckets():
    """
    Gets all S3 buckets in the given account
    Not sure if I'll use this just yet
    """

    # All the buckets are stored here
    result = []

    # Loop over and add them to the list then print the results to the console
    for bucket in s3.buckets.all():
        result.append(bucket.name)

    return result

def delete_bucket():
    """
    Deletes all buckets in the given account
    """

    # Empty the buckets before we delete them
    # Need to add a check here somewhere
    for bucket in s3.buckets.all():
        bucket.objects.all().delete()

    # Now we perform the delete operation
    for bucket in s3.buckets.all():
        print("Deleting " + bucket.name)
        bucket.delete()

delete_bucket()