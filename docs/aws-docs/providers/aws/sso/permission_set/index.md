---
title: permission_set
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_set
  - sso
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>permission_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>permission_set</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sso.permission_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name you want to assign to this permission set.</td></tr>
<tr><td><code>permission_set_arn</code></td><td><code>string</code></td><td>The permission set that the policy will be attached to</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The permission set description.</td></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The sso instance arn that the permission set is owned.</td></tr>
<tr><td><code>session_duration</code></td><td><code>string</code></td><td>The length of time that a user can be signed in to an AWS account.</td></tr>
<tr><td><code>relay_state_type</code></td><td><code>string</code></td><td>The relay state URL that redirect links to any service in the AWS Management Console.</td></tr>
<tr><td><code>managed_policies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>inline_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>customer_managed_policy_references</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>permissions_boundary</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
permission_set_arn,
description,
instance_arn,
session_duration,
relay_state_type,
managed_policies,
inline_policy,
tags,
customer_managed_policy_references,
permissions_boundary
FROM aws.sso.permission_set
WHERE region = 'us-east-1'
AND data__Identifier = '<InstanceArn>'
AND data__Identifier = '<PermissionSetArn>'
```
