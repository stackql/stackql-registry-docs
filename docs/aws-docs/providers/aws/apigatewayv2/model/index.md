---
title: model
hide_title: false
hide_table_of_contents: false
keywords:
  - model
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
Gets an individual <code>model</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.model</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ModelId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ContentType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Schema</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.apigatewayv2.model<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ApiId&gt;'<br/>AND data__Identifier = '&lt;ModelId&gt;'
</pre>
