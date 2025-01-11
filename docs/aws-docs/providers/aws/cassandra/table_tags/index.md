---
title: table_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - table_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Cassandra::Table</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cassandra.table_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="keyspace_name" /></td><td><code>string</code></td><td>Name for Cassandra keyspace</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>Name for Cassandra table</td></tr>
<tr><td><CopyableCode code="regular_columns" /></td><td><code>array</code></td><td>Non-key columns of the table</td></tr>
<tr><td><CopyableCode code="partition_key_columns" /></td><td><code>array</code></td><td>Partition key columns of the table</td></tr>
<tr><td><CopyableCode code="clustering_key_columns" /></td><td><code>array</code></td><td>Clustering key columns of the table</td></tr>
<tr><td><CopyableCode code="billing_mode" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="point_in_time_recovery_enabled" /></td><td><code>boolean</code></td><td>Indicates whether point in time recovery is enabled (true) or disabled (false) on the table</td></tr>
<tr><td><CopyableCode code="client_side_timestamps_enabled" /></td><td><code>boolean</code></td><td>Indicates whether client side timestamps are enabled (true) or disabled (false) on the table. False by default, once it is enabled it cannot be disabled again.</td></tr>
<tr><td><CopyableCode code="default_time_to_live" /></td><td><code>integer</code></td><td>Default TTL (Time To Live) in seconds, where zero is disabled. If the value is greater than zero, TTL is enabled for the entire table and an expiration timestamp is added to each column.</td></tr>
<tr><td><CopyableCode code="encryption_specification" /></td><td><code>object</code></td><td>Represents the settings used to enable server-side encryption</td></tr>
<tr><td><CopyableCode code="auto_scaling_specifications" /></td><td><code>object</code></td><td>Represents the read and write settings used for AutoScaling.</td></tr>
<tr><td><CopyableCode code="replica_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>tables</code> in a region.
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
default_time_to_live,
encryption_specification,
auto_scaling_specifications,
replica_specifications,
tag_key,
tag_value
FROM aws.cassandra.table_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>table_tags</code> resource, see <a href="/providers/aws/cassandra/tables/#permissions"><code>tables</code></a>

