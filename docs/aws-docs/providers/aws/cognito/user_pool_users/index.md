---
title: user_pool_users
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_users
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


Used to retrieve a list of <code>user_pool_users</code> in a region or to create or delete a <code>user_pool_users</code> resource, use <code>user_pool_user</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolUser</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_users" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td></td></tr>
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
username
FROM aws.cognito.user_pool_users
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
INSERT INTO aws.cognito.user_pool_users (
 UserPoolId,
 region
)
SELECT 
{{ .UserPoolId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DesiredDeliveryMediums": [
  "{{ DesiredDeliveryMediums[0] }}"
 ],
 "ForceAliasCreation": "{{ ForceAliasCreation }}",
 "UserAttributes": [
  {
   "Name": "{{ Name }}",
   "Value": "{{ Value }}"
  }
 ],
 "MessageAction": "{{ MessageAction }}",
 "Username": "{{ Username }}",
 "UserPoolId": "{{ UserPoolId }}",
 "ValidationData": [
  null
 ],
 "ClientMetadata": {}
}
>>>
--all properties
INSERT INTO aws.cognito.user_pool_users (
 DesiredDeliveryMediums,
 ForceAliasCreation,
 UserAttributes,
 MessageAction,
 Username,
 UserPoolId,
 ValidationData,
 ClientMetadata,
 region
)
SELECT 
 {{ .DesiredDeliveryMediums }},
 {{ .ForceAliasCreation }},
 {{ .UserAttributes }},
 {{ .MessageAction }},
 {{ .Username }},
 {{ .UserPoolId }},
 {{ .ValidationData }},
 {{ .ClientMetadata }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cognito.user_pool_users
WHERE data__Identifier = '<UserPoolId|Username>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pool_users</code> resource, the following permissions are required:

### Create
```json
cognito-idp:AdminCreateUser,
cognito-idp:AdminGetUser,
iam:PassRole
```

### Delete
```json
cognito-idp:AdminDeleteUser
```

### List
```json
cognito-idp:ListUsers
```

