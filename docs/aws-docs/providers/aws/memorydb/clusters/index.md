---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
Retrieves a list of <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>clusters</td></tr>
<tr><td><b>Id</b></td><td><code>aws.memorydb.clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ClusterName</code></td><td><code>string</code></td><td>The name of the cluster. This value must be unique as it also serves as the cluster identifier.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>An optional description of the cluster.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>The status of the cluster. For example, Available, Updating, Creating.</td></tr>
<tr><td><code>NodeType</code></td><td><code>string</code></td><td>The compute and memory capacity of the nodes in the cluster.</td></tr>
<tr><td><code>NumShards</code></td><td><code>integer</code></td><td>The number of shards the cluster will contain.</td></tr>
<tr><td><code>NumReplicasPerShard</code></td><td><code>integer</code></td><td>The number of replicas to apply to each shard. The limit is 5.</td></tr>
<tr><td><code>SubnetGroupName</code></td><td><code>string</code></td><td>The name of the subnet group to be used for the cluster.</td></tr>
<tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td>One or more Amazon VPC security groups associated with this cluster.</td></tr>
<tr><td><code>MaintenanceWindow</code></td><td><code>string</code></td><td>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</td></tr>
<tr><td><code>ParameterGroupName</code></td><td><code>string</code></td><td>The name of the parameter group associated with the cluster.</td></tr>
<tr><td><code>ParameterGroupStatus</code></td><td><code>string</code></td><td>The status of the parameter group used by the cluster.</td></tr>
<tr><td><code>Port</code></td><td><code>integer</code></td><td>The port number on which each member of the cluster accepts connections.</td></tr>
<tr><td><code>SnapshotRetentionLimit</code></td><td><code>integer</code></td><td>The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</td></tr>
<tr><td><code>SnapshotWindow</code></td><td><code>string</code></td><td>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your cluster.</td></tr>
<tr><td><code>ACLName</code></td><td><code>string</code></td><td>The name of the Access Control List to associate with the cluster.</td></tr>
<tr><td><code>SnsTopicArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</td></tr>
<tr><td><code>SnsTopicStatus</code></td><td><code>string</code></td><td>The status of the Amazon SNS notification topic. Notifications are sent only if the status is enabled.</td></tr>
<tr><td><code>TLSEnabled</code></td><td><code>boolean</code></td><td>A flag that enables in-transit encryption when set to true.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.</td></tr>
<tr><td><code>DataTiering</code></td><td><code>object</code></td><td>Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes.</td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>The ID of the KMS key used to encrypt the cluster.</td></tr>
<tr><td><code>SnapshotArns</code></td><td><code>array</code></td><td>A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.</td></tr>
<tr><td><code>SnapshotName</code></td><td><code>string</code></td><td>The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.</td></tr>
<tr><td><code>FinalSnapshotName</code></td><td><code>string</code></td><td>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.</td></tr>
<tr><td><code>ARN</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><code>EngineVersion</code></td><td><code>string</code></td><td>The Redis engine version used by the cluster.</td></tr>
<tr><td><code>ClusterEndpoint</code></td><td><code>undefined</code></td><td>The cluster endpoint.</td></tr>
<tr><td><code>AutoMinorVersionUpgrade</code></td><td><code>boolean</code></td><td>A flag that enables automatic minor version upgrade when set to true.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;You cannot modify the value of AutoMinorVersionUpgrade after the cluster is created. To enable AutoMinorVersionUpgrade on a cluster you must set AutoMinorVersionUpgrade to true when you create a cluster.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this cluster.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.memorydb.clusters
WHERE region = 'us-east-1'
</pre>
