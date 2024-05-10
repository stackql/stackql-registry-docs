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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>warm_pool</code> resource, use <code>warm_pools</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warm_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AutoScaling::WarmPool.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.warm_pool" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_group_prepared_capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="min_size" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="pool_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_reuse_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
auto_scaling_group_name,
max_group_prepared_capacity,
min_size,
pool_state,
instance_reuse_policy
FROM aws.autoscaling.warm_pool
WHERE region = 'us-east-1' AND data__Identifier = '<AutoScalingGroupName>';
```


## Permissions

To operate on the <code>warm_pool</code> resource, the following permissions are required:

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

