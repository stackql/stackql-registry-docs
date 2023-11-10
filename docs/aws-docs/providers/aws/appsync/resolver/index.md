---
title: resolver
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver
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
Gets an individual <code>resolver</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.resolver</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pipeline_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>request_mapping_template</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_mapping_template</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_batch_size</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>resolver_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sync_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_mapping_template_s3_location</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>runtime</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>code_s3_location</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_source_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kind</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>caching_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>request_mapping_template_s3_location</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>field_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type_name,
pipeline_config,
request_mapping_template,
response_mapping_template,
max_batch_size,
resolver_arn,
sync_config,
code,
response_mapping_template_s3_location,
runtime,
code_s3_location,
data_source_name,
kind,
caching_config,
id,
request_mapping_template_s3_location,
field_name,
api_id
FROM aws.appsync.resolver
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
