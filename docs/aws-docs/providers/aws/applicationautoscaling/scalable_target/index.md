---
title: scalable_target
hide_title: false
hide_table_of_contents: false
keywords:
  - scalable_target
  - applicationautoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>scalable_target</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scalable_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scalable_target</td></tr>
<tr><td><b>Id</b></td><td><code>aws.applicationautoscaling.scalable_target</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scheduled_actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scalable_dimension</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>suspended_state</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>min_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>role_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
scheduled_actions,
resource_id,
service_namespace,
scalable_dimension,
suspended_state,
id,
min_capacity,
role_ar_n,
max_capacity
FROM aws.applicationautoscaling.scalable_target
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
