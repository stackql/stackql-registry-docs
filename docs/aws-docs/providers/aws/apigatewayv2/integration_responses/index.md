---
title: integration_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_responses
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
Retrieves a list of <code>integration_responses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.integration_responses</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResponseTemplates</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>TemplateSelectionExpression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResponseParameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ContentHandlingStrategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IntegrationId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IntegrationResponseKey</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigatewayv2.integration_responses
WHERE region = 'us-east-1'
</pre>
