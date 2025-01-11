---
title: db_shard_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - db_shard_groups
  - rds
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

Creates, updates, deletes or gets a <code>db_shard_group</code> resource or lists <code>db_shard_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_shard_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::DBShardGroup resource creates an Amazon Aurora Limitless DB Shard Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_shard_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_shard_group_resource_id" /></td><td><code>string</code></td><td>The Amazon Web Services Region-unique, immutable identifier for the DB shard group.</td></tr>
<tr><td><CopyableCode code="db_shard_group_identifier" /></td><td><code>string</code></td><td>The name of the DB shard group.</td></tr>
<tr><td><CopyableCode code="db_cluster_identifier" /></td><td><code>string</code></td><td>The name of the primary DB cluster for the DB shard group.</td></tr>
<tr><td><CopyableCode code="compute_redundancy" /></td><td><code>integer</code></td><td>Specifies whether to create standby instances for the DB shard group.</td></tr>
<tr><td><CopyableCode code="max_ac_u" /></td><td><code>number</code></td><td>The maximum capacity of the DB shard group in Aurora capacity units (ACUs).</td></tr>
<tr><td><CopyableCode code="min_ac_u" /></td><td><code>number</code></td><td>The minimum capacity of the DB shard group in Aurora capacity units (ACUs).</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>Indicates whether the DB shard group is publicly accessible.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The connection endpoint for the DB shard group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbshardgroup.html"><code>AWS::RDS::DBShardGroup</code></a>.

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
    <td><CopyableCode code="DBClusterIdentifier, MaxACU, region" /></td>
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
Gets all <code>db_shard_groups</code> in a region.
```sql
SELECT
region,
db_shard_group_resource_id,
db_shard_group_identifier,
db_cluster_identifier,
compute_redundancy,
max_ac_u,
min_ac_u,
publicly_accessible,
endpoint,
tags
FROM aws.rds.db_shard_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>db_shard_group</code>.
```sql
SELECT
region,
db_shard_group_resource_id,
db_shard_group_identifier,
db_cluster_identifier,
compute_redundancy,
max_ac_u,
min_ac_u,
publicly_accessible,
endpoint,
tags
FROM aws.rds.db_shard_groups
WHERE region = 'us-east-1' AND data__Identifier = '<DBShardGroupIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>db_shard_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rds.db_shard_groups (
 DBClusterIdentifier,
 MaxACU,
 region
)
SELECT 
'{{ DBClusterIdentifier }}',
 '{{ MaxACU }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.db_shard_groups (
 DBShardGroupIdentifier,
 DBClusterIdentifier,
 ComputeRedundancy,
 MaxACU,
 MinACU,
 PubliclyAccessible,
 Tags,
 region
)
SELECT 
 '{{ DBShardGroupIdentifier }}',
 '{{ DBClusterIdentifier }}',
 '{{ ComputeRedundancy }}',
 '{{ MaxACU }}',
 '{{ MinACU }}',
 '{{ PubliclyAccessible }}',
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
  - name: db_shard_group
    props:
      - name: DBShardGroupIdentifier
        value: '{{ DBShardGroupIdentifier }}'
      - name: DBClusterIdentifier
        value: '{{ DBClusterIdentifier }}'
      - name: ComputeRedundancy
        value: '{{ ComputeRedundancy }}'
      - name: MaxACU
        value: null
      - name: MinACU
        value: null
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
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
DELETE FROM aws.rds.db_shard_groups
WHERE data__Identifier = '<DBShardGroupIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_shard_groups</code> resource, the following permissions are required:

### Create
```json
rds:AddTagsToResource,
rds:CreateDBShardGroup,
rds:DescribeDBClusters,
rds:DescribeDBShardGroups,
rds:ListTagsForResource
```

### Read
```json
rds:DescribeDBShardGroups,
rds:ListTagsForResource
```

### Update
```json
rds:AddTagsToResource,
rds:DescribeDBShardGroups,
rds:DescribeDBClusters,
rds:RemoveTagsFromResource,
rds:ModifyDBShardGroup,
rds:ListTagsForResource
```

### Delete
```json
rds:DeleteDBShardGroup,
rds:DescribeDBClusters,
rds:DescribeDbShardGroups
```

### List
```json
rds:DescribeDBShardGroups,
rds:ListTagsForResource
```
