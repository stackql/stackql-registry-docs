---
title: subnet_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_groups
  - memorydb
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

Creates, updates, deletes or gets a <code>subnet_group</code> resource or lists <code>subnet_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::SubnetGroup resource creates an Amazon MemoryDB Subnet Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.subnet_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="subnet_group_name" /></td><td><code>string</code></td><td>The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description of the subnet group.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>A list of VPC subnet IDs for the subnet group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this subnet group.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the subnet group.</td></tr>
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
    <td><CopyableCode code="SubnetGroupName, SubnetIds, region" /></td>
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
List all <code>subnet_groups</code> in a region.
```sql
SELECT
region,
subnet_group_name
FROM aws.memorydb.subnet_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>subnet_group</code>.
```sql
SELECT
region,
subnet_group_name,
description,
subnet_ids,
tags,
arn
FROM aws.memorydb.subnet_groups
WHERE region = 'us-east-1' AND data__Identifier = '<SubnetGroupName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subnet_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.memorydb.subnet_groups (
 SubnetGroupName,
 SubnetIds,
 region
)
SELECT 
'{{ SubnetGroupName }}',
 '{{ SubnetIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.memorydb.subnet_groups (
 SubnetGroupName,
 Description,
 SubnetIds,
 Tags,
 region
)
SELECT 
 '{{ SubnetGroupName }}',
 '{{ Description }}',
 '{{ SubnetIds }}',
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
  - name: subnet_group
    props:
      - name: SubnetGroupName
        value: '{{ SubnetGroupName }}'
      - name: Description
        value: '{{ Description }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
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
DELETE FROM aws.memorydb.subnet_groups
WHERE data__Identifier = '<SubnetGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subnet_groups</code> resource, the following permissions are required:

### Create
```json
memorydb:CreateSubnetGroup,
memorydb:DescribeSubnetGroups,
memorydb:TagResource,
memorydb:ListTags
```

### Read
```json
memorydb:DescribeSubnetGroups,
memorydb:ListTags
```

### Update
```json
memorydb:UpdateSubnetGroup,
memorydb:DescribeSubnetGroups,
memorydb:ListTags,
memorydb:TagResource,
memorydb:UntagResource
```

### Delete
```json
memorydb:DeleteSubnetGroup,
memorydb:DescribeSubnetGroups
```

### List
```json
memorydb:DescribeSubnetGroups
```

