---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fleets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.gamelift.fleets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>fleet_id</code></td><td><code>string</code></td><td>Unique fleet ID</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>fleets</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateFleet,
gamelift:DescribeFleetAttributes,
gamelift:DescribeFleetLocationAttributes,
gamelift:UpdateFleetCapacity,
gamelift:DescribeFleetLocationCapacity,
gamelift:PutScalingPolicy,
gamelift:DescribeScalingPolicies
```

### List
```json
gamelift:ListFleets
```


## Example
```sql
SELECT
region,
fleet_id
FROM awscc.gamelift.fleets
WHERE region = 'us-east-1'
```
