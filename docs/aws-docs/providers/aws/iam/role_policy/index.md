---
title: role_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - role_policy
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


Gets or updates an individual <code>role_policy</code> resource, use <code>role_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Adds or updates an inline policy document that is embedded in the specified IAM role.&lt;br&#x2F;&gt; When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role, using &#91;CreateRole&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;APIReference&#x2F;API_CreateRole.html). You can update a role's trust policy using &#91;UpdateAssumeRolePolicy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;APIReference&#x2F;API_UpdateAssumeRolePolicy.html). For information about roles, see &#91;roles&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;roles-toplevel.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; A role can also have a managed policy attached to it. To attach a managed policy to a role, use &#91;AWS::IAM::Role&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-iam-role.html). To create a new managed policy, use &#91;AWS::IAM::ManagedPolicy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-iam-managedpolicy.html). For information about policies, see &#91;Managed policies and inline policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;policies-managed-vs-inline.html) in the *IAM User Guide*.&lt;br&#x2F;&gt; For information about the maximum number of inline policies that you can embed with a role, see &#91;IAM and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_iam-quotas.html) in the *IAM User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.role_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>The policy document.&lt;br&#x2F;&gt; You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.&lt;br&#x2F;&gt; The &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex) used to validate this parameter is a string of characters consisting of the following:&lt;br&#x2F;&gt;  +  Any printable ASCII character ranging from the space character (``\u0020``) through the end of the ASCII character range&lt;br&#x2F;&gt;  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\u00FF``)&lt;br&#x2F;&gt;  +  The special characters tab (``\u0009``), line feed (``\u000A``), and carriage return (``\u000D``)</td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the policy document.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>The name of the role to associate the policy with.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
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
policy_document,
policy_name,
role_name
FROM aws.iam.role_policy
WHERE data__Identifier = '<PolicyName>|<RoleName>';
```


## Permissions

To operate on the <code>role_policy</code> resource, the following permissions are required:

### Read
```json
iam:GetRolePolicy
```

### Update
```json
iam:PutRolePolicy,
iam:GetRolePolicy
```

