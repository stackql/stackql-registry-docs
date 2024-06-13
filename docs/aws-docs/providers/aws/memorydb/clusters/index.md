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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>cluster</code> resource or lists <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::Cluster resource creates an Amazon MemoryDB Cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.clusters" /></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ClusterName, NodeType, ACLName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>clusters</code> in a region.
```sql
SELECT
region,
cluster_name
FROM aws.memorydb.clusters
WHERE region = 'us-east-1';
```
Gets all properties from a <code>cluster</code>.
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
FROM aws.memorydb.clusters
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.memorydb.clusters (
 ClusterName,
 NodeType,
 ACLName,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ NodeType }}',
 '{{ ACLName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.memorydb.clusters (
 ClusterName,
 Description,
 NodeType,
 NumShards,
 NumReplicasPerShard,
 SubnetGroupName,
 SecurityGroupIds,
 MaintenanceWindow,
 ParameterGroupName,
 Port,
 SnapshotRetentionLimit,
 SnapshotWindow,
 ACLName,
 SnsTopicArn,
 SnsTopicStatus,
 TLSEnabled,
 DataTiering,
 KmsKeyId,
 SnapshotArns,
 SnapshotName,
 FinalSnapshotName,
 EngineVersion,
 ClusterEndpoint,
 AutoMinorVersionUpgrade,
 Tags,
 region
)
SELECT 
 '{{ ClusterName }}',
 '{{ Description }}',
 '{{ NodeType }}',
 '{{ NumShards }}',
 '{{ NumReplicasPerShard }}',
 '{{ SubnetGroupName }}',
 '{{ SecurityGroupIds }}',
 '{{ MaintenanceWindow }}',
 '{{ ParameterGroupName }}',
 '{{ Port }}',
 '{{ SnapshotRetentionLimit }}',
 '{{ SnapshotWindow }}',
 '{{ ACLName }}',
 '{{ SnsTopicArn }}',
 '{{ SnsTopicStatus }}',
 '{{ TLSEnabled }}',
 '{{ DataTiering }}',
 '{{ KmsKeyId }}',
 '{{ SnapshotArns }}',
 '{{ SnapshotName }}',
 '{{ FinalSnapshotName }}',
 '{{ EngineVersion }}',
 '{{ ClusterEndpoint }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: cluster
    props:
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: Description
        value: '{{ Description }}'
      - name: NodeType
        value: '{{ NodeType }}'
      - name: NumShards
        value: '{{ NumShards }}'
      - name: NumReplicasPerShard
        value: '{{ NumReplicasPerShard }}'
      - name: SubnetGroupName
        value: '{{ SubnetGroupName }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: MaintenanceWindow
        value: '{{ MaintenanceWindow }}'
      - name: ParameterGroupName
        value: '{{ ParameterGroupName }}'
      - name: Port
        value: '{{ Port }}'
      - name: SnapshotRetentionLimit
        value: '{{ SnapshotRetentionLimit }}'
      - name: SnapshotWindow
        value: '{{ SnapshotWindow }}'
      - name: ACLName
        value: '{{ ACLName }}'
      - name: SnsTopicArn
        value: '{{ SnsTopicArn }}'
      - name: SnsTopicStatus
        value: '{{ SnsTopicStatus }}'
      - name: TLSEnabled
        value: '{{ TLSEnabled }}'
      - name: DataTiering
        value: '{{ DataTiering }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: SnapshotArns
        value:
          - '{{ SnapshotArns[0] }}'
      - name: SnapshotName
        value: '{{ SnapshotName }}'
      - name: FinalSnapshotName
        value: '{{ FinalSnapshotName }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: ClusterEndpoint
        value:
          Address: '{{ Address }}'
          Port: '{{ Port }}'
      - name: AutoMinorVersionUpgrade
        value: '{{ AutoMinorVersionUpgrade }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.memorydb.clusters
WHERE data__Identifier = '<ClusterName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
```json
memorydb:CreateCluster,
memorydb:DescribeClusters,
memorydb:ListTags
```

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

### List
```json
memorydb:DescribeClusters
```

