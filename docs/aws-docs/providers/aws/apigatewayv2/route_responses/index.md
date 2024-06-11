---
title: route_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - route_responses
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>route_response</code> resource or lists <code>route_responses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::RouteResponse</code> resource creates a route response for a WebSocket API. For more information, see &#91;Set up Route Responses for a WebSocket API in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-response.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.route_responses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="route_response_key" /></td><td><code>string</code></td><td>The route response key.</td></tr>
<tr><td><CopyableCode code="response_parameters" /></td><td><code>undefined</code></td><td>The route response parameters.</td></tr>
<tr><td><CopyableCode code="route_id" /></td><td><code>string</code></td><td>The route ID.</td></tr>
<tr><td><CopyableCode code="model_selection_expression" /></td><td><code>string</code></td><td>The model selection expression for the route response. Supported only for WebSocket APIs.</td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><CopyableCode code="response_models" /></td><td><code>object</code></td><td>The response models for the route response.</td></tr>
<tr><td><CopyableCode code="route_response_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="RouteResponseKey, RouteId, ApiId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>route_responses</code> in a region.
```sql
SELECT
region,
api_id,
route_id,
route_response_id
FROM aws.apigatewayv2.route_responses
WHERE region = 'us-east-1';
```
Gets all properties from a <code>route_response</code>.
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
FROM aws.apigatewayv2.route_responses
WHERE region = 'us-east-1' AND data__Identifier = '<ApiId>|<RouteId>|<RouteResponseId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>route_response</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.apigatewayv2.route_responses (
 RouteResponseKey,
 RouteId,
 ApiId,
 region
)
SELECT 
'{{ RouteResponseKey }}',
 '{{ RouteId }}',
 '{{ ApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigatewayv2.route_responses (
 RouteResponseKey,
 ResponseParameters,
 RouteId,
 ModelSelectionExpression,
 ApiId,
 ResponseModels,
 region
)
SELECT 
 '{{ RouteResponseKey }}',
 '{{ ResponseParameters }}',
 '{{ RouteId }}',
 '{{ ModelSelectionExpression }}',
 '{{ ApiId }}',
 '{{ ResponseModels }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: route_response
    props:
      - name: RouteResponseKey
        value: '{{ RouteResponseKey }}'
      - name: ResponseParameters
        value: null
      - name: RouteId
        value: '{{ RouteId }}'
      - name: ModelSelectionExpression
        value: '{{ ModelSelectionExpression }}'
      - name: ApiId
        value: '{{ ApiId }}'
      - name: ResponseModels
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigatewayv2.route_responses
WHERE data__Identifier = '<ApiId|RouteId|RouteResponseId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>route_responses</code> resource, the following permissions are required:

### Create
```json
apigateway:POST
```

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

### List
```json
apigateway:GET
```

