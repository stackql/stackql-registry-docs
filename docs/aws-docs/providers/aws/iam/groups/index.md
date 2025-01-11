---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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

Creates, updates, deletes or gets a <code>group</code> resource or lists <code>groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new group.<br />For information about the number of groups you can create, see &#91;Limitations on Entities&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The name of the group to create. Do not include the path in this value.<br />The group name must be unique within the account. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins". If you don't specify a name, CFN generates a unique physical ID and uses that ID for the group name.<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.<br />If you specify a name, you must specify the <code>CAPABILITY_NAMED_IAM</code> value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities).<br />Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using <code>Fn::Join</code> and <code>AWS::Region</code> to create a Region-specific name, as in the following example: <code>&#123;"Fn::Join": &#91;"", &#91;&#123;"Ref": "AWS::Region"&#125;, &#123;"Ref": "MyResourceName"&#125;&#93;&#93;&#125;</code>.</td></tr>
<tr><td><CopyableCode code="managed_policy_arns" /></td><td><code>array</code></td><td>The Amazon Resource Name (ARN) of the IAM policy you want to attach.<br />For more information about ARNs, see &#91;Amazon Resource Names (ARNs)&#93;(https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td>The path to the group. For more information about paths, see &#91;IAM identifiers&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.<br />This parameter is optional. If it is not included, it defaults to a slash (/).<br />This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>array</code></td><td>Adds or updates an inline policy document that is embedded in the specified IAM group. To view AWS::IAM::Group snippets, see &#91;Declaring an Group Resource&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-group).<br />The name of each inline policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail. <br />For information about limits on the number of inline policies that you can embed in a group, see &#91;Limitations on Entities&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html"><code>AWS::IAM::Group</code></a>.

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
Gets all <code>groups</code> in a region.
```sql
SELECT
region,
arn,
group_name,
managed_policy_arns,
path,
policies
FROM aws.iam.groups
;
```
Gets all properties from an individual <code>group</code>.
```sql
SELECT
region,
arn,
group_name,
managed_policy_arns,
path,
policies
FROM aws.iam.groups
WHERE data__Identifier = '<GroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iam.groups (
 GroupName,
 ManagedPolicyArns,
 Path,
 Policies,
 region
)
SELECT 
'{{ GroupName }}',
 '{{ ManagedPolicyArns }}',
 '{{ Path }}',
 '{{ Policies }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iam.groups (
 GroupName,
 ManagedPolicyArns,
 Path,
 Policies,
 region
)
SELECT 
 '{{ GroupName }}',
 '{{ ManagedPolicyArns }}',
 '{{ Path }}',
 '{{ Policies }}',
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
  - name: group
    props:
      - name: GroupName
        value: '{{ GroupName }}'
      - name: ManagedPolicyArns
        value:
          - '{{ ManagedPolicyArns[0] }}'
      - name: Path
        value: '{{ Path }}'
      - name: Policies
        value:
          - PolicyDocument: {}
            PolicyName: '{{ PolicyName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iam.groups
WHERE data__Identifier = '<GroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>groups</code> resource, the following permissions are required:

### Create
```json
iam:CreateGroup,
iam:PutGroupPolicy,
iam:AttachGroupPolicy,
iam:GetGroupPolicy,
iam:GetGroup
```

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

### List
```json
iam:ListGroups
```
