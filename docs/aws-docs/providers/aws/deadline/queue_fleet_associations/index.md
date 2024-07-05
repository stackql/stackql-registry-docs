---
title: queue_fleet_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_fleet_associations
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>queue_fleet_association</code> resource or lists <code>queue_fleet_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_fleet_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::QueueFleetAssociation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.queue_fleet_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="FarmId, FleetId, QueueId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>queue_fleet_associations</code> in a region.
```sql
SELECT
region,
farm_id,
fleet_id,
queue_id
FROM aws.deadline.queue_fleet_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>queue_fleet_association</code>.
```sql
SELECT
region,
farm_id,
fleet_id,
queue_id
FROM aws.deadline.queue_fleet_associations
WHERE region = 'us-east-1' AND data__Identifier = '<FarmId>|<FleetId>|<QueueId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queue_fleet_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.deadline.queue_fleet_associations (
 FarmId,
 FleetId,
 QueueId,
 region
)
SELECT 
'{{ FarmId }}',
 '{{ FleetId }}',
 '{{ QueueId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.deadline.queue_fleet_associations (
 FarmId,
 FleetId,
 QueueId,
 region
)
SELECT 
 '{{ FarmId }}',
 '{{ FleetId }}',
 '{{ QueueId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: queue_fleet_association
    props:
      - name: FarmId
        value: '{{ FarmId }}'
      - name: FleetId
        value: '{{ FleetId }}'
      - name: QueueId
        value: '{{ QueueId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.deadline.queue_fleet_associations
WHERE data__Identifier = '<FarmId|FleetId|QueueId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>queue_fleet_associations</code> resource, the following permissions are required:

### Create
```json
deadline:CreateQueueFleetAssociation,
deadline:GetQueueFleetAssociation,
identitystore:ListGroupMembershipsForMember
```

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

### List
```json
deadline:ListQueueFleetAssociations,
identitystore:ListGroupMembershipsForMember
```

