---
title: directory_bucket
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_bucket
  - s3express
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>directory_bucket</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_bucket</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>directory_bucket</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3express.directory_bucket</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bucket_name</code></td><td><code>string</code></td><td>Specifies a name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format 'bucket_base_name--az_id--x-s3' (for example, 'DOC-EXAMPLE-BUCKET--usw2-az1--x-s3'). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.</td></tr>
<tr><td><code>location_name</code></td><td><code>string</code></td><td>Specifies the AZ ID of the Availability Zone where the directory bucket will be created. An example AZ ID value is 'use1-az5'.</td></tr>
<tr><td><code>data_redundancy</code></td><td><code>string</code></td><td>Specifies the number of Availability Zone that's used for redundancy for the bucket.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Returns the Amazon Resource Name (ARN) of the specified bucket.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
bucket_name,
location_name,
data_redundancy,
arn
FROM awscc.s3express.directory_bucket
WHERE data__Identifier = '<BucketName>';
```

## Permissions

To operate on the <code>directory_bucket</code> resource, the following permissions are required:

### Read
```json
s3express:ListAllMyDirectoryBuckets
```

### Delete
```json
s3express:DeleteBucket,
s3express:ListAllMyDirectoryBuckets
```

