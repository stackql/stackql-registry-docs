---
title: function_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - function_configuration
  - appsync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>function_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>function_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>function_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.function_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>function_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>request_mapping_template</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_mapping_template</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_batch_size</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>sync_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_mapping_template_s3_location</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>runtime</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>code_s3_location</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_source_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>function_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>request_mapping_template_s3_location</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
function_id,
function_arn,
description,
request_mapping_template,
response_mapping_template,
max_batch_size,
sync_config,
code,
name,
response_mapping_template_s3_location,
runtime,
code_s3_location,
data_source_name,
function_version,
id,
request_mapping_template_s3_location,
api_id
FROM aws.appsync.function_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
