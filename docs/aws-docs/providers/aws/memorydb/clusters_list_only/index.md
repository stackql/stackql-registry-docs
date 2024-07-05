---
title: clusters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_list_only
  - memorydb
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

Lists <code>clusters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/clusters/"><code>clusters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::Cluster resource creates an Amazon MemoryDB Cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.clusters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the cluster. This value must be unique as it also serves as the cluster identifier.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description of the cluster.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the cluster. For example, Available, Updating, Creating.</td></tr>
<tr><td><CopyableCode code="node_type" /></td><td><code>string</code></td><td>The compute and memory capacity of the nodes in the cluster.</td></tr>
<tr><td><CopyableCode code="num_shards" /></td><td><code>integer</code></td><td>The number of shards the cluster will contain.</td></tr>
<tr><td><CopyableCode code="num_replicas_per_shard" /></td><td><code>integer</code></td><td>The number of replicas to apply to each shard. The limit is 5.</td></tr>
<tr><td><CopyableCode code="subnet_group_name" /></td><td><code>string</code></td><td>The name of the subnet group to be used for the cluster.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>One or more Amazon VPC security groups associated with this cluster.</td></tr>
<tr><td><CopyableCode code="maintenance_window" /></td><td><code>string</code></td><td>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</td></tr>
<tr><td><CopyableCode code="parameter_group_name" /></td><td><code>string</code></td><td>The name of the parameter group associated with the cluster.</td></tr>
<tr><td><CopyableCode code="parameter_group_status" /></td><td><code>string</code></td><td>The status of the parameter group used by the cluster.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port number on which each member of the cluster accepts connections.</td></tr>
<tr><td><CopyableCode code="snapshot_retention_limit" /></td><td><code>integer</code></td><td>The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</td></tr>
<tr><td><CopyableCode code="snapshot_window" /></td><td><code>string</code></td><td>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your cluster.</td></tr>
<tr><td><CopyableCode code="acl_name" /></td><td><code>string</code></td><td>The name of the Access Control List to associate with the cluster.</td></tr>
<tr><td><CopyableCode code="sns_topic_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</td></tr>
<tr><td><CopyableCode code="sns_topic_status" /></td><td><code>string</code></td><td>The status of the Amazon SNS notification topic. Notifications are sent only if the status is enabled.</td></tr>
<tr><td><CopyableCode code="tls_enabled" /></td><td><code>boolean</code></td><td>A flag that enables in-transit encryption when set to true.<br />You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.</td></tr>
<tr><td><CopyableCode code="data_tiering" /></td><td><code>object</code></td><td>Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The ID of the KMS key used to encrypt the cluster.</td></tr>
<tr><td><CopyableCode code="snapshot_arns" /></td><td><code>array</code></td><td>A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.</td></tr>
<tr><td><CopyableCode code="snapshot_name" /></td><td><code>string</code></td><td>The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.</td></tr>
<tr><td><CopyableCode code="final_snapshot_name" /></td><td><code>string</code></td><td>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The Redis engine version used by the cluster.</td></tr>
<tr><td><CopyableCode code="cluster_endpoint" /></td><td><code>object</code></td><td>The cluster endpoint.</td></tr>
<tr><td><CopyableCode code="auto_minor_version_upgrade" /></td><td><code>boolean</code></td><td>A flag that enables automatic minor version upgrade when set to true.<br />You cannot modify the value of AutoMinorVersionUpgrade after the cluster is created. To enable AutoMinorVersionUpgrade on a cluster you must set AutoMinorVersionUpgrade to true when you create a cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this cluster.</td></tr>
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
Lists all <code>clusters</code> in a region.
```sql
SELECT
region,
cluster_name
FROM aws.memorydb.clusters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>clusters_list_only</code> resource, see <a href="/providers/aws/memorydb/clusters/#permissions"><code>clusters</code></a>


