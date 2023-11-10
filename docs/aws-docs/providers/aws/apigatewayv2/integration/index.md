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
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_selection_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connection_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>integration_method</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>passthrough_behavior</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>request_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>connection_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>integration_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>payload_format_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>credentials_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>request_templates</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>timeout_in_millis</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tls_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>content_handling_strategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>integration_subtype</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>integration_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
template_selection_expression,
connection_type,
response_parameters,
integration_method,
passthrough_behavior,
request_parameters,
connection_id,
integration_uri,
payload_format_version,
credentials_arn,
request_templates,
timeout_in_millis,
tls_config,
content_handling_strategy,
id,
integration_subtype,
api_id,
integration_type
FROM aws.apigatewayv2.integration
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
