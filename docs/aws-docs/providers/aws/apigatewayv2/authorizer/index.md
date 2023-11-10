---
title: authorizer
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizer
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
Gets an individual <code>authorizer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>authorizer</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.authorizer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>identity_validation_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorizer_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorizer_credentials_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorizer_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>jwt_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>authorizer_result_ttl_in_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>identity_source</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>authorizer_payload_format_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_simple_responses</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>authorizer_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
identity_validation_expression,
authorizer_uri,
authorizer_credentials_arn,
authorizer_type,
jwt_configuration,
authorizer_result_ttl_in_seconds,
identity_source,
authorizer_payload_format_version,
api_id,
enable_simple_responses,
authorizer_id,
name
FROM aws.apigatewayv2.authorizer
WHERE region = 'us-east-1'
AND data__Identifier = '<AuthorizerId>'
AND data__Identifier = '<ApiId>'
```
