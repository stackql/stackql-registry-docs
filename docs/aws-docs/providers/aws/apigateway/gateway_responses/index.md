---
title: gateway_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_responses
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
Retrieves a list of <code>gateway_responses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>gateway_responses</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.gateway_responses</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>A Cloudformation auto generated ID.</td></tr>
<tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The identifier of the API.</td></tr>
<tr><td><code>ResponseType</code></td><td><code>string</code></td><td>The type of the Gateway Response.</td></tr>
<tr><td><code>StatusCode</code></td><td><code>string</code></td><td>The HTTP status code for the response.</td></tr>
<tr><td><code>ResponseParameters</code></td><td><code>object</code></td><td>The response parameters (paths, query strings, and headers) for the response.</td></tr>
<tr><td><code>ResponseTemplates</code></td><td><code>object</code></td><td>The response templates for the response.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.gateway_responses
WHERE region = 'us-east-1'
</pre>
