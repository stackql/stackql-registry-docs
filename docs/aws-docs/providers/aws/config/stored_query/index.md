---
title: stored_query
hide_title: false
hide_table_of_contents: false
keywords:
  - stored_query
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>stored_query</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stored_query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stored_query</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.stored_query</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>query_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>query_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>query_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>query_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>query_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the stored query.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
query_arn,
query_id,
query_name,
query_description,
query_expression,
tags
FROM aws.config.stored_query
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;QueryName&gt;'
```
