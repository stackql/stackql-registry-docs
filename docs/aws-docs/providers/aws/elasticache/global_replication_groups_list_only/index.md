---
title: global_replication_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - global_replication_groups_list_only
  - elasticache
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

Lists <code>global_replication_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/global_replication_groups/"><code>global_replication_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_replication_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ElastiCache::GlobalReplicationGroup resource creates an Amazon ElastiCache Global Replication Group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.global_replication_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="global_replication_group_id_suffix" /></td><td><code>string</code></td><td>The suffix name of a Global Datastore. Amazon ElastiCache automatically applies a prefix to the Global Datastore ID when it is created. Each AWS Region has its own prefix.</td></tr>
<tr><td><CopyableCode code="automatic_failover_enabled" /></td><td><code>boolean</code></td><td>AutomaticFailoverEnabled</td></tr>
<tr><td><CopyableCode code="cache_node_type" /></td><td><code>string</code></td><td>The cache node type of the Global Datastore</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The engine version of the Global Datastore.</td></tr>
<tr><td><CopyableCode code="cache_parameter_group_name" /></td><td><code>string</code></td><td>Cache parameter group name to use for the new engine version. This parameter cannot be modified independently.</td></tr>
<tr><td><CopyableCode code="global_node_group_count" /></td><td><code>integer</code></td><td>Indicates the number of node groups in the Global Datastore.</td></tr>
<tr><td><CopyableCode code="global_replication_group_description" /></td><td><code>string</code></td><td>The optional description of the Global Datastore</td></tr>
<tr><td><CopyableCode code="global_replication_group_id" /></td><td><code>string</code></td><td>The name of the Global Datastore, it is generated by ElastiCache adding a prefix to GlobalReplicationGroupIdSuffix.</td></tr>
<tr><td><CopyableCode code="members" /></td><td><code>array</code></td><td>The replication groups that comprise the Global Datastore.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Global Datastore</td></tr>
<tr><td><CopyableCode code="regional_configurations" /></td><td><code>array</code></td><td>Describes the replication group IDs, the AWS regions where they are stored and the shard configuration for each that comprise the Global Datastore</td></tr>
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
Lists all <code>global_replication_groups</code> in a region.
```sql
SELECT
region,
global_replication_group_id
FROM aws.elasticache.global_replication_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>global_replication_groups_list_only</code> resource, see <a href="/providers/aws/elasticache/global_replication_groups/#permissions"><code>global_replication_groups</code></a>


