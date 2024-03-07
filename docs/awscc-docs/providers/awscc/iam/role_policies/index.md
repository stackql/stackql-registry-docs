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
Retrieves a list of <code>role_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>role_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.role_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name of the policy document.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><code>role_name</code></td><td><code>string</code></td><td>The name of the role to associate the policy with.&lt;br&#x2F;&gt; This parameter allows (through its &#91;regex pattern&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;http:&#x2F;&#x2F;wikipedia.org&#x2F;wiki&#x2F;regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
policy_name,
role_name
FROM awscc.iam.role_policies

```

## Permissions

To operate on the <code>role_policies</code> resource, the following permissions are required:

### Create
```json
iam:PutRolePolicy,
iam:GetRolePolicy
```

