---
title: placement_group
hide_title: false
hide_table_of_contents: false
keywords:
  - placement_group
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>placement_group</code> resource, use <code>placement_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>placement_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::PlacementGroup</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.placement_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>strategy</code></td><td><code>string</code></td><td>The placement strategy.</td></tr>
<tr><td><code>group_name</code></td><td><code>string</code></td><td>The Group Name of Placement Group.</td></tr>
<tr><td><code>spread_level</code></td><td><code>string</code></td><td>The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread</td></tr>
<tr><td><code>partition_count</code></td><td><code>integer</code></td><td>The number of partitions. Valid only when **Strategy** is set to `partition`</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
strategy,
group_name,
spread_level,
partition_count,
tags
FROM aws.ec2.placement_group
WHERE data__Identifier = '<GroupName>';
```

## Permissions

To operate on the <code>placement_group</code> resource, the following permissions are required:

### Read
```json
ec2:DescribePlacementGroups
```

### Delete
```json
ec2:DeletePlacementGroup,
ec2:DescribePlacementGroups
```

