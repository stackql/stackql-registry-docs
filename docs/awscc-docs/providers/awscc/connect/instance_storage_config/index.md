---
title: instance_storage_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_storage_config
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>instance_storage_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_storage_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance_storage_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.instance_storage_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>Connect Instance ID with which the storage config will be associated</td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>association_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>storage_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>s3_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kinesis_video_stream_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kinesis_stream_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kinesis_firehose_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn,
resource_type,
association_id,
storage_type,
s3_config,
kinesis_video_stream_config,
kinesis_stream_config,
kinesis_firehose_config
FROM awscc.connect.instance_storage_config
WHERE region = 'us-east-1'
AND data__Identifier = '{InstanceArn}';
AND data__Identifier = '{AssociationId}';
AND data__Identifier = '{ResourceType}';
```

## Permissions

To operate on the <code>instance_storage_config</code> resource, the following permissions are required:

### Read
```json
connect:DescribeInstanceStorageConfig,
connect:ListInstanceStorageConfigs,
connect:DescribeInstance,
ds:DescribeDirectories,
s3:GetBucketAcl,
s3:GetBucketLocation
```

### Update
```json
connect:UpdateInstanceStorageConfig,
ds:DescribeDirectories,
s3:GetBucketAcl,
s3:GetBucketLocation,
kinesis:DescribeStream,
iam:PutRolePolicy,
kms:DescribeKey,
kms:CreateGrant,
kms:RetireGrant,
firehose:DescribeDeliveryStream
```

### Delete
```json
connect:DisassociateInstanceStorageConfig,
connect:DescribeInstance,
s3:GetBucketAcl,
s3:GetBucketLocation,
kms:RetireGrant
```

