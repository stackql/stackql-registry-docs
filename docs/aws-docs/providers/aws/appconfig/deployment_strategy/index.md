---
title: deployment_strategy
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_strategy
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>deployment_strategy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_strategy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deployment_strategy</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appconfig.deployment_strategy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>replicate_to</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>growth_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deployment_duration_in_minutes</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>growth_factor</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>final_bake_time_in_minutes</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
replicate_to,
growth_type,
description,
deployment_duration_in_minutes,
growth_factor,
id,
final_bake_time_in_minutes,
tags,
name
FROM aws.appconfig.deployment_strategy
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
