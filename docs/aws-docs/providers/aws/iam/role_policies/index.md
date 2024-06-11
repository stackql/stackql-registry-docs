---
title: role_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - role_policies
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

Creates, updates, deletes or gets a <code>role_policy</code> resource or lists <code>role_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Adds or updates an inline policy document that is embedded in the specified IAM role.<br/> When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role, using &#91;CreateRole&#93;(https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html). You can update a role's trust policy using &#91;UpdateAssumeRolePolicy&#93;(https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAssumeRolePolicy.html). For information about roles, see &#91;roles&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html) in the *IAM User Guide*.<br/> A role can also have a managed policy attached to it. To attach a managed policy to a role, use &#91;AWS::IAM::Role&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html). To create a new managed policy, use &#91;AWS::IAM::ManagedPolicy&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html). For information about policies, see &#91;Managed policies and inline policies&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.<br/> For information about the maximum number of inline policies that you can embed with a role, see &#91;IAM and quotas&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.role_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>The policy document.<br/> You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.<br/> The &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:<br/>  +  Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range<br/>  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)<br/>  +  The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the policy document.<br/> This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>The name of the role to associate the policy with.<br/> This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="PolicyName, RoleName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="undefined" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>role_policy</code>.
```sql
SELECT
region,
policy_document,
policy_name,
role_name
FROM aws.iam.role_policies
WHERE data__Identifier = '<PolicyName>|<RoleName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iam.role_policies (
 PolicyName,
 RoleName,
 region
)
SELECT 
'{{ PolicyName }}',
 '{{ RoleName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iam.role_policies (
 PolicyDocument,
 PolicyName,
 RoleName,
 region
)
SELECT 
 '{{ PolicyDocument }}',
 '{{ PolicyName }}',
 '{{ RoleName }}',
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
  - name: role_policy
    props:
      - name: PolicyDocument
        value: {}
      - name: PolicyName
        value: '{{ PolicyName }}'
      - name: RoleName
        value: '{{ RoleName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iam.role_policies
WHERE data__Identifier = '<PolicyName|RoleName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>role_policies</code> resource, the following permissions are required:

### Create
```json
iam:PutRolePolicy,
iam:GetRolePolicy
```

### Read
```json
iam:GetRolePolicy
```

### Update
```json
iam:PutRolePolicy,
iam:GetRolePolicy
```

### Delete
```json
iam:DeleteRolePolicy,
iam:GetRolePolicy
```

