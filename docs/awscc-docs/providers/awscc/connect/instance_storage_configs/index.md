---
title: instance_storage_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_storage_configs
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
Retrieves a list of <code>instance_storage_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_storage_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance_storage_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.instance_storage_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>Connect Instance ID with which the storage config will be associated</td></tr>
<tr><td><code>association_id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>resource_type</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>instance_storage_configs</code> resource, the following permissions are required:

### Create
<pre>
connect:AssociateInstanceStorageConfig,
connect:DescribeInstance,
ds:DescribeDirectories,
s3:GetBucketAcl,
s3:GetBucketLocation,
iam:PutRolePolicy,
kinesis:DescribeStream,
kms:DescribeKey,
kms:CreateGrant,
firehose:DescribeDeliveryStream</pre>

### List
<pre>
connect:DescribeInstance,
connect:ListInstanceStorageConfigs,
ds:DescribeDirectories</pre>


## Example
```sql
SELECT
region,
instance_arn,
association_id,
resource_type
FROM awscc.connect.instance_storage_configs
WHERE region = 'us-east-1'
```
