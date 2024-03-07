---
title: method
hide_title: false
hide_table_of_contents: false
keywords:
  - method
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
Gets an individual <code>method</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>method</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>method</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.method</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_key_required</code></td><td><code>boolean</code></td><td>A boolean flag specifying whether a valid ApiKey is required to invoke this method.</td></tr>
<tr><td><code>authorization_scopes</code></td><td><code>array</code></td><td>A list of authorization scopes configured on the method. The scopes are used with a ``COGNITO_USER_POOLS`` authorizer to authorize the method invocation. The authorization works by matching the method scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any method scopes matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the method scope is configured, the client must provide an access token instead of an identity token for authorization purposes.</td></tr>
<tr><td><code>authorization_type</code></td><td><code>string</code></td><td>The method's authorization type. This parameter is required. For valid values, see &#91;Method&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;api&#x2F;API_Method.html) in the *API Gateway API Reference*.&lt;br&#x2F;&gt;  If you specify the ``AuthorizerId`` property, specify ``CUSTOM`` or ``COGNITO_USER_POOLS`` for this property.</td></tr>
<tr><td><code>authorizer_id</code></td><td><code>string</code></td><td>The identifier of an authorizer to use on this method. The method's authorization type must be ``CUSTOM`` or ``COGNITO_USER_POOLS``.</td></tr>
<tr><td><code>http_method</code></td><td><code>string</code></td><td>The method's HTTP verb.</td></tr>
<tr><td><code>integration</code></td><td><code>object</code></td><td>Represents an ``HTTP``, ``HTTP_PROXY``, ``AWS``, ``AWS_PROXY``, or Mock integration.</td></tr>
<tr><td><code>method_responses</code></td><td><code>array</code></td><td>Gets a method response associated with a given HTTP status code.</td></tr>
<tr><td><code>operation_name</code></td><td><code>string</code></td><td>A human-friendly operation identifier for the method. For example, you can assign the ``operationName`` of ``ListPets`` for the ``GET &#x2F;pets`` method in the ``PetStore`` example.</td></tr>
<tr><td><code>request_models</code></td><td><code>object</code></td><td>A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).</td></tr>
<tr><td><code>request_parameters</code></td><td><code>object</code></td><td>A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of ``method.request.&#123;location&#125;.&#123;name&#125;``, where ``location`` is ``querystring``, ``path``, or ``header`` and ``name`` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (``true``) or optional (``false``). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or templates.</td></tr>
<tr><td><code>request_validator_id</code></td><td><code>string</code></td><td>The identifier of a RequestValidator for request validation.</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>The Resource identifier for the MethodResponse resource.</td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>method</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:DELETE,
apigateway:PUT,
iam:PassRole
```

### Delete
```json
apigateway:DELETE
```


## Example
```sql
SELECT
region,
api_key_required,
authorization_scopes,
authorization_type,
authorizer_id,
http_method,
integration,
method_responses,
operation_name,
request_models,
request_parameters,
request_validator_id,
resource_id,
rest_api_id
FROM awscc.apigateway.method
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RestApiId&gt;'
AND data__Identifier = '&lt;ResourceId&gt;'
AND data__Identifier = '&lt;HttpMethod&gt;'
```
