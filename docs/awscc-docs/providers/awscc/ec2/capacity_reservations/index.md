---
title: capacity_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservations
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
Retrieves a list of <code>capacity_reservations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>capacity_reservations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.capacity_reservations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM awscc.ec2.capacity_reservations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>capacity_reservations</code> resource, the following permissions are required:

### Create
```json
ec2:CreateCapacityReservation,
ec2:DescribeCapacityReservations,
ec2:CancelCapacityReservation,
ec2:CreateTags
```

### List
```json
ec2:DescribeCapacityReservations
```

