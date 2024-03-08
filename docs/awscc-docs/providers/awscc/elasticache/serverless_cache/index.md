---
title: serverless_cache
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_cache
  - elasticache
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>serverless_cache</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_cache</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>serverless_cache</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticache.serverless_cache</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>serverless_cache_name</code></td><td><code>string</code></td><td>The name of the Serverless Cache. This value must be unique.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the Serverless Cache.</td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td>The engine name of the Serverless Cache.</td></tr>
<tr><td><code>major_engine_version</code></td><td><code>string</code></td><td>The major engine version of the Serverless Cache.</td></tr>
<tr><td><code>full_engine_version</code></td><td><code>string</code></td><td>The full engine version of the Serverless Cache.</td></tr>
<tr><td><code>cache_usage_limits</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The ID of the KMS key used to encrypt the cluster.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>One or more Amazon VPC security groups associated with this Serverless Cache.</td></tr>
<tr><td><code>snapshot_arns_to_restore</code></td><td><code>array</code></td><td>The ARN's of snapshot to restore Serverless Cache.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this Serverless Cache.</td></tr>
<tr><td><code>user_group_id</code></td><td><code>string</code></td><td>The ID of the user group.</td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td>The subnet id's of the Serverless Cache.</td></tr>
<tr><td><code>snapshot_retention_limit</code></td><td><code>integer</code></td><td>The snapshot retention limit of the Serverless Cache.</td></tr>
<tr><td><code>daily_snapshot_time</code></td><td><code>string</code></td><td>The daily time range (in UTC) during which the service takes automatic snapshot of the Serverless Cache.</td></tr>
<tr><td><code>create_time</code></td><td><code>string</code></td><td>The creation time of the Serverless Cache.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the Serverless Cache.</td></tr>
<tr><td><code>endpoint</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>reader_endpoint</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the Serverless Cache.</td></tr>
<tr><td><code>final_snapshot_name</code></td><td><code>string</code></td><td>The final snapshot name which is taken before Serverless Cache is deleted.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
serverless_cache_name,
description,
engine,
major_engine_version,
full_engine_version,
cache_usage_limits,
kms_key_id,
security_group_ids,
snapshot_arns_to_restore,
tags,
user_group_id,
subnet_ids,
snapshot_retention_limit,
daily_snapshot_time,
create_time,
status,
endpoint,
reader_endpoint,
a_rn,
final_snapshot_name
FROM awscc.elasticache.serverless_cache
WHERE region = 'us-east-1'
AND data__Identifier = '{ServerlessCacheName}';
```

## Permissions

To operate on the <code>serverless_cache</code> resource, the following permissions are required:

### Read
```json
elasticache:DescribeServerlessCaches,
elasticache:ListTagsForResource
```

### Update
```json
elasticache:ModifyServerlessCache,
elasticache:DescribeServerlessCaches,
elasticache:AddTagsToResource,
elasticache:ListTagsForResource,
elasticache:RemoveTagsFromResource
```

### Delete
```json
elasticache:DeleteServerlessCache,
elasticache:DescribeServerlessCaches,
elasticache:ListTagsForResource
```

