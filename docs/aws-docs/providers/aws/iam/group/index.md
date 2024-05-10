---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
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


Gets or updates an individual <code>group</code> resource, use <code>groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new group.&lt;br&#x2F;&gt;  For information about the number of groups you can create, see &#91;Limitations on Entities&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;LimitationsOnEntities.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The name of the group to create. Do not include the path in this value.&lt;br&#x2F;&gt; The group name must be unique within the account. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins". If you don't specify a name, CFN generates a unique physical ID and uses that ID for the group name.&lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.&lt;br&#x2F;&gt;  If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see &#91;Acknowledging Resources in Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;using-iam-template.html#using-iam-capabilities).&lt;br&#x2F;&gt;  Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``&#123;"Fn::Join": &#91;"", &#91;&#123;"Ref": "AWS::Region"&#125;, &#123;"Ref": "MyResourceName"&#125;&#93;&#93;&#125;``.</td></tr>
<tr><td><CopyableCode code="managed_policy_arns" /></td><td><code>array</code></td><td>The Amazon Resource Name (ARN) of the IAM policy you want to attach.&lt;br&#x2F;&gt; For more information about ARNs, see &#91;Amazon Resource Names (ARNs)&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td>The path to the group. For more information about paths, see &#91;IAM identifiers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;Using_Identifiers.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; This parameter is optional. If it is not included, it defaults to a slash (&#x2F;).&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of either a forward slash (&#x2F;) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (``\u0021``) through the DEL character (``\u007F``), including most punctuation characters, digits, and upper and lowercased letters.</td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>array</code></td><td>Adds or updates an inline policy document that is embedded in the specified IAM group. To view AWS::IAM::Group snippets, see &#91;Declaring an Group Resource&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;quickref-iam.html#scenario-iam-group).&lt;br&#x2F;&gt;  The name of each inline policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail. &lt;br&#x2F;&gt;  For information about limits on the number of inline policies that you can embed in a group, see &#91;Limitations on Entities&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;LimitationsOnEntities.html) in the *User Guide*.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
group_name,
managed_policy_arns,
path,
policies
FROM aws.iam.group
WHERE data__Identifier = '<GroupName>';
```


## Permissions

To operate on the <code>group</code> resource, the following permissions are required:

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

