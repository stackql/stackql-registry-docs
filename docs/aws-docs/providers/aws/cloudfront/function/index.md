---
title: function
hide_title: false
hide_table_of_contents: false
keywords:
  - function
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>function</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>function</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>function</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudfront.function</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_publish</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>function_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>function_code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>function_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>function_metadata</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stage</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
auto_publish,
function_ar_n,
function_code,
function_config,
function_metadata,
name,
stage
FROM aws.cloudfront.function
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;FunctionARN&gt;'
```
