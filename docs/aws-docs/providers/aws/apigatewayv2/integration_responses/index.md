---
title: integration_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_responses
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
Retrieves a list of <code>integration_responses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::IntegrationResponse`` resource updates an integration response for an WebSocket API. For more information, see &#91;Set up WebSocket API Integration Responses in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;apigateway-websocket-api-integration-responses.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.integration_responses</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><code>integration_id</code></td><td><code>string</code></td><td>The integration ID.</td></tr>
<tr><td><code>integration_response_id</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
api_id,
integration_id,
integration_response_id
FROM aws.apigatewayv2.integration_responses
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>integration_responses</code> resource, the following permissions are required:

### Create
```json
apigateway:POST
```

### List
```json
apigateway:GET
```

