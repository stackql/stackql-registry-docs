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
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::RouteResponse`` resource creates a route response for a WebSocket API. For more information, see &#91;Set up Route Responses for a WebSocket API in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;apigateway-websocket-api-route-response.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.route_response</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.apigatewayv2.route_response
WHERE data__Identifier = '<ApiId>|<RouteId>|<RouteResponseId>';
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

