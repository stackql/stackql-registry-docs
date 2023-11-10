---
title: table
hide_title: false
hide_table_of_contents: false
keywords:
  - table
  - cassandra
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
<tr><td><b>Id</b></td><td><code>aws.cassandra.table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>keyspace_name</code></td><td><code>string</code></td><td>Name for Cassandra keyspace</td></tr>
<tr><td><code>table_name</code></td><td><code>string</code></td><td>Name for Cassandra table</td></tr>
<tr><td><code>regular_columns</code></td><td><code>array</code></td><td>Non-key columns of the table</td></tr>
<tr><td><code>partition_key_columns</code></td><td><code>array</code></td><td>Partition key columns of the table</td></tr>
<tr><td><code>clustering_key_columns</code></td><td><code>array</code></td><td>Clustering key columns of the table</td></tr>
<tr><td><code>billing_mode</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>point_in_time_recovery_enabled</code></td><td><code>boolean</code></td><td>Indicates whether point in time recovery is enabled (true) or disabled (false) on the table</td></tr>
<tr><td><code>client_side_timestamps_enabled</code></td><td><code>boolean</code></td><td>Indicates whether client side timestamps are enabled (true) or disabled (false) on the table. False by default, once it is enabled it cannot be disabled again.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource</td></tr>
<tr><td><code>default_time_to_live</code></td><td><code>integer</code></td><td>Default TTL (Time To Live) in seconds, where zero is disabled. If the value is greater than zero, TTL is enabled for the entire table and an expiration timestamp is added to each column.</td></tr>
<tr><td><code>encryption_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
keyspace_name,
table_name,
regular_columns,
partition_key_columns,
clustering_key_columns,
billing_mode,
point_in_time_recovery_enabled,
client_side_timestamps_enabled,
tags,
default_time_to_live,
encryption_specification
FROM aws.cassandra.table
WHERE region = 'us-east-1'
AND data__Identifier = '<KeyspaceName>'
AND data__Identifier = '<TableName>'
```
