---
title: usage_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_plan
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>usage_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>usage_plan</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.usage_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The provider-assigned unique ID for this managed resource.</td></tr>
<tr><td><code>api_stages</code></td><td><code>array</code></td><td>The API stages to associate with this usage plan.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the usage plan.</td></tr>
<tr><td><code>quota</code></td><td><code>object</code></td><td>Configures the number of requests that users can make within a given interval.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of arbitrary tags (key-value pairs) to associate with the usage plan.</td></tr>
<tr><td><code>throttle</code></td><td><code>object</code></td><td>Configures the overall request rate (average requests per second) and burst capacity.</td></tr>
<tr><td><code>usage_plan_name</code></td><td><code>string</code></td><td>A name for the usage plan.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
api_stages,
description,
quota,
tags,
throttle,
usage_plan_name
FROM aws.apigateway.usage_plan
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
