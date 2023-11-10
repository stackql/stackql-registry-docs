---
title: trigger
hide_title: false
hide_table_of_contents: false
keywords:
  - trigger
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
Gets an individual <code>trigger</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trigger</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>trigger</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.trigger</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>start_on_creation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>event_batching_condition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>workflow_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>predicate</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type,
start_on_creation,
description,
actions,
event_batching_condition,
workflow_name,
schedule,
id,
tags,
name,
predicate
FROM aws.glue.trigger
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
