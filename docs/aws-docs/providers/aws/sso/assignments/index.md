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
Used to retrieve a list of <code>assignments</code> in a region or create a <code>assignments</code> resource, use <code>assignment</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO assignmet</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sso.assignments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The sso instance that the permission set is owned.</td></tr>
<tr><td><code>target_id</code></td><td><code>string</code></td><td>The account id to be provisioned.</td></tr>
<tr><td><code>target_type</code></td><td><code>string</code></td><td>The type of resource to be provsioned to, only aws account now</td></tr>
<tr><td><code>permission_set_arn</code></td><td><code>string</code></td><td>The permission set that the assignemt will be assigned</td></tr>
<tr><td><code>principal_type</code></td><td><code>string</code></td><td>The assignee's type, user&#x2F;group</td></tr>
<tr><td><code>principal_id</code></td><td><code>string</code></td><td>The assignee's identifier, user id&#x2F;group id</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
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
WHERE region = 'us-east-1'
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

### List
```json
sso:ListAccountAssignments,
iam:ListRolePolicies
```

