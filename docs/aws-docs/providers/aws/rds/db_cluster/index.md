---
title: db_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - db_cluster
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
Gets or operates on an individual <code>db_cluster</code> resource, use <code>db_clusters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>endpoint</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>read_endpoint</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>allocated_storage</code></td><td><code>integer</code></td><td>The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.</td></tr>
<tr><td><code>associated_roles</code></td><td><code>array</code></td><td>Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.</td></tr>
<tr><td><code>availability_zones</code></td><td><code>array</code></td><td>A list of Availability Zones (AZs) where instances in the DB cluster can be created. For information on AWS Regions and Availability Zones, see Choosing the Regions and Availability Zones in the Amazon Aurora User Guide.</td></tr>
<tr><td><code>auto_minor_version_upgrade</code></td><td><code>boolean</code></td><td>A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.</td></tr>
<tr><td><code>backtrack_window</code></td><td><code>integer</code></td><td>The target backtrack window, in seconds. To disable backtracking, set this value to 0.</td></tr>
<tr><td><code>backup_retention_period</code></td><td><code>integer</code></td><td>The number of days for which automated backups are retained.</td></tr>
<tr><td><code>copy_tags_to_snapshot</code></td><td><code>boolean</code></td><td>A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.</td></tr>
<tr><td><code>database_name</code></td><td><code>string</code></td><td>The name of your database. If you don't provide a name, then Amazon RDS won't create a database in this DB cluster. For naming constraints, see Naming Constraints in the Amazon RDS User Guide.</td></tr>
<tr><td><code>db_cluster_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the DB cluster.</td></tr>
<tr><td><code>db_cluster_instance_class</code></td><td><code>string</code></td><td>The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.</td></tr>
<tr><td><code>db_cluster_resource_id</code></td><td><code>string</code></td><td>The AWS Region-unique, immutable identifier for the DB cluster.</td></tr>
<tr><td><code>db_instance_parameter_group_name</code></td><td><code>string</code></td><td>The name of the DB parameter group to apply to all instances of the DB cluster.</td></tr>
<tr><td><code>db_system_id</code></td><td><code>string</code></td><td>Reserved for future use.</td></tr>
<tr><td><code>global_cluster_identifier</code></td><td><code>string</code></td><td>If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;If you aren't configuring a global database cluster, don't specify this property.</td></tr>
<tr><td><code>db_cluster_identifier</code></td><td><code>string</code></td><td>The DB cluster identifier. This parameter is stored as a lowercase string.</td></tr>
<tr><td><code>db_cluster_parameter_group_name</code></td><td><code>string</code></td><td>The name of the DB cluster parameter group to associate with this DB cluster.</td></tr>
<tr><td><code>db_subnet_group_name</code></td><td><code>string</code></td><td>A DB subnet group that you want to associate with this DB cluster.</td></tr>
<tr><td><code>deletion_protection</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.</td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td>The Active Directory directory ID to create the DB cluster in.</td></tr>
<tr><td><code>domain_iam_role_name</code></td><td><code>string</code></td><td>Specify the name of the IAM role to be used when making API calls to the Directory Service.</td></tr>
<tr><td><code>enable_cloudwatch_logs_exports</code></td><td><code>array</code></td><td>The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.</td></tr>
<tr><td><code>enable_global_write_forwarding</code></td><td><code>boolean</code></td><td>Specifies whether to enable this DB cluster to forward write operations to the primary cluster of a global cluster (Aurora global database). By default, write operations are not allowed on Aurora DB clusters that are secondary clusters in an Aurora global database.</td></tr>
<tr><td><code>enable_http_endpoint</code></td><td><code>boolean</code></td><td>A value that indicates whether to enable the HTTP endpoint for DB cluster. By default, the HTTP endpoint is disabled.</td></tr>
<tr><td><code>enable_iam_database_authentication</code></td><td><code>boolean</code></td><td>A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.</td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td>The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql</td></tr>
<tr><td><code>engine_mode</code></td><td><code>string</code></td><td>The DB engine mode of the DB cluster, either provisioned, serverless, parallelquery, global, or multimaster.</td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td>The version number of the database engine to use.</td></tr>
<tr><td><code>manage_master_user_password</code></td><td><code>boolean</code></td><td>A value that indicates whether to manage the master user password with AWS Secrets Manager.</td></tr>
<tr><td><code>iops</code></td><td><code>integer</code></td><td>The amount of Provisioned IOPS (input&#x2F;output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS Key Management Service master key that is used to encrypt the database instances in the DB cluster, such as arn:aws:kms:us-east-1:012345678910:key&#x2F;abcd1234-a123-456a-a12b-a123b4cd56ef. If you enable the StorageEncrypted property but don't specify this property, the default master key is used. If you specify this property, you must set the StorageEncrypted property to true.</td></tr>
<tr><td><code>master_username</code></td><td><code>string</code></td><td>The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.</td></tr>
<tr><td><code>master_user_password</code></td><td><code>string</code></td><td>The master password for the DB instance.</td></tr>
<tr><td><code>master_user_secret</code></td><td><code>object</code></td><td>Contains the secret managed by RDS in AWS Secrets Manager for the master user password.</td></tr>
<tr><td><code>monitoring_interval</code></td><td><code>integer</code></td><td>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.</td></tr>
<tr><td><code>monitoring_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.</td></tr>
<tr><td><code>network_type</code></td><td><code>string</code></td><td>The network type of the DB cluster.</td></tr>
<tr><td><code>performance_insights_enabled</code></td><td><code>boolean</code></td><td>A value that indicates whether to turn on Performance Insights for the DB cluster.</td></tr>
<tr><td><code>performance_insights_kms_key_id</code></td><td><code>string</code></td><td>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</td></tr>
<tr><td><code>performance_insights_retention_period</code></td><td><code>integer</code></td><td>The amount of time, in days, to retain Performance Insights data.</td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td>The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.</td></tr>
<tr><td><code>preferred_backup_window</code></td><td><code>string</code></td><td>The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.</td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.</td></tr>
<tr><td><code>publicly_accessible</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB cluster is publicly accessible.</td></tr>
<tr><td><code>replication_source_identifier</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.</td></tr>
<tr><td><code>restore_to_time</code></td><td><code>string</code></td><td>The date and time to restore the DB cluster to. Value must be a time in Universal Coordinated Time (UTC) format. An example: 2015-03-07T23:45:00Z</td></tr>
<tr><td><code>restore_type</code></td><td><code>string</code></td><td>The type of restore to be performed. You can specify one of the following values:&lt;br&#x2F;&gt;full-copy - The new DB cluster is restored as a full copy of the source DB cluster.&lt;br&#x2F;&gt;copy-on-write - The new DB cluster is restored as a clone of the source DB cluster.</td></tr>
<tr><td><code>serverless_v2_scaling_configuration</code></td><td><code>object</code></td><td>Contains the scaling configuration of an Aurora Serverless v2 DB cluster.</td></tr>
<tr><td><code>scaling_configuration</code></td><td><code>object</code></td><td>The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.</td></tr>
<tr><td><code>snapshot_identifier</code></td><td><code>string</code></td><td>The identifier for the DB snapshot or DB cluster snapshot to restore from.&lt;br&#x2F;&gt;You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.&lt;br&#x2F;&gt;After you restore a DB cluster with a SnapshotIdentifier property, you must specify the same SnapshotIdentifier property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the SnapshotIdentifier property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the specified SnapshotIdentifier property, and the original DB cluster is deleted.</td></tr>
<tr><td><code>source_db_cluster_identifier</code></td><td><code>string</code></td><td>The identifier of the source DB cluster from which to restore.</td></tr>
<tr><td><code>source_region</code></td><td><code>string</code></td><td>The AWS Region which contains the source DB cluster when replicating a DB cluster. For example, us-east-1.</td></tr>
<tr><td><code>storage_encrypted</code></td><td><code>boolean</code></td><td>Indicates whether the DB instance is encrypted.&lt;br&#x2F;&gt;If you specify the DBClusterIdentifier, SnapshotIdentifier, or SourceDBInstanceIdentifier property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance.</td></tr>
<tr><td><code>storage_throughput</code></td><td><code>integer</code></td><td>Specifies the storage throughput value for the DB cluster. This setting applies only to the gp3 storage type.</td></tr>
<tr><td><code>storage_type</code></td><td><code>string</code></td><td>Specifies the storage type to be associated with the DB cluster.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>use_latest_restorable_time</code></td><td><code>boolean</code></td><td>A value that indicates whether to restore the DB cluster to the latest restorable backup time. By default, the DB cluster is not restored to the latest restorable backup time.</td></tr>
<tr><td><code>vpc_security_group_ids</code></td><td><code>array</code></td><td>A list of EC2 VPC security groups to associate with this DB cluster.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
endpoint,
read_endpoint,
allocated_storage,
associated_roles,
availability_zones,
auto_minor_version_upgrade,
backtrack_window,
backup_retention_period,
copy_tags_to_snapshot,
database_name,
db_cluster_arn,
db_cluster_instance_class,
db_cluster_resource_id,
db_instance_parameter_group_name,
db_system_id,
global_cluster_identifier,
db_cluster_identifier,
db_cluster_parameter_group_name,
db_subnet_group_name,
deletion_protection,
domain,
domain_iam_role_name,
enable_cloudwatch_logs_exports,
enable_global_write_forwarding,
enable_http_endpoint,
enable_iam_database_authentication,
engine,
engine_mode,
engine_version,
manage_master_user_password,
iops,
kms_key_id,
master_username,
master_user_password,
master_user_secret,
monitoring_interval,
monitoring_role_arn,
network_type,
performance_insights_enabled,
performance_insights_kms_key_id,
performance_insights_retention_period,
port,
preferred_backup_window,
preferred_maintenance_window,
publicly_accessible,
replication_source_identifier,
restore_to_time,
restore_type,
serverless_v2_scaling_configuration,
scaling_configuration,
snapshot_identifier,
source_db_cluster_identifier,
source_region,
storage_encrypted,
storage_throughput,
storage_type,
tags,
use_latest_restorable_time,
vpc_security_group_ids
FROM aws.rds.db_cluster
WHERE data__Identifier = '<DBClusterIdentifier>';
```

## Permissions

To operate on the <code>db_cluster</code> resource, the following permissions are required:

### Read
```json
rds:DescribeDBClusters
```

### Update
```json
ec2:DescribeSecurityGroups,
iam:PassRole,
rds:AddRoleToDBCluster,
rds:AddTagsToResource,
rds:DescribeDBClusters,
rds:DescribeDBSubnetGroups,
rds:DescribeEvents,
rds:DescribeGlobalClusters,
rds:DisableHttpEndpoint,
rds:EnableHttpEndpoint,
rds:ModifyDBCluster,
rds:ModifyDBInstance,
rds:RemoveFromGlobalCluster,
rds:RemoveRoleFromDBCluster,
rds:RemoveTagsFromResource,
secretsmanager:CreateSecret,
secretsmanager:TagResource
```

### Delete
```json
rds:CreateDBClusterSnapshot,
rds:DeleteDBCluster,
rds:DeleteDBInstance,
rds:DescribeDBClusters,
rds:DescribeGlobalClusters,
rds:RemoveFromGlobalCluster
```

