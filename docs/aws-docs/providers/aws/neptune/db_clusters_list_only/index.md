---
title: db_clusters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - db_clusters_list_only
  - neptune
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

Lists <code>db_clusters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/db_clusters/"><code>db_clusters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_clusters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Neptune::DBCluster resource creates an Amazon Neptune DB cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.neptune.db_clusters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The connection endpoint for the DB cluster. For example: `mystack-mydbcluster-1apw1j4phylrk.cg034hpkmmjt.us-east-2.rds.amazonaws.com`</td></tr>
<tr><td><CopyableCode code="read_endpoint" /></td><td><code>string</code></td><td>The reader endpoint for the DB cluster. For example: `mystack-mydbcluster-ro-1apw1j4phylrk.cg034hpkmmjt.us-east-2.rds.amazonaws.com`</td></tr>
<tr><td><CopyableCode code="cluster_resource_id" /></td><td><code>string</code></td><td>The resource id for the DB cluster. For example: `cluster-ABCD1234EFGH5678IJKL90MNOP`. The cluster ID uniquely identifies the cluster and is used in things like IAM authentication policies.</td></tr>
<tr><td><CopyableCode code="associated_roles" /></td><td><code>array</code></td><td>Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.</td></tr>
<tr><td><CopyableCode code="availability_zones" /></td><td><code>array</code></td><td>Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.</td></tr>
<tr><td><CopyableCode code="backup_retention_period" /></td><td><code>integer</code></td><td>Specifies the number of days for which automatic DB snapshots are retained.</td></tr>
<tr><td><CopyableCode code="copy_tags_to_snapshot" /></td><td><code>boolean</code></td><td>A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default behaviour is not to copy them.</td></tr>
<tr><td><CopyableCode code="db_cluster_identifier" /></td><td><code>string</code></td><td>The DB cluster identifier. Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="db_cluster_parameter_group_name" /></td><td><code>string</code></td><td>Provides the name of the DB cluster parameter group.</td></tr>
<tr><td><CopyableCode code="db_instance_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB parameter group to apply to all instances of the DB cluster. Used only in case of a major EngineVersion upgrade request.</td></tr>
<tr><td><CopyableCode code="db_port" /></td><td><code>integer</code></td><td>The port number on which the DB instances in the DB cluster accept connections. <br />If not specified, the default port used is `8182`. <br />Note: `Port` property will soon be deprecated from this resource. Please update existing templates to rename it with new property `DBPort` having same functionalities.</td></tr>
<tr><td><CopyableCode code="db_subnet_group_name" /></td><td><code>string</code></td><td>Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.</td></tr>
<tr><td><CopyableCode code="deletion_protection" /></td><td><code>boolean</code></td><td>Indicates whether or not the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled.</td></tr>
<tr><td><CopyableCode code="enable_cloudwatch_logs_exports" /></td><td><code>array</code></td><td>Specifies a list of log types that are enabled for export to CloudWatch Logs.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>Indicates the database engine version.</td></tr>
<tr><td><CopyableCode code="iam_auth_enabled" /></td><td><code>boolean</code></td><td>True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>If `StorageEncrypted` is true, the Amazon KMS key identifier for the encrypted DB cluster.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>string</code></td><td>The port number on which the DB cluster accepts connections. For example: `8182`.</td></tr>
<tr><td><CopyableCode code="preferred_backup_window" /></td><td><code>string</code></td><td>Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod.</td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td>Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</td></tr>
<tr><td><CopyableCode code="restore_to_time" /></td><td><code>string</code></td><td>Creates a new DB cluster from a DB snapshot or DB cluster snapshot.<br />If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.<br />If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.</td></tr>
<tr><td><CopyableCode code="restore_type" /></td><td><code>string</code></td><td>Creates a new DB cluster from a DB snapshot or DB cluster snapshot.<br />If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.<br />If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.</td></tr>
<tr><td><CopyableCode code="serverless_scaling_configuration" /></td><td><code>object</code></td><td>Contains the scaling configuration used by the Neptune Serverless Instances within this DB cluster.</td></tr>
<tr><td><CopyableCode code="snapshot_identifier" /></td><td><code>string</code></td><td>Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.<br />After you restore a DB cluster using a SnapshotIdentifier, you must specify the same SnapshotIdentifier for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.<br />However, if you don't specify the SnapshotIdentifier, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the SnapshotIdentifier, and the original DB cluster is deleted.</td></tr>
<tr><td><CopyableCode code="source_db_cluster_identifier" /></td><td><code>string</code></td><td>Creates a new DB cluster from a DB snapshot or DB cluster snapshot.<br />If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.<br />If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.</td></tr>
<tr><td><CopyableCode code="storage_encrypted" /></td><td><code>boolean</code></td><td>Indicates whether the DB cluster is encrypted.<br />If you specify the `DBClusterIdentifier`, `DBSnapshotIdentifier`, or `SourceDBInstanceIdentifier` property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance. If you specify the KmsKeyId property, you must enable encryption.<br />If you specify the KmsKeyId, you must enable encryption by setting StorageEncrypted to true.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags assigned to this cluster.</td></tr>
<tr><td><CopyableCode code="use_latest_restorable_time" /></td><td><code>boolean</code></td><td>Creates a new DB cluster from a DB snapshot or DB cluster snapshot.<br />If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.<br />If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>Provides a list of VPC security groups that the DB cluster belongs to.</td></tr>
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
Lists all <code>db_clusters</code> in a region.
```sql
SELECT
region,
db_cluster_identifier
FROM aws.neptune.db_clusters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_clusters_list_only</code> resource, see <a href="/providers/aws/neptune/db_clusters/#permissions"><code>db_clusters</code></a>


