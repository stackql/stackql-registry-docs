---
title: route
hide_title: false
hide_table_of_contents: false
keywords:
  - route
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
Gets an individual <code>route</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>route</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.route</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>route_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>route_response_selection_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>request_models</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>operation_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorization_scopes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>api_key_required</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>route_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorization_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_selection_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>request_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>target</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorizer_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
route_id,
route_response_selection_expression,
request_models,
operation_name,
authorization_scopes,
api_key_required,
route_key,
authorization_type,
model_selection_expression,
api_id,
request_parameters,
target,
authorizer_id
FROM aws.apigatewayv2.route
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApiId&gt;'
AND data__Identifier = '&lt;RouteId&gt;'
```
