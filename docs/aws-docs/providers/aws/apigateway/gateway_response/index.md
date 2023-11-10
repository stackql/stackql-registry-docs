---
title: gateway_response
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_response
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
Gets an individual <code>gateway_response</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_response</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>gateway_response</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.gateway_response</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>A Cloudformation auto generated ID.</td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The identifier of the API.</td></tr>
<tr><td><code>response_type</code></td><td><code>string</code></td><td>The type of the Gateway Response.</td></tr>
<tr><td><code>status_code</code></td><td><code>string</code></td><td>The HTTP status code for the response.</td></tr>
<tr><td><code>response_parameters</code></td><td><code>object</code></td><td>The response parameters (paths, query strings, and headers) for the response.</td></tr>
<tr><td><code>response_templates</code></td><td><code>object</code></td><td>The response templates for the response.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
rest_api_id,
response_type,
status_code,
response_parameters,
response_templates
FROM aws.apigateway.gateway_response
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
