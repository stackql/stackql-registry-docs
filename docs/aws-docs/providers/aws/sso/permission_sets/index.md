---
title: permission_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_sets
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
Retrieves a list of <code>permission_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>permission_sets</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sso.permission_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The sso instance arn that the permission set is owned.</td></tr>
<tr><td><code>permission_set_arn</code></td><td><code>string</code></td><td>The permission set that the policy will be attached to</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn,
permission_set_arn
FROM aws.sso.permission_sets
WHERE region = 'us-east-1'
```
