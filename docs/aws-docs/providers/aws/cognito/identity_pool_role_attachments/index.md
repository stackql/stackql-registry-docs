---
title: identity_pool_role_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pool_role_attachments
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

Creates, updates, deletes or gets an <code>identity_pool_role_attachment</code> resource or lists <code>identity_pool_role_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pool_role_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::IdentityPoolRoleAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.identity_pool_role_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="identity_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="roles" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_mappings" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="IdentityPoolId, region" /></td>
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
List all <code>identity_pool_role_attachments</code> in a region.
```sql
SELECT
region,
id
FROM aws.cognito.identity_pool_role_attachments
WHERE region = 'us-east-1';
```
Gets all properties from an <code>identity_pool_role_attachment</code>.
```sql
SELECT
region,
identity_pool_id,
roles,
id,
role_mappings
FROM aws.cognito.identity_pool_role_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>identity_pool_role_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.identity_pool_role_attachments (
 IdentityPoolId,
 region
)
SELECT 
'{{ IdentityPoolId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.identity_pool_role_attachments (
 IdentityPoolId,
 Roles,
 RoleMappings,
 region
)
SELECT 
 '{{ IdentityPoolId }}',
 '{{ Roles }}',
 '{{ RoleMappings }}',
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
  - name: identity_pool_role_attachment
    props:
      - name: IdentityPoolId
        value: '{{ IdentityPoolId }}'
      - name: Roles
        value: null
      - name: RoleMappings
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cognito.identity_pool_role_attachments
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>identity_pool_role_attachments</code> resource, the following permissions are required:

### Create
```json
cognito-identity:GetIdentityPoolRoles,
cognito-identity:SetIdentityPoolRoles,
iam:PassRole
```

### Read
```json
cognito-identity:GetIdentityPoolRoles
```

### Update
```json
cognito-identity:GetIdentityPoolRoles,
cognito-identity:SetIdentityPoolRoles,
iam:PassRole
```

### Delete
```json
cognito-identity:GetIdentityPoolRoles,
cognito-identity:SetIdentityPoolRoles
```

### List
```json
cognito-identity:GetIdentityPoolRoles
```

