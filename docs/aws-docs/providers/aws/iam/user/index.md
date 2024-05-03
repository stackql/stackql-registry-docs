---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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

Gets or operates on an individual <code>user</code> resource, use <code>users</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new IAM user for your AWS-account.&lt;br&#x2F;&gt;  For information about quotas for the number of IAM users you can create, see &#91;IAM and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.user" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td>The path for the user name. For more information about paths, see &#91;IAM identifiers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;Using_Identifiers.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; This parameter is optional. If it is not included, it defaults to a slash (&#x2F;).&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of either a forward slash (&#x2F;) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (``\u0021``) through the DEL character (``\u007F``), including most punctuation characters, digits, and upper and lowercased letters.</td></tr>
<tr><td><CopyableCode code="managed_policy_arns" /></td><td><code>array</code></td><td>A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the user.&lt;br&#x2F;&gt; For more information about ARNs, see &#91;Amazon Resource Names (ARNs) and Service Namespaces&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>array</code></td><td>Adds or updates an inline policy document that is embedded in the specified IAM user. To view AWS::IAM::User snippets, see &#91;Declaring an User Resource&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;quickref-iam.html#scenario-iam-user).&lt;br&#x2F;&gt;  The name of each policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail. &lt;br&#x2F;&gt;  For information about limits on the number of inline policies that you can embed in a user, see &#91;Limitations on Entities&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;LimitationsOnEntities.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td>The name of the user to create. Do not include the path in this value.&lt;br&#x2F;&gt; This parameter allows (per its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The user name must be unique within the account. User names are not distinguished by case. For example, you cannot create users named both "John" and "john".&lt;br&#x2F;&gt; If you don't specify a name, CFN generates a unique physical ID and uses that ID for the user name.&lt;br&#x2F;&gt; If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;using-iam-template.html#using-iam-capabilities).&lt;br&#x2F;&gt;  Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``&#123;"Fn::Join": &#91;"", &#91;&#123;"Ref": "AWS::Region"&#125;, &#123;"Ref": "MyResourceName"&#125;&#93;&#93;&#125;``.</td></tr>
<tr><td><CopyableCode code="groups" /></td><td><code>array</code></td><td>A list of group names to which you want to add the user.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="login_profile" /></td><td><code>object</code></td><td>Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the console.&lt;br&#x2F;&gt; You can use the CLI, the AWS API, or the *Users* page in the IAM console to create a password for any IAM user. Use &#91;ChangePassword&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;APIReference&#x2F;API_ChangePassword.html) to update your own existing password in the *My Security Credentials* page in the console.&lt;br&#x2F;&gt; For more information about managing passwords, see &#91;Managing passwords&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;Using_ManagingLogins.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags that you want to attach to the new user. Each tag consists of a key name and an associated value. For more information about tagging, see &#91;Tagging IAM resources&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;id_tags.html) in the *IAM User Guide*.&lt;br&#x2F;&gt;  If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.</td></tr>
<tr><td><CopyableCode code="permissions_boundary" /></td><td><code>string</code></td><td>The ARN of the managed policy that is used to set the permissions boundary for the user.&lt;br&#x2F;&gt; A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see &#91;Permissions boundaries for IAM entities&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;access_policies_boundaries.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; For more information about policy types, see &#91;Policy types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;access_policies.html#access_policy-types) in the *IAM User Guide*.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
path,
managed_policy_arns,
policies,
user_name,
groups,
arn,
login_profile,
tags,
permissions_boundary
FROM aws.iam.user
WHERE data__Identifier = '<UserName>';
```

## Permissions

To operate on the <code>user</code> resource, the following permissions are required:

### Read
```json
iam:GetUserPolicy,
iam:ListGroupsForUser,
iam:ListAttachedUserPolicies,
iam:ListUserPolicies,
iam:GetUser,
iam:GetLoginProfile
```

### Update
```json
iam:UpdateLoginProfile,
iam:UpdateUser,
iam:PutUserPermissionsBoundary,
iam:AttachUserPolicy,
iam:DeleteUserPolicy,
iam:DeleteUserPermissionsBoundary,
iam:TagUser,
iam:UntagUser,
iam:CreateLoginProfile,
iam:RemoveUserFromGroup,
iam:AddUserToGroup,
iam:PutUserPolicy,
iam:DetachUserPolicy,
iam:GetLoginProfile,
iam:DeleteLoginProfile,
iam:GetUser,
iam:ListUserTags
```

### Delete
```json
iam:DeleteAccessKey,
iam:RemoveUserFromGroup,
iam:DeleteUserPolicy,
iam:DeleteUser,
iam:DetachUserPolicy,
iam:DeleteLoginProfile,
iam:ListAccessKeys,
iam:GetUserPolicy,
iam:ListGroupsForUser,
iam:ListAttachedUserPolicies,
iam:ListUserPolicies,
iam:GetUser,
iam:GetLoginProfile
```

