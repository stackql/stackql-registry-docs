---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
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
Retrieves a list of <code>roles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>roles</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.roles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>role_name</code></td><td><code>string</code></td><td>A name for the IAM role, up to 64 characters in length. For valid values, see the ``RoleName`` parameter for the &#91;CreateRole&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;APIReference&#x2F;API_CreateRole.html) action in the *User Guide*.&lt;br&#x2F;&gt; This parameter allows (per its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The role name must be unique within the account. Role names are not distinguished by case. For example, you cannot create roles named both "Role1" and "role1".&lt;br&#x2F;&gt; If you don't specify a name, CFN generates a unique physical ID and uses that ID for the role name.&lt;br&#x2F;&gt; If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;Use</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>roles</code> resource, the following permissions are required:

### Create
```json
iam:CreateRole,
iam:PutRolePolicy,
iam:AttachRolePolicy,
iam:GetRolePolicy,
iam:TagRole,
iam:UntagRole,
iam:GetRole
```

### List
```json
iam:ListRoles
```


## Example
```sql
SELECT
region,
role_name
FROM awscc.iam.roles

```
