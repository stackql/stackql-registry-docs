---
title: macro
hide_title: false
hide_table_of_contents: false
keywords:
  - macro
  - cloudformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>macro</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>macro</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>macro</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.macro</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_role_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
description,
function_name,
log_group_name,
log_role_ar_n,
name
FROM aws.cloudformation.macro
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
