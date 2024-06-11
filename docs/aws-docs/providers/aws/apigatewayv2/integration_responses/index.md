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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>integration_response</code> resource or lists <code>integration_responses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::IntegrationResponse</code> resource updates an integration response for an WebSocket API. For more information, see &#91;Set up WebSocket API Integration Responses in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-responses.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.integration_responses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="integration_response_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="response_templates" /></td><td><code>object</code></td><td>The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.</td></tr>
<tr><td><CopyableCode code="template_selection_expression" /></td><td><code>string</code></td><td>The template selection expression for the integration response. Supported only for WebSocket APIs.</td></tr>
<tr><td><CopyableCode code="response_parameters" /></td><td><code>object</code></td><td>A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of <code>method.response.header.&#123;name&#125;</code>, where name is a valid and unique header name. The mapped non-static value must match the pattern of <code>integration.response.header.&#123;name&#125;</code> or <code>integration.response.body.&#123;JSON-expression&#125;</code>, where <code>&#123;name&#125;</code> is a valid and unique response header name and <code>&#123;JSON-expression&#125;</code> is a valid JSON expression without the <code>$</code> prefix.</td></tr>
<tr><td><CopyableCode code="content_handling_strategy" /></td><td><code>string</code></td><td>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are <code>CONVERT_TO_BINARY</code> and <code>CONVERT_TO_TEXT</code>, with the following behaviors:<br/>  <code>CONVERT_TO_BINARY</code>: Converts a response payload from a Base64-encoded string to the corresponding binary blob.<br/>  <code>CONVERT_TO_TEXT</code>: Converts a response payload from a binary blob to a Base64-encoded string.<br/> If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</td></tr>
<tr><td><CopyableCode code="integration_id" /></td><td><code>string</code></td><td>The integration ID.</td></tr>
<tr><td><CopyableCode code="integration_response_key" /></td><td><code>string</code></td><td>The integration response key.</td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The API identifier.</td></tr>
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
    <td><CopyableCode code="ApiId, IntegrationId, IntegrationResponseKey, region" /></td>
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
List all <code>integration_responses</code> in a region.
```sql
SELECT
region,
api_id,
integration_id,
integration_response_id
FROM aws.apigatewayv2.integration_responses
WHERE region = 'us-east-1';
```
Gets all properties from an <code>integration_response</code>.
```sql
SELECT
region,
integration_response_id,
response_templates,
template_selection_expression,
response_parameters,
content_handling_strategy,
integration_id,
integration_response_key,
api_id
FROM aws.apigatewayv2.integration_responses
WHERE region = 'us-east-1' AND data__Identifier = '<ApiId>|<IntegrationId>|<IntegrationResponseId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_response</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigatewayv2.integration_responses (
 IntegrationId,
 IntegrationResponseKey,
 ApiId,
 region
)
SELECT 
'{{ IntegrationId }}',
 '{{ IntegrationResponseKey }}',
 '{{ ApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigatewayv2.integration_responses (
 ResponseTemplates,
 TemplateSelectionExpression,
 ResponseParameters,
 ContentHandlingStrategy,
 IntegrationId,
 IntegrationResponseKey,
 ApiId,
 region
)
SELECT 
 '{{ ResponseTemplates }}',
 '{{ TemplateSelectionExpression }}',
 '{{ ResponseParameters }}',
 '{{ ContentHandlingStrategy }}',
 '{{ IntegrationId }}',
 '{{ IntegrationResponseKey }}',
 '{{ ApiId }}',
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
  - name: integration_response
    props:
      - name: ResponseTemplates
        value: {}
      - name: TemplateSelectionExpression
        value: '{{ TemplateSelectionExpression }}'
      - name: ResponseParameters
        value: {}
      - name: ContentHandlingStrategy
        value: '{{ ContentHandlingStrategy }}'
      - name: IntegrationId
        value: '{{ IntegrationId }}'
      - name: IntegrationResponseKey
        value: '{{ IntegrationResponseKey }}'
      - name: ApiId
        value: '{{ ApiId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigatewayv2.integration_responses
WHERE data__Identifier = '<ApiId|IntegrationId|IntegrationResponseId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>integration_responses</code> resource, the following permissions are required:

### Create
```json
apigateway:POST
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:PATCH,
apigateway:PUT,
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

