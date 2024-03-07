---
title: user_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - user_policies
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
Retrieves a list of <code>user_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.user_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name of the policy document.</td></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td>The name of the user to associate the policy with.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>user_policies</code> resource, the following permissions are required:

### Create
```json
iam:PutUserPolicy,
iam:GetUserPolicy
```


## Example
```sql
SELECT
region,
policy_name,
user_name
FROM awscc.iam.user_policies

```
