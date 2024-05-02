---
title: capacity_reservation_fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation_fleet
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
Gets an individual <code>capacity_reservation_fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation_fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservationFleet</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.capacity_reservation_fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>allocation_strategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tag_specifications</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>instance_type_specifications</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>total_target_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>end_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_match_criteria</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>capacity_reservation_fleet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tenancy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>remove_end_date</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>no_remove_end_date</code></td><td><code>boolean</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
allocation_strategy,
tag_specifications,
instance_type_specifications,
total_target_capacity,
end_date,
instance_match_criteria,
capacity_reservation_fleet_id,
tenancy,
remove_end_date,
no_remove_end_date
FROM aws.ec2.capacity_reservation_fleet
WHERE data__Identifier = '<CapacityReservationFleetId>';
```

## Permissions

To operate on the <code>capacity_reservation_fleet</code> resource, the following permissions are required:

### Delete
```json
ec2:CreateCapacityReservationFleet,
ec2:ModifyCapacityReservationFleet,
ec2:DescribeCapacityReservationFleets,
ec2:CancelCapacityReservationFleets,
ec2:CreateCapacityReservation,
ec2:DescribeCapacityReservations,
ec2:CancelCapacityReservation,
ec2:DeleteTags
```

### Read
```json
ec2:DescribeCapacityReservationFleets,
ec2:DescribeInstances,
ec2:DescribeCapacityReservations
```

### Update
```json
ec2:CreateCapacityReservationFleet,
ec2:ModifyCapacityReservationFleet,
ec2:DescribeCapacityReservationFleets,
ec2:CancelCapacityReservationFleets,
ec2:CreateCapacityReservation,
ec2:ModifyCapacityReservation,
ec2:DescribeCapacityReservations,
ec2:CancelCapacityReservation,
ec2:DescribeInstances,
ec2:DeleteTags
```

