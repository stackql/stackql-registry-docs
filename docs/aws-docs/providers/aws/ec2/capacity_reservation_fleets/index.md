---
title: capacity_reservation_fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation_fleets
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


Used to retrieve a list of <code>capacity_reservation_fleets</code> in a region or to create or delete a <code>capacity_reservation_fleets</code> resource, use <code>capacity_reservation_fleet</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation_fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservationFleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.capacity_reservation_fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="capacity_reservation_fleet_id" /></td><td><code>string</code></td><td></td></tr>
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
capacity_reservation_fleet_id
FROM aws.ec2.capacity_reservation_fleets
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>capacity_reservation_fleet</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- capacity_reservation_fleet.iql (required properties only)
INSERT INTO aws.ec2.capacity_reservation_fleets (
 AllocationStrategy,
 TagSpecifications,
 InstanceTypeSpecifications,
 TotalTargetCapacity,
 EndDate,
 InstanceMatchCriteria,
 Tenancy,
 RemoveEndDate,
 NoRemoveEndDate,
 region
)
SELECT 
'{{ AllocationStrategy }}',
 '{{ TagSpecifications }}',
 '{{ InstanceTypeSpecifications }}',
 '{{ TotalTargetCapacity }}',
 '{{ EndDate }}',
 '{{ InstanceMatchCriteria }}',
 '{{ Tenancy }}',
 '{{ RemoveEndDate }}',
 '{{ NoRemoveEndDate }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- capacity_reservation_fleet.iql (all properties)
INSERT INTO aws.ec2.capacity_reservation_fleets (
 AllocationStrategy,
 TagSpecifications,
 InstanceTypeSpecifications,
 TotalTargetCapacity,
 EndDate,
 InstanceMatchCriteria,
 Tenancy,
 RemoveEndDate,
 NoRemoveEndDate,
 region
)
SELECT 
 '{{ AllocationStrategy }}',
 '{{ TagSpecifications }}',
 '{{ InstanceTypeSpecifications }}',
 '{{ TotalTargetCapacity }}',
 '{{ EndDate }}',
 '{{ InstanceMatchCriteria }}',
 '{{ Tenancy }}',
 '{{ RemoveEndDate }}',
 '{{ NoRemoveEndDate }}',
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
  - name: capacity_reservation_fleet
    props:
      - name: AllocationStrategy
        value: '{{ AllocationStrategy }}'
      - name: TagSpecifications
        value:
          - ResourceType: '{{ ResourceType }}'
            Tags:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
      - name: InstanceTypeSpecifications
        value:
          - InstanceType: '{{ InstanceType }}'
            InstancePlatform: '{{ InstancePlatform }}'
            Weight: null
            AvailabilityZone: '{{ AvailabilityZone }}'
            AvailabilityZoneId: '{{ AvailabilityZoneId }}'
            EbsOptimized: '{{ EbsOptimized }}'
            Priority: '{{ Priority }}'
      - name: TotalTargetCapacity
        value: '{{ TotalTargetCapacity }}'
      - name: EndDate
        value: '{{ EndDate }}'
      - name: InstanceMatchCriteria
        value: '{{ InstanceMatchCriteria }}'
      - name: Tenancy
        value: '{{ Tenancy }}'
      - name: RemoveEndDate
        value: '{{ RemoveEndDate }}'
      - name: NoRemoveEndDate
        value: '{{ NoRemoveEndDate }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.capacity_reservation_fleets
WHERE data__Identifier = '<CapacityReservationFleetId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>capacity_reservation_fleets</code> resource, the following permissions are required:

### Create
```json
ec2:CreateCapacityReservationFleet,
ec2:ModifyCapacityReservationFleet,
ec2:DescribeCapacityReservationFleets,
ec2:CancelCapacityReservationFleets,
ec2:CreateCapacityReservation,
ec2:DescribeCapacityReservations,
ec2:CancelCapacityReservation,
ec2:DescribeInstances,
ec2:CreateTags,
iam:CreateServiceLinkedRole
```

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

### List
```json
ec2:DescribeCapacityReservationFleets,
ec2:DescribeCapacityReservations,
ec2:DescribeInstances
```

