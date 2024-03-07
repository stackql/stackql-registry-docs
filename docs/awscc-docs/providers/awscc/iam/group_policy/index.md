---
title: group_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - group_policy
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
Gets an individual <code>group_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>group_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.group_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>The policy document.&lt;br&#x2F;&gt; You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.&lt;br&#x2F;&gt; The &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex) used to validate this parameter is a string of characters consisting of the following:&lt;br&#x2F;&gt;  +  Any printable ASCII character ranging from the space character (``\u0020``) through the end of the ASCII character range&lt;br&#x2F;&gt;  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\u00FF``)&lt;br&#x2F;&gt;  +  The special characters tab (``\u0009``), line feed (``\u000A``), and carriage return (``\u000D``)</td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name of the policy document.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><code>group_name</code></td><td><code>string</code></td><td>The name of the group to associate the policy with.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>group_policy</code> resource, the following permissions are required:

### Read
```json
iam:GetGroupPolicy
```

### Update
```json
iam:PutGroupPolicy,
iam:GetGroupPolicy
```

### Delete
```json
iam:DeleteGroupPolicy,
iam:GetGroupPolicy
```


## Example
```sql
SELECT
region,
policy_document,
policy_name,
group_name
FROM awscc.iam.group_policy
WHERE data__Identifier = '&lt;PolicyName&gt;'
AND data__Identifier = '&lt;GroupName&gt;'
```
