---
title: managed_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_policy
  - iam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>managed_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>managed_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.managed_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A friendly description of the policy.</td></tr>
<tr><td><code>groups</code></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the group to attach the policy to.</td></tr>
<tr><td><code>managed_policy_name</code></td><td><code>string</code></td><td>The friendly name of the policy.</td></tr>
<tr><td><code>path</code></td><td><code>string</code></td><td>The path for the policy.</td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>The JSON policy document that you want to use as the content for the new policy.</td></tr>
<tr><td><code>roles</code></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the role to attach the policy to.</td></tr>
<tr><td><code>users</code></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the IAM user to attach the policy to.</td></tr>
<tr><td><code>policy_arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the managed policy</td></tr>
<tr><td><code>attachment_count</code></td><td><code>integer</code></td><td>The number of entities (users, groups, and roles) that the policy is attached to.</td></tr>
<tr><td><code>create_date</code></td><td><code>string</code></td><td>The date and time, in ISO 8601 date-time format, when the policy was created.</td></tr>
<tr><td><code>update_date</code></td><td><code>string</code></td><td>The date and time, in ISO 8601 date-time format, when the policy was last updated.</td></tr>
<tr><td><code>default_version_id</code></td><td><code>string</code></td><td>The identifier for the version of the policy that is set as the default version.</td></tr>
<tr><td><code>is_attachable</code></td><td><code>boolean</code></td><td>Specifies whether the policy can be attached to an IAM user, group, or role.</td></tr>
<tr><td><code>permissions_boundary_usage_count</code></td><td><code>integer</code></td><td>The number of entities (users and roles) for which the policy is used to set the permissions boundary.</td></tr>
<tr><td><code>policy_id</code></td><td><code>string</code></td><td>The stable and unique string identifying the policy.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
groups,
managed_policy_name,
path,
policy_document,
roles,
users,
policy_arn,
attachment_count,
create_date,
update_date,
default_version_id,
is_attachable,
permissions_boundary_usage_count,
policy_id
FROM awscc.iam.managed_policy
WHERE data__Identifier = '<PolicyArn>';
```

## Permissions

To operate on the <code>managed_policy</code> resource, the following permissions are required:

### Read
```json
iam:GetPolicy,
iam:ListEntitiesForPolicy,
iam:GetPolicyVersion
```

### Update
```json
iam:DetachRolePolicy,
iam:GetPolicy,
iam:ListPolicyVersions,
iam:DetachGroupPolicy,
iam:DetachUserPolicy,
iam:CreatePolicyVersion,
iam:DeletePolicyVersion,
iam:AttachGroupPolicy,
iam:AttachUserPolicy,
iam:AttachRolePolicy
```

### Delete
```json
iam:DetachRolePolicy,
iam:GetPolicy,
iam:ListPolicyVersions,
iam:DetachGroupPolicy,
iam:DetachUserPolicy,
iam:DeletePolicyVersion,
iam:DeletePolicy,
iam:ListEntitiesForPolicy
```

