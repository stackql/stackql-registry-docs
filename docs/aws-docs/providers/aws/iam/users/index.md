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
Retrieves a list of <code>users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new IAM user for your AWS-account.&lt;br&#x2F;&gt;  For information about quotas for the number of IAM users you can create, see &#91;IAM and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.users</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td>The name of the user to create. Do not include the path in this value.&lt;br&#x2F;&gt; This parameter allows (per its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The user name must be unique within the account. User names are not distinguished by case. For example, you cannot create users named both "John" and "john".&lt;br&#x2F;&gt; If you don't specify a name, CFN generates a unique physical ID and uses that ID for the user name.&lt;br&#x2F;&gt; If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;using-iam-template.html#using-iam-capabilities).&lt;br&#x2F;&gt;  Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``&#123;"Fn::Join": &#91;"", &#91;&#123;"Ref": "AWS::Region"&#125;, &#123;"Ref": "MyResourceName"&#125;&#93;&#93;&#125;``.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
user_name
FROM aws.iam.users

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

### List
```json
iam:listUsers
```

