---
title: gateway_response
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_response
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>gateway_response</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_response</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>gateway_response</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.gateway_response</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>response_type</code></td><td><code>string</code></td><td>The response type of the associated GatewayResponse.</td></tr>
<tr><td><code>status_code</code></td><td><code>string</code></td><td>The HTTP status code for this GatewayResponse.</td></tr>
<tr><td><code>response_parameters</code></td><td><code>object</code></td><td>Response parameters (paths, query strings and headers) of the GatewayResponse as a string-to-string map of key-value pairs.</td></tr>
<tr><td><code>response_templates</code></td><td><code>object</code></td><td>Response templates of the GatewayResponse as a string-to-string map of key-value pairs.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
rest_api_id,
response_type,
status_code,
response_parameters,
response_templates
FROM awscc.apigateway.gateway_response
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>gateway_response</code> resource, the following permissions are required:

### Update
```json
apigateway:GET,
apigateway:PUT
```

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

