---
title: event_invoke_config
hide_title: false
hide_table_of_contents: false
keywords:
  - event_invoke_config
  - lambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>event_invoke_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_invoke_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_invoke_config</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.event_invoke_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>maximum_retry_attempts</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>qualifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>destination_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>maximum_event_age_in_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
function_name,
maximum_retry_attempts,
qualifier,
destination_config,
id,
maximum_event_age_in_seconds
FROM aws.lambda.event_invoke_config
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
