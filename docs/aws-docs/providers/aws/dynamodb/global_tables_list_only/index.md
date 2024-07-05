---
title: global_tables_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - global_tables_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>global_tables</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/global_tables/"><code>global_tables</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_tables_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Version: None. Resource Type definition for AWS::DynamoDB::GlobalTable</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dynamodb.global_tables_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stream_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_definitions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="global_secondary_indexes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="key_schema" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="local_secondary_indexes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="write_provisioned_throughput_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="write_on_demand_throughput_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="replicas" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sse_specification" /></td><td><code>object</code></td><td>Represents the settings used to enable server-side encryption.</td></tr>
<tr><td><CopyableCode code="stream_specification" /></td><td><code>object</code></td><td>Represents the DynamoDB Streams configuration for a table in DynamoDB.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="table_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="time_to_live_specification" /></td><td><code>object</code></td><td>Represents the settings used to enable or disable Time to Live (TTL) for the specified table.</td></tr>
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
Lists all <code>global_tables</code> in a region.
```sql
SELECT
region,
table_name
FROM aws.dynamodb.global_tables_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>global_tables_list_only</code> resource, see <a href="/providers/aws/dynamodb/global_tables/#permissions"><code>global_tables</code></a>


