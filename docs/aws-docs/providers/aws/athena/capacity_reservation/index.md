---
title: capacity_reservation
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation
  - athena
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>capacity_reservation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::CapacityReservation</td></tr>
<tr><td><b>Id</b></td><td><code>aws.athena.capacity_reservation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The reservation name.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the reservation.</td></tr>
<tr><td><code>target_dpus</code></td><td><code>integer</code></td><td>The number of DPUs to request to be allocated to the reservation.</td></tr>
<tr><td><code>allocated_dpus</code></td><td><code>integer</code></td><td>The number of DPUs Athena has provisioned and allocated for the reservation</td></tr>
<tr><td><code>capacity_assignment_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The date and time the reservation was created.</td></tr>
<tr><td><code>last_successful_allocation_time</code></td><td><code>string</code></td><td>The timestamp when the last successful allocated was made</td></tr>
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
arn,
name,
status,
target_dpus,
allocated_dpus,
capacity_assignment_configuration,
creation_time,
last_successful_allocation_time,
tags
FROM aws.athena.capacity_reservation
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>capacity_reservation</code> resource, the following permissions are required:

### Read
```json
athena:GetCapacityReservation,
athena:GetCapacityAssignmentConfiguration,
athena:ListTagsForResource
```

### Update
```json
athena:UpdateCapacityReservation,
athena:PutCapacityAssignmentConfiguration,
athena:GetCapacityReservation,
athena:TagResource,
athena:UntagResource
```

### Delete
```json
athena:CancelCapacityReservation,
athena:GetCapacityReservation,
athena:DeleteCapacityReservation
```

