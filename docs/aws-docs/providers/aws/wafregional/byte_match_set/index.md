---
title: byte_match_set
hide_title: false
hide_table_of_contents: false
keywords:
  - byte_match_set
  - wafregional
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>byte_match_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>byte_match_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>byte_match_set</td></tr>
<tr><td><b>Id</b></td><td><code>aws.wafregional.byte_match_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>byte_match_tuples</code></td><td><code>array</code></td><td></td></tr>
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
byte_match_tuples,
name
FROM aws.wafregional.byte_match_set
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```