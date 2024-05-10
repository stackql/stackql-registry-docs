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


Used to retrieve a list of <code>route_responses</code> in a region or to create or delete a <code>route_responses</code> resource, use <code>route_response</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::RouteResponse`` resource creates a route response for a WebSocket API. For more information, see &#91;Set up Route Responses for a WebSocket API in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;apigateway-websocket-api-route-response.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.route_responses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><CopyableCode code="route_id" /></td><td><code>string</code></td><td>The route ID.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
api_id,
route_id,
route_response_id
FROM aws.apigatewayv2.route_responses
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>route_response</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- route_response.iql (required properties only)
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
-- route_response.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

### List
```json
apigateway:GET
```

