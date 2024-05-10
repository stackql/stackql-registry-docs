---
title: role_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - role_aliases
  - iot
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


Used to retrieve a list of <code>role_aliases</code> in a region or to create or delete a <code>role_aliases</code> resource, use <code>role_alias</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.role_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="role_alias" /></td><td><code>string</code></td><td></td></tr>
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
role_alias
FROM aws.iot.role_aliases
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
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.iot.role_aliases (
 RoleArn,
 region
)
SELECT 
{{ .RoleArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "RoleAlias": "{{ RoleAlias }}",
 "RoleArn": "{{ RoleArn }}",
 "CredentialDurationSeconds": "{{ CredentialDurationSeconds }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iot.role_aliases (
 RoleAlias,
 RoleArn,
 CredentialDurationSeconds,
 Tags,
 region
)
SELECT 
 {{ .RoleAlias }},
 {{ .RoleArn }},
 {{ .CredentialDurationSeconds }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.role_aliases
WHERE data__Identifier = '<RoleAlias>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>role_aliases</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:PassRole,
iot:CreateRoleAlias,
iot:DescribeRoleAlias,
iot:TagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:DeleteRoleAlias,
iot:DescribeRoleAlias
```

### List
```json
iot:ListRoleAliases
```

