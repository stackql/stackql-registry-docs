---
title: api
hide_title: false
hide_table_of_contents: false
keywords:
  - api
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
Gets an individual <code>api</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>api</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.api</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>route_selection_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>body_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>base_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>fail_on_warnings</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>disable_execute_api_endpoint</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>disable_schema_validation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>credentials_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cors_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>protocol_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>route_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>body</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>This resource type use map for Tags, suggest to use List of Tag</td></tr>
<tr><td><code>api_key_selection_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
route_selection_expression,
body_s3_location,
description,
api_endpoint,
base_path,
fail_on_warnings,
disable_execute_api_endpoint,
disable_schema_validation,
name,
target,
credentials_arn,
cors_configuration,
version,
protocol_type,
route_key,
api_id,
body,
tags,
api_key_selection_expression
FROM aws.apigatewayv2.api
WHERE region = 'us-east-1'
AND data__Identifier = '<ApiId>'
```
