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

Creates, updates, deletes or gets an <code>user_pool_group</code> resource or lists <code>user_pool_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="precedence" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="UserPoolId, region" /></td>
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
Gets all <code>user_pool_groups</code> in a region.
```sql
SELECT
region,
description,
group_name,
precedence,
role_arn,
user_pool_id
FROM aws.cognito.user_pool_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_pool_group</code>.
```sql
SELECT
region,
description,
group_name,
precedence,
role_arn,
user_pool_id
FROM aws.cognito.user_pool_groups
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<GroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_pool_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.user_pool_groups (
 UserPoolId,
 region
)
SELECT 
'{{ UserPoolId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pool_groups (
 Description,
 GroupName,
 Precedence,
 RoleArn,
 UserPoolId,
 region
)
SELECT 
 '{{ Description }}',
 '{{ GroupName }}',
 '{{ Precedence }}',
 '{{ RoleArn }}',
 '{{ UserPoolId }}',
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
  - name: user_pool_group
    props:
      - name: Description
        value: '{{ Description }}'
      - name: GroupName
        value: '{{ GroupName }}'
      - name: Precedence
        value: '{{ Precedence }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: UserPoolId
        value: '{{ UserPoolId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
cognito-idp:GetGroup
```

### Update
```json
cognito-idp:UpdateGroup,
iam:PassRole,
iam:PutRolePolicy
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

