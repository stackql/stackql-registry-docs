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
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>root_resource_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_key_source_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>binary_media_types</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>body</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>body_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>clone_from</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>disable_execute_api_endpoint</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>fail_on_warnings</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>minimum_compression_size</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
rest_api_id,
root_resource_id,
api_key_source_type,
binary_media_types,
body,
body_s3_location,
clone_from,
endpoint_configuration,
description,
disable_execute_api_endpoint,
fail_on_warnings,
name,
minimum_compression_size,
mode,
policy,
parameters,
tags
FROM aws.apigateway.rest_api
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RestApiId&gt;'
```
