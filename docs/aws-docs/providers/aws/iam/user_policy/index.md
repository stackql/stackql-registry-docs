---
title: user_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - user_policy
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
Gets or operates on an individual <code>user_policy</code> resource, use <code>user_policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Adds or updates an inline policy document that is embedded in the specified IAM user.&lt;br&#x2F;&gt; An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use &#91;AWS::IAM::User&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-iam-user.html). To create a new managed policy, use &#91;AWS::IAM::ManagedPolicy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-iam-managedpolicy.html). For information about policies, see &#91;Managed policies and inline policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;policies-managed-vs-inline.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; For information about the maximum number of inline policies that you can embed in a user, see &#91;IAM and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.user_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>The policy document.&lt;br&#x2F;&gt; You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.&lt;br&#x2F;&gt; The &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex) used to validate this parameter is a string of characters consisting of the following:&lt;br&#x2F;&gt;  +  Any printable ASCII character ranging from the space character (``\u0020``) through the end of the ASCII character range&lt;br&#x2F;&gt;  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\u00FF``)&lt;br&#x2F;&gt;  +  The special characters tab (``\u0009``), line feed (``\u000A``), and carriage return (``\u000D``)</td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name of the policy document.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td>The name of the user to associate the policy with.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
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
policy_document,
policy_name,
user_name
FROM aws.iam.user_policy
WHERE data__Identifier = '<PolicyName>|<UserName>';
```

## Permissions

To operate on the <code>user_policy</code> resource, the following permissions are required:

### Read
```json
iam:GetUserPolicy
```

### Update
```json
iam:PutUserPolicy,
iam:GetUserPolicy
```

### Delete
```json
iam:DeleteUserPolicy,
iam:GetUserPolicy
```

