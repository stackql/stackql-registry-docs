---
title: authorizers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizers
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
Retrieves a list of <code>authorizers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.authorizers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>IdentityValidationExpression</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AuthorizerUri</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AuthorizerCredentialsArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AuthorizerType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>JwtConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AuthorizerResultTtlInSeconds</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>IdentitySource</code></td><td><code>array</code></td><td></td></tr><tr><td><code>AuthorizerPayloadFormatVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EnableSimpleResponses</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>AuthorizerId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigatewayv2.authorizers
WHERE region = 'us-east-1'
</pre>
