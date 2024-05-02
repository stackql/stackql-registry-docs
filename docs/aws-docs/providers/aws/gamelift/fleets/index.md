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
Used to retrieve a list of <code>fleets</code> in a region or create a <code>fleets</code> resource, use <code>fleet</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers. A fleet is a set of EC2 or Anywhere instances, each of which can host multiple game sessions.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.gamelift.fleets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>fleet_id</code></td><td><code>string</code></td><td>Unique fleet ID</td></tr>
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
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
fleet_id
FROM aws.gamelift.fleets
WHERE region = 'us-east-1'
```

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

