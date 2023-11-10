---
title: profile
hide_title: false
hide_table_of_contents: false
keywords:
  - profile
  - rolesanywhere
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>profile</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rolesanywhere.profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>duration_seconds</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>managed_policy_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>profile_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>profile_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>require_instance_properties</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>role_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>session_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
duration_seconds,
enabled,
managed_policy_arns,
name,
profile_arn,
profile_id,
require_instance_properties,
role_arns,
session_policy,
tags
FROM aws.rolesanywhere.profile
WHERE region = 'us-east-1'
AND data__Identifier = '<ProfileId>'
```
