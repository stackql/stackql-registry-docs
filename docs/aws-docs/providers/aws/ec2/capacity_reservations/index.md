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

Creates, updates, deletes or gets a <code>capacity_reservation</code> resource or lists <code>capacity_reservations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.capacity_reservations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tenancy" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="InstanceCount, AvailabilityZone, InstancePlatform, InstanceType, region" /></td>
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
Gets all <code>capacity_reservations</code> in a region.
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
FROM aws.ec2.capacity_reservations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>capacity_reservation</code>.
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
FROM aws.ec2.capacity_reservations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

