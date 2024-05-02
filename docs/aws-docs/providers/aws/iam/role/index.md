---
title: role
hide_title: false
hide_table_of_contents: false
keywords:
  - role
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
Gets or operates on an individual <code>role</code> resource, use <code>roles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new role for your AWS-account.&lt;br&#x2F;&gt;  For more information about roles, see &#91;IAM roles&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;id_roles.html) in the *IAM User Guide*. For information about quotas for role names and the number of roles you can create, see &#91;IAM and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.role</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assume_role_policy_document</code></td><td><code>object</code></td><td>The trust policy that is associated with this role. Trust policies define which entities can assume the role. You can associate only one trust policy with a role. For an example of a policy that can be used to assume a role, see &#91;Template Examples&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-iam-role.html#aws-resource-iam-role--examples). For more information about the elements that you can use in an IAM policy, see &#91;Policy Elements Reference&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_policies_elements.html) in the *User Guide*.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the role that you provide.</td></tr>
<tr><td><code>managed_policy_arns</code></td><td><code>array</code></td><td>A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.&lt;br&#x2F;&gt; For more information about ARNs, see &#91;Amazon Resource Names (ARNs) and Service Namespaces&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><code>max_session_duration</code></td><td><code>integer</code></td><td>The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default value of one hour is applied. This setting can have a value from 1 hour to 12 hours.&lt;br&#x2F;&gt; Anyone who assumes the role from the CLI or API can use the ``DurationSeconds`` API parameter or the ``duration-seconds`` CLI parameter to request a longer session. The ``MaxSessionDuration`` setting determines the maximum duration that can be requested using the ``DurationSeconds`` parameter. If users don't specify a value for the ``DurationSeconds`` parameter, their security credentials are valid for one hour by default. This applies when you use the ``AssumeRole*`` API operations or the ``assume-role*`` CLI operations but does not apply when you use those operations to create a console URL. For more information, see &#91;Using IAM roles&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;id_roles_use.html) in the *IAM User Guide*.</td></tr>
<tr><td><code>path</code></td><td><code>string</code></td><td>The path to the role. For more information about paths, see &#91;IAM Identifiers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;Using_Identifiers.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; This parameter is optional. If it is not included, it defaults to a slash (&#x2F;).&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of either a forward slash (&#x2F;) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (``\u0021``) through the DEL character (``\u007F``), including most punctuation characters, digits, and upper and lowercased letters.</td></tr>
<tr><td><code>permissions_boundary</code></td><td><code>string</code></td><td>The ARN of the policy used to set the permissions boundary for the role.&lt;br&#x2F;&gt; For more information about permissions boundaries, see &#91;Permissions boundaries for IAM identities&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;access_policies_boundaries.html) in the *IAM User Guide*.</td></tr>
<tr><td><code>policies</code></td><td><code>array</code></td><td>Adds or updates an inline policy document that is embedded in the specified IAM role.&lt;br&#x2F;&gt; When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role. You can update a role's trust policy later. For more information about IAM roles, go to &#91;Using Roles to Delegate Permissions and Federate Identities&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;roles-toplevel.html).&lt;br&#x2F;&gt; A role can also have an attached managed policy. For information about policies, see &#91;Managed Policies and Inline Policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;policies-managed-vs-inline.html) in the *User Guide*.&lt;br&#x2F;&gt; For information about limits on the number of inline policies that you can embed with a role, see &#91;Limitations on Entities&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;LimitationsOnEntities.html) in the *User Guide*.&lt;br&#x2F;&gt;  If an external policy (such as ``AWS::IAM::Policy`` or</td></tr>
<tr><td><code>role_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_name</code></td><td><code>string</code></td><td>A name for the IAM role, up to 64 characters in length. For valid values, see the ``RoleName`` parameter for the &#91;CreateRole&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;APIReference&#x2F;API_CreateRole.html) action in the *User Guide*.&lt;br&#x2F;&gt; This parameter allows (per its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The role name must be unique within the account. Role names are not distinguished by case. For example, you cannot create roles named both "Role1" and "role1".&lt;br&#x2F;&gt; If you don't specify a name, CFN generates a unique physical ID and uses that ID for the role name.&lt;br&#x2F;&gt; If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;Use</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags that are attached to the role. For more information about tagging, see &#91;Tagging IAM resources&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;id_tags.html) in the *IAM User Guide*.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
assume_role_policy_document,
description,
managed_policy_arns,
max_session_duration,
path,
permissions_boundary,
policies,
role_id,
role_name,
tags
FROM aws.iam.role
WHERE data__Identifier = '<RoleName>';
```

## Permissions

To operate on the <code>role</code> resource, the following permissions are required:

### Read
```json
iam:GetRole,
iam:ListAttachedRolePolicies,
iam:ListRolePolicies,
iam:GetRolePolicy
```

### Update
```json
iam:UpdateRole,
iam:UpdateRoleDescription,
iam:UpdateAssumeRolePolicy,
iam:DetachRolePolicy,
iam:AttachRolePolicy,
iam:DeleteRolePermissionsBoundary,
iam:PutRolePermissionsBoundary,
iam:DeleteRolePolicy,
iam:PutRolePolicy,
iam:TagRole,
iam:UntagRole
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

