---
title: user_pool_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_groups
  - cognito
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


Used to retrieve a list of <code>user_pool_groups</code> in a region or to create or delete a <code>user_pool_groups</code> resource, use <code>user_pool_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td></td></tr>
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
user_pool_id,
group_name
FROM aws.cognito.user_pool_groups
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
 "UserPoolId": "{{ UserPoolId }}"
}
>>>
--required properties only
INSERT INTO aws.cognito.user_pool_groups (
 UserPoolId,
 region
)
SELECT 
{{ UserPoolId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "GroupName": "{{ GroupName }}",
 "Precedence": "{{ Precedence }}",
 "RoleArn": "{{ RoleArn }}",
 "UserPoolId": "{{ UserPoolId }}"
}
>>>
--all properties
INSERT INTO aws.cognito.user_pool_groups (
 Description,
 GroupName,
 Precedence,
 RoleArn,
 UserPoolId,
 region
)
SELECT 
 {{ Description }},
 {{ GroupName }},
 {{ Precedence }},
 {{ RoleArn }},
 {{ UserPoolId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cognito.user_pool_groups
WHERE data__Identifier = '<UserPoolId|GroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pool_groups</code> resource, the following permissions are required:

### Create
```json
cognito-idp:CreateGroup,
iam:PassRole,
iam:PutRolePolicy,
cognito-idp:GetGroup
```

### Delete
```json
cognito-idp:DeleteGroup,
cognito-idp:GetGroup,
iam:PutRolePolicy
```

### List
```json
cognito-idp:ListGroups
```

