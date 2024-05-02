---
title: model
hide_title: false
hide_table_of_contents: false
keywords:
  - model
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
Gets an individual <code>model</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::Model`` resource updates data model for a WebSocket API. For more information, see &#91;Model Selection Expressions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.model</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>model_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the model.</td></tr>
<tr><td><code>content_type</code></td><td><code>string</code></td><td>The content-type for the model, for example, "application&#x2F;json".</td></tr>
<tr><td><code>schema</code></td><td><code>object</code></td><td>The schema for the model. For application&#x2F;json models, this should be JSON schema draft 4 model.</td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the model.</td></tr>
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
model_id,
description,
content_type,
schema,
api_id,
name
FROM aws.apigatewayv2.model
WHERE data__Identifier = '<ApiId>|<ModelId>';
```

## Permissions

To operate on the <code>model</code> resource, the following permissions are required:

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

