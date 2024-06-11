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

Creates, updates, deletes or gets an <code>assignment</code> resource or lists <code>assignments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO assignmet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.assignments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The sso instance that the permission set is owned.</td></tr>
<tr><td><CopyableCode code="target_id" /></td><td><code>string</code></td><td>The account id to be provisioned.</td></tr>
<tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>The type of resource to be provsioned to, only aws account now</td></tr>
<tr><td><CopyableCode code="permission_set_arn" /></td><td><code>string</code></td><td>The permission set that the assignemt will be assigned</td></tr>
<tr><td><CopyableCode code="principal_type" /></td><td><code>string</code></td><td>The assignee's type, user/group</td></tr>
<tr><td><CopyableCode code="principal_id" /></td><td><code>string</code></td><td>The assignee's identifier, user id/group id</td></tr>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>assignments</code> in a region.
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
Gets all properties from an <code>assignment</code>.
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
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceArn>|<TargetId>|<TargetType>|<PermissionSetArn>|<PrincipalType>|<PrincipalId>';
```


## `INSERT` example

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

## `DELETE` example

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

### Read
```json
sso:ListAccountAssignments,
iam:GetSAMLProvider,
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

