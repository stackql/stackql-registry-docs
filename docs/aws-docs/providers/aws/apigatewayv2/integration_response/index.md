---
title: integration_response
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_response
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
Gets an individual <code>integration_response</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_response</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integration_response</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.integration_response</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_templates</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>template_selection_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>content_handling_strategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>integration_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>integration_response_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
response_templates,
template_selection_expression,
response_parameters,
content_handling_strategy,
integration_id,
integration_response_key,
api_id
FROM aws.apigatewayv2.integration_response
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
