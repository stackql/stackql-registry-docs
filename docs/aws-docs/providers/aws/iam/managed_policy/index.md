---
title: managed_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_policy
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
Gets an individual <code>managed_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new managed policy for your AWS-account.&lt;br&#x2F;&gt; This operation creates a policy version with a version identifier of ``v1`` and sets v1 as the policy's default version. For more information about policy versions, see &#91;Versioning for managed policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;policies-managed-versions.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; As a best practice, you can validate your IAM policies. To learn more, see &#91;Validating IAM policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;access_policies_policy-validator.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; For more information about managed policies in general, see &#91;Managed policies and inline policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;policies-managed-vs-inline.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.managed_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A friendly description of the policy.&lt;br&#x2F;&gt; Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables."&lt;br&#x2F;&gt; The policy description is immutable. After a value is assigned, it cannot be changed.</td></tr>
<tr><td><code>groups</code></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the group to attach the policy to.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><code>managed_policy_name</code></td><td><code>string</code></td><td>The friendly name of the policy.&lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.&lt;br&#x2F;&gt;  If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;using-iam-template.html#using-iam-capabilities).&lt;br&#x2F;&gt;  Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``&#123;"Fn::Join": &#91;"", &#91;&#123;"Ref": "AWS::Region"&#125;, &#123;"Ref": "MyResourceName"&#125;&#93;&#93;&#125;``.</td></tr>
<tr><td><code>path</code></td><td><code>string</code></td><td>The path for the policy.&lt;br&#x2F;&gt; For more information about paths, see &#91;IAM identifiers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;Using_Identifiers.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; This parameter is optional. If it is not included, it defaults to a slash (&#x2F;).&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of either a forward slash (&#x2F;) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (``\u0021``) through the DEL character (``\u007F``), including most punctuation characters, digits, and upper and lowercased letters.&lt;br&#x2F;&gt;  You cannot use an asterisk (*) in the path name.</td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>The JSON policy document that you want to use as the content for the new policy.&lt;br&#x2F;&gt; You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.&lt;br&#x2F;&gt; The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see &#91;IAM and character quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_iam-quotas.html#reference_iam-quotas-entity-length).&lt;br&#x2F;&gt; To learn more about JSON policy grammar, see &#91;Grammar of the IAM JSON policy language&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_policies_grammar.html) in the *IAM User Guide*. &lt;br&#x2F;&gt; The &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex) used to validate this parameter is a string of characters consisting of the following:&lt;br&#x2F;&gt;  +  Any printable ASCII character ranging from the space character (``\u0020``) through the end of the ASCII character range&lt;br&#x2F;&gt;  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\u00FF``)&lt;br&#x2F;&gt;  +  The special characters tab (``\u0009``), line feed (``\u000A``), and carriage return (``\u000D``)</td></tr>
<tr><td><code>roles</code></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the role to attach the policy to.&lt;br&#x2F;&gt; This parameter allows (per its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-&lt;br&#x2F;&gt;  If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy``) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service``) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that CFN deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.</td></tr>
<tr><td><code>users</code></td><td><code>array</code></td><td>The name (friendly name, not ARN) of the IAM user to attach the policy to.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><code>policy_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attachment_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>create_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>update_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_version_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>is_attachable</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>permissions_boundary_usage_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>policy_id</code></td><td><code>string</code></td><td></td></tr>
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
FROM aws.iam.managed_policy
WHERE data__Identifier = '<PolicyArn>';
```

## Permissions

To operate on the <code>managed_policy</code> resource, the following permissions are required:

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

