---
title: route
hide_title: false
hide_table_of_contents: false
keywords:
  - route
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
Gets an individual <code>route</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>route</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.route</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RouteId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RouteResponseSelectionExpression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RequestModels</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>OperationName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AuthorizationScopes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ApiKeyRequired</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>RouteKey</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AuthorizationType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ModelSelectionExpression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RequestParameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Target</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AuthorizerId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.apigatewayv2.route<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ApiId&gt;'<br/>AND data__Identifier = '&lt;RouteId&gt;'
</pre>
