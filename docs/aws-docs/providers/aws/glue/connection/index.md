---
title: connection
hide_title: false
hide_table_of_contents: false
keywords:
  - connection
  - glue
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>connection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connection</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connection_input</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>catalog_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
connection_input,
catalog_id,
id
FROM aws.glue.connection
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
