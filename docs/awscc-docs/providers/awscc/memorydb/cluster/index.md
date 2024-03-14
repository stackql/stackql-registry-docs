---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
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
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.memorydb.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>The name of the cluster. This value must be unique as it also serves as the cluster identifier.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>An optional description of the cluster.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the cluster. For example, Available, Updating, Creating.</td></tr>
<tr><td><code>node_type</code></td><td><code>string</code></td><td>The compute and memory capacity of the nodes in the cluster.</td></tr>
<tr><td><code>num_shards</code></td><td><code>integer</code></td><td>The number of shards the cluster will contain.</td></tr>
<tr><td><code>num_replicas_per_shard</code></td><td><code>integer</code></td><td>The number of replicas to apply to each shard. The limit is 5.</td></tr>
<tr><td><code>subnet_group_name</code></td><td><code>string</code></td><td>The name of the subnet group to be used for the cluster.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>One or more Amazon VPC security groups associated with this cluster.</td></tr>
<tr><td><code>maintenance_window</code></td><td><code>string</code></td><td>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</td></tr>
<tr><td><code>parameter_group_name</code></td><td><code>string</code></td><td>The name of the parameter group associated with the cluster.</td></tr>
<tr><td><code>parameter_group_status</code></td><td><code>string</code></td><td>The status of the parameter group used by the cluster.</td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td>The port number on which each member of the cluster accepts connections.</td></tr>
<tr><td><code>snapshot_retention_limit</code></td><td><code>integer</code></td><td>The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</td></tr>
<tr><td><code>snapshot_window</code></td><td><code>string</code></td><td>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your cluster.</td></tr>
<tr><td><code>acl_name</code></td><td><code>string</code></td><td>The name of the Access Control List to associate with the cluster.</td></tr>
<tr><td><code>sns_topic_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</td></tr>
<tr><td><code>sns_topic_status</code></td><td><code>string</code></td><td>The status of the Amazon SNS notification topic. Notifications are sent only if the status is enabled.</td></tr>
<tr><td><code>tls_enabled</code></td><td><code>boolean</code></td><td>A flag that enables in-transit encryption when set to true.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.</td></tr>
<tr><td><code>data_tiering</code></td><td><code>string</code></td><td>Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The ID of the KMS key used to encrypt the cluster.</td></tr>
<tr><td><code>snapshot_arns</code></td><td><code>array</code></td><td>A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.</td></tr>
<tr><td><code>snapshot_name</code></td><td><code>string</code></td><td>The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.</td></tr>
<tr><td><code>final_snapshot_name</code></td><td><code>string</code></td><td>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td>The Redis engine version used by the cluster.</td></tr>
<tr><td><code>cluster_endpoint</code></td><td><code>object</code></td><td>The cluster endpoint.</td></tr>
<tr><td><code>auto_minor_version_upgrade</code></td><td><code>boolean</code></td><td>A flag that enables automatic minor version upgrade when set to true.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;You cannot modify the value of AutoMinorVersionUpgrade after the cluster is created. To enable AutoMinorVersionUpgrade on a cluster you must set AutoMinorVersionUpgrade to true when you create a cluster.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this cluster.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
cluster_name,
description,
status,
node_type,
num_shards,
num_replicas_per_shard,
subnet_group_name,
security_group_ids,
maintenance_window,
parameter_group_name,
parameter_group_status,
port,
snapshot_retention_limit,
snapshot_window,
acl_name,
sns_topic_arn,
sns_topic_status,
tls_enabled,
data_tiering,
kms_key_id,
snapshot_arns,
snapshot_name,
final_snapshot_name,
arn,
engine_version,
cluster_endpoint,
auto_minor_version_upgrade,
tags
FROM awscc.memorydb.cluster
WHERE data__Identifier = '<ClusterName>';
```

## Permissions

To operate on the <code>cluster</code> resource, the following permissions are required:

### Read
```json
memorydb:DescribeClusters,
memorydb:ListTags
```

### Update
```json
memorydb:UpdateCluster,
memorydb:DescribeClusters,
memorydb:ListTags,
memorydb:TagResource,
memorydb:UntagResource
```

### Delete
```json
memorydb:DeleteCluster,
memorydb:DescribeClusters
```

