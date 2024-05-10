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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>capacity_reservation</code> resource, use <code>capacity_reservations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::CapacityReservation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.capacity_reservation" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The reservation name.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the reservation.</td></tr>
<tr><td><CopyableCode code="target_dpus" /></td><td><code>integer</code></td><td>The number of DPUs to request to be allocated to the reservation.</td></tr>
<tr><td><CopyableCode code="allocated_dpus" /></td><td><code>integer</code></td><td>The number of DPUs Athena has provisioned and allocated for the reservation</td></tr>
<tr><td><CopyableCode code="capacity_assignment_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The date and time the reservation was created.</td></tr>
<tr><td><CopyableCode code="last_successful_allocation_time" /></td><td><code>string</code></td><td>The timestamp when the last successful allocated was made</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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

