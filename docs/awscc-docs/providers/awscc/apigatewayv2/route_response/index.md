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
<tr><td><b>Id</b></td><td><code>awscc.apigatewayv2.route_response</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>route_response_key</code></td><td><code>string</code></td><td>The route response key.</td></tr>
<tr><td><code>response_parameters</code></td><td><code>undefined</code></td><td>The route response parameters.</td></tr>
<tr><td><code>route_id</code></td><td><code>string</code></td><td>The route ID.</td></tr>
<tr><td><code>model_selection_expression</code></td><td><code>string</code></td><td>The model selection expression for the route response. Supported only for WebSocket APIs.</td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><code>response_models</code></td><td><code>object</code></td><td>The response models for the route response.</td></tr>
<tr><td><code>route_response_id</code></td><td><code>string</code></td><td></td></tr>
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
model_selection_expression,
api_id,
response_models,
route_response_id
FROM awscc.apigatewayv2.route_response
WHERE region = 'us-east-1'
AND data__Identifier = '{ApiId}';
AND data__Identifier = '{RouteId}';
AND data__Identifier = '{RouteResponseId}';
```

## Permissions

To operate on the <code>route_response</code> resource, the following permissions are required:

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT
```

### Read
```json
apigateway:GET
```

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

