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


Used to retrieve a list of <code>users</code> in a region or to create or delete a <code>users</code> resource, use <code>user</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new IAM user for your AWS-account.&lt;br&#x2F;&gt;  For information about quotas for the number of IAM users you can create, see &#91;IAM and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.users" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td>The name of the user to create. Do not include the path in this value.&lt;br&#x2F;&gt; This parameter allows (per its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The user name must be unique within the account. User names are not distinguished by case. For example, you cannot create users named both "John" and "john".&lt;br&#x2F;&gt; If you don't specify a name, CFN generates a unique physical ID and uses that ID for the user name.&lt;br&#x2F;&gt; If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;using-iam-template.html#using-iam-capabilities).&lt;br&#x2F;&gt;  Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``&#123;"Fn::Join": &#91;"", &#91;&#123;"Ref": "AWS::Region"&#125;, &#123;"Ref": "MyResourceName"&#125;&#93;&#93;&#125;``.</td></tr>
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
user_name
FROM aws.iam.users
;
```

## `INSERT` Example

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
-- user.iql (required properties only)
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
-- user.iql (all properties)
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

## `DELETE` Example

```sql
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

