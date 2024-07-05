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

Creates, updates, deletes or gets a <code>role</code> resource or lists <code>roles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new role for your AWS-account.<br />For more information about roles, see &#91;IAM roles&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide*. For information about quotas for role names and the number of roles you can create, see &#91;IAM and quotas&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.roles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assume_role_policy_document" /></td><td><code>object</code></td><td>The trust policy that is associated with this role. Trust policies define which entities can assume the role. You can associate only one trust policy with a role. For an example of a policy that can be used to assume a role, see &#91;Template Examples&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#aws-resource-iam-role--examples). For more information about the elements that you can use in an IAM policy, see &#91;Policy Elements Reference&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the role that you provide.</td></tr>
<tr><td><CopyableCode code="managed_policy_arns" /></td><td><code>array</code></td><td>A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.<br />For more information about ARNs, see &#91;Amazon Resource Names (ARNs) and Service Namespaces&#93;(https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><CopyableCode code="max_session_duration" /></td><td><code>integer</code></td><td>The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default value of one hour is applied. This setting can have a value from 1 hour to 12 hours.<br />Anyone who assumes the role from the CLI or API can use the <code>DurationSeconds</code> API parameter or the <code>duration-seconds</code> CLI parameter to request a longer session. The <code>MaxSessionDuration</code> setting determines the maximum duration that can be requested using the <code>DurationSeconds</code> parameter. If users don't specify a value for the <code>DurationSeconds</code> parameter, their security credentials are valid for one hour by default. This applies when you use the <code>AssumeRole*</code> API operations or the <code>assume-role*</code> CLI operations but does not apply when you use those operations to create a console URL. For more information, see &#91;Using IAM roles&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) in the *IAM User Guide*.</td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td>The path to the role. For more information about paths, see &#91;IAM Identifiers&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.<br />This parameter is optional. If it is not included, it defaults to a slash (/).<br />This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</td></tr>
<tr><td><CopyableCode code="permissions_boundary" /></td><td><code>string</code></td><td>The ARN of the policy used to set the permissions boundary for the role.<br />For more information about permissions boundaries, see &#91;Permissions boundaries for IAM identities&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.</td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>array</code></td><td>Adds or updates an inline policy document that is embedded in the specified IAM role.<br />When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role. You can update a role's trust policy later. For more information about IAM roles, go to &#91;Using Roles to Delegate Permissions and Federate Identities&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html).<br />A role can also have an attached managed policy. For information about policies, see &#91;Managed Policies and Inline Policies&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *User Guide*.<br />For information about limits on the number of inline policies that you can embed with a role, see &#91;Limitations on Entities&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html) in the *User Guide*.<br />If an external policy (such as <code>AWS::IAM::Policy</code> or</td></tr>
<tr><td><CopyableCode code="role_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>A name for the IAM role, up to 64 characters in length. For valid values, see the <code>RoleName</code> parameter for the &#91;CreateRole&#93;(https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html) action in the *User Guide*.<br />This parameter allows (per its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The role name must be unique within the account. Role names are not distinguished by case. For example, you cannot create roles named both "Role1" and "role1".<br />If you don't specify a name, CFN generates a unique physical ID and uses that ID for the role name.<br />If you specify a name, you must specify the <code>CAPABILITY_NAMED_IAM</code> value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/Use</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags that are attached to the role. For more information about tagging, see &#91;Tagging IAM resources&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.</td></tr>
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
    <td><CopyableCode code="AssumeRolePolicyDocument, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>roles</code> in a region.
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
FROM aws.iam.roles
;
```
Gets all properties from an individual <code>role</code>.
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
FROM aws.iam.roles
WHERE data__Identifier = '<RoleName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iam.roles (
 AssumeRolePolicyDocument,
 region
)
SELECT 
'{{ AssumeRolePolicyDocument }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ AssumeRolePolicyDocument }}',
 '{{ Description }}',
 '{{ ManagedPolicyArns }}',
 '{{ MaxSessionDuration }}',
 '{{ Path }}',
 '{{ PermissionsBoundary }}',
 '{{ Policies }}',
 '{{ RoleName }}',
 '{{ Tags }}',
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
  - name: role
    props:
      - name: AssumeRolePolicyDocument
        value: {}
      - name: Description
        value: '{{ Description }}'
      - name: ManagedPolicyArns
        value:
          - '{{ ManagedPolicyArns[0] }}'
      - name: MaxSessionDuration
        value: '{{ MaxSessionDuration }}'
      - name: Path
        value: '{{ Path }}'
      - name: PermissionsBoundary
        value: '{{ PermissionsBoundary }}'
      - name: Policies
        value:
          - PolicyDocument: {}
            PolicyName: '{{ PolicyName }}'
      - name: RoleName
        value: '{{ RoleName }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### List
```json
iam:ListRoles
```

