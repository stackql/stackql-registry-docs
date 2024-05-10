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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>roles</code> in a region or to create or delete a <code>roles</code> resource, use <code>role</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new role for your AWS-account.&lt;br&#x2F;&gt;  For more information about roles, see &#91;IAM roles&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;id_roles.html) in the *IAM User Guide*. For information about quotas for role names and the number of roles you can create, see &#91;IAM and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.roles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>A name for the IAM role, up to 64 characters in length. For valid values, see the ``RoleName`` parameter for the &#91;CreateRole&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;APIReference&#x2F;API_CreateRole.html) action in the *User Guide*.&lt;br&#x2F;&gt; This parameter allows (per its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The role name must be unique within the account. Role names are not distinguished by case. For example, you cannot create roles named both "Role1" and "role1".&lt;br&#x2F;&gt; If you don't specify a name, CFN generates a unique physical ID and uses that ID for the role name.&lt;br&#x2F;&gt; If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;Use</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
role_name
FROM aws.iam.roles
;
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "AssumeRolePolicyDocument": {}
}
>>>
--required properties only
INSERT INTO aws.iam.roles (
 AssumeRolePolicyDocument,
 region
)
SELECT 
{{ .AssumeRolePolicyDocument }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AssumeRolePolicyDocument": {},
 "Description": "{{ Description }}",
 "ManagedPolicyArns": [
  "{{ ManagedPolicyArns[0] }}"
 ],
 "MaxSessionDuration": "{{ MaxSessionDuration }}",
 "Path": "{{ Path }}",
 "PermissionsBoundary": "{{ PermissionsBoundary }}",
 "Policies": [
  {
   "PolicyDocument": {},
   "PolicyName": "{{ PolicyName }}"
  }
 ],
 "RoleName": "{{ RoleName }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iam.roles (
 AssumeRolePolicyDocument,
 Description,
 ManagedPolicyArns,
 MaxSessionDuration,
 Path,
 PermissionsBoundary,
 Policies,
 RoleName,
 Tags,
 region
)
SELECT 
 {{ .AssumeRolePolicyDocument }},
 {{ .Description }},
 {{ .ManagedPolicyArns }},
 {{ .MaxSessionDuration }},
 {{ .Path }},
 {{ .PermissionsBoundary }},
 {{ .Policies }},
 {{ .RoleName }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iam.roles
WHERE data__Identifier = '<RoleName>'
AND region = 'us-east-1';
```

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

### Delete
```json
iam:DeleteRole,
iam:DetachRolePolicy,
iam:DeleteRolePolicy,
iam:GetRole,
iam:ListAttachedRolePolicies,
iam:ListRolePolicies,
iam:TagRole,
iam:UntagRole
```

### List
```json
iam:ListRoles
```

