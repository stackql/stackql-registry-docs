---
title: rest_api
hide_title: false
hide_table_of_contents: false
keywords:
  - rest_api
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
Gets an individual <code>rest_api</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rest_api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rest_api</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.rest_api</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RestApiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RootResourceId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiKeySourceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BinaryMediaTypes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Body</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BodyS3Location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>CloneFrom</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EndpointConfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DisableExecuteApiEndpoint</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>FailOnWarnings</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MinimumCompressionSize</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Parameters</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.apigateway.rest_api<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;RestApiId&gt;'
</pre>
