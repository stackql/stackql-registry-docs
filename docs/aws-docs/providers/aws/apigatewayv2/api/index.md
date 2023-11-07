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
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.api</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RouteSelectionExpression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BodyS3Location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiEndpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BasePath</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>FailOnWarnings</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>DisableExecuteApiEndpoint</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>DisableSchemaValidation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Target</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CredentialsArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CorsConfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProtocolType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RouteKey</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Body</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>This resource type use map for Tags, suggest to use List of Tag</td></tr>
<tr><td><code>ApiKeySelectionExpression</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.apigatewayv2.api<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ApiId&gt;'
</pre>
