---
title: capacity_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservations
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

Creates, updates, deletes or gets a <code>capacity_reservation</code> resource or lists <code>capacity_reservations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::CapacityReservation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.capacity_reservations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>The Amazon Resource Name (ARN) of the specified capacity reservation</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The reservation name.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the reservation.</td></tr>
<tr><td><CopyableCode code="target_dpus" /></td><td><code>integer</code></td><td>The number of DPUs to request to be allocated to the reservation.</td></tr>
<tr><td><CopyableCode code="allocated_dpus" /></td><td><code>integer</code></td><td>The number of DPUs Athena has provisioned and allocated for the reservation</td></tr>
<tr><td><CopyableCode code="capacity_assignment_configuration" /></td><td><code>Assignment configuration to assign workgroups to a reservation</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Name, TargetDpus, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>capacity_reservations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.athena.capacity_reservations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>capacity_reservation</code>.
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
FROM aws.athena.capacity_reservations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>capacity_reservation</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.athena.capacity_reservations (
 Name,
 TargetDpus,
 region
)
SELECT 
'{{ Name }}',
 '{{ TargetDpus }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.athena.capacity_reservations (
 Name,
 TargetDpus,
 CapacityAssignmentConfiguration,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ TargetDpus }}',
 '{{ CapacityAssignmentConfiguration }}',
 '{{ Tags }}',
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
  - name: capacity_reservation
    props:
      - name: Name
        value: '{{ Name }}'
      - name: TargetDpus
        value: '{{ TargetDpus }}'
      - name: CapacityAssignmentConfiguration
        value:
          CapacityAssignments:
            - WorkgroupNames:
                - '{{ WorkgroupNames[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.athena.capacity_reservations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>capacity_reservations</code> resource, the following permissions are required:

### Create
```json
athena:CreateCapacityReservation,
athena:PutCapacityAssignmentConfiguration,
athena:GetCapacityReservation,
athena:TagResource
```

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

### List
```json
athena:ListCapacityReservations,
athena:GetCapacityReservation
```

