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
Retrieves a list of <code>assignments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>assignments</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sso.assignments</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn,
target_id,
target_type,
permission_set_arn,
principal_type,
principal_id
FROM awscc.sso.assignments
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

