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
Retrieves a list of <code>warm_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warm_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AutoScaling::WarmPool.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.autoscaling.warm_pools</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_scaling_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
auto_scaling_group_name
FROM aws.autoscaling.warm_pools
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>warm_pools</code> resource, the following permissions are required:

### Create
```json
autoscaling:PutWarmPool,
autoscaling:DescribeWarmPool,
autoscaling:DescribeAutoScalingGroups
```

