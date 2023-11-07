---
title: integration
hide_title: false
hide_table_of_contents: false
keywords:
  - integration
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
Gets an individual <code>integration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.integration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TemplateSelectionExpression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConnectionType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResponseParameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>IntegrationMethod</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PassthroughBehavior</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RequestParameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ConnectionId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IntegrationUri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PayloadFormatVersion</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CredentialsArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RequestTemplates</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>TimeoutInMillis</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>TlsConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ContentHandlingStrategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IntegrationSubtype</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IntegrationType</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.apigatewayv2.integration<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
