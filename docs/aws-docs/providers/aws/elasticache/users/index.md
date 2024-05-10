---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - elasticache
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


Used to retrieve a list of <code>users</code> in a region or to create or delete a <code>users</code> resource, use <code>user</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElastiCache::User</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.users" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_id" /></td><td><code>string</code></td><td>The ID of the user.</td></tr>
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
user_id
FROM aws.elasticache.users
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
 "UserId": "{{ UserId }}",
 "UserName": "{{ UserName }}",
 "Engine": "{{ Engine }}"
}
>>>
--required properties only
INSERT INTO aws.elasticache.users (
 UserId,
 UserName,
 Engine,
 region
)
SELECT 
{{ UserId }},
 {{ UserName }},
 {{ Engine }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "UserId": "{{ UserId }}",
 "UserName": "{{ UserName }}",
 "Engine": "{{ Engine }}",
 "AccessString": "{{ AccessString }}",
 "NoPasswordRequired": "{{ NoPasswordRequired }}",
 "Passwords": [
  "{{ Passwords[0] }}"
 ],
 "AuthenticationMode": {
  "Type": "{{ Type }}",
  "Passwords": [
   "{{ Passwords[0] }}"
  ]
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.elasticache.users (
 UserId,
 UserName,
 Engine,
 AccessString,
 NoPasswordRequired,
 Passwords,
 AuthenticationMode,
 Tags,
 region
)
SELECT 
 {{ UserId }},
 {{ UserName }},
 {{ Engine }},
 {{ AccessString }},
 {{ NoPasswordRequired }},
 {{ Passwords }},
 {{ AuthenticationMode }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.elasticache.users
WHERE data__Identifier = '<UserId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>users</code> resource, the following permissions are required:

### Create
```json
elasticache:CreateUser,
elasticache:DescribeUsers,
elasticache:ListTagsForResource,
elasticache:AddTagsToResource
```

### Delete
```json
elasticache:DeleteUser,
elasticache:DescribeUsers
```

### List
```json
elasticache:DescribeUsers,
elasticache:ListTagsForResource
```

