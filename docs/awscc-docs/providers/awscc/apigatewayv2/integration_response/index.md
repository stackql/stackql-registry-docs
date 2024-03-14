---
title: integration_response
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_response
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
Gets an individual <code>integration_response</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_response</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integration_response</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigatewayv2.integration_response</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>integration_response_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_templates</code></td><td><code>object</code></td><td>The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key&#x2F;value map, with a content-type as the key and a template as the value.</td></tr>
<tr><td><code>template_selection_expression</code></td><td><code>string</code></td><td>The template selection expression for the integration response. Supported only for WebSocket APIs.</td></tr>
<tr><td><code>response_parameters</code></td><td><code>object</code></td><td>A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.&#123;name&#125;``, where name is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.&#123;name&#125;`` or ``integration.response.body.&#123;JSON-expression&#125;``, where ``&#123;name&#125;`` is a valid and unique response header name and ``&#123;JSON-expression&#125;`` is a valid JSON expression without the ``$`` prefix.</td></tr>
<tr><td><code>content_handling_strategy</code></td><td><code>string</code></td><td>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT``, with the following behaviors:&lt;br&#x2F;&gt;  ``CONVERT_TO_BINARY``: Converts a response payload from a Base64-encoded string to the corresponding binary blob.&lt;br&#x2F;&gt;  ``CONVERT_TO_TEXT``: Converts a response payload from a binary blob to a Base64-encoded string.&lt;br&#x2F;&gt; If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</td></tr>
<tr><td><code>integration_id</code></td><td><code>string</code></td><td>The integration ID.</td></tr>
<tr><td><code>integration_response_key</code></td><td><code>string</code></td><td>The integration response key.</td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.apigatewayv2.integration_response
WHERE data__Identifier = '<ApiId>|<IntegrationId>|<IntegrationResponseId>';
```

## Permissions

To operate on the <code>integration_response</code> resource, the following permissions are required:

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

