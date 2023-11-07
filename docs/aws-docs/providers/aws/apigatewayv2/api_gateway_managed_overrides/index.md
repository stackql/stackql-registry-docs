---
title: api_gateway_managed_overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - api_gateway_managed_overrides
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
Gets an individual <code>api_gateway_managed_overrides</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_gateway_managed_overrides</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.api_gateway_managed_overrides</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Stage</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Integration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Route</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigatewayv2.api_gateway_managed_overrides
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
