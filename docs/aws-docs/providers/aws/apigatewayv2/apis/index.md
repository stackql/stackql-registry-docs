---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
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
Retrieves a list of <code>apis</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.apis</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RouteSelectionExpression</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BodyS3Location</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApiEndpoint</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BasePath</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FailOnWarnings</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>DisableExecuteApiEndpoint</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>DisableSchemaValidation</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Target</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CredentialsArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CorsConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Version</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ProtocolType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RouteKey</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Body</code></td><td><code>object</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>This resource type use map for Tags, suggest to use List of Tag</td></tr><tr><td><code>ApiKeySelectionExpression</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigatewayv2.apis
WHERE region = 'us-east-1'
</pre>
