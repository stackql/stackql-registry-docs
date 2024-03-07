---
title: instance_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_profile
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
Gets an individual <code>instance_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance_profile</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.instance_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>path</code></td><td><code>string</code></td><td>The path to the instance profile. For more information about paths, see &#91;IAM Identifiers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;Using_Identifiers.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; This parameter is optional. If it is not included, it defaults to a slash (&#x2F;).&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of either a forward slash (&#x2F;) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (``\u0021``) through the DEL character (``\u007F``), including most punctuation characters, digits, and upper and lowercased letters.</td></tr>
<tr><td><code>roles</code></td><td><code>array</code></td><td>The name of the role to associate with the instance profile. Only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.</td></tr>
<tr><td><code>instance_profile_name</code></td><td><code>string</code></td><td>The name of the instance profile to create.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>instance_profile</code> resource, the following permissions are required:

### Read
```json
iam:GetInstanceProfile
```

### Update
```json
iam:PassRole,
iam:RemoveRoleFromInstanceProfile,
iam:AddRoleToInstanceProfile,
iam:GetInstanceProfile
```

### Delete
```json
iam:GetInstanceProfile,
iam:RemoveRoleFromInstanceProfile,
iam:DeleteInstanceProfile
```


## Example
```sql
SELECT
region,
path,
roles,
instance_profile_name,
arn
FROM awscc.iam.instance_profile
WHERE data__Identifier = '&lt;InstanceProfileName&gt;'
```
