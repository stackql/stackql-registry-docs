---
title: capacity_reservation
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation
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

Gets or operates on an individual <code>capacity_reservation</code> resource, use <code>capacity_reservations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.capacity_reservation" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="tenancy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="end_date_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="total_instance_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="end_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ebs_optimized" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="out_post_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="placement_group_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="available_instance_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_platform" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ephemeral_storage" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_match_criteria" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
tenancy,
end_date_type,
tag_specifications,
availability_zone,
total_instance_count,
end_date,
ebs_optimized,
out_post_arn,
instance_count,
placement_group_arn,
available_instance_count,
instance_platform,
id,
instance_type,
ephemeral_storage,
instance_match_criteria
FROM aws.ec2.capacity_reservation
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>capacity_reservation</code> resource, the following permissions are required:

### Delete
```json
ec2:CreateCapacityReservation,
ec2:DescribeCapacityReservations,
ec2:CancelCapacityReservation,
ec2:DeleteTags
```

### Read
```json
ec2:DescribeCapacityReservations
```

### Update
```json
ec2:ModifyCapacityReservation,
ec2:CreateCapacityReservation,
ec2:DescribeCapacityReservations,
ec2:CancelCapacityReservation,
ec2:CreateTags,
ec2:DeleteTags
```

