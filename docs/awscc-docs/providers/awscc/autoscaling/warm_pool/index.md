---
title: warm_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - warm_pool
  - autoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>warm_pool</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warm_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>warm_pool</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.autoscaling.warm_pool</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_scaling_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_group_prepared_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>min_size</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>pool_state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_reuse_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>warm_pool</code> resource, the following permissions are required:

### Delete
```json
autoscaling:DeleteWarmPool,
autoscaling:DescribeWarmPool
```

### Read
```json
autoscaling:DescribeWarmPool
```

### Update
```json
autoscaling:PutWarmPool,
autoscaling:DescribeWarmPool,
autoscaling:DescribeAutoScalingGroups
```


## Example
```sql
SELECT
region,
auto_scaling_group_name,
max_group_prepared_capacity,
min_size,
pool_state,
instance_reuse_policy
FROM awscc.autoscaling.warm_pool
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AutoScalingGroupName&gt;'
```
