---
title: route_response
hide_title: false
hide_table_of_contents: false
keywords:
  - route_response
  - apigatewayv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>route_response</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_response</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>route_response</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.route_response</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>route_response_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>route_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_selection_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_models</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
route_response_key,
response_parameters,
route_id,
id,
model_selection_expression,
api_id,
response_models
FROM aws.apigatewayv2.route_response
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
