---
title: managed_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_policies
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

Creates, updates, deletes or gets a <code>managed_policy</code> resource or lists <code>managed_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new managed policy for your AWS-account.<br/> This operation creates a policy version with a version identifier of <code>v1</code> and sets v1 as the policy's default version. For more information about policy versions, see &#91;Versioning for managed policies&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html) in the *IAM User Guide*.<br/> As a best practice, you can validate your IAM policies. To learn more, see &#91;Validating IAM policies&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html) in the *IAM User Guide*.<br/> For more information about managed policies in general, see &#91;Managed policies and inline policies&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.managed_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A friendly description of the policy.<br/> Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables."<br/> The policy description is immutable. After a value is assigned, it cannot be changed.</td></tr>
<tr><td><CopyableCode code="groups" /></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the group to attach the policy to.<br/> This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><CopyableCode code="managed_policy_name" /></td><td><code>string</code></td><td>The friendly name of the policy.<br/>  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.<br/>  If you specify a name, you must specify the <code>CAPABILITY_NAMED_IAM</code> value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities).<br/>  Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using <code>Fn::Join</code> and <code>AWS::Region</code> to create a Region-specific name, as in the following example: <code>&#123;"Fn::Join": &#91;"", &#91;&#123;"Ref": "AWS::Region"&#125;, &#123;"Ref": "MyResourceName"&#125;&#93;&#93;&#125;</code>.</td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td>The path for the policy.<br/> For more information about paths, see &#91;IAM identifiers&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.<br/> This parameter is optional. If it is not included, it defaults to a slash (/).<br/> This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.<br/>  You cannot use an asterisk (*) in the path name.</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>The JSON policy document that you want to use as the content for the new policy.<br/> You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.<br/> The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see &#91;IAM and character quotas&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length).<br/> To learn more about JSON policy grammar, see &#91;Grammar of the IAM JSON policy language&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html) in the *IAM User Guide*. <br/> The &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:<br/>  +  Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range<br/>  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)<br/>  +  The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</td></tr>
<tr><td><CopyableCode code="roles" /></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the role to attach the policy to.<br/> This parameter allows (per its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-<br/>  If an external policy (such as <code>AWS::IAM::Policy</code> or <code>AWS::IAM::ManagedPolicy</code>) has a <code>Ref</code> to a role and if a resource (such as <code>AWS::ECS::Service</code>) also has a <code>Ref</code> to the same role, add a <code>DependsOn</code> attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an <code>AWS::ECS::Service</code> resource, the <code>DependsOn</code> attribute ensures that CFN deletes the <code>AWS::ECS::Service</code> resource before deleting its role's policy.</td></tr>
<tr><td><CopyableCode code="users" /></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the IAM user to attach the policy to.<br/> This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><CopyableCode code="policy_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attachment_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="create_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="update_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_version_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="is_attachable" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions_boundary_usage_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="PolicyDocument, region" /></td>
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
List all <code>managed_policies</code> in a region.
```sql
SELECT
region,
policy_arn
FROM aws.iam.managed_policies
;
```
Gets all properties from a <code>managed_policy</code>.
```sql
SELECT
region,
description,
groups,
managed_policy_name,
path,
policy_document,
roles,
users,
policy_arn,
attachment_count,
create_date,
update_date,
default_version_id,
is_attachable,
permissions_boundary_usage_count,
policy_id
FROM aws.iam.managed_policies
WHERE data__Identifier = '<PolicyArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iam.managed_policies (
 PolicyDocument,
 region
)
SELECT 
'{{ PolicyDocument }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iam.managed_policies (
 Description,
 Groups,
 ManagedPolicyName,
 Path,
 PolicyDocument,
 Roles,
 Users,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Groups }}',
 '{{ ManagedPolicyName }}',
 '{{ Path }}',
 '{{ PolicyDocument }}',
 '{{ Roles }}',
 '{{ Users }}',
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
  - name: managed_policy
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Groups
        value:
          - '{{ Groups[0] }}'
      - name: ManagedPolicyName
        value: '{{ ManagedPolicyName }}'
      - name: Path
        value: '{{ Path }}'
      - name: PolicyDocument
        value: {}
      - name: Roles
        value:
          - '{{ Roles[0] }}'
      - name: Users
        value:
          - '{{ Users[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iam.managed_policies
WHERE data__Identifier = '<PolicyArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>managed_policies</code> resource, the following permissions are required:

### Create
```json
iam:CreatePolicy,
iam:AttachGroupPolicy,
iam:AttachUserPolicy,
iam:AttachRolePolicy
```

### Read
```json
iam:GetPolicy,
iam:ListEntitiesForPolicy,
iam:GetPolicyVersion
```

### Update
```json
iam:DetachRolePolicy,
iam:GetPolicy,
iam:ListPolicyVersions,
iam:DetachGroupPolicy,
iam:DetachUserPolicy,
iam:CreatePolicyVersion,
iam:DeletePolicyVersion,
iam:AttachGroupPolicy,
iam:AttachUserPolicy,
iam:AttachRolePolicy
```

### Delete
```json
iam:DetachRolePolicy,
iam:GetPolicy,
iam:ListPolicyVersions,
iam:DetachGroupPolicy,
iam:DetachUserPolicy,
iam:DeletePolicyVersion,
iam:DeletePolicy,
iam:ListEntitiesForPolicy
```

### List
```json
iam:ListPolicies
```

