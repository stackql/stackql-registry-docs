---
title: queue_fleet_association
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_fleet_association
  - deadline
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

Gets or operates on an individual <code>queue_fleet_association</code> resource, use <code>queue_fleet_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_fleet_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::QueueFleetAssociation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.queue_fleet_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="queue_id" /></td><td><code>string</code></td><td></td></tr>
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
farm_id,
fleet_id,
queue_id
FROM aws.deadline.queue_fleet_association
WHERE data__Identifier = '<FarmId>|<FleetId>|<QueueId>';
```

## Permissions

To operate on the <code>queue_fleet_association</code> resource, the following permissions are required:

### Read
```json
deadline:GetQueueFleetAssociation,
identitystore:ListGroupMembershipsForMember
```

### Delete
```json
deadline:DeleteQueueFleetAssociation,
deadline:GetQueueFleetAssociation,
deadline:UpdateQueueFleetAssociation,
identitystore:ListGroupMembershipsForMember
```

