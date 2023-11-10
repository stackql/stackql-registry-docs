---
title: parameter
hide_title: false
hide_table_of_contents: false
keywords:
  - parameter
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>parameter</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>parameter</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.parameter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policies</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>allowed_pattern</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>value</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type,
description,
policies,
allowed_pattern,
tier,
value,
data_type,
id,
tags,
name
FROM aws.ssm.parameter
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
