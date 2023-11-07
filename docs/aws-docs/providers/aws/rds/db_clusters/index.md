---
title: db_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - db_clusters
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
Retrieves a list of <code>db_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.rds.db_clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Endpoint</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ReadEndpoint</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AllocatedStorage</code></td><td><code>integer</code></td><td>The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.</td></tr>
<tr><td><code>AssociatedRoles</code></td><td><code>array</code></td><td>Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.</td></tr>
<tr><td><code>AvailabilityZones</code></td><td><code>array</code></td><td>A list of Availability Zones (AZs) where instances in the DB cluster can be created. For information on AWS Regions and Availability Zones, see Choosing the Regions and Availability Zones in the Amazon Aurora User Guide.</td></tr>
<tr><td><code>AutoMinorVersionUpgrade</code></td><td><code>boolean</code></td><td>A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.</td></tr>
<tr><td><code>BacktrackWindow</code></td><td><code>integer</code></td><td>The target backtrack window, in seconds. To disable backtracking, set this value to 0.</td></tr>
<tr><td><code>BackupRetentionPeriod</code></td><td><code>integer</code></td><td>The number of days for which automated backups are retained.</td></tr>
<tr><td><code>CopyTagsToSnapshot</code></td><td><code>boolean</code></td><td>A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.</td></tr>
<tr><td><code>DatabaseName</code></td><td><code>string</code></td><td>The name of your database. If you don't provide a name, then Amazon RDS won't create a database in this DB cluster. For naming constraints, see Naming Constraints in the Amazon RDS User Guide.</td></tr>
<tr><td><code>DBClusterArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the DB cluster.</td></tr>
<tr><td><code>DBClusterInstanceClass</code></td><td><code>string</code></td><td>The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.</td></tr>
<tr><td><code>DBClusterResourceId</code></td><td><code>string</code></td><td>The AWS Region-unique, immutable identifier for the DB cluster.</td></tr>
<tr><td><code>DBInstanceParameterGroupName</code></td><td><code>string</code></td><td>The name of the DB parameter group to apply to all instances of the DB cluster.</td></tr>
<tr><td><code>DBSystemId</code></td><td><code>string</code></td><td>Reserved for future use.</td></tr>
<tr><td><code>GlobalClusterIdentifier</code></td><td><code>string</code></td><td>If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;If you aren't configuring a global database cluster, don't specify this property.</td></tr>
<tr><td><code>DBClusterIdentifier</code></td><td><code>string</code></td><td>The DB cluster identifier. This parameter is stored as a lowercase string.</td></tr>
<tr><td><code>DBClusterParameterGroupName</code></td><td><code>string</code></td><td>The name of the DB cluster parameter group to associate with this DB cluster.</td></tr>
<tr><td><code>DBSubnetGroupName</code></td><td><code>string</code></td><td>A DB subnet group that you want to associate with this DB cluster.</td></tr>
<tr><td><code>DeletionProtection</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.</td></tr>
<tr><td><code>Domain</code></td><td><code>string</code></td><td>The Active Directory directory ID to create the DB cluster in.</td></tr>
<tr><td><code>DomainIAMRoleName</code></td><td><code>string</code></td><td>Specify the name of the IAM role to be used when making API calls to the Directory Service.</td></tr>
<tr><td><code>EnableCloudwatchLogsExports</code></td><td><code>array</code></td><td>The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.</td></tr>
<tr><td><code>EnableHttpEndpoint</code></td><td><code>boolean</code></td><td>A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.</td></tr>
<tr><td><code>EnableIAMDatabaseAuthentication</code></td><td><code>boolean</code></td><td>A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.</td></tr>
<tr><td><code>Engine</code></td><td><code>string</code></td><td>The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql</td></tr>
<tr><td><code>EngineMode</code></td><td><code>string</code></td><td>The DB engine mode of the DB cluster, either provisioned, serverless, parallelquery, global, or multimaster.</td></tr>
<tr><td><code>EngineVersion</code></td><td><code>string</code></td><td>The version number of the database engine to use.</td></tr>
<tr><td><code>ManageMasterUserPassword</code></td><td><code>boolean</code></td><td>A value that indicates whether to manage the master user password with AWS Secrets Manager.</td></tr>
<tr><td><code>Iops</code></td><td><code>integer</code></td><td>The amount of Provisioned IOPS (input&#x2F;output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS Key Management Service master key that is used to encrypt the database instances in the DB cluster, such as arn:aws:kms:us-east-1:012345678910:key&#x2F;abcd1234-a123-456a-a12b-a123b4cd56ef. If you enable the StorageEncrypted property but don't specify this property, the default master key is used. If you specify this property, you must set the StorageEncrypted property to true.</td></tr>
<tr><td><code>MasterUsername</code></td><td><code>string</code></td><td>The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.</td></tr>
<tr><td><code>MasterUserPassword</code></td><td><code>string</code></td><td>The master password for the DB instance.</td></tr>
<tr><td><code>MasterUserSecret</code></td><td><code>undefined</code></td><td>Contains the secret managed by RDS in AWS Secrets Manager for the master user password.</td></tr>
<tr><td><code>MonitoringInterval</code></td><td><code>integer</code></td><td>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.</td></tr>
<tr><td><code>MonitoringRoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.</td></tr>
<tr><td><code>NetworkType</code></td><td><code>string</code></td><td>The network type of the DB cluster.</td></tr>
<tr><td><code>PerformanceInsightsEnabled</code></td><td><code>boolean</code></td><td>A value that indicates whether to turn on Performance Insights for the DB cluster.</td></tr>
<tr><td><code>PerformanceInsightsKmsKeyId</code></td><td><code>string</code></td><td>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</td></tr>
<tr><td><code>PerformanceInsightsRetentionPeriod</code></td><td><code>integer</code></td><td>The amount of time, in days, to retain Performance Insights data.</td></tr>
<tr><td><code>Port</code></td><td><code>integer</code></td><td>The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.</td></tr>
<tr><td><code>PreferredBackupWindow</code></td><td><code>string</code></td><td>The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.</td></tr>
<tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.</td></tr>
<tr><td><code>PubliclyAccessible</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB cluster is publicly accessible.</td></tr>
<tr><td><code>ReplicationSourceIdentifier</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.</td></tr>
<tr><td><code>RestoreToTime</code></td><td><code>string</code></td><td>The date and time to restore the DB cluster to. Value must be a time in Universal Coordinated Time (UTC) format. An example: 2015-03-07T23:45:00Z</td></tr>
<tr><td><code>RestoreType</code></td><td><code>string</code></td><td>The type of restore to be performed. You can specify one of the following values:&lt;br&#x2F;&gt;full-copy - The new DB cluster is restored as a full copy of the source DB cluster.&lt;br&#x2F;&gt;copy-on-write - The new DB cluster is restored as a clone of the source DB cluster.</td></tr>
<tr><td><code>ServerlessV2ScalingConfiguration</code></td><td><code>undefined</code></td><td>Contains the scaling configuration of an Aurora Serverless v2 DB cluster.</td></tr>
<tr><td><code>ScalingConfiguration</code></td><td><code>undefined</code></td><td>The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.</td></tr>
<tr><td><code>SnapshotIdentifier</code></td><td><code>string</code></td><td>The identifier for the DB snapshot or DB cluster snapshot to restore from.&lt;br&#x2F;&gt;You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.&lt;br&#x2F;&gt;After you restore a DB cluster with a SnapshotIdentifier property, you must specify the same SnapshotIdentifier property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the SnapshotIdentifier property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the specified SnapshotIdentifier property, and the original DB cluster is deleted.</td></tr>
<tr><td><code>SourceDBClusterIdentifier</code></td><td><code>string</code></td><td>The identifier of the source DB cluster from which to restore.</td></tr>
<tr><td><code>SourceRegion</code></td><td><code>string</code></td><td>The AWS Region which contains the source DB cluster when replicating a DB cluster. For example, us-east-1.</td></tr>
<tr><td><code>StorageEncrypted</code></td><td><code>boolean</code></td><td>Indicates whether the DB instance is encrypted.&lt;br&#x2F;&gt;If you specify the DBClusterIdentifier, SnapshotIdentifier, or SourceDBInstanceIdentifier property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance.</td></tr>
<tr><td><code>StorageType</code></td><td><code>string</code></td><td>Specifies the storage type to be associated with the DB cluster.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>UseLatestRestorableTime</code></td><td><code>boolean</code></td><td>A value that indicates whether to restore the DB cluster to the latest restorable backup time. By default, the DB cluster is not restored to the latest restorable backup time.</td></tr>
<tr><td><code>VpcSecurityGroupIds</code></td><td><code>array</code></td><td>A list of EC2 VPC security groups to associate with this DB cluster.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.rds.db_clusters
WHERE region = 'us-east-1'
</pre>
