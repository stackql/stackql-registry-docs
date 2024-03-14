---
title: assignment
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment
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
Gets an individual <code>assignment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>assignment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sso.assignment</code></td></tr>
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
FROM awscc.sso.assignment
WHERE data__Identifier = '<InstanceArn>|<TargetId>|<TargetType>|<PermissionSetArn>|<PrincipalType>|<PrincipalId>';
```

## Permissions

To operate on the <code>assignment</code> resource, the following permissions are required:

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

