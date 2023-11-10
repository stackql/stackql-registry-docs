---
title: replication_task
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_task
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>replication_task</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replication_task</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dms.replication_task</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>replication_task_settings</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cdc_start_position</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cdc_stop_position</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>migration_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_endpoint_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>replication_instance_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>task_data</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cdc_start_time</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>table_mappings</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>replication_task_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_endpoint_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
replication_task_settings,
cdc_start_position,
cdc_stop_position,
migration_type,
target_endpoint_arn,
replication_instance_arn,
task_data,
cdc_start_time,
resource_identifier,
table_mappings,
replication_task_identifier,
source_endpoint_arn,
id,
tags
FROM aws.dms.replication_task
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
