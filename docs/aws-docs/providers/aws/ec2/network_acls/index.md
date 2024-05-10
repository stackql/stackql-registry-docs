---
title: network_acls
hide_title: false
hide_table_of_contents: false
keywords:
  - network_acls
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


Used to retrieve a list of <code>network_acls</code> in a region or to create or delete a <code>network_acls</code> resource, use <code>network_acl</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a network ACL for your VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_acls" /></td></tr>
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
FROM aws.ec2.network_acls
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
 "VpcId": "{{ VpcId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.network_acls (
 VpcId,
 region
)
SELECT 
{{ VpcId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "VpcId": "{{ VpcId }}"
}
>>>
--all properties
INSERT INTO aws.ec2.network_acls (
 Tags,
 VpcId,
 region
)
SELECT 
 {{ Tags }},
 {{ VpcId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.network_acls
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_acls</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkAcl,
ec2:DescribeNetworkAcls,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteTags,
ec2:DeleteNetworkAcl,
ec2:DescribeNetworkAcls
```

### List
```json
ec2:DescribeNetworkAcls
```

