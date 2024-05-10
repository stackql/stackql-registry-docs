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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>capacity_reservation_fleet</code> resource, use <code>capacity_reservation_fleets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation_fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservationFleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.capacity_reservation_fleet" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="allocation_strategy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="total_target_capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="end_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_match_criteria" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity_reservation_fleet_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tenancy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remove_end_date" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="no_remove_end_date" /></td><td><code>boolean</code></td><td></td></tr>
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
WHERE region = 'us-east-1' AND data__Identifier = '<CapacityReservationFleetId>';
```


## Permissions

To operate on the <code>capacity_reservation_fleet</code> resource, the following permissions are required:

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

