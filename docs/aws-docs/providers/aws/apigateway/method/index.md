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
<tr><td><b>Id</b></td><td><code>aws.apigateway.method</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_key_required</code></td><td><code>boolean</code></td><td>Indicates whether the method requires clients to submit a valid API key.</td></tr>
<tr><td><code>authorization_scopes</code></td><td><code>array</code></td><td>A list of authorization scopes configured on the method.</td></tr>
<tr><td><code>authorization_type</code></td><td><code>string</code></td><td>The method's authorization type.</td></tr>
<tr><td><code>authorizer_id</code></td><td><code>string</code></td><td>The identifier of the authorizer to use on this method.</td></tr>
<tr><td><code>http_method</code></td><td><code>string</code></td><td>The backend system that the method calls when it receives a request.</td></tr>
<tr><td><code>integration</code></td><td><code>object</code></td><td>The backend system that the method calls when it receives a request.</td></tr>
<tr><td><code>method_responses</code></td><td><code>array</code></td><td>The responses that can be sent to the client who calls the method.</td></tr>
<tr><td><code>operation_name</code></td><td><code>string</code></td><td>A friendly operation name for the method.</td></tr>
<tr><td><code>request_models</code></td><td><code>object</code></td><td>The resources that are used for the request's content type. Specify request models as key-value pairs (string-to-string mapping), with a content type as the key and a Model resource name as the value.</td></tr>
<tr><td><code>request_parameters</code></td><td><code>object</code></td><td>The request parameters that API Gateway accepts. Specify request parameters as key-value pairs (string-to-Boolean mapping), with a source as the key and a Boolean as the value.</td></tr>
<tr><td><code>request_validator_id</code></td><td><code>string</code></td><td>The ID of the associated request validator.</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>The ID of an API Gateway resource.</td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The ID of the RestApi resource in which API Gateway creates the method.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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
FROM aws.apigateway.method
WHERE region = 'us-east-1'
AND data__Identifier = '<RestApiId>'
AND data__Identifier = '<ResourceId>'
AND data__Identifier = '<HttpMethod>'
```
