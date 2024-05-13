---
title: authorizer
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizer
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


Gets or updates an individual <code>authorizer</code> resource, use <code>authorizers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::Authorizer</code> resource creates an authorizer for a WebSocket API or an HTTP API. To learn more, see &#91;Controlling and managing access to a WebSocket API in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;apigateway-websocket-api-control-access.html) and &#91;Controlling and managing access to an HTTP API in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;http-api-access-control.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.authorizer" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_validation_expression" /></td><td><code>string</code></td><td>This parameter is not used.</td></tr>
<tr><td><CopyableCode code="authorizer_uri" /></td><td><code>string</code></td><td>The authorizer's Uniform Resource Identifier (URI). For <code>REQUEST</code> authorizers, this must be a well-formed Lambda function URI, for example, <code>arn:aws:apigateway:us-west-2:lambda:path&#x2F;2015-03-31&#x2F;functions&#x2F;arn:aws:lambda:us-west-2:&#123;account_id&#125;:function:&#123;lambda_function_name&#125;&#x2F;invocations</code>. In general, the URI has this form: <code>arn:aws:apigateway:&#123;region&#125;:lambda:path&#x2F;&#123;service_api&#125;</code>, where *&#123;region&#125;* is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial <code>&#x2F;</code>. For Lambda functions, this is usually of the form <code>&#x2F;2015-03-31&#x2F;functions&#x2F;&#91;FunctionARN&#93;&#x2F;invocations</code>.</td></tr>
<tr><td><CopyableCode code="authorizer_credentials_arn" /></td><td><code>string</code></td><td>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for <code>REQUEST</code> authorizers.</td></tr>
<tr><td><CopyableCode code="authorizer_type" /></td><td><code>string</code></td><td>The authorizer type. Specify <code>REQUEST</code> for a Lambda function using incoming request parameters. Specify <code>JWT</code> to use JSON Web Tokens (supported only for HTTP APIs).</td></tr>
<tr><td><CopyableCode code="jwt_configuration" /></td><td><code>object</code></td><td>The <code>JWTConfiguration</code> property specifies the configuration of a JWT authorizer. Required for the <code>JWT</code> authorizer type. Supported only for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="authorizer_result_ttl_in_seconds" /></td><td><code>integer</code></td><td>The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.</td></tr>
<tr><td><CopyableCode code="identity_source" /></td><td><code>array</code></td><td>The identity source for which authorization is requested.&lt;br&#x2F;&gt; For a <code>REQUEST</code> authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with <code>$</code>, for example, <code>$request.header.Auth</code>, <code>$request.querystring.Name</code>. These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see &#91;Working with Lambda authorizers for HTTP APIs&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;http-api-lambda-authorizer.html).&lt;br&#x2F;&gt; For <code>JWT</code>, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example <code>$request.header.Authorization</code>.</td></tr>
<tr><td><CopyableCode code="authorizer_payload_format_version" /></td><td><code>string</code></td><td>Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are <code>1.0</code> and <code>2.0</code>. To learn more, see &#91;Working with Lambda authorizers for HTTP APIs&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;http-api-lambda-authorizer.html).</td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><CopyableCode code="enable_simple_responses" /></td><td><code>boolean</code></td><td>Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see &#91;Working with Lambda authorizers for HTTP APIs&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;http-api-lambda-authorizer.html).</td></tr>
<tr><td><CopyableCode code="authorizer_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the authorizer.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
identity_validation_expression,
authorizer_uri,
authorizer_credentials_arn,
authorizer_type,
jwt_configuration,
authorizer_result_ttl_in_seconds,
identity_source,
authorizer_payload_format_version,
api_id,
enable_simple_responses,
authorizer_id,
name
FROM aws.apigatewayv2.authorizer
WHERE region = 'us-east-1' AND data__Identifier = '<AuthorizerId>|<ApiId>';
```


## Permissions

To operate on the <code>authorizer</code> resource, the following permissions are required:

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT,
iam:PassRole
```

### Read
```json
apigateway:GET
```

