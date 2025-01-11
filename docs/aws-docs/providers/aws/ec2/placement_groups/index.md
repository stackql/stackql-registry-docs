---
title: placement_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - placement_groups
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

Creates, updates, deletes or gets a <code>placement_group</code> resource or lists <code>placement_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>placement_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::PlacementGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.placement_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="strategy" /></td><td><code>string</code></td><td>The placement strategy.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The Group Name of Placement Group.</td></tr>
<tr><td><CopyableCode code="spread_level" /></td><td><code>string</code></td><td>The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread</td></tr>
<tr><td><CopyableCode code="partition_count" /></td><td><code>integer</code></td><td>The number of partitions. Valid only when **Strategy** is set to `partition`</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html"><code>AWS::EC2::PlacementGroup</code></a>.

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
Gets all <code>placement_groups</code> in a region.
```sql
SELECT
region,
strategy,
group_name,
spread_level,
partition_count,
tags
FROM aws.ec2.placement_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>placement_group</code>.
```sql
SELECT
region,
strategy,
group_name,
spread_level,
partition_count,
tags
FROM aws.ec2.placement_groups
WHERE region = 'us-east-1' AND data__Identifier = '<GroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>placement_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.placement_groups (
 Strategy,
 SpreadLevel,
 PartitionCount,
 Tags,
 region
)
SELECT 
'{{ Strategy }}',
 '{{ SpreadLevel }}',
 '{{ PartitionCount }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.placement_groups (
 Strategy,
 SpreadLevel,
 PartitionCount,
 Tags,
 region
)
SELECT 
 '{{ Strategy }}',
 '{{ SpreadLevel }}',
 '{{ PartitionCount }}',
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
  - name: placement_group
    props:
      - name: Strategy
        value: '{{ Strategy }}'
      - name: SpreadLevel
        value: '{{ SpreadLevel }}'
      - name: PartitionCount
        value: '{{ PartitionCount }}'
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
DELETE FROM aws.ec2.placement_groups
WHERE data__Identifier = '<GroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>placement_groups</code> resource, the following permissions are required:

### Create
```json
ec2:CreatePlacementGroup,
ec2:DescribePlacementGroups,
ec2:CreateTags
```

### Read
```json
ec2:DescribePlacementGroups
```

### Delete
```json
ec2:DeletePlacementGroup,
ec2:DescribePlacementGroups
```

### List
```json
ec2:DescribePlacementGroups
```
