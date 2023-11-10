---
title: global_table
hide_title: false
hide_table_of_contents: false
keywords:
  - global_table
  - dynamodb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>global_table</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>global_table</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dynamodb.global_table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stream_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attribute_definitions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>billing_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>global_secondary_indexes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>key_schema</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>local_secondary_indexes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>write_provisioned_throughput_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>replicas</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>s_se_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>stream_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>table_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>table_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>time_to_live_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
stream_arn,
attribute_definitions,
billing_mode,
global_secondary_indexes,
key_schema,
local_secondary_indexes,
write_provisioned_throughput_settings,
replicas,
s_se_specification,
stream_specification,
table_name,
table_id,
time_to_live_specification
FROM aws.dynamodb.global_table
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TableName&gt;'
```
