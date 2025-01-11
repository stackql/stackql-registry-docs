---
title: warm_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - warm_pools
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

Creates, updates, deletes or gets a <code>warm_pool</code> resource or lists <code>warm_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warm_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AutoScaling::WarmPool.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.warm_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_group_prepared_capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="min_size" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="pool_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_reuse_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html"><code>AWS::AutoScaling::WarmPool</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="AutoScalingGroupName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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

## `SELECT` examples

Gets all properties from an individual <code>warm_pool</code>.
```sql
SELECT
region,
auto_scaling_group_name,
max_group_prepared_capacity,
min_size,
pool_state,
instance_reuse_policy
FROM aws.autoscaling.warm_pools
WHERE region = 'us-east-1' AND data__Identifier = '<AutoScalingGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>warm_pool</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.autoscaling.warm_pools (
 AutoScalingGroupName,
 region
)
SELECT 
'{{ AutoScalingGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.autoscaling.warm_pools (
 AutoScalingGroupName,
 MaxGroupPreparedCapacity,
 MinSize,
 PoolState,
 InstanceReusePolicy,
 region
)
SELECT 
 '{{ AutoScalingGroupName }}',
 '{{ MaxGroupPreparedCapacity }}',
 '{{ MinSize }}',
 '{{ PoolState }}',
 '{{ InstanceReusePolicy }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: warm_pool
    props:
      - name: AutoScalingGroupName
        value: '{{ AutoScalingGroupName }}'
      - name: MaxGroupPreparedCapacity
        value: '{{ MaxGroupPreparedCapacity }}'
      - name: MinSize
        value: '{{ MinSize }}'
      - name: PoolState
        value: '{{ PoolState }}'
      - name: InstanceReusePolicy
        value:
          ReuseOnScaleIn: '{{ ReuseOnScaleIn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.autoscaling.warm_pools
WHERE data__Identifier = '<AutoScalingGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>warm_pools</code> resource, the following permissions are required:

### Create
```json
autoscaling:PutWarmPool,
autoscaling:DescribeWarmPool,
autoscaling:DescribeAutoScalingGroups
```

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
