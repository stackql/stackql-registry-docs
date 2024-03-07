---
title: api
hide_title: false
hide_table_of_contents: false
keywords:
  - api
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
Gets an individual <code>api</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>api</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigatewayv2.api</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>route_selection_expression</code></td><td><code>string</code></td><td>The route selection expression for the API. For HTTP APIs, the ``routeSelectionExpression`` must be ``$&#123;request.method&#125; $&#123;request.path&#125;``. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</td></tr>
<tr><td><code>body_s3_location</code></td><td><code>object</code></td><td>The S3 location of an OpenAPI definition. Supported only for HTTP APIs. To import an HTTP API, you must specify a ``Body`` or ``BodyS3Location``. If you specify a ``Body`` or ``BodyS3Location``, don't specify CloudFormation resources such as ``AWS::ApiGatewayV2::Authorizer`` or ``AWS::ApiGatewayV2::Route``. API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the API.</td></tr>
<tr><td><code>api_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>base_path</code></td><td><code>string</code></td><td>Specifies how to interpret the base path of the API during import. Valid values are ``ignore``, ``prepend``, and ``split``. The default value is ``ignore``. To learn more, see &#91;Set the OpenAPI basePath Property&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;api-gateway-import-api-basePath.html). Supported only for HTTP APIs.</td></tr>
<tr><td><code>fail_on_warnings</code></td><td><code>boolean</code></td><td>Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.</td></tr>
<tr><td><code>disable_execute_api_endpoint</code></td><td><code>boolean</code></td><td>Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint. By default, clients can invoke your API with the default https:&#x2F;&#x2F;&#123;api_id&#125;.execute-api.&#123;region&#125;.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</td></tr>
<tr><td><code>disable_schema_validation</code></td><td><code>boolean</code></td><td>Avoid validating models when creating a deployment. Supported only for WebSocket APIs.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the API. Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation``.</td></tr>
<tr><td><code>target</code></td><td><code>string</code></td><td>This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.</td></tr>
<tr><td><code>credentials_arn</code></td><td><code>string</code></td><td>This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify ``arn:aws:iam::*:user&#x2F;*``. To use resource-based permissions on supported AWS services, specify ``null``. Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.</td></tr>
<tr><td><code>cors_configuration</code></td><td><code>object</code></td><td>A CORS configuration. Supported only for HTTP APIs. See &#91;Configuring CORS&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;http-api-cors.html) for more information.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>A version identifier for the API.</td></tr>
<tr><td><code>protocol_type</code></td><td><code>string</code></td><td>The API protocol. Valid values are ``WEBSOCKET`` or ``HTTP``. Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation``.</td></tr>
<tr><td><code>route_key</code></td><td><code>string</code></td><td>This property is part of quick create. If you don't specify a ``routeKey``, a default route of ``$default`` is created. The ``$default`` route acts as a catch-all for any request made to your API, for a particular stage. The ``$default`` route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.</td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>body</code></td><td><code>object</code></td><td>The OpenAPI definition. Supported only for HTTP APIs. To import an HTTP API, you must specify a ``Body`` or ``BodyS3Location``. If you specify a ``Body`` or ``BodyS3Location``, don't specify CloudFormation resources such as ``AWS::ApiGatewayV2::Authorizer`` or ``AWS::ApiGatewayV2::Route``. API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><code>api_key_selection_expression</code></td><td><code>string</code></td><td>An API key selection expression. Supported only for WebSocket APIs. See &#91;API Key Selection Expressions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
route_selection_expression,
body_s3_location,
description,
api_endpoint,
base_path,
fail_on_warnings,
disable_execute_api_endpoint,
disable_schema_validation,
name,
target,
credentials_arn,
cors_configuration,
version,
protocol_type,
route_key,
api_id,
body,
tags,
api_key_selection_expression
FROM awscc.apigatewayv2.api
WHERE region = 'us-east-1'
AND data__Identifier = '{ApiId}';
```

## Permissions

To operate on the <code>api</code> resource, the following permissions are required:

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT,
apigateway:POST,
s3:getObject
```

### Read
```json
apigateway:GET,
s3:getObject
```

### Delete
```json
apigateway:GET,
apigateway:DELETE,
s3:getObject
```

