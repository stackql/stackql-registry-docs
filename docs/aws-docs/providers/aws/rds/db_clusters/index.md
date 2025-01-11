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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>db_cluster</code> resource or lists <code>db_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBCluster</code> resource creates an Amazon Aurora DB cluster or Multi-AZ DB cluster.<br />For more information about creating an Aurora DB cluster, see &#91;Creating an Amazon Aurora DB cluster&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the *Amazon Aurora User Guide*.<br />For more information about creating a Multi-AZ DB cluster, see &#91;Creating a Multi-AZ DB cluster&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html) in the *Amazon RDS User Guide*.<br />You can only create this resource in AWS Regions where Amazon Aurora or Multi-AZ DB clusters are supported.<br />*Updating DB clusters* <br />When properties labeled "*Update requires:* &#91;Replacement&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)" are updated, AWS CloudFormation first creates a replacement DB cluster, then changes references from other dependent resources to point to the replacement DB cluster, and finally deletes the old DB cluster.<br />We highly recommend that you take a snapshot of the database before updating the stack. If you don't, you lose the data when AWS CloudFormation replaces your DB cluster. To preserve your data, perform the following procedure:<br />1. Deactivate any applications that are using the DB cluster so that there's no activity on the DB instance.<br />1. Create a snapshot of the DB cluster. For more information, see &#91;Creating a DB cluster snapshot&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CreateSnapshotCluster.html).<br />1. If you want to restore your DB cluster using a DB cluster snapshot, modify the updated template with your DB cluster changes and add the <code>SnapshotIdentifier</code> property with the ID of the DB cluster snapshot that you want to use.<br />After you restore a DB cluster with a <code>SnapshotIdentifier</code> property, you must specify the same <code>SnapshotIdentifier</code> property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the DB cluster snapshot again, and the data in the database is not changed. However, if you don't specify the <code>SnapshotIdentifier</code> property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, a new DB cluster is restored from the specified <code>SnapshotIdentifier</code> property, and the original DB cluster is deleted.<br />1. Update the stack.<br /><br />Currently, when you are updating the stack for an Aurora Serverless DB cluster, you can't include changes to any other properties when you specify one of the following properties: <code>PreferredBackupWindow</code>, <code>PreferredMaintenanceWindow</code>, and <code>Port</code>. This limitation doesn't apply to provisioned DB clusters.<br />For more information about updating other properties of this resource, see <code>ModifyDBCluster</code>. For more information about updating stacks, see &#91;CloudFormation Stacks Updates&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html).<br />*Deleting DB clusters* <br />The default <code>DeletionPolicy</code> for <code>AWS::RDS::DBCluster</code> resources is <code>Snapshot</code>. For more information about how AWS CloudFormation deletes resources, see &#91;DeletionPolicy Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="endpoint" /></td><td><code>object</code></td><td>This data type represents the information you need to connect to an Amazon RDS DB instance. This data type is used as a response element in the following actions:<br />+ <code>CreateDBInstance</code> <br />+ <code>DescribeDBInstances</code> <br />+ <code>DeleteDBInstance</code> <br /><br />For the data structure that represents Amazon Aurora DB cluster endpoints, see <code>DBClusterEndpoint</code>.</td></tr>
<tr><td><CopyableCode code="read_endpoint" /></td><td><code>object</code></td><td>This data type represents the information you need to connect to an Amazon RDS DB instance. This data type is used as a response element in the following actions:<br />+ <code>CreateDBInstance</code> <br />+ <code>DescribeDBInstances</code> <br />+ <code>DeleteDBInstance</code> <br /><br />For the data structure that represents Amazon Aurora DB cluster endpoints, see <code>DBClusterEndpoint</code>.</td></tr>
<tr><td><CopyableCode code="allocated_storage" /></td><td><code>integer</code></td><td>The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.<br />Valid for Cluster Type: Multi-AZ DB clusters only<br />This setting is required to create a Multi-AZ DB cluster.</td></tr>
<tr><td><CopyableCode code="associated_roles" /></td><td><code>array</code></td><td>Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon Web Services on your behalf.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="availability_zones" /></td><td><code>array</code></td><td>A list of Availability Zones (AZs) where instances in the DB cluster can be created. For information on AWS Regions and Availability Zones, see &#91;Choosing the Regions and Availability Zones&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html) in the *Amazon Aurora User Guide*. <br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="auto_minor_version_upgrade" /></td><td><code>boolean</code></td><td>Specifies whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.<br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB cluster</td></tr>
<tr><td><CopyableCode code="backtrack_window" /></td><td><code>integer</code></td><td>The target backtrack window, in seconds. To disable backtracking, set this value to <code>0</code>.<br />Valid for Cluster Type: Aurora MySQL DB clusters only<br />Default: <code>0</code> <br />Constraints:<br />+ If specified, this value must be set to a number from 0 to 259,200 (72 hours).</td></tr>
<tr><td><CopyableCode code="backup_retention_period" /></td><td><code>integer</code></td><td>The number of days for which automated backups are retained.<br />Default: 1<br />Constraints:<br />+ Must be a value from 1 to 35<br /><br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="cluster_scalability_type" /></td><td><code>string</code></td><td>Specifies the scalability mode of the Aurora DB cluster. When set to <code>limitless</code>, the cluster operates as an Aurora Limitless Database, allowing you to create a DB shard group for horizontal scaling (sharding) capabilities. When set to <code>standard</code> (the default), the cluster uses normal DB instance creation.</td></tr>
<tr><td><CopyableCode code="copy_tags_to_snapshot" /></td><td><code>boolean</code></td><td>A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="database_insights_mode" /></td><td><code>string</code></td><td>The mode of Database Insights to enable for the DB cluster.<br />If you set this value to <code>advanced</code>, you must also set the <code>PerformanceInsightsEnabled</code> parameter to <code>true</code> and the <code>PerformanceInsightsRetentionPeriod</code> parameter to 465.<br />Valid for Cluster Type: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name of your database. If you don't provide a name, then Amazon RDS won't create a database in this DB cluster. For naming constraints, see &#91;Naming Constraints&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html#RDS_Limits.Constraints) in the *Amazon Aurora User Guide*. <br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="db_cluster_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="db_cluster_instance_class" /></td><td><code>string</code></td><td>The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example <code>db.m6gd.xlarge</code>. Not all DB instance classes are available in all AWS-Regions, or for all database engines.<br />For the full list of DB instance classes and availability for your engine, see &#91;DB instance class&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.<br />This setting is required to create a Multi-AZ DB cluster.<br />Valid for Cluster Type: Multi-AZ DB clusters only</td></tr>
<tr><td><CopyableCode code="db_cluster_resource_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="db_instance_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB parameter group to apply to all instances of the DB cluster.<br />When you apply a parameter group using the <code>DBInstanceParameterGroupName</code> parameter, the DB cluster isn't rebooted automatically. Also, parameter changes are applied immediately rather than during the next maintenance window.<br />Valid for Cluster Type: Aurora DB clusters only<br />Default: The existing name setting<br />Constraints:<br />+ The DB parameter group must be in the same DB parameter group family as this DB cluster.<br />+ The <code>DBInstanceParameterGroupName</code> parameter is valid in combination with the <code>AllowMajorVersionUpgrade</code> parameter for a major version upgrade only.</td></tr>
<tr><td><CopyableCode code="db_system_id" /></td><td><code>string</code></td><td>Reserved for future use.</td></tr>
<tr><td><CopyableCode code="global_cluster_identifier" /></td><td><code>string</code></td><td>If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the &#91;AWS::RDS::GlobalCluster&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html) resource. <br />If you aren't configuring a global database cluster, don't specify this property. <br />To remove the DB cluster from a global database cluster, specify an empty value for the <code>GlobalClusterIdentifier</code> property.<br />For information about Aurora global databases, see &#91;Working with Amazon Aurora Global Databases&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) in the *Amazon Aurora User Guide*.<br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="db_cluster_identifier" /></td><td><code>string</code></td><td>The DB cluster identifier. This parameter is stored as a lowercase string.<br />Constraints:<br />+ Must contain from 1 to 63 letters, numbers, or hyphens.<br />+ First character must be a letter.<br />+ Can't end with a hyphen or contain two consecutive hyphens.<br /><br />Example: <code>my-cluster1</code> <br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="db_cluster_parameter_group_name" /></td><td><code>string</code></td><td>The name of the DB cluster parameter group to associate with this DB cluster.<br />If you apply a parameter group to an existing DB cluster, then its DB instances might need to reboot. This can result in an outage while the DB instances are rebooting.<br />If you apply a change to parameter group associated with a stopped DB cluster, then the update stack waits until the DB cluster is started.<br />To list all of the available DB cluster parameter group names, use the following command:<br /><code>aws rds describe-db-cluster-parameter-groups --query "DBClusterParameterGroups&#91;&#93;.DBClusterParameterGroupName" --output text</code> <br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="db_subnet_group_name" /></td><td><code>string</code></td><td>A DB subnet group that you want to associate with this DB cluster. <br />If you are restoring a DB cluster to a point in time with <code>RestoreType</code> set to <code>copy-on-write</code>, and don't specify a DB subnet group name, then the DB cluster is restored with a default DB subnet group.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="deletion_protection" /></td><td><code>boolean</code></td><td>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>Indicates the directory ID of the Active Directory to create the DB cluster.<br />For Amazon Aurora DB clusters, Amazon RDS can use Kerberos authentication to authenticate users that connect to the DB cluster.<br />For more information, see &#91;Kerberos authentication&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/kerberos-authentication.html) in the *Amazon Aurora User Guide*.<br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="domain_iam_role_name" /></td><td><code>string</code></td><td>Specifies the name of the IAM role to use when making API calls to the Directory Service.<br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="enable_cloudwatch_logs_exports" /></td><td><code>array</code></td><td>The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see &#91;Publishing Database Logs to Amazon CloudWatch Logs&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Aurora User Guide*.<br />*Aurora MySQL* <br />Valid values: <code>audit</code>, <code>error</code>, <code>general</code>, <code>slowquery</code> <br />*Aurora PostgreSQL* <br />Valid values: <code>postgresql</code> <br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="enable_global_write_forwarding" /></td><td><code>boolean</code></td><td>Specifies whether to enable this DB cluster to forward write operations to the primary cluster of a global cluster (Aurora global database). By default, write operations are not allowed on Aurora DB clusters that are secondary clusters in an Aurora global database.<br />You can set this value only on Aurora DB clusters that are members of an Aurora global database. With this parameter enabled, a secondary cluster can forward writes to the current primary cluster, and the resulting changes are replicated back to this cluster. For the primary DB cluster of an Aurora global database, this value is used immediately if the primary is demoted by a global cluster API operation, but it does nothing until then.<br />Valid for Cluster Type: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="enable_http_endpoint" /></td><td><code>boolean</code></td><td>Specifies whether to enable the HTTP endpoint for the DB cluster. By default, the HTTP endpoint isn't enabled.<br />When enabled, the HTTP endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the DB cluster. You can also query your database from inside the RDS console with the RDS query editor.<br />For more information, see &#91;Using RDS Data API&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.<br />Valid for Cluster Type: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="enable_iam_database_authentication" /></td><td><code>boolean</code></td><td>A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.<br />For more information, see &#91;IAM Database Authentication&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon Aurora User Guide.* <br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="enable_local_write_forwarding" /></td><td><code>boolean</code></td><td>Specifies whether read replicas can forward write operations to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.<br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The name of the database engine to be used for this DB cluster.<br />Valid Values:<br />+ <code>aurora-mysql</code> <br />+ <code>aurora-postgresql</code> <br />+ <code>mysql</code> <br />+ <code>postgres</code> <br /><br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="engine_lifecycle_support" /></td><td><code>string</code></td><td>The life cycle type for this DB cluster.<br />By default, this value is set to <code>open-source-rds-extended-support</code>, which enrolls your DB cluster into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to <code>open-source-rds-extended-support-disabled</code>. In this case, creating the DB cluster will fail if the DB major version is past its end of standard support date.<br />You can use this setting to enroll your DB cluster into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB cluster past the end of standard support for that engine version. For more information, see the following sections:<br />+ Amazon Aurora - &#91;Using Amazon RDS Extended Support&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html) in the *Amazon Aurora User Guide* <br />+ Amazon RDS - &#91;Using Amazon RDS Extended Support&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide* <br /><br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters<br />Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> <br />Default: <code>open-source-rds-extended-support</code></td></tr>
<tr><td><CopyableCode code="engine_mode" /></td><td><code>string</code></td><td>The DB engine mode of the DB cluster, either <code>provisioned</code> or <code>serverless</code>.<br />The <code>serverless</code> engine mode only applies for Aurora Serverless v1 DB clusters. Aurora Serverless v2 DB clusters use the <code>provisioned</code> engine mode.<br />For information about limitations and requirements for Serverless DB clusters, see the following sections in the *Amazon Aurora User Guide*:<br />+ &#91;Limitations of Aurora Serverless v1&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html#aurora-serverless.limitations) <br />+ &#91;Requirements for Aurora Serverless v2&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.html) <br /><br />Valid for Cluster Type: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The version number of the database engine to use.<br />To list all of the available engine versions for Aurora MySQL version 2 (5.7-compatible) and version 3 (8.0-compatible), use the following command:<br /><code>aws rds describe-db-engine-versions --engine aurora-mysql --query "DBEngineVersions&#91;&#93;.EngineVersion"</code> <br />You can supply either <code>5.7</code> or <code>8.0</code> to use the default engine version for Aurora MySQL version 2 or version 3, respectively.<br />To list all of the available engine versions for Aurora PostgreSQL, use the following command:<br /><code>aws rds describe-db-engine-versions --engine aurora-postgresql --query "DBEngineVersions&#91;&#93;.EngineVersion"</code> <br />To list all of the available engine versions for RDS for MySQL, use the following command:<br /><code>aws rds describe-db-engine-versions --engine mysql --query "DBEngineVersions&#91;&#93;.EngineVersion"</code> <br />To list all of the available engine versions for RDS for PostgreSQL, use the following command:<br /><code>aws rds describe-db-engine-versions --engine postgres --query "DBEngineVersions&#91;&#93;.EngineVersion"</code> <br />*Aurora MySQL* <br />For information, see &#91;Database engine updates for Amazon Aurora MySQL&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) in the *Amazon Aurora User Guide*.<br />*Aurora PostgreSQL* <br />For information, see &#91;Amazon Aurora PostgreSQL releases and engine versions&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html) in the *Amazon Aurora User Guide*.<br />*MySQL* <br />For information, see &#91;Amazon RDS for MySQL&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt) in the *Amazon RDS User Guide*.<br />*PostgreSQL* <br />For information, see &#91;Amazon RDS for PostgreSQL&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts) in the *Amazon RDS User Guide*.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="manage_master_user_password" /></td><td><code>boolean</code></td><td>Specifies whether to manage the master user password with AWS Secrets Manager.<br />For more information, see &#91;Password management with Secrets Manager&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and &#91;Password management with Secrets Manager&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.* <br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters<br />Constraints:<br />+ Can't manage the master user password with AWS Secrets Manager if <code>MasterUserPassword</code> is specified.</td></tr>
<tr><td><CopyableCode code="iops" /></td><td><code>integer</code></td><td>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.<br />For information about valid IOPS values, see &#91;Provisioned IOPS storage&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS) in the *Amazon RDS User Guide*.<br />This setting is required to create a Multi-AZ DB cluster.<br />Valid for Cluster Type: Multi-AZ DB clusters only<br />Constraints:<br />+ Must be a multiple between .5 and 50 of the storage amount for the DB cluster.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt the database instances in the DB cluster, such as <code>arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef</code>. If you enable the <code>StorageEncrypted</code> property but don't specify this property, the default KMS key is used. If you specify this property, you must set the <code>StorageEncrypted</code> property to <code>true</code>.<br />If you specify the <code>SnapshotIdentifier</code> property, the <code>StorageEncrypted</code> property value is inherited from the snapshot, and if the DB cluster is encrypted, the specified <code>KmsKeyId</code> property is used.<br />If you create a read replica of an encrypted DB cluster in another AWS Region, make sure to set <code>KmsKeyId</code> to a KMS key identifier that is valid in the destination AWS Region. This KMS key is used to encrypt the read replica in that AWS Region.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="master_username" /></td><td><code>string</code></td><td>The name of the master user for the DB cluster.<br />If you specify the <code>SourceDBClusterIdentifier</code>, <code>SnapshotIdentifier</code>, or <code>GlobalClusterIdentifier</code> property, don't specify this property. The value is inherited from the source DB cluster, the snapshot, or the primary DB cluster for the global database cluster, respectively.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="master_user_password" /></td><td><code>string</code></td><td>The master password for the DB instance.<br />If you specify the <code>SourceDBClusterIdentifier</code>, <code>SnapshotIdentifier</code>, or <code>GlobalClusterIdentifier</code> property, don't specify this property. The value is inherited from the source DB cluster, the snapshot, or the primary DB cluster for the global database cluster, respectively.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="master_user_secret" /></td><td><code>object</code></td><td>The secret managed by RDS in AWS Secrets Manager for the master user password.<br />When you restore a DB cluster from a snapshot, Amazon RDS generates a new secret instead of reusing the secret specified in the <code>SecretArn</code> property. This ensures that the restored DB cluster is securely managed with a dedicated secret. To maintain consistent integration with your application, you might need to update resource configurations to reference the newly created secret.<br />For more information, see &#91;Password management with Secrets Manager&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and &#91;Password management with Secrets Manager&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*</td></tr>
<tr><td><CopyableCode code="monitoring_interval" /></td><td><code>integer</code></td><td>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify <code>0</code>.<br />If <code>MonitoringRoleArn</code> is specified, also set <code>MonitoringInterval</code> to a value other than <code>0</code>.<br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters<br />Valid Values: <code>0 | 1 | 5 | 10 | 15 | 30 | 60</code> <br />Default: <code>0</code></td></tr>
<tr><td><CopyableCode code="monitoring_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs. An example is <code>arn:aws:iam:123456789012:role/emaccess</code>. For information on creating a monitoring role, see &#91;Setting up and enabling Enhanced Monitoring&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling) in the *Amazon RDS User Guide*.<br />If <code>MonitoringInterval</code> is set to a value other than <code>0</code>, supply a <code>MonitoringRoleArn</code> value.<br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="network_type" /></td><td><code>string</code></td><td>The network type of the DB cluster.<br />Valid values:<br />+ <code>IPV4</code> <br />+ <code>DUAL</code> <br /><br />The network type is determined by the <code>DBSubnetGroup</code> specified for the DB cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and IPv6 protocols (<code>DUAL</code>).<br />For more information, see &#91;Working with a DB instance in a VPC&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon Aurora User Guide.* <br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="performance_insights_enabled" /></td><td><code>boolean</code></td><td>Specifies whether to turn on Performance Insights for the DB cluster.<br />For more information, see &#91;Using Amazon Performance Insights&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide*.<br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="performance_insights_kms_key_id" /></td><td><code>string</code></td><td>The AWS KMS key identifier for encryption of Performance Insights data.<br />The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.<br />If you don't specify a value for <code>PerformanceInsightsKMSKeyId</code>, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS-account. Your AWS-account has a different default KMS key for each AWS-Region.<br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="performance_insights_retention_period" /></td><td><code>integer</code></td><td>The number of days to retain Performance Insights data.<br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters<br />Valid Values:<br />+ <code>7</code> <br />+ *month* * 31, where *month* is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)<br />+ <code>731</code> <br /><br />Default: <code>7</code> days<br />If you specify a retention period that isn't valid, such as <code>94</code>, Amazon RDS issues an error.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port number on which the DB instances in the DB cluster accept connections.<br />Default:<br />+ When <code>EngineMode</code> is <code>provisioned</code>, <code>3306</code> (for both Aurora MySQL and Aurora PostgreSQL)<br />+ When <code>EngineMode</code> is <code>serverless</code>:<br />+ <code>3306</code> when <code>Engine</code> is <code>aurora</code> or <code>aurora-mysql</code> <br />+ <code>5432</code> when <code>Engine</code> is <code>aurora-postgresql</code> <br /><br /><br />The <code>No interruption</code> on update behavior only applies to DB clusters. If you are updating a DB instance, see &#91;Port&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-port) for the AWS::RDS::DBInstance resource.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="preferred_backup_window" /></td><td><code>string</code></td><td>The daily time range during which automated backups are created. For more information, see &#91;Backup Window&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.Backups.BackupWindow) in the *Amazon Aurora User Guide.* <br />Constraints:<br />+ Must be in the format <code>hh24:mi-hh24:mi</code>.<br />+ Must be in Universal Coordinated Time (UTC).<br />+ Must not conflict with the preferred maintenance window.<br />+ Must be at least 30 minutes.<br /><br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).<br />Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> <br />The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see &#91;Adjusting the Preferred DB Cluster Maintenance Window&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow.Aurora) in the *Amazon Aurora User Guide.* <br />Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.<br />Constraints: Minimum 30-minute window.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>Specifies whether the DB cluster is publicly accessible.<br />When the DB cluster is publicly accessible and you connect from outside of the DB cluster's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB cluster, the endpoint resolves to the private IP address. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.<br />When the DB cluster isn't publicly accessible, it is an internal DB cluster with a DNS name that resolves to a private IP address.<br />Valid for Cluster Type: Multi-AZ DB clusters only<br />Default: The default behavior varies depending on whether <code>DBSubnetGroupName</code> is specified.<br />If <code>DBSubnetGroupName</code> isn't specified, and <code>PubliclyAccessible</code> isn't specified, the following applies:<br />+ If the default VPC in the target Region doesn’t have an internet gateway attached to it, the DB cluster is private.<br />+ If the default VPC in the target Region has an internet gateway attached to it, the DB cluster is public.<br /><br />If <code>DBSubnetGroupName</code> is specified, and <code>PubliclyAccessible</code> isn't specified, the following applies:<br />+ If the subnets are part of a VPC that doesn’t have an internet gateway attached to it, the DB cluster is private.<br />+ If the subnets are part of a VPC that has an internet gateway attached to it, the DB cluster is public.</td></tr>
<tr><td><CopyableCode code="replication_source_identifier" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a read replica.<br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="restore_to_time" /></td><td><code>string</code></td><td>The date and time to restore the DB cluster to.<br />Valid Values: Value must be a time in Universal Coordinated Time (UTC) format<br />Constraints:<br />+ Must be before the latest restorable time for the DB instance<br />+ Must be specified if <code>UseLatestRestorableTime</code> parameter isn't provided<br />+ Can't be specified if the <code>UseLatestRestorableTime</code> parameter is enabled<br />+ Can't be specified if the <code>RestoreType</code> parameter is <code>copy-on-write</code> <br /><br />This property must be used with <code>SourceDBClusterIdentifier</code> property. The resulting cluster will have the identifier that matches the value of the <code>DBclusterIdentifier</code> property.<br />Example: <code>2015-03-07T23:45:00Z</code> <br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="restore_type" /></td><td><code>string</code></td><td>The type of restore to be performed. You can specify one of the following values:<br />+ <code>full-copy</code> - The new DB cluster is restored as a full copy of the source DB cluster.<br />+ <code>copy-on-write</code> - The new DB cluster is restored as a clone of the source DB cluster.<br /><br />If you don't specify a <code>RestoreType</code> value, then the new DB cluster is restored as a full copy of the source DB cluster.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="serverless_v2_scaling_configuration" /></td><td><code>object</code></td><td>The scaling configuration of an Aurora Serverless V2 DB cluster. <br />This property is only supported for Aurora Serverless v2. For Aurora Serverless v1, Use the <code>ScalingConfiguration</code> property.<br />Valid for: Aurora Serverless v2 DB clusters only</td></tr>
<tr><td><CopyableCode code="scaling_configuration" /></td><td><code>object</code></td><td>The scaling configuration of an Aurora Serverless v1 DB cluster.<br />This property is only supported for Aurora Serverless v1. For Aurora Serverless v2, Use the <code>ServerlessV2ScalingConfiguration</code> property.<br />Valid for: Aurora Serverless v1 DB clusters only</td></tr>
<tr><td><CopyableCode code="snapshot_identifier" /></td><td><code>string</code></td><td>The identifier for the DB snapshot or DB cluster snapshot to restore from.<br />You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.<br />After you restore a DB cluster with a <code>SnapshotIdentifier</code> property, you must specify the same <code>SnapshotIdentifier</code> property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the <code>SnapshotIdentifier</code> property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, a new DB cluster is restored from the specified <code>SnapshotIdentifier</code> property, and the original DB cluster is deleted.<br />If you specify the <code>SnapshotIdentifier</code> property to restore a DB cluster (as opposed to specifying it for DB cluster updates), then don't specify the following properties:<br />+ <code>GlobalClusterIdentifier</code> <br />+ <code>MasterUsername</code> <br />+ <code>MasterUserPassword</code> <br />+ <code>ReplicationSourceIdentifier</code> <br />+ <code>RestoreType</code> <br />+ <code>SourceDBClusterIdentifier</code> <br />+ <code>SourceRegion</code> <br />+ <code>StorageEncrypted</code> (for an encrypted snapshot)<br />+ <code>UseLatestRestorableTime</code> <br /><br />Constraints:<br />+ Must match the identifier of an existing Snapshot.<br /><br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="source_db_cluster_identifier" /></td><td><code>string</code></td><td>When restoring a DB cluster to a point in time, the identifier of the source DB cluster from which to restore.<br />Constraints:<br />+ Must match the identifier of an existing DBCluster.<br /><br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="source_region" /></td><td><code>string</code></td><td>The AWS Region which contains the source DB cluster when replicating a DB cluster. For example, <code>us-east-1</code>. <br />Valid for: Aurora DB clusters only</td></tr>
<tr><td><CopyableCode code="storage_encrypted" /></td><td><code>boolean</code></td><td>Indicates whether the DB cluster is encrypted.<br />If you specify the <code>KmsKeyId</code> property, then you must enable encryption.<br />If you specify the <code>SourceDBClusterIdentifier</code> property, don't specify this property. The value is inherited from the source DB cluster, and if the DB cluster is encrypted, the specified <code>KmsKeyId</code> property is used.<br />If you specify the <code>SnapshotIdentifier</code> and the specified snapshot is encrypted, don't specify this property. The value is inherited from the snapshot, and the specified <code>KmsKeyId</code> property is used.<br />If you specify the <code>SnapshotIdentifier</code> and the specified snapshot isn't encrypted, you can use this property to specify that the restored DB cluster is encrypted. Specify the <code>KmsKeyId</code> property for the KMS key to use for encryption. If you don't want the restored DB cluster to be encrypted, then don't set this property or set it to <code>false</code>.<br />If you specify both the <code>StorageEncrypted</code> and <code>SnapshotIdentifier</code> properties without specifying the <code>KmsKeyId</code> property, then the restored DB cluster inherits the encryption settings from the DB snapshot that provide.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="storage_throughput" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="storage_type" /></td><td><code>string</code></td><td>The storage type to associate with the DB cluster.<br />For information on storage types for Aurora DB clusters, see &#91;Storage configurations for Amazon Aurora DB clusters&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html#aurora-storage-type). For information on storage types for Multi-AZ DB clusters, see &#91;Settings for creating Multi-AZ DB clusters&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html#create-multi-az-db-cluster-settings).<br />This setting is required to create a Multi-AZ DB cluster.<br />When specified for a Multi-AZ DB cluster, a value for the <code>Iops</code> parameter is required.<br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters<br />Valid Values:<br />+ Aurora DB clusters - <code>aurora | aurora-iopt1</code> <br />+ Multi-AZ DB clusters - <code>io1 | io2 | gp3</code> <br /><br />Default:<br />+ Aurora DB clusters - <code>aurora</code> <br />+ Multi-AZ DB clusters - <code>io1</code> <br /><br />When you create an Aurora DB cluster with the storage type set to <code>aurora-iopt1</code>, the storage type is returned in the response. The storage type isn't returned when you set it to <code>aurora</code>.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags to assign to the DB cluster.<br />Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="use_latest_restorable_time" /></td><td><code>boolean</code></td><td>A value that indicates whether to restore the DB cluster to the latest restorable backup time. By default, the DB cluster is not restored to the latest restorable backup time. <br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>A list of EC2 VPC security groups to associate with this DB cluster.<br />If you plan to update the resource, don't specify VPC security groups in a shared VPC.<br />Valid for: Aurora DB clusters and Multi-AZ DB clusters</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html"><code>AWS::RDS::DBCluster</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>db_clusters</code> in a region.
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
cluster_scalability_type,
copy_tags_to_snapshot,
database_insights_mode,
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
enable_local_write_forwarding,
engine,
engine_lifecycle_support,
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
FROM aws.rds.db_clusters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>db_cluster</code>.
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
cluster_scalability_type,
copy_tags_to_snapshot,
database_insights_mode,
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
enable_local_write_forwarding,
engine,
engine_lifecycle_support,
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
FROM aws.rds.db_clusters
WHERE region = 'us-east-1' AND data__Identifier = '<DBClusterIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>db_cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rds.db_clusters (
 ReadEndpoint,
 AllocatedStorage,
 AssociatedRoles,
 AvailabilityZones,
 AutoMinorVersionUpgrade,
 BacktrackWindow,
 BackupRetentionPeriod,
 ClusterScalabilityType,
 CopyTagsToSnapshot,
 DatabaseInsightsMode,
 DatabaseName,
 DBClusterInstanceClass,
 DBInstanceParameterGroupName,
 DBSystemId,
 GlobalClusterIdentifier,
 DBClusterIdentifier,
 DBClusterParameterGroupName,
 DBSubnetGroupName,
 DeletionProtection,
 Domain,
 DomainIAMRoleName,
 EnableCloudwatchLogsExports,
 EnableGlobalWriteForwarding,
 EnableHttpEndpoint,
 EnableIAMDatabaseAuthentication,
 EnableLocalWriteForwarding,
 Engine,
 EngineLifecycleSupport,
 EngineMode,
 EngineVersion,
 ManageMasterUserPassword,
 Iops,
 KmsKeyId,
 MasterUsername,
 MasterUserPassword,
 MasterUserSecret,
 MonitoringInterval,
 MonitoringRoleArn,
 NetworkType,
 PerformanceInsightsEnabled,
 PerformanceInsightsKmsKeyId,
 PerformanceInsightsRetentionPeriod,
 Port,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 PubliclyAccessible,
 ReplicationSourceIdentifier,
 RestoreToTime,
 RestoreType,
 ServerlessV2ScalingConfiguration,
 ScalingConfiguration,
 SnapshotIdentifier,
 SourceDBClusterIdentifier,
 SourceRegion,
 StorageEncrypted,
 StorageType,
 Tags,
 UseLatestRestorableTime,
 VpcSecurityGroupIds,
 region
)
SELECT 
'{{ ReadEndpoint }}',
 '{{ AllocatedStorage }}',
 '{{ AssociatedRoles }}',
 '{{ AvailabilityZones }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ BacktrackWindow }}',
 '{{ BackupRetentionPeriod }}',
 '{{ ClusterScalabilityType }}',
 '{{ CopyTagsToSnapshot }}',
 '{{ DatabaseInsightsMode }}',
 '{{ DatabaseName }}',
 '{{ DBClusterInstanceClass }}',
 '{{ DBInstanceParameterGroupName }}',
 '{{ DBSystemId }}',
 '{{ GlobalClusterIdentifier }}',
 '{{ DBClusterIdentifier }}',
 '{{ DBClusterParameterGroupName }}',
 '{{ DBSubnetGroupName }}',
 '{{ DeletionProtection }}',
 '{{ Domain }}',
 '{{ DomainIAMRoleName }}',
 '{{ EnableCloudwatchLogsExports }}',
 '{{ EnableGlobalWriteForwarding }}',
 '{{ EnableHttpEndpoint }}',
 '{{ EnableIAMDatabaseAuthentication }}',
 '{{ EnableLocalWriteForwarding }}',
 '{{ Engine }}',
 '{{ EngineLifecycleSupport }}',
 '{{ EngineMode }}',
 '{{ EngineVersion }}',
 '{{ ManageMasterUserPassword }}',
 '{{ Iops }}',
 '{{ KmsKeyId }}',
 '{{ MasterUsername }}',
 '{{ MasterUserPassword }}',
 '{{ MasterUserSecret }}',
 '{{ MonitoringInterval }}',
 '{{ MonitoringRoleArn }}',
 '{{ NetworkType }}',
 '{{ PerformanceInsightsEnabled }}',
 '{{ PerformanceInsightsKmsKeyId }}',
 '{{ PerformanceInsightsRetentionPeriod }}',
 '{{ Port }}',
 '{{ PreferredBackupWindow }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ PubliclyAccessible }}',
 '{{ ReplicationSourceIdentifier }}',
 '{{ RestoreToTime }}',
 '{{ RestoreType }}',
 '{{ ServerlessV2ScalingConfiguration }}',
 '{{ ScalingConfiguration }}',
 '{{ SnapshotIdentifier }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ SourceRegion }}',
 '{{ StorageEncrypted }}',
 '{{ StorageType }}',
 '{{ Tags }}',
 '{{ UseLatestRestorableTime }}',
 '{{ VpcSecurityGroupIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.db_clusters (
 ReadEndpoint,
 AllocatedStorage,
 AssociatedRoles,
 AvailabilityZones,
 AutoMinorVersionUpgrade,
 BacktrackWindow,
 BackupRetentionPeriod,
 ClusterScalabilityType,
 CopyTagsToSnapshot,
 DatabaseInsightsMode,
 DatabaseName,
 DBClusterInstanceClass,
 DBInstanceParameterGroupName,
 DBSystemId,
 GlobalClusterIdentifier,
 DBClusterIdentifier,
 DBClusterParameterGroupName,
 DBSubnetGroupName,
 DeletionProtection,
 Domain,
 DomainIAMRoleName,
 EnableCloudwatchLogsExports,
 EnableGlobalWriteForwarding,
 EnableHttpEndpoint,
 EnableIAMDatabaseAuthentication,
 EnableLocalWriteForwarding,
 Engine,
 EngineLifecycleSupport,
 EngineMode,
 EngineVersion,
 ManageMasterUserPassword,
 Iops,
 KmsKeyId,
 MasterUsername,
 MasterUserPassword,
 MasterUserSecret,
 MonitoringInterval,
 MonitoringRoleArn,
 NetworkType,
 PerformanceInsightsEnabled,
 PerformanceInsightsKmsKeyId,
 PerformanceInsightsRetentionPeriod,
 Port,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 PubliclyAccessible,
 ReplicationSourceIdentifier,
 RestoreToTime,
 RestoreType,
 ServerlessV2ScalingConfiguration,
 ScalingConfiguration,
 SnapshotIdentifier,
 SourceDBClusterIdentifier,
 SourceRegion,
 StorageEncrypted,
 StorageType,
 Tags,
 UseLatestRestorableTime,
 VpcSecurityGroupIds,
 region
)
SELECT 
 '{{ ReadEndpoint }}',
 '{{ AllocatedStorage }}',
 '{{ AssociatedRoles }}',
 '{{ AvailabilityZones }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ BacktrackWindow }}',
 '{{ BackupRetentionPeriod }}',
 '{{ ClusterScalabilityType }}',
 '{{ CopyTagsToSnapshot }}',
 '{{ DatabaseInsightsMode }}',
 '{{ DatabaseName }}',
 '{{ DBClusterInstanceClass }}',
 '{{ DBInstanceParameterGroupName }}',
 '{{ DBSystemId }}',
 '{{ GlobalClusterIdentifier }}',
 '{{ DBClusterIdentifier }}',
 '{{ DBClusterParameterGroupName }}',
 '{{ DBSubnetGroupName }}',
 '{{ DeletionProtection }}',
 '{{ Domain }}',
 '{{ DomainIAMRoleName }}',
 '{{ EnableCloudwatchLogsExports }}',
 '{{ EnableGlobalWriteForwarding }}',
 '{{ EnableHttpEndpoint }}',
 '{{ EnableIAMDatabaseAuthentication }}',
 '{{ EnableLocalWriteForwarding }}',
 '{{ Engine }}',
 '{{ EngineLifecycleSupport }}',
 '{{ EngineMode }}',
 '{{ EngineVersion }}',
 '{{ ManageMasterUserPassword }}',
 '{{ Iops }}',
 '{{ KmsKeyId }}',
 '{{ MasterUsername }}',
 '{{ MasterUserPassword }}',
 '{{ MasterUserSecret }}',
 '{{ MonitoringInterval }}',
 '{{ MonitoringRoleArn }}',
 '{{ NetworkType }}',
 '{{ PerformanceInsightsEnabled }}',
 '{{ PerformanceInsightsKmsKeyId }}',
 '{{ PerformanceInsightsRetentionPeriod }}',
 '{{ Port }}',
 '{{ PreferredBackupWindow }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ PubliclyAccessible }}',
 '{{ ReplicationSourceIdentifier }}',
 '{{ RestoreToTime }}',
 '{{ RestoreType }}',
 '{{ ServerlessV2ScalingConfiguration }}',
 '{{ ScalingConfiguration }}',
 '{{ SnapshotIdentifier }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ SourceRegion }}',
 '{{ StorageEncrypted }}',
 '{{ StorageType }}',
 '{{ Tags }}',
 '{{ UseLatestRestorableTime }}',
 '{{ VpcSecurityGroupIds }}',
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
  - name: db_cluster
    props:
      - name: ReadEndpoint
        value:
          Address: '{{ Address }}'
      - name: AllocatedStorage
        value: '{{ AllocatedStorage }}'
      - name: AssociatedRoles
        value:
          - FeatureName: '{{ FeatureName }}'
            RoleArn: '{{ RoleArn }}'
      - name: AvailabilityZones
        value:
          - '{{ AvailabilityZones[0] }}'
      - name: AutoMinorVersionUpgrade
        value: '{{ AutoMinorVersionUpgrade }}'
      - name: BacktrackWindow
        value: '{{ BacktrackWindow }}'
      - name: BackupRetentionPeriod
        value: '{{ BackupRetentionPeriod }}'
      - name: ClusterScalabilityType
        value: '{{ ClusterScalabilityType }}'
      - name: CopyTagsToSnapshot
        value: '{{ CopyTagsToSnapshot }}'
      - name: DatabaseInsightsMode
        value: '{{ DatabaseInsightsMode }}'
      - name: DatabaseName
        value: '{{ DatabaseName }}'
      - name: DBClusterInstanceClass
        value: '{{ DBClusterInstanceClass }}'
      - name: DBInstanceParameterGroupName
        value: '{{ DBInstanceParameterGroupName }}'
      - name: DBSystemId
        value: '{{ DBSystemId }}'
      - name: GlobalClusterIdentifier
        value: '{{ GlobalClusterIdentifier }}'
      - name: DBClusterIdentifier
        value: '{{ DBClusterIdentifier }}'
      - name: DBClusterParameterGroupName
        value: '{{ DBClusterParameterGroupName }}'
      - name: DBSubnetGroupName
        value: '{{ DBSubnetGroupName }}'
      - name: DeletionProtection
        value: '{{ DeletionProtection }}'
      - name: Domain
        value: '{{ Domain }}'
      - name: DomainIAMRoleName
        value: '{{ DomainIAMRoleName }}'
      - name: EnableCloudwatchLogsExports
        value:
          - '{{ EnableCloudwatchLogsExports[0] }}'
      - name: EnableGlobalWriteForwarding
        value: '{{ EnableGlobalWriteForwarding }}'
      - name: EnableHttpEndpoint
        value: '{{ EnableHttpEndpoint }}'
      - name: EnableIAMDatabaseAuthentication
        value: '{{ EnableIAMDatabaseAuthentication }}'
      - name: EnableLocalWriteForwarding
        value: '{{ EnableLocalWriteForwarding }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: EngineLifecycleSupport
        value: '{{ EngineLifecycleSupport }}'
      - name: EngineMode
        value: '{{ EngineMode }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: ManageMasterUserPassword
        value: '{{ ManageMasterUserPassword }}'
      - name: Iops
        value: '{{ Iops }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: MasterUsername
        value: '{{ MasterUsername }}'
      - name: MasterUserPassword
        value: '{{ MasterUserPassword }}'
      - name: MasterUserSecret
        value:
          SecretArn: '{{ SecretArn }}'
          KmsKeyId: '{{ KmsKeyId }}'
      - name: MonitoringInterval
        value: '{{ MonitoringInterval }}'
      - name: MonitoringRoleArn
        value: '{{ MonitoringRoleArn }}'
      - name: NetworkType
        value: '{{ NetworkType }}'
      - name: PerformanceInsightsEnabled
        value: '{{ PerformanceInsightsEnabled }}'
      - name: PerformanceInsightsKmsKeyId
        value: '{{ PerformanceInsightsKmsKeyId }}'
      - name: PerformanceInsightsRetentionPeriod
        value: '{{ PerformanceInsightsRetentionPeriod }}'
      - name: Port
        value: '{{ Port }}'
      - name: PreferredBackupWindow
        value: '{{ PreferredBackupWindow }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: ReplicationSourceIdentifier
        value: '{{ ReplicationSourceIdentifier }}'
      - name: RestoreToTime
        value: '{{ RestoreToTime }}'
      - name: RestoreType
        value: '{{ RestoreType }}'
      - name: ServerlessV2ScalingConfiguration
        value:
          MinCapacity: null
          MaxCapacity: null
          SecondsUntilAutoPause: '{{ SecondsUntilAutoPause }}'
      - name: ScalingConfiguration
        value:
          AutoPause: '{{ AutoPause }}'
          MaxCapacity: '{{ MaxCapacity }}'
          MinCapacity: '{{ MinCapacity }}'
          SecondsBeforeTimeout: '{{ SecondsBeforeTimeout }}'
          SecondsUntilAutoPause: '{{ SecondsUntilAutoPause }}'
          TimeoutAction: '{{ TimeoutAction }}'
      - name: SnapshotIdentifier
        value: '{{ SnapshotIdentifier }}'
      - name: SourceDBClusterIdentifier
        value: '{{ SourceDBClusterIdentifier }}'
      - name: SourceRegion
        value: '{{ SourceRegion }}'
      - name: StorageEncrypted
        value: '{{ StorageEncrypted }}'
      - name: StorageType
        value: '{{ StorageType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: UseLatestRestorableTime
        value: '{{ UseLatestRestorableTime }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.rds.db_clusters
WHERE data__Identifier = '<DBClusterIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_clusters</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
iam:PassRole,
rds:AddRoleToDBCluster,
rds:AddTagsToResource,
rds:CreateDBCluster,
rds:CreateDBInstance,
rds:DescribeDBClusters,
rds:DescribeDBClusterSnapshots,
rds:DescribeDBSnapshots,
rds:DescribeEvents,
rds:EnableHttpEndpoint,
rds:ModifyDBCluster,
rds:RestoreDBClusterFromSnapshot,
rds:RestoreDBClusterToPointInTime,
secretsmanager:CreateSecret,
secretsmanager:TagResource
```

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
rds:AddTagsToResource,
rds:CreateDBClusterSnapshot,
rds:DeleteDBCluster,
rds:DeleteDBInstance,
rds:DescribeDBClusters,
rds:DescribeGlobalClusters,
rds:RemoveFromGlobalCluster
```

### List
```json
rds:DescribeDBClusters
```
