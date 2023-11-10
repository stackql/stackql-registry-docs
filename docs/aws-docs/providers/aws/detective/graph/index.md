---
title: graph
hide_title: false
hide_table_of_contents: false
keywords:
  - graph
  - detective
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>graph</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>graph</td></tr>
<tr><td><b>Id</b></td><td><code>aws.detective.graph</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Detective graph ARN</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
tags
FROM aws.detective.graph
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
