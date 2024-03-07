---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - s3
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>buckets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.buckets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bucket_name</code></td><td><code>string</code></td><td>A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow &#91;Amazon S3 bucket restrictions and limitations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;BucketRestrictions.html). For more information, see &#91;Rules for naming Amazon S3 buckets&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;BucketRestrictions.html#bucketnamingrules) in the *Amazon S3 User Guide*. &lt;br&#x2F;&gt;  If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>buckets</code> resource, the following permissions are required:

### Create
```json
s3:CreateBucket,
s3:PutBucketTagging,
s3:PutAnalyticsConfiguration,
s3:PutEncryptionConfiguration,
s3:PutBucketCORS,
s3:PutInventoryConfiguration,
s3:PutLifecycleConfiguration,
s3:PutMetricsConfiguration,
s3:PutBucketNotification,
s3:PutBucketReplication,
s3:PutBucketWebsite,
s3:PutAccelerateConfiguration,
s3:PutBucketPublicAccessBlock,
s3:PutReplicationConfiguration,
s3:PutObjectAcl,
s3:PutBucketObjectLockConfiguration,
s3:GetBucketAcl,
s3:ListBucket,
iam:PassRole,
s3:DeleteObject,
s3:PutBucketLogging,
s3:PutBucketVersioning,
s3:PutObjectLockConfiguration,
s3:PutBucketOwnershipControls,
s3:PutIntelligentTieringConfiguration
```

### List
```json
s3:ListAllMyBuckets
```


## Example
```sql
SELECT
region,
bucket_name
FROM awscc.s3.buckets
WHERE region = 'us-east-1'
```
