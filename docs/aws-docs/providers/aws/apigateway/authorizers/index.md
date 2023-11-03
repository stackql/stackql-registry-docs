---
title: authorizers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizers
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
Retrieves a list of <code>authorizers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigateway.authorizers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The identifier of the API.</td></tr><tr><td><code>AuthorizerId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AuthType</code></td><td><code>string</code></td><td>Optional customer-defined field, used in OpenAPI imports and exports without functional impact.</td></tr><tr><td><code>AuthorizerCredentials</code></td><td><code>string</code></td><td>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.</td></tr><tr><td><code>AuthorizerResultTtlInSeconds</code></td><td><code>integer</code></td><td>The TTL in seconds of cached authorizer results.</td></tr><tr><td><code>AuthorizerUri</code></td><td><code>string</code></td><td>Specifies the authorizer's Uniform Resource Identifier (URI).</td></tr><tr><td><code>IdentitySource</code></td><td><code>string</code></td><td>The identity source for which authorization is requested.</td></tr><tr><td><code>IdentityValidationExpression</code></td><td><code>string</code></td><td>A validation expression for the incoming identity token.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the authorizer.</td></tr><tr><td><code>ProviderARNs</code></td><td><code>array</code></td><td>A list of the Amazon Cognito user pool ARNs for the COGNITO_USER_POOLS authorizer.</td></tr><tr><td><code>Type</code></td><td><code>string</code></td><td>The authorizer type.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.authorizers
WHERE region = 'us-east-1'
</pre>
