---
title: location_s3
hide_title: false
hide_table_of_contents: false
keywords:
  - location_s3
  - datasync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>location_s3</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_s3</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location_s3</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.location_s3</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>s3_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>s3_bucket_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon S3 bucket.</td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.</td></tr>
<tr><td><code>s3_storage_class</code></td><td><code>string</code></td><td>The Amazon S3 storage class you want to store your files in when this location is used as a task destination.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon S3 bucket location.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the S3 location that was described.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>location_s3</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationS3,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationS3,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

### Delete
```json
datasync:DeleteLocation
```


## Example
```sql
SELECT
region,
s3_config,
s3_bucket_arn,
subdirectory,
s3_storage_class,
tags,
location_arn,
location_uri
FROM awscc.datasync.location_s3
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;LocationArn&gt;'
```
