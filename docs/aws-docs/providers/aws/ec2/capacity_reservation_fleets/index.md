---
title: capacity_reservation_fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation_fleets
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
Retrieves a list of <code>capacity_reservation_fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation_fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservationFleet</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.capacity_reservation_fleets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>capacity_reservation_fleet_id</code></td><td><code>string</code></td><td></td></tr>
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
capacity_reservation_fleet_id
FROM aws.ec2.capacity_reservation_fleets
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>capacity_reservation_fleets</code> resource, the following permissions are required:

### Create
```json
ec2:CreateCapacityReservationFleet,
ec2:ModifyCapacityReservationFleet,
ec2:DescribeCapacityReservationFleets,
ec2:CancelCapacityReservationFleets,
ec2:CreateCapacityReservation,
ec2:DescribeCapacityReservations,
ec2:CancelCapacityReservation,
ec2:DescribeInstances,
ec2:CreateTags,
iam:CreateServiceLinkedRole
```

### List
```json
ec2:DescribeCapacityReservationFleets,
ec2:DescribeCapacityReservations,
ec2:DescribeInstances
```

