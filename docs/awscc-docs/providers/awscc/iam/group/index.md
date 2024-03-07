---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
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
Gets an individual <code>group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Arn of the group to create</td></tr>
<tr><td><code>group_name</code></td><td><code>string</code></td><td>The name of the group to create</td></tr>
<tr><td><code>managed_policy_arns</code></td><td><code>array</code></td><td>A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role. </td></tr>
<tr><td><code>path</code></td><td><code>string</code></td><td>The path to the group</td></tr>
<tr><td><code>policies</code></td><td><code>array</code></td><td>Adds or updates an inline policy document that is embedded in the specified IAM group</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>group</code> resource, the following permissions are required:

### Read
```json
iam:GetGroup,
iam:ListGroupPolicies,
iam:GetGroupPolicy,
iam:ListAttachedGroupPolicies
```

### Update
```json
iam:GetGroup,
iam:UpdateGroup,
iam:DetachGroupPolicy,
iam:AttachGroupPolicy,
iam:DeleteGroupPolicy,
iam:PutGroupPolicy,
iam:GetGroupPolicy
```

### Delete
```json
iam:GetGroup,
iam:DeleteGroup,
iam:ListAttachedGroupPolicies,
iam:ListGroupPolicies,
iam:DetachGroupPolicy,
iam:DeleteGroupPolicy,
iam:GetGroupPolicy
```


## Example
```sql
SELECT
region,
arn,
group_name,
managed_policy_arns,
path,
policies
FROM awscc.iam.group
WHERE data__Identifier = '&lt;GroupName&gt;'
```
