---
title: authorizer
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizer
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
Gets an individual <code>authorizer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>authorizer</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.authorizer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>authorizer_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auth_type</code></td><td><code>string</code></td><td>Optional customer-defined field, used in OpenAPI imports and exports without functional impact.</td></tr>
<tr><td><code>authorizer_credentials</code></td><td><code>string</code></td><td>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.</td></tr>
<tr><td><code>authorizer_result_ttl_in_seconds</code></td><td><code>integer</code></td><td>The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.</td></tr>
<tr><td><code>authorizer_uri</code></td><td><code>string</code></td><td>Specifies the authorizer's Uniform Resource Identifier (URI). For ``TOKEN`` or ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path&#x2F;2015-03-31&#x2F;functions&#x2F;arn:aws:lambda:us-west-2:&#123;account_id&#125;:function:&#123;lambda_function_name&#125;&#x2F;invocations``. In general, the URI has this form ``arn:aws:apigateway:&#123;region&#125;:lambda:path&#x2F;&#123;service_api&#125;``, where ``&#123;region&#125;`` is the same as the region hosting the Lambda function, ``path`` indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``&#x2F;``. For Lambda functions, this is usually of the form ``&#x2F;2015-03-31&#x2F;functions&#x2F;&#91;FunctionARN&#93;&#x2F;invocations``.</td></tr>
<tr><td><code>identity_source</code></td><td><code>string</code></td><td>The identity source for which authorization is requested. For a ``TOKEN`` or ``COGNITO_USER_POOLS`` authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is ``Auth``, the header mapping expression is ``method.request.header.Auth``. For the ``REQUEST`` authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an ``Auth`` header, a ``Name`` query string parameter are defined as identity sources, this value is ``method.request.header.Auth, method.request.querystring.Name``. These parameters will be used to derive the authorization caching key and to perform runtime validation of the ``REQUEST`` authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when thi</td></tr>
<tr><td><code>identity_validation_expression</code></td><td><code>string</code></td><td>A validation expression for the incoming identity token. For ``TOKEN`` authorizers, this value is a regular expression. For ``COGNITO_USER_POOLS`` authorizers, API Gateway will match the ``aud`` field of the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function when there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the ``REQUEST`` authorizer.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the authorizer.</td></tr>
<tr><td><code>provider_ar_ns</code></td><td><code>array</code></td><td>A list of the Amazon Cognito user pool ARNs for the ``COGNITO_USER_POOLS`` authorizer. Each element is of this format: ``arn:aws:cognito-idp:&#123;region&#125;:&#123;account_id&#125;:userpool&#x2F;&#123;user_pool_id&#125;``. For a ``TOKEN`` or ``REQUEST`` authorizer, this is not defined.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The authorizer type. Valid values are ``TOKEN`` for a Lambda function using a single authorization token submitted in a custom header, ``REQUEST`` for a Lambda function using incoming request parameters, and ``COGNITO_USER_POOLS`` for using an Amazon Cognito user pool.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>authorizer</code> resource, the following permissions are required:

### Read
<pre>
apigateway:GET</pre>

### Update
<pre>
apigateway:GET,
apigateway:PATCH,
iam:PassRole</pre>

### Delete
<pre>
apigateway:DELETE</pre>


## Example
```sql
SELECT
region,
rest_api_id,
authorizer_id,
auth_type,
authorizer_credentials,
authorizer_result_ttl_in_seconds,
authorizer_uri,
identity_source,
identity_validation_expression,
name,
provider_ar_ns,
type
FROM awscc.apigateway.authorizer
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RestApiId&gt;'
AND data__Identifier = '&lt;AuthorizerId&gt;'
```
