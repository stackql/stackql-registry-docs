---
title: db_shard_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - db_shard_group_tags
  - rds
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

Expands all tag keys and values for <code>db_shard_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_shard_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::DBShardGroup resource creates an Amazon Aurora Limitless DB Shard Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_shard_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_shard_group_resource_id" /></td><td><code>string</code></td><td>The Amazon Web Services Region-unique, immutable identifier for the DB shard group.</td></tr>
<tr><td><CopyableCode code="db_shard_group_identifier" /></td><td><code>string</code></td><td>The name of the DB shard group.</td></tr>
<tr><td><CopyableCode code="db_cluster_identifier" /></td><td><code>string</code></td><td>The name of the primary DB cluster for the DB shard group.</td></tr>
<tr><td><CopyableCode code="compute_redundancy" /></td><td><code>integer</code></td><td>Specifies whether to create standby instances for the DB shard group.</td></tr>
<tr><td><CopyableCode code="max_ac_u" /></td><td><code>number</code></td><td>The maximum capacity of the DB shard group in Aurora capacity units (ACUs).</td></tr>
<tr><td><CopyableCode code="min_ac_u" /></td><td><code>number</code></td><td>The minimum capacity of the DB shard group in Aurora capacity units (ACUs).</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>Indicates whether the DB shard group is publicly accessible.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The connection endpoint for the DB shard group.</td></tr>
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
Expands tags for all <code>db_shard_groups</code> in a region.
```sql
SELECT
region,
db_shard_group_resource_id,
db_shard_group_identifier,
db_cluster_identifier,
compute_redundancy,
max_ac_u,
min_ac_u,
publicly_accessible,
endpoint,
tag_key,
tag_value
FROM aws.rds.db_shard_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_shard_group_tags</code> resource, see <a href="/providers/aws/rds/db_shard_groups/#permissions"><code>db_shard_groups</code></a>

