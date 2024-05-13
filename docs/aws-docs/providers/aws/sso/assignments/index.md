---
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
  - sso
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


Used to retrieve a list of <code>assignments</code> in a region or to create or delete a <code>assignments</code> resource, use <code>assignment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO assignmet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.assignments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The sso instance that the permission set is owned.</td></tr>
<tr><td><CopyableCode code="target_id" /></td><td><code>string</code></td><td>The account id to be provisioned.</td></tr>
<tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>The type of resource to be provsioned to, only aws account now</td></tr>
<tr><td><CopyableCode code="permission_set_arn" /></td><td><code>string</code></td><td>The permission set that the assignemt will be assigned</td></tr>
<tr><td><CopyableCode code="principal_type" /></td><td><code>string</code></td><td>The assignee's type, user&#x2F;group</td></tr>
<tr><td><CopyableCode code="principal_id" /></td><td><code>string</code></td><td>The assignee's identifier, user id&#x2F;group id</td></tr>
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
    <td><CopyableCode code="InstanceArn, TargetId, TargetType, PermissionSetArn, PrincipalType, PrincipalId, region" /></td>
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
instance_arn,
target_id,
target_type,
permission_set_arn,
principal_type,
principal_id
FROM aws.sso.assignments
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>assignment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sso.assignments (
 InstanceArn,
 TargetId,
 TargetType,
 PermissionSetArn,
 PrincipalType,
 PrincipalId,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ TargetId }}',
 '{{ TargetType }}',
 '{{ PermissionSetArn }}',
 '{{ PrincipalType }}',
 '{{ PrincipalId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sso.assignments (
 InstanceArn,
 TargetId,
 TargetType,
 PermissionSetArn,
 PrincipalType,
 PrincipalId,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ TargetId }}',
 '{{ TargetType }}',
 '{{ PermissionSetArn }}',
 '{{ PrincipalType }}',
 '{{ PrincipalId }}',
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
  - name: assignment
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: TargetId
        value: '{{ TargetId }}'
      - name: TargetType
        value: '{{ TargetType }}'
      - name: PermissionSetArn
        value: '{{ PermissionSetArn }}'
      - name: PrincipalType
        value: '{{ PrincipalType }}'
      - name: PrincipalId
        value: '{{ PrincipalId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.sso.assignments
WHERE data__Identifier = '<InstanceArn|TargetId|TargetType|PermissionSetArn|PrincipalType|PrincipalId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>assignments</code> resource, the following permissions are required:

### Create
```json
sso:CreateAccountAssignment,
sso:DescribeAccountAssignmentCreationStatus,
sso:ListAccountAssignments,
iam:GetSAMLProvider,
iam:CreateSAMLProvider,
iam:AttachRolePolicy,
iam:PutRolePolicy,
iam:CreateRole,
iam:ListRolePolicies
```

### Delete
```json
sso:ListAccountAssignments,
sso:DeleteAccountAssignment,
sso:DescribeAccountAssignmentDeletionStatus,
iam:GetSAMLProvider,
iam:ListRolePolicies
```

### List
```json
sso:ListAccountAssignments,
iam:ListRolePolicies
```

