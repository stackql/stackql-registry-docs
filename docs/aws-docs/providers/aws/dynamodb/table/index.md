---
title: table
hide_title: false
hide_table_of_contents: false
keywords:
  - table
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
Gets an individual <code>table</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>table</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dynamodb.table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stream_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attribute_definitions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>billing_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deletion_protection_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>global_secondary_indexes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>key_schema</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>local_secondary_indexes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>point_in_time_recovery_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>table_class</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provisioned_throughput</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>s_se_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>stream_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>table_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>time_to_live_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>contributor_insights_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kinesis_stream_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>import_source_specification</code></td><td><code>object</code></td><td></td></tr>
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
deletion_protection_enabled,
global_secondary_indexes,
key_schema,
local_secondary_indexes,
point_in_time_recovery_specification,
table_class,
provisioned_throughput,
s_se_specification,
stream_specification,
table_name,
tags,
time_to_live_specification,
contributor_insights_specification,
kinesis_stream_specification,
import_source_specification
FROM aws.dynamodb.table
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TableName&gt;'
```
