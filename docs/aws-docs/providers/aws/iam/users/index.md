---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes or gets a <code>user</code> resource or lists <code>users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new IAM user for your AWS-account.<br/>  For information about quotas for the number of IAM users you can create, see &#91;IAM and quotas&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.users" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td>The path for the user name. For more information about paths, see &#91;IAM identifiers&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.<br/> This parameter is optional. If it is not included, it defaults to a slash (/).<br/> This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</td></tr>
<tr><td><CopyableCode code="managed_policy_arns" /></td><td><code>array</code></td><td>A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the user.<br/> For more information about ARNs, see &#91;Amazon Resource Names (ARNs) and Service Namespaces&#93;(https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>array</code></td><td>Adds or updates an inline policy document that is embedded in the specified IAM user. To view AWS::IAM::User snippets, see &#91;Declaring an User Resource&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-user).<br/>  The name of each policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail. <br/>  For information about limits on the number of inline policies that you can embed in a user, see &#91;Limitations on Entities&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td>The name of the user to create. Do not include the path in this value.<br/> This parameter allows (per its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The user name must be unique within the account. User names are not distinguished by case. For example, you cannot create users named both "John" and "john".<br/> If you don't specify a name, CFN generates a unique physical ID and uses that ID for the user name.<br/> If you specify a name, you must specify the <code>CAPABILITY_NAMED_IAM</code> value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities).<br/>  Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using <code>Fn::Join</code> and <code>AWS::Region</code> to create a Region-specific name, as in the following example: <code>&#123;"Fn::Join": &#91;"", &#91;&#123;"Ref": "AWS::Region"&#125;, &#123;"Ref": "MyResourceName"&#125;&#93;&#93;&#125;</code>.</td></tr>
<tr><td><CopyableCode code="groups" /></td><td><code>array</code></td><td>A list of group names to which you want to add the user.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="login_profile" /></td><td><code>object</code></td><td>Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the console.<br/> You can use the CLI, the AWS API, or the *Users* page in the IAM console to create a password for any IAM user. Use &#91;ChangePassword&#93;(https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html) to update your own existing password in the *My Security Credentials* page in the console.<br/> For more information about managing passwords, see &#91;Managing passwords&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags that you want to attach to the new user. Each tag consists of a key name and an associated value. For more information about tagging, see &#91;Tagging IAM resources&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.<br/>  If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.</td></tr>
<tr><td><CopyableCode code="permissions_boundary" /></td><td><code>string</code></td><td>The ARN of the managed policy that is used to set the permissions boundary for the user.<br/> A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see &#91;Permissions boundaries for IAM entities&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.<br/> For more information about policy types, see &#91;Policy types&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types) in the *IAM User Guide*.</td></tr>
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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>users</code> in a region.
```sql
SELECT
region,
user_name
FROM aws.iam.users
;
```
Gets all properties from a <code>user</code>.
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
FROM aws.iam.users
WHERE data__Identifier = '<UserName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.iam.users (
 Path,
 ManagedPolicyArns,
 Policies,
 UserName,
 Groups,
 LoginProfile,
 Tags,
 PermissionsBoundary,
 region
)
SELECT 
'{{ Path }}',
 '{{ ManagedPolicyArns }}',
 '{{ Policies }}',
 '{{ UserName }}',
 '{{ Groups }}',
 '{{ LoginProfile }}',
 '{{ Tags }}',
 '{{ PermissionsBoundary }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iam.users (
 Path,
 ManagedPolicyArns,
 Policies,
 UserName,
 Groups,
 LoginProfile,
 Tags,
 PermissionsBoundary,
 region
)
SELECT 
 '{{ Path }}',
 '{{ ManagedPolicyArns }}',
 '{{ Policies }}',
 '{{ UserName }}',
 '{{ Groups }}',
 '{{ LoginProfile }}',
 '{{ Tags }}',
 '{{ PermissionsBoundary }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: user
    props:
      - name: Path
        value: '{{ Path }}'
      - name: ManagedPolicyArns
        value:
          - '{{ ManagedPolicyArns[0] }}'
      - name: Policies
        value:
          - PolicyDocument: {}
            PolicyName: '{{ PolicyName }}'
      - name: UserName
        value: '{{ UserName }}'
      - name: Groups
        value:
          - '{{ Groups[0] }}'
      - name: LoginProfile
        value:
          PasswordResetRequired: '{{ PasswordResetRequired }}'
          Password: '{{ Password }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: PermissionsBoundary
        value: '{{ PermissionsBoundary }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iam.users
WHERE data__Identifier = '<UserName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>users</code> resource, the following permissions are required:

### Create
```json
iam:CreateLoginProfile,
iam:AddUserToGroup,
iam:PutUserPolicy,
iam:AttachUserPolicy,
iam:CreateUser,
iam:GetUser,
iam:TagUser
```

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

### List
```json
iam:listUsers
```

