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

Creates, updates, deletes or gets a <code>capacity_reservation_fleet</code> resource or lists <code>capacity_reservation_fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation_fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservationFleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.capacity_reservation_fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="allocation_strategy" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
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
Gets all <code>capacity_reservation_fleets</code> in a region.
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
FROM aws.ec2.capacity_reservation_fleets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>capacity_reservation_fleet</code>.
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
FROM aws.ec2.capacity_reservation_fleets
WHERE region = 'us-east-1' AND data__Identifier = '<CapacityReservationFleetId>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

