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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>capacity_reservations</code> in a region or to create or delete a <code>capacity_reservations</code> resource, use <code>capacity_reservation</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.capacity_reservations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.ec2.capacity_reservations
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- capacity_reservation.iql (required properties only)
INSERT INTO aws.ec2.capacity_reservations (
 AvailabilityZone,
 InstanceCount,
 InstancePlatform,
 InstanceType,
 region
)
SELECT 
'{{ AvailabilityZone }}',
 '{{ InstanceCount }}',
 '{{ InstancePlatform }}',
 '{{ InstanceType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- capacity_reservation.iql (all properties)
INSERT INTO aws.ec2.capacity_reservations (
 Tenancy,
 EndDateType,
 TagSpecifications,
 AvailabilityZone,
 EndDate,
 EbsOptimized,
 OutPostArn,
 InstanceCount,
 PlacementGroupArn,
 InstancePlatform,
 InstanceType,
 EphemeralStorage,
 InstanceMatchCriteria,
 region
)
SELECT 
 '{{ Tenancy }}',
 '{{ EndDateType }}',
 '{{ TagSpecifications }}',
 '{{ AvailabilityZone }}',
 '{{ EndDate }}',
 '{{ EbsOptimized }}',
 '{{ OutPostArn }}',
 '{{ InstanceCount }}',
 '{{ PlacementGroupArn }}',
 '{{ InstancePlatform }}',
 '{{ InstanceType }}',
 '{{ EphemeralStorage }}',
 '{{ InstanceMatchCriteria }}',
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
      - name: Tenancy
        value: '{{ Tenancy }}'
      - name: EndDateType
        value: '{{ EndDateType }}'
      - name: TagSpecifications
        value:
          - ResourceType: '{{ ResourceType }}'
            Tags:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: EndDate
        value: '{{ EndDate }}'
      - name: EbsOptimized
        value: '{{ EbsOptimized }}'
      - name: OutPostArn
        value: '{{ OutPostArn }}'
      - name: InstanceCount
        value: '{{ InstanceCount }}'
      - name: PlacementGroupArn
        value: '{{ PlacementGroupArn }}'
      - name: InstancePlatform
        value: '{{ InstancePlatform }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: EphemeralStorage
        value: '{{ EphemeralStorage }}'
      - name: InstanceMatchCriteria
        value: '{{ InstanceMatchCriteria }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.capacity_reservations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
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

### Delete
```json
ec2:CreateCapacityReservation,
ec2:DescribeCapacityReservations,
ec2:CancelCapacityReservation,
ec2:DeleteTags
```

### List
```json
ec2:DescribeCapacityReservations
```

