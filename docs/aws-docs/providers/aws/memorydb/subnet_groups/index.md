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


Used to retrieve a list of <code>subnet_groups</code> in a region or to create or delete a <code>subnet_groups</code> resource, use <code>subnet_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::SubnetGroup resource creates an Amazon MemoryDB Subnet Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.subnet_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="subnet_group_name" /></td><td><code>string</code></td><td>The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.</td></tr>
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
subnet_group_name
FROM aws.memorydb.subnet_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "SubnetGroupName": "{{ SubnetGroupName }}",
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.memorydb.subnet_groups (
 SubnetGroupName,
 SubnetIds,
 region
)
SELECT 
{{ .SubnetGroupName }},
 {{ .SubnetIds }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "SubnetGroupName": "{{ SubnetGroupName }}",
 "Description": "{{ Description }}",
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.memorydb.subnet_groups (
 SubnetGroupName,
 Description,
 SubnetIds,
 Tags,
 region
)
SELECT 
 {{ .SubnetGroupName }},
 {{ .Description }},
 {{ .SubnetIds }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
memorydb:DeleteSubnetGroup,
memorydb:DescribeSubnetGroups
```

### List
```json
memorydb:DescribeSubnetGroups
```

